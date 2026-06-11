#!/usr/bin/env bash
# cycle_runner.sh — per-cycle discipline wrapper.
#
# Runs the cycle-end housekeeping required by .claude/rules/cycle-discipline.md:
#
#   1. refresh_qmd.sh             — re-index docs/wiki/ + docs/source/ in qmd
#   2. wiki_graph.py --file-questions
#                                 — gap detection: auto-file top-3 missing-
#                                   connection questions for next cycle
#   3. gap_search.py              — enrich open questions with arxiv candidates
#   4. wiki_lint.py               — structural health (orphans/broken cites/gaps)
#                                   + anti-bloat surface (near-dup/stale-uncited)
#   5. compounding_metrics.py     — refresh the auto metrics block in metrics.md
#   6. promotion-log check        — surface findings cited 3+ times for human review
#   7. dashboard.py               — regenerate mb/logs/dashboard.html status page
#
# Step ordering matters: refresh_qmd must run BEFORE wiki_graph (otherwise the
# new sources from this cycle are invisible to the gap detector); gap_search
# runs LAST because it appends "## Suggested sources" sections to the
# questions wiki_graph just filed.
#
# Idempotent — safe to run twice. autonomous_loop.py invokes this after each
# cycle attempt; can also be invoked manually as part of /worktree-done.
#
# Usage:
#   docs/tools/cycle_runner.sh <cycle_id> <problem_slug>
#   docs/tools/cycle_runner.sh 5 19-difference-bases
#
# Exits 0 on success, non-zero on any step failure.

set -euo pipefail

CYCLE_ID="${1:?usage: cycle_runner.sh <cycle_id> <problem_slug>}"
PROBLEM_SLUG="${2:?usage: cycle_runner.sh <cycle_id> <problem_slug>}"

cd "$(dirname "$0")/../.."   # repo root

# Goal 7.8b: regression-detect sentinel. Hard failures (wiki_lint exiting
# non-zero) drop `mb/.inner-agent-disabled` which 7.5's precheck honors.
# The human re-enables via `rm`. Other steps (refresh_qmd, gap_search) are
# soft warnings — transient infra issues shouldn't block cycles.
SENTINEL_PATH="${SENTINEL_PATH:-../mb/.inner-agent-disabled}"
HARD_FAIL_REASONS=""

echo "==> cycle $CYCLE_ID — $PROBLEM_SLUG — post-cycle discipline"
echo

# 1. refresh qmd index (so next cycle sees this cycle's new findings/sources)
echo "[1/7] refresh qmd index"
if [[ -x docs/tools/refresh_qmd.sh ]]; then
  if ! bash docs/tools/refresh_qmd.sh; then
    echo "  warning: refresh_qmd.sh exited non-zero (qmd may be offline; continuing)"
  fi
else
  echo "  skip: docs/tools/refresh_qmd.sh not present"
fi
echo

# 2. wiki_graph gap detection — file top-3 missing-connection questions
echo "[2/7] wiki_graph — gap detection + auto-file"
if [[ -f docs/tools/wiki_graph.py ]]; then
  if ! uv run python docs/tools/wiki_graph.py --file-questions; then
    echo "  warning: wiki_graph.py exited non-zero (continuing)"
  fi
else
  echo "  skip: docs/tools/wiki_graph.py not present"
fi
echo

# 3. gap_search — enrich any newly-filed open questions with arxiv candidates
echo "[3/7] gap_search — enrich open questions"
if [[ -f docs/tools/gap_search.py ]]; then
  if ! uv run python docs/tools/gap_search.py; then
    echo "  warning: gap_search.py exited non-zero (continuing)"
  fi
else
  echo "  skip: docs/tools/gap_search.py not present"
fi
echo

# 4. wiki_lint — structural health check (orphans / broken cites / body link gaps)
#    Hard failure (non-zero exit) → drop the regression-detect sentinel
#    (Goal 7.8b). Future cycles skip until a human inspects + `rm`s it.
echo "[4/7] wiki_lint — structural wiki health"
if [[ -f docs/tools/wiki_lint.py ]]; then
  if ! uv run python docs/tools/wiki_lint.py; then
    HARD_FAIL_REASONS="${HARD_FAIL_REASONS}wiki_lint exit non-zero;"
    echo "  HARD-FAIL: wiki_lint reported issues — sentinel will be dropped"
  fi
else
  echo "  skip: docs/tools/wiki_lint.py not present"
fi
echo

# 5. compounding metrics — refresh the auto block in metrics.md (Phase 4 of
#    meta-learning-automation). Cheap, best-effort, never hard-fails: it only
#    reads append-only logs and splices a marker-delimited block.
echo "[5/7] compounding metrics — refresh metrics.md"
if [[ -f docs/tools/compounding_metrics.py ]]; then
  if ! uv run python docs/tools/compounding_metrics.py --write; then
    echo "  warning: compounding_metrics.py exited non-zero (continuing)"
  fi
else
  echo "  skip: docs/tools/compounding_metrics.py not present"
fi
echo

# 6. promotion-log check — surface findings cited 3+ times for human review
echo "[6/7] promotion-log check"
PROMOTION_LOG="docs/agent/promotion-log.md"
if [[ -f "$PROMOTION_LOG" ]]; then
  echo "  promotion-log exists at $PROMOTION_LOG"
  echo "  (human-gated: review for findings → concept proposals)"
else
  echo "  no promotion-log; nothing to surface this cycle"
fi
echo

# 7. dashboard — regenerate the local status page (best-effort; never hard-fails).
#    Read-only over the ledgers; a render failure must not block a cycle.
echo "[7/7] dashboard — regenerate status page"
if [[ -f docs/tools/dashboard.py ]]; then
  if ! uv run python docs/tools/dashboard.py >/dev/null; then
    echo "  warning: dashboard.py exited non-zero (continuing)"
  fi
else
  echo "  skip: docs/tools/dashboard.py not present"
fi
echo

if [[ -n "$HARD_FAIL_REASONS" ]]; then
  echo
  echo "==> HARD REGRESSION detected — writing sentinel"
  uv run python docs/tools/inner_agent_gates.py write-sentinel \
    "$SENTINEL_PATH" \
    --reason "cycle $CYCLE_ID ($PROBLEM_SLUG): $HARD_FAIL_REASONS" \
    --cycle-id "$CYCLE_ID"
  echo
  echo "Future autonomous cycles will skip until you:"
  echo "  rm $SENTINEL_PATH"
  exit 2
fi

echo "✓ cycle $CYCLE_ID discipline complete"
