---
type: source
kind: paper
title: Packing Ellipsoids with Overlap
authors: Caroline Uhler, Stephen J. Wright
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.0235
source_local: ../raw/2012-uhler-packing-ellipsoids-overlap.pdf
topic: general-knowledge
cites:
---

# Packing Ellipsoids with Overlap

**Authors:** Caroline Uhler, Stephen J. Wright  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.0235

## One-line
A bilevel optimization framework for packing ellipsoids of prescribed sizes/shapes into an ellipsoidal container while minimizing pairwise overlap, applied to chromosome territory arrangement in cell nuclei.

## Key claim
Ellipsoidal containment can be encoded as a linear matrix inequality via the S-procedure, enabling a trust-region SDP-based algorithm with provable convergence to Clarke-stationary points for the (nonconvex) min-overlap problem; on uniform-sphere test cases the method recovers known optima (hexagonal lattice in 2D, FCC lattice in 3D, Lubachevsky–Graham curved hexagonal packings for $h(k)=3k(k+1)+1$ discs).

## Method
Containment $\bar E \subset E$ is rewritten via S-procedure as an LMI in $(\bar c, \bar S, c, S^2)$. For spheres, overlap $\xi_{ij}=\max(0, r_i+r_j-\|c_i-c_j\|)$ is minimized by Algorithm 1: successive linearization of the nonconvex distance constraint around the current iterate $z_{ij}=(c_i^- - c_j^-)/\|c_i^- - c_j^-\|$, giving a convex subproblem solvable by CVX. For ellipsoids, a bilevel scheme uses parametrized SDP duality to build a trust-region master model whose subproblems are convex relaxations.

## Result
Algorithm 1 either terminates at a Clarke-stationary point or accumulates only at stationary points / coincident-center degeneracies (Theorem 3.2); the ellipsoid version has analogous convergence (Theorem A.2 + Lemma A.3 establish Lipschitz/concave value-function properties for the parametrized SDP). Empirically, packing 150 unit-area circles in a circle of area $150\sqrt{12}$ produces visible hexagonal interior structure; 200 spheres in a sphere of volume $200\sqrt{18}$ give a neighbor-count histogram peaked at 12 (FCC signature) once boundary spheres are excluded. The chromosome application shows min-overlap alone produces wrong radial trend; adding homologous-pair separation penalty ($c=100$, $\lambda=1.25$) recovers experimentally observed larger-CT-on-periphery preference for ellipsoidal nuclei.

## Why it matters here
General background; no direct arena tie — Einstein Arena problems do not include overlapping ellipsoid packing in an ellipsoidal container, and the algorithmic recipe is biology-motivated rather than density-optimal. The S-procedure LMI form for ellipsoid-in-ellipsoid containment and the successive-linearization-of-distance trick may be reusable scaffolding for any constrained packing where pairwise distance constraints are nonconvex.

## Open questions / connections
- Does Algorithm 1's $\|\cdot\|_\infty$ objective with uniform radius-shrink recover certified optimal packings beyond hexagonal numbers $h(k)$, $k \leq 5$?
- Can the SDP-duality master model be adapted to non-overlap packing problems (Hardin–Sloane n-in-disc, kissing configurations) where the lower-level subproblem is also a parametrized SDP?
- Coincident-center stationary points are formally non-stationary for the original problem — random $z_{ij}$ choices were noted but not pursued; potential escape heuristic for stuck multistart on packing problems.

## Key terms
ellipsoid packing, sphere packing, S-procedure, linear matrix inequality, semidefinite programming, SDP duality, trust-region method, bilevel optimization, successive linearization, Clarke stationarity, hexagonal lattice, FCC lattice, curved hexagonal packing, Lubachevsky–Graham, chromosome territories, minimum overlap
