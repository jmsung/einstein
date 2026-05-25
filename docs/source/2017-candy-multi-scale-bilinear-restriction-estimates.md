---
type: source
kind: paper
title: Multi-scale bilinear restriction estimates for general phases
authors: Timothy Candy
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1707.08944
source_local: ../raw/2017-candy-multi-scale-bilinear-restriction-estimates.pdf
topic: general-knowledge
cites:
---

# Multi-scale bilinear restriction estimates for general phases

**Authors:** Timothy Candy  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1707.08944

## One-line
Proves sharp adjoint bilinear restriction estimates $\|e^{it\Phi_1(-i\nabla)}f \cdot e^{it\Phi_2(-i\nabla)}g\|_{L^q_t L^r_x} \lesssim \|f\|_{L^2}\|g\|_{L^2}$ for general phases $\Phi_1,\Phi_2$ at different scales, in the full non-endpoint bilinear range, with explicit sharp dependence on phase curvature and transversality.

## Key claim
Under transversality/curvature Assumption 1.1 (a normalised version of the shape-operator condition), in the full range $1\le q,r\le 2$, $\tfrac{1}{q}+\tfrac{n+1}{2r}<\tfrac{n+1}{2}$, the constant in (1.1) satisfies $C \approx V_{\max}^{1/r-1}\,(\min\{H_1,H_2\})^{1/2-1/q}\,(\max\{H_1,H_2\})^{1/2-1/r}$ with $V_{\max}=\sup|\nabla\Phi_1(\xi)-\nabla\Phi_2(\eta)|$, $H_j=\|\nabla^2\Phi_j\|_\infty$ (Theorem 1.2). The dependence is sharp (no $\epsilon$-loss).

## Method
Follows Tao's endpoint-cone strategy: induction-on-scales using energy estimates across transverse hypersurfaces (wave-table decomposition), in place of Wolff-style combinatorial Kakeya arguments — this avoids the pigeonhole $\epsilon$-loss. Works directly for $\ell^2$-vector-valued waves, which by a transference principle automatically lifts the estimate to the adapted atomic space $U^2_\Phi$ (Corollary 1.6, Theorem 1.7).

## Result
Theorem 1.2/1.4 give the bilinear bound with explicit $C \approx d_0^{n+1-(n+1)/r-2/q}\,V_{\max}^{1/r-1}\,H_{\min}^{1/q-1/2}\,H_{\max}^{1/r-1/2}$, recovering (without $\epsilon$-loss) prior wave-cone bounds (Wolff, Tao, Tataru, Temur), paraboloid bounds (Tao), and elliptic/finite-type results (Lee–Vargas, Bejenaru, Stovall, Buschenhenke–Müller–Vargas). Applications: new sharp wave–Klein-Gordon bilinear estimates with differing masses (Thm 1.10), and a refined Strichartz inequality $\|e^{it\langle\nabla\rangle}f\|_{L^{2(n+1)/(n-1)}_{t,x}} \lesssim \|f\|_X^\theta \|f\|_{H^{1/2}}^{1-\theta}$ for some $\theta>0$ (Thm 1.12).

## Why it matters here
General background; no direct arena tie. Harmonic-analysis dispersive-PDE machinery (bilinear restriction, Strichartz refinements, $U^p/V^p$ spaces) is well outside the Einstein Arena problem families (sphere packing, autocorrelation, kissing, discrete combinatorics) — closest tangent would be uncertainty-principle / Fourier-restriction concepts, but no concrete arena problem currently maps here.

## Open questions / connections
- Endpoint case $\tfrac{1}{q}+\tfrac{n+1}{2r}=\tfrac{n+1}{2}$ for general phases remains open (only cone-endpoint known via Tao, Temur).
- Sharpness of the $C^{5n}$ smoothness requirement in (A2) — likely improvable.
- Linear restriction conjecture for surfaces with degenerate curvature: the multi-scale bilinear bounds here feed Stovall-type linear results but the full Stein conjecture for degenerate surfaces stays open.

## Key terms
bilinear restriction, adjoint restriction estimate, Fourier extension operator, wave equation, Klein-Gordon equation, Schrödinger paraboloid, transversality, curvature hypothesis, wave-table induction-on-scales, Wolff cone restriction, Tao endpoint, $U^p$ $V^p$ adapted function spaces, refined Strichartz inequality, shape operator, Bejenaru Candy Herr
