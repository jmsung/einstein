---
type: technique
author: agent
drafted: 2026-05-02
related_concepts: []
related_problems: [P9]
compute_profile: [local-cpu]
cost_estimate: "minutes per climb attempt"
hit_rate: "TBD"
---

# k-Climbing (Dimensionality Increase)

## TL;DR

When all optimizers at fixed dimensionality `k` converge to the same basin, the basin is genuine in the k-DOF space — but adding a degree of freedom (climb to `k+1`) can immediately open new basins invisible at `k`. P9 Uncertainty Principle: k=13 → k=14 found `S=0.31817` after every k=13 method (CMA-ES, NM, hillclimb, gradient, BH) was stuck at S≈0.31835. The improvement from a single climb (1.8e-4) was unreachable with any amount of fixed-k search.

## When to apply

- All k-fixed optimizers converge to the same score (basin exhausted in current dimensionality).
- The problem allows variable dimensionality (P9: polynomial degree k).
- A natural insertion point exists for the new variable (P9: a new root in the far cluster).
- minImprovement gate is comfortably below the expected first-climb step size.

## Procedure

1. **Confirm exhaustion at k**: 5+ structurally-distinct optimizers (CMA-ES, NM, hillclimb, gradient descent, BH) all converge to the same basin within ulp tolerance.
2. **Identify natural insertion**: where is the new DOF expected to land? P9: far cluster, beyond existing roots.
3. **Re-parameterize at k+1** (typically gap-space, see `gap-space-parameterization.md`):
   ```python
   # P9: add one extra gap in the far cluster
   g_new = [g_old[i] for i in range(k)] + [delta_far]
   ```
4. **Run gap-space NM** (or similar) at the new dimensionality. P9: immediate breakthrough at k=14.
5. **Verify the climb step exceeds minImprovement** with comfortable margin.

## Diminishing returns rule

Lesson #66: k-climb step shrinks fast as the polynomial approaches the continuous limit.

| Climb | Step size | minImprovement | Ratio |
|---|---|---|---|
| k=13 → 14 | 1.8e-4 | 1e-4 | 1.8 (above gate) |
| k=14 → 15 | 4.57e-6 | 1e-4 | 0.046 (40× below) |

**Decision rule**: compute `ratio = step_size / minImprovement` for the FIRST and SECOND successful climbs. If `ratio_2 < 0.1`, abandon the simple k-climb path and pivot to:
- (a) Structurally different parameterization (4-cluster instead of 3-cluster);
- (b) Different basin entirely;
- (c) Declare the problem locked at current k and move on.

## Pitfalls

- **Wrong insertion location**: putting the new DOF in a cluster the optimizer can't reach is silent failure. Use the structural intuition (where does the polynomial want a root?).
- **mpmath dps must scale with k** (lesson #65): higher k = worse cond number; dps that worked at k=13 may underflow at k=15. Re-derive `dps ≈ log10(cond) + buffer` and verify against a known-good smaller-k.
- **Constraint-verification before optimization** (lesson #87): P9's score 1.07e-13 was invalid because the evaluator missed `f-even, f(0)<0, f̂(0)<0` constraints. Always implement ALL mathematical constraints as hard checks before climbing.
- **k-climbing does not always improve**: if the basin at `k` is the continuous optimum (not a finite-dim artifact), climbing gives nothing. The diminishing-returns ratio is the diagnostic.
- **Distinct from gap-space parameterization**: k-climbing changes dimensionality; gap-space changes coordinate system. Combine them — the new gap is the natural coordinate for the added DOF.

## Compute profile

Local CPU. Gap-space NM at k=14: minutes. CMA-ES at k=14: ~10 min for full convergence. Sequential — GPU offers nothing.

## References

- `wiki/findings/k-climbing.md` (lessons #24, #66 — k-climb beats fixed-k; gate-feasibility ratio).
- `wiki/findings/float64-polish.md` (#65 — mpmath dps scaling).
- knowledge.yaml pattern `k-climbing`.
- `wiki/techniques/gap-space-parameterization.md` (companion).
- `mb/wiki/problem-9-uncertainty-principle/strategy.md`.
