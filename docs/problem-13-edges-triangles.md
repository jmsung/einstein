# Problem 13: Edges vs Triangles (Minimal Triangle Density)

**Status**: No submission (best solution blocked by proximity guard)

## Problem

Given a weight matrix (m × 20), compute edge and triangle densities via complete-multipartite graphon power-sum formulas. The solver must find weight vectors that trace a curve minimizing the area under a piecewise slope-3 interpolation of the (edge_density, triangle_density) mapping.

Score = −(area + 10 × max_gap), where higher (less negative) is better.

## Background

This problem relates to the **Razborov flag algebra** framework for graph density inequalities. The Kruskal-Katona / Razborov curve gives the minimum triangle density as a function of edge density for graphs. The optimal curve is achieved by complete multipartite (Turán-family) constructions, where the scalloped lower boundary traces through balanced k-partite graphs at breakpoints x = 1 − 1/k.

## Arena Details

- **API ID**: 13
- **Direction**: maximize (less negative is better)
- **Solution format**: `{"weights": [[...], ...]}` — (m × 20) matrix, m ≤ 500
- **Scoring**: piecewise slope-3 interpolation area + 10 × max gap penalty

## Approach

### Strategy Overview

The Turán extremal family is provably optimal for each scallop (per-row), so the main optimization lever is **x-sampling placement** — choosing where to place the 500 points along the curve. Two novel techniques made the difference: **per-scallop sigmoid bounding** and **boundary-snap for kinks**.

### Turán Baseline

Complete multipartite constructions at Razborov-optimal breakpoints provide the theoretical lower envelope. Each row of the weight matrix defines a k-partite graphon; the curve is the union of all (edge_density, triangle_density) pairs.

### Per-Scallop Sigmoid Bounding (Key Breakthrough)

Each x-position is constrained to its scallop interval [lo_i, hi_i]. Rather than using box constraints (which have zero gradient at boundaries), parameterize as:

    x_i = lo_i + (hi_i − lo_i) × sigmoid(raw_i)

This keeps gradients nonzero everywhere and prevents silent boundary violations. PyTorch autograd + L-BFGS optimizes over the raw parameters, with gradients flowing cleanly through the sigmoid transform.

### Boundary-Snap for Kinks

The piecewise slope-3 interpolation has first-order discontinuities (kinks) at the Turán breakpoints x = 1 − 1/k. Snapping the nearest sample point exactly to each kink reduces interpolation error by ~1.24 × 10⁻⁸ per snap round.

### Gap-Space Basin-Hopping

For global search, random jumps in gap-space (perturbing the gaps between consecutive x-positions rather than absolute positions) preserve ordering and let basin-hopping explore the solution landscape effectively.

### What Worked

- **Per-scallop sigmoid bounding** — key breakthrough; nonzero gradients everywhere prevent boundary deadlocks
- **Boundary-snap at kinks** — +1.24 × 10⁻⁸ per round at each x = 1 − 1/k breakpoint
- **Gap-space perturbation** — preserves ordering naturally, enables effective basin-hopping
- **Greedy insertion + coordinate descent** — good baseline before advanced techniques

### What Didn't Work

- **Submitting** — minImprovement proximity guard blocks submission when improvement is too close to an existing leaderboard entry
- **Uniform x-spacing** — wastes samples on flat regions of the curve
- **Box constraints** — zero gradients at boundaries kill optimization

## Key Insights

- **Sigmoid bounding is a general technique**: For any problem with per-variable bounded intervals, sigmoid parameterization gives nonzero gradients everywhere. This transfers to any constrained continuous optimization.
- **Kinks in interpolation matter**: First-order discontinuities in the scoring function create opportunities — snapping samples to kinks exploits the scoring formula's structure.
- **Gap-space preserves structure**: Optimizing inter-point gaps rather than absolute positions naturally maintains ordering constraints and improves condition number.
- **The proximity guard is a real barrier**: Even with a score that would rank #1, the minImprovement threshold relative to existing leaderboard entries can block submission.

## References

- Razborov (2010) — On the minimal density of triangles in graphs
- Kruskal (1963) — The number of simplices in a complex
- Katona (1968) — A theorem of finite sets

## Infrastructure

- `src/einstein/edges_triangles/evaluator.py` — arena-matching evaluator with density and scoring functions
- `scripts/edges_triangles/optimize.py` — greedy insertion + coordinate descent + basin-hopping
- `scripts/edges_triangles/push_g_bounded.py` — per-scallop sigmoid bounding optimizer (PyTorch L-BFGS)
- `scripts/edges_triangles/submit.py` — arena submission with pre-flight checks
- `tests/edges_triangles/test_edges_triangles.py` — evaluator tests and cross-validation

*Last updated: 2026-04-13*
