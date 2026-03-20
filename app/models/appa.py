from __future__ import annotations

from pydantic import BaseModel, Field


class LocalizedText(BaseModel):
    zh: str
    en: str


class AppaMetric(BaseModel):
    key: str
    label: LocalizedText
    value: str
    accent: str = "cyan"
    detail: LocalizedText


class AppaMode(BaseModel):
    key: str
    label: LocalizedText
    schedule: LocalizedText
    access: LocalizedText
    status: str


class AppaMethodology(BaseModel):
    key: str
    label: LocalizedText
    emphasis: LocalizedText


class AppaSkillPack(BaseModel):
    skill_id: str
    label: LocalizedText
    mode: str
    phase: str
    summary: LocalizedText


class AppaRole(BaseModel):
    key: str
    label: LocalizedText
    responsibility: LocalizedText


class AppaReportType(BaseModel):
    key: str
    label: LocalizedText
    summary: LocalizedText


class AppaWorkItem(BaseModel):
    key: str
    label: LocalizedText
    detail: LocalizedText
    accent: str = "note"


class AppaOverview(BaseModel):
    product_key: str
    product_name: LocalizedText
    product_summary: LocalizedText
    mission_copy: LocalizedText
    metrics: list[AppaMetric] = Field(default_factory=list)
    modes: list[AppaMode] = Field(default_factory=list)
    methodologies: list[AppaMethodology] = Field(default_factory=list)
    skill_packs: list[AppaSkillPack] = Field(default_factory=list)
    roles: list[AppaRole] = Field(default_factory=list)
    report_types: list[AppaReportType] = Field(default_factory=list)
    attack_paths: list[AppaWorkItem] = Field(default_factory=list)
    evidence_lanes: list[AppaWorkItem] = Field(default_factory=list)
    roadmap: list[AppaWorkItem] = Field(default_factory=list)


class AppaTarget(BaseModel):
    kind: str
    value: str


class AppaEngagement(BaseModel):
    engagement_id: str
    name: str
    project_key: str
    mode: str
    schedule: str
    status: str
    methodologies: list[str] = Field(default_factory=list)
    targets: list[AppaTarget] = Field(default_factory=list)
    created_at: str
    updated_at: str


class AppaRun(BaseModel):
    run_id: str
    engagement_id: str
    mode: str
    status: str
    started_at: str
    updated_at: str
    modeled_paths: int
    evidence_collected: int
    triggered_by: str


class AppaFinding(BaseModel):
    finding_id: str
    canonical_key: str
    title: str
    subtitle: str
    attack_path_label: str
    severity: str
    likelihood: int = Field(ge=1, le=4)
    impact: int = Field(ge=1, le=4)
    target_node: str
    evidence_preview: str
    status: str
    created_at: str


class AppaReport(BaseModel):
    report_id: str
    run_id: str
    engagement_id: str
    report_type: str
    title: str
    summary: str
    generated_at: str
    finding_count: int


class AppaDashboard(BaseModel):
    operator_name: str
    operator_status: str
    mission_status: str
    active_tab: str
    active_nav: str
    overview: AppaOverview
    engagements: list[AppaEngagement] = Field(default_factory=list)
    runs: list[AppaRun] = Field(default_factory=list)
    findings: list[AppaFinding] = Field(default_factory=list)
    reports: list[AppaReport] = Field(default_factory=list)


class AppaLaunchRunRequest(BaseModel):
    mode: str = "green"
    engagement_id: str | None = None
    triggered_by: str = "manual"


class AppaCreateEngagementRequest(BaseModel):
    name: str
    project_key: str = "megaeth"
    mode: str = "green"
    schedule: str = "0 2 * * 1"
    methodologies: list[str] = Field(default_factory=lambda: ["ptes", "mitre-attack", "owasp-top10"])
    targets: list[AppaTarget] = Field(default_factory=list)


class AppaLaunchRunResponse(BaseModel):
    launched: bool
    run: AppaRun
    report: AppaReport
    dashboard: AppaDashboard
