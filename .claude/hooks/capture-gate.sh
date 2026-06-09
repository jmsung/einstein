#!/usr/bin/env bash
# Stop hook — capture gate for the einstein self-improvement loop.
#
# Blocks a "clean" session/cycle end unless this cycle produced (a) a new
# docs/agent/cycle-log.md row AND (b) ≥1 new/edited docs/wiki/findings|concepts
# page with valid attribution frontmatter + ≥1 cite. This makes the
# `cycle-discipline` + `failure-is-a-finding` rules deterministic instead of
# discretionary (design: docs/agent/meta-learning-automation.md, Gap 2 / Phase 0).
#
# Mode (EINSTEIN_CAPTURE_GATE): warn (default) | block | off
#   warn  — emit the reason to stderr, allow the stop (non-trapping; first rollout)
#   block — block the stop (exit 2) so the agent must capture; honors the
#           stop_hook_active guard so it blocks at most once (never traps mid-debug)
#   off   — disabled
# Base ref: EINSTEIN_CAPTURE_GATE_BASE (default: main). The autonomous per-cycle
# loop sets this to the pre-cycle HEAD so the gate scopes to one cycle.
set -euo pipefail

mode="${EINSTEIN_CAPTURE_GATE:-warn}"
[ "$mode" = "off" ] && exit 0

input=$(cat)
stop_active=$(printf '%s' "$input" | jq -r '.stop_hook_active // false' 2>/dev/null || echo false)

proj="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
base="${EINSTEIN_CAPTURE_GATE_BASE:-main}"

# capture_gate.py: exit 0 (+ "OK …") on pass / un-evaluable; exit 1 (+ reason) on fail.
if msg=$(python3 "$proj/docs/tools/capture_gate.py" --repo "$proj" --base "$base" 2>/dev/null); then
  exit 0
fi

# Gate failed. In block mode, block once (stop_hook_active guards against trapping
# the forced continuation); otherwise warn-then-log.
if [ "$mode" = "block" ] && [ "$stop_active" != "true" ]; then
  echo "$msg" >&2
  exit 2
fi
echo "⚠️  $msg" >&2
exit 0
