# Problem 16 — Heilbronn Problem for Convex Regions (n = 14)

**Status**: JSAgent #3

## Problem

Place 14 points in the plane to maximize

score = min_{1 ≤ i < j < k ≤ 14} area(p_i, p_j, p_k) / area(convex_hull({p_1, ..., p_14}))

The score is affine-invariant, so without loss of generality the hull area can be normalized and three points can be fixed as an affine gauge.

## Arena Details

- **API ID**: 16
- **Direction**: maximize
- **Solution format**: `{"points": [[x, y] × 14]}`
- **Scoring**: min triangle area / convex hull area over all C(14,3) = 364 triples

## Approach

### Strategy Overview

All top-rank agents converge to a **10 hull + 4 interior** configuration whose active set pins 16-20 near-minimal triples in an equioscillation pattern. Progress requires structured moves that preserve multiple active triples simultaneously.

### Epigraph SLSQP

`polish_slsqp` maximizes `t` subject to `area_i(points) ≥ t` for all 364 triples, with a 3-point affine gauge and hull-area normalization constraint. This epigraph formulation cleanly handles the min-of-many-areas objective.

### Equioscillation Trap Analysis

The optimal configuration develops an equioscillation pattern where 16-20 triples are simultaneously at or near the minimum area (within ~1e-12 of each other). This creates a balanced stress network:
- Random isotropic perturbations reliably decrease the score
- Structured moves must preserve several active triples at once
- The configuration is effectively frozen at the float64 ceiling

### What Worked

- **Epigraph SLSQP** — clean formulation for min-of-areas optimization
- **Parity verification** — byte-exact against all 15 downloaded leaderboard solutions
- **Structural analysis** — identifying the 10+4 signature and equioscillation count

### What Didn't Work

- **Escaping the equioscillation trap** — 16-20 simultaneously active triples form an unbreakable stress network
- **Alternative topologies** — multistart from random 10+4 and symmetric layouts all converge to the same basin
- **Perturbation** — any move that improves one active triple worsens others

## Key Insights

- **Equioscillation traps are structural**: When 16+ triangles are simultaneously minimal, the stress network is self-reinforcing. This is qualitatively different from problems with 2-3 active constraints.
- **10 hull + 4 interior is universal**: All top-8 agents share the same structural signature, suggesting this topology is globally optimal for n = 14.
- **Affine gauge reduces dimension**: Fixing 3 hull points as an affine gauge eliminates 6 degrees of freedom, making the optimization more tractable.

## References

- Tao et al., *Mathematical exploration and discovery at scale*, [arXiv:2511.02864](https://arxiv.org/abs/2511.02864), Problem 6.49.
- Novikov et al., *AlphaEvolve*, arXiv:2506.13131.
- Cantrell, *Optimal configurations for the Heilbronn problem in convex regions*, 2007.

## Infrastructure

- `src/einstein/heilbronn_convex/evaluator.py` — byte-exact arena verifier + vectorized fast path
- `src/einstein/heilbronn_convex/optimizer.py` — epigraph SLSQP polish
- `scripts/heilbronn_convex/` — multistart search scripts
- `tests/heilbronn_convex/` — parity tests against downloaded solutions

*Last updated: 2026-04-13*
