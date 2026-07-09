---
type: finding
author: agent
drafted: 2026-06-03
question_origin: problem-15
status: answered
related_concepts:
  - basin-rigidity
  - minimprovement-gate
  - float64-ceiling
  - equioscillation
  - symmetry-and-fundamental-domain
cites:
  - ../findings/dead-end-p5-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/dead-end-p11-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/dead-end-p14-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/basin-rigidity.md
  - ../findings/float64-ceiling.md
  - ../problems/15-heilbronn-triangles.md
---

# Dead end: autonomous-loop cycle on P15 (basin-converged at tied SOTA)

## What we tried

Autonomous cycle 42 / attempt 1 of this visit on P15 Heilbronn n=11. Thompson
bandit sampled `bounded-lbfgs-per-region-sigmoid.md` (Beta(2,1), θ=0.74).
Cycle 41 the same recommendation produced no execution (deferred to Phase 5).
Per the P5/P11/P14 templates
(`dead-end-p5-autonomous-loop-basin-converged-no-api-change.md`,
`dead-end-p11-autonomous-loop-basin-converged-no-api-change.md`,
`dead-end-p14-autonomous-loop-basin-converged-no-api-change.md`), dispatched
`verify_seed` for a triple-verify receipt and stopped.

```
uv run python -m einstein.optimizer_dispatch \
    --problem-id 15 --strategy verify_seed
# {ok:true, score:0.036529889880030156, runtime:0.068s}
```

Result: bit-identical to AlphaEvolve Figure 26 / CHRONOS / EinsteinAgent6391
(4-way tied SOTA at rank #1-4). Bandit pick overridden because P15's
blocker is API-state (gap = 0), not technique-rotation.

## Why it failed

P15 is structurally worse than P5/P11/P14: we are **tied at SOTA**, not
below it. The gap to arena #1 is literally zero — beating it requires a
genuinely new basin, not polish.

```
basin_floor    = 0.036529889880030156   (verify_seed; tied with AE/CHRONOS)
mpmath_ceiling = 0.036529889880030220   (+~6.25e-17, ~1 ulp)
arena_#1       = 0.036529889880030156   (tied SOTA; 4-way at this float64 floor)
gap_to_#1      = 0                      (exact tie)
gap_to_#5      = +2.19e-7               (next-distinct-basin below, CHRONOS rank-5)
minImprovement = 1e-8                   (P15 default)
```

Submitting our current basin = rank #5 in a 4-way tie under `4/2/1/...`
medal scoring (0 points). Polishing the float64 ulp lift to the mpmath
ceiling = +6.25e-17 ≈ 1.6e8× below the `minImprovement` gate — would still
not be a strict improvement.

Independent receipts already in the wiki confirm basin uniqueness for P15:

- `problems/15-heilbronn-triangles.md` — frozen status documented; tier C
- `mb/problems/15-heilbronn-triangles/experiment-log.md` — 18,852 prior
  trials across direct SLSQP, 6740-seed multistart, CMA-ES (1612), basin
  hopping (10,500), all zero Δ. Six other agents' attempts likewise failed
  (E008). Sierpinski first-order LP on 17 tight triples → `Δ_min = 0` (no
  feasible ascent direction).
- `findings/basin-rigidity.md` — P15 cited: 17 active triples on 8
  effective DOF after D1 symmetry; over-determined KKT.
- `findings/float64-ceiling.md` — cross-problem inventory; P15 listed.
- AlphaEvolve (Nov 2025) is the only post-Cantrell advance on n=11
  equilateral-triangle Heilbronn in 19 years (E009 literature review).

This is the **fourth concrete instance** of the
"basin-converged + minImprovement-blocked" pattern (P5 → P14 → P11 → P15).
P15 is the strongest case: tied SOTA, not merely close.

## What this rules out

- Re-running any P15 manifest optimizer (`verify_seed`, and any of the
  bandit-suggested `bounded-lbfgs-per-region-sigmoid`,
  `boundary-snap-for-kinks`, `arena-tolerance-slsqp`,
  `slsqp-active-pair-polish`, `cma-es-with-warmstart`,
  `basin-hopping-multistart`) under the current `minImprovement = 1e-8`
  regime. The 18,852-trial corpus in `experiment-log.md` already covers the
  full SLSQP / CMA / basin-hopping technique fanout — none escaped the
  AE/CHRONOS basin.
- Bandit-driven technique rotation on P15 — every technique converges to
  the AE Figure 26 basin. Hit-rate signal is uninformative when the
  underlying physics blocks improvement.
- Council-dispatch on P15 absent a triggering API change — the original
  branch already exhausted persona angles (E008: AIKolmogorov, EA6391,
  Sierpinski, CHRONOS, KawaiiCorgi consensus). No persona angle moves
  the basin floor or widens the gate.

## What might still work

- **API-state gating** (the generalisable fix, identical to P5/P11/P14):
  `autonomous_loop.py` should fetch `/api/problems/15.minImprovement` at
  cycle-start and gate dispatch on `gap_to_arena_#1 ≥ minImprovement`.
  For P15 today, `gap_to_#1 = 0` → mark as `frozen-pending-api-change`
  and skip until either arena #1 moves OR a structurally new basin is
  discovered offline. The same `frozen_problem_gate(problem_id,
  basin_floor, arena_floor, minimprovement) → {dispatch,
  frozen-pending-api-change}` helper proposed in the P14 finding now
  covers four instances: P5, P11, P14, P15.
- **New basin** (the only mathematical move): non-AE Figure 26 basin for
  n=11 in an equilateral triangle. None known in the literature post
  AlphaEvolve (Nov 2025); none surfaced in 18,852 multistart trials.
  Adversarial-init classes not yet tried: contact-graph mutation from
  Cantrell n=12 / n=10 by add/remove (Cantrell n=12, 15, 16 have full
  rotational symmetry inaccessible at n=11 since 11 ∉ {3k, 3k+1 with
  fixed center}). Low-probability path; not a compute-it-tomorrow move.
- **Cross-problem transfer (codified, four instances now)**: P5, P11,
  P14, P15 share the same signature — basin at float64 ceiling, gap to
  #1 ≤ minImprovement, manifest strategies exhausted, multi-agent
  consensus. The four-instance count crosses the promotion threshold
  per `wiki-attribution.md` (3+ findings → concept candidate); propose
  promotion of the API-state-gating pattern to
  `concepts/api-state-gated-frozen-basin.md` for human review.

## See also

- [dead-end-p5-autonomous-loop-basin-converged-no-api-change](dead-end-p5-autonomous-loop-basin-converged-no-api-change.md) — template
- [dead-end-p11-autonomous-loop-basin-converged-no-api-change](dead-end-p11-autonomous-loop-basin-converged-no-api-change.md) — third instance
- [dead-end-p14-autonomous-loop-basin-converged-no-api-change](dead-end-p14-autonomous-loop-basin-converged-no-api-change.md) — codifies `frozen_problem_gate`
- [basin-rigidity](basin-rigidity.md)
- [float64-ceiling](float64-ceiling.md)
- [problems/15-heilbronn-triangles](../problems/15-heilbronn-triangles.md)
