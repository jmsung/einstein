---
type: source
kind: paper
title: Multivariate polynomial approximation in the hypercube
authors: L. Trefethen
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.02216
source_local: ../raw/2016-trefethen-multivariate-polynomial-approximation-hypercu.pdf
topic: general-knowledge
cites:
---

# Multivariate polynomial approximation in the hypercube

**Authors:** L. Trefethen  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.02216

## One-line
Proves that geometric convergence of polynomial approximation on $[-1,1]^s$ is governed by the **Euclidean degree** $\|k\|_2$ of monomial exponents, not the more familiar total or maximal degrees.

## Key claim
If $f$ is analytic in the region where $x_1^2+\cdots+x_s^2 \in N_{s,h^2}$ (Assumption A), then $\inf_{d(p)\le n}\|f-p\|_{[-1,1]^s} = O_\varepsilon(\rho^{-n})$ with $\rho = h+\sqrt{1+h^2}$ when $d=d_E$ or $d_{\max}$, but only $O_\varepsilon(\rho^{-n/\sqrt{s}})$ when $d=d_T$ (total degree) — a $\sqrt{s}$-factor penalty in the exponent for using total degree.

## Method
Lifts the 1D Bernstein–Chebyshev ellipse estimate to $s$ dimensions via a Bochner–Martin polycylinder bound (Lemma 5.1) on multivariate Chebyshev coefficients. The crux is a Minkowski-sum inequality $N_{1,h_1^2}\oplus\cdots\oplus N_{1,h_s^2}\subseteq N_{s,h_1^2+\cdots+h_s^2}$ on "Newton ellipses" (Arnol'd), with weights $c_j = k_j/\|k\|_2$ optimized per monomial so that the resulting decay $\rho_1^{-k_1}\cdots\rho_s^{-k_s} = \rho^{-\|k\|_2}$ depends only on the Euclidean norm of $k$.

## Result
Theorem 4.2: three convergence rates split as $\rho^{-n/\sqrt{s}}$ (total), $\rho^{-n}$ (Euclidean), $\rho^{-n}$ (max). Numerical confirmation on the 2D Runge function $1/(1+10(x^2+y^2))$ matches the predicted slopes. Quantitatively in $s=10$, an isotropic analytic function needs ~11.1× fewer degrees of freedom under Euclidean degree than under total degree, and ~401.5× fewer than under maximal degree — an exponential-in-$s$ effect.

## Why it matters here
Directly relevant to **any arena problem posed as polynomial optimization / approximation on a hypercube** (functional inequalities, autocorrelation extremal problems, density-bound LPs over polynomial bases): basis truncation by $\|k\|_2$ rather than $\|k\|_1$ gives the same accuracy with exponentially fewer variables. Also informs cubature/quadrature design when integrating learned surrogates of the score function.

## Open questions / connections
- Converse theorem (Bernstein-style) to show the $\sqrt{s}$ gap between $d_T$ and $d_E$ is sharp, not just an upper-bound artifact.
- Optimal sampling/interpolation nodes for Euclidean-degree spaces (Padua-like sets in higher $s$) — not addressed here.
- Extends Hale–Trefethen 2008 (nonuniform resolving power, translation) to the rotational-anisotropy axis; combining both could yield further $\pi/2$-style improvements.
- Connects to cubature lineage: Maxwell 1877 → Krommer–Ueberhuber → modern total-degree exactness rules are suboptimal in this lens.

## Key terms
multivariate polynomial approximation, Euclidean degree, total degree, maximal degree, Chebyshev series, Bernstein ellipse, Newton ellipse, polycylinder, hypercube cubature, isotropic functions, Bochner-Martin, Trefethen, Runge function, curse of dimensionality
