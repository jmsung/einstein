---
type: source
kind: paper
title: Stochastic model-based minimization of weakly convex functions
authors: Damek Davis, D. Drusvyatskiy
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.06523
source_local: ../raw/2018-davis-stochastic-model-based-minimization-weakly.pdf
topic: general-knowledge
cites:
---

# Stochastic model-based minimization of weakly convex functions

**Authors:** Damek Davis, D. Drusvyatskiy  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.06523

## One-line
Unified analysis showing that stochastic methods which sample-and-minimize simple models of a weakly convex objective drive a Moreau-envelope stationarity measure to zero at rate $O(k^{-1/4})$.

## Key claim
For any $\rho$-weakly convex $\varphi = f + r$ with mild Lipschitz conditions, the proximal stochastic subgradient, prox-linear, and proximal-point methods all satisfy $\mathbb{E}\,\|\nabla \varphi_{1/(2\rho)}(x)\| \le \varepsilon$ after at most $O(\varepsilon^{-4})$ iterations — the first sample-complexity guarantee for stochastic subgradient on a broad nonsmooth nonconvex class.

## Method
Algorithms are unified as **stochastic one-sided models**: at each step, sample $\xi_t$, form a model $f_{x_t}(\cdot,\xi_t)$ satisfying $\mathbb{E}[f_x(x,\xi)]=f(x)$ and $\mathbb{E}[f_x(y,\xi)-f(y)] \le \tfrac{\tau}{2}\|y-x\|^2$, then minimize model $+ r + \tfrac{1}{2\alpha_t}\|y-x_t\|^2$. The convergence proof shows the iterates perform approximate descent on the **Moreau envelope** $\varphi_\lambda(x)=\min_y \{\varphi(y)+\tfrac{1}{2\lambda}\|y-x\|^2\}$, which is $C^1$-smooth when $\lambda<\rho^{-1}$. Linear models recover proximal subgradient; convex composite linearizations recover prox-linear; identity models recover proximal point.

## Result
Master rate: $\mathbb{E}[\varphi_\lambda(x_{t+1})] \le \mathbb{E}[\varphi_\lambda(x_t)] - \alpha_t c_1 \mathbb{E}[\|\nabla\varphi_\lambda(x_t)\|^2] + \alpha_t^2 c_2$, yielding $O(\varepsilon^{-4})$ for stationarity. In the convex sub-case ($\tau=0$, models convex), function-gap rate is $O(1/\sqrt{T})$; under $\mu$-strong convexity it improves to $O(L^2/(\mu T))$ via nonuniform $(t+1)$-weighted averaging. Removes mini-batching requirement of prior smooth-stochastic results and improves convex proximal-subgradient bounds by dropping $\|\partial r\|$ dependence.

## Why it matters here
General background; no direct arena tie — but the **Moreau envelope as a smooth potential for nonsmooth nonconvex stationarity** is the right analytic frame for any subgradient-style polish on weakly convex Einstein objectives (e.g., $\ell_1$-residual phase-retrieval-like formulations, robust composite losses). Connects to the agent's compute-router stance: prox-linear / prox-point subproblems often have closed forms (e.g., the explicit $\Delta^*$ formula for phase-retrieval models) and are empirically far more stepsize-robust than vanilla subgradient.

## Open questions / connections
- Can $O(\varepsilon^{-4})$ be improved beyond finite-sum / higher-smoothness settings (Allen-Zhu Natasha2, SCSG) for general nonsmooth weakly-convex problems?
- Precise relation to "inexact first-order oracle" framework of Devolder–Glineur–Nesterov in the nonconvex regime is left open.
- Extends Nurminskii (1973–74) almost-sure subsequential convergence to quantitative rates; complements Duchi–Ruan (2017) on stochastic composite optimization.

## Key terms
weakly convex, Moreau envelope, proximal point method, prox-linear, stochastic subgradient, composite optimization, phase retrieval, blind deconvolution, conditional value-at-risk, sample complexity, stationarity measure, subdifferential hypomonotonicity
