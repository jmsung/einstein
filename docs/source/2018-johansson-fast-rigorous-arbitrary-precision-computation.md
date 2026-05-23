---
type: source
kind: paper
title: Fast and rigorous arbitrary-precision computation of Gauss-Legendre quadrature nodes and weights
authors: Fredrik Johansson, M. Mezzarobba
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1802.03948
source_local: ../raw/2018-johansson-fast-rigorous-arbitrary-precision-computation.pdf
topic: general-knowledge
cites:
---

# Fast and rigorous arbitrary-precision computation of Gauss-Legendre quadrature nodes and weights

**Authors:** Fredrik Johansson, M. Mezzarobba  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1802.03948

## One-line
A hybrid algorithm for computing Gauss-Legendre quadrature nodes and weights at hundreds to tens of thousands of bits of precision, with rigorous interval-arithmetic error bounds, implemented in the Arb library.

## Key claim
For precision $p \sim \alpha n$, Gauss-Legendre nodes/weights can be computed to $p$-bit accuracy in $\tilde{O}(n^2)$ bit operations (Theorem 1); in practice, a hybrid method delivers order-of-magnitude speedups over Pari/GP and ARPREC at $p \in [10^3, 10^4]$ digits (e.g. $n{=}2000, p{=}1024$: $474\text{s}\to 1.12\text{s}$, $423\times$ speedup; full ARPREC precomputation $1300\text{s}\to 32\text{s}$).

## Method
Four-method hybrid evaluator for $P_n(x)$ on $[0,1]$, dispatched by $(n, p, x)$: (i) Bonnet three-term recurrence in fixed-point GMP arithmetic with an a-priori roundoff bound $(n+1)(n+2)\bar\varepsilon/4$ (Proposition 5); (ii) large-$n$ asymptotic hypergeometric expansion; (iii) monomial-basis expansion at $0$; (iv) terminating expansion at $1$. Hypergeometric sums are evaluated by *rectangular splitting*; all stages use midpoint-radius ball arithmetic; roots are isolated via Petras-style initial values and refined by interval Newton iteration at doubling precision. Bernstein-type majorant bounds on $|P_n'|, |P_n''|$ (Proposition 3) propagate enclosure widths.

## Result
Bit complexity $\tilde{O}(n^2)$ when $p\sim\alpha n$ (matching Clenshaw-Curtis and tanh-sinh asymptotics up to log factors), reducing to $\tilde{O}(n)$ when $p=O(1)$. The asymptotically fast multipoint-evaluation algorithm of Theorem 1 has too high overhead to beat the hybrid for $n,p \le 10^5$. Bernstein-type a-priori bounds: $|P_n'(x)| \le \min\!\big(\tfrac{\sqrt n}{2^{3/2}\sqrt\pi (1-x^2)^{3/4}},\; \tfrac{n(n+1)}{2}\big)$, $|P_n''(x)| \le \min\!\big(\tfrac{n^{3/2}}{2^{5/2}\sqrt\pi (1-x^2)^{5/4}},\; \tfrac{(n-1)n(n+1)(n+2)}{8}\big)$. The Arb implementation produces certified 53-bit correctly-rounded values via Ziv's strategy.

## Why it matters here
General background; no direct arena tie. Could matter if an arena problem needs rigorous high-precision integration of an analytic kernel (e.g. Cohn-Elkies-style LP dual checks, modular-form integrals, or mpmath-substitute polish work) — Arb's certified Gauss-Legendre gives interval enclosures stronger than mpmath's float arithmetic, relevant to the triple-verify discipline.

## Open questions / connections
- Extension to Jacobi / Hermite / Laguerre weights — same hypergeometric/recurrence machinery, blocked mainly by lack of error-bounded large-$n$ asymptotics.
- For $p \gg 10^6$, would the bit-burst hypergeometric method or fast multipoint evaluation overtake the hybrid? Empirically uncertain.
- How does certified Gauss-Legendre compare to certified tanh-sinh in Arb for endpoint-singular integrands arising in LP/SDP dual computations?

## Key terms
Gauss-Legendre quadrature, Legendre polynomials, Bonnet recurrence, ball arithmetic, midpoint-radius interval arithmetic, interval Newton method, arbitrary-precision arithmetic, Arb library, hypergeometric series, rectangular splitting, Bernstein inequality, Petras, Clenshaw-Curtis, double exponential quadrature, rigorous error bounds
