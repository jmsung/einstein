# Problem 11: Tammes Problem (n = 50)

## Problem

Place 50 points on the unit sphere $S^2 \subset \mathbb{R}^3$ so as to
**maximize** the minimum pairwise Euclidean distance. Each submitted point
is projected onto the unit sphere before scoring.

## Background

The Tammes problem (after P. M. L. Tammes, 1930, studying pollen grain
distributions) asks for the configuration of $n$ points on a sphere that
maximizes the smallest pairwise distance. Exact solutions are proven only
for small $n \in \{2, ..., 14, 24\}$. For other values the global optimum
is conjectured from long computational search.

For $n = 50$ the best-known configuration has been essentially fixed since
the Hardin–Sloane "Sphere Packings, Lattices and Groups" database (published
1996), and has not been improved in the intervening decades. The configuration
is rigid, with every point touching four or five neighbours along the minimum-
distance contact graph.

## Key References

- Hardin & Sloane, putatively optimal sphere codes (online database of
  sphere packings for $n \le 130$ in dimension 3)
- Musin & Tarasov, *The Tammes Problem for N = 14* (Experimental Math., 2015)
- Problem 6.34 of *Mathematical exploration and discovery at scale*
  ([arXiv:2511.02864](https://arxiv.org/abs/2511.02864))

## Arena Details

- **API ID**: 11
- **Direction**: maximize
- **Solution format**: `{"vectors": [[x, y, z] × 50]}` (each row normalized before scoring)
- **Scoring**: minimum pairwise Euclidean distance after L2 normalization
- **minImprovement**: fetched from `/api/problems` at submission time

## Approach

Warm-start from a seed configuration read from a local seed file (path
supplied via `--source`) and refine with an iterated constrained polish
that drives the residuals of the active pair set to machine precision on
the unit-sphere manifold. Score parity with the arena verifier is enforced
bit-exactly by the unit test suite.

*Last updated: 2026-04-06*
