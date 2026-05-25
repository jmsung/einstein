---
type: source
kind: paper
title: Momentum-Based Variance Reduction in Non-Convex SGD
authors: Ashok Cutkosky, Francesco Orabona
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.10018
source_local: ../raw/2019-cutkosky-momentum-based-variance-reduction-non-convex.pdf
topic: general-knowledge
cites:
---

# Momentum-Based Variance Reduction in Non-Convex SGD

**Authors:** Ashok Cutkosky, Francesco Orabona  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.10018

## One-line
Introduces Storm, a single-loop SGD variant whose momentum term itself performs variance reduction, eliminating the need for checkpoint "mega-batches" while matching the optimal non-convex stochastic rate.

## Key claim
Storm finds $\mathbb{E}[\|\nabla F(\hat{x})\|] \leq O(1/\sqrt{T} + \sigma^{1/3}/T^{1/3})$ on $L$-smooth non-convex $F$ with $\sigma^2$-bounded gradient noise, matching the lower bound of Arjevani et al. — without batches, without knowing $\sigma$, and with an AdaGrad-style adaptive step size.

## Method
Replaces standard momentum $d_t = (1-a)d_{t-1} + a\nabla f(x_t,\xi_t)$ with the recursive estimator $d_t = (1-a)d_{t-1} + a\nabla f(x_t,\xi_t) + (1-a)(\nabla f(x_t,\xi_t) - \nabla f(x_{t-1},\xi_t))$, sharing one sample $\xi_t$ across two gradient evaluations. Learning rate $\eta_t \propto (w + \sum_i G_i^2)^{-1/3}$ and momentum $a_{t+1} = c\eta_t^2$ are AdaGrad-style adaptive. The analysis uses a Lyapunov potential $\Phi_t = F(x_t) + z_t\|\epsilon_t\|^2$ with time-varying $z_t \propto 1/\eta_{t-1}$, where $\epsilon_t = d_t - \nabla F(x_t)$.

## Result
Theorem 1 gives explicit constants: with $k = (b G^2/L)^{1/3}$ and tuned $w, c$, the bound holds for any noise level $\sigma$. In the deterministic case ($\sigma=0$) the rate becomes $O(\ln T/\sqrt{T})$, recovering the optimal rate previously achieved only by checkpoint-based SVRG variants (Spider, SNVRG). CIFAR-10 / ResNet-32 experiments show Storm trains marginally faster than AdaGrad and Adam in iterations.

## Why it matters here
General background; no direct arena tie. Could inform any future agent work that needs gradient-based non-convex stochastic optimization at SOTA rates (e.g. learned magic-function parameterizations, neural surrogates for LP/SDP feasibility), but none of the 23 arena problems currently uses SGD as its primary optimizer.

## Open questions / connections
- Does the same recursive-momentum estimator explain *why* heuristic SGD+momentum outperforms plain SGD in practice — i.e. is practical momentum doing implicit variance reduction?
- Can the time-varying Lyapunov potential $\Phi_t = F(x_t) + z_t\|\epsilon_t\|^2$ be adapted to constrained / manifold-valued problems (e.g. Stiefel-manifold parameterizations for sphere-packing configurations)?
- Extends Spider/SNVRG line [Fang et al. 2018, Zhou et al. 2018]; leaves open whether last-iterate (not random-iterate) bounds hold.

## Key terms
Storm, variance reduction, non-convex SGD, recursive momentum, adaptive learning rate, AdaGrad, SVRG, Spider, SARAH, Lyapunov potential, checkpoint-free, stochastic optimization, Cutkosky, Orabona
