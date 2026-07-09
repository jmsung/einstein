#!/usr/bin/env bash
# Refresh qmd indices for the einstein wiki + source collections.
#
# Run this after any commit that touches knowledge/wiki/ or knowledge/source/. The qmd index
# does NOT auto-detect new files; without this, the agent's NEXT cycle
# can't query its prior cycle's findings.
#
# Per .claude/rules/cycle-discipline.md: this script must run before
# end-of-cycle wrap-up. Failure to refresh = stale index = wiki-first
# rule produces wrong answers.
#
# Usage:
#   tools/refresh_qmd.sh                  # update + embed both collections
#   tools/refresh_qmd.sh --check          # report stale-doc count, no work
#
# Exits 0 on success; 1 if qmd is missing.

set -euo pipefail

# Disable Metal/GPU backend for node-llama-cpp.
# On macOS 26.4 + Apple clang 21 + node-llama-cpp 3.18.1, `qmd query` exits
# with `Abort trap: 6` (the documented Darwin Metal finalizer abort).
# CPU fallback is fast enough for our corpus (≤20s for a full hybrid
# query+rerank on ~1700 docs); embed is one-shot and unaffected.
# See: knowledge/wiki/findings/qmd-metal-embed-fix.md
export QMD_FORCE_CPU=1

if ! command -v qmd >/dev/null 2>&1; then
  echo "error: qmd not on PATH. install via 'npm install -g @tobilu/qmd' or equivalent." >&2
  exit 1
fi

if [[ "${1:-}" == "--check" ]]; then
  qmd status 2>&1 | grep -E "einstein-wiki|einstein-wiki-source|stale|need" || true
  exit 0
fi

echo "[1/2] qmd update — re-index file changes for einstein-wiki + einstein-wiki-source"
qmd update

echo "[2/2] qmd embed — generate vector embeddings for any new chunks"
qmd embed --max-batch-mb 50

echo
echo "✓ qmd indices refreshed. Sample check:"
qmd query "kronecker bridging threshold" -c einstein-wiki -n 1 2>&1 | grep -E "qmd://|Score:" | head -2
