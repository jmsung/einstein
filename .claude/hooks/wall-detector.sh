#!/usr/bin/env bash
# PostToolUse(Bash) — automatic wall detector for the einstein math loop.
#
# Counts consecutive HEAVY-COMPUTE launches with NO intervening wisdom step
# (qmd query / wall-ledger grep / council). At the threshold it emits a reminder
# to escalate per .claude/rules/wall-hit-escalation.md — making "consult wisdom
# when stuck" automatic instead of relying on the agent remembering.
#
# Non-blocking: writes to stderr, exits 0. Only counts compute commands; ignores
# git/ls/cat/etc. Resets the counter on any wisdom command.
set -euo pipefail

input=$(cat)
cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // empty' 2>/dev/null || true)
[ -z "$cmd" ] && exit 0

# per-session counter file (keyed by session id / transcript path)
key=$(printf '%s' "$input" | jq -r '.session_id // .transcript_path // "default"' 2>/dev/null \
       | tr -c 'A-Za-z0-9' '_')
state="${TMPDIR:-/tmp}/einstein-wall-${key}.count"
THRESHOLD=3

# WISDOM step → reset the counter (escalation happened).
if printf '%s' "$cmd" | grep -Eq 'qmd query|wall-ledger|wiki-query|wiki-research|knowledge/wiki/questions|/council'; then
  echo 0 > "$state"
  exit 0
fi

# HEAVY-COMPUTE launch (an optimizer/search run) → increment.
if printf '%s' "$cmd" | grep -Eq 'optimize_|escape_|basin_hop|_sweep|campaign_|frag_|spectral_|sign_flip|construction_battery|signed_dual|signed_descent|frozen_sign|tempering|multistart|cma_es|run_branch|autonomous_loop'; then
  n=$(cat "$state" 2>/dev/null || echo 0)
  n=$((n + 1))
  echo "$n" > "$state"
  if [ "$n" -ge "$THRESHOLD" ]; then
    cat >&2 <<EOF
⚠️  WALL PATTERN: $n consecutive compute launches with no wisdom step.
Per .claude/rules/wall-hit-escalation.md, STOP brute-forcing now:
  1. Name the obstruction (knowledge/wiki/questions/).
  2. grep docs/agent/wall-ledger.md for this obstruction — reuse a past resolving move if matched.
  3. qmd query einstein-wiki on the problem + obstruction + "dead-end".
  4. RE-DISPATCH the council seeded with what failed; implement ONE new move OUTSIDE the failed class.
  5. Append a wall-ledger row.
Do NOT launch another variant of a failed approach before escalating.
EOF
    echo 0 > "$state"   # reset so the reminder doesn't spam every subsequent call
  fi
fi
exit 0
