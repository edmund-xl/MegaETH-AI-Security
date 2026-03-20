#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8010}"
LABEL="ai.megaeth.security.${PORT}"
PLIST_PATH="${HOME}/Library/LaunchAgents/${LABEL}.plist"

launchctl bootout "gui/$(id -u)/${LABEL}" >/dev/null 2>&1 || true
rm -f "${PLIST_PATH}"

echo "LaunchAgent removed."
echo "Label: ${LABEL}"
