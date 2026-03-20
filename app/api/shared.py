from __future__ import annotations

from pathlib import Path

from app.core.pipeline import SecurityPipeline


pipeline = SecurityPipeline()
STATIC_DIR = Path(__file__).resolve().parents[1] / "static"
