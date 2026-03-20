from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.utils.store import DATA_DIR, ensure_dir


APPA_STATE_FILE = DATA_DIR / "appa_state.json"


def read_appa_state() -> dict[str, Any] | None:
    ensure_dir()
    if not APPA_STATE_FILE.exists():
        return None
    try:
        return json.loads(APPA_STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def write_appa_state(payload: dict[str, Any]) -> None:
    ensure_dir()
    APPA_STATE_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
