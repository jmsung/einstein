---
type: source
kind: paper
title: A universality law for sign correlations of eigenfunctions of differential operators
authors: F. Gonccalves, D. O. E. Silva, S. Steinerberger
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.06826
source_local: ../raw/2019-gonccalves-universality-law-sign-correlations.pdf
topic: general-knowledge
cites:
---

# A universality law for sign correlations of eigenfunctions of differential operators

**Authors:** F. Gonccalves, D. O. E. Silva, S. Steinerberger  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.06826

## One-line
For WKB-type eigenfunction sequences $\{w_n\}$ (Schrödinger, Hermite, Laguerre, Chebyshev), the asymptotic fraction of indices $n$ at which $w_n(x)$ and $w_n(y)$ share sign is universally trapped in $[1/3, 2/3]$ — never $1/2$ generically, but never extreme.

## Key claim
**Theorem 1:** If $w_n(x) = (1+o_n(1))\,\phi(x,n)\cos(2\pi(\mu_n\varphi(x) - \theta))$ with the equidistribution hypothesis on $\{p^{-1}\mu_n\varphi(x)\}$, $\{q^{-1}\mu_n\varphi(y)\}$, then $1/3 \le \ell_{\{w_n\}}(x,y) \le 2/3$, and both bounds are attained (e.g. $\varphi(x)=3\varphi(y)$).
**Theorem 2 (sharper):** For even Schrödinger potentials, when $x/y = p/q$ (coprime), $\ell = 1/2 + 1/(2pq)$ if $p\equiv q\equiv 1$ or $\equiv 3\pmod 4$, else $1/2$; irrational $x/y$ gives exactly $1/2$.

## Method
Reduce the sign-correlation limit to an integral $\frac{1}{T}\int_0^T \mathrm{sgn}(\cos(2\pi A t)\cos(2\pi B t))\,dt$ over rays on the 2-torus $\mathbb{T}^2$. Apply Weyl equidistribution: irrational slope $B/A$ averages to $0$; rational slope $p/q$ yields a Fourier-series sum $\frac{8}{\pi^2 pq}\sum (2\ell+1)^{-2}\cos(\cdot)$ which is nonzero only when both $p,q$ odd, and bounded by $1/|pq|$. WKB asymptotics (proved via Grönwall on the Volterra integral form of the Schrödinger ODE) bring eigenfunctions into the cosine form Theorem 1 requires.

## Result
The universal envelope $[1/3, 2/3]$ holds for all WKB-type sequences. The exact rational-ratio formula $1/2 \pm 1/(2pq)$ (with the mod-4 selector) follows from the Fourier kernel sum. Applied: Hermite functions give $\ell = 1/2 + 1/(2xy)$ when $xy\equiv 1\pmod 4$ (Prop 3); Laguerre functions in $\mathbb{R}^d$ give a $d$-dependent variant (Prop 4). Empirically for Chebyshev $T_n$ at $\cos(\pi/2^{10})$ vs $\cos(3\pi/2^{10})$, the discrepancy from $N/3$ stays $\le 10$ for $N\le 10^4$ — a bounded-remainder phenomenon hinting at superuniformity.

## Why it matters here
General background; no direct arena tie. Touches the Hilbert/Cohn family of uncertainty- and equidistribution-flavored problems via the linear-flow-on-torus machinery, which is also the analytic backbone of Cohn–Elkies-type sphere-packing bounds and autocorrelation/uncertainty problems (P5, P6, P11, P14, P17). The Fourier-series reduction of an indicator integral on $\mathbb{T}^2$ is the same template used in many extremal constructions.

## Open questions / connections
- Extend to $\ge 3$-point sign correlations: which configurations $(+,-,+,-,-)$ admit nontrivial universal bounds?
- Characterize Schrödinger potentials $V$ for which the equidistribution hypothesis (H2) on $\{\sqrt{\lambda_n}\,x\}$ actually holds; eigenvalue equidistribution theory is underdeveloped.
- Connection to Beck's superuniformity theory and Grepstad–Larcher bounded-remainder sets — Chebyshev observation suggests far stronger error terms in special cases.
- Extends prior work [Goncalves–Silva–Steinerberger, JMAA 2017] on Hermite roots and an uncertainty principle.

## Key terms
WKB approximation, Schrödinger operator, Hermite functions, Laguerre polynomials, Chebyshev polynomials, sign correlation, equidistribution modulo 1, linear flow on torus, Weyl equidistribution, bounded remainder sets, superuniformity, Fourier series, eigenfunction asymptotics, Grönwall inequality
