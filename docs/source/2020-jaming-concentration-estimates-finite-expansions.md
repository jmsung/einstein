---
type: source
kind: paper
title: Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle
authors: Philippe Jaming, Michael Speckbacher
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.02474
source_local: ../raw/2020-jaming-concentration-estimates-finite-expansions.pdf
topic: general-knowledge
cites:
---

# Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle

**Authors:** Philippe Jaming, Michael Speckbacher  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.02474

## One-line
Generalizes the Donoho–Logan large-sieve concentration inequality from the 2-sphere to all compact two-point homogeneous spaces (spheres + real/complex/quaternion/Cayley projective spaces), bounding the $L^2$ mass of a finite Laplace–Beltrami eigenfunction expansion on a measurable set $\Omega$ by a maximum Nyquist density.

## Key claim
For $M$ a compact two-point homogeneous space, $f \in S_K = \bigoplus_{k \le K} H_k$, and $\Omega \subset M$ measurable: $\int_\Omega |f|^2\,d\nu \le A_K \cdot \rho(\Omega,K) \cdot \|f\|_2^2$, where $\rho(\Omega,K) = \sup_{y\in M} |\Omega \cap C_{t_K(M)}(y)| / |C_{t_K(M)}(y)|$ uses geodesic caps of radius set by the largest zero $t_{K,K}$ of the Jacobi polynomial $P_K^{(\alpha,\beta)}$, with $(\alpha,\beta)$ determined by $M$ via (3.20).

## Method
Bell-Labs / Landau–Slepian–Pollak duality: bound concentration via an optimal zonal "filter" supported on a geodesic cap, then use the convolution theorem in the spherical-harmonic basis (Theorem 3.2) to reduce the extremal problem to a single coefficient ratio. The minimizer is the truncated Jacobi polynomial $g_{K,\delta} = \chi_{C_\delta(\eta)} \cdot P_K^{(\alpha,\beta)}(\cos\gamma d(\cdot,\eta))$ (Theorem 4.2), valid because a new monotonicity lemma (Lemma 2.1) shows $P_k^{(\alpha,\beta)}(t)/P_k^{(\alpha,\beta)}(1)$ is dominated by $P_{k-1}^{(\alpha,\beta+1)}(t)/P_{k-1}^{(\alpha,\beta+1)}(1)$ on $[t_{n,n},1)$.

## Result
Explicit constant $A_K$ in (4.37) using the incomplete beta function and a Jacobi-weight integral; asymptotically $\lim_{K\to\infty} A_K = \frac{1}{\alpha+1}\left(\frac{j_{\alpha,1}}{2}\right)^{2\alpha}\frac{1}{J_{\alpha+1}(j_{\alpha,1})^2}$ where $j_{\alpha,1}$ is the first positive Bessel zero. Extends to $L^p$ for $1<p<\infty$ with $\lambda_p(\Omega,K) \le (A_K \rho(\Omega,K))^{\min(p-1,1)}$ via interpolation/duality (Theorem 4.6). On $S^2$ it exactly recovers Speckbacher–Hrycak [23].

## Why it matters here
General background on harmonic-analysis concentration inequalities on symmetric spaces — relevant for any Einstein Arena problem framed as a finite eigenfunction expansion on a sphere or projective space (sphere-packing LP bounds via Cohn–Elkies, kissing-number SDP on $S^{d-1}$, autocorrelation problems with zonal kernels). The Jacobi-polynomial monotonicity (Lemma 2.1) and the explicit asymptotic constant via Bessel zeros are reusable building blocks.

## Open questions / connections
- Does the maximum-Nyquist-density bound improve the *single-eigenfunction* case? Paper notes their method gives no improvement there — gap worth understanding for arena problems pinned to one $H_k$.
- Extends Donoho–Logan [5] (real line), Speckbacher–Hrycak [23] ($S^2$), Abreu–Speckbacher [1,2] (time-frequency) — uniform sieve framework across symmetric spaces.
- Connection to Carleson measures on compact manifolds (Ortega-Cerdà–Pridhnani [20]) and prolate spheroidal / Slepian concentration on the sphere (Simons–Dahlen–Wieczorek [21]).

## Key terms
large sieve principle, maximum Nyquist density, two-point homogeneous space, compact symmetric space rank 1, Jacobi polynomials, spherical harmonics, Laplace-Beltrami eigenfunctions, geodesic cap, zonal function, Donoho-Logan inequality, Bessel zeros, addition formula, Mehler-Heine, Bell-Labs concentration, Slepian-Pollak
