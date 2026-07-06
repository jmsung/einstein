#!/usr/bin/env bash
# Run a command keeping the Mac awake for its whole lifetime. Prevents sleep from
# pausing long P7 solves (the 2026-07-06 offline-hour lesson). Usage:
#   scripts/prime/awake_run.sh <command...>
caffeinate -ims -w $$ &
exec "$@"
