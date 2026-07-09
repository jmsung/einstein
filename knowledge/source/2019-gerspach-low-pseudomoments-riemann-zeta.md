---
type: source
kind: paper
title: Low Pseudomoments of the Riemann Zeta Function and Its Powers
authors: Maxim Gerspach
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.10224
source_local: ../raw/2019-gerspach-low-pseudomoments-riemann-zeta.pdf
topic: general-knowledge
cites:
---

# Low Pseudomoments of the Riemann Zeta Function and Its Powers

**Authors:** Maxim Gerspach  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.10224

## One-line
Determines the order of magnitude (up to $(\log\log x)^{O(1)}$) of all low pseudomoments $\Psi_{2q,\alpha}(x)$ of partial sums of $\zeta^\alpha$ on the critical line for $q \le 1/2$, $\alpha \ge 1$.

## Key claim
For $1 \le \alpha < 2$ and $q \le 1/2$: $\Psi_{2q,\alpha}(x) \ll (\log x)^{2(\alpha-1)q}$ when $0 < q < \frac{\alpha-1}{2\alpha-1}$ (with a $\log\log x$ factor at the threshold) and $\ll (\log x)^{(q\alpha)^2}$ when $\frac{\alpha-1}{2\alpha-1} < q \le 1/2$. Matching lower bounds (up to $(\log\log x)^{O(1)}$) hold for all $\alpha \ge 1$, $0 < q < 1/2$. Corollary: $\Psi_{2q}(x) \asymp (\log x)^{q^2}$ for all $q > 0$.

## Method
Probabilistic/Harper-style approach via the Bohr correspondence: replace partial sums by a random Steinhaus multiplicative function $f$ and reduce to moments of integrals of the random Euler product $F(s)=\prod_{p\le x}(1-f(p)/p^s)^{-1}$ on the critical line. Split the integration range into "small $T$" (where Euler factors are nearly constant on $[T,2T]$, requiring a small-prime / large-prime split at $\exp(1/T)$) and "large $T$" regimes, model $\log|F(1/2+it)|$ as a Gaussian field, and use maxima of (nearly) independent Gaussians plus comparison inequalities for Gaussian processes. Lower bounds use Jensen + multivariate CLT + Harper's Gaussian-process suprema bound; upper bounds use Plancherel for Dirichlet series and Rankin's trick.

## Result
Three growth regimes emerge with optimization point $\theta$ (where the dominant $T \asymp (\log x)^\theta$ contribution sits): $\theta = 0$ giving $(\log x)^{2(\alpha-1)q}$ for $1\le\alpha<2$, $q$ small; $\theta=-1$ giving $(\log x)^{(q\alpha)^2}$ for $1\le\alpha<2$, $q$ moderate; $\theta=\alpha^2/4-1$ giving $(\log x)^{q\alpha^2/2}$ for $\alpha\ge 2$. The phase transition at $q = \frac{\alpha-1}{2\alpha-1}$ contributes an extra $\log\log x$. Settles $\Psi_{2q}(x) \asymp (\log x)^{q^2}$ for all $q>0$, removing $(\log\log x)$ slack in Heap's bound.

## Why it matters here
General background; no direct arena tie. The probabilistic Euler-product / Gaussian-maximum machinery (split into small/large primes, maximum-of-Gaussian-field heuristic for sums of independent log-contributions) is a general technique for analyzing extremal behavior of sums of weakly-correlated random variables that could inform autocorrelation / additive-combinatorics problems where similar log-correlated structure appears.

## Open questions / connections
- Determine the exact exponent of $\log\log x$ in each regime (current bounds match in $\log x$ only).
- Extends Conrey–Gamburd [CG06], Bondarenko–Heap–Seip [BHS15], Heap [Hea18]; parallels Arguin–Ouimet–Radziwiłł [AOR19] on short-interval zeta moments.
- Connection to Fyodorov–Hiary–Keating conjecture and critical multiplicative chaos via Harper's "better than squareroot cancellation" framework.

## Key terms
pseudomoments, Riemann zeta function, Steinhaus random multiplicative function, Euler product, Bohr correspondence, critical line moments, Gaussian process suprema, Harper, multiplicative chaos, divisor function, Dirichlet polynomial, log-correlated field
