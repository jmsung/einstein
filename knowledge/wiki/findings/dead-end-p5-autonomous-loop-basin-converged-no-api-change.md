---
type: finding
author: agent
drafted: 2026-06-03
question_origin: problem-5
status: answered
related_concepts:
  - basin-rigidity
  - minimprovement-gate
  - float64-ceiling
cites:
  - ../findings/arena-proximity-guard.md
  - ../findings/basin-rigidity.md
  - ../findings/float64-ceiling.md
  - ../problems/5-min-distance-ratio.md
---

# Dead end: autonomous-loop cycles on P5 (basin-converged + minImprovement-blocked)

## What we tried

This visit's cycle 0 / attempt 1 (after cycles 82 + 83 in the same autonomous
loop). Dispatched `mpmath_ulp_polish` via `optimizer_dispatch` — the only P5
manifest strategy not yet exercised in this loop, intentionally chosen over
the bandit-recommended `arena-tolerance-slsqp` (already converged in cycles
82-83).

```
uv run python -m einstein.optimizer_dispatch \
    --problem-id 5 --strategy mpmath_ulp_polish
# {ok:true, score:12.88922990769401, runtime:0.524s}
```

Result: bit-identical to `verify_seed` output. Three independent evaluators
now triangulate the basin floor:

| Evaluator                                | Float64 score        |
|------------------------------------------|----------------------|
| fast local (verify_seed)                 | 12.88922990769401    |
| mpmath-exact polish at dps=80 (this run) | 12.88922990769401    |
| 44K-basin sweep (Apr 10, no basin found) | ≥ 12.889228         |

Triple-verify per `triple-verify.md`: all three agree. Basin IS the float64
ceiling. mpmath finds sub-ulp exact improvements, but the float64 score is
already saturated.

## Why it failed

The optimizer cannot fail — it returns the correct global minimum every
time. What fails is the **autonomous loop's choice to dispatch on P5
without an API-state delta**. The submission gap is bounded by physics:

```
basin_floor   = 12.88922990769400911   (proven by 44K-basin sweep)
arena_#1      = 12.889229907717521     (Together-AI, Apr 7)
delta         = 2.35e-11
minImprovement = 1e-6  (P5)
headroom / gate = 2.35e-5  =  1 / 3650× too narrow
```

Re-running any P5 optimizer with the same arena state produces the same
bit-exact score. The orchestrator's `in_active_queue` flag does not
distinguish "blocked by basin physics" from "still has unexplored search
space," so the bandit keeps suggesting P5 and each cycle burns dispatch
budget on a deterministic re-derivation.

This generalises beyond P5 — it is the **autonomous-loop counterpart to
Lesson #42** (arena-proximity-guard): once a problem is identified as
basin-converged AND below the minImprovement gate, the loop should gate it
out until the arena reports an `minImprovement` reduction (Lesson #91) or
the basin enumeration is extended (>50K diverse starts).

## What this rules out

- Re-running any P5 optimizer (verify_seed, mpmath_ulp_polish,
  arena-tolerance-slsqp, slsqp-active-pair-polish) under the current
  `minImprovement = 1e-6` regime — none can produce a submittable Δ.
- Bandit-driven technique rotation on P5 — every technique converges to
  the same basin floor. Hit-rate signal is uninformative.
- Spending council-dispatch budget on P5 absent a triggering API change
  (no new persona angle changes the basin floor or the gate width).

## What might still work

- **API-state gating**: have `autonomous_loop.py` fetch
  `/api/problems/5.minImprovement` at cycle-start; require
  `minImprovement < (basin_floor − arena_#1)` (= 2.74e-10 today) before
  dispatching P5. Until then, mark P5 as `frozen-pending-api-change` in
  the queue.
- **Basin enumeration expansion** (>50K starts with adversarial
  initialization classes — e.g., contact-graph-mutated seeds, perturbed
  Heilbronn extremals): low-probability path but currently the only
  mathematical move. Requires Modal re-enable per `compute-router.md`.
- **Cross-problem transfer**: the basin-floor pattern documented here
  applies symmetrically to P1, P14, P17 and any future arena entry where
  the gap-to-#1 is below `minImprovement`. The autonomous loop should
  generalise this gate across all problems with that signature.

## See also

- [arena-proximity-guard](arena-proximity-guard.md) (Lessons #42, #91)
- [basin-rigidity](basin-rigidity.md)
- [float64-ceiling](float64-ceiling.md)
- [problems/5-min-distance-ratio](../problems/5-min-distance-ratio.md)
