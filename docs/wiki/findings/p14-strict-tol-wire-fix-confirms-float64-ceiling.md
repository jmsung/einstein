---
type: finding
author: agent
drafted: 2026-05-27
question_origin: problem-14
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift, basin-rigidity, contact-graph-rigidity]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/slsqp_polish.py
  - scripts/circle_packing_square/seeds/p14_canonical.json
  - tests/circle_packing_square/test_slsqp_polish_dispatch.py
  - results/circle_packing_square/slsqp_polish_result.json
  - docs/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
---

# P14 strict-tol wire-fix lands — autonomous loop now reproduces the float64 ceiling

## The question this answers

`questions/2026-05-24-p14-strict-tol-manifest-wiring.md` (cycles 50/51): the only
P14 optimizer the autonomous loop could dispatch was `newton_max`, which defaults to
the arena-tolerance-band exploit (`--pair-gap=-9e-10`) explicitly rejected after the
2026-04-09 false-breakthrough 500-pt scare. Cycles 47–49 hit `dispatch-failed`
(missing warm-start) or strict-tol-unsafe candidates; 50/51 marked the problem
converged-with-manifest-blocker.

## What resolved it

The wire-fix has landed in this branch. All four answer criteria from the question are met:

1. **`slsqp_polish` block added** — `scripts/circle_packing_square/slsqp_polish.py` wraps
   `polish()` at strict `overlap_slack=0.0`, reads an in-repo seed
   (`seeds/p14_canonical.json`, no dependence on gitignored `results-temp/`), and
   triple-verifies via `evaluate_strict()` before emitting `{"score", "payload"}`.
2. **`default: slsqp_polish`** in `optimizer_manifest.yaml` — dispatch with `strategy=None`
   now resolves the strict-tol path (test `test_p14_default_is_slsqp_polish`).
3. **`newton_max` kept but non-default**, with `cli_args: ["--pair-gap", "0"]` forcing
   strict-disjoint even on an explicit pick (test `test_p14_newton_max_still_available_but_strict`).
4. **End-to-end test** `tests/circle_packing_square/test_slsqp_polish_dispatch.py` asserts the
   result-file shape and that `evaluate_strict` round-trips the score within 1e-12.

## The reproduced number (triple-verify)

`results/circle_packing_square/slsqp_polish_result.json` → **2.6359830849175245**, the
rank-2-frozen float64 ceiling.

1. Fast evaluator (SLSQP polish loop) → 2.6359830849175245.
2. Independent reimpl: `evaluate_strict()` agrees to < 1e-12 (different code path; the
   script raises if any pair overlaps or wall is violated, so a written result *is* a
   strict-feasibility receipt).
3. Cross-check: matches the 30-year Packomania canonical n=26 basin; 8e-14 below the
   AlphaEvolve #1 ceiling; identical to the 2026-04-09 rank-2 submission.

Three-way agreement → the number is real, and it is the basin's float64 ceiling.

## What this rules out (and what it does NOT)

- **Does not** reopen the math dead-end: `newton_max`'s sub-ulp "improvements" still fail
  strict tol=0 — the arena-tolerance exploit remains rejected. The finding
  `dead-end-newton-max-strict-tol-lockout-p14.md` stands at the math level.
- **Does** close the *infrastructure* blocker: the loop now has a strict-tol-safe default,
  so P14 cycles produce a clean float64-ceiling baseline instead of `dispatch-failed`.
  Any future drift off 2.6359830849175245 means something upstream broke — a useful sentinel.

## What might still move the needle (none of it via more compute on this basin)

P14 is basin-locked. The original 10-approach parallel survey + 6 autonomous cycles all
land here. A genuine improvement would require a *different basin* (none found in 30 years
of Packomania) — not more polishing. The honest next step is "leave it frozen as a
sentinel," not "hammer the optimizer."

## Cross-refs

- [dead-end-newton-max-strict-tol-lockout-p14](dead-end-newton-max-strict-tol-lockout-p14.md)
- [float64-ceiling](float64-ceiling.md)
- [arena-proximity-guard](arena-proximity-guard.md)
- [questions/2026-05-24-p14-strict-tol-manifest-wiring](../questions/2026-05-24-p14-strict-tol-manifest-wiring.md)
- [questions/2026-05-27-optimizer-dispatch-no-cli-inner-agent](../questions/2026-05-27-optimizer-dispatch-no-cli-inner-agent.md)
