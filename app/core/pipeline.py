from __future__ import annotations

# Security-log-analysis mainline analysis pipeline.

import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
import re
from uuid import uuid4

from app.core.agent_model_binding import AGENT_ID, AgentModelBindingService
from app.core.history import HistoryService
from app.core.memory_service import MemoryService
from app.core.normalizer import EventNormalizer
from app.core.planner import Planner
from app.core.report_engine import ReportEngine
from app.core.risk_engine import RiskEngine
from app.models.event import EventEnvelope, NormalizedEvent, RawEvent
from app.models.finding import SecurityReport
from app.skills.implementations import SKILLS


class SecurityPipeline:
    def __init__(self) -> None:
        self.normalizer = EventNormalizer()
        self.memory = MemoryService()
        self.planner = Planner()
        self.history = HistoryService()
        self.risk_engine = RiskEngine()
        self.agent_model_binding = AgentModelBindingService()
        self.report_engine = ReportEngine(self.agent_model_binding)
        self.recent_reports: deque[SecurityReport] = deque(maxlen=30)
        self.metrics = {"events_processed": 0, "findings_generated": 0, "last_event_at": None}
        self._training_index_cache: tuple[float, dict[str, list[str]]] | None = None
        self._restore_runtime_state()

    def _restore_runtime_state(self) -> None:
        reports = self.history.list_reports()
        if reports:
            ordered = sorted(reports, key=lambda item: item.get("generated_at", ""), reverse=True)
            recent_items = self._dedupe_recent_reports(ordered)
            self.metrics = {
                "events_processed": len(reports),
                "findings_generated": sum(len(item.get("findings", [])) for item in reports),
                "last_event_at": ordered[0].get("generated_at"),
            }
            for item in recent_items[:30]:
                self.recent_reports.append(SecurityReport(**item))
            return
        events = self.history.list_events()
        self.metrics = {
            "events_processed": len(events),
            "findings_generated": 0,
            "last_event_at": events[0]["normalized_event"]["timestamp"] if events else None,
        }

    def list_skills(self) -> list[dict]:
        training_index = self._training_case_index()
        return [
            {
                "skill_id": skill.skill_id,
                "skill_name": skill.skill_name,
                "version": "0.1.0",
                "category": skill.category,
                "description": skill.description,
                "stage": "tool-backed",
                "adapter": skill.skill_id.split(".")[-1],
                "execution_mode": skill.execution_mode,
                "agent_trigger_conditions": skill.agent_trigger_conditions,
                "rule_fallback_conditions": skill.rule_fallback_conditions,
                "max_context_policy": skill.max_context_policy,
                "trained_case_count": len(training_index.get(skill.skill_id, [])),
                "trained_cases": training_index.get(skill.skill_id, []),
            }
            for skill in SKILLS.values()
        ]

    def _training_case_index(self) -> dict[str, list[str]]:
        case_root = Path(__file__).resolve().parents[2] / "training_cases"
        readmes = sorted(case_root.glob("case_*/README.md"))
        cache_key = max((path.stat().st_mtime for path in readmes), default=0.0)
        if self._training_index_cache and self._training_index_cache[0] == cache_key:
            return self._training_index_cache[1]
        skill_to_cases: dict[str, list[str]] = {}
        for readme in readmes:
            case_id = readme.parent.name
            content = readme.read_text(encoding="utf-8")
            for skill_id in sorted(set(re.findall(r"`(megaeth\.[^`]+)`", content))):
                skill_to_cases.setdefault(skill_id, []).append(case_id)
        self._training_index_cache = (cache_key, skill_to_cases)
        return skill_to_cases

    def skill_matrix(self) -> dict[str, list[dict]]:
        grouped: dict[str, list[dict]] = {}
        for item in self.list_skills():
            grouped.setdefault(item["category"], []).append(item)
        return grouped

    def overview(self) -> dict:
        matrix = self.skill_matrix()
        return {
            "pipeline": {
                "execution_modes": ["real-time", "batch"],
                "components": ["intake", "memory", "normalizer", "planner", "skills", "agent", "risk", "report"],
            },
            "metrics": self.metrics,
            "agent": {
                "agent_id": AGENT_ID,
                "model_provider": (self.agent_model_binding.binding_for_agent() or {}).get("provider"),
                "model_enabled": self.agent_model_binding.enabled_for_skill("megaeth.identity.jumpserver_multi_source_review"),
                "bound_skills": (self.agent_model_binding.binding_for_agent() or {}).get("skills", []),
            },
            "skill_library": {
                "total_skills": len(SKILLS),
                "categories": {key: len(value) for key, value in matrix.items()},
                "tool_backed": len(SKILLS),
                "skeleton_only": 0,
                "execution_modes": {
                    "rule_only": sum(1 for skill in SKILLS.values() if skill.execution_mode == "rule_only"),
                    "agent_optional": sum(1 for skill in SKILLS.values() if skill.execution_mode == "agent_optional"),
                    "agent_preferred": sum(1 for skill in SKILLS.values() if skill.execution_mode == "agent_preferred"),
                },
            },
        }

    def run(self, event: NormalizedEvent, envelope: EventEnvelope | None = None) -> SecurityReport:
        started = time.perf_counter()
        classification = self.planner.classify(event)
        skills, reason = self.planner.plan(event)
        findings = []
        skill_times = {}
        for skill_id in skills:
            if skill_id not in SKILLS:
                continue
            skill_start = time.perf_counter()
            findings.extend(SKILLS[skill_id].execute(event))
            skill_times[skill_id] = int((time.perf_counter() - skill_start) * 1000)
        risk = self.risk_engine.calculate(event, findings)
        report = self.report_engine.build(
            event=event,
            planner_reason=reason,
            skills_selected=skills,
            findings=findings,
            risk=risk,
            observability={
                "pipeline_latency_ms": int((time.perf_counter() - started) * 1000),
                "skill_execution_time_ms": skill_times,
                "classification": classification,
            },
        )
        self.metrics["events_processed"] += 1
        self.metrics["findings_generated"] += len(findings)
        self.metrics["last_event_at"] = datetime.now(timezone.utc).isoformat()
        self.recent_reports.appendleft(report)
        self.history.save_normalized_event(envelope or EventEnvelope(normalized_event=event, classification=classification))
        self.history.save_report(report)
        return report

    def ingest_raw(self, raw_event: RawEvent) -> SecurityReport:
        raw_event, memory = self.memory.apply_raw_event_memory(raw_event)
        normalized = self.normalizer.normalize(raw_event)
        normalized = self.memory.enrich_normalized_event(normalized, memory)
        classification = self.planner.classify(normalized)
        envelope = EventEnvelope(raw_event=raw_event, normalized_event=normalized, classification=classification)
        self.history.save_raw_event(raw_event)
        planned_skills, _ = self.planner.plan(normalized)
        self.memory.learn_from_analysis(raw_event, normalized, planned_skills)
        return self.run(normalized, envelope)

    def recent(self) -> list[dict]:
        if self.recent_reports:
            return [report.model_dump(mode="json") for report in self.recent_reports]
        reports = self.history.list_reports()
        ordered = sorted(reports, key=lambda item: item.get("generated_at", ""), reverse=True)
        return self._dedupe_recent_reports(ordered)[:30]

    def _dedupe_recent_reports(self, reports: list[dict]) -> list[dict]:
        deduped: list[dict] = []
        seen: dict[tuple[str, str, str, str], int] = {}
        for report in reports:
            timestamp = str(report.get("generated_at") or report.get("created_at") or "")[:19]
            fingerprint = (
                str(report.get("source_type") or ""),
                str(report.get("event_type") or ""),
                str(report.get("verdict") or ""),
                timestamp,
            )
            current_score = (
                int(len(report.get("findings", []))) * 100
                + int(round(float(report.get("overall_risk_score") or 0) * 10))
            )
            existing_index = seen.get(fingerprint)
            if existing_index is None:
                seen[fingerprint] = len(deduped)
                deduped.append(report)
                continue
            existing = deduped[existing_index]
            existing_score = (
                int(len(existing.get("findings", []))) * 100
                + int(round(float(existing.get("overall_risk_score") or 0) * 10))
            )
            if current_score > existing_score:
                deduped[existing_index] = report
        return deduped

    def save_investigation_session(self, name: str, items: list[dict]) -> dict:
        uploaded_files = [
            item for item in items
            if (item.get("raw_event", {}).get("asset_context", {}) or {}).get("source_file")
        ]
        investigation_id = f"inv-{uuid4().hex[:10]}"
        archive_meta = self.history.save_investigation_archive(investigation_id, items)
        session = {
            "investigation_id": investigation_id,
            "name": name,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "file_count": len(uploaded_files),
            "result_count": len(items),
            "top_risk_score": max((item["report"]["overall_risk_score"] for item in items), default=0.0),
            "top_risk_label": max((item["report"]["top_risk_label"] for item in items), default="info", key=lambda x: {"info":1,"low":2,"medium":3,"high":4,"critical":5}.get(x,1)),
            "skills_seen": sorted({skill for item in items for skill in item["planner_preview"]["skills_to_execute"]}),
            "files": [
                {
                    "filename": item["filename"],
                    "event_type": item["normalized_event"]["event_type"],
                    "source_type": item["normalized_event"]["source_type"],
                    "parser_profile": item["raw_event"]["payload"].get("parser_profile", "generic"),
                }
                for item in items
            ],
            "archive": archive_meta,
        }
        self.history.save_investigation(session)
        return session
