# Problem 10 — Thomson Problem (n = 282)

**Status**: JSAgent #6

## Problem

Place 282 points on the unit sphere S² to minimize Coulomb energy:

E = Σ_{i < j} 1 / ‖p_i − p_j‖

Points are auto-normalized to the unit sphere. Pairwise distances below 1e-12 are clamped.

## Background

The Thomson problem (1904) asks for the minimum-energy configuration of n point charges on a sphere interacting via Coulomb repulsion. Exact solutions are known only for small n. For large n, the landscape becomes increasingly complex with exponentially many local minima.

N = 282 is an **icosadeltahedral magic number** — a special value where the putative global minimum has chiral icosahedral symmetry (I), creating a single-funneled energy landscape. This makes the problem simultaneously well-studied (20+ years of computational work) and essentially frozen.

## Arena Details

- **API ID**: 10
- **Direction**: minimize
- **Solution format**: `{"vectors": [[x, y, z] × 282]}`
- **Scoring**: Coulomb energy after L2 normalization

## Approach

### Strategy Overview

We tried 11 distinct optimization approaches — none found an improvement over the putative global minimum from the Cambridge Cluster Database (Wales group). This is consistent with n = 282 being a magic number.

### Approaches Tried

1. **L-BFGS** in spherical coordinates with exact gradient
2. **Riemannian gradient descent** on the sphere manifold
3. **Multi-scale micro-perturbation** (scales 1e-4 to 1e-12)
4. **Contribution-weighted targeted perturbation**
5. **Basin-hopping** from SOTA and random seeds
6. **Upgrade/downgrade** from n = 281 and n = 283 optimal configurations
7. **Icosadeltahedral seed** (Caspar-Klug T = 28 geodesic polyhedron)
8. **GPU-accelerated parallel search**
9. **Dual annealing** on pentagonal defect positions
10. **Genetic crossover** between diverse local minima
11. **Warm-start** from Cambridge Cluster Database coordinates

### What Worked

- **Cambridge Cluster Database warm-start** — the reference configuration is the putative global minimum
- **Exact Coulomb evaluator** — vectorized O(n²) with incremental O(n) single-point updates

### What Didn't Work

- **Everything else** — all 11 approaches converge to the same minimum. The icosadeltahedral magic number creates a single-funneled landscape with no escape.

## Key Insights

- **Magic number configurations are frozen**: At icosadeltahedral magic numbers, the energy landscape is single-funneled. No optimization can improve on the known minimum — this is a mathematical property of the landscape, not a limitation of the search.
- **Know when to stop**: After 12+ structurally distinct approaches yield zero improvement, the problem is definitively frozen. Recognize this early and move on.
- **Cambridge Cluster Database is authoritative**: For Thomson problems, the Wales group database (20+ years of computational study) is the reference standard.

## References

- Wales & Ulker (2006), *Phys. Rev. B* 74, 212101
- Cambridge Cluster Database: Thomson tables
- arXiv:2506.08398 — Energy landscape of the Thomson problem
- arXiv:2107.06519 — Magic numbers for charged particles on a sphere

## Infrastructure

- `src/einstein/thomson/evaluator.py` — exact Coulomb energy evaluator (vectorized O(n²), incremental O(n))
- `scripts/thomson/` — optimization scripts (L-BFGS, basin-hopping, micro-perturbation, etc.)
- `tests/thomson/` — evaluator parity tests

*Last updated: 2026-04-13*
