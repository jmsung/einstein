---
type: source
kind: paper
title: Periodic structure of translational multi-tilings in the plane
authors: Bochen Liu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1809.03440
source_local: ../raw/2018-liu-periodic-structure-translational-multi-tilings.pdf
topic: general-knowledge
cites:
---

# Periodic structure of translational multi-tilings in the plane

**Authors:** Bochen Liu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1809.03440

## One-line
Proves that every convex polygon which multi-tiles the plane by translations also admits a lattice multi-tiling, and that all such multi-tilings are periodic.

## Key claim
Main theorem (Theorem 1.6): if $f \in L^1(\mathbb{R}^d)$ and $\delta_\Lambda = \sum_{j=1}^n \delta_{L_j + z_j}$ is a finite union of translated lattices, and $f + \Lambda$ tiles with a weight, then for each $j$ there is a lattice $\overline{L_j} \supset L_j$ such that $f + \overline{L_j}$ also tiles (with possibly different weight). Corollary 1.7: any convex polygon multi-tiling the plane admits a lattice multi-tiling. Theorem 1.9: every multi-tiling of a non-parallelogram convex polygon in $\mathbb{R}^2$ is periodic.

## Method
Fourier-analytic: Poisson summation converts the tiling identity into $\hat f$ vanishing on a union of cosets in $\mathbb{Z}^d \setminus \{0\}$. The crux uses the Evertse–Schlickewei–Schmidt theorem (2002) on linear equations in multiplicative groups to bound non-degenerate solutions of $\sum a_i x_i = 1$, forcing the "bad" frequencies to lie in finitely many cosets of subgroups. A subgroup-extension lemma then enlarges each $L_j$ to a lattice on which $\hat f$ vanishes. For polygons, Bolle's edge/translation-vector characterization is combined with zonotope identities $\tau_j - \tau_{j+1} = e_j + e_{j+1}$ to give a polynomial-time criterion (Theorem 1.8).

## Result
Theorem 1.8 gives an efficient (polynomial in $m$) criterion: a symmetric $2m$-gon with edge vectors $e_1,\dots,e_m$ and translation vectors $\tau_1,\dots,\tau_m$ multi-tiles iff (i) $m$ odd and $\mathrm{span}_{\mathbb{Z}}\{\tau_1,\dots,\tau_m\}$ is a lattice, or (ii) $m$ even and some $j_0$ exists with $\mathrm{span}_{\mathbb{Z}}\{\tau_j : j\ne j_0\}$ a lattice and $\det(e_{j_0},\tau_{j_0}) \in \det(\Lambda_{j_0})\cdot\mathbb{Q}$. Yields first explicit construction of symmetric $2m$-gons ($m\ge 4$) that do *not* multi-tile (take $e_j$ rationally independent). Also yields exponential Riesz bases for every convex polygon admitting a multi-tiling.

## Why it matters here
General background; no direct arena tie. Touches discrete-geometry / lattice structure (relevant to packing-style problems and Fourier-analytic methods on lattices), but the 23 Einstein Arena problems do not currently feature planar multi-tiling questions.

## Open questions / connections
- Problem 1.4 (Gravin–Robins–Shiryaev): does every convex polytope multi-tiling $\mathbb{R}^d$ admit a lattice multi-tiling? Still open for $d \ge 3$ outside two-flat zonotopes.
- Is the "finite union of translated lattices" hypothesis in Theorem 1.6 necessary? Does there exist $f \in L^1(\mathbb{R}^d)$ tiling by translations but by no lattice with any weight? (Kolountzakis–Lev 2016 partial counterexamples in 1D.)
- Lagarias–Wang rationality fails for indecomposable planar multi-tilings (Example 6.3): octagon example with $\Lambda = \mathbb{Z}\times 2\mathbb{Z} + \{0,\alpha\}$, $\alpha \notin \mathbb{Q}^2$.

## Key terms
multiple tiling, translational tiling, zonotope, convex polygon, lattice tiling, Poisson summation, Evertse–Schlickewei–Schmidt, Bolle theorem, Venkov–McMullen, periodic tiling conjecture, Kolountzakis, exponential Riesz basis, centrally symmetric polytope
