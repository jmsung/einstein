---
type: source
kind: paper
title: Exponential polynomials and identification of polygonal regions from Fourier samples
authors: Mihail N. Kolountzakis, Emmanuil Spyridakis
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2409.01432v2
source_local: ../raw/2024-kolountzakis-exponential-polynomials-identification-pol.pdf
topic: general-knowledge
cites: 
---

# Exponential polynomials and identification of polygonal regions from Fourier samples

**Authors:** Mihail N. Kolountzakis, Emmanuil Spyridakis  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2409.01432v2

## One-line
Shows that bivariate exponential polynomials with $\le N$ terms and polynomial coefficients of degree $<D$ — and consequently certain polygonal regions in the plane — can be uniquely identified from a *nonadaptive*, a priori fixed set of Fourier samples of size $O(D^2 N \log N)$.

## Key claim
For $f(\xi,\eta) = \sum_{j=1}^n p_j(\xi,\eta) e^{-2\pi i (x_j \xi + y_j \eta)}$ with $n \le N$, $(x_j,y_j) \in \mathbb{T}^2$, $\deg p_j < D$, the sampling set $A_{2N} = \bigcup_{1 \le r \le 2N} [2\lfloor 2N/r\rfloor D]_0 \times [2rD]_0 \subset \mathbb{Z}^2$, of size $O(D^2 N \log N)$, determines $f$ uniquely (Theorem 2.1). As corollaries: any axis-parallel polygon with $\le N$ vertices is determined by $O(N \log N)$ Fourier samples; any polygon with $\le N$ vertices and $\le k$ (possibly unknown) edge-slopes by $O(k^2 N \log N)$ samples.

## Method
The construction is layered: Prony-style recurrence-order arguments handle univariate exponential polynomials on $[2ND]_0$ (Lemma 2.1); a Vandermonde argument handles bivariate algebraic polynomials on $[D]_0^2$ (Lemma 2.2); these combine into a recursive "fiber + frequency-multiplicity bucket" scheme that yields the $\log N$ factor via the pigeonhole bound $|X_t \cup \cdots \cup X_r| \le \lfloor N/t \rfloor$ on $x$-projections. The polygon application uses the Brion–Barvinok formula for the Fourier transform of an indicator function, multiplied by $\prod_r (s_r \cdot t)$ to clear denominators and produce an exponential polynomial of degree $<k-1$. Uniqueness is proved *non-constructively* by contradiction (Lemmas 2.5 vs 2.6): finitely many polynomials match given data + projections, but two distinct matches would generate a continuum $\lambda f_1 + (1-\lambda) f_2$.

## Result
Sample-complexity is only a $\log N$ factor above the parameter count $O(D^2 N)$ — essentially optimal up to logs and matching the univariate Prony bound modulo dimension. The unknown-slope case (Corollary 3.3) costs only a factor-2 blow-up in both $k$ and $N$ because $f_1 - f_2$ has parameters $(2k, 2N)$. Slope-count dependence is quadratic in $k$, which the authors flag as suboptimal (Remark 3.2) since the polynomial coefficients are products of $\le k$ linear forms involving only $2k$ parameters.

## Why it matters here
General background; no direct arena tie. Potentially relevant as a sampling-theoretic analogue for problems involving Fourier-side characterizations of geometric configurations (sphere packing via Cohn–Elkies, autocorrelation problems), where minimal-sample identification of a structured object from its FT could inform verifier design or cross-check methods, but the connection is indirect.

## Open questions / connections
- Can the quadratic-in-$k$ dependence be reduced to linear by exploiting that polygon polynomial coefficients are products of linear forms ($2k$ params, not $k^2$)?
- Adaptive vs nonadaptive trade-off: Wischerhoff–Plonka [WP16] achieves reconstruction with adaptive sampling; what's the tight nonadaptive lower bound?
- Extension to higher-dimensional polytopes via the Brion–Barvinok formula in $\mathbb{R}^d$ — sample size scaling with facet/slope count?
- Algorithmic inversion is open; the paper proves only injectivity, not a reconstruction procedure.

## Key terms
exponential polynomials, Prony method, nonadaptive sampling, Fourier sampling, polygon reconstruction, Brion-Barvinok formula, indicator function Fourier transform, Vandermonde, linear recurrence, generalized power sums, sparse exponential sums, Kolountzakis
