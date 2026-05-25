---
type: source
kind: paper
title: Nonparametric graphon estimation
authors: P. Wolfe, S. Olhede
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.5936
source_local: ../raw/2013-wolfe-nonparametric-graphon-estimation.pdf
topic: general-knowledge
cites:
---

# Nonparametric graphon estimation

**Authors:** P. Wolfe, S. Olhede  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.5936

## One-line
Establishes consistency and convergence rates for nonparametric estimation of a graphon $f(x,y)$ — the limit object of an exchangeable random network — via maximum profile likelihood fitting of stochastic blockmodels, covering dense through sparse regimes.

## Key claim
For an $\alpha$-Hölder graphon $f$ scaled by $\rho_n$ with $\rho_n = \omega(n^{-1}\log^3 n)$, the MPLE blockmodel estimator $\hat f$ with $k$ groups (avg size $\bar h = n/k$) achieves MSE bounded by $O_P\!\left(\frac{\log(h_\vee/\rho_n)}{n\rho_n} + \frac{\log^2(1/\rho_n)\log(n/\bar h)}{\bar h^2 \rho_n} + \frac{\log \bar h}{\bar h^2 \rho_n} + (h_\vee/n)^{2\alpha} + n^{-\alpha/2}\right)$ under the cut-distance metric.

## Method
Model edges as $A_{ij}\sim \mathrm{Bernoulli}(\rho_n f(\xi_i,\xi_j))$ with latent uniforms $\xi_i$; approximate $f$ by a $k$-block stepfunction via partition $H$. Profile out block means $\theta_{ab}$ (closed-form $\bar A_{ab}$) to get MPLE $\hat z = \arg\min_z \sum_{i<j} D(A_{ij}\|\bar A_{z_iz_j})$ over admissible partitions. Combines uniform Bernstein-style control of Poisson–Binomial block proportions (excess-risk Theorem 5.1) with Riemann-sum approximation theory bounding $\|f-\bar f\|_\infty \le M(\sqrt 2 \max_a h_a/n)^\alpha$.

## Result
Excess blockmodel risk decomposes into a stochastic term $\max\{\log(\bar h)/(\bar h^2\bar\rho),\, \log^2(1/\rho_\wedge)\log(n/\bar h)/(n\bar\rho)\}$ plus deterministic approximation error of order $(h_\vee/n)^{2\alpha}$. Three regimes: dense ($\rho$ const, $k=O(n^{3/4})$) gives rate $\log n/n$; sparse ($\rho\sim n^{-2\gamma}$, $\gamma<1/2$) gives $\log(n)^{3/2}/n^{1/2-\gamma}$; ultra-sparse at the connectivity threshold $\rho_n \sim \log(n)^{3+\beta}/n$ gives rate $\log(n)^{-\beta/2}$. Below $1/n$, Poisson rather than Normal block limits hold and the theory breaks.

## Why it matters here
General background; no direct arena tie. Closest relevance is the toolkit — Hölder-class stepfunction approximation, profile-likelihood / KL minimization with block effective sample size constraints, and the Szemerédi-regularity-style intuition that any large structure is approximately blocky — which could inform extremal-graph or combinatorial problems if any arena problem reduces to estimating a structured density on $[0,1]^2$.

## Open questions / connections
- Extremely sparse regime $\rho_n \sim 1/n$: Poisson block limits replace Normal; the consistency rate machinery here doesn't apply (cf. Bollobás–Riordan 2009; Olhede–Wolfe companion).
- Computational tractability of the MPLE $\hat z$ is not addressed — it's combinatorial over $k^n$ partitions; in practice approximated via spectral or variational methods (Rohe–Chatterjee–Yu 2011; Airoldi et al. 2008).
- Extends Choi–Wolfe–Airoldi (2012) fixed-density result to growing $k$ and sparse $\rho_n$; complements Chatterjee (2012) universal singular value thresholding as an alternative graphon estimator.

## Key terms
graphon, stochastic blockmodel, Aldous–Hoover theorem, exchangeable random graph, profile likelihood, Hölder continuity, Szemerédi regularity, cut distance, Kullback–Leibler divergence, nonparametric regression, sparse network, connectivity threshold, Bickel–Chen, Lovász graph limits
