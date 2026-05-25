---
type: source
kind: paper
title: Tail bounds for sums of geometric and exponential variables
authors: S. Janson
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.08157
source_local: ../raw/2017-janson-tail-bounds-sums-geometric.pdf
topic: general-knowledge
cites:
---

# Tail bounds for sums of geometric and exponential variables

**Authors:** S. Janson  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.08157

## One-line
Explicit Chernoff-style upper and lower tail bounds for sums of independent geometric (or exponential) random variables with possibly different parameters, governed by the smallest rate $p_* = \min_i p_i$.

## Key claim
For $X = \sum_{i=1}^n X_i$ with $X_i \sim \mathrm{Ge}(p_i)$, $\mu = EX = \sum 1/p_i$, and any $\lambda \geq 1$: $P(X \geq \lambda\mu) \leq \lambda^{-1}(1-p_*)^{(\lambda-1-\ln\lambda)\mu}$ (Theorem 2.3), strengthening the simpler $P(X \geq \lambda\mu) \leq e^{-p_*\mu(\lambda-1-\ln\lambda)}$ (Theorem 2.1); a matching lower bound $P(X \geq \lambda\mu) \geq \frac{(1-p_*)^{1+1/p_*}}{2p_*\mu}(1-p_*)^{(\lambda-1)\mu}$ shows the exponent is tight up to constants.

## Method
Classical Chernoff / moment-generating-function method: bound $Ee^{tX_i} = p_i/(e^{-t}-1+p_i)$, optimize $t$ in $P(X \geq x) \leq e^{-tx} Ee^{tX}$. Sharpening uses convexity of $-\ln(1-x)$ to replace each $p_i$ by $p_*$, plus a tail-integration lemma $P(X \geq x) \leq \frac{1-z(1-p_*)}{p_*} z^{-x} Ee^{tX}$ exploiting the geometric tail. Exponential case (Theorem 5.1) follows by taking $X_i^{(N)} \sim \mathrm{Ge}(a_i/N)$ and letting $N \to \infty$.

## Result
Upper tail: $P(X \geq \lambda\mu) \leq \lambda^{-1}(1-p_*)^{(\lambda-1-\ln\lambda)\mu}$ and the cleaner $P(X \geq \lambda\mu) \leq e^{1-\lambda}$ (independent of the $p_i$). Lower tail: $P(X \leq \lambda\mu) \leq e^{-p_*\mu(\lambda-1-\ln\lambda)}$ for $\lambda \leq 1$. Exponential analogues: $P(X \geq \lambda\mu) \leq \lambda^{-1} e^{-a_*\mu(\lambda-1-\ln\lambda)}$ with matching lower bound $\geq \frac{1}{2ea_*\mu} e^{-a_*\mu(\lambda-1)}$. Exponents are linear in $\lambda$ for large $\lambda$ and quadratic $\sim \tfrac12(\lambda-1)^2$ near $\lambda=1$, though looser than CLT by a factor $\approx p_*\mu \sum p_i^{-2}/\sum p_i^{-1}$.

## Why it matters here
General background; no direct arena tie. Potentially useful as a concentration tool for sieve-theory or combinatorial problems where waiting-time / geometric-sum statistics arise (e.g., randomized rounding, coupon-collector-style bounds in extremal graph constructions).

## Open questions / connections
- Sharpening the gap to CLT-optimal exponents for moderate-deviation regime $\lambda = 1+\varepsilon$ — current bounds are loose by factor $p_*\mu \cdot \mu/\sigma^2$.
- Extending to negative-binomial sums or dependent geometric variables (e.g., Markov-chain hitting times).
- Lower-tail lower bound (only upper bound given in §3) — Theorem 4.1 only handles the upper tail.

## Key terms
Chernoff bound, geometric distribution, exponential distribution, tail probability, moment generating function, large deviations, concentration inequality, Markov inequality, sum of independent variables, Janson inequality, waiting time, rate parameter
