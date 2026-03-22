#!/bin/sh
set -eu

ROOT_DIR="$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"
unset PYTHONPATH

if [ -f "$ROOT_DIR/.env.local" ]; then
  set -a
  . "$ROOT_DIR/.env.local"
  set +a
fi

# Mainline runner for the security-log-analysis service.
exec "$ROOT_DIR/.venv/bin/python" "$ROOT_DIR/run_server.py"
