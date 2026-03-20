from __future__ import annotations

from app.models.appa import (
    AppaMethodology,
    AppaMetric,
    AppaMode,
    AppaOverview,
    AppaReportType,
    AppaRole,
    AppaSkillPack,
    AppaWorkItem,
    LocalizedText,
)


class AppaService:
    """Independent APPA product service.

    This service intentionally does not reuse the security-log-analysis
    pipeline semantics. It exposes the APPA control-plane/workbench model
    as its own product domain.
    """

    def overview(self) -> AppaOverview:
        return AppaOverview(
            product_key="appa",
            product_name=LocalizedText(
                zh="APPA 渗透测试工作台",
                en="APPA Pentest Workbench",
            ),
            product_summary=LocalizedText(
                zh="APPA 是以攻击路径为中心的持续渗透测试编排器。AI 负责规划和综合，受控工具负责执行，输出以审计风格报告为主。",
                en="APPA is an attack-path-centered continuous pentest orchestrator. AI plans and synthesizes, controlled tools execute, and audit-style reports are the primary output.",
            ),
            mission_copy=LocalizedText(
                zh="这里承接 APPA 的控制面、攻击路径、执行计划、证据流和审计风格报告，不和安全日志分析产品混用同一条链路。",
                en="This workbench carries APPA control-plane objects, attack paths, execution plans, evidence flow, and audit-style reports without sharing the same workflow semantics as security log analysis.",
            ),
            metrics=[
                AppaMetric(
                    key="default_mode",
                    label=LocalizedText(zh="默认模式", en="Default Mode"),
                    value="Green",
                    accent="green",
                    detail=LocalizedText(
                        zh="按周调度，优先覆盖外部暴露面、Web/API 基线、CDN / Origin 一致性和外部证据导入。",
                        en="Scheduled weekly, prioritizing exposed surface, Web/API baselines, CDN/origin consistency, and external evidence import.",
                    ),
                ),
                AppaMetric(
                    key="core_skills",
                    label=LocalizedText(zh="V1 核心 Skill", en="V1 Core Skills"),
                    value="6",
                    accent="cyan",
                    detail=LocalizedText(
                        zh="先以 recon-surface、web-api-baseline、origin-consistency、host-review、gcp-review、external-evidence-import 为主。",
                        en="Start with recon-surface, web-api-baseline, origin-consistency, host-review, gcp-review, and external-evidence-import.",
                    ),
                ),
                AppaMetric(
                    key="report_outputs",
                    label=LocalizedText(zh="报告输出", en="Report Outputs"),
                    value="3",
                    accent="violet",
                    detail=LocalizedText(
                        zh="统一输出 Full Audit、Weekly Delta 和 Retest 三类报告。",
                        en="Standardize on Full Audit, Weekly Delta, and Retest outputs.",
                    ),
                ),
            ],
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
                AppaRole(
                    key="verifier",
                    label=LocalizedText(zh="Verifier", en="Verifier"),
                    responsibility=LocalizedText(
                        zh="对 mode、scope、tool allowlist、证据结构做 deterministic 校验。",
                        en="Perform deterministic checks over mode, scope, tool allowlists, and evidence structure.",
                    ),
                ),
            ],
            report_types=[
                AppaReportType(
                    key="full_audit",
                    label=LocalizedText(zh="Full Audit", en="Full Audit"),
                    summary=LocalizedText(
                        zh="适合完整交付，覆盖攻击路径、证据链、风险和修复建议。",
                        en="Best for full delivery covering attack paths, evidence chains, risk, and remediation.",
                    ),
                ),
                AppaReportType(
                    key="weekly_delta",
                    label=LocalizedText(zh="Weekly Delta", en="Weekly Delta"),
                    summary=LocalizedText(
                        zh="适合持续运行后的变化追踪，强调新增暴露和状态流转。",
                        en="Best for continuous tracking, emphasizing new exposure and status movement.",
                    ),
                ),
                AppaReportType(
                    key="retest",
                    label=LocalizedText(zh="Retest", en="Retest"),
                    summary=LocalizedText(
                        zh="适合问题整改后的复测，关注已修复、部分修复和仍未修复项。",
                        en="Best for post-remediation validation, focusing on fixed, partially fixed, and unresolved items.",
                    ),
                ),
            ],
            attack_paths=[
                AppaWorkItem(
                    key="internet_mgmt",
                    label=LocalizedText(zh="互联网管理面暴露", en="Internet Management Plane Exposure"),
                    detail=LocalizedText(
                        zh="优先验证管理入口、控制面和高价值运维端口是否直接暴露在互联网。",
                        en="Prioritize validation of management entry points, control planes, and high-value operations ports exposed to the internet.",
                    ),
                    accent="cyan",
                ),
                AppaWorkItem(
                    key="cdn_origin",
                    label=LocalizedText(zh="CDN / Origin 不一致", en="CDN / Origin Drift"),
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
                        zh="后续接住 GCP posture review，关注服务账号、IAM 和暴露资源之间的路径。",
                        en="Future GCP posture review should focus on paths across service accounts, IAM, and exposed resources.",
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
                        zh="APPA 的 finding 不是扫描器直接产物，而是挂在攻击路径上的证据节点。",
                        en="APPA findings are not direct scanner outputs; they are evidence nodes attached to attack paths.",
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
                        zh="把 scope、资产图、架构图和已有 finding 编译成 attack path 与 job plan。",
                        en="Compile scope, asset graph, diagrams, and prior findings into attack paths and job plans.",
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
