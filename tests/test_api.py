from unittest.mock import patch
from datetime import datetime, timedelta, timezone
from io import BytesIO

from openpyxl import Workbook
from fastapi.testclient import TestClient

from app.main import app
from app.core.pipeline import SecurityPipeline
from app.utils.store import REPORTS_FILE, prune_records
from app.utils.file_ingest import parse_file_to_raw_event


client = TestClient(app)

# Regression coverage for the security-log-analysis mainline.
# Repo hygiene marker: the retired experimental module has been removed from this codebase.


def make_xlsx_bytes(headers: list[str], rows: list[list[object]]) -> bytes:
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(headers)
    for row in rows:
        sheet.append(row)
    buffer = BytesIO()
    workbook.save(buffer)
    return buffer.getvalue()


def make_csv_bytes(headers: list[str], rows: list[list[object]]) -> bytes:
    lines = [",".join(headers)]
    for row in rows:
        lines.append(",".join(str(item) for item in row))
    return ("\n".join(lines) + "\n").encode("utf-8")


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_easm_chinese_csvs_route_to_expected_single_event_types() -> None:
    service_bytes = make_csv_bytes(
        ["工件名称", "工件类型", "端口", "协议", "相关域名", "相关 IP"],
        [["104.18.9.172_https_443_cloudflare", "服务", "443", "https", "token-api.megaeth.com", "104.18.9.172"]],
    )
    cert_bytes = make_csv_bytes(
        ["工件名称", "工件类型", "证书ID", "颁发者名称", "证书过期状态", "相关域名"],
        [["CloudFlare Origin Certificate", "证书", "id-1", "CloudFlare, Inc.", "无需采取任何操作", "token-api.megaeth.com"]],
    )
    dns_bytes = make_csv_bytes(
        ["工件名称", "工件类型", "DNS记录类型", "域名服务器", "相关域名"],
        [["megaeth.com_jake.ns.cloudflare.com", "DNS记录", "SOA", "jake.ns.cloudflare.com", "megaeth.com"]],
    )
    ip_bytes = make_csv_bytes(
        ["工件名称", "工件类型", "相关 IP"],
        [["104.18.0.0/20", "IP地址段", "104.18.9.172"]],
    )

    service_raw = parse_file_to_raw_event("EASM_service.csv", service_bytes)
    cert_raw = parse_file_to_raw_event("EASM_cert.csv", cert_bytes)
    dns_raw = parse_file_to_raw_event("EASM_dns.csv", dns_bytes)
    ip_raw = parse_file_to_raw_event("EASM_ip.csv", ip_bytes)

    assert service_raw.source_type == "easm" and service_raw.event_hint == "service_exposure"
    assert cert_raw.source_type == "easm" and cert_raw.event_hint == "tls_analysis"
    assert dns_raw.source_type == "easm" and dns_raw.event_hint == "external_asset"
    assert ip_raw.source_type == "easm" and ip_raw.event_hint == "external_asset"


def test_easm_multi_file_batch_generates_composite_asset_assessment() -> None:
    service_bytes = make_csv_bytes(
        ["asset", "ip", "port", "protocol", "provider"],
        [
            ["token-api.megaeth.com", "104.16.0.10", "80", "http", "CloudFlare Inc"],
            ["token-api.megaeth.com", "34.120.1.10", "443", "https", "Google LLC"],
            ["mainnet-dashboard.megaeth.com", "104.16.0.11", "443", "https", "CloudFlare Inc"],
            ["mainnet-dashboard.megaeth.com", "34.120.1.11", "443", "https", "Google LLC"],
            ["l1rpc.megaeth.com", "216.245.192.5", "80", "http", "Limestone Networks Inc."],
            ["l1rpc.megaeth.com", "216.245.192.5", "443", "https", "Limestone Networks Inc."],
        ],
    )
    dns_bytes = make_csv_bytes(
        ["domain", "record_type", "value", "provider"],
        [
            ["verify.megaeth.com", "NS", "ns1.vercel-dns-3.com", "Amazon.com Inc."],
        ],
    )
    cert_bytes = make_csv_bytes(
        ["common_name", "issuer", "status"],
        [
            ["token-api.megaeth.com", "Cloudflare Origin Certificate", "active"],
            ["verify.megaeth.com", "Let's Encrypt", "active"],
            ["github.megaeth.com", "Unknown", "expired"],
            ["perftest.megaeth.com", "Unknown", "expired"],
        ],
    )

    response = client.post(
        "/ingest/files",
        files=[
            ("files", ("services.csv", service_bytes, "text/csv")),
            ("files", ("dns_records.csv", dns_bytes, "text/csv")),
            ("files", ("certificates.csv", cert_bytes, "text/csv")),
        ],
    )
    body = response.json()
    assert response.status_code == 200
    assert body["composite_generated"] is True
    composite = next(item for item in body["results"] if item["normalized_event"]["event_type"] == "easm_asset_assessment")
    assert composite["planner_preview"]["skills_to_execute"] == [
        "megaeth.easm.asset_discovery",
        "megaeth.easm.service_scan",
        "megaeth.easm.tls_analysis",
        "megaeth.easm.vulnerability_scan",
        "megaeth.easm.external_intelligence",
    ]
    assert composite["report"]["report_title"] == "EASM 外部攻击面综合评估报告"
    assert composite["report"]["report_template"] == "easm_asset_assessment_v1"
    assessments = composite["normalized_event"]["normalized_data"]["asset_assessments"]
    indexed = {item["asset"]: item for item in assessments}
    assert indexed["token-api.megaeth.com"]["scores"]["severity"] == "High"
    assert "cdn_and_direct_origin_coexist" in indexed["token-api.megaeth.com"]["tags"]
    assert "potential_origin_exposure" in indexed["token-api.megaeth.com"]["tags"]
    assert indexed["verify.megaeth.com"]["scores"]["severity"] == "Medium"
    assert "third_party_dns_delegation" in indexed["verify.megaeth.com"]["tags"]
    assert indexed["github.megaeth.com"]["scores"]["severity"] == "Low"
    assert "historical_asset_hint" in indexed["github.megaeth.com"]["tags"]




