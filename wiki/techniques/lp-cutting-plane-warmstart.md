---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P2, P7]
compute_profile: [local-cpu]
cost_estimate: "minutes (warm-start) to hours (cold-start large-n)"
hit_rate: "TBD"
---

# LP Cutting-Plane with IPM Warm-Start

## TL;DR

For sieve-theory / autocorrelation LPs, an interior-point (IPM) cutting-plane LP with the constraint set seeded from the **near-binding** constraints of the previous solution converges in roughly half the iterations of a cold start. P7 PNT extension from N=3287 to N=3350 took 6 cutting-plane rounds vs 10+ cold; the warm-start point is also near-feasible for IPM, accelerating the inner solve.

## When to apply

- Linear program with many constraints generated lazily (cutting-plane).
- Extending an existing LP to a larger variable set (P7: more squarefree keys; P2: larger n).
- Constraint matrix is dense and tall (constraints ≫ variables): IPM beats simplex (lesson #16).
- A previous solution exists with identifiable near-binding constraints.

## Procedure

1. **Solve LP at `N_old`** with HiGHS IPM:
   ```python
   from scipy.optimize import linprog
   res = linprog(c, A_ub=A, b_ub=b, method='highs-ipm')
   ```
2. **Identify near-binding constraints**: points `x` where `G(x) > 1 − ε` (P7 example: `ε ~ 1e-4`). These are the constraints most likely to be active in the extended LP.
3. **Seed the new constraint set** with the near-binding subset; add cutting planes lazily for the rest.
4. **Solve LP at `N_new`** with the seeded constraints, using the old solution as the IPM warm-start point (near-feasible).
5. **Cutting-plane loop**: at each round, find max-violated constraint; add to set; re-solve.
6. **Score gate** for P7: arena cap at 2000 keys; truncate to top 1997 by `|log(k)/k|` (lesson #96).

## Pitfalls

- **FOSS solvers stall at cross-over n** (lesson #57): cutting-plane LP descends rapidly at n≤200 but per-iter cost grows super-linearly. CLARABEL and `scipy.linprog` both bog at n≥10k. Budget MOSEK/Gurobi or skip the approach — warm-starting won't rescue solver-bound regimes.
- **IPM > simplex for tall dense matrices** (lesson #16): HiGHS simplex timed out at P7 N=3287 (33k×2000). IPM solved in 2029s.
- **LP fixed-point trap** (lesson #47): vanilla cutting-plane converges to the same LP fixed point that vanilla Frank-Wolfe lands at. Adding more constraints or bigger HiGHS won't escape — try away-step / pairwise FW (Lacoste-Julien-Jaggi 2015).
- **Arena tolerance band**: P7 accepts `1.0001×` scaled f-values (lesson #97). Combine genuine improvement (more keys) with arena-tolerance scaling for max score.
- **Don't seed all old constraints**: only the near-binding ones; the rest just bloat the LP. ε=1e-4 is the threshold P7 used.

## Compute profile

Local CPU. P7 N=3287 IPM: ~34 min. N=3350 with warm-start: 6 cutting-plane rounds, ~10 min total. RAM: ~7GB at n=30k for P2 (would need MOSEK to scale higher). Sequential — GPU sits idle.

## References

- `wiki/findings/lp-solver-scaling.md` (lessons #15, #16, #47, #57, #95, #96, #97 — comprehensive LP scaling notes).
- `wiki/findings/prime-number-theorem-lp.md`.
- knowledge.yaml strategy `warm_start_cutting_plane`; pattern `lp-for-constrained-optimization`.
- `mb/tracking/problem-7-prime-number-theorem/strategy.md`.
- Tao's sieve theory LP formulation (`source/papers/2015-tao-sieve-theory-notes.md`).
