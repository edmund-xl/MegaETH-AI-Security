from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import gzip
import json
from pathlib import Path

from app.models.event import EventEnvelope, RawEvent
from app.models.finding import SecurityReport
from app.utils.store import (
    EVENTS_FILE,
    INVESTIGATIONS_FILE,
    RAW_EVENTS_FILE,
    REPORTS_FILE,
    JsonFileStore,
    write_json,
)


ARCHIVE_DIR = Path(__file__).resolve().parents[2] / "data" / "archives" / "investigations"


class HistoryService:
    def __init__(self) -> None:
        self.store = JsonFileStore()
        self._compact_existing_history()

    @staticmethod
    def _slice_list(values, limit: int = 8):
        if not isinstance(values, list):
            return []
        return values[:limit]

    def _compact_asset_context(self, asset_context: dict | None) -> dict:
        if not isinstance(asset_context, dict):
            return {}
        compact = {}
        for key in (
            "asset_name",
            "asset_ip",
            "environment",
            "source_file",
            "host",
            "hostname",
            "user",
            "operator",
            "source_role",
        ):
            value = asset_context.get(key)
            if value not in (None, "", [], {}):
                compact[key] = value
        if asset_context.get("source_files"):
            compact["source_files"] = self._slice_list(asset_context.get("source_files"), limit=6)
        return compact

    def _compact_jumpserver_summary(self, payload: dict) -> dict:
        compact = {}
        if payload.get("login_summary"):
            summary = payload["login_summary"]
            compact["login_summary"] = {
                "total_records": summary.get("total_records"),
                "success_count": summary.get("success_count"),
                "failure_count": summary.get("failure_count"),
                "top_failed_accounts": self._slice_list(summary.get("top_failed_accounts"), limit=6),
                "proxy_ips": self._slice_list(summary.get("proxy_ips"), limit=4),
            }
        if payload.get("command_summary"):
            summary = payload["command_summary"]
            compact["command_summary"] = {
                "total_rows": summary.get("total_rows"),
                "effective_command_count": summary.get("effective_command_count"),
                "high_risk_action_labels": summary.get("high_risk_action_labels"),
                "top_operator_counts": self._slice_list(summary.get("top_operator_counts"), limit=6),
            }
        if payload.get("file_transfer_summary"):
            summary = payload["file_transfer_summary"]
            compact["file_transfer_summary"] = {
                "total_rows": summary.get("total_rows"),
                "top_uploads": self._slice_list(summary.get("top_uploads"), limit=5),
            }
        if payload.get("operation_summary"):
            summary = payload["operation_summary"]
            compact["operation_summary"] = {
                "total_rows": summary.get("total_rows"),
                "action_counts": summary.get("action_counts"),
                "resource_counts": summary.get("resource_counts"),
                "top_operators": self._slice_list(summary.get("top_operators"), limit=6),
                "export_actions": summary.get("export_actions"),
                "host_or_account_creation": summary.get("host_or_account_creation"),
                "authorization_updates": summary.get("authorization_updates"),
            }
        if payload.get("risk_classification"):
            compact["risk_classification"] = payload.get("risk_classification")
        if payload.get("high_risk_accounts"):
            compact["high_risk_accounts"] = self._slice_list(payload.get("high_risk_accounts"), limit=6)
        if payload.get("cross_source_correlations"):
            compact["cross_source_correlations"] = self._slice_list(payload.get("cross_source_correlations"), limit=6)
        if payload.get("recommended_followups"):
            compact["recommended_followups"] = self._slice_list(payload.get("recommended_followups"), limit=6)
        if payload.get("boundary_rules"):
            compact["boundary_rules"] = self._slice_list(payload.get("boundary_rules"), limit=6)
        if payload.get("supplemental_sources"):
            compact["supplemental_sources"] = self._slice_list(payload.get("supplemental_sources"), limit=4)
        if payload.get("sources"):
            compact["source_count"] = len(payload.get("sources") or [])
        return {k: v for k, v in compact.items() if v not in (None, "", [], {})}

    def _compact_payload(self, payload: dict | None) -> dict:
        if not isinstance(payload, dict):
            return {}
        compact = {}
        for key in ("parser_profile", "filename", "target", "row_count", "generated_at", "mode"):
            value = payload.get(key)
            if value not in (None, "", [], {}):
                compact[key] = value
        jumpserver_bits = self._compact_jumpserver_summary(payload)
        compact.update(jumpserver_bits)
        if not compact:
            for key in ("title", "name", "type"):
                value = payload.get(key)
                if value not in (None, "", [], {}):
                    compact[key] = value
        return compact

    def _compact_raw_event_record(self, record: dict) -> dict:
        return {
            "source_type": record.get("source_type"),
            "event_hint": record.get("event_hint"),
            "timestamp": record.get("timestamp"),
            "asset_context": self._compact_asset_context(record.get("asset_context")),
            "payload": self._compact_payload(record.get("payload")),
        }

    def _compact_normalized_event_record(self, record: dict) -> dict:
        normalized = record.get("normalized_event") or {}
        classification = record.get("classification") or {}
        return {
            "normalized_event": {
                "event_id": normalized.get("event_id"),
                "event_type": normalized.get("event_type"),
                "source_type": normalized.get("source_type"),
                "timestamp": normalized.get("timestamp"),
                "asset_context": self._compact_asset_context(normalized.get("asset_context")),
                "normalized_data": self._compact_payload(normalized.get("normalized_data")),
            },
            "classification": {
                "classification": classification.get("classification"),
                "priority": classification.get("priority"),
                "reason": classification.get("reason"),
            },
        }

    def _compact_report_record(self, record: dict) -> dict:
        compact = deepcopy(record)
        observability = compact.get("observability")
        if isinstance(observability, dict):
            compact["observability"] = {
                "pipeline_latency_ms": observability.get("pipeline_latency_ms"),
                "skill_execution_time_ms": observability.get("skill_execution_time_ms"),
                "classification": observability.get("classification"),
                "report_title": observability.get("report_title"),
                "report_template": observability.get("report_template"),
            }
        for finding in compact.get("findings", []) if isinstance(compact.get("findings"), list) else []:
            if isinstance(finding, dict) and isinstance(finding.get("evidence"), list):
                finding["evidence"] = finding["evidence"][:5]
        return compact

    def _compact_record_for_path(self, path, record: dict) -> dict:
        if path == RAW_EVENTS_FILE:
            return self._compact_raw_event_record(record)
        if path == EVENTS_FILE:
            return self._compact_normalized_event_record(record)
        if path == REPORTS_FILE:
            return self._compact_report_record(record)
        if path == INVESTIGATIONS_FILE:
            return self._normalize_investigation(record)
        return record

    def _compact_existing_history(self) -> None:
        for path in (RAW_EVENTS_FILE, EVENTS_FILE, REPORTS_FILE, INVESTIGATIONS_FILE):
            original = self.store.list_records(path, limit=200)
            compacted = [self._compact_record_for_path(path, item) for item in original]
            if compacted != original:
                write_json(path, compacted)

    def _compact_archive_item(self, item: dict) -> dict:
        raw_event = item.get("raw_event") or {}
        normalized_event = item.get("normalized_event") or {}
        planner_preview = item.get("planner_preview") or {}
        report = item.get("report") or {}
        return {
            "filename": item.get("filename"),
            "raw_event": self._compact_raw_event_record(raw_event),
            "normalized_event": {
                "event_id": normalized_event.get("event_id"),
                "event_type": normalized_event.get("event_type"),
                "source_type": normalized_event.get("source_type"),
                "timestamp": normalized_event.get("timestamp"),
                "asset_context": self._compact_asset_context(normalized_event.get("asset_context")),
                "normalized_data": normalized_event.get("normalized_data") or {},
            },
            "planner_preview": {
                "skills_to_execute": planner_preview.get("skills_to_execute"),
                "analysis_reason": planner_preview.get("analysis_reason"),
                "classification": planner_preview.get("classification"),
            },
            "report": self._compact_report_record(report),
        }

    def save_investigation_archive(self, investigation_id: str, items: list[dict]) -> dict:
        ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
        payload = {
            "investigation_id": investigation_id,
            "archived_at": datetime.now(timezone.utc).isoformat(),
            "result_count": len(items),
            "items": [self._compact_archive_item(item) for item in items],
        }
        archive_path = ARCHIVE_DIR / f"{investigation_id}.json.gz"
        with gzip.open(archive_path, "wt", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False)
        return {
            "archive_path": str(archive_path),
            "archive_size_bytes": archive_path.stat().st_size,
            "archive_format": "json.gz",
        }

    @staticmethod
    def _is_composite_investigation_file(file_entry: dict) -> bool:
        return (
            file_entry.get("source_type") == "jumpserver"
            and file_entry.get("event_type") == "jumpserver_multi_source_audit"
        )

    def _normalize_investigation(self, investigation: dict) -> dict:
        files = investigation.get("files") or []
        if not files:
            return investigation
        visible_files = [
            file_entry
            for file_entry in files
            if isinstance(file_entry, dict) and not self._is_composite_investigation_file(file_entry)
        ]
        normalized = dict(investigation)
        normalized["file_count"] = len(visible_files) or int(investigation.get("file_count") or 0)
        normalized["result_count"] = len(files) or int(
            investigation.get("result_count") or investigation.get("file_count") or 0
        )
        return normalized

    def save_raw_event(self, raw_event: RawEvent) -> None:
        self.store.append(RAW_EVENTS_FILE, self._compact_raw_event_record(raw_event.model_dump(mode="json")))

    def save_normalized_event(self, envelope: EventEnvelope) -> None:
        self.store.append(EVENTS_FILE, self._compact_normalized_event_record(envelope.model_dump(mode="json")))

    def save_report(self, report: SecurityReport) -> None:
        self.store.append(REPORTS_FILE, self._compact_report_record(report.model_dump(mode="json")))

    def save_investigation(self, investigation: dict) -> None:
        self.store.append(INVESTIGATIONS_FILE, self._normalize_investigation(investigation), limit=100)

    def list_raw_events(self) -> list[dict]:
        return self.store.list_records(RAW_EVENTS_FILE, limit=30)

    def list_events(self) -> list[dict]:
        return self.store.list_records(EVENTS_FILE, limit=30)

    def list_reports(self) -> list[dict]:
        return self.store.list_records(REPORTS_FILE, limit=30)

    def list_investigations(self) -> list[dict]:
        items = self.store.list_records(INVESTIGATIONS_FILE, limit=30)
        return [self._normalize_investigation(item) for item in items]
