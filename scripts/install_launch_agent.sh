#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${PORT:-8010}"
LABEL="ai.megaeth.security.${PORT}"
LAUNCH_AGENTS_DIR="${HOME}/Library/LaunchAgents"
PLIST_PATH="${LAUNCH_AGENTS_DIR}/${LABEL}.plist"
LOG_FILE="${ROOT_DIR}/.run-${PORT}.log"
BOOT_LOG_FILE="${ROOT_DIR}/.launchd-${PORT}.log"
LINK_PATH="${HOME}/megaeth-ai-security-rebuild"

mkdir -p "${LAUNCH_AGENTS_DIR}"
touch "${LOG_FILE}"
touch "${BOOT_LOG_FILE}"
ln -sfn "${ROOT_DIR}" "${LINK_PATH}"

cat > "${PLIST_PATH}" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>Label</key>
    <string>${LABEL}</string>
    <key>ProgramArguments</key>
    <array>
      <string>/bin/bash</string>
      <string>${LINK_PATH}/scripts/launch_agent_start.sh</string>
    </array>
    <key>EnvironmentVariables</key>
    <dict>
      <key>PORT</key>
      <string>${PORT}</string>
      <key>PATH</key>
      <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
      <key>HOME</key>
      <string>${HOME}</string>
    </dict>
    <key>WorkingDirectory</key>
    <string>${LINK_PATH}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>${BOOT_LOG_FILE}</string>
    <key>StandardErrorPath</key>
    <string>${BOOT_LOG_FILE}</string>
  </dict>
</plist>
PLIST

launchctl bootout "gui/$(id -u)/${LABEL}" >/dev/null 2>&1 || true
launchctl bootstrap "gui/$(id -u)" "${PLIST_PATH}"
launchctl enable "gui/$(id -u)/${LABEL}" >/dev/null 2>&1 || true
launchctl kickstart -k "gui/$(id -u)/${LABEL}"

echo "LaunchAgent installed."
echo "Label: ${LABEL}"
echo "Plist: ${PLIST_PATH}"
echo "Service: http://127.0.0.1:${PORT}"
