# Skill library — ranked techniques by hit-rate

Tracks which techniques actually work, on which problem families. Updated when:
- A technique is invoked during a cycle (increment `tried`)
- The cycle reaches top-3 OR produces a new finding (increment `top3` or `finding`)
- A cycle is recorded in `cycle-log.md`

## Schema

| Column | Notes |
|---|---|
| `technique` | path under `wiki/techniques/` |
| `category` | autocorrelation / packing / kissing / extremal-graph / sieve / discrete-combinatorics / functional-inequality |
| `tried` | times invoked across all cycles |
| `top3` | times that invocation landed top-3 |
| `finding` | times invocation produced a new wiki/finding (positive or dead-end) |
| `last_used` | YYYY-MM-DD |
| `hit_rate` | `top3 / tried` (recomputed weekly) |

Hit-rate is the *first-line filter*. A technique with 0/10 hit-rate gets demoted to `wiki/techniques/anti-patterns/` (low priority) rather than auto-suggested. A technique with 5/5 stays high in dispatch ranking.

## Bootstrap entries

Pre-loaded from migration; counts are HISTORICAL (pre-refactor episodes). New cycles increment from here.

| technique | category | tried | top3 | finding | last_used | hit_rate |
|---|---|---|---|---|---|---|
| `parallel-tempering-sa.md` | kissing / Coulomb | 5 | 3 | 2 | 2026-04-25 | 0.60 |
| `mpmath-ulp-polish.md` | float64-ceiling family | 8 | 5 | 3 | 2026-04-25 | 0.62 |
| `slsqp-active-pair-polish.md` | packing / kissing | 6 | 4 | 1 | 2026-04-12 | 0.67 |
| `arena-tolerance-slsqp.md` | packing | 4 | 3 | 1 | 2026-04-12 | 0.75 |
| `larger-n-cascade.md` | autocorrelation | 4 | 4 | 2 | 2026-04-09 | 1.00 |
| `cross-resolution-basin-transfer.md` | autocorrelation | 1 | 1 | 1 | 2026-04-08 | 1.00 |
| `bounded-lbfgs-per-region-sigmoid.md` | extremal-graph | 1 | 1 | 1 | 2026-04-09 | 1.00 |
| `boundary-snap-for-kinks.md` | extremal-graph | 1 | 1 | 1 | 2026-04-09 | 1.00 |
| `first-order-link-tangent-test.md` | kissing-tight | 2 | 1 | 1 | 2026-04-25 | 0.50 |
| `kronecker-search-decomposition.md` | discrete-combinatorics | 2 | 0 | 2 | 2026-05-02 | 0.00 |
| `bnb-exhaustive-w3.md` | discrete-combinatorics | 1 | 0 | 1 | 2026-04-09 | 0.00 |
| `lp-cutting-plane-warmstart.md` | sieve | 2 | 2 | 1 | 2026-04-15 | 1.00 |
| `dinkelbach-fractional-programming.md` | autocorrelation-ratio | 1 | 1 | 0 | 2026-04-10 | 1.00 |
| `gap-space-parameterization.md` | uncertainty | 2 | 1 | 1 | 2026-04-19 | 0.50 |
| `k-climbing.md` | uncertainty | 2 | 1 | 1 | 2026-04-19 | 0.50 |
| `multistart-with-rotation-lottery.md` | packing | 4 | 1 | 2 | 2026-04-12 | 0.25 |
| `basin-hopping-multistart.md` | packing / extremal | 4 | 2 | 2 | 2026-04-12 | 0.50 |
| `uniform-radius-shrink-fallback.md` | packing | 1 | 1 | 0 | 2026-04-09 | 1.00 |
| `micro-perturbation-multiscale.md` | kissing | 1 | 1 | 1 | 2026-04-09 | 1.00 |
| `cma-es-with-warmstart.md` | exploration | 3 | 1 | 1 | 2026-04-19 | 0.33 |
| `memetic-tabu-search.md` | discrete-combinatorics | 1 | 0 | 1 | 2026-04-02 | 0.00 |
| `sdp-flag-algebra.md` | extremal-graph | 1 | 1 | 1 | 2026-04-09 | 1.00 |
| `remez-equioscillation-diagnostic.md` | autocorrelation | 2 | 0 | 2 | 2026-04-08 | 0.00 |
| `warm-start-from-leader.md` | universal | 11 | 6 | 3 | 2026-05-02 | 0.55 |
| `greedy-insert-cd-redistribute.md` | extremal-graph | 1 | 1 | 0 | 2026-04-09 | 1.00 |
| `gpu-decision-framework.md` | meta | 5 | (meta) | 2 | 2026-04-25 | (n/a) |
| `compute-router.md` | meta | 0 | (meta) | 0 | (TBD) | (n/a) |

## Promotion / demotion rules

- **Promote**: technique with `hit_rate >= 0.5` AND `tried >= 5` → keep prominent in `council-dispatch` recommendations.
- **Demote**: technique with `hit_rate < 0.2` AND `tried >= 5` → move to `wiki/techniques/anti-patterns/` with a finding explaining when NOT to reach for it.
- **Watchlist**: technique with `tried < 3` → not enough data; keep collecting.

Recomputed by `/agent-reflect` (Goal 13 stretch) or by hand weekly.
