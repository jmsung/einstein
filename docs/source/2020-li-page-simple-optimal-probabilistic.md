---
type: source
kind: paper
title: "PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization"
authors: Zhize Li, Hongyan Bao, Xiangliang Zhang, Peter Richtárik
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2008.10898
source_local: ../raw/2020-li-page-simple-optimal-probabilistic.pdf
topic: general-knowledge
cites:
---

# PAGE: A Simple and Optimal Probabilistic Gradient Estimator for Nonconvex Optimization

**Authors:** Zhize Li, Hongyan Bao, Xiangliang Zhang, Peter Richtárik  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2008.10898

## One-line
A single-loop stochastic-gradient method that probabilistically switches between a vanilla minibatch SGD step and a cheap SARAH-style recursive correction, achieving provably optimal gradient complexity for nonconvex finite-sum and online problems.

## Key claim
PAGE attains gradient complexity $O(n + \sqrt{n}/\epsilon^2)$ for nonconvex finite-sum and $O(b + \sqrt{b}/\epsilon^2)$ for nonconvex online (with $b := \min\{\sigma^2/\epsilon^2, n\}$), matching new tight lower bounds $\Omega(n + \sqrt{n}/\epsilon^2)$ and $\Omega(b + \sqrt{b}/\epsilon^2)$ proved in the same paper; under the PL condition it auto-switches to linear rates $O((n+\sqrt{n}\kappa)\log 1/\epsilon)$ and $O((b+\sqrt{b}\kappa)\log 1/\epsilon)$.

## Method
At each step $t$, with probability $p_t$ recompute a minibatch SGD estimator on size-$b$ batch, else reuse $g_t$ plus a SARAH-style correction $\tfrac{1}{b'}\sum_{i\in I}(\nabla f_i(x_{t+1}) - \nabla f_i(x_t))$ on a much smaller batch $b' \ll b$. Optimal tuning: $p_t \equiv b'/(b+b')$, $b' \le \sqrt{b}$, stepsize $\eta \le 1/(L(1+\sqrt{b/b'}))$. Lower bound is proved via a quadratic-with-orthogonal-shifts hard instance combined with Fang et al.'s SPIDER lower-bound construction.

## Result
Theorem 1: $T = (2\Delta_0 L/\epsilon^2)(1 + \sqrt{b/b'})$ iterations suffice for $\mathbb{E}\|\nabla f(\hat{x}_T)\|\le\epsilon$, giving $\#\mathrm{grad} \le n + 8\Delta_0 L\sqrt{n}/\epsilon^2$. Theorem 2 (new lower bound): any linear-span first-order algorithm needs $\Omega(n + \Delta_0 L\sqrt{n}/\epsilon^2)$ stochastic gradient queries, closing the gap that Fang et al.'s bound only covered for $n \le O(1/\epsilon^4)$. Deep-learning experiments (LeNet/VGG/ResNet on MNIST/CIFAR-10) show faster training-loss decrease and higher test accuracy than SGD at matched gradient budget.

## Why it matters here
General background; no direct arena tie — PAGE is a generic nonconvex stochastic optimizer, not a tool for the arena's structured math problems (sphere packing, autocorrelation, kissing numbers, etc.), which are dominated by LP/SDP duality, mpmath polish, parallel tempering, and basin-hopping rather than minibatch SGD. Possible weak relevance: any future agent training over a parameterized neural surrogate (e.g., learned magic-function ansatz or learned energy for configurations) could benefit, but current optimizers in this repo are deterministic / population-based.

## Open questions / connections
- Extends the SPIDER / SARAH / SSRGD line by removing the double-loop and proving matching lower bounds for the previously uncovered $n > 1/\epsilon^4$ regime.
- Does the probabilistic-switch trick port to deterministic optimizers used in this repo (e.g., as a control-variate for stochastic finite-difference Jacobian estimates in basin-hopping)?
- The PL-condition auto-acceleration suggests checking whether arena problems' local landscapes near SOTA basins satisfy PL — would let polish phases enjoy linear instead of sublinear convergence; no current finding on this.

## Key terms
PAGE, ProbAbilistic Gradient Estimator, nonconvex optimization, finite-sum, stochastic gradient descent, SARAH, SPIDER, SVRG, variance reduction, Polyak-Łojasiewicz condition, gradient complexity lower bound, Richtárik
