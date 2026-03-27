#!/usr/bin/env bash
# Security-log-analysis mainline release helper.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ARCHIVE_DIR="${HOME}/Desktop/megaeth-ai-security-rebuild-archives"
STAMP="$(date +%Y%m%d-%H%M%S)"
VERSION="$(cat "${ROOT_DIR}/VERSION")"
MANIFEST="${ARCHIVE_DIR}/release-manifest-${STAMP}.md"

required_files=(
  "README.md"
  "CHANGELOG.md"
  "VERSION"
  "docs/SYSTEM_DESIGN.md"
  "docs/FEATURE_SNAPSHOT.md"
  "docs/REBUILD_GUIDE.md"
  "docs/TRAINING_WORKFLOW.md"
  "docs/PORTABLE_TRANSFER.md"
  "scripts/backup.sh"
  "start.sh"
  "stop.sh"
)

for file in "${required_files[@]}"; do
  if [ ! -f "${ROOT_DIR}/${file}" ]; then
    echo "Missing required release file: ${file}" >&2
    exit 1
  fi
done

mkdir -p "${ARCHIVE_DIR}"

"${ROOT_DIR}/.venv/bin/python" -m pytest -q
"${ROOT_DIR}/scripts/audit_docs.py"

BACKUP_PATH="$("${ROOT_DIR}/scripts/backup.sh")"

{
  echo "# Release Manifest"
  echo
  echo "- Timestamp: ${STAMP}"
  echo "- Version: ${VERSION}"
  echo "- Root: ${ROOT_DIR}"
  echo "- Backup: ${BACKUP_PATH}"
  echo
  echo "## Included docs"
  for file in "${required_files[@]}"; do
    echo "- ${file}"
  done
  echo
  echo "## Data snapshot"
  find "${ROOT_DIR}/data" -maxdepth 1 -type f | sort | while read -r path; do
    bytes="$(wc -c < "${path}")"
    echo "- $(basename "${path}") : ${bytes} bytes"
  done
} > "${MANIFEST}"

ls -1t "${ARCHIVE_DIR}"/release-manifest-*.md 2>/dev/null | awk 'NR>2' | xargs -r rm -f

echo "${MANIFEST}"
