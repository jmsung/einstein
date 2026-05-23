---
type: source
kind: paper
title: On the partition function of the Riemann zeta function, and the Fyodorov--Hiary--Keating conjecture
authors: Adam J. Harper
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1906.05783
source_local: ../raw/2019-harper-partition-function-riemann-zeta.pdf
topic: general-knowledge
cites:
---

# On the partition function of the Riemann zeta function, and the Fyodorov--Hiary--Keating conjecture

**Authors:** Adam J. Harper  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1906.05783

## One-line
Proves a sharp upper bound on the typical short-interval maximum of $|\zeta(1/2+it)|$ matching the first two terms of the Fyodorov--Hiary--Keating conjecture, via a smooth/rough Dirichlet-polynomial factorization linked to critical multiplicative chaos.

## Key claim
For $(1+o(1))T$ values of $t \in [T, 2T]$, $\max_{|h|\le 1/2} \log|\zeta(1/2+it+ih)| \le \log\log T - (3/4+o(1))\log\log\log T$, matching the FHK conjecture's leading and second-order terms (Theorem 2, Corollary 2). Also: the partition function $\int_{-1/2}^{1/2} |\zeta(1/2+it+ih)|^2\,dh$ is typically of size $\log T / \sqrt{\log\log T}$, not $\log T$ (Theorem 1, Corollary 1).

## Method
Approximate $\zeta(1/2+it)$ in mean square as a product of a Dirichlet polynomial over $P$-smooth integers (with $P = T^{1/(\log\log T)^8}$) and one over $P$-rough integers. Restrict to a high-probability "good event" $G_t$ where neither the smooth Euler product $\prod_{p\le P}(1-p^{-1/2-it-ih})^{-1}$ nor its partial products grow too large. Taylor-expand smooth cutoffs, apply mean-value theorem for Dirichlet polynomials, derandomize $p^{-it} \leftrightarrow$ Steinhaus random multiplicative function $f(p)$, then invoke critical multiplicative chaos estimates (from Harper's [10]) and a barrier/Gaussian-walk probability result. Cauchy's integral formula converts $\max_{|h|\le 1/2}$ into a small-rectangle contour integral; never shifts off the critical line by more than $1/\log T$.

## Result
Theorem 1: $\frac{1}{T}\int_T^{2T} \left(\int_{-1/2}^{1/2}|\zeta(1/2+it+ih)|^2 dh\right)^q dt \ll \left(\frac{\log T}{1+(1-q)\sqrt{\log\log T}}\right)^q$ uniformly in $0\le q\le 1$. Theorem 2: $\frac{1}{T}\text{meas}\{t\in[T,2T] : \max_{|h|\le 1/2}|\zeta(1/2+it+ih)| \ge \frac{e^U \log T}{(\log\log T)^{3/4}}\} \ll e^{-2U}(\log\log\log T + U)(\log\log\log T)^2$ for $0\le U\le \log\log T$. Rules out the "independence conjecture" maximum $\log\log T - (1/4)\log\log\log T$.

## Why it matters here
General background; no direct arena tie. Touches autocorrelation/uncertainty-style problems via critical multiplicative chaos and log-correlated extremes — a transferable lens for understanding extremal behavior of sums of "almost-independent" oscillating terms at criticality (denominator $\sqrt{\log\log T}$ as critical renormalization).

## Open questions / connections
- Tighten Theorem 2 to the conjectured $U e^{-2U}$ shape — current proof's third-order term $(3/2)\log\log\log\log T$ is extraneous, traced to a crude treatment of large primes (parameter $V$ forced too large).
- Distributional form of the FHK conjecture (full limiting law of the centered maximum) remains open for $\zeta$; analog is proven for random unitary matrices (Paquette--Zeitouni, Chhaibi--Madaule--Najnudel).
- Extends Arguin--Belius--Bourgade--Radziwiłł--Soundararajan [2] (which gave $(1-\epsilon)\log\log T$ lower bound) and Najnudel [14]; companion contemporaneous proof by Arguin--Bourgade--Radziwiłł--Soundararajan via different methods.

## Key terms
Riemann zeta function, Fyodorov--Hiary--Keating conjecture, critical multiplicative chaos, partition function, log-correlated fields, Steinhaus random multiplicative function, Euler product, Dirichlet polynomial, smooth/rough number decomposition, freezing transition, short-interval maximum, branching random walk, barrier estimate, Gaussian random walk, mean value theorem for Dirichlet polynomials, Harper, Najnudel, Arguin, Soundararajan
