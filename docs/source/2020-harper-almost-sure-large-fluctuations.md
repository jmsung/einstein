---
type: source
kind: paper
title: Almost sure large fluctuations of random multiplicative functions
authors: Adam J. Harper
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2012.15809
source_local: ../raw/2020-harper-almost-sure-large-fluctuations.pdf
topic: general-knowledge
cites:
---

# Almost sure large fluctuations of random multiplicative functions

**Authors:** Adam J. Harper  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2012.15809

## One-line
Proves that partial sums of a Steinhaus or Rademacher random multiplicative function $f(n)$ almost surely fluctuate above $\sqrt{x}(\log\log x)^{1/4+o(1)}$ infinitely often, breaking the $\sqrt{x}$ barrier.

## Key claim
For any $V(x)\to\infty$, almost surely there exist arbitrarily large $x$ with $|\sum_{n\le x} f(n)| \ge \sqrt{x}(\log\log x)^{1/4}/V(x)$ — the first super-$\sqrt{x}$ almost-sure lower bound, answering a question of Halász and proving Erdős's conjecture (in its $\sqrt{x}$-or-larger form). The exponent $1/4$ is conjectured sharp.

## Method
Conditional multivariate Gaussian approximation: condition on $(f(p))_{p\le X}$, split $\sum_{n\le x} f(n)$ using multiplicativity into a smooth-part plus an outer sum over large primes $X<p\le x$, and apply a Stein-type multivariate normal approximation to the outer sum at a logarithmic grid of sample points $x = X^{8/7} e^{2\pi r}$. The crux is bounding conditional covariances via Dirichlet polynomial mean values, high mixed moments of shifted random Euler products, and barrier/ballot-type random walk arguments — all in the critical multiplicative chaos regime tied to $\int_{-1/2}^{1/2} |F(1/2+it)|^2 dt$.

## Result
Theorem 2 (localised, quantitative): uniformly for large $X$ and $1\le W \le (\log\log\log X)/30$, $\max_{X^{8/7}\le x\le X^{4/3}} \frac{1}{\sqrt{x}}|\sum_{n\le x} f(n)| \ge (\log\log X)^{1/4}/e^{1.2W}$ with probability $\ge 1 - O(e^{-0.1W})$. Theorem 1 follows by first Borel–Cantelli along a sparse sequence of $X$. Combined with prior upper bound $O(\sqrt{x}(\log\log x)^{2+\epsilon})$ (Lau–Tenenbaum–Wu), the true growth rate is now pinned to $\sqrt{x}(\log\log x)^c$ with $1/4 \le c \le 2+\epsilon$.

## Why it matters here
General background; no direct arena tie. Random multiplicative functions are a probabilistic-number-theory topic distant from the arena's sphere-packing / autocorrelation / discrete-geometry problems — relevant only as a methodological reference for Gaussian comparison + barrier/ballot random-walk techniques in critical multiplicative chaos.

## Open questions / connections
- Is $\sqrt{x}(\log\log x)^{1/4+o(1)}$ actually sharp? Closing the gap with the LTW upper bound requires controlling the $X$-smooth contribution, not just the large-prime tail.
- Deterministic analogue for character sums: does $\max_{X^{8/7}\le x\le X^{4/3}} |\sum_{n\le x}\chi(n)|/\sqrt{x}$ exhibit the same $(\log\log X)^{1/4}$ behaviour for 99% of Dirichlet characters $\chi \bmod r$ when $X\le r^{3/4}$?
- Relation to Gonek's conjecture $\sqrt{x}(\log\log\log x)^{5/4}$ for the Möbius function — Rademacher model behaviour vs. true $\mu$.

## Key terms
random multiplicative function, Steinhaus, Rademacher, law of the iterated logarithm, critical multiplicative chaos, Euler product, Dirichlet polynomial, Gaussian comparison, ballot theorem, barrier argument, Halász, Erdős conjecture, Möbius function
