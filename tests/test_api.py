from unittest.mock import patch
from datetime import datetime, timedelta, timezone
from io import BytesIO

from openpyxl import Workbook
from fastapi.testclient import TestClient

from app.main import app
from app.core.pipeline import SecurityPipeline
from app.utils.store import REPORTS_FILE, prune_records


client = TestClient(app)


def make_xlsx_bytes(headers: list[str], rows: list[list[object]]) -> bytes:
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(headers)
    for row in rows:
        sheet.append(row)
    buffer = BytesIO()
    workbook.save(buffer)
    return buffer.getvalue()


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}


def test_appa_overview_exposes_independent_pentest_product() -> None:
    body = client.get("/appa/overview").json()
    assert body["product_key"] == "appa"
    assert body["product_name"]["zh"] == "APPA 渗透测试工作台"
    assert len(body["modes"]) == 3
    assert any(item["skill_id"] == "recon-surface" for item in body["skill_packs"])
    assert any(item["key"] == "full_audit" for item in body["report_types"])


def test_skills_expose_execution_modes() -> None:
    body = client.get("/skills").json()
    jumpserver = next(item for item in body if item["skill_id"] == "megaeth.identity.jumpserver_multi_source_review")
    host_baseline = next(item for item in body if item["skill_id"] == "megaeth.host.baseline_compliance_analysis")
    assert jumpserver["execution_mode"] == "agent_optional"
    assert host_baseline["execution_mode"] == "rule_only"
    assert jumpserver["agent_trigger_conditions"]
    assert jumpserver["rule_fallback_conditions"]
    assert jumpserver["max_context_policy"] == "summary_plus_samples"
    assert host_baseline["agent_trigger_conditions"] == []
    assert host_baseline["rule_fallback_conditions"] == []


def test_risk_analytics_csv_maps_to_host_pipeline() -> None:
    files = [
        (
            "files",
            (
                "megalabs_2026-03-13_riskanalytics.csv",
                (
                    "发现名称,风险评分,平台,合规标准\n"
                    "/var/log/audit 目录未单独分区,100,Unix,CIS v8.0\n"
                    "/var/tmp 目录未单独分区,100,Unix,CIS v8.0\n"
                    "未安装 auditd,99,Unix,PCI DSS v4.0.1\n"
                    "挂载 cramfs 文件系统已启用,100,Unix,CIS v8.0\n"
                ).encode("utf-8"),
                "text/csv",
            ),
        ),
    ]
    body = client.post("/ingest/files", files=files).json()
    item = body["results"][0]
    assert item["normalized_event"]["source_type"] == "host_risk_analytics"
    assert item["normalized_event"]["event_type"] == "host_baseline_assessment"
    assert item["report"]["skills_selected"][0] == "megaeth.host.baseline_compliance_analysis"
    assert item["report"]["findings"]
    assert item["report"]["top_risk_label"] == "medium"
    assert "安全基线" in item["report"]["assessment"] or "配置风险" in item["report"]["assessment"]
    assert "中风险" in item["report"]["professional_judgment"]
    assert "文件系统隔离" in item["report"]["summary"]
    finding_types = {finding["risk_type"] for finding in item["report"]["findings"]}
    assert {
        "filesystem_isolation_issue",
        "log_permission_configuration",
    }.issubset(finding_types)


