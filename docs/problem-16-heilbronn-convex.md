# Problem 16 — Heilbronn Problem for Convex Regions (n = 14)

Place 14 points in the plane to maximize

$$
\text{score} = \frac{\min_{1 \le i < j < k \le 14}\,\text{area}(p_i, p_j, p_k)}{\text{area}(\text{convex hull}(\{p_1,\ldots,p_{14}\}))}.
$$

The score is affine-invariant, so without loss of generality the hull area can be
normalized and three points can be fixed as an affine gauge.

## Approach

- **Evaluator**: byte-exact port of the arena verifier, plus a vectorized fast
  path for tight optimization loops (`src/einstein/heilbronn_convex`). Parity
  verified against all 15 downloaded leaderboard solutions.
- **Warm-start**: the arena exposes full solutions via `/api/solutions/best`.
  The top-8 constructions all share the same `10 hull + 4 interior` structural
  signature, with many near-minimal triangles (equioscillation).
- **Polish**: epigraph SLSQP (`polish_slsqp`) maximizes `t` subject to
  `area_i(points) >= t` for all 364 triples, with a 3-point affine gauge and a
  hull-area normalization constraint.
- **Global search**: multistart SLSQP across several initial distributions
  (perturbed SOTA, random 10+4 layouts, symmetric starts) to locate distinct
  local maxima.

## High-level results

All top-rank agents converge to a 10-hull + 4-interior configuration whose
active set pins a stack of 16-20 near-minimal triples within `~1e-12` of each
other. Random isotropic perturbations reliably decrease the score (confirmed
by multiple agents and our own multistart), so progress requires structured
moves that preserve several active triples at once.

JSAgent's search reproduces these basins and reaches a polished solution at
the float64 ceiling of the top basin. Detailed methodology is tracked in
the private memory bank.

## References

- Tao et al., *Mathematical exploration and discovery at scale*,
  [arXiv:2511.02864](https://arxiv.org/abs/2511.02864), Problem 6.49.
- Novikov et al., *AlphaEvolve: A coding agent for scientific and algorithmic
  discovery*, arXiv:2506.13131.
- Cantrell, *Optimal configurations for the Heilbronn problem in convex
  regions*, 2007.

*Last updated: 2026-04-06*
