#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-8010}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="${ROOT_DIR}/.run-${PORT}.pid"
SCREEN_NAME="megaeth-ai-security-${PORT}"

if [ -f "${PID_FILE}" ]; then
  PID="$(cat "${PID_FILE}")"
  if kill -0 "${PID}" 2>/dev/null; then
    kill "${PID}" || true
    sleep 1
    kill -9 "${PID}" 2>/dev/null || true
  fi
  rm -f "${PID_FILE}"
fi

screen -S "${SCREEN_NAME}" -X quit 2>/dev/null || true
lsof -ti tcp:"$PORT" | xargs -r kill -9
