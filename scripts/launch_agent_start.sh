#!/usr/bin/env bash
# Security-log-analysis mainline launch-agent bootstrap.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${PORT:-8011}"
BOOT_LOG_FILE="${ROOT_DIR}/.launchd-${PORT}.log"

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export HOME="${HOME:-/Users/lei}"

exec >> "${BOOT_LOG_FILE}" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] launch_agent_start.sh begin"
echo "ROOT_DIR=${ROOT_DIR}"
echo "PORT=${PORT}"
echo "PATH=${PATH}"
echo "HOME=${HOME}"

cd "${ROOT_DIR}"
./start.sh
status=$?
echo "[$(date '+%Y-%m-%d %H:%M:%S')] launch_agent_start.sh end status=${status}"
exit "${status}"
