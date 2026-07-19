---
type: source
kind: paper
title: Faster Rates of Convergence to Stationary Points in Differentially Private Optimization
authors: R. Arora, Raef Bassily, Tom'as Gonz'alez, Crist'obal Guzm'an, Michael Menart, Enayat Ullah
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2206.00846
source_local: ../raw/2022-arora-faster-rates-convergence-stationary.pdf
topic: general-knowledge
cites:
---

# Faster Rates of Convergence to Stationary Points in Differentially Private Optimization

**Authors:** R. Arora, Raef Bassily, Tom'as Gonz'alez, Crist'obal Guzm'an, Michael Menart, Enayat Ullah  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2206.00846

## One-line
Improved upper and lower bounds for finding approximate stationary points (small gradient norm) of Lipschitz, smooth losses under $(\varepsilon,\delta)$-differential privacy, in both empirical (finite-sum) and population (stochastic) settings.

## Key claim
A noisy variance-reduced SpiderBoost variant attains empirical stationarity $\tilde O\!\left((\sqrt{d}/(n\varepsilon))^{2/3}\right)$, beating the previous $\tilde O\!\left((\sqrt{d}/(n\varepsilon))^{1/2}\right)$ rate of [WYX17]; for the population risk a single-pass noisy SPIDER + tree-aggregation gives $\tilde O\!\left(1/n^{1/3} + (\sqrt{d}/(n\varepsilon))^{1/2}\right)$, and in the convex case the optimal rate $\tilde\Theta\!\left(1/\sqrt{n} + \sqrt{d}/(n\varepsilon)\right)$ is achieved (matching new lower bound $\Omega(\sqrt{d}/(n\varepsilon))$ empirical and $\Omega(1/\sqrt{n})$ non-private population).

## Method
Noisy variance-reduced first-order methods (SpiderBoost / SPIDER / STORM) where Gaussian noise is scaled by $L_1\|w_t-w_{t-1}\|$ rather than the global Lipschitz constant $L_0$ — a tighter per-step sensitivity that exploits small iterate movement. Population guarantees use tree-aggregation prefix-sum estimators on a single-pass SPIDER (avoiding the missing stability-implies-generalization for gradient norm). Convex case uses recursive regularization à la [AZ18]; GLM case wraps the base DP solver inside a Johnson-Lindenstrauss subspace embedding plus a new gradient-uniform-convergence bound with only polylog dependence on the constraint radius. Lower bounds use fingerprinting codes adapted to the unconstrained DP-ERM loss.

## Result
Empirical non-convex: $\tilde O\!\left((\sqrt{d}/(n\varepsilon))^{2/3}\right)$ with oracle complexity $\tilde O\!\left(\max\{(n^5\varepsilon^2/d)^{1/3}, n\sqrt{d}/\varepsilon^2\}\right)$ (Thm. 1). Population non-convex: $\tilde O\!\left(1/n^{1/3} + (\sqrt{d}/(n\varepsilon))^{1/2}\right)$ in time linear in $n$ (Thm. 4). Convex population: optimal $\tilde\Theta(1/\sqrt n + \sqrt d/(n\varepsilon))$ (Thm. 5), tight against $\Omega(\sqrt d/(n\varepsilon))$ DP and $\Omega(1/\sqrt n)$ non-private lower bounds (Thms. 2, 7). GLM dimension-independent: $\tilde O\!\left(1/\sqrt n + \min\{(\sqrt{\text{rank}}/(n\varepsilon))^{2/3}, (1/(n\varepsilon))^{2/5}\}\right)$ (Cor. 1).

## Why it matters here
General background; no direct arena tie — this is a DP-ML optimization paper, not a math-olympiad / discrete-geometry / packing result. Its closest relevance to the agent is methodological: variance-reduced SPIDER/SpiderBoost gradient estimators and the trick of scaling noise to *iterate-difference* rather than global Lipschitz constant are reusable ideas for any noisy / stochastic first-order solver, though none of the 23 Einstein Arena problems currently need DP machinery.

## Open questions / connections
- Are the obtained rates tight in $d/n/\varepsilon$ in the non-convex setting? Paper only proves lower bounds in the convex case; non-convex sample-complexity lower bounds (beyond oracle complexity) remain open.
- Can these methods be extended to constrained settings via gradient-mapping (stronger than Frank-Wolfe gap [Lan20])? Authors defer to future work.
- Extends [WYX17, ZCH+20, BGM21, SSTT21, FSS+19, AZ18, FKT20]; corrects a proof bug in [SSTT21, Thm. 4.1].
- Open: matching lower bounds for stationary points of population risk under DP in the smooth non-convex regime.

## Key terms
differential privacy, stationary points, SpiderBoost, SPIDER, variance reduction, recursive regularization, generalized linear models, Johnson-Lindenstrauss, fingerprinting code lower bound, tree-aggregation, gradient norm, non-convex stochastic optimization, DP-ERM, uniform convergence of gradients