def test_bitdefender_network_endpoint_without_managed_details_still_returns_inventory() -> None:
    fake_inventory = {"total": 2, "items": [{"id": "g-1", "name": "Custom Groups", "type": 4}]}
    fake_endpoints = {"total": 0, "items": []}
    fake_recursive = {"total": 22, "managed_total": 0, "unmanaged_total": 22, "groups_traversed": 5, "items": [{"id": "e-1", "name": "host-1"}]}
    fake_hierarchy = {"total": 44, "managed_total": 0, "unmanaged_total": 44, "groups_traversed": 8, "companies_traversed": 0, "items": [{"id": "e-1", "name": "host-1"}]}
    with patch("app.api.integration_routes.BitdefenderClient.get_network_inventory", return_value=fake_inventory), patch(
        "app.api.integration_routes.BitdefenderClient.get_endpoints", return_value=fake_endpoints
    ), patch("app.api.integration_routes.BitdefenderClient.discover_company_id", return_value="company-1"), patch(
        "app.api.integration_routes.BitdefenderClient.discover_inventory_endpoints", return_value=fake_recursive
    ), patch(
        "app.api.integration_routes.BitdefenderClient.discover_inventory_hierarchy", return_value=fake_hierarchy
    ), patch(
        "app.api.integration_routes.BitdefenderClient.get_all_companies", side_effect=ValueError("forbidden")
    ), patch(
        "app.api.integration_routes.BitdefenderClient.get_all_custom_groups", return_value={"total": 0, "items": []}
    ):
        body = client.post("/integrations/bitdefender/network", json={"api_key": "demo"}).json()
    assert body["inventory_endpoints"]["total"] == 22
    assert body["inventory_hierarchy"]["total"] == 44


def test_bitdefender_collects_all_inventory_pages_for_group_children() -> None:
    from app.integrations.bitdefender import BitdefenderClient

    client_obj = BitdefenderClient(api_key="demo")
    page1 = {"total": 3, "pagesCount": 2, "items": [{"id": "a"}, {"id": "b"}]}
    page2 = {"total": 3, "pagesCount": 2, "items": [{"id": "c"}]}
    with patch.object(BitdefenderClient, "get_network_inventory_children", side_effect=[page1, page2]):
        body = client_obj.get_all_network_inventory_children("group-1", per_page=100)
    assert len(body["items"]) == 3


def test_bitdefender_network_import_uses_recursive_inventory_devices() -> None:
    fake_hierarchy = {
        "total": 22,
        "managed_total": 18,
        "unmanaged_total": 4,
        "groups_traversed": 5,
        "companies_traversed": 1,
        "items": [{"id": "e-1", "name": "host-1", "details": {"fqdn": "host-1.local", "isManaged": True}}],
    }
    with patch("app.api.integration_routes.BitdefenderClient.discover_company_id", return_value="company-1"), patch(
        "app.api.integration_routes.BitdefenderClient.discover_inventory_hierarchy", return_value=fake_hierarchy
    ):
        body = client.post("/integrations/bitdefender/network/import", json={"api_key": "demo"}).json()
    assert body["raw_event"]["event_hint"] == "endpoint_inventory"
    assert body["normalized_event"]["event_type"] == "endpoint_inventory"
    assert body["raw_event"]["payload"]["row_count"] == 1


