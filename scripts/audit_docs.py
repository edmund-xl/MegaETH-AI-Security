#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CN_PATTERN = re.compile(r"[\u4e00-\u9fff]")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED_BILINGUAL_ROOTS = {"docs", "skill_specs", "training_cases"}
REQUIRED_BILINGUAL_FILES = {"README.md", "CHANGELOG.md"}
EXCLUDED_DIRS = {
    ".git",
    ".venv",
    ".venv314-090014",
    ".venv-new-bad-20260316-085812",
    ".pytest_cache",
    "__pycache__",
}


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def requires_bilingual(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if rel.name in REQUIRED_BILINGUAL_FILES:
        return True
    return bool(rel.parts and rel.parts[0] in REQUIRED_BILINGUAL_ROOTS)


def check_bilingual(path: Path, text: str, errors: list[str]) -> None:
    if not requires_bilingual(path):
        return
    if "## 中文" not in text or "## English" not in text:
        errors.append(f"{path.relative_to(ROOT)}: missing bilingual section markers")
        return
    english = text.split("## English", 1)[1]
    if CN_PATTERN.search(english):
        errors.append(f"{path.relative_to(ROOT)}: Chinese text remains inside English section")


def check_links(path: Path, text: str, errors: list[str]) -> None:
    for target in LINK_PATTERN.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("/Users/"):
            errors.append(f"{path.relative_to(ROOT)}: contains local absolute link {target}")
            continue
        relative = target.split("#", 1)[0]
        if not relative:
            continue
        resolved = (path.parent / relative).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link {target}")


def main() -> int:
    errors: list[str] = []
    files = markdown_files()
    for path in files:
        text = path.read_text(encoding="utf-8")
        check_bilingual(path, text, errors)
        check_links(path, text, errors)
    if errors:
        print("Documentation audit failed:", file=sys.stderr)
        for item in errors:
            print(f"- {item}", file=sys.stderr)
        return 1
    print(f"Documentation audit passed for {len(files)} markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
