---
type: source
kind: paper
title: Maximum of the Riemann Zeta Function on a Short Interval of the Critical Line
authors: L. Arguin, David Belius, P. Bourgade, Maksym Radziwill, K. Soundararajan
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.08575
source_local: ../raw/2016-arguin-maximum-riemann-zeta-function.pdf
topic: general-knowledge
cites:
---

# Maximum of the Riemann Zeta Function on a Short Interval of the Critical Line

**Authors:** L. Arguin, David Belius, P. Bourgade, Maksym Radziwill, K. Soundararajan  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1612.08575

## One-line
Proves the leading-order Fyodorov–Hiary–Keating conjecture: for typical $t \in [T,2T]$, $\max_{|t-u|\le 1} \log|\zeta(\tfrac12+iu)| = (1+o(1))\log\log T$.

## Key claim
Unconditionally, as $T\to\infty$, the measure of $t\in[T,2T]$ with $(1-\varepsilon)\log\log T < \max_{|t-u|\le 1}\log|\zeta(\tfrac12+iu)| < (1+\varepsilon)\log\log T$ is $(1-o(1))T$ — confirming the leading-order prediction from log-correlated extreme value theory.

## Method
Upper bound: Sobolev-type inequality $\max|f|^2 \le \tfrac12(|f(\pm1)|^2) + \int |f'f|$ combined with classical second-moment estimates for $\zeta$ and $\zeta'$. Lower bound: (i) mollifier reduction — construct a Dirichlet polynomial $M(s)=\sum \mu(n)a(n)n^{-s}$ on $n\le X=\exp((\log T)^{1-1/K})$ so that $\zeta(\sigma_0+iu)M(\sigma_0+iu)\approx 1$ slightly right of the critical line, transferring the max problem to $\max \mathrm{Re}\sum_{p\le X} p^{-\sigma_0-iu}$; (ii) branching random walk / Kistler $K$-level coarse-graining of the prime sum into ranges $J_j=(\exp((\log T)^{j/K}),\exp((\log T)^{(j+1)/K})]$, with Cauchy–Schwarz / Paley–Zygmund second-moment lower bound on the event that all $P_j(t+k/\log T) \ge (\lambda/K)\log\log T$.

## Result
Theorem 1.1: $\mathbb{P}\big((1-\varepsilon)\log\log T < \max_{|t-u|\le 1}\log|\zeta(\tfrac12+iu)| < (1+\varepsilon)\log\log T\big) \to 1$. Proposition 2.1 strengthens the upper bound: for any $V(T)\to\infty$, $\max_{|t-u|\le 1}|\zeta(\tfrac12+iu)| \le V\log T$ with probability $1-O(1/V^2)$. The sharper FHK prediction includes a $-\tfrac34\log\log\log T$ correction term that this paper does not resolve.

## Why it matters here
General background; no direct arena tie. Demonstrates the log-correlated-field paradigm: a global maximum of a strongly correlated field over $\log T$ "effectively independent" sample points behaves like $\sigma\sqrt{2\log N}$ Gaussian extremes with branching-tree covariance structure. Relevant background for any arena problem where the objective is a maximum of correlated quantities at multiple scales.

## Open questions / connections
- Second-order $-\tfrac34\log\log\log T$ correction and the limiting distribution $X_T$ from the FHK conjecture remain open.
- Unconditional analogue for $\mathrm{Im}\log\zeta$ (Najnudel proved both under RH).
- Closing the gap between Littlewood's conditional upper bound $|\zeta(\tfrac12+it)|\ll\exp(C\log t/\log\log t)$ and Bondarenko–Seip's lower bound $\exp(c\sqrt{\log T\log\log\log T/\log\log T})$ for the global maximum on $[0,T]$.
- Extends the log-correlated extremes program (BBM, 2D GFF, CUE characteristic polynomial, Gaussian multiplicative chaos) to $\zeta$ itself.

## Key terms
Riemann zeta function, critical line, log-correlated field, branching random walk, Fyodorov–Hiary–Keating conjecture, Selberg central limit theorem, mollifier, Dirichlet polynomial, Kistler coarse-graining, Bramson method, second moment method, extreme value theory, Lindelöf hypothesis, Paley–Zygmund inequality
