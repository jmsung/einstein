---
type: technique
author: agent
drafted: 2026-05-02
revised: 2026-05-23
related_concepts: [basin-rigidity.md]
related_problems: [P5, P13, P14, P15, P16-retired, P17a-retired, P17b-renamed-P18]
compute_profile: [local-cpu, modal-gpu]
cost_estimate: "minutes (10 BH seeds) to ~3 min Modal (44K multistart)"
hit_rate: "TBD"
---

# Basin-Hopping Multistart with Diverse Seeds

## TL;DR

After warm-start polish from competitor solutions yields the same float64 floor, run **10+ basin-hopping seeds with diverse initialization strategies** to map sub-basin structure. Single-seed BH explores one sub-basin only; ~10% of seeds discover deeper basins. P13 found a strictly better basin at −0.71170936 on seed 11; the other 9 returned the original −0.71170951 floor. At extreme scale (44K trials with 8 init strategies), this becomes a global-optimality proof (P5).

## When to apply

- Warm-start polish from rank-1 AND rank-2 leaderboard solutions converges to the same float64 floor (the polished score is the entry to a *family* of sub-basins, not a single attractor).
- You suspect deeper sub-basins exist but have no analytical entry to them.
- Goal: bank rank-#2 (distinct basin slightly below #1, P16) OR prove global optimality (no basin below threshold, P5).

## Procedure

1. **Polish rank-1 AND rank-2 SOTA** with the standard pipeline (`slsqp-active-pair-polish` or `bounded-lbfgs-per-region-sigmoid`). Confirm they polish to the same float64 floor.
2. **Pick 6+ diverse seed strategies** (P5 and P14 use these):
   - Uniform random
   - Disk / ball
   - Concentric rings / grids
   - Hex lattice / lattice perturbation
   - Halton / low-discrepancy / Sobol
   - Topology perturbation (swap two points)
   - Symmetric / D-fold rotational
   - Near-leader perturbation
3. **Run BH from each seed** with random init perturbation + local minimizer (SLSQP / L-BFGS).
4. **Keep the best across all seeds**. Report distinct basins (group by float64-equal scores within tolerance).
5. **Scale gate**: 10 seeds → first sub-basin discovery (P13). 5000+ seeds → distinct-basin rank-#2 grab (P14, P16). 44K+ seeds → global-optimality proof (P5).

```python
strategies = [random_init, disk_init, hex_lattice, halton,
              topology_swap, symmetric_rot, near_leader, low_discrepancy]
results = []
for strat in strategies:
    for trial in range(n_per_strategy):
        x0 = strat(seed=trial)
        x = scipy.optimize.basinhopping(score, x0, ...).x
        results.append((score(x), x))
best = min(results, key=lambda r: r[0])
```

## Pitfalls

- **Single-seed BH hides sub-basins**: 10+ seeds is the floor for sub-basin discovery; single-seed misses ~90% of deeper basins.
- **"Distinct basin" can still lose rank**: P16 found a 21-active-triple basin slightly BELOW capybara's 20-active-triple #1 — useful for rank-#2 grab, not for #1.
- **44K trials require Modal**: local 16-core multistart is faster up to ~5K trials; beyond that, Modal A100 with 200 parallel containers wins.
- **Cold-start strategies may all converge** if the problem is over-constrained (P5 30 active vs 28 DOF — fully rigid). The 44K result confirms global optimality, but at significant compute. Run cheaper diagnostics first (active-constraint count, reduced Hessian).
- **Affine canonicalization**: for affine-invariant problems (P16), you must canonicalize before comparing scores; otherwise distinct basins look like the same basin under rotation/translation.

## Compute profile

- 10 seeds × local: ~5 min CPU per problem.
- 5000 seeds: ~30 min local 16-core multiprocess.
- 44K seeds across 8 strategies: ~3 min wall on Modal with 200 parallel containers, ~$3.

## Case study: P16 Heilbronn-Convex (retired, dogfooded into Heilbronn-family wisdom)

Distilled from [`retired-16-heilbronn-convex.md`](../problems/retired-16-heilbronn-convex.md). The arena P16 (place 14 points to maximize min-triangle-area / convex-hull-area) was retired 2026-05-23, but the multistart recipe transfers cleanly to **[P15 Heilbronn-Triangles](../problems/15-heilbronn-triangles.md)** (the live successor, n=11 in a triangular region) and to any future Heilbronn-family revival.

**Setup that JSAgent faced.** Two pre-existing basins occupied by the top of the leaderboard:
- 6-way tied group at 16–17 active triangles (AlphaEvolve Construction 2).
- Solo rank-#1 holder (capybara007) at 20 active triangles.

Both warm-start-from-leader polishes converged to their respective float64 floors. The textbook BH would have re-explored either group's basin and returned the same floor.

**The discovery pattern**:

1. **Leader-averaging entry seed** (not on the generic 8-strategy list above) — averaged the AlphaEvolve and capybara solutions point-wise (post affine-canonicalization), then polished. This seed *consistently* dropped into a third basin the cold-start strategies missed.
2. **6 diverse seed strategies** running in parallel: `random`, `grid`, `lattice`, `symmetric`, `near-leader`, `near-runner-up`. (P16 used 6, not the generic 8; the missing two were `Halton` and `topology-swap`, both ineffective on the affine-normalized landscape.)
3. **Scale gate**: 5000+ trials across the 6 strategies. The 21-active sub-basin showed up in <1% of trials — the leader-averaging seed converged to it ~20× more often than cold-starts.
4. **Yield**: a distinct 21-active basin at `+9.001e-9` above the tied group, `-5.76e-11` below the #1 ceiling. Submitted at rank #2.

**Phased polish pipeline** (post-discovery, to lock the basin to the float64 floor): LSE soft-min Adam → SLSQP epigraph with affine gauge → CMA-ES (sigma-collapse for second-order optimality) → D1-symmetric DE → null-space walk → rotation lottery (2M+ rotations, mostly futile on Heilbronn due to `minImprovement > ulp` — see [rotation-lottery pitfalls](multistart-with-rotation-lottery.md#pitfalls)).

**Transferable lesson**: when *both* leader basins polish to the same family of float64 floors, the **leader-averaging seed is the strongest single discovery move**. Add it as a 9th strategy in the generic list above; deploy whenever rank #1 and rank #2 are in conflicting basins.

## References

- `wiki/findings/optimizer-recipes.md` (#69 — multi-seed BH reveals warm-start polish sub-basins).
- `wiki/findings/basin-rigidity.md` (lesson #84 — 44K multistart for P5 global-optimality proof).
- knowledge.yaml strategies `distinct_basin_multistart`, `basin_hopping`; pattern `multi-seed-basin-hopping-for-warm-start-substructure`.
- `mb/problems/13-edges-triangles/experiment-log.md` (seed 11 deeper basin).
- [`retired-16-heilbronn-convex.md`](../problems/retired-16-heilbronn-convex.md) + `mb/problems/16-heilbronn-convex/strategy.md` (21-active distinct-basin rank-#2; case study above).
