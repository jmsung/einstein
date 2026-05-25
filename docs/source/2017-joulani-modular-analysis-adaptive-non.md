---
type: source
kind: paper
title: "A Modular Analysis of Adaptive (Non-)Convex Optimization: Optimism, Composite Objectives, and Variational Bounds"
authors: Pooria Joulani, A. György, Csaba Szepesvari
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.02726
source_local: ../raw/2017-joulani-modular-analysis-adaptive-non.pdf
topic: general-knowledge
cites:
---

# A Modular Analysis of Adaptive (Non-)Convex Optimization: Optimism, Composite Objectives, and Variational Bounds

**Authors:** Pooria Joulani, A. György, Csaba Szepesvari  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.02726

## One-line
A unified, modular regret analysis for adaptive online/stochastic optimization (FTRL + Mirror Descent variants) that cleanly composes adaptivity, optimism, composite objectives, implicit updates, smoothness, strong convexity, and a class of non-convex losses.

## Key claim
A novel regret decomposition $R_T(x^*) = R_T^+(x^*) + \sum_t \langle g_t, x_t - x_{t+1}\rangle - \sum_t B_{f_t}(x^*,x_t) + \sum_t \delta_t$ (Lemma 2), combined with forward-regret bounds for generalized Ada-FTRL and Ada-MD (Theorem 3), recovers and extends existing $O(\sqrt{T})$ / $O(\log T)$ rates *and* gives variational rates $R_T \le O(R^3 L^2 + R\sqrt{D_T})$ where $D_T = \sum_t \|\nabla f_t(x_t) - \nabla f_{t-1}(x_t)\|_*^2$ for smooth composite losses (Corollary 9), with extension to $\tau$-star-(strongly-)convex non-convex losses.

## Method
Generalized Bregman divergence $B_f(y,x) := f(y) - f(x) - f'(x; y-x)$ defined via directional derivatives (works for non-differentiable, non-convex $f$). Regret is split into a "forward linear regret" $R_T^+(x^*) := \sum_t \langle g_t, x_{t+1} - x^*\rangle$ — bounded by a be-the-leader-style argument over two regularizer sequences $(p_t)$ proximal + $(q_t)$ centered — plus curvature/feedback-error terms. Each algorithmic ingredient (optimism via predictable hint $\tilde g_t$, composite term $\psi_t$, strong convexity, smoothness via Fenchel-Young against $\frac{L}{2}\|\cdot\|^2$) plugs in by canceling/cancelling a single term in the decomposition.

## Result
Recovers AdaGrad, Dual Averaging, FTRL-Centered/Prox, composite-objective MD, implicit MD, AdaDelay (non-monotone regularizers), and optimistic FTRL/MD under one proof template (Table 2, Corollaries 17–19). New: an adaptive optimistic composite-objective FTRL with variational bound $\frac{1}{2}(4R^3L^2 + R) + 2R\sqrt{2D_T}$ for $L$-smooth convex losses (Corollary 9); a one-projection-per-round optimistic MD family; and global convergence rates for $\tau$-star-convex and $\tau$-star-strongly-convex objectives, extending stochastic-optimization guarantees to a non-convex class containing matrix-completion-style problems.

## Why it matters here
General background; no direct arena tie. Possibly relevant if Einstein Arena problems are ever attacked via online-learning-style outer loops over parameterized solution families (e.g., adaptive step-size schedules for SLSQP/L-BFGS multistart), but the wiki's current optimizer stack (basin-hopping, parallel tempering, mpmath polish, Remez, SDP) sits outside the OCO regime this paper addresses.

## Open questions / connections
- Do these adaptive/variational bounds extend to quasi-convex or Polyak-Łojasiewicz objectives (authors flag this explicitly as future work)?
- Can the modular decomposition absorb delayed-feedback / asynchronous variants (e.g., AdaDelay) without re-analysis?
- Practical relevance to einstein: any value in using AdaGrad-style coordinate-wise step sizing inside the local-search phase of basin-hopping for problems with heterogeneous coordinate curvature (P11, P15)?

## Key terms
online convex optimization, AdaGrad, Follow-The-Regularized-Leader, Mirror Descent, Bregman divergence, optimistic online learning, composite objective, variational regret bound, implicit updates, star-convex, Polyak-Łojasiewicz, stochastic gradient descent
