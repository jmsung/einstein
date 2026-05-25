---
type: source
kind: paper
title: Finite field restriction estimates based on Kakeya maximal operator estimates
authors: Mark Lewko
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.8011
source_local: ../raw/2014-lewko-finite-field-restriction-estimates.pdf
topic: general-knowledge
cites:
---

# Finite field restriction estimates based on Kakeya maximal operator estimates

**Authors:** Mark Lewko  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.8011

## One-line
Establishes a formal two-way bridge between the finite-field restriction conjecture and the finite-field Kakeya conjecture, and uses Kakeya maximal operator bounds to break the Stein–Tomas barrier for the paraboloid over fields where $-1$ is a square.

## Key claim
For the $d=2n+1$ dimensional paraboloid $P$ over $\mathbb{F}$ with $-1$ a square, there exists $\delta_d > 0$ such that $\|(fd\sigma)^\vee\|_{L^{(2d+2)/(d-1) - \delta_d}(\mathbb{F}^d)} \lesssim \|f\|_{L^{(2d+2)/(d-1)}(P,d\sigma)}$; explicit values $\delta_3 = 1/04$ and $\delta_5 = 1/61 - \epsilon$ are obtained. Conversely, the $d$-dim restriction conjecture (Witt index $(d-1)/2$) implies the $(n+1)$-dim Kakeya conjecture.

## Method
Three-pronged decomposition of the dual restriction operator: (i) sharp analysis of near-extremizers of Stein–Tomas (which must concentrate on lines / affine totally-isotropic subspaces), (ii) a Mockenhaupt–Tao $L^2$ slicing/$TT^*$ argument when slices are non-degenerate, and (iii) a mixed-norm restriction estimate over cosets of maximal totally-isotropic subspaces derived from the Ellenberg–Oberlin–Tao Kakeya maximal bound. Uses Witt's theorem on quadratic forms over finite fields and induction on dimension; the 3-d case adds Bourgain–Katz–Tao sum-product incidence theory for a further $\delta$-improvement.

## Result
Theorem 3: for the 3-d hyperbolic paraboloid $H$, $\|(fd\sigma)^\vee\|_{L^{18/5}(\mathbb{F}^3)} \lesssim \|f\|_{L^{9/4}(H,d\sigma)}$ (sharp $q=9/4$ at $p=18/5$). Theorem 4 sharpens to $p=18/5-\delta$, $q=(18-5\delta)/(8-5\delta)$. Theorem 1 gives the first sub–Stein-Tomas exponents in any odd dimension where $-1$ is a square. Theorem 7 establishes $K_m^*((2m-1)/(2m-2) \to (2m-1)/(2m-2)) \lesssim |\mathbb{F}|^{(m-1)/(2m-1)}$, recovering Dvir-type lower bounds $|E| \gg |\mathbb{F}|^m$ for Kakeya sets.

## Why it matters here
General background; no direct arena tie — the paper is about finite-field harmonic analysis (restriction/Kakeya duality), not packing/autocorrelation/discrete-geometry optimization. Distantly informs the conceptual lesson that *extremizer concentration on low-dimensional subvarieties* (here: lines / isotropic subspaces) is a recurring obstruction-and-tool pattern, which echoes basin-rigidity and equioscillation-active-set thinking in arena problems.

## Open questions / connections
- Can the recursive additive-energy structure theorem for energetic subsets of quadratic surfaces (§13) be made quantitatively efficient? Author flags this as the likely bottleneck.
- Extension to the $p$-adic / mod-$N$ setting (Wright; Dummit–Hablicsek): do measure-zero Kakeya sets exist $p$-adically, and would they disprove endpoint paraboloid restriction over $\mathbb{Z}/p^k\mathbb{Z}$?
- Transfer of the "extremizer-must-concentrate-on-affine-subspace" lemma to the Euclidean Stein–Tomas / Bochner–Riesz setting via Carbery's slicing.
- $L^p$ mapping properties of unrestricted $k$-plane transforms in finite fields remain open.

## Key terms
finite field restriction conjecture, Kakeya maximal operator, Stein–Tomas inequality, paraboloid, hyperbolic paraboloid, quadratic form Witt index, totally isotropic subspace, Mockenhaupt–Tao slicing, Ellenberg–Oberlin–Tao, polynomial method, Bourgain–Katz–Tao sum-product, Bochner–Riesz, additive energy, Dvir theorem, extremizer concentration
