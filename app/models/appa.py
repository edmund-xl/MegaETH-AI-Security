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
