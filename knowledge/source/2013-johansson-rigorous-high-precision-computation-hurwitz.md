---
type: source
kind: paper
title: Rigorous high-precision computation of the Hurwitz zeta function and its derivatives
authors: Fredrik Johansson
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1309.2877v1
source_local: ../raw/2013-johansson-rigorous-high-precision-computation-hurwitz.pdf
topic: general-knowledge
cites: 
---

# Rigorous high-precision computation of the Hurwitz zeta function and its derivatives

**Authors:** Fredrik Johansson  ·  **Year:** 2013  ·  **Source:** http://arxiv.org/abs/1309.2877v1

## One-line
An Euler–Maclaurin algorithm with rigorous, computable error bounds that evaluates the Hurwitz zeta function $\zeta(s,a)$ and arbitrarily many of its $s$-derivatives to arbitrary precision, implemented in the open-source Arb library.

## Key claim
For any $s,a \in \mathbb{C}$ with $\Re(a)+N>1$ and $\Re(s)+2M>1$, the remainder of Euler–Maclaurin applied to $\zeta(s+x,a) \in \mathbb{C}[[x]]$ is bounded coefficient-wise by $|R(s+x)| \le \frac{4|(s+x)_{2M}|}{(2\pi)^{2M}} \sum_k R_k x^k$ with $R_k \le (K/k!)\,J_k(N+\alpha,\sigma+2M,C)$ (Theorem 1), where $J_k$ is a closed-form integral computable by an $O(n)$ recurrence and $K,C$ are explicit constants in $s,a,N$.

## Method
Apply Euler–Maclaurin with $f(k)=(a+k)^{-s}$ lifted to formal power series in $x$ (so $s\to s+x$ encodes all derivatives). The remainder integral is majorized via the classical bound $|\tilde B_{2M}(t)|<4(2M)!/(2\pi)^{2M}$ and an explicit majorant on $|\log(a+t)|$. Implementation uses ball arithmetic, FFT-based polynomial multiplication, binary splitting for the tail, a sieved Horner scheme exploiting complete multiplicativity of $k^{-(s+x)}$ when $a=1$, and the Borel/binomial-transform identity $T[f]=B^{-1}[e^x B[f(-x)]]$ for the right-composition $x/(x-1)$ used to extract Keiper–Li coefficients.

## Result
Sets several records: first nontrivial zero $\rho_1$ of $\zeta$ to 303 000 digits (~$10^6$ bits); Keiper–Li coefficients $\lambda_n$ for all $n\le 100\,000$ (e.g. $\lambda_{100000}\approx 4.62580782406902231409416038\ldots$), confirming Keiper's conjecture and matching Li's criterion empirically; all Stieltjes constants $\gamma_n$ for $n\le 100\,000$, yielding $\gamma_{100000}=1.991927306312541095658\ldots\times 10^{83432}$ and confirming that $n=137$ is the unique sign discrepancy of the Knessl–Coffey asymptotic for $n\le 10^5$. Benchmarks show ~$10\times$–$100\times$ speedups over mpmath/Mathematica at 10 000 digits.

## Why it matters here
General background; no direct arena tie. Useful infrastructure note: when an Einstein Arena problem requires high-precision special-function evaluation with rigorous error control (e.g. mpmath polish on autocorrelation/uncertainty problems P5/P14/P17), the Arb library and ball-arithmetic + Euler–Maclaurin methodology described here are the state-of-the-art reference.

## Open questions / connections
- Tighter error bounds for large $|a|$ and optimal joint selection of $N,M$ when the derivative order $D$ is large.
- Parallelization of the tail sum and memory-efficient evaluation of a single high-order derivative.
- Stability fix for binary-splitting composition of power series (currently numerically unstable, despite $O(M(n)\log n)$ cost).
- Comparison with Borwein, Vepštas, and Coffey algorithms for $\zeta(s,a)$.

## Key terms
Hurwitz zeta function, Riemann zeta function, Euler–Maclaurin formula, Bernoulli numbers, ball arithmetic, rigorous error bounds, power series arithmetic, binary splitting, Keiper–Li coefficients, Stieltjes constants, Riemann hypothesis, Li's criterion, Arb library, arbitrary precision, Fredrik Johansson
