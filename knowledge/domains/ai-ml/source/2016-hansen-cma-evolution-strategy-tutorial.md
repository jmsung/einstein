---
type: source
kind: paper
title: "The CMA Evolution Strategy: A Tutorial"
authors: N. Hansen
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1604.00772
source_local: ../raw/2016-hansen-cma-evolution-strategy-tutorial.pdf
topic: general-knowledge
cites:
---

# The CMA Evolution Strategy: A Tutorial

**Authors:** N. Hansen  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1604.00772

## One-line
Tutorial deriving the Covariance Matrix Adaptation Evolution Strategy (CMA-ES), a derandomized black-box optimizer for non-linear, non-convex, ill-conditioned, non-separable continuous problems.

## Key claim
On convex-quadratic $f_H(x) = \tfrac{1}{2}x^T H x$, the optimal search covariance $C$ equals $H^{-1}$ up to a scalar, so CMA-ES's adapted $C$ is a stochastic quasi-Newton approximation of the inverse Hessian — making the strategy affine-invariant and competitive on ill-conditioned landscapes without gradient information.

## Method
Samples $\lambda$ offspring from $\mathcal{N}(m^{(g)}, (\sigma^{(g)})^2 C^{(g)})$, then updates $(m, C, \sigma)$ from the ranked $\mu$ best: weighted recombination for $m$ (eq. 9); covariance via a convex combination of **rank-$\mu$-update** (outer products of selected steps $y_{i:\lambda}y_{i:\lambda}^T$) and **rank-one update** along the cumulated evolution path $p_c$ (eq. 47); step-size $\sigma$ via cumulative step-size adaptation (CSA) comparing $\|p_\sigma\|$ to $E\|\mathcal{N}(0,I)\|$ (eq. 44). Active-CMA uses negative weights on worst offspring. Default $\lambda = 4 + \lfloor 3\ln n\rfloor$, $\mu = \lfloor\lambda/2\rfloor$, $w_i \propto \ln(\tfrac{\lambda+1}{2}) - \ln i$.

## Result
Provides the full default-parameter recipe (Table 1, eqs. 48–58) that requires no per-problem tuning: $c_\sigma, d_\sigma, c_c \propto 1/n$, $c_1 \approx 2/((n+1.3)^2+\mu_{\text{eff}})$, $c_\mu \approx 2\mu_{\text{eff}}/((n+2)^2+\mu_{\text{eff}})$. Strategy-internal cost reduced from $O(n^3)$ to $O(n^2)$ per eval by deferring eigendecomposition. Lists 8 termination criteria (NoEffectAxis, ConditionCov $>10^{14}$, EqualFunValues, Stagnation, TolFun, TolX, TolXUp). Recommends restarts with doubled $\lambda$ for multimodal problems (IPOP-CMA-ES).

## Why it matters here
Direct relevance to the arena agent's optimizer toolkit: CMA-ES is already in the compute-router decision matrix (large population, float32 on MPS or float64 on Modal). This tutorial is the canonical reference for the default parameters used in `src/`, the active-CMA negative-weight variant, and the boundary-handling penalization patterns (eqs. 62–64) — applicable to constrained problems like P14, P17, P18 where infeasible candidates arise.

## Open questions / connections
- Rigorous proof that optimal $C \propto H^{-1}$ is still missing (the paper notes "good intuition and strong empirical evidence" only).
- When to prefer rank-$\mu$ vs rank-one updates for problems with very small $\mu_{\text{eff}}$ relative to $n$ — relevant when polishing near a known basin.
- Boundary-handling via repair-with-Mahalanobis-clipping ($\|x-m\|_{\sigma^2 C} \le \sqrt{n}+2n/(n+2)$) vs penalty (eq. 63) — which is more robust for arena problems with box constraints?
- Connection to natural-gradient interpretation [Akimoto, ref 19] — does the information-geometric view suggest better step-size control for noisy / equioscillation landscapes?

## Key terms
CMA-ES, covariance matrix adaptation, evolution strategy, rank-mu update, rank-one update, evolution path, cumulative step-size adaptation, CSA, active CMA, weighted recombination, mu-effective, derandomized self-adaptation, black-box optimization, inverse Hessian, Hansen, Ostermeier
