from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from app.appa.store import read_appa_state, write_appa_state
from app.models.appa import (
    AppaDashboard,
    AppaCreateEngagementRequest,
    AppaEngagement,
    AppaFinding,
    AppaLaunchRunRequest,
    AppaLaunchRunResponse,
    AppaMethodology,
    AppaMetric,
    AppaMode,
    AppaOverview,
    AppaReport,
    AppaReportType,
    AppaRole,
    AppaRun,
    AppaSkillPack,
    AppaTarget,
    AppaWorkItem,
    LocalizedText,
)


class AppaService:
    """Independent APPA product service."""

    def __init__(self) -> None:
        self._bootstrap()

    def overview(self) -> AppaOverview:
        state = self._state()
        overview = self._base_overview()
        overview.metrics = self._dynamic_metrics(state)
        return overview

    def dashboard(self) -> AppaDashboard:
        state = self._state()
        return AppaDashboard(
            operator_name=state["operator_name"],
            operator_status=state["operator_status"],
            mission_status=state["mission_status"],
            active_tab=state["active_tab"],
            active_nav=state["active_nav"],
            overview=self.overview(),
            engagements=[AppaEngagement.model_validate(item) for item in state["engagements"]],
            runs=[AppaRun.model_validate(item) for item in state["runs"][:5]],
            findings=[AppaFinding.model_validate(item) for item in state["findings"][:6]],
            reports=[AppaReport.model_validate(item) for item in state["reports"][:4]],
        )

    def list_runs(self) -> list[AppaRun]:
        return [AppaRun.model_validate(item) for item in self._state()["runs"]]

    def list_engagements(self) -> list[AppaEngagement]:
        return [AppaEngagement.model_validate(item) for item in self._state()["engagements"]]

    def create_engagement(self, payload: AppaCreateEngagementRequest) -> AppaEngagement:
        state = self._state()
        now = self._now()
        engagement = AppaEngagement(
            engagement_id=f"eng-{uuid4().hex[:10]}",
            name=payload.name,
            project_key=payload.project_key,
            mode=payload.mode,
            schedule=payload.schedule,
            status="active",
            methodologies=payload.methodologies,
            targets=payload.targets,
            created_at=now,
            updated_at=now,
        )
        state["engagements"].insert(0, engagement.model_dump(mode="json"))
        self._save(state)
        return engagement

    def list_findings(self) -> list[AppaFinding]:
        return [AppaFinding.model_validate(item) for item in self._state()["findings"]]

    def list_reports(self) -> list[AppaReport]:
        return [AppaReport.model_validate(item) for item in self._state()["reports"]]

    def launch_run(self, payload: AppaLaunchRunRequest) -> AppaLaunchRunResponse:
        state = self._state()
        engagement = next(
            (item for item in state["engagements"] if item["engagement_id"] == (payload.engagement_id or state["engagements"][0]["engagement_id"])),
            state["engagements"][0],
        )
        now = self._now()
        run = AppaRun(
            run_id=f"run-{uuid4().hex[:10]}",
            engagement_id=engagement["engagement_id"],
            mode=payload.mode,
            status="running",
            started_at=now,
            updated_at=now,
            modeled_paths=6,
            evidence_collected=3,
            triggered_by=payload.triggered_by,
        )
        report = AppaReport(
            report_id=f"report-{uuid4().hex[:10]}",
            run_id=run.run_id,
            engagement_id=engagement["engagement_id"],
            report_type="weekly_delta",
            title=f"{engagement['name']} Weekly Delta",
            summary="Weekly Green run refreshed path coverage, evidence-first findings, and audit-ready report output.",
            generated_at=now,
            finding_count=len(state["findings"][:3]),
        )

        state["mission_status"] = "WEEKLY GREEN RUN • IN PROGRESS"
        state["operator_status"] = "ACTIVE · JUST TRIGGERED"
        state["runs"].insert(0, run.model_dump(mode="json"))
        state["reports"].insert(0, report.model_dump(mode="json"))
        state["engagements"][0]["updated_at"] = now
        state["findings"] = self._refresh_findings(state["findings"], now)
        self._save(state)
        return AppaLaunchRunResponse(launched=True, run=run, report=report, dashboard=self.dashboard())

    def latest_report_markdown(self) -> str:
        state = self._state()
        report = AppaReport.model_validate(state["reports"][0])
        findings = [AppaFinding.model_validate(item) for item in state["findings"][:4]]
        lines = [
            f"# {report.title}",
            "",
            f"- Report Type: {report.report_type}",
            f"- Generated At: {report.generated_at}",
            f"- Finding Count: {report.finding_count}",
            "",
            "## Summary",
            "",
            report.summary,
            "",
            "## Evidence-First Findings",
            "",
        ]
        for finding in findings:
            lines.extend(
                [
                    f"### {finding.title}",
                    f"- Canonical Key: {finding.canonical_key}",
                    f"- Attack Path: {finding.attack_path_label}",
                    f"- Severity: {finding.severity}",
                    f"- Target Node: {finding.target_node}",
                    f"- Evidence Preview: {finding.evidence_preview}",
                    "",
                    finding.subtitle,
                    "",
                ]
            )
        return "\n".join(lines)

    def _bootstrap(self) -> None:
        if read_appa_state():
            return
        now = self._now()
        write_appa_state(
            {
                "operator_name": "Sentinel-01",
                "operator_status": "ACTIVE · 4H 12M",
                "mission_status": "WEEKLY GREEN RUN • IN PROGRESS",
                "active_tab": "dashboard",
                "active_nav": "overview",
                "engagements": [
                    AppaEngagement(
                        engagement_id="eng-green-prod",
                        name="weekly-green-prod",
                        project_key="megaeth",
                        mode="green",
                        schedule="0 2 * * 1",
                        status="active",
                        methodologies=["ptes", "mitre-attack", "owasp-top10"],
                        targets=[
                            AppaTarget(kind="domain", value="*.megaeth.com"),
                            AppaTarget(kind="ip", value="203.0.113.0/24"),
                            AppaTarget(kind="gcp_project", value="prod-project-1"),
                        ],
                        created_at=now,
                        updated_at=now,
                    ).model_dump(mode="json")
                ],
                "runs": [
                    AppaRun(
                        run_id="run-green-001",
                        engagement_id="eng-green-prod",
                        mode="green",
                        status="running",
                        started_at=now,
                        updated_at=now,
                        modeled_paths=6,
                        evidence_collected=3,
                        triggered_by="scheduler",
                    ).model_dump(mode="json")
                ],
                "findings": [item.model_dump(mode="json") for item in self._default_findings(now)],
                "reports": [
                    AppaReport(
                        report_id="report-green-001",
                        run_id="run-green-001",
                        engagement_id="eng-green-prod",
                        report_type="weekly_delta",
                        title="weekly-green-prod Weekly Delta",
                        summary="Evidence-first pentest coverage is active across management-plane exposure, CDN/origin drift, host secrets, and IAM path review.",
                        generated_at=now,
                        finding_count=4,
                    ).model_dump(mode="json")
                ],
            }
        )

    def _state(self) -> dict:
        state = read_appa_state()
        if state is None:
            self._bootstrap()
            state = read_appa_state() or {}
        return state

    def _save(self, state: dict) -> None:
        write_appa_state(state)

    def _now(self) -> str:
        return datetime.now(UTC).isoformat()

    def _dynamic_metrics(self, state: dict) -> list[AppaMetric]:
        engagements = state.get("engagements", [])
        runs = state.get("runs", [])
        findings = state.get("findings", [])
        reports = state.get("reports", [])
        return [
            AppaMetric(
                key="engagements",
                label=LocalizedText(zh="活动 Engagement", en="Active Engagements"),
                value=f"{len(engagements):02d}",
                accent="cyan",
                detail=LocalizedText(zh="当前纳入 APPA 控制面的活动任务。", en="Current engagements inside the APPA control plane."),
            ),
            AppaMetric(
                key="modeled_paths",
                label=LocalizedText(zh="建模路径", en="Modeled Paths"),
                value=f"{sum(item.get('modeled_paths', 0) for item in runs[:3]):02d}",
                accent="green",
                detail=LocalizedText(zh="最近运行批次里已经落成的攻击路径。", en="Attack paths modeled across the most recent runs."),
            ),
            AppaMetric(
                key="report_outputs",
                label=LocalizedText(zh="报告输出", en="Report Outputs"),
                value=f"{len(reports):02d}",
                accent="violet",
                detail=LocalizedText(zh="当前可回看的 APPA 审计交付物。", en="Audit-style deliverables currently available for review."),
            ),
            AppaMetric(
                key="evidence_findings",
                label=LocalizedText(zh="证据化发现", en="Evidence Findings"),
                value=f"{len(findings):02d}",
                accent="amber",
                detail=LocalizedText(zh="当前挂在攻击路径上的证据优先发现。", en="Evidence-first findings attached to active attack paths."),
            ),
        ]

    def _base_overview(self) -> AppaOverview:
        return AppaOverview(
            product_key="appa",
            product_name=LocalizedText(zh="APPA 渗透测试工作台", en="APPA Pentest Workbench"),
            product_summary=LocalizedText(
                zh="APPA 是以攻击路径为中心的持续渗透测试编排器。AI 负责规划和综合，受控工具负责执行，输出以审计风格报告为主。",
                en="APPA is an attack-path-centered continuous pentest orchestrator. AI plans and synthesizes, controlled tools execute, and audit-style reports are the primary output.",
            ),
            mission_copy=LocalizedText(
                zh="这里承接 APPA 的控制面、攻击路径、执行计划、证据流和审计风格报告，不和安全日志分析产品混用同一条链路。",
                en="This workbench carries APPA control-plane objects, attack paths, execution plans, evidence flow, and audit-style reports without sharing the same workflow semantics as security log analysis.",
            ),
            modes=[
                AppaMode(
                    key="green",
                    label=LocalizedText(zh="Green", en="Green"),
                    schedule=LocalizedText(zh="默认周跑", en="Default weekly cadence"),
                    access=LocalizedText(zh="低风险发现与基线验证", en="Low-risk discovery and baseline checks"),
                    status="active",
                ),
                AppaMode(
                    key="yellow",
                    label=LocalizedText(zh="Yellow", en="Yellow"),
                    schedule=LocalizedText(zh="按需触发", en="On-demand"),
                    access=LocalizedText(zh="审批后只读验证", en="Approval-gated read-only verification"),
                    status="gated",
                ),
                AppaMode(
                    key="red",
                    label=LocalizedText(zh="Red", en="Red"),
                    schedule=LocalizedText(zh="人工专项", en="Manual campaigns only"),
                    access=LocalizedText(zh="不进入自治范围", en="Excluded from autonomous scope"),
                    status="manual",
                ),
            ],
            methodologies=[
                AppaMethodology(
                    key="ptes",
                    label=LocalizedText(zh="PTES 生命周期", en="PTES Lifecycle"),
                    emphasis=LocalizedText(
                        zh="按 Recon → Analysis → Targeted Verification → Reporting 的顺序组织工作。",
                        en="Organize work as Recon → Analysis → Targeted Verification → Reporting.",
                    ),
                ),
                AppaMethodology(
                    key="mitre",
                    label=LocalizedText(zh="MITRE ATT&CK", en="MITRE ATT&CK"),
                    emphasis=LocalizedText(
                        zh="用攻击路径语言描述验证对象，而不是只堆扫描器 finding。",
                        en="Use attack-path language to describe validation objects instead of only listing scanner findings.",
                    ),
                ),
                AppaMethodology(
                    key="owasp",
                    label=LocalizedText(zh="OWASP Top 10", en="OWASP Top 10"),
                    emphasis=LocalizedText(
                        zh="把 Web / API 风险归到可复核的控制点，而不是只给模糊风险分。",
                        en="Map Web/API issues to reviewable control points instead of vague risk scores.",
                    ),
                ),
            ],
            skill_packs=[
                AppaSkillPack(
                    skill_id="recon-surface",
                    label=LocalizedText(zh="攻击面侦察", en="Recon Surface"),
                    mode="Green",
                    phase="V1",
                    summary=LocalizedText(
                        zh="把域名、IP、URL 和服务清单编织成攻击面资产图。",
                        en="Turn domains, IPs, URLs, and services into an attack-surface asset graph.",
                    ),
                ),
                AppaSkillPack(
                    skill_id="web-api-baseline",
                    label=LocalizedText(zh="Web / API 基线", en="Web/API Baseline"),
                    mode="Green",
                    phase="V1",
                    summary=LocalizedText(
                        zh="执行低风险的 Web 与 API 基线验证，优先输出可复核证据。",
                        en="Run low-risk Web and API baseline validation with evidence-first outputs.",
                    ),
                ),
                AppaSkillPack(
                    skill_id="origin-consistency",
                    label=LocalizedText(zh="CDN / Origin 一致性", en="Origin Consistency"),
                    mode="Green",
                    phase="V1",
                    summary=LocalizedText(
                        zh="专门识别域名受保护但源站仍可直连的路径。",
                        en="Specifically detect paths where the domain is protected but the origin remains directly reachable.",
                    ),
                ),
                AppaSkillPack(
                    skill_id="host-review",
                    label=LocalizedText(zh="主机只读审计", en="Host Review"),
                    mode="Yellow",
                    phase="V1+",
                    summary=LocalizedText(
                        zh="通过预定义只读检查包做主机配置、凭证残留和系统卫生验证。",
                        en="Use approved read-only packs to validate host posture, residue, and hygiene.",
                    ),
                ),
                AppaSkillPack(
                    skill_id="gcp-review",
                    label=LocalizedText(zh="GCP 姿态审计", en="GCP Review"),
                    mode="Yellow",
                    phase="V1+",
                    summary=LocalizedText(
                        zh="聚焦 GCP posture、IAM 和暴露面审计，不让 LLM 直接拿高权限云凭证。",
                        en="Focus on GCP posture, IAM, and exposure review without handing high-privilege cloud creds to the LLM.",
                    ),
                ),
                AppaSkillPack(
                    skill_id="external-evidence-import",
                    label=LocalizedText(zh="外部证据导入", en="External Evidence Import"),
                    mode="Green",
                    phase="V1",
                    summary=LocalizedText(
                        zh="接收第三方扫描、审计或安全工具结果，把它们并入路径证据。",
                        en="Import third-party scan, audit, or security-tool results and merge them into path evidence.",
                    ),
                ),
            ],
            roles=[
                AppaRole(
                    key="planner",
                    label=LocalizedText(zh="Planner", en="Planner"),
                    responsibility=LocalizedText(
                        zh="读取范围、资产图和历史 finding，生成 attack path 与 job plan。",
                        en="Read scope, asset graph, and prior findings to generate attack paths and job plans.",
                    ),
                ),
                AppaRole(
                    key="analyst",
                    label=LocalizedText(zh="Analyst", en="Analyst"),
                    responsibility=LocalizedText(
                        zh="把各个 skill 的证据汇总成路径级观察，形成 evidence-first finding。",
                        en="Aggregate evidence across skills into path-level observations and evidence-first findings.",
                    ),
                ),
                AppaRole(
                    key="reporter",
                    label=LocalizedText(zh="Reporter", en="Reporter"),
                    responsibility=LocalizedText(
                        zh="按审计风格输出 Full Audit、Weekly Delta 和 Retest。",
                        en="Produce Full Audit, Weekly Delta, and Retest outputs in an audit-style format.",
                    ),
                ),
            ],
            report_types=[
                AppaReportType(
                    key="full_audit",
                    label=LocalizedText(zh="Full Audit", en="Full Audit"),
                    summary=LocalizedText(
                        zh="完整交付，覆盖攻击路径、证据链、风险和修复建议。",
                        en="Full delivery covering attack paths, evidence chains, risk, and remediation.",
                    ),
                ),
                AppaReportType(
                    key="weekly_delta",
                    label=LocalizedText(zh="Weekly Delta", en="Weekly Delta"),
                    summary=LocalizedText(
                        zh="持续运行后的变化追踪，强调新增暴露和状态流转。",
                        en="Continuous tracking focused on new exposure and status movement.",
                    ),
                ),
                AppaReportType(
                    key="retest",
                    label=LocalizedText(zh="Retest", en="Retest"),
                    summary=LocalizedText(
                        zh="问题整改后的复测，关注已修复、部分修复和仍未修复项。",
                        en="Post-remediation validation across fixed, partial, and unresolved items.",
                    ),
                ),
            ],
            attack_paths=[
                AppaWorkItem(
                    key="internet_mgmt",
                    label=LocalizedText(zh="互联网管理面暴露", en="Management Plane Exposure"),
                    detail=LocalizedText(
                        zh="优先验证管理入口、控制面和高价值运维端口是否直接暴露在互联网。",
                        en="Prioritize validation of management entry points, control planes, and high-value operations ports exposed to the internet.",
                    ),
                    accent="cyan",
                ),
                AppaWorkItem(
                    key="cdn_origin",
                    label=LocalizedText(zh="CDN / Origin 不一致", en="CDN/Origin Inconsistency"),
                    detail=LocalizedText(
                        zh="重点识别域名受保护但源站仍可直连的路径，以及默认 vhost 泄露。",
                        en="Focus on paths where the domain is protected but the origin remains directly reachable, including default vhost leakage.",
                    ),
                    accent="green",
                ),
                AppaWorkItem(
                    key="host_secret",
                    label=LocalizedText(zh="主机残留凭证", en="Host Residual Secrets"),
                    detail=LocalizedText(
                        zh="Yellow 模式下只读核查主机残留 secrets、历史凭证和配置卫生。",
                        en="Use Yellow mode read-only checks for host residual secrets, legacy credentials, and configuration hygiene.",
                    ),
                    accent="violet",
                ),
                AppaWorkItem(
                    key="gcp_iam",
                    label=LocalizedText(zh="GCP IAM 过宽路径", en="Over-Broad GCP IAM Paths"),
                    detail=LocalizedText(
                        zh="关注服务账号、IAM 和暴露资源之间的路径。",
                        en="Focus on paths across service accounts, IAM, and exposed resources.",
                    ),
                    accent="amber",
                ),
            ],
            evidence_lanes=[
                AppaWorkItem(
                    key="raw_artifacts",
                    label=LocalizedText(zh="Raw Artifact", en="Raw Artifact"),
                    detail=LocalizedText(
                        zh="原始 artifact 先入库，再由系统做 redaction 和 evidence id 回链。",
                        en="Store raw artifacts first, then apply redaction and evidence-id back-linking.",
                    ),
                    accent="cyan",
                ),
                AppaWorkItem(
                    key="redacted_preview",
                    label=LocalizedText(zh="Redacted Preview", en="Redacted Preview"),
                    detail=LocalizedText(
                        zh="报告和 AI 只消费脱敏预览，不直接接触原始敏感材料。",
                        en="Reports and AI only consume redacted previews rather than raw sensitive material.",
                    ),
                    accent="green",
                ),
                AppaWorkItem(
                    key="path_finding",
                    label=LocalizedText(zh="Path-Level Finding", en="Path-Level Finding"),
                    detail=LocalizedText(
                        zh="APPA 的 finding 是挂在攻击路径上的证据节点。",
                        en="APPA findings are evidence nodes attached to attack paths.",
                    ),
                    accent="violet",
                ),
            ],
            roadmap=[
                AppaWorkItem(
                    key="control_plane",
                    label=LocalizedText(zh="控制面与 scope guard", en="Control Plane & Scope Guard"),
                    detail=LocalizedText(
                        zh="先把 engagement、scope、allowlist、approval 和 mode guard 落稳。",
                        en="Stabilize engagement, scope, allowlists, approvals, and mode guards first.",
                    ),
                    accent="cyan",
                ),
                AppaWorkItem(
                    key="planner",
                    label=LocalizedText(zh="攻击路径 Planner", en="Attack-Path Planner"),
                    detail=LocalizedText(
                        zh="把 scope、资产图和已有 finding 编译成 attack path 与 job plan。",
                        en="Compile scope, asset graph, and prior findings into attack paths and job plans.",
                    ),
                    accent="green",
                ),
                AppaWorkItem(
                    key="evidence_report",
                    label=LocalizedText(zh="证据层与报告层", en="Evidence & Reporting"),
                    detail=LocalizedText(
                        zh="统一 raw artifact、redacted preview、severity 评估和审计风格报告。",
                        en="Unify raw artifacts, redacted previews, severity assessment, and audit-style reporting.",
                    ),
                    accent="violet",
                ),
            ],
        )

    def _default_findings(self, now: str) -> list[AppaFinding]:
        return [
            AppaFinding(
                finding_id="fd-001",
                canonical_key="CVE-2024-21626",
                title="CVE-2024-21626",
                subtitle="runc-escape-found",
                attack_path_label="Management Plane Exposure",
                severity="critical",
                likelihood=4,
                impact=4,
                target_node="k8s-prod-cluster-01",
                evidence_preview="Redacted_Preview.log",
                status="confirmed",
                created_at=now,
            ),
            AppaFinding(
                finding_id="fd-002",
                canonical_key="JWT-ALG-NONE",
                title="JWT-ALG-NONE",
                subtitle="api-auth-bypass",
                attack_path_label="CDN/Origin Inconsistency",
                severity="high",
                likelihood=3,
                impact=3,
                target_node="api.payments.internal",
                evidence_preview="Payload_Dump.json",
                status="running",
                created_at=now,
            ),
            AppaFinding(
                finding_id="fd-003",
                canonical_key="S3-READ-GLOBAL",
                title="S3-READ-GLOBAL",
                subtitle="misconfig-public-bucket",
                attack_path_label="Over-Broad GCP IAM Paths",
                severity="medium",
                likelihood=2,
                impact=2,
                target_node="static-assets-prd",
                evidence_preview="Bucket_Policy.xml",
                status="collecting",
                created_at=now,
            ),
        ]

    def _refresh_findings(self, findings: list[dict], now: str) -> list[dict]:
        updated = []
        for index, item in enumerate(findings):
            finding = AppaFinding.model_validate(item)
            if index == 0:
                finding.status = "confirmed"
            elif index == 1:
                finding.status = "running"
            else:
                finding.status = "collecting"
            finding.created_at = now
            updated.append(finding.model_dump(mode="json"))
        return updated
