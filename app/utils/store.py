from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any
from datetime import datetime, timedelta, timezone


# Security-log-analysis mainline persistence paths.
DATA_DIR = Path(__file__).resolve().parents[2] / "data"
EVENTS_FILE = DATA_DIR / "events.json"
RAW_EVENTS_FILE = DATA_DIR / "raw_events.json"
REPORTS_FILE = DATA_DIR / "reports.json"
INVESTIGATIONS_FILE = DATA_DIR / "investigations.json"
MEMORY_RULES_FILE = DATA_DIR / "memory_rules.json"
MEMORY_FEEDBACK_FILE = DATA_DIR / "memory_feedback.json"
HISTORY_RETENTION_DAYS = 2

FILE_CONFIG: dict[Path, dict[str, Any]] = {
    EVENTS_FILE: {"timestamp_paths": ["normalized_event.timestamp"], "limit": 100},
    RAW_EVENTS_FILE: {"timestamp_paths": ["timestamp"], "limit": 100},
    REPORTS_FILE: {"timestamp_paths": ["generated_at"], "limit": 100},
    INVESTIGATIONS_FILE: {"timestamp_paths": ["created_at"], "limit": 100},
    MEMORY_RULES_FILE: {"timestamp_paths": ["updated_at", "created_at"], "limit": 200},
    MEMORY_FEEDBACK_FILE: {"timestamp_paths": ["created_at"], "limit": 200},
}

_READ_CACHE: dict[Path, tuple[int, int, list[dict[str, Any]]]] = {}


def ensure_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def read_json(path: Path) -> list[dict[str, Any]]:
    ensure_dir()
    if not path.exists():
        return []
    try:
        stat = path.stat()
        cached = _READ_CACHE.get(path)
        if cached and cached[0] == stat.st_mtime_ns and cached[1] == stat.st_size:
            return deepcopy(cached[2])
        payload = json.loads(path.read_text(encoding="utf-8"))
        _READ_CACHE[path] = (stat.st_mtime_ns, stat.st_size, payload)
        return deepcopy(payload)
    except json.JSONDecodeError:
        return []


def write_json(path: Path, payload: list[dict[str, Any]]) -> None:
    ensure_dir()
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    stat = path.stat()
    _READ_CACHE[path] = (stat.st_mtime_ns, stat.st_size, deepcopy(payload))


def _parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def _get_nested(record: dict[str, Any], dotted_path: str) -> Any:
    current: Any = record
    for part in dotted_path.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def _record_timestamp(record: dict[str, Any], path: Path) -> datetime | None:
    config = FILE_CONFIG.get(path, {})
    for ts_path in config.get("timestamp_paths", []):
        parsed = _parse_datetime(_get_nested(record, ts_path))
        if parsed:
            return parsed.astimezone(timezone.utc)
    return None


def prune_records(path: Path, payload: list[dict[str, Any]]) -> list[dict[str, Any]]:
    config = FILE_CONFIG.get(path, {})
    limit = int(config.get("limit", 200))
    if path in {EVENTS_FILE, RAW_EVENTS_FILE, REPORTS_FILE, INVESTIGATIONS_FILE}:
        cutoff = datetime.now(timezone.utc) - timedelta(days=HISTORY_RETENTION_DAYS)
        payload = [
            record
            for record in payload
            if (_record_timestamp(record, path) or datetime.now(timezone.utc)) >= cutoff
        ]
    return payload[:limit]


class JsonFileStore:
    def append(self, path: Path, record: dict[str, Any], limit: int = 200) -> None:
        data = read_json(path)
        data.insert(0, record)
        config_limit = int(FILE_CONFIG.get(path, {}).get("limit", limit))
        write_json(path, prune_records(path, data[:config_limit]))

    def list_records(self, path: Path, limit: int = 50) -> list[dict[str, Any]]:
        original = read_json(path)
        data = prune_records(path, original)
        if data != original:
            write_json(path, data)
        return data[:limit]

    def summary(self, path: Path) -> dict[str, Any]:
        original = read_json(path)
        data = prune_records(path, original)
        if data != original:
            write_json(path, data)
        latest = data[0] if data else None
        return {
            "count": len(data),
            "latest": latest,
        }
