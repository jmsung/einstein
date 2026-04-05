# Problem 13: Edges vs Triangles (Minimal Triangle Density)

## Problem

Given a weight matrix (m x 20), compute edge and triangle densities via
complete-multipartite graphon power-sum formulas. The solver must find weight
vectors that trace a curve minimizing the area under a piecewise slope-3
interpolation of the (edge_density, triangle_density) mapping.

Score = -(area + 10 * max_gap), where higher (less negative) is better.

## Background

This problem relates to the Razborov flag algebra framework for graph density
inequalities. The Kruskal-Katona / Razborov curve gives the minimum triangle
density as a function of edge density for graphs. The optimal curve is
achieved by complete multipartite (Turan-family) constructions, where the
scalloped lower boundary traces through balanced k-partite graphs at
breakpoints x = 1 - 1/k.

## Arena Details

- **API ID**: 13
- **Direction**: maximize (less negative is better)
- **Solution format**: `{"weights": [[...], ...]}`  -- (m x 20) matrix, m <= 500
- **Scoring**: piecewise slope-3 interpolation area + 10 * max gap penalty

## Approach

1. **Turan baseline**: complete multipartite constructions at Razborov-optimal breakpoints
2. **Greedy insertion**: best-insert algorithm to fill the curve with 500 points
3. **Coordinate descent**: local optimization of x-positions to minimize interpolated area

## Infrastructure

- `src/einstein/edges_triangles/evaluator.py` -- arena-matching evaluator with density and scoring functions
- `scripts/edges_triangles/optimize.py` -- greedy insertion + coordinate descent optimizer
- `scripts/edges_triangles/submit.py` -- arena submission with pre-flight checks
- `tests/edges_triangles/test_edges_triangles.py` -- evaluator tests and cross-validation

## References

- Razborov (2010) -- On the minimal density of triangles in graphs
- Kruskal (1963) -- The number of simplices in a complex
- Katona (1968) -- A theorem of finite sets

*Last updated: 2026-04-05*
