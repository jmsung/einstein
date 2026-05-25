---
type: source
kind: paper
title: Pure point measures with sparse support and sparse Fourier–Bohr support
authors: M. Baake, Nicolae Strungaru, Venta Terauds
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1908.00579
source_local: ../raw/2019-baake-pure-point-measures-sparse.pdf
topic: general-knowledge
cites:
---

# Pure point measures with sparse support and sparse Fourier–Bohr support

**Authors:** M. Baake, Nicolae Strungaru, Venta Terauds  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1908.00579

## One-line
Extends the theory of "doubly sparse" Fourier-transformable measures (pure point with locally finite support on both sides) from $\mathbb{R}^d$ to second-countable LCAGs, characterising them via cut-and-project schemes and crystallographic structure.

## Key claim
For a Fourier-transformable measure $\mu$ on an LCAG $G$ with Meyer-set support and sparse Fourier–Bohr spectrum, both $\mu$ and $\hat{\mu}$ must be supported on finite unions of translates of a lattice and its dual, and admit a representation as finite sums of trigonometric-polynomial-weighted lattice Dirac combs (Theorems 4.8, 4.10, 6.6).

## Method
Replaces tempered-distribution machinery with the general theory of Radon measures on LCAGs, leveraging cut-and-project schemes (CPS), weighted model combs, and the connection between Fourier transformability and almost periodicity. Uses van Hove sequence density formulas (Prop. 3.8), the qualitative uncertainty principle for LCAGs, and SAP/WAP measure decomposition to force the internal CPS space to have the form $\mathbb{Z}^m \times K$ with $K$ compact.

## Result
A dichotomy theorem: a measure with Meyer support is either fully crystallographic (lattice-supported with trigonometric-polynomial weights) or its support meets every open set's translates unboundedly often. For positive definite measures with uniformly discrete support and sparse FBS, derives a Poisson-summation-type formula $\hat{\omega}_h = \text{dens}(L)\,\omega_{\check{h}}$ over a CPS lattice $L$, with unique autocorrelation $\gamma = \text{dens}(L)\,\omega_{h*\tilde{h}}$ and pure point diffraction $\hat{\gamma} = \text{dens}(L)^2\,\omega_{|\check{h}|^2}$ (Cor. 5.5, 5.8).

## Why it matters here
General background for autocorrelation/Fourier-analytic problems on the arena — gives the structural template for "what doubly-sparse pure point measures must look like" (lattice-plus-finite-shifts with trig-poly weights), relevant when an optimizer's candidate measure shows sparse spectrum. No direct arena tie to a specific problem unless an autocorrelation or sphere-packing problem invites Poisson-summation arguments via CPS.

## Open questions / connections
- Whether Lemma 6.3 extends from uniformly discrete $\Lambda$ to weakly uniformly discrete support — would strengthen Section 6.
- Meyer's original question (PNAS 2016 [29]): does a fully Euclidean CPS admit nontrivial $(\mu, \hat{\mu})$ pair with model-set $\Lambda$ and locally finite spectrum? Cor. 6.9 answers it no under translation-boundedness; Cor. 6.10 extends to slowly increasing.
- Extends/parallels Lev–Olevskii [25,26] crystalline-measure results from $\mathbb{R}^d$ to LCAGs; relates to Kellendonk–Lenz [16], Favorov [10] on discrete-support tempered distributions.

## Key terms
doubly sparse measure, Fourier–Bohr spectrum, cut and project scheme, Meyer set, model set, weighted model comb, Poisson summation formula, crystallographic measure, almost periodic measure, locally compact Abelian group, qualitative uncertainty principle, van Hove sequence, weak uniform discreteness, autocorrelation, diffraction measure