def test_bitdefender_reports_import_runs_pipeline() -> None:
    fake_reports = {
        "total": 1,
        "items": [{"id": "r-1", "name": "安全审计报表", "type": 17, "occurrence": 4}],
    }
    with patch("app.api.integration_routes.BitdefenderClient.get_reports", return_value=fake_reports):
        body = client.post("/integrations/bitdefender/reports/import", json={"api_key": "demo"}).json()
    assert body["raw_event"]["source_type"] == "bitdefender"
    assert body["report"]["event_type"] == "integration_catalog"
    assert body["report"]["verdict"] == "informational_platform_observation"


def test_bitdefender_report_download_links_endpoint() -> None:
    fake_reports = {
        "total": 1,
        "items": [{"id": "r-1", "name": "安全审计报表", "type": 17, "occurrence": 4}],
    }
    fake_links = {
        "lastInstanceDownloadLink": "https://example.com/latest.zip",
        "allInstancesDownloadLink": "https://example.com/all.zip",
    }
    fake_bundle_summary = {
        "row_count": 128,
        "unique_host_count": 28,
        "malware_count": 2,
        "attack_count": 5,
        "blocked_count": 2,
    }
    with patch("app.api.integration_routes.BitdefenderClient.get_reports", return_value=fake_reports), patch(
        "app.api.integration_routes.BitdefenderClient.get_report_download_links", return_value=fake_links
    ), patch("app.api.integration_routes.BitdefenderClient.download_report_zip", return_value=b"demo"), patch(
        "app.api.integration_routes.parse_report_zip_bundle", return_value=fake_bundle_summary
    ):
        body = client.post("/integrations/bitdefender/reports/download-links", json={"api_key": "demo"}).json()
    assert body["report"]["id"] == "r-1"
    assert body["download_links"]["lastInstanceDownloadLink"] == "https://example.com/latest.zip"
    assert body["latest_report_summary"]["unique_host_count"] == 28


def test_bitdefender_latest_report_import_runs_pipeline() -> None:
    fake_reports = {
        "total": 1,
        "items": [{"id": "r-1", "name": "安全审计报表", "type": 17, "occurrence": 4}],
    }
    fake_links = {"lastInstanceUrl": "https://example.com/latest.zip"}
    fake_bundle = b"PK-demo"
    fake_parsed = {
        "csv_name": "audit.csv",
        "pdf_name": "audit.pdf",
        "row_count": 2,
        "headers": ["端点名称", "事件类型"],
        "rows": [{"端点名称": "host-1", "事件类型": "恶意软件检测"}],
        "content": "恶意软件检测 host-1",
    }
    with patch("app.api.integration_routes.BitdefenderClient.get_reports", return_value=fake_reports), patch(
        "app.api.integration_routes.BitdefenderClient.get_report_download_links", return_value=fake_links
    ), patch("app.api.integration_routes.BitdefenderClient.download_report_zip", return_value=fake_bundle), patch(
        "app.api.integration_routes.parse_report_zip_bundle", return_value=fake_parsed
    ):
        body = client.post("/integrations/bitdefender/reports/latest/import", json={"api_key": "demo"}).json()
    assert body["raw_event"]["source_type"] == "endpoint"
    assert body["normalized_event"]["event_type"] == "endpoint_process"
    assert body["planner_preview"]["skills_to_execute"] == ["megaeth.endpoint.process_anomaly"]
    assert body["report"]["event_type"] == "endpoint_process"
    assert "megaeth.endpoint.process_anomaly" in body["report"]["skills_selected"]


def test_whitebox_test_endpoint() -> None:
    fake_result = {
        "configured": True,
        "engine_mode": "command",
        "repo_path": "/tmp/demo-app",
        "repo_exists": True,
        "target_url": "https://demo.test",
        "capabilities": [
            "whitebox_recon",
            "whitebox_exploit_validation",
            "whitebox_report_synthesis",
        ],
        "status": "ready",
        "message": "MegaETH whitebox engine is ready for orchestration.",
    }
    with patch("app.api.integration_routes.MegaETHWhiteboxClient.test_connection", return_value=fake_result):
        body = client.post(
            "/integrations/whitebox/test",
            json={"repo_path": "/tmp/demo-app", "target_url": "https://demo.test"},
        ).json()
    assert body["configured"] is True
    assert "whitebox_recon" in body["capabilities"]


