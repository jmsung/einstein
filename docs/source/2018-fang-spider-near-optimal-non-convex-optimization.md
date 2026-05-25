---
type: source
kind: paper
title: "SPIDER: Near-Optimal Non-Convex Optimization via Stochastic Path Integrated Differential Estimator"
authors: Cong Fang, C. Li, Zhouchen Lin, T. Zhang
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1807.01695
source_local: ../raw/2018-fang-spider-near-optimal-non-convex-optimization.pdf
topic: general-knowledge
cites:
---

# SPIDER: Near-Optimal Non-Convex Optimization via Stochastic Path Integrated Differential Estimator

**Authors:** Cong Fang, C. Li, Zhouchen Lin, T. Zhang  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1807.01695

## One-line
A variance-reduced stochastic gradient estimator (Spider) that recursively tracks the gradient along the optimization path, achieving near-optimal complexity for finding stationary points of smooth non-convex objectives.

## Key claim
Combined with normalized gradient descent, Spider finds an $\epsilon$-first-order stationary point in $O(\min(n^{1/2}\epsilon^{-2}, \epsilon^{-3}))$ stochastic gradient evaluations, and an $(\epsilon, O(\epsilon^{0.5}))$-second-order stationary point in $\tilde O(\min(n^{1/2}\epsilon^{-2}+\epsilon^{-2.5}, \epsilon^{-3}))$; the first-order rate matches the algorithmic lower bound in the finite-sum setting.

## Method
Spider builds an unbiased path-integrated estimator $V_k = \nabla f_{S_2}(x_k) - \nabla f_{S_2}(x_{k-1}) + V_{k-1}$, periodically refreshed with a large-batch anchor ($S_1$). Under $L$-Lipschitz gradients, the martingale variance bound $E\|V_k - \nabla f(x_k)\|^2 \le k L^2 \|x_k - x_{k-1}\|^2 / S_2 + \text{init error}$ keeps tracking error $O(\epsilon)$. The estimator is hybridized with normalized gradient descent (step $\eta \cdot v_k/\|v_k\|$, $\eta = \epsilon/(L n_0)$), and saddle escape uses a Neon2 negative-curvature subroutine; the same construction also yields zeroth-order rates $O(d\min(n^{1/2}\epsilon^{-2}, \epsilon^{-3}))$.

## Result
Sharp bounds (Theorems 1, 2): on-line gradient cost $16L\Delta\sigma\epsilon^{-3} + 2\sigma^2\epsilon^{-2}$; finite-sum cost $n + 8L\Delta n^{1/2}\epsilon^{-2}$. Lower bound (Theorem 3): no algorithm in the linear-span model can beat $\Omega(n^{1/2}\Delta L\epsilon^{-2})$ for finite-sum first-order stationarity, proven by extending Carmon et al.'s orthogonal-rotation hard instance to $n$ components. Zeroth-order analog (Theorem 8) achieves $O(d\min(n^{1/2}\epsilon^{-2}, \epsilon^{-3}))$, strictly better than prior SCSG-based zeroth-order results.

## Why it matters here
General background; no direct arena tie. Potentially relevant to large stochastic non-convex polishes (e.g., neural-net-style parameterizations), but the einstein problems are deterministic and either small-d (basin polish via L-BFGS / mpmath) or large-d but discrete (LP/SDP), so Spider's $\sqrt{n}$ savings don't trigger.

## Open questions / connections
- Does adding acceleration (Nesterov/Katyusha-style) close the $\epsilon^{-2.5}$ vs $\epsilon^{-1.75}$ gap with Neon+FastCubic in the small-$n$ regime?
- Can the path-integrated trick track other deterministic quantities (Hessian-vector products, function values, Fisher info) in einstein's evaluator stack with similar variance gains?
- Connection to SARAH (Nguyen 2017) — same recursion, different stepsize regime; concurrent SNVRG (Zhou 2018) matches the upper bound — what's the minimal recipe?

## Key terms
Spider, SARAH, variance reduction, stochastic gradient descent, normalized gradient descent, non-convex optimization, finite-sum optimization, second-order stationary point, negative curvature search, Neon2, cubic regularization, algorithmic lower bound, zeroth-order optimization, path-integrated estimator, Carmon, Allen-Zhu