def test_memory_learning_reclassifies_upload() -> None:
    payload = {
        "raw_event": {
            "source_type": "github",
            "asset_context": {
                "asset_id": "baseline",
                "asset_name": "baseline",
                "source_file": "riskanalytics-memory.csv",
            },
            "payload": {
                "headers": ["发现名称", "风险评分", "平台", "合规标准"],
                "rows": [{"发现名称": "未安装 auditd", "风险评分": "99", "平台": "Unix"}],
                "parser_profile": "csv-tabular",
            },
        },
        "expected_source_type": "host",
        "expected_event_type": "host_integrity",
        "preferred_skills": ["megaeth.host.integrity_monitor", "megaeth.host.systemd_service_risk"],
        "name": "Risk analytics memory",
    }
    assert client.post("/memory/learn/classification", json=payload).status_code == 200

    files = [
        (
            "files",
            (
                "riskanalytics-memory.csv",
                (
                    "发现名称,风险评分,平台,合规标准\n"
                    "SSH 访问未受限制,100,Unix,CIS v8.0\n"
                    "未安装 auditd,99,Unix,PCI DSS v4.0.1\n"
                ).encode("utf-8"),
                "text/csv",
            ),
        ),
    ]
    body = client.post("/ingest/files", files=files).json()
    item = body["results"][0]
    assert item["normalized_event"]["normalized_data"]["_memory_context"]["expected_source_type"] == "host_risk_analytics"
    assert item["normalized_event"]["normalized_data"]["_memory_context"]["expected_event_type"] == "host_baseline_assessment"
    assert item["normalized_event"]["source_type"] == "host_risk_analytics"
    assert item["normalized_event"]["event_type"] == "host_baseline_assessment"


def test_memory_rules_deduplicate_similar_manual_entries() -> None:
    payload = {
        "raw_event": {
            "source_type": "github",
            "asset_context": {
                "asset_id": "baseline",
                "asset_name": "baseline",
                "source_file": "dedupe-risk.csv",
            },
            "payload": {
                "headers": ["发现名称", "风险评分", "平台", "合规标准"],
                "rows": [{"发现名称": "未安装 auditd", "风险评分": "99", "平台": "Unix"}],
                "parser_profile": "csv-tabular",
            },
        },
        "expected_source_type": "host",
        "expected_event_type": "host_integrity",
        "preferred_skills": ["megaeth.host.integrity_monitor"],
    }
    assert client.post("/memory/learn/classification", json=payload).status_code == 200
    assert client.post("/memory/learn/classification", json=payload).status_code == 200
    rules = [item for item in client.get("/memory/rules").json() if item["expected_event_type"] == "host_integrity"]
    dedupe_rules = [item for item in rules if "dedupe-risk.csv" in item.get("filename_tokens", [])]
    assert len(dedupe_rules) == 1


def test_pdf_endpoint_material_maps_to_endpoint() -> None:
    files = [("files", ("incident.pdf", b"%PDF-1.7", "application/pdf"))]
    with patch("app.utils.file_ingest.extract_pdf_text", return_value="Attack.LocalFileInclusion.132 /.env endpoint shellspawned"):
        body = client.post("/ingest/files", files=files).json()
    assert body["results"][0]["normalized_event"]["source_type"] == "endpoint"


