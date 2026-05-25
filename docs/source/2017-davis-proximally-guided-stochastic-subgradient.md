---
type: source
kind: paper
title: Proximally Guided Stochastic Subgradient Method for Nonsmooth, Nonconvex Problems
authors: Damek Davis, Benjamin Grimmer
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1707.03505
source_local: ../raw/2017-davis-proximally-guided-stochastic-subgradient.pdf
topic: general-knowledge
cites:
---

# Proximally Guided Stochastic Subgradient Method for Nonsmooth, Nonconvex Problems

**Authors:** Damek Davis, Benjamin Grimmer  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1707.03505

## One-line
First convergence-rate analysis of a stochastic subgradient method for nonsmooth nonconvex losses, using an inexact proximal-point outer loop on $\rho$-weakly convex functions.

## Key claim
For $\rho$-weakly convex $F$ (i.e., $F + \tfrac{\rho}{2}\|\cdot\|^2$ convex), PGSG produces $\bar{x}$ with $\mathbb{E}\,\mathrm{dist}(\bar{x}, \{x : \mathrm{dist}(0,\partial F(x))^2 \le \varepsilon\})^2 \le \varepsilon$ in $O(\Delta L^2 \varepsilon^{-2})$ stochastic subgradient evaluations — matching the smooth nonconvex rate of Ghadimi–Lan–Zhang.

## Method
Inexact proximal-point outer loop: $x_{t+1} \approx \arg\min_x F(x) + \tfrac{1}{2\gamma}\|x-x_t\|^2$ with $\gamma < 1/\rho$, so each subproblem is $\mu = \gamma^{-1}-\rho$ strongly convex. The inner loop (PSSM) is a projected stochastic subgradient method tuned for strong convexity with weighted-average output and stepsizes $\alpha_j = (\mu(j+2+36/(\gamma^4\mu^4(j+1))))^{-1}$. A two-phase variant (2PGSG) runs $S = \log_2(2/\Lambda)$ independent copies and picks the candidate with smallest proxy step $\|x_R - \tilde{x}_R\|$ to sharpen tail bounds; a parameter-free variant (PFPGSG) lets $\gamma_t = (t+1)^{-\beta}$, $j_t = t+44$ without knowing $\rho$.

## Result
Stationarity measured via $\|x_t - \hat{x}_t\|/\gamma$ where $\hat{x}_t$ is the (unobserved) prox point; Lemma 3.2 converts this into nearness to an actual near-stationary point. PGSG: $O(\varepsilon^{-2})$ oracle calls for expected $\varepsilon$-near-near-stationarity. 2PGSG sharpens the high-probability $(\varepsilon,\Lambda)$-bound from $O(\varepsilon^{-2}\Lambda^{-2})$ to $O(\log(1/\Lambda)\varepsilon^{-2} + \log(1/\Lambda)\varepsilon^{-1}\Lambda^{-1})$. PFPGSG attains $O(T^{1-\beta})$ rate without $\rho$. Class covers convex composites $h \circ c$ ($\beta L$-weakly convex), additive composites $g+r$, robust phase retrieval (2-weakly convex, proved here), nonsmooth trimmed estimation ($L$-weakly convex, proved here), and censored block models.

## Why it matters here
General background; no direct arena tie — this is foundational stochastic-optimization theory for nonsmooth nonconvex losses, not a math-olympiad / combinatorial result. The weak-convexity framework and prox-point-as-stationarity measure could inform any Einstein Arena problem whose objective is a nonsmooth composite (e.g., robust phase-retrieval-style or trimmed-loss formulations of packing/autocorrelation problems), but it does not directly bear on LP/SDP bounds, equioscillation, or any of the 23 problems' current optimizer stacks.

## Open questions / connections
- Can the $O(\varepsilon^{-2})$ rate be improved to the $O(\varepsilon^{-3/2})$ now known in smooth nonconvex (Fang et al. SPIDER 2018) for the weakly convex case?
- The standard SGD-on-weakly-convex analysis (Davis–Drusvyatskiy 2018, arXiv:1802.02988 / 1803.06523) achieves the same expectation rate without the inner-outer structure — when does the prox guidance still pay off (variance reduction, parameter-free settings)?
- The natural stationarity surrogate $\|x_t-\hat{x}_t\|/\gamma$ is never directly computable; the paper's $\|x_R - \tilde{x}_R\|$ proxy is heuristic — tighter computable certificates?

## Key terms
weakly convex, prox-regular, stochastic subgradient method, inexact proximal point, Moreau envelope, strongly convex inner subproblem, convex composite optimization, additive composite, robust phase retrieval, trimmed estimation, censored block model, nonsmooth nonconvex optimization, $(\varepsilon,\Lambda)$-solution, variance reduction, Ghadimi-Lan-Zhang, Davis-Drusvyatskiy