def test_whitebox_report_import_runs_pipeline() -> None:
    fake_report = {
        "scan_scope": {
            "repo_path": "/tmp/demo-app",
            "repo_name": "demo-app",
            "target_url": "https://demo.test",
            "config_path": None,
            "mode": "standard",
        },
        "executive_summary": "白盒安全测试显示该应用存在需要进一步治理的入口暴露与权限边界风险。",
        "validated_findings": [
            {
                "category": "authorization_bypass",
                "severity": "high",
                "summary": "管理接口存在权限边界薄弱路径。",
                "proof_status": "validated",
            }
        ],
        "priority_actions": ["复核关键管理接口的鉴权覆盖。"],
    }
    with patch("app.api.integration_routes.MegaETHWhiteboxClient.synthesize_report", return_value=fake_report):
        body = client.post(
            "/integrations/whitebox/report/import",
            json={"repo_path": "/tmp/demo-app", "target_url": "https://demo.test"},
        ).json()
    assert body["raw_event"]["source_type"] == "appsec"
    assert body["normalized_event"]["event_type"] == "whitebox_security_report"
    assert body["planner_preview"]["skills_to_execute"] == ["megaeth.appsec.whitebox_report_synthesis"]
    assert "megaeth.appsec.whitebox_report_synthesis" in body["report"]["skills_selected"]
    assert body["report"]["findings"]


def test_whitebox_recon_import_uses_appsec_report_language() -> None:
    fake_recon = {
        "scan_scope": {
            "repo_path": "/tmp/demo-app",
            "repo_name": "demo-app",
            "target_url": "https://demo.test",
            "mode": "standard",
        },
        "attack_surfaces": [{"surface": "web_routes", "count": 14}],
        "exposed_patterns": ["鉴权中间件覆盖不均衡"],
        "candidate_paths": ["/api/v1/admin"],
    }
    with patch("app.api.integration_routes.MegaETHWhiteboxClient.collect_recon", return_value=fake_recon):
        body = client.post(
            "/integrations/whitebox/recon/import",
            json={"repo_path": "/tmp/demo-app", "target_url": "https://demo.test"},
        ).json()
    assert body["normalized_event"]["event_type"] == "whitebox_recon_assessment"
    assert body["planner_preview"]["skills_to_execute"] == ["megaeth.appsec.whitebox_recon"]
    assert body["report"]["verdict"] == "whitebox_recon_review"
    assert "白盒侦察" in body["report"]["assessment"]


def test_whitebox_validate_import_uses_validation_report_language() -> None:
    fake_validation = {
        "scan_scope": {
            "repo_path": "/tmp/demo-app",
            "repo_name": "demo-app",
            "target_url": "https://demo.test",
            "mode": "standard",
        },
        "validated_findings": [
            {
                "category": "authorization_bypass",
                "severity": "high",
                "summary": "管理接口存在权限边界薄弱路径。",
                "proof_status": "validated",
            },
            {
                "category": "input_handling",
                "severity": "medium",
                "summary": "输入边界需要继续复核。",
                "proof_status": "candidate",
            },
        ],
        "proof_counts": {"validated": 1, "candidate": 1},
    }
    with patch("app.api.integration_routes.MegaETHWhiteboxClient.collect_validation", return_value=fake_validation):
        body = client.post(
            "/integrations/whitebox/validate/import",
            json={"repo_path": "/tmp/demo-app", "target_url": "https://demo.test"},
        ).json()
    assert body["normalized_event"]["event_type"] == "whitebox_exploit_validation"
    assert body["planner_preview"]["skills_to_execute"] == ["megaeth.appsec.whitebox_exploit_validation"]
    assert body["report"]["verdict"] == "whitebox_validation_review"
    assert "白盒安全验证" in body["report"]["assessment"]


def test_endpoint_skill_extracts_multiple_bitdefender_patterns() -> None:
    payload = {
        "event_id": "evt-test",
        "event_type": "endpoint_process",
        "source_type": "endpoint",
        "timestamp": "2026-03-14T10:00:00Z",
        "asset_context": {"asset_name": "安全审计报表", "criticality": 4},
        "normalized_data": {
            "rows": [
                {"端点名称": "host-1", "模块": "反恶意软件", "事件类型": "恶意软件检测", "详情": "恶意软件名称:Generic.SH.Amos"},
                {"端点名称": "host-2", "模块": "网络攻击防护", "事件类型": "网络攻击", "详情": "Attack.LocalFileInclusion.132"},
                {"端点名称": "host-3", "模块": "反钓鱼", "事件类型": "阻止的网站", "详情": "网站：https://example.bad"},
            ]
        },
    }
    body = client.post("/event", json=payload).json()
    assert len(body["findings"]) >= 3


def test_store_prunes_history_older_than_two_days() -> None:
    fresh = {
        "event_id": "evt-fresh",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    stale = {
        "event_id": "evt-stale",
        "generated_at": (datetime.now(timezone.utc) - timedelta(days=3)).isoformat(),
    }
    pruned = prune_records(REPORTS_FILE, [fresh, stale])
    assert [item["event_id"] for item in pruned] == ["evt-fresh"]
