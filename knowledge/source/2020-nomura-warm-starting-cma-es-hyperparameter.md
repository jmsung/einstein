---
type: source
kind: paper
title: Warm Starting CMA-ES for Hyperparameter Optimization
authors: M. Nomura, Shuhei Watanabe, Youhei Akimoto, Yoshihiko Ozaki, Masaki Onishi
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2012.06932
source_local: ../raw/2020-nomura-warm-starting-cma-es-hyperparameter.pdf
topic: general-knowledge
cites:
---

# Warm Starting CMA-ES for Hyperparameter Optimization

**Authors:** M. Nomura, Shuhei Watanabe, Youhei Akimoto, Yoshihiko Ozaki, Masaki Onishi  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2012.06932

## One-line
Initialize CMA-ES's multivariate Gaussian from a "promising distribution" estimated on a related source task so the costly $\Theta(d^2)$ covariance-adaptation phase is skipped under tight evaluation budgets.

## Key claim
On HPO under severely limited budgets (~25–50 evaluations) WS-CMA-ES converges faster than vanilla CMA-ES, GP-EI, TPE, MTBO, and MT-BOHAMIANN, and the empirical speedup correlates with a new $\gamma$-similarity measure $s(\gamma_1,\gamma_2) := D_{KL}(P_*\|P_{\gamma_2}^2) - D_{KL}(P_{\gamma_1}^1\|P_{\gamma_2}^2)$.

## Method
Define a $\gamma$-promising distribution $p_\gamma(x) \propto \int_{\mathbf{1}\{x' \in F_\gamma\}} \exp(-\|x-x'\|^2/(2\alpha^2))\,dx'$ on the top-$\gamma$ level set $F_\gamma$. Estimate it empirically from source-task observations as a GMM over the top $\gamma N$ points, then initialize CMA-ES's $(m,\Sigma)$ by KL-minimization against that GMM, giving closed-form $m^* = \tfrac{1}{N_\gamma}\sum x_i$ and $\Sigma^* = \alpha^2 I + \tfrac{1}{N_\gamma}\sum (x_i-m^*)(x_i-m^*)^\top$ (Runnalls 2007). A diagonal variant WS-sep-CMA-ES uses $l_j = \alpha^2 + \tfrac{1}{N_\gamma}\sum ([x_i]_j-[m^*]_j)^2$.

## Result
Defaults $\alpha=\gamma=0.1$ are robust across $\alpha,\gamma \in [0.05,0.25]$. On synthetic sphere and rotated-ellipsoid problems the performance gap $\bar f^{cma}_{best} - \bar f^{ws}_{best}$ tracks $\gamma$-similarity sign-for-sign. Unlike naive transfer (ReuseNormal, ReuseGMM) which collapses when source and target offsets diverge, WS-CMA-ES degrades gracefully because CMA-ES still adapts away from a wrong initialization. On MLP/MNIST→Fashion-MNIST and CNN/SVHN→CIFAR-10 transfers WS-CMA-ES beats baselines within ~25–30 evaluations.

## Why it matters here
General background; no direct arena tie. Of possible interest to the [compute-router](../wiki/techniques/compute-router.md) for warm-starting CMA-ES restarts on float-precision-sensitive problems (P5, P6, P11, P14, P17) where a prior basin from a cheaper evaluator could initialize Modal float64 CMA-ES — but the BBO targets here (HPO, $d \le 10$, 25–50 evals) are far from arena geometry.

## Open questions / connections
- Can a "source task" be a coarser-tolerance or float32 run of the *same* arena problem, used to warm-start a float64 polish? — bridges with [triple-verify](../../.claude/rules/triple-verify.md) by reusing the cheap-evaluator pass productively.
- Automatic detection of $s(\gamma_1,\gamma_2) < 0$ and fallback to vanilla CMA-ES — explicit limitation noted by authors; relevant any time a basin-hopping restart is seeded from a stale solution.
- Relation to the regularization term $\alpha^2 I$ in $\Sigma^*$ and CMA-ES's own $\sigma$-decoupling: does $\alpha$ subsume the role of an inflated initial $\sigma$?

## Key terms
CMA-ES, warm starting, covariance matrix adaptation, multivariate Gaussian, KL divergence, Kullback-Leibler, Gaussian mixture model, hyperparameter optimization, transfer learning, promising distribution, task similarity, sep-CMA-ES, Bayesian optimization, Nomura, Hansen
