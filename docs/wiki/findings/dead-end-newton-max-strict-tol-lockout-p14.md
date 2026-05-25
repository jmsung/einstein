---
type: finding
author: agent
drafted: 2026-05-24
question_origin: problem-14
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift, basin-rigidity]
cites:
  - scripts/circle_packing_square/newton_max.py
  - mb/problems/14-circle-packing-square/experiment-log.md
  - docs/wiki/findings/arena-proximity-guard.md
  - docs/wiki/problems/14-circle-packing-square.md
---

# Dead end: `newton_max` default config is strict-tol-unsafe on P14

## What we tried

Autonomous-loop cycles 47–49 attempted to invoke `scripts/circle_packing_square/newton_max.py`
via `einstein.optimizer_dispatch` (`optimizer_manifest.yaml` entry for problem 14).
The manifest sets `cli_args: []`, which means newton_max runs with its argparse defaults:

```python
--base    results-temp/p14_top.json      # warm-start, not present in repo
--pair-gap -9e-10                         # negative ⇒ allows pair overlap up to ~1e-9
--wall-gap 1e-13                          # tiny positive wall slack
--output  results-temp/p14_newton.json
```

Two symptoms observed across cycles:

- **Cycles 47, 48**: optimizer exited with code 1 (`dispatch-failed: optimizer exited with code 1`).
  Root cause: `results-temp/p14_top.json` is not present in the worktree (it lived in a
  prior session's results-temp/ which is gitignored). Newton has no warm start, raises on open.
- **Cycle 49**: even if a warm start were materialised, the default `--pair-gap=-9e-10`
  guarantees the produced solution is **strict-tol-unsafe**: every contact pair is allowed
  to overlap by up to 9e-10. The arena verifier on P14 is empirically strict on overlaps
  (per the P14 experiment log; cross-checked vs P17 which DOES tolerate ~7.5e-12). A score
  produced this way would be rejected on submission and the agent would burn a 500-pt
  penalty (the "false breakthrough trap" already paid for once on 2026-04-09).

## Why it failed

The optimizer is *intentionally* designed to exploit the arena's tolerance band — the
script's docstring states the design: "We exploit the arena's tolerance band: pair_gap = 9e-10
(within arena 1e-9 limit, with 1e-10 safety) lets every contact 'overlap' slightly,
inflating Σr_i versus the strict-zero baseline (= AlphaEvolve)."

That was an exploratory tool in the original 10-approach breadth search (cycle of 2026-04-08).
It was never meant to be the **default optimizer** invoked headlessly by an autonomous loop
without the strict-tol triple-verify gate (axiom A1) in front of it. Wiring it through
the manifest with empty `cli_args` skips that gate by construction.

This is a **structural lockout**, not a math failure: there is no math reason P14 cannot be
poked at again, only that the single optimizer exposed in the manifest cannot produce a
submission-safe candidate by default. Strict-tol-safe optimizers do exist in the repo:

- `scripts/circle_packing_square/polish.py` — SLSQP with strict-disjoint floor (the
  optimizer that actually produced the submitted rank-#2 score 2.6359830849175245).
- `src/einstein/circle_packing_square/polish.py` — the underlying library function.

Neither is wired into `optimizer_manifest.yaml`.

## What this rules out

- **Routing autonomous-loop cycles through `newton_max` with manifest defaults** —
  produces strict-tol-unsafe candidates (or, more commonly, exits 1 on missing warm-start).
  Every cycle that picks this path loses an attempt.
- **Treating "the manifest is the contract" as sufficient** — the manifest contract must
  ALSO encode the strict-tol gate. A default optimizer that requires arena-tolerance
  exploitation cannot be the default for a problem where triple-verify is mandatory.

## What might still work

- Wire `slsqp-polish` (existing `scripts/circle_packing_square/polish.py`) into
  `optimizer_manifest.yaml` as the new `default:` for problem 14, with a result_file
  emitter that writes `{"score": float, "payload": {"circles": [...]}}` per the
  `json_score_payload` parser contract. Demote `newton_max` to a non-default optimizer
  callable only with explicit `--pair-gap 0` (strict mode).
- For P14, the **score is float64-ceiling-locked** regardless — even a perfectly wired
  strict-tol optimizer would reproduce 2.6359830849175245. The wire-up matters for cycle
  hygiene (no more `dispatch-failed`) and for future strict-tol-aware exploration
  (e.g., mpmath-ulp-polish, which would replace newton_max's role correctly), not for
  rank improvement on P14 specifically.
- The open question
  [`docs/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md`](../questions/2026-05-24-p14-strict-tol-manifest-wiring.md)
  owns the wire-fix.

## See also

- [arena-proximity-guard](arena-proximity-guard.md) — the original recipe for catching
  the same trap pre-submission.
- [float64-ceiling](float64-ceiling.md) — why P14 has no headroom regardless of optimizer.
- [packing-techniques](packing-techniques.md) — the larger context.
