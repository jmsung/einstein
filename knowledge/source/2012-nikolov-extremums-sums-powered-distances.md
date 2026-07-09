---
type: source
kind: paper
title: On extremums of sums of powered distances to a finite set of points
authors: N. Nikolov, Rafael Rafailov
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1211.2975
source_local: ../raw/2012-nikolov-extremums-sums-powered-distances.pdf
topic: general-knowledge
cites:
---

# On extremums of sums of powered distances to a finite set of points

**Authors:** N. Nikolov, Rafael Rafailov  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1211.2975

## One-line
Full characterization of which points $M$ on a concentric sphere $\Gamma$ extremize $\sum_i |MA_i|^\lambda$ when $\{A_i\}$ are vertices of a regular simplex, cross-polytope, or hypercube — across all real $\lambda$.

## Key claim
For each of the three polytope families, the extremal points on $\Gamma$ are explicitly determined as a piecewise function of $\lambda$ (with breakpoints at $\lambda \in \{0, 2, 4, 6\}$ for cross-polytope/cube and $\{0, 2, 4\}$ for simplex), and the even integers $\lambda \in \{2, 4, 6\}$ (resp. $\{2, 4\}$ for simplex) are precisely the values for which $\sum_i |MA_i|^\lambda$ is constant on $\Gamma$ — i.e., these polytopes form spherical designs of corresponding strength.

## Method
Induction on dimension via slicing: intersect $\Gamma$ with hyperplanes parallel to facets, reducing the $n$-dim sum to a lower-dim sum on a codimension-2 sphere plus a constant offset $h$ (Pythagoras). Combined with: (a) Lemma 1 — a generalized polynomial $\sum a_i b_i^\lambda$ has at most $n-1$ real zeros (Rolle/Descartes-style), bounding how many $\lambda$ can give constancy; (b) Lemma 2/3 — connectivity of $\Gamma$ via chains of codim-2 slices parallel to two non-parallel hyperplanes (uses Jordan–Brouwer); (c) complex-polynomial / Newton's identities for converse characterizations in the plane.

## Result
- **Regular simplex** ($n+1$ vertices in $\mathbb{R}^n$): sum is constant iff $\lambda \in \{0, 2, 4\}$. For $\lambda < 0$ or $\lambda \in (2m, 2m+2)$, extremum is at $B_i$ (radial through vertex) or its antipode $-B_iO \cap \Gamma$ depending on parity of $m$; for $\lambda > 4$, max at antipode, min at $B_i$.
- **Cross-polytope** ($2n$ vertices): constant iff $\lambda \in \{0, 2, 4, 6\}$. Extrema alternate between vertices $B_i$ and face-centers $(\sum \pm B_i)/\sqrt{n}$.
- **Hypercube** ($2^n$ vertices): constant iff $\lambda \in \{0, 2, 4, 6\}$. Extrema alternate between vertex-radial points $B_i = (\pm c,\dots,\pm c)$ and face-center points $r e_i$.
- **Dodecahedron/Icosahedron** in $\mathbb{R}^3$: sum constant for $\lambda \in \{2, 4, 6, 8, 10\}$; these are the only even values in the allowed range (proved via reduction to regular decagon/hexagon slices).

## Why it matters here
Directly informs **spherical-design / cubature** structure underlying autocorrelation and packing problems: tells you exactly which moments $\sum |MA_i|^{2k}$ are invariant under $M$-rotation on $\Gamma$ — i.e., the strength of the polytope as a spherical $t$-design. Useful seed for any Einstein Arena problem where a candidate configuration is a regular polytope and one needs to know which power-sum constraints are automatic vs. binding (kissing-number candidates, energy minimization, polarization).

## Open questions / connections
- Conjecture 1: if $\sum |PA_i|^{2n-2}$ is constant on $\Gamma$, are $A_i$ vertices of a regular $n$-gon? (proved for $n=2,3$; open for $n \geq 4$).
- Conjecture 2/3: converse characterization for regular simplex ($n \geq 4$) and cross-polytope ($n \geq 3$) — sum-constancy at the right even powers implies the polytope is regular.
- Conjecture 4 (duality): if $P^*$ is the polar-dual polytope of $P$, then max-points of $\sum_{A \in V(P)} |MA|^\lambda$ coincide with min-points of $\sum_{A \in V(P^*)} |MA|^\lambda$. Verified for polygons/simplex/cube–cross-polytope; open for icosahedron–dodecahedron, 600-cell–120-cell.
- Counterexample noted: rotated unions of cross-polytopes in $\mathbb{R}^{2^k}$ satisfy the cube's constancy condition without being cubes — design-strength does not uniquely determine the configuration.

## Key terms
powered distances, regular simplex, cross-polytope, orthoplex, hypercube, dodecahedron, icosahedron, spherical design, polarization inequality, potential minimization, polar duality, Cohn–Kumar, Stolarsky, Newton's identities