def test_jumpserver_xlsx_batch_creates_composite_audit_report() -> None:
    login_old_bytes = make_xlsx_bytes(
        ["用户名", "登录 IP", "状态", "原因描述", "认证方式", "登录日期"],
        [
            ["abel.chen", "10.30.0.4", "失败", "OTP 失效", "MFA", "2026-03-18 08:41:00"],
        ],
    )
    login_bytes = make_xlsx_bytes(
        ["用户名", "登录 IP", "状态", "原因描述", "认证方式", "登录日期"],
        [
            ["abel.chen", "10.30.0.4", "失败", "OTP 失效", "MFA", "2026-03-18 09:01:00"],
            ["wenze.yan", "10.30.0.4", "成功", "登录成功", "MFA", "2026-03-18 09:05:00"],
        ],
    )
    command_bytes = make_xlsx_bytes(
        ["用户", "资产", "命令", "会话", "账号", "风险等级", "时间戳", "远端地址"],
        [
            ["wenze.yan", "512f(192.168.0.206)", "sudo su", "sess-1", "root", "接受(0)", "2026-03-18 09:06:00", "10.30.0.4"],
            ["wenze.yan", "512f(192.168.0.206)", "mv /tmp/bft-rpc-client .", "sess-1", "root", "接受(0)", "2026-03-18 09:07:00", "10.30.0.4"],
            ["wenze.yan", "512f(192.168.0.206)", "chmod 0777 bft-rpc-client", "sess-1", "root", "接受(0)", "2026-03-18 09:07:10", "10.30.0.4"],
            ["wenze.yan", "512f(192.168.0.206)", "./bft-rpc-client get-leader", "sess-1", "root", "接受(0)", "2026-03-18 09:07:30", "10.30.0.4"],
            ["wenze.yan", "512f(192.168.0.206)", "curl -i http://152.32.135.103:8090", "sess-1", "root", "接受(0)", "2026-03-18 09:08:00", "10.30.0.4"],
        ],
    )
    transfer_bytes = make_xlsx_bytes(
        ["用户", "资产", "账号", "操作", "文件名", "开始日期", "成功", "可下载", "会话", "远端地址"],
        [
            ["wenze.yan", "512f(192.168.0.206)", "root", "上传", "/tmp/bft-rpc-client", "2026-03-18 09:05:30", "成功", "否", "ftp-1", "10.30.0.4"],
        ],
    )
    operate_bytes = make_xlsx_bytes(
        ["用户", "动作", "资源类型", "资源", "远端地址", "组织名称", "日期"],
        [
            ["admin", "导出审计日志", "审计任务", "weekly-audit", "10.20.0.8", "Default", "2026-03-18 09:00:00"],
            ["admin", "创建用户会话", "会话", "sess-1", "10.20.0.8", "Default", "2026-03-18 09:04:00"],
            ["admin", "更新资产授权", "资产", "512f(192.168.0.206)", "10.20.0.8", "Default", "2026-03-18 09:04:30"],
        ],
    )
    files = [
        ("files", ("userloginlog_2026-03-17_15-34-48.xlsx", login_old_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("userloginlog_1.xlsx", login_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("command.xlsx", command_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("ftplog.xlsx", transfer_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("operatelog_2026-03-17_16-15-48.xlsx", operate_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
    ]
    body = client.post("/ingest/files", files=files).json()
    composite = body["results"][0]
    assert composite["normalized_event"]["source_type"] == "jumpserver"
    assert composite["normalized_event"]["event_type"] == "jumpserver_multi_source_audit"
    assert composite["planner_preview"]["skills_to_execute"] == ["megaeth.identity.jumpserver_multi_source_review"]
    assert composite["report"]["skills_selected"] == ["megaeth.identity.jumpserver_multi_source_review"]
    assert composite["report"]["top_risk_label"] in {"high", "critical"}
    assert composite["report"]["verdict"] in {"high_risk_pending_review", "high_risk_operations"}
    assert any(finding["risk_type"] == "cross_source_high_risk_chain" for finding in composite["report"]["findings"])
    assert any(finding["risk_type"] == "control_plane_high_impact_actions" for finding in composite["report"]["findings"])
    assert composite["normalized_event"]["normalized_data"]["operation_summary"]["total_rows"] == 3
    assert composite["normalized_event"]["normalized_data"]["supplemental_sources"][0]["source_role"] == "supplemental_snapshot_only"
    assert "JumpServer" in composite["report"]["summary"]
    assert composite["report"]["report_template"] == "jumpserver_multisource_v2"
    assert composite["report"]["report_title"] == "JumpServer 综合审计报告"
    assert composite["report"]["structured_sections"][0]["title"] == "综合结论："
    assert any(section["title"] == "5. 重点高危操作账户与命令汇总" for section in composite["report"]["structured_sections"])
    assert body["investigation"]["archive"]["archive_format"] == "json.gz"
    assert body["investigation"]["archive"]["archive_size_bytes"] > 0


def test_jumpserver_single_source_files_do_not_reuse_composite_skill() -> None:
    command_bytes = make_xlsx_bytes(
        ["用户", "资产", "命令", "会话", "账号", "风险等级", "时间戳", "远端地址"],
        [["wenze.yan", "512f(192.168.0.206)", "sudo su", "sess-1", "root", "接受(0)", "2026-03-18 09:06:00", "10.30.0.4"]],
    )
    transfer_bytes = make_xlsx_bytes(
        ["用户", "资产", "账号", "操作", "文件名", "开始日期", "成功", "可下载", "会话", "远端地址"],
        [["wenze.yan", "512f(192.168.0.206)", "root", "上传", "/tmp/bft-rpc-client", "2026-03-18 09:05:30", "成功", "否", "ftp-1", "10.30.0.4"]],
    )
    operate_bytes = make_xlsx_bytes(
        ["用户", "动作", "资源类型", "资源", "远端地址", "组织名称", "日期"],
        [["admin", "导出审计日志", "审计任务", "weekly-audit", "10.20.0.8", "Default", "2026-03-18 09:00:00"]],
    )

    command_body = client.post(
        "/ingest/files",
        files=[("files", ("command.xlsx", command_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))],
    ).json()
    command_item = command_body["results"][0]
    assert command_item["normalized_event"]["event_type"] == "jumpserver_command_review"
    assert command_item["planner_preview"]["skills_to_execute"] == ["megaeth.identity.jumpserver_command_review"]
    assert command_item["report"]["skills_selected"] == ["megaeth.identity.jumpserver_command_review"]
    assert command_item["report"]["report_title"] == "JumpServer 命令审计报告"

    transfer_body = client.post(
        "/ingest/files",
        files=[("files", ("ftplog.xlsx", transfer_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))],
    ).json()
    transfer_item = transfer_body["results"][0]
    assert transfer_item["normalized_event"]["event_type"] == "jumpserver_transfer_review"
    assert transfer_item["planner_preview"]["skills_to_execute"] == ["megaeth.identity.jumpserver_transfer_review"]
    assert transfer_item["report"]["skills_selected"] == ["megaeth.identity.jumpserver_transfer_review"]
    assert transfer_item["report"]["report_title"] == "JumpServer 文件传输审计报告"

    operate_body = client.post(
        "/ingest/files",
        files=[("files", ("operatelog.xlsx", operate_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))],
    ).json()
    operate_item = operate_body["results"][0]
    assert operate_item["normalized_event"]["event_type"] == "jumpserver_operation_review"
    assert operate_item["planner_preview"]["skills_to_execute"] == ["megaeth.identity.jumpserver_operation_review"]
    assert operate_item["report"]["skills_selected"] == ["megaeth.identity.jumpserver_operation_review"]
    assert operate_item["report"]["report_title"] == "JumpServer 管理平面审计报告"


def test_jumpserver_agent_model_binding_can_override_narrative() -> None:
    login_bytes = make_xlsx_bytes(
        ["用户名", "登录 IP", "状态", "原因描述", "认证方式", "登录日期"],
        [["abel.chen", "10.30.0.4", "失败", "OTP 失效", "MFA", "2026-03-18 09:01:00"]],
    )
    command_bytes = make_xlsx_bytes(
        ["用户", "资产", "命令", "会话", "账号", "风险等级", "时间戳", "远端地址"],
        [["wenze.yan", "512f(192.168.0.206)", "./bft-rpc-client get-leader", "sess-1", "root", "接受(0)", "2026-03-18 09:07:30", "10.30.0.4"]],
    )
    transfer_bytes = make_xlsx_bytes(
        ["用户", "资产", "账号", "操作", "文件名", "开始日期", "成功", "可下载", "会话", "远端地址"],
        [["wenze.yan", "512f(192.168.0.206)", "root", "上传", "/tmp/bft-rpc-client", "2026-03-18 09:05:30", "成功", "否", "ftp-1", "10.30.0.4"]],
    )
    operate_bytes = make_xlsx_bytes(
        ["用户", "动作", "资源类型", "资源", "远端地址", "组织名称", "日期"],
        [["admin", "导出审计日志", "审计任务", "weekly-audit", "10.20.0.8", "Default", "2026-03-18 09:00:00"]],
    )
    files = [
        ("files", ("userloginlog_1.xlsx", login_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("command.xlsx", command_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("ftplog.xlsx", transfer_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("operatelog.xlsx", operate_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
    ]
    with patch(
        "app.core.agent_model_binding.AgentModelBindingService.generate_jumpserver_narrative",
        return_value={
            "comprehensive_conclusion": "这是 Agent 模型生成的 JumpServer 综合结论。",
            "final_judgment_lines": [
                "本批样本中最典型的重点链条包括：",
                "1) wenze.yan 的 /tmp 二进制上传与执行链",
                "本批样本的最终定性应为：高风险运维链，需要继续结合更多证据复核。",
            ],
            "provider": "gemini",
            "agent_id": "megaeth.agent.core",
            "model": "gemini-2.5-flash",
        },
    ):
        body = client.post("/ingest/files", files=files).json()
    composite = body["results"][0]
    assert composite["report"]["summary"] == "这是 Agent 模型生成的 JumpServer 综合结论。"
    assert composite["report"]["execution_mode"] == "agent_augmented"
    assert composite["report"]["agent_context"]["provider"] == "gemini"
    section7 = next(section for section in composite["report"]["structured_sections"] if section["title"] == "7. 综合判断")
    assert section7["bullets"][0] == "本批样本中最典型的重点链条包括："
    assert "wenze.yan 的 /tmp 二进制上传与执行链" in " ".join(section7["bullets"])


def test_jumpserver_xlsx_parser_keeps_full_rows_and_normalizes_star_headers() -> None:
    login_rows = [["abel.chen", "10.30.0.4", "失败(False)", "OTP 失效", "MFA", f"2026-03-18 09:{index:02d}:00"] for index in range(250)]
    command_rows = [["wenze.yan", "512f(192.168.0.206)", "sudo su", "sess-1", "root", "接受(0)", f"2026-03-18 09:{index:02d}:00", "10.30.0.4"] for index in range(250)]
    transfer_rows = [["wenze.yan", "512f(192.168.0.206)", "root", "上传(upload)", "/tmp/bft-rpc-client", "2026-03-18 09:05:30", "Yes", "No", "ftp-1", "10.30.0.4"]]
    operate_rows = [["Administrator(admin)", "导出(export)", "文件传输", "导出搜索", "10.30.0.4", "DEFAULT", "2026-03-18 09:00:00"]]

    files = [
        ("files", ("userloginlog.xlsx", make_xlsx_bytes(["*用户名", "*登录 IP", "*状态", "原因描述", "认证方式", "登录日期"], login_rows), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("command.xlsx", make_xlsx_bytes(["*用户", "*资产", "*命令", "*会话", "*账号", "风险等级", "日期", "远端地址"], command_rows), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("ftplog.xlsx", make_xlsx_bytes(["*用户", "*资产", "*账号", "*操作", "*文件名", "开始日期", "成功", "可下载", "会话", "远端地址"], transfer_rows), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
        ("files", ("operatelog.xlsx", make_xlsx_bytes(["*用户", "*动作", "资源类型", "资源", "远端地址", "组织名称", "日期"], operate_rows), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")),
    ]

    body = client.post("/ingest/files", files=files).json()
    composite = body["results"][0]
    normalized = composite["normalized_event"]["normalized_data"]
    assert normalized["login_summary"]["total_rows"] == 250
    assert normalized["command_summary"]["total_rows"] == 250
    assert normalized["command_summary"]["effective_command_count"] == 250
    assert normalized["file_transfer_summary"]["upload_count"] == 1
    assert normalized["operation_summary"]["export_actions"] == 1


def test_textual_project_docs_do_not_map_to_jumpserver_or_endpoint_by_keyword_collision() -> None:
    body = client.post(
        "/ingest/files",
        files=[
            (
                "files",
                (
                    "PulseOps_前端页面原型说明_字段定义_v0.1.md",
                    "# 字段定义\n这里包含 endpoint、资源类型、动作、组织名称 等产品文档说明。",
                    "text/markdown",
                ),
            )
        ],
    ).json()
    assert body["results"][0]["normalized_event"]["source_type"] == "github"


def test_pipeline_restores_overview_metrics_and_recent_reports_from_history() -> None:
    fake_report = {
        "event_id": "evt-1",
        "event_type": "host_integrity",
        "source_type": "host",
        "planner_reason": "restored",
        "skills_selected": ["megaeth.host.integrity_monitor"],
        "findings": [
            {
                "finding_id": "f-1",
                "skill_id": "megaeth.host.integrity_monitor",
                "risk_level": 4,
                "risk_label": "high",
                "risk_type": "integrity_change",
                "confidence": 0.84,
                "summary": "restored finding",
                "affected_assets": ["host-1"],
                "evidence": [],
                "recommendations": [],
            }
        ],
        "summary": "restored summary",
        "assessment": "restored assessment",
        "likely_issue": True,
        "verdict": "confirmed_posture_risk",
        "evidence_highlights": [],
        "recommended_actions": [],
        "analyst_notes": [],
        "key_facts": [],
        "probable_causes": [],
        "why_flagged": "",
        "report_gaps": [],
        "quick_checks": [],
        "escalation_conditions": [],
        "professional_judgment": "",
        "top_risk_level": 4,
        "top_risk_label": "high",
        "overall_risk_score": 4.2,
        "generated_at": "2026-03-14T10:00:00Z",
        "observability": {},
    }
    with patch("app.core.pipeline.HistoryService.list_reports", return_value=[fake_report]), patch(
        "app.core.pipeline.HistoryService.list_events", return_value=[]
    ):
        pipeline = SecurityPipeline()
    overview = pipeline.overview()
    assert overview["metrics"]["events_processed"] == 1
    assert overview["metrics"]["findings_generated"] == 1
    assert overview["metrics"]["last_event_at"] == "2026-03-14T10:00:00Z"
    assert pipeline.recent()[0]["event_id"] == "evt-1"


def test_pipeline_recent_deduplicates_same_second_same_conclusion() -> None:
    def make_report(event_id: str, event_type: str, source_type: str, verdict: str, summary: str, generated_at: str) -> dict:
        return {
            "event_id": event_id,
            "event_type": event_type,
            "source_type": source_type,
            "planner_reason": "test",
            "skills_selected": ["megaeth.host.integrity_monitor"],
            "findings": [],
            "summary": summary,
            "assessment": summary,
            "likely_issue": True,
            "verdict": verdict,
            "evidence_highlights": [],
            "recommended_actions": [],
            "analyst_notes": [],
            "key_facts": [],
            "probable_causes": [],
            "why_flagged": "",
            "report_gaps": [],
            "quick_checks": [],
            "escalation_conditions": [],
            "professional_judgment": summary,
            "top_risk_level": 3,
            "top_risk_label": "medium",
            "overall_risk_score": 3.0,
            "generated_at": generated_at,
        }

    duplicate_reports = [
        make_report("evt-1", "host_baseline_assessment", "host_risk_analytics", "confirmed_posture_risk", "same summary", "2026-03-15T08:48:50.652721+00:00"),
        make_report("evt-2", "host_baseline_assessment", "host_risk_analytics", "confirmed_posture_risk", "same summary", "2026-03-15T08:48:50.576171+00:00"),
        make_report("evt-3", "endpoint_process", "endpoint", "needs_review", "different summary", "2026-03-15T08:48:50.615755+00:00"),
    ]
    with patch("app.core.pipeline.HistoryService.list_reports", return_value=duplicate_reports), patch(
        "app.core.pipeline.HistoryService.list_events", return_value=[]
    ):
        pipeline = SecurityPipeline()
    recent = pipeline.recent()
    assert len(recent) == 2
    assert recent[0]["event_id"] == "evt-1"
    assert recent[1]["event_id"] == "evt-3"


def test_bitdefender_test_endpoint() -> None:
    fake_result = {
        "base_url": "https://cloud.gravityzone.bitdefender.com/api/v1.0/jsonrpc",
        "company_id": "company-1",
        "inventory_total": 2,
        "endpoint_total": 0,
        "incident_total": 0,
        "incident_error": None,
        "report_total": 1,
        "report_error": None,
        "inventory_items": [{"id": "a"}],
        "endpoint_items": [],
        "incident_items": [],
        "report_items": [{"id": "r"}],
    }
    with patch("app.api.integration_routes.BitdefenderClient.test_connection", return_value=fake_result):
        body = client.post("/integrations/bitdefender/test", json={"api_key": "demo"}).json()
    assert body["company_id"] == "company-1"


def test_bitdefender_network_endpoint_includes_recursive_inventory_devices() -> None:
    fake_inventory = {"total": 2, "items": [{"id": "g-1", "name": "Custom Groups", "type": 4}]}
    fake_endpoints = {"total": 0, "items": []}
    fake_recursive = {"total": 22, "managed_total": 1, "unmanaged_total": 21, "groups_traversed": 5, "items": [{"id": "e-1", "name": "host-1", "details": {"isManaged": True}}]}
    fake_hierarchy = {"total": 44, "managed_total": 10, "unmanaged_total": 34, "groups_traversed": 8, "companies_traversed": 2, "items": [{"id": "e-1", "name": "host-1", "details": {"isManaged": True}}]}
    fake_detail = {"id": "e-1", "name": "host-1", "operatingSystem": "macOS", "riskScore": {"value": "9%"}}
    fake_reports = {"items": [{"id": "r-1", "name": "安全审计报表"}]}
    fake_links = {"lastInstanceUrl": "https://example.com/report.zip"}
    fake_parsed = {
        "row_count": 128,
        "unique_host_count": 28,
        "malware_count": 2,
        "attack_count": 5,
        "blocked_count": 2,
        "top_hosts": [{"name": "host-1", "count": 6}],
        "top_event_types": [{"name": "恶意软件检测", "count": 2}],
        "top_modules": [{"name": "反恶意软件", "count": 2}],
    }
    with patch("app.api.integration_routes.BitdefenderClient.get_network_inventory", return_value=fake_inventory), patch(
        "app.api.integration_routes.BitdefenderClient.get_endpoints", return_value=fake_endpoints
    ), patch("app.api.integration_routes.BitdefenderClient.discover_company_id", return_value="company-1"), patch(
        "app.api.integration_routes.BitdefenderClient.discover_inventory_endpoints", return_value=fake_recursive
    ), patch(
        "app.api.integration_routes.BitdefenderClient.discover_inventory_hierarchy", return_value=fake_hierarchy
    ), patch(
        "app.api.integration_routes.BitdefenderClient.get_all_companies", side_effect=ValueError("forbidden")
    ), patch(
        "app.api.integration_routes.BitdefenderClient.get_all_custom_groups", return_value={"total": 2, "items": [{"id": "cg-1"}]}
    ), patch("app.api.integration_routes.BitdefenderClient.get_reports", return_value=fake_reports), patch(
        "app.api.integration_routes.BitdefenderClient.get_report_download_links", return_value=fake_links
    ), patch(
        "app.api.integration_routes.BitdefenderClient.download_report_zip", return_value=b"zip"
    ), patch(
        "app.api.integration_routes.parse_report_zip_bundle", return_value=fake_parsed
    ), patch("app.api.integration_routes.BitdefenderClient.get_managed_endpoint_details", return_value=fake_detail):
        body = client.post("/integrations/bitdefender/network", json={"api_key": "demo"}).json()
    assert body["inventory_endpoints"]["total"] == 22
    assert body["inventory_hierarchy"]["total"] == 44
    assert body["custom_groups"]["total"] == 2
    assert body["managed_endpoint_details_preview"][0]["id"] == "e-1"
    assert body["latest_report_summary"]["row_count"] == 128
    assert body["latest_report_summary"]["top_hosts"][0]["name"] == "host-1"


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
