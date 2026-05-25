---
type: source
kind: paper
title: On the extreme values of the Riemann zeta function on random intervals of the critical line
authors: J. Najnudel
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.05562
source_local: ../raw/2016-najnudel-extreme-values-riemann-zeta.pdf
topic: general-knowledge
cites:
---

# On the extreme values of the Riemann zeta function on random intervals of the critical line

**Authors:** J. Najnudel  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.05562

## One-line
Proves (under RH) that the supremum of $\log\zeta(1/2+it)$ on a random length-$2h$ interval $[UT-h, UT+h]$ is $(1+o(1))\log\log T$ with probability $\to 1$, the leading-order term of the Fyodorov–Hiary–Keating conjecture.

## Key claim
Under RH, for fixed $h,\epsilon>0$ and $U$ uniform on $[0,1]$: $\sup_{t\in[UT-h,UT+h]} \Re\log\zeta(1/2+it) \in [(1-\epsilon)\log\log T,\,(1+\epsilon)\log\log T]$ with probability $\to 1$ as $T\to\infty$; analogous statement for $\Im\log\zeta$ and its infimum. **Unconditional** upper bound (Theorem 1.3): $\sup \Re\log\zeta(1/2+it) \le \log\log T + g(T)$ for any $g\to\infty$.

## Method
Upper bound via Riemann–Siegel formula + a sampling lemma: a band-limited function on $\mathbb{R}$ is recovered (Shannon-style, via a Schwartz kernel $\varphi$ from Poisson summation) from samples at spacing $\pi/2\lambda$, so $\sup|\zeta|$ on $[UT-h, UT+h]$ is controlled by $O_h(\log T)$ sample points plus a classical second-moment estimate. Lower bound: average $\log\zeta$ to approximate it by a Dirichlet polynomial over primes, cut into $K$ scale-shells $(e^{e^{m\log H/K}}, e^{e^{(m+1)\log H/K}}]$ to manufacture an approximate branching/tree structure, apply Gaussian comparison to the prime sums, then the **second-moment / Paley–Zygmund method** as in Bolthausen–Deuschel–Giacomin and Arguin–Belius–Bourgade for log-correlated fields.

## Result
Leading-order term $\log\log T$ in FHK conjecture (1.1) is correct on a random short interval. Matches accuracy of Arguin–Belius–Bourgade [3] for the CUE characteristic polynomial. The method does **not** recover the conjectured $-\frac{3}{4}\log\log\log T$ subleading term: averaging scale $H \le \log T/\log\log T$ forces a $\log\log\log T$ loss. Corollary: for $\Delta(t) = N(t) - \frac{t\log t}{2\pi} + \frac{t(1+\log 2\pi)}{2\pi}$, $\sup \Delta \in [(1-\epsilon)/\pi,\,(1+\epsilon)/\pi]\log\log T$ w.h.p.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the second-moment / Paley–Zygmund machinery for extrema of log-correlated fields (branching structure via dyadic/multi-scale shells) is a transferable template for any extremal problem where covariances decay logarithmically — but none of the 23 Einstein Arena problems currently live in this regime.

## Open questions / connections
- Remove RH for the $\Im\log\zeta$ case (Arguin–Belius–Bourgade–Radziwiłł–Soundararajan [4] did so for $\Re$ only).
- Push to second-order term $-A\log\log\log T$ with $A>3/4$; matching $-3/4$ (Paquette–Zeitouni for CUE) appears blocked by the $\log T/\log\log T$ averaging-scale cap.
- Extension to Dirichlet $L$-functions; behaviour when interval length $h=h(T)$ scales with $T$.

## Key terms
Riemann zeta function, extreme values, critical line, Fyodorov–Hiary–Keating conjecture, log-correlated Gaussian field, branching random walk, second moment method, Paley–Zygmund, Riemann–Siegel formula, CUE characteristic polynomial, Selberg central limit theorem, Poisson summation sampling
