---
type: source
kind: paper
title: A sharp trilinear inequality related to Fourier restriction on the circle
authors: E. Carneiro, Damiano Foschi, D. O. E. Silva, C. Thiele
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.06674
source_local: ../raw/2015-carneiro-sharp-trilinear-inequality-related.pdf
topic: general-knowledge
cites:
---

# A sharp trilinear inequality related to Fourier restriction on the circle

**Authors:** E. Carneiro, Damiano Foschi, D. O. E. Silva, C. Thiele  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.06674

## One-line
Proves a sharp trilinear monotonicity inequality $T(h,h,h) \le T(c,c,c)$ (with $c$ the mean of $h$) that is the penultimate step in a six-step program to obtain the sharp $L^2\to L^6$ Tomas–Stein adjoint restriction constant on $S^1$, conditional on one remaining Cauchy–Schwarz-type conjecture.

## Key claim
For nonnegative antipodally symmetric $h\in L^1(S^1)$, the trilinear form $T(h_1,h_2,h_3):=\int_{(S^1)^6} h_1(\omega_1)h_2(\omega_2)h_3(\omega_3)(|\omega_4+\omega_5+\omega_6|^2-1)\,d\Sigma_\omega$ satisfies $T(h,h,h)\le T(c,c,c)$ with equality iff $h$ is constant. Conditional on Conjecture 4, $C_{\text{opt}}=(2\pi)^{-1/2}\|\widehat{\sigma}\|_{L^6(\mathbb R^2)}$ and all complex extremizers are $f(\omega)=c\,e^{i\xi\cdot\omega}$.

## Method
Spectral decomposition $h=c+g$ with $g\perp 1$ kills the linear term by rotational invariance; the bilinear term $T(c,g,g)$ becomes $-2c(2\pi)^5\sum_n |\hat g(n)|^2\beta_n$ where $\beta_n>0$ comes from sixfold Bessel integrals $\beta_n=\int_0^\infty J_n^2(r)J_0^2(r)(3J_1^2(r)-J_0^2(r))\,r\,dr$ with asymptotic $\beta_n \sim c_0/n^3$, $c_0=3/(8\pi^2)$. The trilinear term $T(g,g,g)$ is controlled by the bilinear term via a sharp Hardy inequality plus Cauchy–Schwarz, using companion-paper [arXiv:1509.06309] estimates for $\gamma_{n,m},\widetilde\gamma_{n,m}$ — the final coefficient $0.974<1$ closes the loop.

## Result
Theorem 2 (sharp trilinear inequality on $S^1$); Theorem 1 (constants are local extremizers of $\Phi(f)=\|\widehat{f\sigma}\|_{L^6}/\|f\|_{L^2}$); Theorem 6 (local Cauchy–Schwarz-type lower bound $\Psi(f)\ge 0$ near $f=1$ for all real $f$). Conditional Theorem 5: sharp Tomas–Stein constant on $S^1$ and full characterization of complex extremizers as imaginary exponentials, assuming Conjecture 4.

## Why it matters here
General background; no direct arena tie. Sixfold Bessel-integral asymptotics ($\beta_n\sim c_0/n^3$, $\delta_{n,m}$ decay) and the "linear + bilinear-controls-trilinear" spectral decomposition pattern are techniques that could inform autocorrelation / uncertainty-type extremization problems where Fourier-side spherical-harmonic decomposition is natural.

## Open questions / connections
- Conjecture 4 (the partially-negative-weight Cauchy–Schwarz step) remains open — only a local version near $f=1$ is proved.
- Sphere $S^2$ endpoint (Foschi 2015 [15]) and non-endpoint $S^d$, $3\le d\le 6$ (Carneiro–Oliveira e Silva [7]) are solved; $S^1$ endpoint is harder due to logarithmic singularity of $\sigma*\sigma*\sigma$ at $|x|=1$ and partially-negative weight.
- Existence of global extremizers established by Shao [30] (arXiv:1507.04302); this paper identifies them conditionally.

## Key terms
Tomas–Stein restriction, Fourier restriction on circle, sharp constant, trilinear form, Bessel function integrals, sixfold Bessel product, spectral decomposition, antipodal symmetry, Hardy inequality, Cauchy–Schwarz, extremizers, convolution of surface measures, Carneiro, Foschi, Oliveira e Silva, Thiele
