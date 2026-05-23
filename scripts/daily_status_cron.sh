#!/bin/bash
# Daily cron: refresh arena status, write to mb/logs/status/, update README.
# Logged via crontab redirect to mb/logs/status/cron.log.
set -euo pipefail
cd /Users/jmsung/projects/einstein/cb
echo "=== $(date -u +%FT%TZ) ==="
/opt/homebrew/bin/uv run python scripts/update_status.py
