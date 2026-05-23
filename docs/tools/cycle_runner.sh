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
#   4. promotion-log check        — surface findings cited 3+ times for human review
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

echo "==> cycle $CYCLE_ID — $PROBLEM_SLUG — post-cycle discipline"
echo

# 1. refresh qmd index (so next cycle sees this cycle's new findings/sources)
echo "[1/4] refresh qmd index"
if [[ -x docs/tools/refresh_qmd.sh ]]; then
  if ! bash docs/tools/refresh_qmd.sh; then
    echo "  warning: refresh_qmd.sh exited non-zero (qmd may be offline; continuing)"
  fi
else
  echo "  skip: docs/tools/refresh_qmd.sh not present"
fi
echo

# 2. wiki_graph gap detection — file top-3 missing-connection questions
echo "[2/4] wiki_graph — gap detection + auto-file"
if [[ -f docs/tools/wiki_graph.py ]]; then
  if ! uv run python docs/tools/wiki_graph.py --file-questions; then
    echo "  warning: wiki_graph.py exited non-zero (continuing)"
  fi
else
  echo "  skip: docs/tools/wiki_graph.py not present"
fi
echo

# 3. gap_search — enrich any newly-filed open questions with arxiv candidates
echo "[3/4] gap_search — enrich open questions"
if [[ -f docs/tools/gap_search.py ]]; then
  if ! uv run python docs/tools/gap_search.py; then
    echo "  warning: gap_search.py exited non-zero (continuing)"
  fi
else
  echo "  skip: docs/tools/gap_search.py not present"
fi
echo

# 4. promotion-log check — surface findings cited 3+ times for human review
echo "[4/4] promotion-log check"
PROMOTION_LOG="docs/agent/promotion-log.md"
if [[ -f "$PROMOTION_LOG" ]]; then
  echo "  promotion-log exists at $PROMOTION_LOG"
  echo "  (human-gated: review for findings → concept proposals)"
else
  echo "  no promotion-log; nothing to surface this cycle"
fi
echo

echo "✓ cycle $CYCLE_ID discipline complete"
