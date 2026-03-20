#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT="${PORT:-8010}"
PID_FILE="${ROOT_DIR}/.run-${PORT}.pid"
LOG_FILE="${ROOT_DIR}/.run-${PORT}.log"
SCREEN_NAME="megaeth-ai-security-${PORT}"

if [ -f "${ROOT_DIR}/.env.local" ]; then
  # Load local-only secrets without committing them into the repository.
  set -a
  . "${ROOT_DIR}/.env.local"
  set +a
fi

if command -v python3.13 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3.13)"
elif command -v python3.12 >/dev/null 2>&1; then
  PYTHON_BIN="$(command -v python3.12)"
else
  PYTHON_BIN="$(command -v python3)"
fi

cd "${ROOT_DIR}"
unset PYTHONPATH

if [ ! -d "${ROOT_DIR}/.venv" ]; then
  "$PYTHON_BIN" -m venv "${ROOT_DIR}/.venv"
  "${ROOT_DIR}/.venv/bin/pip" install -r "${ROOT_DIR}/requirements.txt"
fi

if [ -f "${PID_FILE}" ] && kill -0 "$(cat "${PID_FILE}")" 2>/dev/null; then
  echo "MegaETH AI Security is already running on port ${PORT} (pid $(cat "${PID_FILE}"))."
  exit 0
fi

rm -f "${PID_FILE}"
touch "${LOG_FILE}"

screen -S "${SCREEN_NAME}" -X quit >/dev/null 2>&1 || true
screen -dmS "${SCREEN_NAME}" /bin/sh -c "exec \"${ROOT_DIR}/scripts/run_server.sh\" >> \"${LOG_FILE}\" 2>&1"

for _ in $(seq 1 30); do
  if lsof -ti tcp:"${PORT}" >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

if ! lsof -ti tcp:"${PORT}" >/dev/null 2>&1; then
  echo "Failed to start MegaETH AI Security on port ${PORT}."
  echo "Check log: ${LOG_FILE}"
  exit 1
fi

PID="$(lsof -tiTCP:"${PORT}" -sTCP:LISTEN | head -n 1)"

echo "${PID}" > "${PID_FILE}"

echo "MegaETH AI Security started on http://127.0.0.1:${PORT}"
echo "PID: ${PID}"
echo "Log: ${LOG_FILE}"
