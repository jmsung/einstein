---
type: source
kind: paper
title: The Fyodorov-Hiary-Keating Conjecture. I
authors: L. Arguin, P. Bourgade, Maksym Radziwill
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.00988
source_local: ../raw/2020-arguin-fyodorov-hiary-keating-conjecture.pdf
topic: general-knowledge
cites:
---

# The Fyodorov-Hiary-Keating Conjecture. I

**Authors:** L. Arguin, P. Bourgade, Maksym Radziwill  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.00988

## One-line
Proves the sharp upper-tail bound predicted by Fyodorov–Hiary–Keating for the maximum of $|\zeta(\tfrac12+it)|$ in a typical unit interval on the critical line.

## Key claim
For $T\ge 3$, $y\ge 1$, the Lebesgue measure of $t\in[T,2T]$ with $\max_{|h|\le 1}|\zeta(\tfrac12+it+ih)| > e^y \frac{\log T}{(\log\log T)^{3/4}}$ is $\le C\, y\, e^{-2y}\, T$ uniformly, with the $(\log\log T)^{3/4}$ exponent and the $ye^{-2y}$ decay both sharp (expected optimal for $y=O(\sqrt{\log\log T})$).

## Method
Multiscale iteration on dyadic prime-scale Dirichlet partial sums $S_k(h)=\sum_{e^{1000}\le \log p\le e^k}\mathrm{Re}\,p^{-1/2-i\tau-ih}$, treated as an approximate branching random walk in $k\le n=\log\log T$. Recursively constructs upper barriers $U_y(k)=y+O(\log k)$ AND lower barriers $L_y(k)=y-20k$ on partial sums, the lower barrier shrinking the high-point set so subsequent scales need only modest moment bounds. Each induction step uses sharp second moments and twisted fourth moments of $\zeta$ together with random mollifiers $\prod_\ell M_\ell$ approximating $e^{-S_k}$, plus a curved-barrier ballot theorem (Berry–Esseen + [Webb '11] extension).

## Result
Theorem 1: $\mathrm{meas}\{t\in[T,2T]:\max_{|h|\le 1}|\zeta(\tfrac12+it+ih)|>e^y\frac{\log T}{(\log\log T)^{3/4}}\}\le C y e^{-2y} T$, sharper than the corresponding random-matrix CUE/CβE result of Chhaibi–Madaule–Najnudel (which only gives tightness, no decay rate). Improves Harper '19's second-order upper bound $\log\log T-\tfrac34\log\log\log T+\log\log\log\log T$ to a uniform tail. Conjectured sharp range $y=O(\sqrt{\log\log T})$; for $y\in[1,\log\log T]$ extra Gaussian factor $\exp(-y^2/\log\log T)$ expected.

## Why it matters here
General background; no direct arena tie. Closest relevance: log-correlated extremes / branching-random-walk extreme-value technology (barrier + ballot theorem + multiscale moments), which is methodologically related to autocorrelation-inequality and uncertainty-principle problems where partial-Dirichlet decompositions and barrier estimates arise.

## Open questions / connections
- Matching lower bound (announced as Part II by same authors) — would settle the FHK conjecture's tail asymptotic up to the constant.
- Whether the same multiscale + twisted moment scheme transfers back to CUE/CβE characteristic polynomials to give decay rates (currently only tightness known [Chhaibi–Madaule–Najnudel '18]).
- Extension to the conjectured Gaussian correction $\exp(-y^2/\log\log T)$ in the regime $y\in[\sqrt{\log\log T},\log\log T]$.
- Generalizes Bramson '78 barrier method from BRW / 2D GFF [Bramson–Ding–Zeitouni '16, Ding–Zeitouni '14] to a number-theoretic process.

## Key terms
Riemann zeta function, Fyodorov-Hiary-Keating conjecture, log-correlated maximum, branching random walk, barrier method, ballot theorem, multiscale iteration, twisted fourth moment, Dirichlet polynomial mollifier, characteristic polynomial CUE, freezing transition, Bramson, Berry-Esseen
