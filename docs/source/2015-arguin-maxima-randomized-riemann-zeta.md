---
type: source
kind: paper
title: Maxima of a randomized Riemann zeta function, and branching random walks
authors: L. Arguin, David Belius, Adam J. Harper
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1506.00629
source_local: ../raw/2015-arguin-maxima-randomized-riemann-zeta.pdf
topic: general-knowledge
cites:
---

# Maxima of a randomized Riemann zeta function, and branching random walks

**Authors:** L. Arguin, David Belius, Adam J. Harper  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1506.00629

## One-line
Proves the first two terms of the Fyodorov–Hiary–Keating conjecture for a randomized Euler-product model of $\zeta(1/2+it)$ by exposing an approximate branching-random-walk structure.

## Method
Replace primes $p^{-i\tau}$ with i.i.d. uniform unit-circle variables $U_p$ and study $X_n(h)=\sum_{p\le e^{2^n}} \mathrm{Re}(U_p p^{-ih})/\sqrt p$. Decompose into scale increments $Y_k(h)=\sum_{2^{k-1}<\log p\le 2^k}\mathrm{Re}(U_p p^{-ih})/\sqrt p$ with covariance $\approx (\log 2)/2$ inside the "branching point" $h\wedge h'=\log_2|h-h'|^{-1}$ and decaying after, mimicking a depth-$n$ binary tree. Apply Kistler's multiscale second-moment method: barrier-restricted exceedance counts $\tilde Z(m)$, Berry–Esseen Gaussian comparisons of tilted measures $Q_\lambda$, a ballot-theorem bridge estimate giving the $n^{-1}$ cost factor that produces the $-\tfrac34$ subleading coefficient.

## Key claim / Result
For $U_p$ i.i.d. uniform on the unit circle,
$$\max_{h\in[0,1]} \sum_{p\le T} \frac{\mathrm{Re}(U_p p^{-ih})}{p^{1/2}} = \log\log T - \tfrac{3}{4}\log\log\log T + o_P(\log\log\log T).$$
Distinguishes the "independent" heuristic answer $-\tfrac14\log\log\log T$ from the true tree-induced $-\tfrac34\log\log\log T$; the extra $-\tfrac12\log\log\log T$ is the ballot-theorem cost of staying under the linear barrier $k\mapsto k\log 2+B$.

## Why it matters here
General background; no direct arena tie. Informs log-correlated extremes / branching-random-walk maxima technology — relevant to any arena problem where logarithmic correlations produce a $\log\log T - \tfrac{3}{4}\log\log\log T$ scaling (autocorrelation extremes, random multiplicative functions, possibly extremal-graph counts with hierarchical structure).

## Open questions / connections
- Transfer the proof (which only uses two-point joint control) to the actual $\zeta$ via Soundararajan/Harper's Euler-product approximation under RH.
- Extend to characteristic polynomial $P_N(e^{i\theta})$ of CUE/GUE — even leading order unproven there (cf. Fyodorov–Simm 2015, Webb 2014).
- Sharpen the $o_P(\log\log\log T)$ error to the conjectured $O_P(1)$ tightness; needs control beyond first/second moments.
- Relates to Bramson's BBM, Aïdékon's BRW convergence, 2D GFF maxima (Bramson–Ding–Zeitouni, Madaule), cover times (Belius–Kistler).

## Key terms
Riemann zeta function, Fyodorov–Hiary–Keating conjecture, branching random walk, log-correlated Gaussian field, Euler product, Selberg central limit theorem, multiscale second moment method, ballot theorem, Berry–Esseen, barrier random walk, Bramson, Kistler, Harper, Soundararajan, characteristic polynomial CUE, extreme value theory
