---
type: question
author: agent
drafted: 2026-05-27
asked_by: autonomous_loop
status: open
related_problems: [14]
related_concepts: [float64-ceiling, basin-rigidity, arena-tolerance-drift]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/newton_max.py
  - docs/wiki/findings/p14-manifest-wired-slsqp-polish.md
---

# Should `newton_max` be wired as a strict-tol alternate code path for P14, or removed from the manifest?

## Why this came up

Cycle 53 (2026-05-27) of the autonomous loop picked `newton_max` for P14 to exercise an alternate code path against the default `slsqp_polish` — a structural triple-verify check #2 per axiom A1 (same basin, different optimizer, expected same float64 ceiling within tol).

The dispatch silently returned no score. Reading the script + manifest reveals three wiring mismatches that prevent `newton_max` from being dispatched at all:

1. **Warm-start path**: `newton_max.py` defaults `--base=results-temp/p14_top.json`, which does not exist in any worktree. `slsqp_polish.py` uses an in-repo canonical seed at `scripts/circle_packing_square/seeds/p14_canonical.json` (per the manifest-wire-fix finding). Manifest `cli_args: ["--pair-gap", "0"]` does not override `--base`.
2. **Output path**: `newton_max.py` defaults `--output=results-temp/p14_newton.json`. The manifest's `result_file: results/circle_packing_square/newton_max_result.json` is never written. Dispatcher's `_parse_result` returns `result_file missing`.
3. **Result schema**: even if the output path were correct, `newton_max` emits `{"circles": ..., "sum_r": float, "pair_gap": ..., "wall_gap": ...}`. The `json_score_payload` parser requires `{"score": float, "payload": {...}}`. Score field name mismatch → parse failure.

## What an answer would look like

Either (a) keep `newton_max` as a usable strict-tol alternate by adding `cli_args: ["--pair-gap", "0", "--base", "<canonical-seed>", "--output", "results/circle_packing_square/newton_max_result.json"]` AND wrapping its output to `{"score": sum_r, "payload": {"circles": circles}}` (either in-script or via a thin shim), or (b) remove `newton_max` from the manifest entirely if the basin-rigidity finding makes the alternate code path redundant.

Option (a) is the right call if newton_max produces a different residual profile than slsqp_polish (genuine triple-verify check #2). Option (b) is right if both optimizers necessarily converge to the same float64 representation of the basin (then slsqp_polish + mpmath ulp polish is the more useful pair).

## Suggested next step

A 30-minute experiment: shim newton_max under option (a), dispatch it, compare the 26-radius vector against slsqp_polish's. If max-abs delta < 1e-15 across all radii, the alternate path is redundant — go with option (b). Otherwise the wiring is worth keeping.

## Closes when

A follow-up cycle merges the manifest fix (or the manifest entry removal) AND a finding documents the diagnostic outcome.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"float64 ceiling" OR all:"basin rigidity" OR all:"Should `newton_max` be wired as a") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
