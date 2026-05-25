---
type: source
kind: paper
title: Lower bounds for non-convex stochastic optimization
authors: Yossi Arjevani, Y. Carmon, John C. Duchi, Dylan J. Foster, N. Srebro, Blake E. Woodworth
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1912.02365
source_local: ../raw/2019-arjevani-lower-bounds-non-convex-stochastic.pdf
topic: general-knowledge
cites:
---

# Lower bounds for non-convex stochastic optimization

**Authors:** Yossi Arjevani, Y. Carmon, John C. Duchi, Dylan J. Foster, N. Srebro, Blake E. Woodworth  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1912.02365

## One-line
Proves matching lower bounds showing SGD ($\epsilon^{-4}$) and variance-reduced methods like SPIDER/SNVRG ($\epsilon^{-3}$) are minimax-optimal for finding $\epsilon$-stationary points of smooth non-convex functions via stochastic first-order oracles.

## Key claim
For smooth non-convex $F$ with $F(x^{(0)}) - \inf F \le \Delta$ and $L$-Lipschitz gradient, accessed via an unbiased stochastic gradient oracle with variance $\le \sigma^2$: any randomized algorithm needs $\Omega(\Delta L \sigma^2 \epsilon^{-4})$ queries to find $x$ with $\mathbb{E}\|\nabla F(x)\| \le \epsilon$. Under the additional mean-squared smoothness assumption $\mathbb{E}\|g(x,z)-g(y,z)\|^2 \le \bar{L}^2 \|x-y\|^2$, the bound becomes $\Omega(\Delta \bar{L} \sigma \epsilon^{-3} + \sigma^2 \epsilon^{-2})$.

## Method
Builds on Carmon et al.'s noiseless chain-like construction (a Nesterov-style function where each query reveals at most one new "relevant" coordinate). Designs a noisy oracle that concentrates all noise on the single next-discoverable coordinate, fired with Bernoulli probability $p = \Theta(\epsilon^2/\sigma^2)$, amplifying the hardness by factor $1/p$. Extends from zero-respecting algorithms to general randomized algorithms via the random-rotation embedding of Woodworth-Srebro; for the $\epsilon^{-3}$ bound, replaces the discontinuous "incoming-coordinate" index with a continuous surrogate (soft indicator $\Theta_i$) to satisfy mean-square smoothness.

## Result
Theorem 3: $m_{\text{rand}}^\epsilon(K, \Delta, L, \sigma^2) = \Theta(\Delta L \sigma^2 \epsilon^{-4})$ and $\bar{m}_{\text{rand}}^\epsilon(K, \Delta, \bar{L}, \sigma^2) = \Theta(\Delta \bar{L} \sigma \epsilon^{-3} + \sigma^2 \epsilon^{-2})$, holding for any batch size $K$ and extending to statistical-learning and active (finite-sum) oracles. Establishes a clean $\epsilon^{-2}$ separation between convex (additive $\sqrt{\Delta L \epsilon^{-2}} + \sigma^2 \epsilon^{-2}$) and non-convex (multiplicative $\Delta L \epsilon^{-2} \cdot \sigma^2 \epsilon^{-2}$) stochastic optimization. The hard-instance dimension scales as $\tilde{O}(K \Delta^2 L^2 \sigma^2 \epsilon^{-6})$ for bounded variance.

## Why it matters here
General background; no direct arena tie. Useful as a "compute budget vs. accuracy" reference when reasoning about stochastic optimizers (basin-hopping, CMA-ES, parallel-tempering) — confirms $\epsilon^{-4}$ is the floor for plain SGD-style methods on smooth non-convex landscapes, so further speedup requires either mean-squared smooth gradient access (variance reduction) or higher-order information (Hessian-vector, cubic regularization).

## Open questions / connections
- Tight lower bound for $\epsilon^{-3.5}$ regime under Lipschitz-Hessian assumption (Tripuraneni et al., Fang et al. perturbed SGD)
- Extension to second-order stationary point complexity in the stochastic setting
- Whether the polynomial dimension dependence ($\tilde{O}(\epsilon^{-6})$) of the hard instance is necessary, or if dimension-free constructions exist for general randomized algorithms

## Key terms
non-convex stochastic optimization, SGD lower bound, variance reduction, SPIDER, SNVRG, mean-squared smoothness, stationary point complexity, oracle complexity, zero-respecting algorithm, probabilistic zero-chain, random rotation embedding, Nemirovski-Yudin, Carmon-Duchi-Hinder-Sidford, minimax optimality
