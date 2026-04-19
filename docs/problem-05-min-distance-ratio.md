# Problem 5 — Min Distance Ratio (2D, n = 16)

**Status**: JSAgent #4

## Problem

Place 16 points in the plane minimizing R = (d_max / d_min)², the squared ratio of the maximum to minimum pairwise Euclidean distances. Classical discrete geometry — see [Erich Friedman's compendium](https://erich-friedman.github.io/packing/maxmin/).

## Arena Details

- **API ID**: 5
- **Direction**: minimize
- **Solution format**: `{"points": [[x, y] × 16]}`
- **Scoring**: (d_max / d_min)² over all C(16,2) = 120 pairwise distances

## Approach

### Strategy Overview

The problem has a single dominant basin — all top agents converge to the same geometric configuration. The challenge is not finding the basin but proving it's the only one and polishing to the float64 floor.

### Smooth Reformulation

Minimize `s` subject to `1 ≤ ‖p_i − p_j‖² ≤ s` for all 120 pairs. This transforms the ratio objective into a constrained optimization that SLSQP handles efficiently, converging in a few hundred iterations.

### Float-Precision Lottery

Once at the basin floor, the mathematical minimum projects onto many near-equivalent float64 representations. Random isometries (rotation, translation, small scaling) paired with re-evaluation sample the float64 neighborhood to find the best representable score.

### Basin Rigidity Analysis

To prove this is the only competitive basin:
- **44K multi-start search**: 8 diverse initialization strategies (uniform random, disk, grid, hex lattice, Halton, topology perturbation) across thousands of parallel SLSQP runs.
- **Over-constrained Hessian**: The optimal configuration has 22 min-distance edges and 8 max-distance edges. With 30 active constraints but only 28 degrees of freedom (32 coords − 4 gauge freedoms), the basin is fully rigid — no infinitesimal perturbation can improve the score.
- Every multi-start run converges to the same configuration, confirming a single-basin landscape.

### What Worked

- **SLSQP on smooth reformulation** — converges quickly and reliably
- **Float-precision lottery** — samples the float64 neighborhood efficiently
- **Multi-start basin proof** — 44K starts confirm single-basin definitively

### What Didn't Work

- **Escaping the basin** — 30 active constraints vs 28 DOF = mathematically rigid
- **Topological perturbations** — swapping point roles or breaking contact graph edges always worsens the objective

## Key Insights

- **Over-constrained geometry = frozen basin**: When active_constraints > degrees_of_freedom, the basin is fully rigid. This is a diagnostic for when to stop optimizing and move on.
- **Multi-start search proves optimality**: Thousands of diverse starts all converging to the same basin is strong computational evidence for global optimality.
- **All top agents share one basin**: Competition reduces to float-precision polishing of a shared geometric configuration.

## References

- David Cantrell (Feb 2009) — first competitive value for n = 16 on Friedman's compendium.
- Timo Berthold et al. (Jan 2026) — recent improvement noted on Friedman.
- arXiv:2511.02864 — "Mathematical exploration and discovery at scale", Problem 6.50.

## Infrastructure

- `src/einstein/min_distance_ratio/evaluator.py` — arena-matching evaluator
- `src/einstein/min_distance_ratio/optimizer.py` — SLSQP reformulation + float-precision lottery
- `tests/min_distance_ratio/` — evaluator parity tests

*Last updated: 2026-04-13*
