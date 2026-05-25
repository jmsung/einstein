---
type: source
kind: paper
title: "Moments of random multiplicative functions, II: High moments"
authors: Adam J. Harper
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.04114
source_local: ../raw/2018-harper-moments-random-multiplicative-functions.pdf
topic: general-knowledge
cites:
---

# Moments of random multiplicative functions, II: High moments

**Authors:** Adam J. Harper  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.04114

## One-line
Determines the order of magnitude (up to $e^{O(q^2)}$ factors) of the $2q$-th moments $\mathbb{E}|\sum_{n\leq x} f(n)|^{2q}$ for Steinhaus and Rademacher random multiplicative functions, uniformly for all real $1 \leq q \leq c\log x/\log\log x$.

## Key claim
Steinhaus case: $\mathbb{E}|\sum_{n\leq x} f(n)|^{2q} = e^{-q^2\log q - q^2\log\log(2q) + O(q^2)} x^q (\log x)^{(q-1)^2}$. Rademacher case: same form but with exponent $\max\{(q-1)^2, q(2q-3)\}$ on $\log x$, plus an unexpected $(1+\min\{\log\log x, 1/|q-q_0|\})$ factor where $q_0 = (1+\sqrt 5)/2$ is the golden ratio — a transition from "unitary" to "orthogonal" behavior.

## Method
Reduces $\mathbb{E}|\sum_{n\leq x} f(n)|^{2q}$ to the $q$-th moment of an Euler-product integral $\mathbb{E}[\frac{1}{\log x}\int_{-1/2}^{1/2} |F(1/2+q/\log x + it)|^2 dt]^q$ via conditioning on small-prime behavior, Khintchine-style moment inequalities, and Parseval. Bounds on high conditional moments come from hypercontractive (Bonami) inequalities. The hardest regime ($q$ just above $1$) is handled with Doob's $L^p$ martingale maximal inequality to simultaneously maximize over many Euler-product splittings. Rankin's shift by $q/\log x$ tracks throughout.

## Result
Proves Theorem 1 (Steinhaus) and Theorem 2 (Rademacher) as above, uniformly for real $q \in [1, c\log x/\log\log x]$. Corollary 1: large-deviation tail $\mathbb{P}(|\sum_{n\leq x} f(n)| \geq \lambda\sqrt x) \ll \lambda^{-2} e^{-(\log^2\lambda)/\log\log x}$ for $2 \leq \lambda \leq \sqrt{\log x}$, obtained by optimizing $q$ in the moment bound. Together with the low-moments companion paper, this fairly completely describes the tail of $\sum_{n\leq x} f(n)$ up to $(\log\log x)^{O(1)}$ factors.

## Why it matters here
General background; no direct arena tie. Relevant as deep technique for moment-of-random-multiplicative-function problems and for the Euler-product / hypercontractivity / martingale-maximal toolkit, which could inform autocorrelation-inequality or sieve-theory questions if a random-multiplicative model arises; not directly tied to current Einstein Arena problems.

## Open questions / connections
- Sharp asymptotics (not just order-of-magnitude up to $e^{O(q^2)}$) for non-integer $q$ remain open.
- Behavior for $q \geq c\log x/\log\log x$ only partially understood (Granville–Soundararajan §6 + footnote estimates here).
- The min$\{\log\log x, 1/|q-q_0|\}$ factor at the Rademacher golden-ratio transition lacks a conceptual (non-proof-inspection) explanation.
- Connection to critical multiplicative chaos at $q > 1$ not previously investigated.
- Potential alternative Perron-integral route via Hölder with $d=3$ extracted brackets may extend Munsch's theta-function moment bounds to non-integer $k \geq 5$.

## Key terms
random multiplicative functions, Steinhaus, Rademacher, high moments, Euler product, hypercontractive inequality, Bonami inequality, Doob martingale maximal inequality, Rankin's trick, Dirichlet series, critical multiplicative chaos, unitary-orthogonal transition, golden ratio, large deviations, Helson conjecture, theta functions, L-function moments, Harper
