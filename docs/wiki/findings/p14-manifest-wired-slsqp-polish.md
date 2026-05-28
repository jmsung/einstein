---
type: finding
author: agent
drafted: 2026-05-27
question_origin: docs/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md
status: answered
related_problems: [14]
related_concepts: [float64-ceiling, basin-rigidity]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/slsqp_polish.py
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
  - docs/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md
---

# P14 manifest now exposes strict-tol-safe default (`slsqp_polish`)

## What was open

Cycles 50/51 of the autonomous loop diagnosed that P14's manifest entry defaulted to `newton_max --pair-gap=-9e-10`, the arena-tolerance-band exploit that produced the 2026-04-09 false-breakthrough (would-be 500-pt penalty). Loop cycles either `dispatch-failed` or returned strict-tol-unsafe candidates. Question filed in `2026-05-24-p14-strict-tol-manifest-wiring.md`.

## What changed

`src/einstein/optimizer_manifest.yaml` now lists:

- `default: slsqp_polish` — new wrapper `scripts/circle_packing_square/slsqp_polish.py` runs `polish.polish()` at `overlap_slack=0.0` from an in-repo canonical warm-start (`scripts/circle_packing_square/seeds/p14_canonical.json`), emits `{"score": float, "payload": {"circles": ...}}` to `results/circle_packing_square/slsqp_polish_result.json`.
- `newton_max` retained but **not default**, forced to `--pair-gap 0` via manifest `cli_args` so even an explicit pick stays strict-tol-safe.

## Confirmation (cycle 52, 2026-05-27)

`uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish` returns `score=2.6359830849175245` — the canonical strict-tol-disjoint basin floor documented in `mb/problems/14-circle-packing-square/experiment-log.md`. Result file shape matches `json_score_payload` parser.

## What this rules out

- The "dispatch-failed / strict-tol-unsafe default" blocker that wedged P14 cycles 47–51 is resolved structurally.
- P14 is now a usable sanity baseline: any future dispatch drifting from `2.6359830849175245` flags upstream breakage (polish.py, warm-start, evaluator).

## What this does NOT do

- Does not improve the rank-2 score. P14 remains basin-locked at the float64 ceiling. AlphaEvolve's `2.6359830849176` (~8e-14 above ours) is the float64 ceiling for the AE basin and not crossable without higher-precision arithmetic on a different basin.
- Does not address the broader question of whether a strict-improvement P14 result exists at all — Packomania's 30-year-known-optimal status suggests no.

## Closes

[2026-05-24-p14-strict-tol-manifest-wiring](../questions/2026-05-24-p14-strict-tol-manifest-wiring.md) — status flipped to `answered`.
