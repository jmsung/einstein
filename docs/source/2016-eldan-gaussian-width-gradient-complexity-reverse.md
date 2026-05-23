---
type: source
kind: paper
title: Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations
authors: Ronen Eldan
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1612.04346
source_local: ../raw/2016-eldan-gaussian-width-gradient-complexity-reverse.pdf
topic: general-knowledge
cites:
---

# Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations

**Authors:** Ronen Eldan  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1612.04346

## One-line
Introduces Gaussian-width of the log-density's gradient as a complexity measure that, when small, forces a measure on $\{-1,1\}^n$ or $\mathbb{R}^n$ to decompose into a mixture of near-product measures, sharpening the Chatterjee–Dembo nonlinear large-deviation framework.

## Key claim
For any $f:C_n\to\mathbb{R}$ there is a product measure $\xi$ with $\log\int e^f d\mu \le \int f d\xi - D_{KL}(\xi\|\mu) + 64\,\mathrm{Lip}(f)^{2/3} D(f)^{1/3} n^{2/3}$, where $D(f) = \mathrm{GW}(\{\nabla f(y):y\in C_n\})$ is the Gaussian-width of the discrete-gradient image; whenever $D(f)=o(n)$ and $\mathrm{Lip}(f)=O(1)$, mean-field is tight to first order, and the full measure $\nu$ decomposes as $\int \tau_\theta \nu\, dm(\theta)$ with $\tau_\theta\nu$ close in $W_1$ to a product measure for $m$-most $\theta$.

## Method
Stochastic-control coupling of $\nu$ to a Brownian motion (Föllmer/Borell/Lehec entropy-optimal drift), tracking a martingale $X_t$ whose tilt parameter at a stopping time $\tau$ produces the decomposition $\nu = \int \tau_\theta \nu\, dm(\theta)$. The trace of the covariance $\Sigma_t$ of the conditioned measure is controlled by $\mathrm{GW}(K)$ via Sudakov-Fernique / Slepian comparison, giving low-rank tilts; in the Gaussian case the same drift yields a reverse log-Sobolev $I(\nu) - 2 D_{KL}(\nu\|\gamma) \le 2 D(\nu)^{2/3} I(\nu)^{1/3} + \max(-\inf \Delta f, 0)$.

## Result
Three quantitative payoffs: (1) the LDP bound $\log P(f(Y)\ge tn) \le -\phi_p(t-\delta)(1-64 L n^{-1/3})$ with explicit $L$ in $D(f)$, $\mathrm{Lip}(f)$, $\delta$, $p$; (2) triangle-count large deviations in $G(N,p)$ extend down to $p_N \gg N^{-1/18}\log N$ via $D(f_{\triangle}) \le 5 n^{3/4}$ (and $D(f_H)\le |E(H)|N^{3/2}$ for general subgraphs); (3) any exponential random graph $G$ couples to an $\varepsilon$-mixture $G' = G(N,\rho)$ with $\mathbb{E} d_H(G,G') \le 20 n^{11/12}\varepsilon^{-1/3}(\sum|\beta_i||E(H_i)|)^{1/3}$.

## Why it matters here
General background; no direct arena tie — none of the 23 arena problems are mean-field statistical-mechanics partition-function questions. The stochastic-localization / entropic-coupling toolkit and the Gaussian-width-of-gradient complexity measure could inform any future arena problem framed as extremal density of a subgraph/arithmetic structure in a random set, and the reverse log-Sobolev inequality is a generic tool for entropy-energy tradeoffs that may surface in functional-inequality problems.

## Open questions / connections
- Extends Chatterjee–Dembo [2016] by replacing covering numbers with Gaussian-width and dropping the second-derivative hypothesis — what is the right discrete analogue of "gradient complexity" for non-Lipschitz $f$ (Remark 3's mesoscopic-oscillation condition)?
- Subsequent Eldan–Gross [2017a,b] show the mixture components are critical points of the mean-field functional and (dense regime) supported on block matrices — a stochastic-block-model picture of exponential random graphs.
- Does the reverse log-Sobolev inequality have a sharp form, and can it replace Brascamp–Lieb / Talagrand transport inequalities in concentration arguments?

## Key terms
Gaussian width, gradient complexity, mean-field approximation, nonlinear large deviations, reverse log-Sobolev inequality, stochastic localization, Föllmer drift, entropic coupling, exponential random graph, subgraph density, triangle count, Erdős–Rényi, Wasserstein distance, Kullback–Leibler divergence, Ising model, Chatterjee, Dembo, Eldan
