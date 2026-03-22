from __future__ import annotations

# Security-log-analysis mainline finding/report models.

from typing import Any

from pydantic import BaseModel, Field


class Finding(BaseModel):
    finding_id: str
    skill_id: str
    risk_level: int = Field(ge=1, le=5)
    risk_label: str
    risk_type: str
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str
    affected_assets: list[str] = Field(default_factory=list)
    evidence: list[dict[str, Any]] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)


class SecurityReport(BaseModel):
    event_id: str
    event_type: str
    source_type: str
    report_title: str = ""
    report_template: str = ""
    planner_reason: str
    skills_selected: list[str]
    findings: list[Finding]
    summary: str
    assessment: str = ""
    likely_issue: bool = False
    verdict: str = "needs_review"
    evidence_highlights: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    analyst_notes: list[str] = Field(default_factory=list)
    key_facts: list[str] = Field(default_factory=list)
    probable_causes: list[str] = Field(default_factory=list)
    why_flagged: str = ""
    report_gaps: list[str] = Field(default_factory=list)
    quick_checks: list[str] = Field(default_factory=list)
    escalation_conditions: list[str] = Field(default_factory=list)
    professional_judgment: str = ""
    top_risk_level: int
    top_risk_label: str
    overall_risk_score: float
    generated_at: str
    structured_sections: list[dict[str, Any]] = Field(default_factory=list)
    execution_mode: str = "rule_only"
    agent_context: dict[str, Any] = Field(default_factory=dict)
    observability: dict[str, Any] = Field(default_factory=dict)
