---
type: source
kind: paper
title: Estimates for certain integrals of products of six Bessel functions
authors: D. O. E. Silva, C. Thiele
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.06309
source_local: ../raw/2015-silva-estimates-certain-integrals-products.pdf
topic: general-knowledge
cites:
---

# Estimates for certain integrals of products of six Bessel functions

**Authors:** D. O. E. Silva, C. Thiele  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.06309

## One-line
Establishes precise $O(n^{-4})$ numerical bounds for a family of integrals of sixfold Bessel-function products $\int_0^\infty J_{n+m}(r)J_n(r)J_m(r)J_0^3(r)\,r\,dr$ and the $J_1^2 J_0$ variant, needed to control a sharp Fourier restriction inequality on the circle.

## Key claim
**Theorem 1:** For integer $n \geq 2$ and even $0 \leq m \leq n$, the integrals $I_{0,m,n}$ and $I_{1,m,n}$ (defined in (5)-(6)) match explicit closed-form main terms (rational in $n$, dependent on $m$) up to error $< 0.002\,n^{-4}$ for $m \in \{0,2\}$ and $< 0.0015\,n^{-4}$ for $m \geq 4$, with a small finite set of low-$n$ exceptions tabulated to $\leq 0.01\,n^{-4}$.

## Method
Asymptotic expansion of the four lowest-order Bessel factors ($J_0$, $J_1$, $J_m$) to length-6 series with explicit remainder control (Lemma 6, Corollaries 7-9), reducing to core integrals $\int J_n J_{n+m} \sin(\ell r)\,r^{-k}\,dr$ for $\ell \in \{0,\pm 2,\pm 4\}$. These are evaluated via Kapteyn's orthogonality identity (Lemma 3) and its generalization (Lemma 4 via Weber-Schafheitlin), with $\ell = \pm 4$ residuals bounded by a contour-descent argument (Lemma 5). For $n < 20$, falls back to high-degree Newton-Cotes quadrature (degree 7) with Cauchy-integral derivative bounds, plus asymptotic tail analysis at $R = 63000$.

## Result
Explicit main terms include $I_{0,0,n} \approx \frac{3}{4\pi^2}\frac{1}{n} + \frac{3}{32\pi^2}\frac{1}{(n-1)n(n+1)}$, $I_{0,2,n} \approx \frac{15}{64\pi^2}\frac{1}{n(n+1)(n+2)}$, $I_{0,4,n} \approx \frac{1557}{1024\pi^2}\frac{1}{n(n+1)(n+2)(n+3)(n+4)}$, and analogous formulas for $I_1$. For $m \geq 6$ (even), both integrals are $O(n^{-4})$ with no main term. Table 1 gives numerical constants for $2 \leq n \leq 19$.

## Why it matters here
General background; no direct arena tie. Bessel-product integral technology is the analytic engine behind Fourier-restriction sharp constants — relevant if the agent ever tackles autocorrelation / uncertainty problems (P15, P16) via Fourier-side bounds, since the methods (Kapteyn orthogonality, Weber-Schafheitlin, asymptotic remainder bookkeeping) generalize.

## Open questions / connections
- Companion paper [1] (Carneiro-Foschi-Oliveira e Silva-Thiele, arXiv:1509.06674) uses these estimates to attack $C_{\mathrm{opt}}$ in the Tomas-Stein endpoint on $S^1$; conjecture that constants extremize the inequality remains open.
- The "elementary but laborious" approach hints that hypergeometric closed forms exist for sixfold Bessel products but extracting tight numerical bounds from them is not easier.
- Sharper Bessel bound $r^{1/2}|J_0(r)| \leq (2/\pi)^{1/2}$ from Landau [3] not used here — could tighten constants if reworked.

## Key terms
Bessel functions, Fourier restriction, Tomas-Stein inequality, Kapteyn identity, Weber-Schafheitlin, asymptotic expansion, Newton-Cotes quadrature, Stirling formula, sharp constants, sphere $S^1$, Poisson integral representation, hypergeometric integrals
