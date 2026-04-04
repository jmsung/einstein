# Problem 10 — Thomson Problem (n = 282)

## Problem Statement

Place 282 points on the unit sphere S² to minimize Coulomb energy:

$$E = \sum_{i < j} \frac{1}{\|p_i - p_j\|}$$

Points are auto-normalized to the unit sphere. Pairwise distances below 1e-12 are clamped.

## Approach

### Evaluator
Built an exact Coulomb energy evaluator matching the arena verifier:
- Vectorized O(n²) pairwise distance computation
- Incremental O(n) update for single-point perturbation
- Validated against known analytical results and SOTA solutions

### Optimization Pipeline
1. **Warm-start** from Cambridge Cluster Database (Wales group) coordinates
2. **L-BFGS** in spherical coordinates with exact gradient
3. **Riemannian gradient descent** on the sphere manifold
4. **Multi-scale micro-perturbation** (scales 1e-4 to 1e-12)
5. **Contribution-weighted targeted perturbation**
6. **Basin-hopping** from SOTA and random seeds
7. **Upgrade/downgrade** from n=281 and n=283 optimal configs
8. **Icosadeltahedral seed** (Caspar-Klug T=28 geodesic polyhedron)
9. **GPU-accelerated search** on Modal A100
10. **Dual annealing** on pentagonal defect positions
11. **Genetic crossover** between diverse local minima

### Key Finding
N=282 is an icosadeltahedral magic number with chiral icosahedral symmetry (I).
The SOTA configuration is the putative global minimum from the Cambridge Cluster Database,
confirmed by 20+ years of computational study and three independent arena agents.

## Results

| Metric | Value |
|--------|-------|
| SOTA (arena) | 37147.29441846226 |
| Our best | 37147.29441846226 |
| Target (SOTA - 1e-5) | 37147.29440846226 |
| Improvement | ~0 |

## References

- Wales & Ulker (2006), *Phys. Rev. B* 74, 212101
- Cambridge Cluster Database: Thomson tables
- arXiv:2506.08398 — Energy landscape of the Thomson problem
- arXiv:2107.06519 — Magic numbers for charged particles on a sphere

*Last updated: 2026-04-03*
