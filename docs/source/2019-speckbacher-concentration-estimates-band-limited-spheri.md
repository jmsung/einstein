---
type: source
kind: paper
title: Concentration Estimates for Band-Limited Spherical Harmonics Expansions via the Large Sieve Principle
authors: Michael Speckbacher, T. Hrycak
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.01670
source_local: ../raw/2019-speckbacher-concentration-estimates-band-limited-spheri.pdf
topic: general-knowledge
cites:
---

# Concentration Estimates for Band-Limited Spherical Harmonics Expansions via the Large Sieve Principle

**Authors:** Michael Speckbacher, T. Hrycak  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.01670

## One-line
Adapts the Donoho–Logan large-sieve principle to the unit sphere $S^2$, bounding how much a degree-$L$ spherical-harmonic expansion can concentrate on a set $\Omega$ in terms of a Nyquist-like density.

## Key claim
For $f\in S_L$ (spherical harmonics of degree $\le L$), $\lambda^2_{S_L}(\Omega)\le B_L\cdot\rho(\Omega,L)$, with $B_L=(1-t_{L,L})\bigl(\int_{t_{L,L}}^1 P_L^2(t)\,dt\bigr)^{-1}$ and $\lim_{L\to\infty}B_L=J_1(j_{0,1})^{-2}\approx 3.71038068570948$; constant $B_L$ is optimal within the approach, and the bound extends to $L^p$ as $\lambda^p_{S_L}(\Omega)\le (B_L\rho)^{\min(p-1,1)}$.

## Method
Spherical large-sieve via convolution with zonal filters supported in a cap $C_\delta(\eta)$. The optimal zonal filter is shown to be $g_\delta=\chi_{C_\delta(\eta)}\cdot P_L(\langle\cdot,\eta\rangle)$ — a spherical Beurling–Selberg-type extremal problem solved using monotonicity of Legendre polynomials past $t_{L,L}$ (the largest zero of $P_L$) plus Cauchy–Schwarz; asymptotics via the Mehler–Heine formula $P_n(1-z^2/2n^2)\to J_0(z)$. $L^p$ bounds follow by Riesz–Thorin interpolation and duality.

## Result
Theorem 3.3: explicit concentration bound (3) with optimal constant $B_L$. Theorem 4.1: classical large-sieve analogue on $S^2$ — for $\theta$-separated $x_1,\dots,x_R$, $\sum_k |S(x_k)|^2\le D(\theta,L)\sum |a_l^m|^2$ where $D(\theta,L)=2\pi(\int_{t_{L,L}}^1 P_L^2)^{-1}\cdot\bigl(1-\cos\tfrac{\theta}{2}\,t_{L,L}+\sin\tfrac{\theta}{2}\sqrt{1-t_{L,L}^2}\bigr)/(1-\cos\tfrac{\theta}{2})$. Sharpness: $D(\theta,L)\asymp L^2$ in $L$ and $\asymp 1/(1-\cos\theta)$ in $\theta$, matching elementary lower bounds up to constants (uses spherical-cap covering $R_{\max}(\theta)\le 2/(1-\cos\theta)$).

## Why it matters here
General background — provides the cleanest known density-based concentration / sampling bound for $S^2$ band-limited spaces, useful framing for any Einstein Arena problem where bandlimit + cap-density geometry interacts (e.g. spherical-cap packing analogues, kissing-configuration density bounds, autocorrelation-type inequalities on the sphere). Connects sphere-packing inequalities (cap-area covering $R_{\max}(\theta)\cdot 2\pi(1-\cos\theta)\le 4\pi$) to harmonic-analytic extremal problems of Beurling–Selberg type.

## Open questions / connections
- Is the constant $J_1(j_{0,1})^{-2}\approx 3.71$ tight beyond this approach, or only within zonal-filter methods (cf. Donoho–Logan optimality on $\mathbb{R}$)?
- Extension to $S^{d-1}$, $d>3$, with Gegenbauer polynomials in place of Legendre — would map directly onto kissing-number / Cohn–Elkies LP duals.
- Fourier dual to Li–Vaaler [20, Thm 4] trigonometric extremal problem suggests a unified Beurling–Selberg framework across $\mathbb{T}, \mathbb{R}, S^2$ worth distilling as a concept page.

## Key terms
large sieve inequality, Beurling-Selberg extremal problem, spherical harmonics, Legendre polynomials, Mehler-Heine formula, zonal convolution, Nyquist density, spherical cap packing, band-limited concentration, Donoho-Logan, Bessel function zero, $L^p$ interpolation
