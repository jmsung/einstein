#!/usr/bin/env bash
# build_ablation_repos.sh — clean-room Cold/Warm checkouts (pre-reg §7).
#
# Produces two air-gapped checkouts from the SAME commit that differ ONLY by the
# knowledge layer being physically absent. The Cold/Warm *behavioral* difference
# (run-kb persistence + reuse) is supplied later by the run driver (pre-reg §10.4)
# — both checkouts are identical on disk; the driver threads run-kb for Warm and
# wipes it for Cold. This script just guarantees neither checkout contains the
# pre-built knowledge base or any stored answer.
#
# Air-gap by construction, not by policing (pre-reg §7): a checkout that
# physically lacks the wiki/solutions cannot leak them.
#
# Usage:
#   scripts/build_ablation_repos.sh [COMMIT] [OUT_DIR]
#     COMMIT   git commit-ish to build from   (default: HEAD)
#     OUT_DIR  base dir for the two checkouts  (default: <repo>/ablation-build)
#
# Idempotent: re-running rebuilds both checkouts from scratch. Prints a manifest
# of everything removed (also written to <checkout>/AIR_GAP_MANIFEST.txt) so the
# air-gap is auditable, and self-verifies before exiting non-zero on any breach.
set -euo pipefail

COMMIT="${1:-HEAD}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
OUT_DIR="${2:-$REPO_ROOT/ablation-build}"

# --- the knowledge layer to remove from each clean-room checkout (pre-reg §7) ---
# Directories that are the pre-built knowledge base + stored answers.
KNOWLEDGE_DIRS=(
  "docs/wiki"
  "docs/source"
  "docs/agent"
)
# .claude/rules/ is stripped to the GENERIC subset only. These four (+ README
# index) are the keep-set — everything else in rules/ is the knowledge harness
# (wiki-first-lookup, council-dispatch, self-improvement-loop, wall-hit-escalation,
# cycle-discipline, wiki-attribution, ask-the-question-first, failure-is-a-finding,
# math-solving-protocol) and is removed.
KEEP_RULES=(
  "agent-stance.md"
  "triple-verify.md"
  "compute-router.md"
  "axioms.md"
  "README.md"
)
# Answer/solution dumps to remove wherever they appear.
SOLUTION_GLOBS=(
  "results"
  "solution-best.json"
)

resolved_commit="$(git rev-parse --short "$COMMIT")"
echo "build_ablation_repos: commit=$resolved_commit  out=$OUT_DIR"

build_one() {
  # $1 = arm name (cold|warm); checkout dir = $OUT_DIR/einstein-$1
  local arm="$1"
  local dir="$OUT_DIR/einstein-$arm"
  local manifest="$dir/AIR_GAP_MANIFEST.txt"

  # Idempotent: drop any prior worktree + dir.
  if git worktree list --porcelain | grep -qx "worktree $dir"; then
    git worktree remove --force "$dir"
  fi
  rm -rf "$dir"
  mkdir -p "$OUT_DIR"
  git worktree add --detach "$dir" "$COMMIT" >/dev/null

  {
    echo "# Air-gap manifest — einstein-$arm"
    echo "# built from commit $resolved_commit ($(git rev-parse "$COMMIT"))"
    echo "# $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo
    echo "## Removed knowledge directories (pre-reg §7)"
  } >"$manifest"

  local p
  for p in "${KNOWLEDGE_DIRS[@]}"; do
    if [[ -e "$dir/$p" ]]; then
      du -sh "$dir/$p" | sed 's/^/  removed  /' >>"$manifest"
      rm -rf "${dir:?}/$p"
    fi
  done

  echo >>"$manifest"
  echo "## Stripped .claude/rules/ to generic subset" >>"$manifest"
  if [[ -d "$dir/.claude/rules" ]]; then
    local f base keep
    for f in "$dir/.claude/rules/"*; do
      [[ -e "$f" ]] || continue
      base="$(basename "$f")"
      keep=0
      for k in "${KEEP_RULES[@]}"; do [[ "$base" == "$k" ]] && keep=1; done
      if [[ "$keep" == 0 ]]; then
        echo "  removed  .claude/rules/$base" >>"$manifest"
        rm -f "$f"
      else
        echo "  kept     .claude/rules/$base" >>"$manifest"
      fi
    done
  fi

  echo >>"$manifest"
  echo "## Removed solution / results dumps" >>"$manifest"
  for p in "${SOLUTION_GLOBS[@]}"; do
    if [[ -e "$dir/$p" ]]; then
      echo "  removed  $p" >>"$manifest"
      rm -rf "${dir:?}/$p"
    fi
  done
  # Any solution-best* anywhere in the tree.
  while IFS= read -r -d '' sol; do
    echo "  removed  ${sol#"$dir"/}" >>"$manifest"
    rm -f "$sol"
  done < <(find "$dir" -name 'solution-best*' -print0 2>/dev/null)

  # Warm gets an empty run KB it writes into during the run; Cold gets none.
  if [[ "$arm" == "warm" ]]; then
    mkdir -p "$dir/run-kb"
    : >"$dir/run-kb/.gitkeep"
    echo >>"$manifest"
    echo "## Created empty Warm run KB: run-kb/" >>"$manifest"
  fi

  echo "  [$arm] $dir"
  sed 's/^/    /' "$manifest"
}

verify_one() {
  # Assert the air-gap holds; exit non-zero on any breach (pre-reg §9 sanity).
  local arm="$1"
  local dir="$OUT_DIR/einstein-$arm"
  local p
  for p in "${KNOWLEDGE_DIRS[@]}"; do
    [[ -e "$dir/$p" ]] && { echo "VERIFY FAIL [$arm]: $p still present"; return 1; }
  done
  # removed knowledge rules must be gone
  for bad in wiki-first-lookup council-dispatch self-improvement-loop \
             wall-hit-escalation cycle-discipline wiki-attribution \
             ask-the-question-first failure-is-a-finding math-solving-protocol; do
    [[ -e "$dir/.claude/rules/$bad.md" ]] && { echo "VERIFY FAIL [$arm]: rule $bad.md still present"; return 1; }
  done
  # kept rules must remain
  local k
  for k in "${KEEP_RULES[@]}"; do
    [[ -e "$dir/.claude/rules/$k" ]] || { echo "VERIFY FAIL [$arm]: kept rule $k missing"; return 1; }
  done
  # shared infrastructure must remain (pre-reg §4)
  for p in src scripts tests; do
    [[ -d "$dir/$p" ]] || { echo "VERIFY FAIL [$arm]: $p/ missing"; return 1; }
  done
  if [[ "$arm" == "warm" ]]; then
    [[ -d "$dir/run-kb" ]] || { echo "VERIFY FAIL [warm]: run-kb/ missing"; return 1; }
  else
    [[ -e "$dir/run-kb" ]] && { echo "VERIFY FAIL [cold]: run-kb/ must not exist"; return 1; }
  fi
  echo "  [$arm] air-gap verified ✓"
}

build_one cold
build_one warm
echo "verifying air-gap..."
verify_one cold
verify_one warm
echo "done: $OUT_DIR/einstein-cold  $OUT_DIR/einstein-warm"
