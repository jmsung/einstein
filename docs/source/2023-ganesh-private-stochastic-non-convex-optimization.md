---
type: source
kind: paper
title: "Private (Stochastic) Non-Convex Optimization Revisited: Second-Order Stationary Points and Excess Risks"
authors: Arun Ganesh, Daogao Liu, Sewoong Oh, Abhradeep Thakurta
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.09699
source_local: ../raw/2023-ganesh-private-stochastic-non-convex-optimization.pdf
topic: general-knowledge
cites:
---

# Private (Stochastic) Non-Convex Optimization Revisited: Second-Order Stationary Points and Excess Risks

**Authors:** Arun Ganesh, Daogao Liu, Sewoong Oh, Abhradeep Thakurta  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.09699

## One-line
Improves differentially private non-convex optimization by giving sharper rates for finding approximate second-order stationary points (SOSP) and tighter excess-risk bounds via the regularized exponential mechanism.

## Key claim
Algorithm 1 (Stochastic Spider) finds an $\alpha$-SOSP with $\alpha = \tilde O((\sqrt{d}/n)^{2/3})$ on the empirical risk and $\alpha = \tilde O(n^{-1/3} + (\sqrt{d}/n)^{3/7})$ on the population risk under $(\varepsilon,\delta)$-DP, beating the prior SOTA $\min\{(\sqrt{d}/n)^{1/2},(d/n)^{4/7}\}$ of [WCX19]; a regularized exponential mechanism achieves excess population risk $O(GDd\log\log(n)\sqrt{\log(1/\delta)}/(\varepsilon\log(nd)))$ without smoothness, and an exponential-time exponential mechanism attains the nearly tight bound $\tilde\Theta(d/(\varepsilon n) + \sqrt{d/n})$.

## Method
A variance-reduced SpiderBoost-style framework using two gradient oracles: $\mathcal{O}_1$ (accurate, costly, full-gradient estimate) and $\mathcal{O}_2$ (cheap difference estimator $\nabla f(x_t) - \nabla f(x_{t-1})$). Instead of refreshing on a fixed schedule, the algorithm tracks a *drift* $\sum \|x_i - x_{i-1}\|^2$ and only invokes $\mathcal{O}_1$ when the drift exceeds a threshold $\kappa$ — bounding cumulative gradient-estimation error via norm-subGaussian Hoeffding inequalities. For excess risk, sample from $\exp(-\beta(F_D(x) + \tfrac{\mu}{2}\|x\|^2))$; privacy follows from Log-Sobolev Inequality + Holley–Stroock perturbation, and generalization from the LSI-induced Talagrand $W_2$ transport bound.

## Result
- Empirical SOSP: $\alpha = \tilde O((\sqrt{d}/n)^{2/3})$ (Theorem 3.9), improving on all parameter regimes vs $\min\{(\sqrt{d}/n)^{1/2}, (d/n)^{4/7}\}$.
- Population SOSP: $\alpha = \tilde O(n^{-1/3} + (\sqrt{d}/n)^{3/7})$ (Theorem 3.12) — first private population guarantee for SOSP.
- Excess risk (poly-time): $O(GDd\log\log(n)\sqrt{\log(1/\delta)}/(\varepsilon\log(nd)))$ without smoothness (Theorem 4.6/4.7).
- Excess population risk (exp-time): nearly matching upper/lower bound $\tilde\Theta(d/(\varepsilon n) + \sqrt{d/n})$ (Theorem 4.8).
Gap remains: a factor $(\sqrt{d}/n)^{-1/6}$ to the known $\Omega(\sqrt{d}/n)$ lower bound [ABG+22].

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems involve differential privacy or stochastic ERM. Marginally relevant as background on variance-reduced stochastic optimizers (SpiderBoost / drift-triggered oracle switching) and on LSI-based sampling analyses, which only loosely touch the project's interest in basin-hopping / parallel tempering convergence.

## Open questions / connections
- Closing the $(\sqrt{d}/n)^{-1/6}$ upper/lower gap for private SOSP rates.
- Whether the drift-triggered oracle-switching idea generalizes to non-private variance-reduced solvers (cheaper batched-gradient + full-gradient hybrid schedules).
- Extends SpiderBoost [WJZ+19], private SpiderBoost [ABG+22], and the exponential-mechanism non-convex bounds of [GTU22, WCX19].

## Key terms
differential privacy, non-convex optimization, second-order stationary point, SOSP, SpiderBoost, variance reduction, exponential mechanism, Log-Sobolev inequality, Holley-Stroock perturbation, norm-subGaussian, stochastic gradient, excess population risk
