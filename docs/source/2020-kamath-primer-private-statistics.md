---
type: source
kind: paper
title: A Primer on Private Statistics
authors: Gautam Kamath, Jonathan Ullman
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.00010
source_local: ../raw/2020-kamath-primer-private-statistics.pdf
topic: general-knowledge
cites:
---

# A Primer on Private Statistics

**Authors:** Gautam Kamath, Jonathan Ullman  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.00010

## One-line
Survey/primer translating differential-privacy results from the CS literature into statistical language, with worked examples for private mean estimation and CDF estimation.

## Key claim
For mean estimation of bounded product distributions on $[\pm 1]^d$ under $(\varepsilon, 1/n)$-differential privacy, the minimax $\ell_2^2$ rate is $\Theta(d/n + d^2/(\varepsilon^2 n^2))$; for CDF estimation over $\{1,\ldots,D\}$ under $(\varepsilon,\delta)$-DP, an $\ell_\infty$ rate of $O(1/\sqrt{n} + \log^{3/2}(D)\log^{1/2}(1/\delta)/(\varepsilon n))$ is achievable.

## Method
Upper bounds: Gaussian mechanism applied to the empirical mean, and the binary-tree / hierarchical-decomposition mechanism that releases noisy counts on $O(\log D)$ dyadic interval scales (sensitivity $\sqrt{2\log D}/n$), recombined via a postprocessing matrix $A$ with row-sparsity $\log D$. Lower bound: tracing / fingerprinting attacks — construct a hard prior $\mu \sim \mathrm{Unif}([-1,1]^d)$, build a test statistic $Z_i = \langle M(X)-\mu, X_i-\mu\rangle$, then use the Fingerprinting Lemma (DP forces $\sum E[Z_i]$ small while accuracy forces it $\geq d/3 - \alpha^2$).

## Result
Mean-estimation upper bound $\leq d/n + 2d^2\log(2/\delta)/(\varepsilon^2 n^2)$ (Theorem 3.2); matching lower bound $\Omega(\min\{d^2/(\varepsilon^2 n^2), d\})$ for $\delta < 1/(96n)$ (Theorem 3.3). CDF upper bound $O(1/\sqrt n + \log^{3/2}(D)\log^{1/2}(1/\delta)/(\varepsilon n))$ (Theorem 4.1); lower bound $\Omega(\min\{\log^* D/n, 1/\sqrt n\})$ shows finite support is required (Theorem 4.2 of BNSV15) — no DP CDF estimator works uniformly over distributions with infinite support.

## Why it matters here
General background; no direct arena tie. The Fingerprinting Lemma and dyadic / binary-tree mechanism are reusable proof tools (correlation-vs-error lower bounds, hierarchical decomposition of a function on an ordered domain into $O(\log D)$ pieces) that could conceivably surface in autocorrelation or sieve-style decomposition arguments, but no Arena problem here is privacy-flavored.

## Open questions / connections
- Tight $\delta$-dependence in the mean-estimation lower bound (current proof loose; see SU17a, CWZ19 for refinement).
- Formal connections between robust statistics (median, IQR via propose-test-release) and DP remain "relatively scant" — suggested as a productive research area.
- Node-DP graph statistics: empirical vs population formulations diverge more than for vector statistics due to high worst-case sensitivity; graphon estimation (BCSZ18, SU19) still has efficiency gaps.

## Key terms
differential privacy, Gaussian mechanism, fingerprinting lemma, tracing attack, membership inference, minimax lower bound, binary-tree mechanism, dyadic decomposition, CDF estimation, Kolmogorov distance, mean estimation, post-processing, Dvoretzky-Kiefer-Wolfowitz
