---
type: source
kind: paper
title: Computing Hypergeometric Functions Rigorously
authors: Fredrik Johansson
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1606.06977
source_local: ../raw/2016-johansson-computing-hypergeometric-functions-rigorously.pdf
topic: general-knowledge
cites:
---

# Computing Hypergeometric Functions Rigorously

**Authors:** Fredrik Johansson  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1606.06977

## One-line
An efficient implementation of $_0F_1, _1F_1, _2F_1, _2F_0$ (and the Kummer $U$-function) in arbitrary-precision interval arithmetic with rigorous error bounds for unrestricted complex parameters and argument, shipped in the C library Arb.

## Key claim
Hypergeometric functions — and by extension Bessel, Airy, Legendre, incomplete gamma/beta, error/Fresnel, elliptic integrals, Jacobi polynomials — can be evaluated with provably correct rounding at arbitrary precision, often orders of magnitude faster than Mathematica/Maple; e.g. 1F1 with $N=10^4$ parameter computed in 82 s vs. >$10^5$ s in Mathematica, and 19 208 complex Bessel evaluations completed with certified 113-bit correct rounding while Mathematica returns 687–3826 wrong results.

## Method
Direct series expansion at $z=0$ with rigorous geometric-series tail bound (Theorem 1: $|\sum_{k\ge N} T(k)| \le C|T(N)|$ where $C=1/(1-D)$ if $D<1$); midpoint-radius ("ball") interval arithmetic propagates errors automatically. For evaluation away from $z=0$, explicit connection formulas reduce to $_pF_q$ with $p\le 2, q\le 1$; the asymptotic $_2F_0$ near $z=0$ uses Borel-regularization with literature error bounds. Summation uses three complexity-reducing algorithms picked by precision: binary splitting ($O(N)$ bit ops), rectangular splitting ($O(\sqrt{N})$ mults when $z$ is long), and FFT-based fast multipoint evaluation. Parameter derivatives are handled via truncated power-series arithmetic in $\mathbb{C}[[x]]/\langle x^n\rangle$ (automatic differentiation), and limits of removable singularities are resolved by formal power-series cancellation.

## Result
Rigorous arbitrary-precision evaluation across the full complex domain for all the standard $_pF_q$ with $p\le 2, q\le 1$. Concrete performance: Jν(z) Bessel evaluations are competitive with MPFR (≈2-3× slower) at low precision while providing correct rounding; Airy zero-finding on $[-1000,0]$ isolates 6710 zeros in 0.42 s and refines to 1000 digits in 23 s (vs Mathematica's 264 s); $\partial_\nu^{10000} J_\nu(z)|_{\nu=1,z=\pi}$ to 100 digits in 1400 s where Maple times out > 1 hour at $n=100$. Theorem 1 gives the explicit tail constant in terms of $D=|z|\prod(1+|a_i-b_i|/|b_i+N|)\prod 1/|b_i+N|$.

## Why it matters here
General background for the agent's mpmath-polish stack and triple-verify discipline — Arb's interval/ball arithmetic is the formal-correctness backbone for the float-precision-critical problems (P5, P6, P11, P14, P17). Directly informs the [[triple-verify]] check #2 (exact reimplementation via Arb-style ball arithmetic) and any wiki content on rigorous evaluation of special functions appearing in autocorrelation, uncertainty (Hilbert), or modular-form (Ramanujan) problems.

## Open questions / connections
- Rigorous error bounds for asymptotic expansions of higher $_pF_q$ ($p > q+1$) not covered by the $U$-function — open at time of writing.
- Polynomial-in-$\log|a|$ evaluation for exponentially large parameters $|a| \gg 10^4$ remains unaddressed (currently linear in $|a|$).
- Tight bounds on wide input intervals (e.g. $[\pi, 2\pi]$) — subdivision blows up exponentially; only ad-hoc monotonicity tricks available.
- Connects to Mezzarobba's NumGfun / D-finite framework [44,45,46] as the more general but heavier alternative.
- Bogolubsky–Skorokhodov [7] and Skorokhodov [56] cover the singular $z=1$ regime via Hurwitz zeta — complementary to this work's $|z|<1$ direct expansion.

## Key terms
hypergeometric function, Arb library, ball arithmetic, interval arithmetic, arbitrary precision, rigorous error bounds, binary splitting, rectangular splitting, Bessel function, Airy function, Kummer U-function, Borel summation, D-finite holonomic, parameter derivatives, Johansson
