---
type: source
kind: paper
title: Adapting to Function Difficulty and Growth Conditions in Private Optimization
authors: Hilal Asi, Daniel Lévy, John C. Duchi
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.02391
source_local: ../raw/2021-asi-adapting-function-difficulty-growth.pdf
topic: general-knowledge
cites:
---

# Adapting to Function Difficulty and Growth Conditions in Private Optimization

**Authors:** Hilal Asi, Daniel Lévy, John C. Duchi  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.02391

## One-line
Private stochastic convex optimization algorithms that automatically adapt to the local growth exponent $\kappa$ of the loss, achieving faster rates than the worst-case bound without knowing $\kappa$.

## Key claim
For losses satisfying $\kappa$-growth $f(x) - f(x^\star) \ge (\lambda/\kappa)\|x-x^\star\|_2^\kappa$ with $\kappa > 1$, the worst-case private rate $\sqrt{d}/(n\varepsilon)$ is improvable to $(\sqrt{d}/(n\varepsilon))^{\kappa/(\kappa-1)}$ for $(\varepsilon,\delta)$-DP (and $(d/(n\varepsilon))^{\kappa/(\kappa-1)}$ for pure $\varepsilon$-DP), simultaneously minimax-optimal across all $\kappa \ge 1 + \Theta(1)$ — without prior knowledge of $\kappa$.

## Method
Two-pronged. (i) **Inverse sensitivity mechanism** (Asi-Duchi) used with a $\rho$-smoothed gradient-based proxy $G^\rho_S(x) = \inf_{\|y-x\|\le\rho}\|\nabla f_S(y)\|_2$, exploiting the Kurdyka-Łojasiewicz inequality $f(x)-f(x^\star) \le (\kappa/\lambda)^{1/(\kappa-1)}\|\nabla f(x)\|_2^{\kappa/(\kappa-1)}$ to convert gradient-norm control into excess-loss control. (ii) **Epoch-based localization** (Algorithm 2 on top of Feldman-Koren-Talwar Algorithm 1): iteratively solve regularized ERMs on shrinking domains $\mathcal X_i = \{x: \|x-x_i\|_2 \le 2^{-i}D_0\}$ with Laplace/Gaussian noise; growth lets the diameter halve each epoch, so the agent never needs $\kappa$ explicitly. Lower bounds via Fano + Gilbert-Varshamov packing for $\kappa\ge 2$, privatized Le Cam for $\kappa\in(1,2)$, and an ERM-to-SCO reduction via geometrically increasing $\|\cdot\|_2^\kappa$ regularization (Proposition 3).

## Result
- **Pure $\varepsilon$-DP upper bound (Thm 2):** $(1/\lambda)^{1/(\kappa-1)}\cdot \tilde O\big(L/\sqrt n + Ld/(n\varepsilon(\kappa-1))\big)^{\kappa/(\kappa-1)}$.
- **Approximate $(\varepsilon,\delta)$-DP upper bound (Thm 3):** same form with $\sqrt{d\log(1/\delta)}$ replacing $d$.
- **Matching lower bounds:** Thm 4 ($\kappa\ge 2$, any $d$, pure DP), Thm 5 ($\kappa\in(1,2]$, $d=1$, pure DP), Thm 6 ($\kappa\ge 2$, approximate DP).
- High-probability guarantees throughout, strengthening prior expected-loss results.
- Illustrative: $\kappa = 5/4 \Rightarrow$ privacy term scales as $(d/(n\varepsilon))^5$ — dramatic vs. worst-case $d/(n\varepsilon)$.

## Why it matters here
General background; no direct arena tie — this is private SCO, not deterministic math optimization, and Einstein Arena problems are non-stochastic. The structural idea worth flagging is **growth-exponent adaptation via epoch-shrinking domains**: when the optimizer can certify $\kappa$-growth (e.g. $\kappa$-norm regression, equioscillation neighborhoods, basin rigidity), iterative trust-region halving extracts rate-improvement automatically — conceptually parallel to how mpmath polish tightens around an active set.

## Open questions / connections
- Tight lower bound for $\kappa\in(1,2)$ in dimension $d>1$ left open (Theorem 5 is 1-D only).
- Practical (gradient-method) version of the inverse-sensitivity mechanism for non-DP instance-optimal optimization.
- Extension to non-Euclidean ($\ell_p$) geometries — current matrix is $\ell_2$-only.
- Connections: Juditsky-Nesterov uniform convexity, Ramdas-Singh stochastic-oracle bounds, Zhu-Chatterjee-Duchi-Lafferty local minimax complexity, Feldman-Koren-Talwar localization.

## Key terms
differential privacy, stochastic convex optimization, $\kappa$-growth, uniform convexity, Kurdyka-Łojasiewicz inequality, inverse sensitivity mechanism, localization, epoch-based algorithm, Laplace mechanism, Gaussian mechanism, Fano's method, Le Cam's method, Gilbert-Varshamov packing, minimax lower bound, Asi-Duchi, Feldman-Koren-Talwar
