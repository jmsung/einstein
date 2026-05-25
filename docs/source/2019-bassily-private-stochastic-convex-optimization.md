---
type: source
kind: paper
title: Private Stochastic Convex Optimization with Optimal Rates
authors: Raef Bassily, V. Feldman, Kunal Talwar, Abhradeep Thakurta
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1908.09970
source_local: ../raw/2019-bassily-private-stochastic-convex-optimization.pdf
topic: general-knowledge
cites:
---

# Private Stochastic Convex Optimization with Optimal Rates

**Authors:** Raef Bassily, V. Feldman, Kunal Talwar, Abhradeep Thakurta  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1908.09970

## One-line
Closes the gap between private ERM and private stochastic convex optimization (SCO) by showing the optimal excess population loss rate is $O(1/\sqrt{n} + \sqrt{d}/(n\epsilon))$, matching non-private SCO when $d = O(n)$.

## Key claim
For $(\epsilon,\delta)$-DP SCO with convex $L$-Lipschitz losses over an $M$-bounded convex $W \subset \mathbb{R}^d$, the optimal excess population loss is $\Theta\!\left(ML \cdot \max\!\left(\frac{1}{\sqrt n},\, \frac{\sqrt{d\log(1/\delta)}}{n\epsilon}\right)\right)$ — improving the prior $O(n^{-1/4})$ bound of [BST14] to the optimal $1/\sqrt n$ in the regime $d = O(n\epsilon^2)$.

## Method
Three algorithmic routes, all leveraging *uniform stability* (Bousquet–Elisseeff) to bound generalization. (1) Mini-batch **noisy SGD** ($A_{\mathrm{NSGD}}$) with $T \approx \min(n, n^2\epsilon^2/d)$ steps and batch size $m \approx \max(\sqrt n, 1)$, extending the SGD-stability analysis of [HRS15, FV19] to the noisy case. (2) For non-smooth losses, a **Moreau–Yosida envelope** reduction with $\beta$-smoothing parameter tuned to $n$, implemented efficiently via approximate proximal steps ($A_{\mathrm{ProxGD}}$). (3) **Objective perturbation** ($A_{\mathrm{ObjP}}$) with a noisy linear term plus $\lambda\|w\|^2$ regularizer; combined with SVRG it yields $O(n\log n)$ gradient-oracle complexity.

## Result
Theorem 3.2/4.4/5.3: all three algorithms achieve $\Delta L \leq O\!\left(ML \cdot \max\!\left(1/\sqrt n,\, \sqrt{d\log(1/\delta)}/(n\epsilon)\right)\right)$. Stability bound for noisy SGD: $\alpha = L^2 T\eta/n$ (Lemma 3.4). Objective perturbation reaches optimal rate with regularizer $\lambda = \tfrac{2L}{M}\sqrt{2/n^2 + 4d\log(1/\delta)/(\epsilon^2 n^2)}$. Lower bound (Appendix C) reduces private ERM to private SCO via empirical-distribution resampling, certifying tightness up to log factors.

## Why it matters here
General background; no direct arena tie. The Moreau–Yosida smoothing reduction and the uniform-stability-as-generalization framework could inform meta-methodology for non-smooth optimization (e.g. proximal steps replacing direct gradients when the loss is non-differentiable at active constraints), which intersects loosely with techniques like Remez exchange or active-set polishing — but the paper's privacy focus and high-dimensional regime are out of scope for the Einstein Arena problem family.

## Open questions / connections
- Can the $O(n\log n)$ oracle complexity of objective perturbation be extended beyond the rank-1 Hessian assumption (Assumption 5.1) to general smooth convex losses?
- Does uniform stability provide tight high-probability (not just expectation) bounds for DP-SCO? [FV19] suggests yes up to log factors.
- Extends [BST14] (DP-ERM tight bounds) and [SSSSS09] (non-private SCO via stability); connects to [Fel16] showing uniform convergence is $\Omega(\sqrt{d/n})$ even when SCO is $O(1/\sqrt n)$.

## Key terms
differential privacy, stochastic convex optimization, DP-SCO, DP-ERM, uniform stability, noisy SGD, Moreau-Yosida envelope, proximal operator, objective perturbation, SVRG, Gaussian mechanism, moments accountant, generalization bound, Bassily, Feldman
