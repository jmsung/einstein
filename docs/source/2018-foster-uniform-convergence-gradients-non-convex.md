---
type: source
kind: paper
title: Uniform Convergence of Gradients for Non-Convex Learning and Optimization
authors: Dylan J. Foster, Ayush Sekhari, Karthik Sridharan
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.11059
source_local: ../raw/2018-foster-uniform-convergence-gradients-non-convex.pdf
topic: general-knowledge
cites:
---

# Uniform Convergence of Gradients for Non-Convex Learning and Optimization

**Authors:** Dylan J. Foster, Ayush Sekhari, Karthik Sridharan  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.11059

## One-line
Proves dimension-free uniform convergence rates for gradients of empirical risk in non-convex learning, using vector-valued Rademacher complexity, and turns these into optimal sample-complexity bounds for any algorithm that finds an approximate stationary point.

## Key claim
For non-convex losses satisfying a population-level $(\alpha,\mu)$-Gradient Domination condition ($L_D(w)-L^\star \le \mu\|\nabla L_D(w)\|^\alpha$, $\alpha\in[1,2]$), any algorithm returning $\hat{w}$ with $\|\nabla\hat{L}_n(\hat{w})\|\le\varepsilon$ achieves excess risk $O\!\big((\varepsilon + C(W)/\sqrt{n})^\alpha\cdot\mu\big)$ where $C(W)$ is a *norm-based, dimension-independent* capacity — so generalized linear models and robust regression hit $O(\varepsilon^{-2})$ sample complexity in infinite dimension and $O(d\varepsilon^{-1})$ in low dimension, matching known optimal rates.

## Method
Symmetrize $\sup_{w}\|\nabla\hat{L}_n(w)-\nabla L_D(w)\|$ via a normed (vector-valued) Rademacher complexity $\mathcal{R}_{\|\cdot\|}(\nabla\ell\circ W)$. Introduce a **chain rule for Rademacher complexity** (Theorem 1): for $\ell(w;x,y)=G_t(F_t(w))$, $\mathbb{E}_\epsilon\sup\|\sum\epsilon_t\nabla(G_t\circ F_t)\| \le L_F\,\mathbb{E}\sup\sum\langle\epsilon_t,\nabla G_t\rangle + L_G\,\mathbb{E}\sup\|\sum\nabla F_t\,\epsilon_t\|$, leveraging Maurer's vector contraction lemma. Combine with Pisier-type bounds ($\mathbb{E}\|\sum\epsilon_t x_t\|=O(\sqrt{n})$ in Rademacher type-2 / smooth Banach spaces) to get norm-based, dimension-free gradient convergence; extends to Hessians (Theorem 10).

## Result
- **GLM / robust regression**: $\sup_w\|\nabla\hat{L}_n(w)-\nabla L_D(w)\| \le O(C(W)/\sqrt{n})$ with $C(W)$ depending only on $\|w\|\le B$, $\|x\|\le R$, link/loss smoothness $C_\sigma$ — no $d$ dependence for $\ell_2$ or smooth-norm balls.
- Three rate regimes for GLM (Theorem 3): norm-based slow rate ($\alpha=1$, $\mu\propto B$), low-dim $\ell_2$ fast rate ($\mu\propto 1/\lambda_{\min}(\Sigma)$), sparse $\ell_\infty/\ell_1$ fast rate ($\mu\propto\|w^\star\|_0/\psi_{\min}(\Sigma)$).
- **Lower bound (Theorem 5)**: for a single ReLU, worst-case gradient Rademacher complexity is $\Omega(\sqrt{dn})$ — dimension-free uniform convergence is *impossible* for non-smooth losses without further assumptions.
- **Margin workaround (Theorem 6)**: under a soft-margin distributional assumption $\phi$, dimension-free rate is recovered.

## Why it matters here
General background; no direct arena tie. The arena problems are deterministic geometry/combinatorics optimization, not statistical learning — there is no population/empirical split, no Rademacher generalization concern. Tangential relevance only if the agent itself ever does empirical-risk-style learning on noisy verifier samples; otherwise this is off-domain.

## Open questions / connections
- Extends Mei et al. (2016) (dimension-dependent gradient/Hessian convergence) by adding norm-based capacity control — same problem class, sharper rate.
- Leaves open: structural conditions beyond soft-margin under which non-smooth (e.g. piecewise-linear) losses admit dimension-free gradient UC.
- Hessian chain rule (Theorem 10) is stated but not used here — open how much it buys for second-order / saddle-escape analyses.

## Key terms
vector-valued Rademacher complexity, Maurer contraction, chain rule Rademacher, gradient uniform convergence, Polyak-Łojasiewicz, gradient domination, norm-based capacity control, generalized linear model, robust regression, approximate stationary point, Rademacher type-2, fat-shattering dimension
