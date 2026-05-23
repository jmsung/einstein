---
type: source
kind: paper
title: "Bypassing the Ambient Dimension: Private SGD with Gradient Subspace Identification"
authors: Yingxue Zhou, Zhiwei Steven Wu, A. Banerjee
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.03813
source_local: ../raw/2020-zhou-bypassing-ambient-dimension-private.pdf
topic: general-knowledge
cites:
---

# Bypassing the Ambient Dimension: Private SGD with Gradient Subspace Identification

**Authors:** Yingxue Zhou, Zhiwei Steven Wu, A. Banerjee  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.03813

## One-line
Projected DP-SGD reduces the dimension-dependence of private deep-network training by perturbing gradients only inside a low-dim subspace estimated from a tiny public dataset.

## Key claim
The error rate of DP-SGD can be made to scale with the *intrinsic* gradient subspace dimension $k$ (and only $\log p$) instead of the ambient parameter count $p$, by projecting the noisy gradient onto the top-$k$ eigenspace $\hat V_k(t)$ of the public second-moment matrix $M_t = \tfrac{1}{m}\sum_i \nabla\ell(w_t,\tilde z_i)\nabla\ell(w_t,\tilde z_i)^\top$.

## Method
At each step they (i) estimate $\hat V_k(t)$ from $m$ public samples drawn from the same distribution as the private data, (ii) form $\tilde g_t = \hat V_k\hat V_k^\top(g_t + b_t)$ with isotropic Gaussian $b_t\sim N(0,\sigma^2 I_p)$, (iii) update $w_{t+1}=w_t-\eta_t\tilde g_t$. Subspace error is controlled by a *uniform* second-moment concentration bound proved via generic chaining (Talagrand's $\gamma_2$ functional) on the iterate set $W$, then converted to $\|\hat V_k\hat V_k^\top - V_kV_k^\top\|$ via Davis–Kahan.

## Result
Smooth non-convex: $\mathbb{E}\|\nabla\hat L_n(w_R)\|_2^2 \le \tilde O(k\rho G^2/(n\varepsilon)) + O(\Lambda G^4\rho^2\gamma_2^2(W,d)\log p/m)$, where $\Lambda = \tfrac{1}{T}\sum_t 1/\alpha_t^2$ depends on eigen-gaps. Lipschitz convex: $\mathbb{E}[\hat L_n(\bar w)-\hat L_n(w^*)]\le O(kG^2/(n\varepsilon))+O(\Lambda G\rho\gamma_2(W,d)\log p/\sqrt m)$. When the gradient set is a union of ellipsoids with decay $e(j)\le c/\sqrt j$, $\gamma_2 = O(\sqrt{\log p})$, so the public-sample complexity is only logarithmic in $p$; experiments on MNIST / Fashion-MNIST with only $m=100$ public samples show substantial accuracy gains over DP-SGD in the small-$\varepsilon$ regime.

## Why it matters here
General background; no direct arena tie. The math content of interest is the uniform $\gamma_2$/generic-chaining bound on empirical-vs-population second-moment matrices, and the observation that union-of-ellipsoids gradient geometry kills the $\sqrt p$ factor — both potentially relevant for any high-dimensional optimization where the iterates live on low-complexity manifolds.

## Open questions / connections
- Can the subspace identification be done *privately* (instead of via public data) with reconstruction error better than the $\sqrt p$ bound of Dwork et al. 2014?
- How tight is the $\gamma_2(W,d)$ estimate when $W$ is the actual SGD trajectory rather than the worst-case iterate set?
- Extends Jain–Thakurta (2014), Song et al. (2020), Kairouz et al. (2020) on dimension-independent private ERM; contrasts with Yu et al. (2021) which adds residual noise and requires fresh public samples per step.

## Key terms
differential privacy, DP-SGD, gradient subspace identification, generic chaining, Talagrand $\gamma_2$ functional, Gaussian width, Davis–Kahan sin-$\theta$ theorem, Ahlswede–Winter inequality, ellipsoid gradient geometry, Polyak–Łojasiewicz condition, eigen-gap, empirical risk minimization
