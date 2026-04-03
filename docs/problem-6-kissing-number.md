# Problem 6: Kissing Number in Dimension 11

## Problem Statement

Place n=594 unit vectors in R^11 to minimize total overlap penalty. Sphere
centers are placed at c_i = 2v_i/||v_i||. The score is:

    loss = sum_{i<j} max(0, 2 - ||c_i - c_j||)

Score = 0 would prove kappa(11) >= 594, an open problem in mathematics.

## Approach

- Warm-start from best known arena solution
- Multi-scale targeted micro-perturbation on sphere manifold
- Incremental O(n) loss evaluation per perturbation step
- Contribution-weighted sampling to focus perturbation on high-overlap vectors

## Key Findings

- Scales 1e-10 through 1e-14 all find improvements; finer scales yield higher hit rates
- The optimization landscape has a fractal-like structure at atomic scales
- Riemannian gradient descent finds no improvement (basin is flat at gradient scale)
- Targeted perturbation (contribution-weighted sampling) outperforms uniform sampling

## References

- Novikov et al. (2025), "AlphaEvolve" — kappa(11) >= 593
- Conway & Sloane, "Sphere Packings, Lattices and Groups"
- Odlyzko & Sloane (1979), kissing number bounds

*Last updated: 2026-04-03*
