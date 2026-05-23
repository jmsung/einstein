---
type: source
kind: paper
title: Computing Upper Bounds for the Packing Density of Congruent Copies of a Convex Body
authors: F. M. D. O. Filho, F. Vallentin
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1308.4893
source_local: ../raw/2013-filho-computing-upper-bounds-packing.pdf
topic: general-knowledge
cites:
---

# Computing Upper Bounds for the Packing Density of Congruent Copies of a Convex Body

**Authors:** F. M. D. O. Filho, F. Vallentin  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1308.4893

## One-line
Generalizes the Cohn–Elkies linear programming bound for sphere packings to congruent (rotated + translated) copies of an arbitrary convex body via semidefinite programming on the Euclidean motion group $M(n) = \mathbb{R}^n \rtimes SO(n)$.

## Key claim
For any convex body $K \subseteq \mathbb{R}^n$ and any continuous real-valued $f \in L^1(M(n))$ of positive type with $f(x,A) \leq 0$ whenever $K^\circ \cap (x+AK^\circ) = \emptyset$ and $\lambda = \int_{M(n)} f \, d(x,A) > 0$, the density of any packing of congruent copies of $K$ is at most $(f(0,I)/\lambda)\,\mathrm{vol}\,K$. Applied to regular pentagons in $\mathbb{R}^2$, this yields an upper bound of $0.98103$.

## Method
Reformulates packing density as the independence number of an infinite "packing graph" on $M(n)$, then extends the Lovász $\vartheta'$ number to graphs over compact measure spaces via continuous positive kernels (Theorem 2.1). Searches for the witness function $f$ using SDP + sums-of-squares + harmonic analysis of $M(2)$ (Laguerre-polynomial basis, block-diagonalization by 5-fold pentagon symmetry $S(K)$, irreducible representations indexed by Bessel-type radial functions). Nonpositivity outside the Minkowski difference $K - AK$ is enforced via SOS for $\rho \geq 1$ plus a discretized sample of ~6.5M points for $\rho \leq 1$, with the body slightly enlarged ($1.02K$) to absorb numerical slack.

## Result
Proves Theorem 1.1 (the SDP-bound generalization). Concrete instantiation: regular pentagon packing density $\leq 0.98103$, computed by solving an SDP with $d=11$, $N=5$, 537 sample points, polished to 256-bit precision, solver CSDP. Best known construction is the Kuperberg–Kuperberg double-lattice at $(5-\sqrt{5})/3 \approx 0.9213$; Hales–Kusner subsequently improved the upper bound to $0.9611$ by a different (Voronoi) method.

## Why it matters here
Directly informs the SDP-on-motion-group bounding technique relevant to any arena problem involving packings of non-spherical congruent bodies in $\mathbb{R}^2$ or $\mathbb{R}^3$ (pentagons, polygons, tetrahedra, polytopes). Sits alongside the Cohn–Elkies LP bound in the wiki's bounds-toolbox: when only translations are allowed → LP suffices; when rotations matter → escalate to this SDP framework.

## Open questions / connections
- Extension to $M(3)$ for tetrahedron packings (much harder harmonic analysis; the authors' stated long-term goal).
- Does a complex-SDP solver close the gap from $0.98103$ to the Hales–Kusner $0.9611$ or the conjectured $0.9213$ optimum?
- Can the discretization-heuristic for the Minkowski-difference exterior be replaced by a pure SOS certificate at tractable matrix size?
- Generalizes Delsarte's LP method (compact case) and Cohn–Elkies (noncompact commutative $\mathbb{R}^n$) to the noncompact noncommutative $M(n)$.

## Key terms
convex body packing, Cohn-Elkies bound, Lovász theta number, semidefinite programming, sums of squares, Euclidean motion group, harmonic analysis, pentagon packing, Minkowski difference, positive-type function, Laguerre polynomials, Delsarte LP method
