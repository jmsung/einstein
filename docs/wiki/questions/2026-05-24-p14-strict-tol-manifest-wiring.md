---
type: question
author: agent
drafted: 2026-05-24
asked_by: autonomous_loop (cycle 50/51)
related_problems: [14]
status: open
related_concepts: [float64-ceiling, arena-tolerance-drift]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/newton_max.py
  - scripts/circle_packing_square/polish.py
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
---

# Wire a strict-tol-safe default optimizer into the P14 manifest

## The question

What is the minimal change to `src/einstein/optimizer_manifest.yaml` (and possibly to
`scripts/circle_packing_square/polish.py`) that makes the autonomous loop's default
P14 dispatch produce a **strict tol=0 disjoint** candidate, instead of a
strict-tol-unsafe one or a `dispatch-failed: exit 1`?

## Why this is open

Currently P14 is the only problem with a manifest entry in
`optimizer_manifest.yaml` whose default optimizer is **incompatible with axiom A1**
(triple-verify). `newton_max` defaults to `--pair-gap=-9e-10`, which is the
arena-tolerance-band exploit the project explicitly rejected on 2026-04-09 (see
P14 experiment log, "The 'false breakthrough' trap"). Cycles 47–49 of the autonomous
loop all hit either `dispatch-failed` (missing warm-start file) or a strict-tol-unsafe
candidate; cycle 50 marked the problem converged-with-manifest-blocker; this question
makes the blocker explicit and addressable.

## What an answer looks like

A concrete diff that:

1. Adds a `slsqp_polish` (or similarly named) block to `optimizer_manifest.yaml` for
   problem 14, pointing at a thin wrapper around
   `src/einstein/circle_packing_square/polish.py` that:
   - Reads the canonical Packomania n=26 / AlphaEvolve warm-start from a path that
     **lives inside the repo or is materialised by the script** (not from `results-temp/`).
   - Runs SLSQP at strict tol=0 (`pair_gap=0`, `wall_gap=0`).
   - Emits `{"score": float, "payload": {"circles": [[cx, cy, r] × 26]}}` to a
     deterministic `results/circle_packing_square/slsqp_polish_result.json`.
2. Sets `default: slsqp_polish`.
3. Keeps `newton_max` available but **not default**, with a docstring note that it is
   strict-tol-unsafe by design and should only be invoked with explicit
   `--pair-gap 0` if used at all.
4. Adds a minimal test that exercises the dispatch path end-to-end (e.g. `tests/test_p14_dispatch_strict_tol.py`)
   confirming the result file shape and that the score lands within 1 ulp of 2.6359830849175.

## Why not just remove the entry

Removing the manifest entry would mean every P14 cycle returns "no manifest entry" and
the loop produces zero usable signal on P14 — which would be honest but wasteful given
the float64-ceiling state is a useful sanity baseline (any drift means something
upstream broke).

## Suggested next step

Open a sibling branch (not this autonomous-loop branch) to land the wire-fix. This
question stays open until that PR merges; once merged, close with `status: answered,
answer_finding: <path to the wire-fix commit + a follow-up finding noting cycles now
return strict-tol-safe scores>`.

## Cross-refs

- [dead-end-newton-max-strict-tol-lockout-p14](../findings/dead-end-newton-max-strict-tol-lockout-p14.md)
- [arena-proximity-guard](../findings/arena-proximity-guard.md)
- [float64-ceiling](../findings/float64-ceiling.md)

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"float64 ceiling" OR all:"arena tolerance drift" OR all:"Wire a strict-tol-safe default optimizer into") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
