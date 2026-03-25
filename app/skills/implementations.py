from __future__ import annotations

from typing import Any
from uuid import uuid4

from app.core.jumpserver_summary import (
    summarize_command_rows,
    summarize_login_rows,
    summarize_operation_rows,
    summarize_transfer_rows,
)
from app.models.event import NormalizedEvent
from app.models.finding import Finding


# Security-log-analysis mainline skill implementations.
def _risk_label(level: int) -> str:
    return {1: "info", 2: "low", 3: "medium", 4: "high", 5: "critical"}.get(level, "info")


class Skill:
    def __init__(
        self,
        skill_id: str,
        skill_name: str,
        category: str,
        description: str,
        execution_mode: str = "rule_only",
        agent_trigger_conditions: list[str] | None = None,
        rule_fallback_conditions: list[str] | None = None,
        max_context_policy: str = "full",
    ) -> None:
        self.skill_id = skill_id
        self.skill_name = skill_name
        self.category = category
        self.description = description
        self.execution_mode = execution_mode
        self.agent_trigger_conditions = agent_trigger_conditions or []
        self.rule_fallback_conditions = rule_fallback_conditions or []
        self.max_context_policy = max_context_policy

    def execute(self, event: NormalizedEvent) -> list[Finding]:
        data = event.normalized_data
        blob = " ".join(str(v).lower() for v in data.values())
        findings: list[Finding] = []
        easm_assessments = data.get("asset_assessments", []) if isinstance(data.get("asset_assessments"), list) else []
        if event.event_type == "easm_asset_assessment" and easm_assessments:
            high_assets = [item for item in easm_assessments if str((item.get("scores") or {}).get("severity") or "") in {"High", "Critical"}]
            delegation_assets = [item for item in easm_assessments if "third_party_dns_delegation" in item.get("tags", [])]
            historical_assets = [item for item in easm_assessments if "historical_asset_hint" in item.get("tags", [])]
            origin_assets = [
                item for item in easm_assessments
                if "potential_origin_exposure" in item.get("tags", []) or "cdn_and_direct_origin_coexist" in item.get("tags", [])
            ]
            if self.skill_id == "megaeth.easm.asset_discovery":
                findings.append(
                    self._finding(
                        event,
                        4 if high_assets else 3,
                        "external_surface_inventory",
                        f"EASM 多文件关联后共识别 {len(easm_assessments)} 个外部资产，其中高风险资产 {len(high_assets)} 个。",
                        evidence=[{"top_assets": [item.get("asset") for item in easm_assessments[:8]]}],
                        recommendations=[
                            "优先对功能性域名、历史资产和跨层重复出现的资产建立治理清单。",
                            "把证书层、DNS 层和服务层交叉出现的资产作为长期跟踪对象。",
                        ],
                    )
                )
                return findings
            if self.skill_id == "megaeth.easm.service_scan" and origin_assets:
                findings.append(
                    self._finding(
                        event,
                        4,
                        "origin_exposure_risk",
                        f"外部攻击面中发现 {len(origin_assets)} 个资产同时具备 CDN 与直连源站信号，存在潜在源站暴露风险。",
                        evidence=[{"origin_exposure_assets": [item.get("asset") for item in origin_assets[:8]]}],
                        recommendations=[
                            "优先验证是否仅允许 CDN 回源，确认直连公网 IP 是否仍然必要。",
                            "复核 API、Dashboard 和 RPC 命名资产的源站隔离策略。",
                        ],
                    )
                )
                return findings
            if self.skill_id == "megaeth.easm.tls_analysis":
                cert_assets = [item for item in easm_assessments if item.get("providers") or item.get("evidence")]
                if cert_assets:
                    findings.append(
                        self._finding(
                            event,
                            3 if historical_assets else 4,
                            "tls_and_certificate_signal",
                            f"证书层与服务层交叉后识别出 {len(cert_assets)} 个资产存在证书生命周期或 Origin Certificate 相关信号。",
                            evidence=[{"historical_assets": [item.get("asset") for item in historical_assets[:8]]}],
                            recommendations=[
                                "确认历史证书对应资产是否已完成 DNS、托管与证书侧清理。",
                                "对 Cloudflare Origin Certificate 相关资产复核是否存在绕过 CDN 的路径。",
                            ],
                        )
                    )
                    return findings
            if self.skill_id == "megaeth.easm.vulnerability_scan":
                exposed_assets = [
                    item for item in easm_assessments
                    if "public_http_enabled" in item.get("tags", []) or "public_https_enabled" in item.get("tags", [])
                ]
                if exposed_assets:
                    findings.append(
                        self._finding(
                            event,
                            4 if high_assets else 3,
                            "internet_reachable_functional_surface",
                            f"共有 {len(exposed_assets)} 个资产具备公网协议暴露信号，功能性资产需要优先核实暴露必要性。",
                            evidence=[{"exposed_assets": [item.get("asset") for item in exposed_assets[:8]]}],
                            recommendations=[
                                "优先下钻 RPC、API、Dashboard 等功能面资产，确认是否需要公网直接暴露。",
                                "关闭不必要的明文 HTTP，或为必要暴露资产补强鉴权与访问控制。",
                            ],
                        )
                    )
                    return findings
            if self.skill_id == "megaeth.easm.external_intelligence" and (delegation_assets or historical_assets):
                findings.append(
                    self._finding(
                        event,
                        3,
                        "boundary_and_lifecycle_signal",
                        f"外部情报层识别出 {len(delegation_assets)} 个第三方委派资产，以及 {len(historical_assets)} 个历史资产线索。",
                        evidence=[
                            {"delegation_assets": [item.get("asset") for item in delegation_assets[:6]]},
                            {"historical_assets": [item.get("asset") for item in historical_assets[:6]]},
                        ],
                        recommendations=[
                            "确认第三方 DNS/托管委派是否仍然必要，并补齐资产所有权与生命周期记录。",
                            "把历史资产线索纳入 stale asset 治理与下线核查范围。",
                        ],
                    )
                )
                return findings
        if self.skill_id == "megaeth.cicd.pr_security_review" and any(token in blob for token in ("subprocess", "curl", "bash")):
            findings.append(self._finding(event, 4, "dangerous_code", "Potential dangerous execution flow found in supplied code or PR content."))
        elif self.skill_id == "megaeth.cicd.secret_detection" and any(token in blob for token in ("akia", "private key", "api_key", "secret")):
            findings.append(self._finding(event, 5, "secret_exposure", "Potential secret material detected in supplied content."))
        elif self.skill_id == "megaeth.endpoint.process_anomaly":
            rows = data.get("rows", [])
            if isinstance(rows, list) and rows:
                malware_rows = []
                network_attack_rows = []
                blocked_site_rows = []
                affected_hosts: set[str] = set()
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    event_type = str(row.get("事件类型") or row.get("event_type") or "").lower()
                    module = str(row.get("模块") or row.get("module") or "").lower()
                    details = str(row.get("详情") or row.get("details") or "")
                    host = str(row.get("端点名称") or row.get("endpoint_name") or row.get("端点 FQDN") or "").strip()
                    if host:
                        affected_hosts.add(host)
                    if "恶意软件检测" in event_type or "恶意软件" in module:
                        malware_rows.append({"host": host, "details": details[:220]})
                    if "网络攻击" in event_type or "attack." in details.lower() or "network attack" in event_type:
                        network_attack_rows.append({"host": host, "details": details[:220]})
                    if "阻止的网站" in event_type or "反钓鱼" in module:
                        blocked_site_rows.append({"host": host, "details": details[:220]})
                if malware_rows:
                    findings.append(
                        self._finding(
                            event,
                            5,
                            "malware_detection",
                            f"Bitdefender report contains {len(malware_rows)} malware detection record(s) across managed endpoints.",
                            evidence=[
                                {"malware_samples": malware_rows[:5]},
                                {"affected_hosts": sorted(affected_hosts)[:8]},
                                {"top_malware_hosts": [item["host"] for item in malware_rows[:5] if item.get("host")]},
                            ],
                            recommendations=[
                                "Validate whether the detected files were fully removed or quarantined on each affected endpoint.",
                                "Review the impacted endpoints for persistence, credential access, and follow-on activity around the detection time.",
                            ],
                        )
                    )
                if network_attack_rows:
                    findings.append(
                        self._finding(
                            event,
                            4,
                            "network_attack_detection",
                            f"Bitdefender report contains {len(network_attack_rows)} network attack detection record(s), including exploit-style signatures.",
                            evidence=[
                                {"network_attack_samples": network_attack_rows[:5]},
                                {"top_attack_hosts": [item["host"] for item in network_attack_rows[:5] if item.get("host")]},
                            ],
                            recommendations=[
                                "Correlate the detected attack signatures with web access logs and endpoint telemetry to confirm whether exploitation succeeded.",
                                "Prioritize repeated exploit-style detections on the same host for deeper incident review.",
                            ],
                        )
                    )
                if blocked_site_rows:
                    findings.append(
                        self._finding(
                            event,
                            3,
                            "phishing_or_malicious_web",
                            f"Bitdefender report shows {len(blocked_site_rows)} blocked website event(s), suggesting phishing or malicious web exposure.",
                            evidence=[
                                {"blocked_sites": blocked_site_rows[:5]},
                                {"top_blocked_site_hosts": [item["host"] for item in blocked_site_rows[:5] if item.get("host")]},
                            ],
                            recommendations=[
                                "Review the blocked domains and identify whether any user repeatedly attempted to access the same suspicious destination.",
                                "Correlate blocked-site activity with endpoint malware detections on the same host or user profile.",
                            ],
                        )
                    )
                if findings:
                    return findings
            if any(token in blob for token in ("attack.localfileinclusion", "/.env", "shellspawned", "credentialtheft")):
                findings.append(self._finding(event, 4, "endpoint_process", "Endpoint incident material contains suspicious process or exploit indicators."))
        elif self.skill_id == "megaeth.host.integrity_monitor":
            if event.event_type == "host_baseline_assessment":
                return findings
            rows = data.get("rows", [])
            if isinstance(rows, list) and rows:
                severe = []
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    title = str(row.get("发现名称") or row.get("\ufeff发现名称") or "")
                    score = str(row.get("风险评分") or "0")
                    try:
                        if int(float(score)) >= 95:
                            severe.append(title)
                    except ValueError:
                        pass
                if severe:
                    findings.append(
                        self._finding(
                            event,
                            4,
                            "integrity_change",
                            f"Host hardening report contains {len(severe)} critical or near-critical control gaps across operating system baselines.",
                            evidence=[{"top_findings": severe[:5]}],
                            recommendations=[
                                "Prioritize filesystem, logging, and audit control gaps with risk scores above 95.",
                                "Deploy missing host integrity controls such as auditd and AIDE on affected Unix assets.",
                            ],
                        )
                    )
        elif self.skill_id == "megaeth.host.baseline_compliance_analysis":
            rows = data.get("rows", [])
            filesystem_findings = []
            temp_findings = []
            log_findings = []
            module_findings = []
            if isinstance(rows, list):
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    title = str(row.get("发现名称") or row.get("\ufeff发现名称") or row.get("finding_name") or "").strip()
                    risk_score = str(row.get("风险评分") or row.get("risk_score") or "0")
                    try:
                        numeric_score = int(float(risk_score))
                    except ValueError:
                        numeric_score = 0
                    lowered = title.lower()
                    if "/var/log/audit" in lowered:
                        filesystem_findings.append({"title": title, "score": numeric_score})
                    elif "/var/tmp" in lowered and "目录未单独分区" in lowered:
                        temp_findings.append({"title": title, "score": numeric_score})

                    if any(token in title for token in ("日志文件的权限未配置", "日志权限未正确配置")):
                        log_findings.append({"title": title, "score": numeric_score})

                    if "未安装 auditd" in title:
                        log_findings.append({"title": title, "score": numeric_score})

                    if any(token in lowered for token in ("cramfs", "udf")):
                        module_findings.append({"title": title, "score": numeric_score})
            if filesystem_findings:
                findings.append(
                    self._finding(
                        event,
                        3,
                        "filesystem_isolation_issue",
                        "发现关键日志目录隔离配置问题，可能增加日志耗尽与系统稳定性风险。",
                        evidence=[
                            {"filesystem_isolation_issues": list(dict.fromkeys(item["title"] for item in filesystem_findings[:4]))},
                        ],
                        recommendations=[
                            "为 /var/log/audit 创建独立分区，并确认日志轮转策略已启用。",
                        ],
                    )
                )
            if temp_findings:
                findings.append(
                    self._finding(
                        event,
                        3,
                        "temporary_directory_configuration",
                        "发现临时目录隔离配置不足，可能增加临时文件滥用或权限提升风险。",
                        evidence=[
                            {"temporary_directory_configuration": list(dict.fromkeys(item["title"] for item in temp_findings[:4]))},
                        ],
                        recommendations=[
                            "为 /var/tmp 等临时目录启用 nodev、nosuid、noexec 挂载参数。",
                        ],
                    )
                )
            if log_findings:
                findings.append(
                    self._finding(
                        event,
                        3,
                        "log_permission_configuration",
                        "发现日志权限或审计配置问题，可能导致日志篡改、泄露或审计能力不足。",
                        evidence=[
                            {"log_configuration_issues": list(dict.fromkeys(item["title"] for item in log_findings[:4]))},
                        ],
                        recommendations=[
                            "收紧安全日志权限，关键日志建议控制在 chmod 600 范围。",
                        ],
                    )
                )
            if module_findings:
                findings.append(
                    self._finding(
                        event,
                        2,
                        "unused_filesystem_modules",
                        "发现不必要文件系统模块处于启用状态，会扩大系统攻击面。",
                        evidence=[
                            {"unused_filesystem_modules": list(dict.fromkeys(item["title"] for item in module_findings[:4]))},
                        ],
                        recommendations=[
                            "禁用 cramfs、udf 等未使用文件系统模块，减少不必要攻击面。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.host.systemd_service_risk":
            rows = data.get("rows", [])
            service_findings = []
            if isinstance(rows, list):
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    title = str(row.get("发现名称") or row.get("\ufeff发现名称") or "")
                    if any(token in title.lower() for token in ("ssh", "telnet", "rsync", "icmp", "openssh", "rds", "printer")):
                        service_findings.append(title)
            if service_findings:
                findings.append(
                    self._finding(
                        event,
                        4,
                        "service_risk",
                        f"Network-facing service posture includes {len(service_findings)} risky exposure or remote-access control findings.",
                        evidence=[{"service_findings": service_findings[:6]}],
                        recommendations=[
                            "Tighten SSH exposure, legacy remote services, and insecure network control settings.",
                            "Validate that remote administration paths are restricted to approved management boundaries.",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.cloud.config_audit" and any(token in blob for token in ("public bucket", "security group", "cloudtrail", "bucket")):
            findings.append(self._finding(event, 3, "cloud_misconfiguration", "Cloud posture issues suggest misconfiguration or missing controls."))
        elif self.skill_id == "megaeth.easm.service_scan" and any(token in blob for token in ("port", "service", "ssh", "http")):
            findings.append(self._finding(event, 3, "service_exposure", "Service exposure data indicates externally reachable services requiring review."))
        elif self.skill_id == "megaeth.key.kms_risk" and any(token in blob for token in ("sign", "kms", "caller")):
            findings.append(self._finding(event, 5, "kms_access", "KMS signing activity deviates from expected operational baseline."))
        elif self.skill_id == "megaeth.identity.anomalous_access_review":
            login_summary = data.get("login_summary", {}) if isinstance(data.get("login_summary"), dict) else {}
            if not login_summary:
                rows = [row for row in data.get("rows", []) if isinstance(row, dict)] if isinstance(data.get("rows"), list) else []
                login_summary = summarize_login_rows(rows)
            failure_count = int(login_summary.get("failure_count", 0) or 0)
            top_failed_accounts = login_summary.get("top_failed_accounts", []) if isinstance(login_summary.get("top_failed_accounts"), list) else []
            if failure_count:
                findings.append(
                    self._finding(
                        event,
                        2 if failure_count < 50 else 3,
                        "login_failure_cluster",
                        f"登录侧存在 {failure_count} 条认证失败记录，需要结合 MFA 和代理地址语义判断是否属于异常访问。",
                        evidence=[{"top_failed_accounts": top_failed_accounts[:6]}],
                        recommendations=[
                            "优先确认失败登录是否集中在单一代理地址、过期 OTP 或已知口令错误场景。",
                            "不要把 JumpServer 代理地址直接当成真实攻击源。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.identity.jumpserver_command_review":
            command_summary = data.get("command_summary", {}) if isinstance(data.get("command_summary"), dict) else {}
            if not command_summary:
                rows = [row for row in data.get("rows", []) if isinstance(row, dict)] if isinstance(data.get("rows"), list) else []
                command_summary = summarize_command_rows(rows)
            total_rows = int(command_summary.get("total_rows", 0) or 0)
            effective_command_count = int(command_summary.get("effective_command_count", 0) or 0)
            high_risk_semantics = command_summary.get("high_risk_semantics", {}) if isinstance(command_summary.get("high_risk_semantics"), dict) else {}
            top_accounts = command_summary.get("top_risk_accounts", []) if isinstance(command_summary.get("top_risk_accounts"), list) else []
            if total_rows or effective_command_count:
                findings.append(
                    self._finding(
                        event,
                        4 if effective_command_count >= 100 or top_accounts else 3,
                        "high_risk_command_activity",
                        f"命令审计共 {total_rows} 条，去噪后有效命令约 {effective_command_count} 条，已经出现提权、服务控制、下载执行或横向操作等高风险命令语义。",
                        evidence=[
                            {"high_risk_semantics": high_risk_semantics},
                            {"top_risk_accounts": top_accounts[:6]},
                        ],
                        recommendations=[
                            "优先按账户、资产和时间窗复核高风险命令链，确认是否处于授权发布或维护窗口。",
                            "把下载执行、跨主机同步、服务启停和权限放开链条作为重点复核对象。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.identity.jumpserver_transfer_review":
            transfer_summary = data.get("file_transfer_summary", {}) if isinstance(data.get("file_transfer_summary"), dict) else {}
            if not transfer_summary:
                rows = [row for row in data.get("rows", []) if isinstance(row, dict)] if isinstance(data.get("rows"), list) else []
                transfer_summary = summarize_transfer_rows(rows)
            total_rows = int(transfer_summary.get("total_rows", 0) or 0)
            high_risk_upload_count = int(transfer_summary.get("high_risk_upload_count", 0) or 0)
            top_uploads = transfer_summary.get("top_uploads", []) if isinstance(transfer_summary.get("top_uploads"), list) else []
            if total_rows or high_risk_upload_count:
                findings.append(
                    self._finding(
                        event,
                        5 if high_risk_upload_count else 3,
                        "high_risk_file_transfer",
                        f"文件传输日志共 {total_rows} 条，其中高风险上传 {high_risk_upload_count} 条，重点是 /tmp 投放、root 账号上传和二进制落地信号。",
                        evidence=[{"top_uploads": top_uploads[:6]}],
                        recommendations=[
                            "优先核实上传文件是否属于授权工具、测试二进制或临时调试载荷。",
                            "结合命令侧继续复核这些文件是否已经被移动、放权和执行。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.identity.jumpserver_operation_review":
            operation_summary = data.get("operation_summary", {}) if isinstance(data.get("operation_summary"), dict) else {}
            if not operation_summary:
                rows = [row for row in data.get("rows", []) if isinstance(row, dict)] if isinstance(data.get("rows"), list) else []
                operation_summary = summarize_operation_rows(rows)
            total_rows = int(operation_summary.get("total_rows", 0) or 0)
            export_actions = int(operation_summary.get("export_actions", 0) or 0)
            authorization_updates = int(operation_summary.get("authorization_updates", 0) or 0)
            host_or_account_creation = int(operation_summary.get("host_or_account_creation", 0) or 0)
            session_creation = int(operation_summary.get("session_creation", 0) or 0)
            top_operations = operation_summary.get("top_operations", []) if isinstance(operation_summary.get("top_operations"), list) else []
            if total_rows:
                findings.append(
                    self._finding(
                        event,
                        3,
                        "high_impact_control_plane_activity",
                        f"管理平面共记录 {total_rows} 条操作，涉及导出 {export_actions} 条、授权/更新 {authorization_updates} 条、主机/账号创建 {host_or_account_creation} 条、会话创建 {session_creation} 条。",
                        evidence=[{"top_operations": top_operations[:8]}],
                        recommendations=[
                            "把管理平面动作与主机执行链分开定性，避免直接把控制台动作当成入侵证据。",
                            "优先复核日志导出、资产授权调整、主机接入和账号创建是否对应正常管理动作。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.identity.jumpserver_multi_source_review":
            correlations = data.get("cross_source_correlations", []) if isinstance(data.get("cross_source_correlations"), list) else []
            accounts = data.get("high_risk_accounts", []) if isinstance(data.get("high_risk_accounts"), list) else []
            login_summary = data.get("login_summary", {}) if isinstance(data.get("login_summary"), dict) else {}
            file_transfer_summary = data.get("file_transfer_summary", {}) if isinstance(data.get("file_transfer_summary"), dict) else {}
            operation_summary = data.get("operation_summary", {}) if isinstance(data.get("operation_summary"), dict) else {}
            if correlations:
                findings.append(
                    self._finding(
                        event,
                        4,
                        "cross_source_high_risk_chain",
                        f"JumpServer 多源日志已经拼接出 {len(correlations)} 条高风险操作链，重点是上传、提权、放权、执行与网络验证的连续行为。",
                        evidence=[{"cross_source_correlations": correlations[:5]}],
                        recommendations=[
                            "按用户、资产、时间窗和文件名继续做会话级复核，确认是否属于授权维护窗口。",
                            "优先检查包含 /tmp 上传、二进制执行和服务变更的链条。",
                        ],
                    )
                )
            if accounts:
                findings.append(
                    self._finding(
                        event,
                        4,
                        "high_risk_operations_cluster",
                        f"JumpServer 审计中识别出 {len(accounts)} 个需要优先复核的高风险账户，已经出现高权限运维或调试链。",
                        evidence=[{"high_risk_accounts": accounts[:5]}],
                        recommendations=[
                            "逐个复核高风险账户的资产范围、代表命令和 supporting sources，判断是否与正式变更单一致。",
                            "对高频出现服务控制、跨主机分发和二进制替换的账户建立专项排查列表。",
                        ],
                    )
                )
            high_risk_upload_count = int(file_transfer_summary.get("high_risk_upload_count", 0) or 0)
            if high_risk_upload_count:
                findings.append(
                    self._finding(
                        event,
                        5 if correlations else 4,
                        "binary_drop_to_tmp",
                        f"文件传输侧发现 {high_risk_upload_count} 条高风险上传，已出现 /tmp 投放、root 账号上传或二进制落地信号。",
                        evidence=[{"top_uploads": file_transfer_summary.get("top_uploads", [])[:5]}],
                        recommendations=[
                            "优先确认上传文件是否属于授权工具、测试二进制或临时调试载荷。",
                            "对已上传文件补充哈希、落地路径、执行结果和相关命令会话证据。",
                        ],
                    )
                )
            if int(operation_summary.get("total_rows", 0) or 0):
                export_actions = int(operation_summary.get("export_actions", 0) or 0)
                authorization_updates = int(operation_summary.get("authorization_updates", 0) or 0)
                host_or_account_creation = int(operation_summary.get("host_or_account_creation", 0) or 0)
                session_creation = int(operation_summary.get("session_creation", 0) or 0)
                if export_actions or authorization_updates or host_or_account_creation or session_creation:
                    findings.append(
                        self._finding(
                            event,
                            3,
                            "control_plane_high_impact_actions",
                            "管理平面存在导出、授权、主机/账号创建或会话创建等高影响动作，应与主机侧执行链分开理解。",
                            evidence=[{"top_operations": operation_summary.get("top_operations", [])[:6]}],
                            recommendations=[
                                "把管理平面动作与主机侧命令执行分开定性，避免直接把控制台动作当成入侵证据。",
                                "优先确认这些操作是否对应资产授权调整、日志导出、主机接入或维护窗口内的正常管理动作。",
                            ],
                        )
                    )
            failure_count = int(login_summary.get("failure_count", 0) or 0)
            if failure_count:
                findings.append(
                    self._finding(
                        event,
                        2 if failure_count < 50 else 3,
                        "authentication_failure_cluster",
                        f"登录侧出现 {failure_count} 条认证失败记录，但当前仍不足以单独支持外部入侵已成立。",
                        evidence=[{"top_failed_accounts": login_summary.get("top_failed_accounts", [])[:6]}],
                        recommendations=[
                            "优先结合 MFA 失败、OTP 失效和代理地址语义判断真实风险。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.appsec.whitebox_recon":
            surfaces = data.get("attack_surfaces", [])
            routes = data.get("candidate_paths", [])
            patterns = data.get("exposed_patterns", [])
            if surfaces or routes or patterns:
                findings.append(
                    self._finding(
                        event,
                        3,
                        "whitebox_attack_surface",
                        "白盒安全侦察显示应用存在值得优先验证的入口暴露与攻击面线索。",
                        evidence=[
                            {"attack_surfaces": surfaces[:5] if isinstance(surfaces, list) else []},
                            {"candidate_paths": routes[:6] if isinstance(routes, list) else []},
                            {"exposed_patterns": patterns[:5] if isinstance(patterns, list) else []},
                        ],
                        recommendations=[
                            "优先复核高风险 API 与管理入口的鉴权覆盖情况。",
                            "将高风险入口加入后续 exploit validation 与回归测试范围。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.appsec.whitebox_exploit_validation":
            validated = []
            candidates = []
            for item in data.get("validated_findings", []) if isinstance(data.get("validated_findings"), list) else []:
                if not isinstance(item, dict):
                    continue
                if str(item.get("proof_status")).lower() == "validated":
                    validated.append(item)
                else:
                    candidates.append(item)
            if validated:
                findings.append(
                    self._finding(
                        event,
                        4,
                        "validated_whitebox_exploit",
                        f"白盒安全验证已确认 {len(validated)} 条可复现的高优先级利用路径。",
                        evidence=[{"validated_findings": validated[:5]}],
                        recommendations=[
                            "优先修复已确认可复现的问题，并保留最小 PoC 用于回归验证。",
                            "对相关接口补充鉴权、输入校验与日志审计规则。",
                        ],
                    )
                )
            if candidates:
                findings.append(
                    self._finding(
                        event,
                        3,
                        "candidate_whitebox_issue",
                        f"白盒安全验证还识别出 {len(candidates)} 条待进一步确认的候选风险。",
                        evidence=[{"candidate_findings": candidates[:5]}],
                        recommendations=[
                            "将候选风险纳入下一轮验证或人工复核。",
                        ],
                    )
                )
        elif self.skill_id == "megaeth.appsec.whitebox_report_synthesis":
            summary = str(data.get("executive_summary") or "").strip()
            validated = [item for item in data.get("validated_findings", []) if isinstance(item, dict)] if isinstance(data.get("validated_findings"), list) else []
            actions = data.get("priority_actions", []) if isinstance(data.get("priority_actions"), list) else []
            if summary or validated:
                findings.append(
                    self._finding(
                        event,
                        4 if any(str(item.get("severity")).lower() in {"high", "critical"} for item in validated) else 3,
                        "whitebox_security_report",
                        summary or "白盒安全综合报告显示应用存在需要尽快治理的攻击路径与输入边界风险。",
                        evidence=[
                            {"validated_findings": validated[:5]},
                            {"priority_actions": actions[:5]},
                        ],
                        recommendations=actions[:4] or [
                            "将白盒测试结果纳入发布前门禁，并持续回归关键业务路径。",
                        ],
                    )
                )
        return findings

    def _finding(
        self,
        event: NormalizedEvent,
        level: int,
        risk_type: str,
        summary: str,
        evidence: list[dict[str, Any]] | None = None,
        recommendations: list[str] | None = None,
    ) -> Finding:
        return Finding(
            finding_id=f"{event.event_id}-{self.skill_id}-{uuid4().hex[:8]}",
            skill_id=self.skill_id,
            risk_level=level,
            risk_label=_risk_label(level),
            risk_type=risk_type,
            confidence=0.84 if level >= 4 else 0.74,
            summary=summary,
            affected_assets=[str(event.asset_context.get("asset_name", "unknown"))],
            evidence=evidence or [],
            recommendations=recommendations or [],
        )


SKILLS = {
    "megaeth.cicd.pr_security_review": Skill("megaeth.cicd.pr_security_review", "PR Security Review", "cicd", "Reviews supplied code and change content."),
    "megaeth.cicd.secret_detection": Skill("megaeth.cicd.secret_detection", "Secret Detection", "cicd", "Detects exposed keys and secrets."),
    "megaeth.endpoint.process_anomaly": Skill("megaeth.endpoint.process_anomaly", "Endpoint Process Anomaly", "endpoint", "Analyzes endpoint incident material."),
    "megaeth.host.baseline_compliance_analysis": Skill("megaeth.host.baseline_compliance_analysis", "Baseline Compliance Analysis", "host", "Parses host baseline reports and compliance findings."),
    "megaeth.host.integrity_monitor": Skill("megaeth.host.integrity_monitor", "Host Integrity Monitor", "host", "Evaluates host baseline and integrity drift."),
    "megaeth.host.systemd_service_risk": Skill("megaeth.host.systemd_service_risk", "Service Risk Review", "host", "Reviews remote-access and service posture issues."),
    "megaeth.host.binary_tamper_review": Skill("megaeth.host.binary_tamper_review", "Binary Tamper Review", "host", "Reserved for binary integrity review."),
    "megaeth.cloud.config_audit": Skill("megaeth.cloud.config_audit", "Cloud Config Audit", "cloud", "Reviews cloud configuration drift."),
    "megaeth.appsec.whitebox_recon": Skill("megaeth.appsec.whitebox_recon", "Whitebox Recon", "appsec", "Analyzes whitebox reconnaissance output and attack surface hints."),
    "megaeth.appsec.whitebox_exploit_validation": Skill("megaeth.appsec.whitebox_exploit_validation", "Whitebox Exploit Validation", "appsec", "Processes whitebox exploit validation results."),
    "megaeth.appsec.whitebox_report_synthesis": Skill(
        "megaeth.appsec.whitebox_report_synthesis",
        "Whitebox Report Synthesis",
        "appsec",
        "Synthesizes delivery-grade whitebox security reports.",
        execution_mode="agent_optional",
        agent_trigger_conditions=[
            "需要综合多个白盒发现并输出更像分析师的结论时",
            "结构化发现与证据已经齐全、适合生成正式报告时",
        ],
        rule_fallback_conditions=[
            "模型不可用、超时或返回结构不合规时",
            "上游白盒发现不足，无法支撑可靠综合结论时",
        ],
        max_context_policy="summary_first",
    ),
    "megaeth.easm.asset_discovery": Skill("megaeth.easm.asset_discovery", "Asset Discovery", "easm", "Processes asset inventory material."),
    "megaeth.easm.service_scan": Skill("megaeth.easm.service_scan", "Service Exposure", "easm", "Processes service exposure outputs."),
    "megaeth.easm.tls_analysis": Skill("megaeth.easm.tls_analysis", "TLS Analysis", "easm", "Reserved for TLS posture review."),
    "megaeth.key.kms_risk": Skill("megaeth.key.kms_risk", "KMS Risk", "key", "Reviews abnormal key usage."),
    "megaeth.key.private_key_exposure": Skill("megaeth.key.private_key_exposure", "Private Key Exposure", "key", "Detects exposed key material."),
    "megaeth.identity.policy_risk_analysis": Skill("megaeth.identity.policy_risk_analysis", "Policy Risk Analysis", "identity", "Analyzes policy sprawl and privilege risk."),
    "megaeth.identity.anomalous_access_review": Skill(
        "megaeth.identity.anomalous_access_review",
        "Anomalous Access Review",
        "identity",
        "Reviews identity-driven access anomalies.",
        execution_mode="agent_optional",
        agent_trigger_conditions=[
            "登录数据完整，且需要生成更自然的异常访问判断时",
            "同一批存在成功/失败模式、账户集中度和代理地址线索时",
        ],
        rule_fallback_conditions=[
            "只有基础计数、缺少可解释线索时",
            "模型不可用或单文件内容不足以支持归纳时",
        ],
        max_context_policy="summary_first",
    ),
    "megaeth.identity.jumpserver_command_review": Skill(
        "megaeth.identity.jumpserver_command_review",
        "JumpServer Command Audit",
        "identity",
        "Reviews JumpServer command audit material and high-risk command chains.",
        execution_mode="agent_optional",
        agent_trigger_conditions=[
            "命令审计已完成去噪，并能提供高风险语义摘要与代表命令时",
            "需要把提权、服务控制、横向动作写成更像审计结论的文字时",
        ],
        rule_fallback_conditions=[
            "命令原始数据过大且摘要不足时",
            "去噪失败、有效命令统计明显不可信时",
            "模型不可用或超时时",
        ],
        max_context_policy="summary_plus_samples",
    ),
    "megaeth.identity.jumpserver_transfer_review": Skill(
        "megaeth.identity.jumpserver_transfer_review",
        "JumpServer Transfer Review",
        "identity",
        "Reviews JumpServer file transfer material and binary delivery signals.",
        execution_mode="agent_optional",
        agent_trigger_conditions=[
            "上传/下载链条和目标路径清晰，适合生成风险链描述时",
            "需要把文件投放与后续执行动作串起来解释时",
        ],
        rule_fallback_conditions=[
            "只有少量传输记录，无法形成稳定链条时",
            "模型不可用或上下文摘要缺失时",
        ],
        max_context_policy="summary_plus_samples",
    ),
    "megaeth.identity.jumpserver_operation_review": Skill(
        "megaeth.identity.jumpserver_operation_review",
        "JumpServer Control Plane Audit",
        "identity",
        "Reviews JumpServer control-plane actions such as export, authorization, and host/account creation.",
        execution_mode="agent_optional",
        agent_trigger_conditions=[
            "管理平面存在创建、授权、导出等高影响动作，需要生成管理面判断时",
            "需要把操作者、资源类型和时间线解释成安全背景时",
        ],
        rule_fallback_conditions=[
            "只有零散操作记录，无法形成管理平面结论时",
            "模型不可用或摘要字段不完整时",
        ],
        max_context_policy="summary_plus_samples",
    ),
    "megaeth.identity.jumpserver_multi_source_review": Skill(
        "megaeth.identity.jumpserver_multi_source_review",
        "JumpServer Multi-Source Review",
        "identity",
        "Correlates JumpServer login, command, and file transfer evidence into high-risk operation chains.",
        execution_mode="agent_optional",
        agent_trigger_conditions=[
            "同批已覆盖多个 JumpServer 场景，需要输出综合结论与综合判断时",
            "跨源关联和高危账户画像已经提炼完成时",
        ],
        rule_fallback_conditions=[
            "只上传了单文件或跨源摘要明显缺失时",
            "模型不可用、超时或返回结构不合规时",
        ],
        max_context_policy="summary_plus_samples",
    ),
    "megaeth.cloud.identity_surface": Skill("megaeth.cloud.identity_surface", "Cloud Identity Surface", "cloud", "Reviews cloud privilege surface."),
    "megaeth.easm.vulnerability_scan": Skill("megaeth.easm.vulnerability_scan", "Exposure Verification", "easm", "Processes vulnerability and exposure verification results."),
    "megaeth.easm.external_intelligence": Skill("megaeth.easm.external_intelligence", "External Intelligence", "easm", "Processes internet intelligence and exposure context."),
}
