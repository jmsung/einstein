---
type: source
kind: paper
title: Exponentials rarely maximize Fourier extension inequalities for cones
authors: Giuseppe Negro, Diogo Oliveira e Silva, Betsy Stovall, J. Tautges
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.00356
source_local: ../raw/2023-negro-exponentials-rarely-maximize-fourier.pdf
topic: general-knowledge
cites:
---

# Exponentials rarely maximize Fourier extension inequalities for cones

**Authors:** Giuseppe Negro, Diogo Oliveira e Silva, Betsy Stovall, J. Tautges  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.00356

## One-line
Proves existence/precompactness of maximizers for all scale-invariant Fourier extension inequalities on the cone in $\mathbb{R}^{1+d}$, and shows the "exponential" $F$-functions are critical points of the $L^p \to L^q$ inequality if and only if $p=2$.

## Key claim
(Thm 1.1) For $1<p<p_0<2d/(d-1)$ and $q=q(p):=\frac{d+1}{d-1}p'$, conditional on boundedness of the extension operator at $p_0$, $L^p$-normalized maximizing sequences for $\|Ef\|_{L^q} \le C\|f\|_{L^p(d\mu)}$ are precompact modulo the symmetry group (dilations, Lorentz boosts, spacetime translations), so maximizers exist. (Thm 1.3) The Foschi-type $F$-functions $f_\star(\xi)=|\xi|^{-1}\exp(A|\xi|+b\cdot\xi+c)$, which maximize the Strichartz case $p=2$ for $d\in\{2,3\}$, satisfy the Euler–Lagrange equation for $L^p\to L^q$ extension on the cone **iff $p=2$**.

## Method
For Thm 1.1: two-stage frequency localization of maximizing sequences (dyadic annulus → angular sector) adapted to the cone's symmetry group, combined with profile decomposition; reduces non-$L^2$ case to the $L^2$ theory of Quilodrán/Ramos. For Thm 1.3: **Penrose transform** $g(x)=(1+X_0)^{(d-1)/2} G(X)$ conformally compactifying $\mathbb{R}^{1+d}\to[-\pi,\pi]\times S^d$, transforming $\|e^{itD}g\|_{L^q}^q = \tfrac12\int |e^{iTD_{S^d}}G|^q |\Omega|^{(d+1)(p'/2-1)}\,d\sigma dT$ where $\Omega=\cos T+\cos R$ is a symmetry breaker; test against zonal spherical harmonics $C_k^\nu$ of degree $k\ge 2$, evaluate via Gegenbauer/Bessel/Chebyshev identities, and split into subcritical ($1<p<2$, sign argument) and supercritical ($2<p<2d/(d-1)$, asymptotic analysis) regimes.

## Result
$F$-functions are not critical points (hence cannot maximize) for the conic extension inequality at any $p\ne 2$ in the conjectured range $1<p<2d/(d-1)$, $d\ge 2$. Conformal-factor exponent $\gamma_p=(d+1)(p'/2-1)$ is integrable on $[-\pi,\pi]\times S^d$ iff $p$ lies in the conjectured range — recovering the necessary conditions for the cone restriction conjecture as a byproduct. Vanishing of $\Omega$'s exponent at $p=2$ exposes a hidden $SO(d+1)$ rotational symmetry of the Strichartz functional, explaining why exponentials only extremize at $p=2$.

## Why it matters here
General background for sharp Fourier-extension / restriction theory; no direct arena tie among the current 23 problems, but the Penrose-transform symmetry-breaking argument is a transferable template for "when do Gaussian/exponential ansätze extremize a functional inequality?" — a recurring question for Cohn–Elkies-style magic-function approaches (sphere packing P1, kissing-number style problems) and autocorrelation/uncertainty problems where hidden conformal symmetry at the critical exponent can rule out simple closed-form maximizers off-critical.

## Open questions / connections
- Extending Thm 1.1/1.3 to the two-sheeted cone, where $F$-functions fail to be critical at $p=2$ in even spatial dimension (Negro 2023 [24]).
- Whether maximizers can be explicitly described in higher dimensions $d\ge 4$ at $p=2$ (Foschi's result only covers $d=2,3$).
- Parallel paraboloid/hyperbolic-paraboloid results (Christ–Quilodrán [11], Carneiro–Oliveira–Sousa [10]) used complex-analyticity of Gaussians; this paper's Penrose route handles the singular ansatz $|\xi|^{-1}e^{-|\xi|}$ — suggests a unified conformal-geometric framework for "exponentials rarely extremize" across quadric surfaces.

## Key terms
Fourier extension inequality, restriction conjecture, cone, Strichartz inequality, half-wave propagator, Penrose transform, F-function, Euler–Lagrange critical point, conformal symmetry breaker, Gegenbauer polynomial, spherical harmonic, profile decomposition, Foschi maximizer, Negro, Oliveira e Silva, Stovall
