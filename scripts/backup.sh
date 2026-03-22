#!/usr/bin/env bash
# Security-log-analysis mainline backup helper.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHIVE_DIR="${HOME}/Desktop/megaeth-ai-security-rebuild-archives"
STAMP="$(date +%Y%m%d-%H%M%S)"
NAME="megaeth-ai-security-rebuild-backup-${STAMP}.tar.gz"

mkdir -p "${ARCHIVE_DIR}"

tar \
  --exclude=".venv" \
  --exclude="__pycache__" \
  --exclude=".pytest_cache" \
  --exclude="dist" \
  -czf "${ARCHIVE_DIR}/${NAME}" \
  -C "${ROOT_DIR}" .

ls -1t "${ARCHIVE_DIR}"/megaeth-ai-security-rebuild-backup-*.tar.gz 2>/dev/null | awk 'NR>2' | xargs -r rm -f

echo "${ARCHIVE_DIR}/${NAME}"
