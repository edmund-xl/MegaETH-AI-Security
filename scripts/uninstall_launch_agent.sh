#!/usr/bin/env bash
# Security-log-analysis mainline launch-agent remover.
set -euo pipefail

PORT="${PORT:-8011}"
LABEL="ai.megaeth.security.${PORT}"
PLIST_PATH="${HOME}/Library/LaunchAgents/${LABEL}.plist"

launchctl bootout "gui/$(id -u)/${LABEL}" >/dev/null 2>&1 || true
rm -f "${PLIST_PATH}"

echo "LaunchAgent removed."
echo "Label: ${LABEL}"
