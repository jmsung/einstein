---
type: source
kind: paper
title: Stochastic Halpern Iteration with Variance Reduction for Stochastic Monotone Inclusions
authors: Xufeng Cai, Chaobing Song, Cristóbal Guzmán, Jelena Diakonikolas
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2203.09436v4
source_local: ../raw/2022-cai-stochastic-halpern-iteration-variance.pdf
topic: general-knowledge
cites: 
---

# Stochastic Halpern Iteration with Variance Reduction for Stochastic Monotone Inclusions

**Authors:** Xufeng Cai, Chaobing Song, Cristóbal Guzmán, Jelena Diakonikolas  ·  **Year:** 2022  ·  **Source:** http://arxiv.org/abs/2203.09436v4

## One-line
Variance-reduced stochastic Halpern iteration that finds approximate zeros of monotone operators with substantially fewer stochastic oracle calls than prior methods.

## Key claim
For stochastic Lipschitz-monotone (and cocoercive) inclusions, achieves $O(1/\epsilon^3)$ stochastic oracle complexity for $\|F(u)\| \le \epsilon$ — improving the prior best $O(1/\epsilon^4)$ — and $O(\log(1/\epsilon)/\epsilon^2)$ under additional sharpness/strong monotonicity, which is unimprovable in $\epsilon$.

## Method
Combines classical Halpern iteration $u_{k+1} = \lambda_{k+1} u_0 + (1-\lambda_{k+1})(u_k - \frac{2}{L_{k+1}}\tilde F(u_k))$ (with $\lambda_k = 1/(k+1)$) with a PAGE-style recursive variance-reduced operator estimator using data-dependent batch sizes $S_2(k) \propto \|u_k - u_{k-1}\|^2 / (p_k^2 \epsilon^2)$. For Lipschitz-monotone (non-cocoercive) case, uses Tran-Dinh–Luo two-step extrapolated Halpern variant. Sharpness case adds a scheduled restart wrapper. Analysis: potential function $C_k = (A_k/L_k)\|F(u_k)\|^2 + B_k\langle F(u_k), u_k - u_0\rangle$ plus an inductive argument bounding $\mathbb{E}\|\tilde F(u_k) - F(u_k)\|^2 = O(\epsilon^2/k)$ and $\mathbb{E}\|u_k - u_{k-1}\|^2 = O(1/k^2)$.

## Result
Algorithm 1 (cocoercive) and Algorithm 2 (Lipschitz monotone) both return $u_N$ with $\mathbb{E}\|F(u_N)\| \le O(\epsilon)$ using $O(\sigma^2 L \|u_0 - u^*\|/\epsilon^2 + L^3\|u_0 - u^*\|^3/\epsilon^3)$ stochastic operator evaluations. Algorithm 3 (sharpness/strong monotonicity with parameter $\mu$) achieves $\mathbb{E}\|u_N - u^*\|^2 \le \epsilon^2$ in $O((L/\mu)\log(\|u_0-u^*\|/\epsilon))$ outer iterations and $O(\sigma^2(\mu+L)\log(\|u_0-u^*\|/\epsilon)/(\mu^3\epsilon^2) + L^3\|u_0-u^*\|^2/(\mu^3\epsilon^2))$ total queries.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are stochastic monotone inclusions or min-max equilibrium computations — this work targets ML training (GANs, adversarial robustness) rather than the deterministic geometric/extremal optimization landscape the agent solves on.

## Open questions / connections
- Extends Diakonikolas (2020), Yoon–Ryu (2021), Tran-Dinh–Luo (2021) deterministic Halpern results to stochastic oracles via PAGE (Li et al. 2021).
- Whether the $O(1/\epsilon^3)$ rate is optimal for stochastic monotone inclusion under finite-variance oracle remains open (only $O(\log(1/\epsilon)/\epsilon^2)$ is shown tight under sharpness).
- Connection to negative comonotone / weakly monotone Lipschitz operators (Lee–Kim 2021) under variance reduction is not addressed.

## Key terms
Halpern iteration, monotone inclusion, variational inequality, cocoercive operator, Lipschitz monotone, variance reduction, PAGE estimator, stochastic oracle complexity, sharpness condition, fixed point iteration, min-max optimization, extragradient, Diakonikolas, Tran-Dinh
