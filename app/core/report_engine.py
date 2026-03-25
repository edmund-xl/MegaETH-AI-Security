from __future__ import annotations

# Security-log-analysis mainline report engine.

from datetime import datetime, timezone
from typing import Any

from app.core.agent_model_binding import AgentModelBindingService
from app.core.jumpserver_summary import (
    summarize_command_rows,
    summarize_login_rows,
    summarize_operation_rows,
    summarize_transfer_rows,
)
from app.models.event import NormalizedEvent
from app.models.finding import Finding, SecurityReport


class ReportEngine:
    def __init__(self, agent_model_binding: AgentModelBindingService | None = None) -> None:
        self.agent_model_binding = agent_model_binding

    def _jumpserver_sample_commands(self, rows: list[dict[str, Any]], limit: int = 8) -> list[dict[str, str]]:
        samples: list[dict[str, str]] = []
        for row in rows:
            command = str(row.get("命令") or row.get("command") or "").strip()
            if not command:
                continue
            lowered = command.lower()
            if any(token in lowered for token in ("\u001b", "tmux", "codex", "claude")):
                continue
            samples.append(
                {
                    "user": str(row.get("用户") or row.get("user") or "").strip(),
                    "asset": str(row.get("资产") or row.get("asset") or "").strip(),
                    "command": command,
                }
            )
            if len(samples) >= limit:
                break
        return samples

    def _jumpserver_sample_operations(self, rows: list[dict[str, Any]], limit: int = 8) -> list[dict[str, str]]:
        samples: list[dict[str, str]] = []
        for row in rows[:limit]:
            samples.append(
                {
                    "user": str(row.get("用户") or row.get("user") or "").strip(),
                    "action": str(row.get("动作") or row.get("action") or "").strip(),
                    "resource_type": str(row.get("资源类型") or row.get("resource_type") or "").strip(),
                    "resource": str(row.get("资源") or row.get("resource") or "").strip(),
                    "event_time": str(row.get("日期") or row.get("event_time") or "").strip(),
                }
            )
        return samples

    def _jumpserver_account_focus(self, account: dict[str, Any]) -> str:
        user = str(account.get("user") or "unknown")
        commands = account.get("representative_commands", []) if isinstance(account.get("representative_commands"), list) else []
        command_blob = " ".join(str(item) for item in commands).lower()
        judgement = str(account.get("judgement") or "").strip()

        if any("/tmp/" in command.lower() or "./" in command.lower() for command in commands):
            return f"{user} 的 /tmp 二进制上传与执行链"
        if "cast send --private-key" in command_blob or "--private-key" in command_blob:
            return f"{user} 的 curl|bash / 明文私钥调用链"
        if "hot-upgrade" in command_blob:
            return f"{user} 的热升级与多节点变更链"
        if "patch.sh" in command_blob or "installer" in command_blob or "setup_downloader.tar" in command_blob:
            return f"{user} 的多主机安装 / 补丁分发链"
        if "witness-generator" in command_blob or "test_validator.sh" in command_blob:
            return f"{user} 的内部二进制替换与测试验证链"
        if "rsync" in command_blob or "scp" in command_blob:
            return f"{user} 的跨主机同步与服务切换链"
        if "管理平面" in judgement or user.lower() in {"administrator(admin)", "admin", "administrator"}:
            return f"{user} 的高影响管理平面创建 / 授权 / 导出链"
        return f"{user} 的高风险操作链"

    def _jumpserver_dynamic_conclusion(
        self,
        *,
        login_summary: dict[str, Any],
        command_summary: dict[str, Any],
        transfer_summary: dict[str, Any],
        operation_summary: dict[str, Any],
        accounts: list[dict[str, Any]],
        risk_classification: dict[str, Any],
    ) -> str:
        command_labels = command_summary.get("high_risk_action_labels", {}) if isinstance(command_summary.get("high_risk_action_labels"), dict) else {}
        signal_phrases: list[str] = []

        if int(transfer_summary.get("total_rows", 0) or 0) > 0:
            signal_phrases.append("二进制投放与执行")
        if int(command_labels.get("服务控制", 0) or 0) > 0:
            signal_phrases.append("服务启停")
        if int(command_labels.get("远程/横向操作", 0) or 0) > 0:
            signal_phrases.append("跨主机传输")
        if int(command_labels.get("明文敏感参数", 0) or 0) > 0:
            signal_phrases.append("明文敏感参数调用")
        if int(operation_summary.get("host_or_account_creation", 0) or 0) > 0:
            signal_phrases.append("主机/账号创建")
        if int(operation_summary.get("authorization_updates", 0) or 0) > 0:
            signal_phrases.append("资产授权调整")
        if int(operation_summary.get("export_actions", 0) or 0) > 0:
            signal_phrases.append("日志导出行为")

        if not signal_phrases:
            signal_phrases = ["高风险运维操作", "管理平面高影响变更"]

        joined = "、".join(signal_phrases[:7])
        if str(risk_classification.get("overall_level") or "").startswith("confirmed"):
            boundary = "当前证据已经不再只是高风险运维背景，而是更接近需要立即响应的安全事件。"
        else:
            boundary = "整体风险画像更接近“高权限运维动作密集 + 管理平面高影响变更 + 原始审计标签失真 + 需要会话级复核”的场景，而非已经闭环确认的外部攻击事件。"

        return (
            "本批 JumpServer 审计样本未发现足以直接判定“外部入侵已成立”的强证据，"
            f"但已明显暴露出{joined}。"
            f"{boundary}"
        )

    def _structured_section(
        self,
        title: str,
        *,
        paragraphs: list[str] | None = None,
        bullets: list[str] | None = None,
        subsections: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        return {
            "title": title,
            "paragraphs": paragraphs or [],
            "bullets": bullets or [],
            "subsections": subsections or [],
        }

    def _jumpserver_account_sections(
        self,
        accounts: list[dict[str, Any]],
        operator_counts: dict[str, int] | None = None,
    ) -> list[dict[str, Any]]:
        sections: list[dict[str, Any]] = []
        operator_counts = operator_counts or {}
        for index, account in enumerate(accounts[:8], start=1):
            risk_counts = account.get("risk_counts", {}) if isinstance(account.get("risk_counts"), dict) else {}
            bullets: list[str] = []
            user = str(account.get("user") or "unknown")
            has_host_commands = bool(account.get("representative_commands"))
            has_control_plane = user in operator_counts
            if user.lower() in {"administrator(admin)", "admin", "administrator"}:
                bullets.append("风险范围：管理平面")
            elif has_host_commands and has_control_plane:
                bullets.append("风险范围：主机执行 + 管理平面背景")
            elif has_host_commands:
                bullets.append("风险范围：主机执行")
            elif has_control_plane:
                bullets.append("风险范围：管理平面")
            if risk_counts:
                interesting = []
                labels = {
                    "privilege_escalation": "提权",
                    "service_control": "服务控制",
                    "file_replace": "删除/替换",
                    "permission_relaxation": "权限变更",
                    "lateral_movement": "远程/横向操作",
                    "download_and_execute": "下载执行",
                    "binary_execution": "本地执行",
                    "runner_driven_batch_change": "批量发布/补丁分发",
                }
                for key in (
                    "privilege_escalation",
                    "service_control",
                    "file_replace",
                    "permission_relaxation",
                    "lateral_movement",
                    "download_and_execute",
                    "binary_execution",
                    "runner_driven_batch_change",
                ):
                    count = int(risk_counts.get(key, 0) or 0)
                    if count:
                        interesting.append(f"{labels[key]}约 {count} 次")
                if interesting:
                    bullets.append("风险特征（去噪后近似统计）：")
                    bullets.extend(f"  - {item}" for item in interesting)
            assets = account.get("assets", []) if isinstance(account.get("assets"), list) else []
            if assets:
                bullets.append("主要资产：")
                bullets.extend(f"  - {item}" for item in assets[:8])
            commands = account.get("representative_commands", []) if isinstance(account.get("representative_commands"), list) else []
            if commands:
                bullets.append("代表动作与命令：" if any("/tmp/" in command.lower() for command in commands) else "代表命令：")
                bullets.extend(f"  - {item}" for item in commands[:10])
            judgement = str(account.get("judgement") or "").strip()
            if judgement:
                bullets.append(f"判断：{judgement}")
            sections.append(
                self._structured_section(
                    f"5.{index} {user}",
                    bullets=bullets,
                )
            )
        return sections

    def _jumpserver_composite_payload(
        self,
        event: NormalizedEvent,
        findings: list[Finding],
    ) -> dict[str, Any]:
        data = event.normalized_data
        login_summary = data.get("login_summary", {}) if isinstance(data.get("login_summary"), dict) else {}
        command_summary = data.get("command_summary", {}) if isinstance(data.get("command_summary"), dict) else {}
        transfer_summary = data.get("file_transfer_summary", {}) if isinstance(data.get("file_transfer_summary"), dict) else {}
        operation_summary = data.get("operation_summary", {}) if isinstance(data.get("operation_summary"), dict) else {}
        correlations = data.get("cross_source_correlations", []) if isinstance(data.get("cross_source_correlations"), list) else []
        accounts = data.get("high_risk_accounts", []) if isinstance(data.get("high_risk_accounts"), list) else []
        evidence_provenance = data.get("evidence_provenance", []) if isinstance(data.get("evidence_provenance"), list) else []
        risk_classification = data.get("risk_classification", {}) if isinstance(data.get("risk_classification"), dict) else {}

        failed_accounts = login_summary.get("top_failed_accounts", []) if isinstance(login_summary.get("top_failed_accounts"), list) else []
        proxy_ips = login_summary.get("proxy_ips", []) if isinstance(login_summary.get("proxy_ips"), list) else []
        command_labels = command_summary.get("high_risk_action_labels", {}) if isinstance(command_summary.get("high_risk_action_labels"), dict) else {}
        top_uploads = transfer_summary.get("top_uploads", []) if isinstance(transfer_summary.get("top_uploads"), list) else []
        operator_counts = operation_summary.get("operator_counts", {}) if isinstance(operation_summary.get("operator_counts"), dict) else {}
        resource_type_counts = operation_summary.get("resource_type_counts", {}) if isinstance(operation_summary.get("resource_type_counts"), dict) else {}
        export_events = operation_summary.get("export_events", []) if isinstance(operation_summary.get("export_events"), list) else []

        leading_correlation = correlations[0] if correlations else {}
        lead_upload = top_uploads[0] if top_uploads else {}
        lead_account = accounts[0] if accounts else {}

        sections: list[dict[str, Any]] = []
        fallback_conclusion = self._jumpserver_dynamic_conclusion(
            login_summary=login_summary,
            command_summary=command_summary,
            transfer_summary=transfer_summary,
            operation_summary=operation_summary,
            accounts=accounts,
            risk_classification=risk_classification,
        )
        fallback_final_bullets: list[str] = []
        if accounts:
            fallback_final_bullets.append("本批样本中最典型的重点链条包括：")
            for index, account in enumerate(accounts[:6], start=1):
                fallback_final_bullets.append(f"  {index}) {self._jumpserver_account_focus(account)}")
        fallback_final_bullets.append(
            "本批样本的最终定性应为：“未发现足以直接确认外部入侵成功的证据，但已发现多组需要重点审计和治理的高风险运维操作链，以及高影响管理平面操作。后续应以用户、资产、命令、会话、文件传输和管理平面变更六个维度进行联合判断，而不能仅依赖 JumpServer 原始风险标签。”"
        )
        if risk_classification.get("why_not_direct_intrusion"):
            fallback_final_bullets.append(str(risk_classification.get("why_not_direct_intrusion")))

        agent_narrative = None
        if self.agent_model_binding:
            agent_narrative = self.agent_model_binding.generate_jumpserver_narrative(
                skill_id="megaeth.identity.jumpserver_multi_source_review",
                event=event,
                fallback_conclusion=fallback_conclusion,
                fallback_judgment_lines=fallback_final_bullets,
            )
        dynamic_conclusion = (
            str(agent_narrative.get("comprehensive_conclusion")).strip()
            if agent_narrative and agent_narrative.get("comprehensive_conclusion")
            else fallback_conclusion
        )
        final_bullets = (
            [str(item).strip() for item in agent_narrative.get("final_judgment_lines", []) if str(item).strip()]
            if agent_narrative and agent_narrative.get("final_judgment_lines")
            else fallback_final_bullets
        )
        sections.append(
            self._structured_section(
                "综合结论：",
                paragraphs=[dynamic_conclusion],
            )
        )

        basis_subsections: list[dict[str, Any]] = []
        login_bullets = [
            f"最新登录快照共 {int(login_summary.get('total_rows', 0) or 0)} 条记录，其中成功 {int(login_summary.get('success_count', 0) or 0)} 条，失败 {int(login_summary.get('failure_count', 0) or 0)} 条。",
            "失败记录主要集中在用户名/密码错误、OTP 失效或无效，未体现明显分布式爆破或多源异常尝试特征。",
        ]
        if failed_accounts:
            login_bullets.append("登录失败较多的账户主要包括：")
            login_bullets.extend(f"  - {item.get('user')}：{item.get('count')} 次" for item in failed_accounts[:6])
        if proxy_ips:
            login_bullets.append(f"登录 IP 目前主要显示为 {', '.join(str(ip) for ip in proxy_ips[:4])}，更可能是 JumpServer 代理地址，因此不能直接作为攻击源判断依据。")
        basis_subsections.append(self._structured_section("1. 登录侧", bullets=login_bullets))

        command_bullets = [
            f"命令审计共 {int(command_summary.get('total_rows', 0) or 0)} 条，其中混有终端控制字符、tmux 和 Claude/Codex 交互噪声；去噪后可识别有效命令约 {int(command_summary.get('effective_command_count', 0) or 0)} 条。"
        ]
        if command_labels:
            command_bullets.append("去噪后反复出现的高风险语义包括：")
            for label, count in command_labels.items():
                command_bullets.append(f"  - {label}：约 {count} 次")
        command_bullets.append("JumpServer 原始风险等级或接受标签不能作为最终判断依据，需要和真实命令语义分开看。")
        basis_subsections.append(self._structured_section("2. 命令侧", bullets=command_bullets))

        transfer_bullets = [
            f"文件传输日志共 {int(transfer_summary.get('total_rows', 0) or 0)} 条。"
        ]
        if top_uploads:
            highlighted = [
                item for item in top_uploads
                if "/tmp/" in str(item.get("filename") or "").lower() or str(item.get("account") or "").lower() == "root"
            ]
            target = highlighted[0] if highlighted else lead_upload
            if target:
                transfer_bullets.append(
                    f"其中最值得关注的是 {target.get('user') or 'unknown'} 在 {target.get('asset') or 'unknown'} 上，以 {target.get('account') or 'unknown'} 账号上传 {target.get('filename') or 'unknown'}。"
                )
        if leading_correlation:
            chain = leading_correlation.get("correlation_chain", []) if isinstance(leading_correlation.get("correlation_chain"), list) else []
            if chain:
                transfer_bullets.append(f"当前已经形成“{' -> '.join(str(item) for item in chain)}”的高风险操作链。")
        transfer_bullets.append("这类链条应被视为高风险运维/调试样本，并优先进入人工复核。")
        basis_subsections.append(self._structured_section("3. 文件传输侧", bullets=transfer_bullets))

        operation_bullets = [
            f"操作记录日志共 {int(operation_summary.get('total_rows', 0) or 0)} 条。",
            f"其中创建(create) {int(operation_summary.get('create_count', 0) or 0)} 条、更新(update) {int(operation_summary.get('update_count', 0) or 0)} 条、导出(export) {int(operation_summary.get('export_actions', 0) or 0)} 条。",
        ]
        if operator_counts:
            operation_bullets.append("主要操作者：")
            for user, count in sorted(operator_counts.items(), key=lambda item: item[1], reverse=True)[:8]:
                operation_bullets.append(f"  - {user}：{count} 条")
        if resource_type_counts:
            operation_bullets.append("资源类型分布：")
            for resource_type, count in sorted(resource_type_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
                operation_bullets.append(f"  - {resource_type}：{count}")
        if export_events:
            operation_bullets.append("关键管理平面特征包括：")
            for item in export_events[:8]:
                operation_bullets.append(
                    f"  - {item.get('event_time') or '未知时间'} {item.get('user') or 'unknown'} 导出 {item.get('resource_type') or 'unknown'}"
                )
        operation_bullets.append("这些记录可以解释样本导出来源、资产接入和授权配置背景，但不能替代主机侧执行证据。")
        basis_subsections.append(self._structured_section("4. 操作记录侧", bullets=operation_bullets))

        sections.append(self._structured_section("主要依据如下：", subsections=basis_subsections))

        account_subsections = self._jumpserver_account_sections(accounts, operator_counts)
        if not account_subsections:
            account_subsections = [
                self._structured_section(
                    "5.1 当前样本暂未提炼出可直接归档的高危账户画像",
                    bullets=[
                        "风险范围：待继续复核",
                        "判断：当前样本已经呈现多源高风险语义，但还缺少足够稳定的账户级画像，后续应继续结合用户、资产、命令、文件传输和管理平面动作补齐。",
                    ],
                )
            ]
        sections.append(
            self._structured_section(
                "5. 重点高危操作账户与命令汇总",
                subsections=account_subsections,
            )
        )

        provenance_bullets = []
        if evidence_provenance:
            provenance_bullets.append("操作记录日志明确显示，本次登录日志、命令日志、文件传输日志具备导出来源记录。")
            provenance_bullets.extend(
                f"  - {item.get('export_time') or '未知时间'} {item.get('export_user') or 'unknown'} 导出 {item.get('resource_type') or 'unknown'}"
                for item in evidence_provenance[:8]
            )
            provenance_bullets.append("这意味着样本来源链较清晰，后续训练系统可以把 operation_audit.export 作为“证据链完整性”的一个字段学习。")
        else:
            provenance_bullets.append("当前尚未从管理平面完整还原导出来源链，需要继续补齐 operation_audit 证据。")
        sections.append(self._structured_section("6. 证据来源与导出链", bullets=provenance_bullets))

        sections.append(self._structured_section("7. 综合判断", bullets=final_bullets))
        return {
            "sections": sections,
            "dynamic_conclusion": dynamic_conclusion,
            "agent_context": dict(agent_narrative or {}),
        }

    def _evidence(self, findings: list[Finding]) -> list[str]:
        entries: list[str] = []
        for finding in findings:
            for evidence in finding.evidence:
                for key, value in evidence.items():
                    if isinstance(value, list):
                        if not value:
                            continue
                        entries.append(f"{key}: {', '.join(str(item) for item in value[:4])}")
                    else:
                        entries.append(f"{key}: {value}")
        return entries[:6]

    def _actions(self, findings: list[Finding]) -> list[str]:
        out: list[str] = []
        for finding in findings:
            for action in finding.recommendations:
                if action not in out:
                    out.append(action)
        return out[:8]

    def _appsec_analysis(self, event: NormalizedEvent, findings: list[Finding]) -> dict[str, object]:
        scope = event.normalized_data.get("scan_scope", {})
        repo_name = str(scope.get("repo_name") or event.asset_context.get("asset_name") or "目标应用")
        target_url = str(scope.get("target_url") or event.asset_context.get("target_url") or "").strip()
        validated = []
        candidates = []
        for item in event.normalized_data.get("validated_findings", []) if isinstance(event.normalized_data.get("validated_findings"), list) else []:
            if not isinstance(item, dict):
                continue
            if str(item.get("proof_status") or "").lower() == "validated":
                validated.append(item)
            else:
                candidates.append(item)
        actions = event.normalized_data.get("priority_actions", []) if isinstance(event.normalized_data.get("priority_actions"), list) else []
        if event.event_type == "whitebox_recon_assessment":
            surfaces = event.normalized_data.get("attack_surfaces", [])
            paths = event.normalized_data.get("candidate_paths", [])
            patterns = event.normalized_data.get("exposed_patterns", [])
            return {
                "assessment": "这份材料属于应用白盒侦察结果，当前重点不是确认漏洞已经成立，而是明确哪些入口、鉴权边界和高风险路径值得进入下一轮验证。",
                "likely_issue": bool(findings),
                "verdict": "whitebox_recon_review",
                "key_facts": [
                    f"系统已将目标识别为应用白盒侦察输入，当前分析对象为 {repo_name}。"
                    + (f" 目标地址为 {target_url}。" if target_url else ""),
                    f"当前共整理出 {len(surfaces) if isinstance(surfaces, list) else 0} 类攻击面线索，以及 {len(paths) if isinstance(paths, list) else 0} 条优先验证路径。",
                    f"主要暴露模式包括：{('、'.join(str(item) for item in patterns[:3])) if isinstance(patterns, list) and patterns else '鉴权覆盖不足、输入边界不清晰、关键入口需要继续验证'}。",
                ],
                "probable_causes": [
                    "应用的路由、鉴权中间件和输入处理路径之间存在覆盖不均衡。",
                    "代码结构显示高风险入口集中，但还需要下一阶段验证是否能够形成真实可利用问题。",
                ],
                "why_flagged": "系统将仓库路径、目标地址和白盒侦察结果识别为应用安全侦察输入，因此先输出攻击面与优先验证范围。",
                "report_gaps": [
                    "当前阶段还没有形成足够的可利用证据，不能直接把所有侦察线索升级为已确认漏洞。",
                ],
                "quick_checks": [
                    "优先进入 validate 阶段，针对高风险入口做 exploit validation。",
                    "结合鉴权边界和高风险参数，缩小下一轮验证范围。",
                ],
                "escalation_conditions": [
                    "如果下一阶段确认存在可复现利用路径，应升级为应用安全问题并进入修复闭环。",
                ],
                "professional_judgment": "我的判断是：这类结果应被视为白盒应用安全侦察结论，而不是最终漏洞报告。当前重点在于帮助后续验证聚焦。",
            }
        if event.event_type == "whitebox_exploit_validation":
            return {
                "assessment": "这份材料属于白盒安全验证结果，重点在于区分哪些利用路径已经被确认，哪些还只是候选风险。",
                "likely_issue": bool(validated) or any(f.risk_level >= 4 for f in findings),
                "verdict": "whitebox_validation_review",
                "key_facts": [
                    f"当前分析对象为 {repo_name}。"
                    + (f" 目标地址为 {target_url}。" if target_url else ""),
                    f"已确认利用路径 {len(validated)} 条，待继续复核的候选问题 {len(candidates)} 条。",
                    "这一步的价值在于把白盒侦察阶段的大量线索，压缩成少量更接近真实风险的验证结果。",
                ],
                "probable_causes": [
                    "关键管理接口、输入边界或鉴权链存在薄弱路径。",
                    "部分问题已具备可复现性，说明风险不只是代码味道，而是更接近真实应用安全缺陷。",
                ],
                "why_flagged": "系统识别到该输入属于白盒 exploit validation 结果，因此输出验证导向的结论。",
                "report_gaps": [
                    "仍需要补充更完整的上下文，包括影响范围、修复复杂度和回归方式。",
                ],
                "quick_checks": [
                    "优先把已确认问题转成修复项与回归项。",
                    "对候选问题保留最小复现信息，便于继续验证。",
                ],
                "escalation_conditions": [
                    "如果已确认利用路径涉及管理面、认证、数据越权或外部输入执行，应直接升级为高优先级应用安全问题。",
                ],
                "professional_judgment": "我的判断是：validate 阶段的结果已经比侦察结论更接近可执行治理项，尤其是 proof_status 为 validated 的问题，应尽快进入修复闭环。",
            }
        return {
            "assessment": "这份材料属于白盒应用安全综合报告，重点在于把侦察与验证结果收敛成一份更适合交付和治理的结论。",
            "likely_issue": bool(validated) or any(f.risk_level >= 4 for f in findings),
            "verdict": "whitebox_security_assessment",
            "key_facts": [
                f"当前综合报告针对 {repo_name} 输出。"
                + (f" 目标地址为 {target_url}。" if target_url else ""),
                f"已确认问题 {len(validated)} 条，候选问题 {len(candidates)} 条，当前重点行动建议 {len(actions)} 条。",
                "这类结果比目录型输入更接近真实治理材料，适合直接进入应用安全修复与回归计划。",
            ],
            "probable_causes": [
                "应用在鉴权边界、输入处理和敏感路径控制上存在实际薄弱点。",
                "白盒侦察与验证结果已经形成闭环，因此可以输出更稳定的综合判断。",
            ],
            "why_flagged": "系统识别到当前输入属于应用安全综合白盒结果，因此按交付型安全报告语境组织内容。",
            "report_gaps": [
                "当前仍可继续补充更细粒度的业务影响分析与修复优先级解释。",
            ],
            "quick_checks": [
                "优先修复已确认且高优先级的问题，再安排候选问题复核。",
                "把本轮白盒结果转成发布前回归清单和长期检测规则。",
            ],
            "escalation_conditions": [
                "如果已确认问题涉及管理接口、越权、敏感数据读取或外部输入执行，应升级为发布阻断级问题。",
            ],
            "professional_judgment": "我的判断是：这类白盒综合报告已经可以作为应用安全治理输入。后续重点不再是继续扩大侦察范围，而是收敛修复、验证和回归。",
        }

    def _host_analysis(self, event: NormalizedEvent, findings: list[Finding]) -> dict[str, object]:
        rows = event.normalized_data.get("rows", [])
        row_count = len(rows) if isinstance(rows, list) else 0
        severe = 0
        service = 0
        standards: set[str] = set()
        baseline_filesystem: list[str] = []
        baseline_logs: list[str] = []
        baseline_modules: list[str] = []
        if isinstance(rows, list):
            for row in rows:
                if not isinstance(row, dict):
                    continue
                try:
                    score = int(float(str(row.get("风险评分") or "0")))
                except ValueError:
                    score = 0
                title = str(row.get("发现名称") or row.get("\ufeff发现名称") or "")
                if score >= 95:
                    severe += 1
                if any(token in title.lower() for token in ("ssh", "telnet", "rsync", "icmp", "openssh", "rds", "printer")):
                    service += 1
                lowered = title.lower()
                if "/var/log/audit" in lowered:
                    baseline_filesystem.append(title)
                if any(token in title for token in ("日志文件的权限未配置", "日志权限未正确配置", "未安装 auditd")):
                    baseline_logs.append(title)
                if any(token in lowered for token in ("cramfs", "udf")):
                    baseline_modules.append(title)
                for item in str(row.get("合规标准") or "").split(","):
                    item = item.strip()
                    if item:
                        standards.add(item)
        if event.event_type == "host_baseline_assessment":
            environment = str(event.asset_context.get("environment") or "unknown")
            asset_name = str(event.asset_context.get("asset_name") or "该主机")
            role = str(event.asset_context.get("host_role") or event.asset_context.get("asset_role") or event.asset_context.get("role") or "")
            higher_risk = environment == "production" or role in {"sequencer", "signing_service", "signing service"}
            category_labels = {
                "filesystem_isolation_issue": "文件系统隔离配置",
                "temporary_directory_configuration": "临时目录配置",
                "log_permission_configuration": "日志权限配置",
                "unused_filesystem_modules": "不必要文件系统模块",
            }
            ordered_categories = list(
                dict.fromkeys(
                    category_labels[f.risk_type]
                    for f in findings
                    if f.risk_type in category_labels
                )
            )
            category_summary = "、".join(ordered_categories) if ordered_categories else "主机安全基线配置"
            return {
                "assessment": "本次分析识别出一组主机安全基线配置弱点，重点集中在文件系统隔离、临时目录配置、日志权限配置和不必要文件系统模块。这类问题属于系统安全基线配置风险，并不表示主机已经遭受攻击，但在生产环境中会直接扩大攻击面并提高治理优先级。",
                "likely_issue": True,
                "verdict": "baseline_configuration_weakness",
                "key_facts": [
                    f"系统已将这份材料识别为主机安全基线评估，共解析出 {row_count} 条记录；当前判断它属于 Host Baseline Security Assessment，而不是 Security Incident。",
                    f"当前聚合出的关键问题为：{category_summary}。",
                    f"当前主机环境为 {environment}，资产名称为 {asset_name}。"
                    + (f" 角色标记为 {role}，因此应提升治理优先级。" if role else ""),
                    "这些结果更像配置弱点与基线缺口，而不是已经确认的入侵行为。"
                    + (" 由于当前环境或角色更关键，整体风险应从中风险上调关注。" if higher_risk else ""),
                ],
                "probable_causes": [
                    "主机镜像、初始化模板或基线加固流程中没有完成分区、日志和模块层面的统一收敛。",
                    "运维基线与真实环境之间存在偏差，导致部分目录权限、挂载选项和模块禁用策略没有真正落地。",
                    "在容器化环境、共享日志分区或已存在额外补偿措施时，个别项也可能属于可接受偏差，因此仍需结合实际环境做二次确认。",
                ],
                "why_flagged": "材料中的列名、风险评分模式与命名方式符合 Risk Analytics / Host Baseline Scanner 报告特征，并且包含典型的主机基线弱点项。",
                "report_gaps": [
                    "当前材料没有直接说明这些问题是否已经在目标主机上完成修复或接受补偿措施。",
                    "当前材料没有说明受影响主机是否属于容器环境、共享日志设计或带额外防护的特例场景。",
                ],
                "quick_checks": [
                    "确认 /var/log/audit 是否已经使用独立分区，避免日志耗尽进一步影响系统盘稳定性。",
                    "检查 /var/tmp 等临时目录是否启用了 nodev、nosuid、noexec 挂载参数。",
                    "确认日志权限是否已收紧到合适范围，并检查 cramfs、udf 等未使用文件系统模块是否已经禁用。",
                ],
                "escalation_conditions": [
                    "如果该主机处于 production 环境，应将这类基线缺口提升为优先治理项。",
                    "如果该主机承担 sequencer、signing service 等关键角色，应将整体风险提升到更高治理优先级。",
                    "如果这些配置弱点与外部暴露、弱权限或监控缺失叠加出现，应升级为系统性主机风险。",
                ],
                "professional_judgment": "我的判断是：这类结果属于主机安全基线配置风险，而不是 Security Incident。默认应按中风险处理；如果环境为 production，或主机承担 Sequencer、Signing Service、核心生产服务等关键角色，再提升到高优先级。",
            }
        return {
            "assessment": "这份材料反映的不是单点噪音，而是一批真实存在的主机基线与服务暴露风险。",
            "likely_issue": True,
            "verdict": "confirmed_posture_risk",
            "key_facts": [
                f"这是一份主机基线 / 加固风险清单，共包含 {row_count} 条风险记录。",
                f"其中 {severe} 条记录的风险评分在 95 分及以上，说明存在大量高优先级整改项。",
                f"至少 {service} 条记录涉及 SSH、远程访问或网络暴露等服务侧风险。",
                f"这些风险同时映射到了 {min(len(standards), 8)} 个合规或审计标准，影响面较广。",
            ],
            "probable_causes": [
                "受影响主机存在长期未完成的基线加固项，导致高风险配置持续暴露。",
                "同一套系统镜像或初始化模板可能在多台资产上继承了相同的安全缺口。",
                "审计与完整性监控组件缺失，说明主机监测基线本身也存在不足。",
            ],
            "why_flagged": "系统识别到这份材料是主机风险分析/加固清单，并从中提炼出高风险基线缺口与服务暴露问题。",
            "report_gaps": [],
            "quick_checks": [
                "优先核对前 10 条最高分风险项是否仍然处于活动状态，并确认受影响资产范围。",
                "检查 SSH、telnet、rsync、ICMP 重定向等远程访问相关项，确认是否暴露在不受控网络边界。",
                "确认 auditd、AIDE、日志权限、关键分区挂载选项等基线控制是否已经具备统一修复计划。",
            ],
            "escalation_conditions": [
                "如果这些基线缺口覆盖生产核心主机或跳板机，应立即按高优先级整改推进。",
                "如果远程访问、弱协议或默认端口暴露同时出现在外网可达资产上，应提升为外部暴露事件。",
                "如果审计、日志、完整性监控缺失与高危服务暴露叠加出现，应升级为系统性主机安全风险。",
            ],
            "professional_judgment": "从主机安全视角看，这更像一份需要分批治理的高风险基线缺口清单，而不是误报。",
        }

    def _generic_analysis(self, event: NormalizedEvent, findings: list[Finding]) -> dict[str, object]:
        if event.source_type == "easm" or event.event_type in {"external_asset", "service_exposure", "tls_analysis", "easm_asset_assessment"}:
            assessments = event.normalized_data.get("asset_assessments", []) if isinstance(event.normalized_data.get("asset_assessments"), list) else []
            if event.event_type == "easm_asset_assessment" and assessments:
                return self._easm_analysis(event, findings)
            row_count = len(event.normalized_data.get("rows", [])) if isinstance(event.normalized_data.get("rows"), list) else int(event.normalized_data.get("row_count", 0) or 0)
            return {
                "report_title": "EASM 单源材料审查报告",
                "report_template": "easm_single_source_review_v1",
                "assessment": "这份材料属于外部攻击面单源输入，当前价值在于提供资产、端口、证书或 DNS 线索，适合纳入后续多文件关联，而不是单独给出过强结论。",
                "likely_issue": any(f.risk_level >= 4 for f in findings),
                "verdict": "easm_single_source_review",
                "key_facts": [
                    f"当前材料共包含 {row_count} 条记录，事件类型为 {event.event_type}。",
                    "单源 EASM 输入更适合当作资产线索层，而不是最终综合评估结果。",
                ],
                "probable_causes": ["当前仅上传了单一层数据，尚不足以形成完整的跨层边界判断。"],
                "why_flagged": "系统识别到这是 EASM 相关材料，因此保留为外部攻击面线索并等待进一步关联。",
                "report_gaps": ["需要继续补充 DNS、证书、ASN、IP 段或服务层数据，才能形成更稳定的资产评估。"],
                "quick_checks": ["建议把同一批外部资产材料一起上传，触发综合 EASM 评估。"],
                "escalation_conditions": ["只有当多层数据形成一致边界信号时，才应升级为外部暴露治理项。"],
                "professional_judgment": "单源 EASM 材料更适合作为后续综合分析输入，而不是独立结论。",
            }
        if event.event_type == "integration_catalog":
            rows = event.normalized_data.get("rows", [])
            row_count = len(rows) if isinstance(rows, list) else 0
            return {
                "assessment": "这份材料更像安全平台中的目录或配置观测结果，本身不代表已经发现真实安全事件。",
                "likely_issue": False,
                "verdict": "informational_platform_observation",
                "key_facts": [
                    f"系统识别到这是一份来自外部安全平台的目录型材料，共包含 {row_count} 条记录。",
                    "这类输入更适合先作为平台上下文、资产线索或后续调查入口，而不是直接当作告警本身。",
                ],
                "probable_causes": [
                    "当前导入的是控制台中的报表目录、能力目录或管理视图，而不是具体威胁事件。",
                ],
                "why_flagged": "系统识别到这是来自集成平台的观测材料，因此先纳入平台上下文，而不是直接升级为安全事件。",
                "report_gaps": [],
                "quick_checks": [
                    "确认这些目录项中是否存在可进一步导出的真实扫描结果、事件报表或终端明细。",
                    "优先继续拉取带有详细结果的数据，而不是停留在目录层。",
                ],
                "escalation_conditions": [
                    "只有当后续导出的结果中包含真实告警、异常终端或高风险报表内容时，才应升级为安全事件分析。",
                ],
                "professional_judgment": "当前更像一份可继续下钻的平台目录观测，而不是已经确认的问题。",
            }
        if event.event_type == "endpoint_inventory":
            rows = event.normalized_data.get("rows", [])
            row_count = len(rows) if isinstance(rows, list) else 0
            managed_total = int(event.normalized_data.get("managed_total", 0) or 0)
            unmanaged_total = int(event.normalized_data.get("unmanaged_total", 0) or 0)
            groups_traversed = int(event.normalized_data.get("groups_traversed", 0) or 0)
            return {
                "assessment": "这份材料是 Bitdefender 资产树中的终端盘点结果，更适合用来确认设备覆盖面、管理状态和后续调查范围。",
                "likely_issue": False,
                "verdict": "informational_endpoint_inventory",
                "key_facts": [
                    f"系统递归遍历了 {groups_traversed} 个资产分组，共发现 {row_count} 台设备。",
                    f"其中 {managed_total} 台是受管设备，{unmanaged_total} 台是未受管或当前未生效策略的设备。",
                    "这份结果比公开 getEndpointsList 更接近控制台里的真实设备规模。",
                ],
                "probable_causes": [
                    "公开终端枚举接口没有返回完整设备列表，因此需要通过资产树递归下钻来还原真实设备覆盖范围。",
                ],
                "why_flagged": "系统识别到这是终端资产清单导入，而不是安全事件本身。",
                "report_gaps": [],
                "quick_checks": [
                    "优先检查未受管设备是否属于应受控但未成功纳管的资产。",
                    "将这份设备清单与最新安全报表中的主机做交叉映射，确认哪些设备已有安全记录但管理状态异常。",
                ],
                "escalation_conditions": [
                    "如果核心服务器或办公终端出现在未受管设备列表中，应升级为资产纳管风险。",
                ],
                "professional_judgment": "这条链更适合作为资产与终端覆盖基线，而不是直接判断攻击事件。",
            }
        if event.event_type in {"jumpserver_multi_source_audit", "login_auth_review", "jumpserver_command_review", "jumpserver_transfer_review", "jumpserver_operation_review"}:
            login_summary = event.normalized_data.get("login_summary", {}) if isinstance(event.normalized_data.get("login_summary"), dict) else {}
            command_summary = event.normalized_data.get("command_summary", {}) if isinstance(event.normalized_data.get("command_summary"), dict) else {}
            transfer_summary = event.normalized_data.get("file_transfer_summary", {}) if isinstance(event.normalized_data.get("file_transfer_summary"), dict) else {}
            operation_summary = event.normalized_data.get("operation_summary", {}) if isinstance(event.normalized_data.get("operation_summary"), dict) else {}
            rows = [row for row in event.normalized_data.get("rows", []) if isinstance(row, dict)] if isinstance(event.normalized_data.get("rows"), list) else []
            if event.event_type == "login_auth_review" and not login_summary:
                login_summary = summarize_login_rows(rows)
            if event.event_type == "jumpserver_command_review" and not command_summary:
                command_summary = summarize_command_rows(rows)
            if event.event_type == "jumpserver_transfer_review" and not transfer_summary:
                transfer_summary = summarize_transfer_rows(rows)
            if event.event_type == "jumpserver_operation_review" and not operation_summary:
                operation_summary = summarize_operation_rows(rows)
            correlations = event.normalized_data.get("cross_source_correlations", []) if isinstance(event.normalized_data.get("cross_source_correlations"), list) else []
            accounts = event.normalized_data.get("high_risk_accounts", []) if isinstance(event.normalized_data.get("high_risk_accounts"), list) else []
            risk_classification = event.normalized_data.get("risk_classification", {}) if isinstance(event.normalized_data.get("risk_classification"), dict) else {}
            if event.event_type == "login_auth_review":
                fallback = {
                    "report_title": "JumpServer 登录审计报告",
                    "report_template": "jumpserver_login_review_v1",
                    "assessment": "这份材料是 JumpServer 登录认证快照，主要价值在于提供登录成功/失败、MFA 异常和代理地址语义，不能单独当成攻击成立依据。",
                    "likely_issue": any(f.risk_level >= 3 for f in findings),
                    "verdict": "jumpserver_login_review",
                    "key_facts": [
                        f"当前登录快照中成功 {int(login_summary.get('success_count', 0) or 0)} 条，失败 {int(login_summary.get('failure_count', 0) or 0)} 条。",
                        "失败登录需要结合 OTP 失效、用户名/密码错误和代理地址语义再判断，而不是直接判定为爆破。",
                    ],
                    "probable_causes": [
                        "JumpServer 登录失败记录可能包含过期 OTP、MFA 配置问题或普通口令错误。",
                    ],
                    "why_flagged": "系统识别到这是 JumpServer 登录侧材料，适合用于会话背景和账号异常判断。",
                    "report_gaps": ["单独的登录快照不足以支撑入侵结论，需要结合命令和文件传输侧进一步关联。"],
                    "quick_checks": ["优先确认失败账户是否集中于已知代理地址，以及是否伴随命令侧高危行为。"],
                    "escalation_conditions": ["如果同一用户在短时间内伴随文件投放、提权和执行链，应提升为多源高风险会话。"],
                    "professional_judgment": "登录侧更多用于提供背景和边界条件，不能脱离命令与传输链单独定性。",
                }
                if self.agent_model_binding:
                    compact_context = {
                        "login_summary": login_summary,
                    }
                    agent_narrative = self.agent_model_binding.generate_jumpserver_single_source_narrative(
                        skill_id="megaeth.identity.anomalous_access_review",
                        event=event,
                        compact_context=compact_context,
                        fallback_assessment=fallback["assessment"],
                        fallback_key_facts=list(fallback["key_facts"]),
                        fallback_professional_judgment=fallback["professional_judgment"],
                    )
                    if agent_narrative:
                        fallback["assessment"] = str(agent_narrative.get("assessment") or fallback["assessment"])
                        fallback["key_facts"] = list(agent_narrative.get("key_facts") or fallback["key_facts"])
                        fallback["professional_judgment"] = str(agent_narrative.get("professional_judgment") or fallback["professional_judgment"])
                        fallback["agent_context"] = dict(agent_narrative)
                return fallback
            if event.event_type == "jumpserver_command_review":
                fallback = {
                    "report_title": "JumpServer 命令审计报告",
                    "report_template": "jumpserver_command_review_v1",
                    "assessment": "这份材料是 JumpServer 命令审计结果，重点不在于单条 sudo 或 systemctl，而在于去噪后是否出现提权、服务控制、下载执行、跨主机操作和敏感参数暴露的连续链条。",
                    "likely_issue": any(f.risk_level >= 3 for f in findings),
                    "verdict": "jumpserver_command_review",
                    "key_facts": [
                        f"当前命令审计共 {int(command_summary.get('total_rows', 0) or 0)} 条，去噪后有效命令约 {int(command_summary.get('effective_command_count', 0) or 0)} 条。",
                        "高风险命令语义通常需要按用户、资产和时间窗做串联判断，而不是按单条命令告警理解。",
                    ],
                    "probable_causes": [
                        "高权限运维、批量发布、调试修复或跨主机维护动作集中出现。",
                    ],
                    "why_flagged": "系统识别到这是 JumpServer 命令侧材料，适合用于提权、服务启停、下载执行和横向操作的复核。",
                    "report_gaps": ["仅凭命令审计还不足以还原完整会话，需要继续结合登录、文件传输和管理平面侧证据。"],
                    "quick_checks": ["优先复核下载执行、跨主机同步、服务启停和权限放开命令链。"],
                    "escalation_conditions": ["如果命令侧和文件传输、登录异常、管理平面导出/授权动作形成闭环，应升级为多源高风险会话。"],
                    "professional_judgment": "命令侧是识别高风险运维链的核心材料，但仍需要结合其他日志源才能完成定性。",
                }
                if self.agent_model_binding:
                    compact_context = {
                        "command_summary": command_summary,
                        "sample_commands": self._jumpserver_sample_commands(rows),
                    }
                    agent_narrative = self.agent_model_binding.generate_jumpserver_single_source_narrative(
                        skill_id="megaeth.identity.jumpserver_command_review",
                        event=event,
                        compact_context=compact_context,
                        fallback_assessment=fallback["assessment"],
                        fallback_key_facts=list(fallback["key_facts"]),
                        fallback_professional_judgment=fallback["professional_judgment"],
                    )
                    if agent_narrative:
                        fallback["assessment"] = str(agent_narrative.get("assessment") or fallback["assessment"])
                        fallback["key_facts"] = list(agent_narrative.get("key_facts") or fallback["key_facts"])
                        fallback["professional_judgment"] = str(agent_narrative.get("professional_judgment") or fallback["professional_judgment"])
                        fallback["agent_context"] = dict(agent_narrative)
                return fallback
            if event.event_type == "jumpserver_transfer_review":
                fallback = {
                    "report_title": "JumpServer 文件传输审计报告",
                    "report_template": "jumpserver_transfer_review_v1",
                    "assessment": "这份材料是 JumpServer 文件传输审计结果，重点在于识别 /tmp 投放、root 账号上传、二进制落地与后续执行链，而不是把单次上传直接判成恶意载荷。",
                    "likely_issue": any(f.risk_level >= 3 for f in findings),
                    "verdict": "jumpserver_transfer_review",
                    "key_facts": [
                        f"当前文件传输共 {int(transfer_summary.get('total_rows', 0) or 0)} 条，其中上传 {int(transfer_summary.get('upload_count', 0) or 0)} 条、下载 {int(transfer_summary.get('download_count', 0) or 0)} 条。",
                        f"其中高风险上传 {int(transfer_summary.get('high_risk_upload_count', 0) or 0)} 条，重点关注 /tmp、root 账号和可执行二进制。",
                    ],
                    "probable_causes": [
                        "调试工具投放、临时二进制执行、补丁传输或运维维护动作集中出现。",
                    ],
                    "why_flagged": "系统识别到这是 JumpServer 文件传输侧材料，适合用于追踪文件投放、落地和后续执行链。",
                    "report_gaps": ["仅凭文件传输日志还无法确认文件是否执行成功，需要继续结合命令侧和会话证据。"],
                    "quick_checks": ["优先核实高风险上传文件是否被移动、放权、执行以及是否存在外联验证动作。"],
                    "escalation_conditions": ["如果文件传输与后续 chmod、./binary、curl/telnet 等动作形成连续链，应升级为高风险操作链。"],
                    "professional_judgment": "文件传输侧更多提供载荷投放和落地线索，真正的定性仍需要结合命令和会话背景。",
                }
                if self.agent_model_binding:
                    compact_context = {
                        "transfer_summary": transfer_summary,
                        "sample_uploads": list((transfer_summary.get("top_uploads") or [])[:8]),
                    }
                    agent_narrative = self.agent_model_binding.generate_jumpserver_single_source_narrative(
                        skill_id="megaeth.identity.jumpserver_transfer_review",
                        event=event,
                        compact_context=compact_context,
                        fallback_assessment=fallback["assessment"],
                        fallback_key_facts=list(fallback["key_facts"]),
                        fallback_professional_judgment=fallback["professional_judgment"],
                    )
                    if agent_narrative:
                        fallback["assessment"] = str(agent_narrative.get("assessment") or fallback["assessment"])
                        fallback["key_facts"] = list(agent_narrative.get("key_facts") or fallback["key_facts"])
                        fallback["professional_judgment"] = str(agent_narrative.get("professional_judgment") or fallback["professional_judgment"])
                        fallback["agent_context"] = dict(agent_narrative)
                return fallback
            if event.event_type == "jumpserver_operation_review":
                fallback = {
                    "report_title": "JumpServer 管理平面审计报告",
                    "report_template": "jumpserver_operation_review_v1",
                    "assessment": "这份材料是 JumpServer 管理平面操作记录，主要用于解释导出、授权、主机/账号创建和会话建立等背景动作，不能替代主机侧执行证据。",
                    "likely_issue": any(f.risk_level >= 3 for f in findings),
                    "verdict": "jumpserver_operation_review",
                    "key_facts": [
                        f"当前共记录 {int(operation_summary.get('total_rows', 0) or 0)} 条管理平面动作。",
                        f"其中导出 {int(operation_summary.get('export_actions', 0) or 0)} 条，授权/更新 {int(operation_summary.get('authorization_updates', 0) or 0)} 条，主机/账号创建 {int(operation_summary.get('host_or_account_creation', 0) or 0)} 条，会话创建 {int(operation_summary.get('session_creation', 0) or 0)} 条。",
                        "这些动作更适合作为主机侧高危行为的背景解释，而不是直接证明入侵。",
                    ],
                    "probable_causes": [
                        "资产授权、审计导出、主机接入和管理动作集中发生。",
                    ],
                    "why_flagged": "系统识别到这是 JumpServer 的管理平面日志，适合用于解释样本来源和管理动作背景。",
                    "report_gaps": ["仅凭管理平面日志无法替代命令执行、文件上传和登录侧证据。"],
                    "quick_checks": ["优先确认导出动作、授权调整和主机/账号创建是否处于正常维护窗口。"],
                    "escalation_conditions": ["如果这些管理平面动作与同时间窗内的高危命令和 /tmp 二进制投放形成连续链，应升级为高风险待复核。"],
                    "professional_judgment": "管理平面动作本身不等于恶意，但它们是解释整条 JumpServer 风险链的重要背景证据。",
                }
                if self.agent_model_binding:
                    compact_context = {
                        "operation_summary": operation_summary,
                        "sample_operations": self._jumpserver_sample_operations(rows),
                    }
                    agent_narrative = self.agent_model_binding.generate_jumpserver_single_source_narrative(
                        skill_id="megaeth.identity.jumpserver_operation_review",
                        event=event,
                        compact_context=compact_context,
                        fallback_assessment=fallback["assessment"],
                        fallback_key_facts=list(fallback["key_facts"]),
                        fallback_professional_judgment=fallback["professional_judgment"],
                    )
                    if agent_narrative:
                        fallback["assessment"] = str(agent_narrative.get("assessment") or fallback["assessment"])
                        fallback["key_facts"] = list(agent_narrative.get("key_facts") or fallback["key_facts"])
                        fallback["professional_judgment"] = str(agent_narrative.get("professional_judgment") or fallback["professional_judgment"])
                        fallback["agent_context"] = dict(agent_narrative)
                return fallback
            if event.event_type == "jumpserver_multi_source_audit":
                composite_payload = self._jumpserver_composite_payload(event, findings)
                structured_sections = list(composite_payload.get("sections") or [])
                dynamic_conclusion = str(composite_payload.get("dynamic_conclusion") or "").strip()
                agent_context = dict(composite_payload.get("agent_context") or {})
                return {
                    "assessment": dynamic_conclusion,
                    "likely_issue": True,
                    "verdict": str(risk_classification.get("overall_level") or "high_risk_pending_review"),
                    "key_facts": [
                        f"登录侧共 {int(login_summary.get('total_rows', 0) or 0)} 条，命令侧共 {int(command_summary.get('total_rows', 0) or 0)} 条，文件传输共 {int(transfer_summary.get('total_rows', 0) or 0)} 条，操作记录共 {int(operation_summary.get('total_rows', 0) or 0)} 条。",
                        f"当前已识别 {len(accounts)} 个高风险账户，以及 {len(correlations)} 条跨源高风险链。",
                        "原始 JumpServer 风险标签不能直接作为最终定性依据。",
                    ],
                    "probable_causes": [
                        "样本同时包含主机执行侧高危动作和管理平面高影响变更，说明环境处于高权限运维密集状态。",
                        "当前更接近高风险运维/调试/发布链，而不是已经闭环确认的外部攻击事件。",
                    ],
                    "why_flagged": "系统识别到同一批 JumpServer 日志在登录、命令、文件传输和管理平面之间形成了可复核的多源关联链。",
                    "report_gaps": [
                        "当前仍需要按用户、资产、会话和时间窗补齐会话级证据，不能只靠单条日志定性。",
                    ],
                    "quick_checks": [
                        "优先复核 /tmp 二进制投放与执行链。",
                        "优先复核高权限发布、补丁分发与跨主机同步链。",
                        "把管理平面变更与主机侧命令执行分开判断，再做会话级合并。",
                    ],
                    "escalation_conditions": [
                        "如果同一用户/资产同时出现上传、放权、执行、外联或服务变更链，应提升为高优先级待处置事件。",
                        "如果管理平面导出、授权和主机侧执行在同一时间窗形成闭环，应升级为高风险会话。",
                    ],
                    "professional_judgment": "这批样本最重要的训练目标，不是自动定罪，而是学会在高风险运维、管理平面高影响变更和真正入侵证据之间保持边界感，并优先标出最需要人工复核的链条。",
                    "structured_sections": structured_sections,
                    "report_title": "JumpServer 综合审计报告",
                    "report_template": "jumpserver_multisource_v2",
                    "agent_context": agent_context,
                }
            return {
                "report_title": "JumpServer 单源审计报告",
                "report_template": "jumpserver_single_source_review_v1",
                "assessment": "本批 JumpServer 审计样本更接近高风险运维、调试与发布链，而不是已被闭环确认的外部入侵事件。重点不在于单条 sudo 或 systemctl，而在于多个日志源是否拼出上传、提权、放权、执行与服务变更的连续链路。",
                "likely_issue": True,
                "verdict": str(risk_classification.get("overall_level") or "high_risk_pending_review"),
                "key_facts": [
                    f"登录侧成功 {int(login_summary.get('success_count', 0) or 0)} 条，失败 {int(login_summary.get('failure_count', 0) or 0)} 条；命令侧有效命令约 {int(command_summary.get('effective_command_count', 0) or 0)} 条。",
                    f"文件传输侧共记录上传 {int(transfer_summary.get('upload_count', 0) or 0)} 条、下载 {int(transfer_summary.get('download_count', 0) or 0)} 条，其中高风险上传 {int(transfer_summary.get('high_risk_upload_count', 0) or 0)} 条。",
                    f"管理平面共记录 {int(operation_summary.get('total_rows', 0) or 0)} 条操作，其中导出 {int(operation_summary.get('export_actions', 0) or 0)} 条、授权/更新 {int(operation_summary.get('authorization_updates', 0) or 0)} 条、主机/账号创建 {int(operation_summary.get('host_or_account_creation', 0) or 0)} 条。",
                    f"当前已经关联出 {len(correlations)} 条跨源高风险操作链，并汇总出 {len(accounts)} 个需要优先复核的高风险账户。",
                    str(risk_classification.get("why_not_direct_intrusion") or "当前还不足以直接确认外部入侵已成立。"),
                ],
                "probable_causes": [
                    "高权限运维、批量变更、临时调试工具执行与服务控制链在同一批审计样本里集中出现。",
                    "管理平面存在导出、授权与会话创建动作，可用于解释日志来源和资产变更背景。",
                    "JumpServer 原始风险等级和代理地址语义存在明显失真，必须结合跨源证据重建判断链。",
                ],
                "why_flagged": "系统识别到这是 JumpServer 多源审计批次，并检测到上传、命令、登录和会话链之间的高风险关联。",
                "report_gaps": [
                    "当前仍缺少完整会话级映射、维护窗口证明和文件哈希/执行结果等补充证据。",
                    "FTP 会话号与命令会话号未必能直接对应，仍需要人工结合时间窗和文件名继续复核。",
                ],
                "quick_checks": [
                    "优先复核 /tmp 二进制上传、权限放开、执行与网络连通性测试链条。",
                    "把管理平面导出、授权和会话创建动作与主机侧高危命令分开定性。",
                    "逐个确认高风险账户是否存在授权发布、运维变更或临时调试背景。",
                    "不要直接信任 JumpServer 原始风险等级，也不要把 10.x 代理地址直接当成真实攻击源。",
                ],
                "escalation_conditions": [
                    "如果同一用户在同一资产上形成上传 -> 提权 -> 放权 -> 执行 -> 服务变更链，应升级为高风险待复核事件。",
                    "如果补充证据显示存在未知来源载荷、异常持久化或未授权跨主机批量变更，应升级为已确认恶意事件。",
                ],
                "professional_judgment": "我的判断是：这批材料最适合定性为高风险运维 / 调试链与高风险待复核会话，而不是直接确认外部入侵。后续判断要以用户、资产、命令、会话和文件传输的联合证据为准。",
            }
        if event.source_type == "appsec" or event.event_type in {"whitebox_recon_assessment", "whitebox_exploit_validation", "whitebox_security_report"}:
            return self._appsec_analysis(event, findings)
        if event.source_type == "endpoint":
            rows = event.normalized_data.get("rows", [])
            row_count = len(rows) if isinstance(rows, list) else 0
            malware = 0
            blocked_sites = 0
            network_attacks = 0
            affected_hosts: set[str] = set()
            if isinstance(rows, list):
                for row in rows:
                    if not isinstance(row, dict):
                        continue
                    event_type = str(row.get("事件类型") or row.get("event_type") or "")
                    module = str(row.get("模块") or row.get("module") or "")
                    host = str(row.get("端点名称") or row.get("endpoint_name") or row.get("端点 FQDN") or "").strip()
                    if host:
                        affected_hosts.add(host)
                    if "恶意软件检测" in event_type or "反恶意软件" in module:
                        malware += 1
                    if "阻止的网站" in event_type or "反钓鱼" in module:
                        blocked_sites += 1
                    if "网络攻击" in event_type or "网络攻击防护" in module:
                        network_attacks += 1
            return {
                "assessment": "这份材料是来自端点安全平台的真实检测结果导入，已经包含终端安全事件，而不是单纯目录信息。",
                "likely_issue": any(f.risk_level >= 4 for f in findings),
                "verdict": "endpoint_incident_review",
                "key_facts": [
                    f"系统已将材料识别为端点 / EDR / incident 类输入，共包含 {row_count} 条终端安全记录。",
                    f"当前提炼出 {len(findings)} 条与端点行为相关的发现，影响主机数至少为 {len(affected_hosts)} 台。",
                    f"报表中包含 {malware} 条恶意软件检测、{network_attacks} 条网络攻击防护记录，以及 {blocked_sites} 条阻止网站记录。",
                    f"当前最值得优先排查的是命中过恶意软件或 exploit-style 规则的终端，而不是普通设备允许记录。",
                ],
                "probable_causes": [
                    "终端侧恶意软件、防钓鱼或网络攻击防护模块已经命中过真实检测结果。",
                    "部分记录可能是被拦截或已删除的威胁，但仍需要结合终端上下文确认是否存在后续活动或重复命中。",
                ],
                "why_flagged": "材料中包含 Bitdefender 导出的终端检测记录，包括恶意软件检测、攻击签名和恶意网站拦截信号。",
                "report_gaps": [],
                "quick_checks": [
                    "优先核对出现恶意软件检测和网络攻击防护命中的主机，确认相关文件是否已删除、隔离或仍然存在。",
                    "补充原始 EDR / XDR 事件、命令行、父子进程关系，以及同一主机上是否有重复命中。",
                ],
                "escalation_conditions": [
                    "如果同一主机反复出现恶意软件检测或 exploit-style 网络攻击记录，应升级为真实端点事件排查。",
                    "如果关联到外联、提权、持久化、凭据访问或横向移动链路，应立即升级处置。",
                ],
                "professional_judgment": "这类 Bitdefender 安全审计报表已经足以作为真实端点风险线索的输入，后续重点在于分清哪些主机需要升级调查、哪些只是被成功阻断。",
            }
        if event.source_type == "github":
            return {
                "assessment": "这份材料属于代码或供应链输入，当前结论以代码风险和凭据暴露为主。",
                "likely_issue": any(f.risk_level >= 4 for f in findings),
                "verdict": "supply_chain_review",
                "key_facts": [
                    f"系统已选择 {len(findings)} 条与代码、依赖或秘密信息相关的发现。",
                ],
                "probable_causes": [
                    "代码变更、依赖变更或凭据暴露触发了供应链安全分析。",
                ],
                "why_flagged": "材料中存在代码执行、依赖风险或敏感信息暴露信号。",
                "report_gaps": [],
                "quick_checks": [
                    "确认相关代码变更是否经过安全评审。",
                    "检查是否需要对暴露凭据执行轮换。",
                ],
                "escalation_conditions": [
                    "如果相关代码已经进入生产分支，应立即升级修复优先级。",
                ],
                "professional_judgment": "这类材料需要尽快回到代码和发布流程中完成修复闭环。",
            }
        likely = any(f.risk_level >= 4 for f in findings)
        return {
            "assessment": "这份材料包含值得继续跟进的安全信号。" if findings else "当前材料里没有提炼出足够具体的发现。",
            "likely_issue": likely,
            "verdict": "likely_true_positive" if likely else "needs_review",
            "key_facts": [],
            "probable_causes": [],
            "why_flagged": "系统从原始材料中提取到可疑安全信号。",
            "report_gaps": [],
            "quick_checks": [],
            "escalation_conditions": [],
            "professional_judgment": "建议结合更多上下文继续判断。",
        }

    def _easm_analysis(self, event: NormalizedEvent, findings: list[Finding]) -> dict[str, object]:
        data = event.normalized_data
        assessments = data.get("asset_assessments", []) if isinstance(data.get("asset_assessments"), list) else []
        surface_summary = data.get("surface_summary", {}) if isinstance(data.get("surface_summary"), dict) else {}
        key_assets = [item for item in assessments if str((item.get("scores") or {}).get("severity") or "") in {"Critical", "High"}][:8]
        high_assets = [item for item in assessments if str((item.get("scores") or {}).get("severity") or "") in {"Critical", "High"}]
        delegation_assets = [item for item in assessments if "third_party_dns_delegation" in item.get("tags", [])]
        historical_assets = [item for item in assessments if "historical_asset_hint" in item.get("tags", [])]
        layer_findings = data.get("layer_findings", []) if isinstance(data.get("layer_findings"), list) else []
        structured_sections = [
            {
                "title": "综合结论",
                "paragraphs": [],
                "bullets": [],
                "subsections": [],
            },
            {
                "title": "主要依据",
                "paragraphs": [],
                "bullets": [
                    f"当前样本覆盖 {surface_summary.get('asset_count', 0)} 个资产，层次分布为 {surface_summary.get('layer_counts', {})}。",
                    *layer_findings[:4],
                ],
                "subsections": [],
            },
            {
                "title": "重点资产评估",
                "paragraphs": [],
                "bullets": [
                    f"{item.get('asset')}：{(item.get('scores') or {}).get('severity')}，标签 {', '.join(item.get('tags', [])[:4])}"
                    for item in key_assets
                ],
                "subsections": [],
            },
        ]

        fallback_assessment = "这批外部攻击面材料已经能够支撑按资产输出结构化风险评估，当前重点不是发现数量，而是找出功能性域名、源站暴露、第三方委派和历史资产残留之间的治理优先级。"
        fallback_professional_judgment = "我的判断是：这批 EASM 材料已经足够作为资产治理和验证优先级排序的输入。当前最重要的是围绕高风险功能面资产构建后续验证计划，而不是把所有外部资产一视同仁。"
        agent_narrative = None
        if self.agent_model_binding:
            compact_context = {
                "asset_count": len(assessments),
                "high_risk_asset_count": len(high_assets),
                "delegation_asset_count": len(delegation_assets),
                "historical_asset_count": len(historical_assets),
                "layer_counts": surface_summary.get("layer_counts", {}),
                "top_assets": [
                    {
                        "asset": item.get("asset"),
                        "severity": (item.get("scores") or {}).get("severity"),
                        "tags": item.get("tags", [])[:6],
                    }
                    for item in key_assets[:6]
                ],
                "layer_findings": layer_findings[:6],
            }
            agent_narrative = self.agent_model_binding.generate_easm_composite_narrative(
                skill_id="megaeth.easm.asset_discovery",
                event=event,
                compact_context=compact_context,
                fallback_assessment=fallback_assessment,
                fallback_professional_judgment=fallback_professional_judgment,
            )

        assessment = str(agent_narrative.get("assessment")) if agent_narrative and agent_narrative.get("assessment") else fallback_assessment
        professional_judgment = str(agent_narrative.get("professional_judgment")) if agent_narrative and agent_narrative.get("professional_judgment") else fallback_professional_judgment
        if structured_sections:
            structured_sections[0]["paragraphs"] = [assessment]

        return {
            "report_title": "EASM 外部攻击面综合评估报告",
            "report_template": "easm_asset_assessment_v1",
            "assessment": assessment,
            "likely_issue": bool(high_assets),
            "verdict": "easm_asset_assessment",
            "key_facts": [
                f"系统已跨文件关联出 {len(assessments)} 个外部资产，其中高风险资产 {len(high_assets)} 个。",
                f"当前至少有 {len(delegation_assets)} 个资产涉及第三方 DNS/托管委派，另有 {len(historical_assets)} 个资产只在证书层留下历史线索。",
                f"重点资产包括：{', '.join(str(item.get('asset')) for item in key_assets[:5])}。",
            ],
            "probable_causes": [
                "同一功能面同时暴露 CDN 边缘与直连源站，导致边界治理不清晰。",
                "部分资产存在第三方委派或历史遗留托管痕迹，说明生命周期治理仍有缺口。",
            ],
            "why_flagged": "系统把服务、DNS、证书、IP 段和 ASN 数据做了跨文件关联，并按资产输出了事实与推断分离的外部攻击面评估结果。",
            "report_gaps": [
                "当前仍需补充更完整的真实原始 CSV 样本，持续校准字段映射与跨层关联逻辑。",
                "当前结论仍偏向暴露面治理与边界复核，不能替代后续验证扫描或人工确认。",
            ],
            "quick_checks": [
                "优先核实 API、Dashboard、RPC 等功能面资产是否存在直连源站暴露。",
                "优先确认第三方 DNS/托管委派资产的所有权、必要性和下线路径。",
                "对仅在证书层出现的历史资产继续核查 DNS、托管与证书清理状态。",
            ],
            "escalation_conditions": [
                "如果后续验证确认直连源站可绕过 CDN/WAF，应升级为高优先级外部暴露问题。",
                "如果功能性公网资产同时存在明文 HTTP、未限制回源或敏感接口，应继续升级处置。",
            ],
            "professional_judgment": professional_judgment,
            "structured_sections": structured_sections,
            "agent_context": dict(agent_narrative or {}),
        }

    def build(
        self,
        event: NormalizedEvent,
        planner_reason: str,
        skills_selected: list[str],
        findings: list[Finding],
        risk: dict[str, float | int | str],
        observability: dict[str, object],
    ) -> SecurityReport:
        if event.event_type == "host_baseline_assessment":
            summary = "本次分析识别出主机安全基线配置弱点，整体应按中风险治理。重点集中在文件系统隔离、临时目录配置、日志权限和不必要文件系统模块；若主机承担关键生产角色，风险应继续上调。"
        elif event.event_type == "easm_asset_assessment":
            summary = "本次分析输出 EASM 外部攻击面综合评估结果，重点是功能性域名、源站暴露、第三方委派与历史资产残留的治理优先级。"
        elif event.event_type == "jumpserver_multi_source_audit":
            summary = ""
        elif event.event_type == "login_auth_review":
            summary = "本次分析输出 JumpServer 登录认证结论，重点是失败登录、MFA 异常和代理地址语义，不能把登录快照直接当成入侵证据。"
        elif event.event_type == "jumpserver_command_review":
            summary = "本次分析输出 JumpServer 命令审计结论，重点是高危命令链、提权、服务控制和跨主机动作，而不是单条命令告警。"
        elif event.event_type == "jumpserver_transfer_review":
            summary = "本次分析输出 JumpServer 文件传输结论，重点是 /tmp 投放、root 账号上传、二进制落地与下载行为。"
        elif event.event_type == "jumpserver_operation_review":
            summary = "本次分析输出 JumpServer 管理平面结论，重点是导出、授权、主机/账号创建与会话建立等高影响动作，它们用于解释背景，不替代主机侧执行证据。"
        elif event.event_type == "whitebox_recon_assessment":
            summary = "本次分析输出应用白盒侦察结果，重点是确定高风险入口、鉴权边界与后续应优先验证的攻击路径。"
        elif event.event_type == "whitebox_exploit_validation":
            summary = "本次分析输出白盒安全验证结果，重点是区分哪些路径已经被确认，哪些仍需继续复核。"
        elif event.event_type == "whitebox_security_report":
            summary = "本次分析生成应用白盒安全综合报告，重点聚焦已确认问题、候选风险和优先治理动作。"
        elif findings:
            summary = f"{findings[0].summary} 本次分析共生成 {len(findings)} 条核心发现。"
        else:
            summary = "当前没有提炼出足够具体的发现，建议回看原始材料、分类结果和归一化质量。"
        analysis = self._host_analysis(event, findings) if event.source_type in {"host", "host_risk_analytics"} or event.event_type in {"host_integrity", "host_baseline_assessment"} else self._generic_analysis(event, findings)
        if event.event_type == "jumpserver_multi_source_audit":
            summary = str(analysis["assessment"])
        observability_payload = dict(observability)
        if analysis.get("structured_sections"):
            observability_payload["structured_sections"] = list(analysis["structured_sections"])
        if analysis.get("report_title"):
            observability_payload["report_title"] = str(analysis["report_title"])
        if analysis.get("report_template"):
            observability_payload["report_template"] = str(analysis["report_template"])
        agent_context = dict(analysis.get("agent_context") or {})
        execution_mode = "agent_augmented" if agent_context else "rule_only"
        if agent_context:
            observability_payload["agent_context"] = agent_context
        return SecurityReport(
            event_id=event.event_id,
            event_type=event.event_type,
            source_type=event.source_type,
            report_title=str(analysis.get("report_title") or ""),
            report_template=str(analysis.get("report_template") or ""),
            planner_reason=planner_reason,
            skills_selected=skills_selected,
            findings=findings,
            summary=summary,
            assessment=str(analysis["assessment"]),
            likely_issue=bool(analysis["likely_issue"]),
            verdict=str(analysis["verdict"]),
            evidence_highlights=self._evidence(findings),
            recommended_actions=self._actions(findings),
            analyst_notes=[f"系统当前将该事件判断为 {event.event_type}，并执行了 {len(findings)} 条有效发现。"],
            key_facts=list(analysis["key_facts"]),
            probable_causes=list(analysis["probable_causes"]),
            why_flagged=str(analysis["why_flagged"]),
            report_gaps=list(analysis["report_gaps"]),
            quick_checks=list(analysis["quick_checks"]),
            escalation_conditions=list(analysis["escalation_conditions"]),
            professional_judgment=str(analysis["professional_judgment"]),
            top_risk_level=int(risk["top_risk_level"]),
            top_risk_label=str(risk["top_risk_label"]),
            overall_risk_score=float(risk["overall_risk_score"]),
            generated_at=datetime.now(timezone.utc).isoformat(),
            structured_sections=list(analysis.get("structured_sections") or []),
            execution_mode=execution_mode,
            agent_context=agent_context,
            observability=observability_payload,
        )
