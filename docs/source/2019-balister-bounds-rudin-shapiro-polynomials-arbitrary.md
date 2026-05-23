---
type: source
kind: paper
title: Bounds on Rudin-Shapiro polynomials of arbitrary degree
authors: P. Balister
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.08777
source_local: ../raw/2019-balister-bounds-rudin-shapiro-polynomials-arbitrary.pdf
topic: general-knowledge
cites:
---

# Bounds on Rudin-Shapiro polynomials of arbitrary degree

**Authors:** P. Balister  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.08777

## One-line
Proves the longstanding $\sqrt{6n}$ sup-norm conjecture for Rudin–Shapiro polynomials of arbitrary degree and refutes Montgomery's $3\sqrt{n-m}$ conjecture for partial sums.

## Key claim
$|P_{<n}(z)| \le \sqrt{6n-2} - 1$ for all $n\ge 1$ and $|z|=1$ (sharp at $n=(2\cdot 4^k+1)/3$, $z=1$); and $|P_{[m,n)}(z)| \le \sqrt{10(n-m)}$, asymptotically sharp with constant $\sqrt{10} > 3$, contradicting Montgomery's conjecture.

## Method
Introduces the auxiliary norm $\|P\|_L = \sup_{|z|=1}\sqrt{|P(z)|^2 + |P(-z)|^2}$, which scales cleanly under the Rudin–Shapiro recursion ($\|P_{[2m,2n)}\|_L^2 = 2\|P_{[m,n)}\|_L^2$) via the parallelogram identity. Extends $f(n)=\|P_{<n}\|_L^2$ by dyadic self-similarity to a continuous function on $[0,\infty)$ and proves piecewise bounds by induction plus computer-assisted verification on a finite cover of dyadic intervals (FFT on $2^{24}$-th roots of unity). For the partial-sum bound, a refined two-variable function $g(r,s)$ tracks phase coherence between $P_{<r}(-z^{-1})$ and $P_{<s}(z)$ blocks near the critical point $(4/3, 8/3)$, with recursive dyadic-square verification. Equation (2) (sharpness of constant 10) follows from Rodgers' SU(2) equidistribution result strengthened to non-uniform measures with $E(w^n)=0$ when $2^k\mid n$.

## Result
Sup-norm constant for Rudin–Shapiro $P_{<n}$ is exactly $\sqrt{6}\approx 2.449$, improving Shapiro's $2+\sqrt{2}$ and Saffari's $(2+\sqrt{2})\sqrt{3/5}$. For consecutive-block sums $P_{[m,n)}$, the tight constant is $\sqrt{10}\approx 3.162$, achieved asymptotically at $m_k=(5\cdot 4^k+1)/3$, $n_k=(8\cdot 4^k+1)/3$; the maximizing $z$ is *not* $z=1$ for large $k$ (the value at $z=e^{3\pi i/4}$ already gives $\sqrt{5+\sqrt{72}}\approx 3.155 > 3$).

## Why it matters here
Direct background for autocorrelation / flat-polynomial problems in the arena: Rudin–Shapiro is the canonical $\pm 1$ low-sup-norm Littlewood polynomial family, and the $\|\cdot\|_L$ dyadic-scaling trick is a transferable proof technique for any extremal $\pm 1$ sequence with a doubling recursion. General background for autocorrelation-class problems; no direct single-problem tie.

## Open questions / connections
- Exact maximizing $z_k$ for $|P_{[m_k,n_k)}(z)|$ is erratic in $k$ — no explicit sequence known achieving the $\sqrt{10}$ limit.
- The $\|\cdot\|_L$-norm + dyadic continuous extension framework may generalize to other recursive $\pm 1$ constructions (Golay, Shapiro-like).
- Extends Rodgers (2017) SU(2)/Haar equidistribution to non-uniform $w$-distributions with vanishing Fourier mass on multiples of $2^k$.

## Key terms
Rudin-Shapiro polynomials, Littlewood polynomials, sup-norm bounds, $\pm 1$ sequences, Shapiro sequence, Golay sequence, parallelogram identity, dyadic self-similarity, Montgomery conjecture, autocorrelation, SU(2) equidistribution, Haar measure, flat polynomials, Saffari, Rodgers, computer-assisted proof
