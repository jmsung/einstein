---
type: source
kind: paper
title: Spectrality and tiling by cylindric domains
authors: Rachel Greenfeld, Nir Lev
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1602.08850
source_local: ../raw/2016-greenfeld-spectrality-tiling-cylindric-domains.pdf
topic: general-knowledge
cites:
---

# Spectrality and tiling by cylindric domains

**Authors:** Rachel Greenfeld, Nir Lev  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1602.08850

## One-line
Proves that a cylindric set $\Omega = I \times \Sigma$ in $\mathbb{R}^d$ is spectral (resp. tiles by translation) if and only if its base $\Sigma \subset \mathbb{R}^{d-1}$ is spectral (resp. tiles).

## Key claim
**Theorem 1.1:** $\Omega = I \times \Sigma$ admits an orthogonal exponential basis in $L^2(\Omega)$ iff $\Sigma$ does in $L^2(\Sigma)$. **Theorem 1.2:** analogous statement for translational tiling. Consequence: Fuglede's conjecture holds for cylindric convex bodies in $\mathbb{R}^3$ — spectral $\Leftrightarrow$ tiling $\Leftrightarrow$ parallelepiped or centrally symmetric hexagonal prism.

## Method
Reduce to the normalized case $I = [-\tfrac{1}{2}, \tfrac{1}{2}]$ via affine invariance, then run an **iterative spectrum-modification procedure** adapted from Iosevich–Pedersen [IP98]. Each step applies a piecewise translation $\alpha_t$ that shifts only the non-integer-first-coordinate points of a spectrum $\Lambda$, and Corollary 4.3 (an orthogonality+packing↔tiling lemma via Kolountzakis's $f = |\hat{1}_\Omega|^2/|\Omega|^2$ tiling characterization) guarantees the result is still a spectrum. Take a weak limit of the sequence $\Lambda_n$ to get a spectrum $\Lambda' \subset \mathbb{Z} \times \mathbb{R}^{d-1}$, then apply Jorgensen–Pedersen [JP99] to slice it into spectra $\Gamma_k$ for $\Sigma$.

## Result
- A cylindric set over a smooth convex base in $\mathbb{R}^{d-1}$ ($d \geq 3$) is **not** spectral (in particular: cylinder over a ball is not spectral — settles a previously open question).
- A cylindric convex body in $\mathbb{R}^3$ is spectral iff it is a parallelepiped or centrally symmetric hexagonal prism.
- Theorem 7.1 generalizes: $\Omega = Q \times \Sigma$ with $Q$ a cube in $\mathbb{R}^n$ inherits spectrality/tiling from $\Sigma$ in either direction.

## Why it matters here
General background on Fuglede-type spectral/tiling equivalences and the weak-limit-of-spectra technique; no direct Einstein Arena problem tie. Potentially informs functional-inequality / autocorrelation problems where exponential-basis or tile-decomposition structure is exploited, and supplies a worked example of the "factor through a product structure" reduction.

## Open questions / connections
- Note added in proof (Kolountzakis): the "only if" half of Theorem 1.2 extends to arbitrary product sets $A \times B$, not just $I \times \Sigma$; analogous extension for spectral sets is **open**.
- Companion paper [GL16] uses Corollary 1.3 to establish Fuglede's conjecture for **all convex polytopes** in $\mathbb{R}^3$.
- Fuglede's conjecture remains open in dimensions $d = 1, 2$ (both directions); known false for $d \geq 3$ via Tao [Tao04] and successors.

## Key terms
Fuglede conjecture, spectral set, translational tiling, cylindric domain, orthogonal exponential basis, Iosevich-Pedersen, Jorgensen-Pedersen, Kolountzakis packing-tiling duality, weak limit of spectra, convex polytope tiling, centrally symmetric hexagonal prism, Fourier transform indicator function
