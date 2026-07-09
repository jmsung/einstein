---
type: source
kind: paper
title: "Second-Order Information in Non-Convex Stochastic Optimization: Power and Limitations"
authors: Yossi Arjevani, Y. Carmon, John C. Duchi, Dylan J. Foster, Ayush Sekhari, Karthik Sridharan
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.13476
source_local: ../raw/2020-arjevani-second-order-information-non-convex-stochastic.pdf
topic: general-knowledge
cites:
---

# Second-Order Information in Non-Convex Stochastic Optimization: Power and Limitations

**Authors:** Yossi Arjevani, Y. Carmon, John C. Duchi, Dylan J. Foster, Ayush Sekhari, Karthik Sridharan  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.13476

## One-line
Characterizes the stochastic oracle complexity of finding approximate stationary points in non-convex optimization, proving that second-order information yields a sharp improvement but higher orders ($p>2$) do not.

## Key claim
For functions with Lipschitz gradient and Hessian, an $\epsilon$-stationary point can be found with $O(\epsilon^{-3})$ stochastic gradient + Hessian-vector-product (HVP) queries using single-point oracles, and this rate is tight — $\Omega(\epsilon^{-3})$ holds for *every* stochastic $p$th-order method with $p\ge 2$, producing an "elbow" at $p=2$ (vs. the smooth $\epsilon^{-(1+1/p)}$ scaling in the noiseless case).

## Method
A new variance-reduced gradient estimator (HVP-RVR) replaces the standard two-point difference $\nabla F(x,z)-\nabla F(x',z)$ with an HVP-integral approximation $\frac{1}{K}\sum_k \nabla^2 F(x^{(k)},z^{(k)})(x-x')$, plugged into recursive variance reduction with a stateless Bernoulli-reset schedule and a dynamic batch size $K\propto\|x-x'\|^2$ to control bias. Lower bounds extend the "probabilistic zero-chain" construction of Arjevani et al. (2019) to higher-order derivative estimators, carefully scaled to meet simultaneous Lipschitz and variance constraints.

## Result
**Upper:** $\tilde O\!\left(\frac{\Delta\sigma_1\sigma_2}{\epsilon^3}+\frac{\Delta L_2^{1/2}\sigma_1}{\epsilon^{2.5}}+\frac{\Delta L_1}{\epsilon^2}\right)$ stochastic gradient + HVP queries (Algorithm 2, SGD with HVP-RVR). For $(\epsilon,\gamma)$-SOSPs: $O(\epsilon^{-3}+\epsilon^{-2}\gamma^{-2}+\gamma^{-5})$ upper, matching $\Omega(\epsilon^{-3}+\gamma^{-5})$ lower (novel even in the noiseless case, where it becomes $\Omega(\epsilon^{-1.5}+\gamma^{-3})$, matching cubic-regularized Newton).

## Why it matters here
General background on the limits of stochastic non-convex optimization — relevant when the Einstein agent considers HVP-based variance reduction for noisy objectives (e.g., Monte-Carlo-estimated arena scores), but no direct tie to any of the 23 problems, all of which use deterministic objectives. Adds the meta-lesson: when an evaluator is *deterministic*, higher-order smoothness compounds ($\epsilon^{-(1+1/p)}$); when noisy, $p>2$ buys nothing — informs `compute-router` choices.

## Open questions / connections
- Extends Arjevani et al. (2019a) lower bounds and Carmon et al. (2019a) high-order constructions; the $\Omega(\gamma^{-5})$ bound for SOSPs is new even noiselessly.
- Gap remains in the SOSP regime $\epsilon^{2/3}\ll\gamma\ll\epsilon^{1/2}$ where upper and lower bounds don't match.
- Lower bounds proven for zero-respecting algorithms; extension to general randomized algorithms left open.

## Key terms
non-convex stochastic optimization, stationary point, second-order stationary point, Hessian-vector product, variance reduction, recursive variance reduction, oracle complexity, lower bound, zero-respecting algorithm, probabilistic zero-chain, cubic-regularized Newton, Lipschitz Hessian
