# Problem 11: Tammes Problem (n = 50)

**Status**: JSAgent #2

## Problem

Place 50 points on the unit sphere S² ⊂ ℝ³ to **maximize** the minimum pairwise Euclidean distance. Each submitted point is projected onto the unit sphere before scoring.

## Background

The Tammes problem (P. M. L. Tammes, 1930, studying pollen grain distributions) asks for the configuration of n points on a sphere that maximizes the smallest pairwise distance. Exact solutions are proven only for small n ∈ {2, ..., 14, 24}. For other values the global optimum is conjectured from long computational search.

For n = 50, the best-known configuration has been essentially fixed since the Hardin-Sloane database (1996) and has not been improved in the intervening decades. The configuration is rigid, with every point touching four or five neighbours along the minimum-distance contact graph.

## Arena Details

- **API ID**: 11
- **Direction**: maximize
- **Solution format**: `{"vectors": [[x, y, z] × 50]}` (each row normalized before scoring)
- **Scoring**: minimum pairwise Euclidean distance after L2 normalization
- **minImprovement**: fetched from `/api/problems` at submission time

## Approach

### Strategy Overview

Warm-start from the Hardin-Sloane reference configuration and refine with constrained polish on the unit-sphere manifold.

### Constrained Polish

An iterated constrained polish drives the residuals of the active pair set to machine precision on the unit-sphere manifold. Score parity with the arena verifier is enforced bit-exactly by the unit test suite.

### What Worked

- **Hardin-Sloane warm-start** — the reference configuration is effectively the global optimum
- **Manifold-constrained polish** — pushes to float64 ceiling while maintaining sphere constraint

### What Didn't Work

- **Any attempt to beat the known configuration** — the Hardin-Sloane n = 50 configuration appears to be at the float64 ceiling
- **Multi-start from random configurations** — all converge back to the same contact graph structure

## Key Insights

- **Byte-identical consensus = float64 ceiling**: When 8+ independent agents submit byte-identical solutions, the solution is at the float64 ceiling of a known published construction. No from-scratch optimization can beat it without a fundamentally different algorithm.
- **Hardin-Sloane database is the reference standard**: For Tammes problems at moderate n, this database represents decades of computational work. Verify your evaluator against it before attempting improvements.
- **Rigid contact graph**: The n = 50 configuration has every point touching 4-5 neighbors, forming a rigid contact graph with no room for perturbation.

## References

- Hardin & Sloane, putatively optimal sphere codes (online database for n ≤ 130 in dimension 3)
- Musin & Tarasov, *The Tammes Problem for N = 14* (Experimental Math., 2015)
- Problem 6.34 of *Mathematical exploration and discovery at scale* ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))

## Infrastructure

- `src/einstein/tammes/evaluator.py` — arena-matching evaluator
- `scripts/tammes/` — optimization and polish scripts
- `tests/tammes/` — evaluator parity tests

*Last updated: 2026-04-13*
