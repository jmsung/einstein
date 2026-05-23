---
type: source
kind: paper
title: Stochastic Nested Variance Reduction for Nonconvex Optimization
authors: Dongruo Zhou, Pan Xu, Quanquan Gu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1806.07811
source_local: ../raw/2018-zhou-stochastic-nested-variance-reduction.pdf
topic: general-knowledge
cites:
---

# Stochastic Nested Variance Reduction for Nonconvex Optimization

**Authors:** Dongruo Zhou, Pan Xu, Quanquan Gu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1806.07811

## One-line
Proposes SNVRG, a stochastic gradient method that uses $K+1$ nested reference points (instead of SVRG's 2) to drive variance to zero faster, lowering gradient complexity for nonconvex finite-sum optimization.

## Key claim
For smooth nonconvex $F(x) = \frac{1}{n}\sum_{i=1}^n f_i(x)$ with averaged $L$-Lipschitz gradient and bounded stochastic-gradient variance $\sigma^2$, SNVRG finds an $\epsilon$-approximate stationary point ($\|\nabla F(x)\|_2^2 \le \epsilon$) in $\widetilde{O}(n \wedge \epsilon^{-2} + \epsilon^{-3} \wedge n^{1/2}\epsilon^{-2})$ stochastic gradient evaluations — strictly better than SVRG's $O(n + n^{2/3}\epsilon^{-2})$ and SCSG's $O(n \wedge \epsilon^{-2} + \epsilon^{-10/3} \wedge n^{2/3}\epsilon^{-2})$.

## Method
Nested variance reduction: at each iterate $x_t$, maintain $K+1$ reference points $x_t^{(0)},\dots,x_t^{(K)}$ updated on a hierarchy of timescales $T_1,\dots,T_K$, and build a telescoped semi-stochastic gradient $v_t = \sum_{l=0}^K g_t^{(l)}$ where $g_t^{(l)} = \frac{1}{B_l}\sum_{i \in I_l}[\nabla f_i(x_t^{(l)}) - \nabla f_i(x_t^{(l-1)})]$. Choosing $K = \log\log B$, $T_l = 2^{2^{l-1}}$, $B_l = 6^{K-l+1}B/2^{2^{l-2}}$ makes the cascade telescope so variance contracts geometrically per level while the per-epoch gradient cost stays $\widetilde{O}(B)$. Storage is $O(Kd) = O(d\log\log n)$.

## Result
Theorem 4.2: gradient complexity $\widetilde{O}\big((\sigma^2/\epsilon^2 \wedge n) + L\Delta_F \epsilon^{-2}(\sigma^2/\epsilon^2 \wedge n)^{1/2}\big)$ where $\Delta_F = F(z_0) - F^*$. Theorem 4.4: under $\tau$-gradient-dominance (P-L) condition, SNVRG-PL reaches an $\epsilon$-global minimizer in $\widetilde{O}\big((n \wedge \tau\sigma^2/\epsilon) + \tau L (n \wedge \tau\sigma^2/\epsilon)^{1/2}\big)$, beating SCSG by an $(n \wedge \tau\epsilon^{-1})^{1/6}$ factor. Beats Natasha 2's $\widetilde{O}(\epsilon^{-3.25})$ without needing Hessian Lipschitzness. LeNet experiments on MNIST/CIFAR10/SVHN confirm faster training-loss and lower test-error than SGD, SGD-momentum, ADAM, SCSG.

## Why it matters here
General background; no direct arena tie. SNVRG is a stochastic optimizer for $n$-large empirical-risk problems; the arena workload is small-$n$, deterministic, high-precision (mpmath polish, L-BFGS, parallel tempering) where variance reduction over a sum of $n$ component losses isn't the bottleneck. Could be relevant only if a future arena problem reduces to large-$n$ ERM with stochastic gradient noise — none of the 23 do.

## Open questions / connections
- Lower bound for nonconvex finite-sum: SNVRG's $\epsilon^{-3} \wedge n^{1/2}\epsilon^{-2}$ matches the concurrent SPIDER bound (Fang et al. 2018, arXiv:1807.01695); is this tight under only smoothness + bounded-variance?
- Extension to second-order stationarity / saddle-point escape without Hessian-Lipschitz assumption.
- Whether the $K = \log\log n$ nesting depth is fundamental or an artifact of the analysis.

## Key terms
SNVRG, SVRG, SCSG, SPIDER, variance reduction, nested reference points, nonconvex finite-sum optimization, stochastic gradient descent, gradient complexity, Polyak-Lojasiewicz condition, gradient dominated function, semi-stochastic gradient
