---
type: source
kind: paper
title: Simple and optimal high-probability bounds for strongly-convex stochastic gradient descent
authors: Nicholas J. A. Harvey, Christopher Liaw, Sikander Randhawa
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.00843
source_local: ../raw/2019-harvey-simple-optimal-high-probability-bounds.pdf
topic: general-knowledge
cites:
---

# Simple and optimal high-probability bounds for strongly-convex stochastic gradient descent

**Authors:** Nicholas J. A. Harvey, Christopher Liaw, Sikander Randhawa  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.00843

## One-line
Proves that the simple non-uniform iterate average of SGD (weight $\propto t$) achieves the optimal $O(1/T)$ convergence rate with high probability for non-smooth strongly-convex objectives.

## Key claim
For $\mu$-strongly-convex, $L$-Lipschitz $f$ with step size $\eta_t = 2/(\mu(t+1))$, the weighted average $\sum_t \tfrac{2t}{T(T+1)} x_t$ satisfies $f(\bar x) - f(x^*) \le O\!\big(\tfrac{(L+1)^2}{\mu} \cdot \tfrac{\log(1/\delta)}{T}\big)$ with probability $\ge 1-\delta$, and a matching $\Omega(\log(1/\delta)/T)$ lower bound holds with probability $\ge \delta$.

## Method
Standard projected SGD analysis (Lacoste-Julien et al.) is combined with a Generalized Freedman inequality (Harvey et al. 2018) that handles martingales whose total conditional variance is itself bounded by a linear combination of the martingale increments — the "chicken-and-egg" recursive TCV property. Lemmas 4.4–4.5 (adapted from Rakhlin et al.) give a recursive bound $\|x_{t+1}-x^*\|^2 \le \sum a_i(t)\langle \hat z_i, x_i-x^*\rangle + \sum b_i(t)\|\hat g_i\|^2$ that feeds the Freedman application. Lower bound uses a 1-D construction $f(x)=x^2/2$ with a Rademacher-noise gradient oracle and a reverse Chernoff bound from Klein–Young.

## Result
Theorem 3.1: $O\!\big(\tfrac{L^2}{\mu}\cdot\tfrac{\log(1/\delta)}{T}\big)$ high-probability error for the non-uniform average; Claim 3.3: tight $\Omega(\log(1/\delta)/(9T))$ matching lower bound. Theorem C.3 extends to $\kappa$-subgaussian (not just bounded) gradient noise with rate $O\!\big(\tfrac{(L+\kappa)^2}{\mu}\cdot\tfrac{\log(1/\delta)}{T}\big)$. Experiments on cina0/protein/rcv1/covtype/quantum SVM problems show suffix-average and non-uniform-average dominate final-iterate and uniform-average in both mean and concentration.

## Why it matters here
General background; no direct arena tie. Could marginally inform any internal SGD-based optimizer used in the agent stack (e.g. neural surrogate training), but none of the 23 Einstein Arena problems are stochastic-convex-optimization in form — they are deterministic geometric/extremal optimization where the relevant tools are LP/SDP, basin-hopping, mpmath polish, parallel tempering.

## Open questions / connections
- Does the recursive TCV property generalize to other non-smooth iterative schemes (e.g. subgradient methods on the dual of an LP)?
- Last-iterate high-probability bound for strongly-convex SGD with unknown horizon — Jain et al. 2019 only does the known-horizon case.
- Connection to high-probability bounds for non-convex (e.g. SDP) stochastic methods used in flag-algebra solvers.

## Key terms
stochastic gradient descent, SGD, strongly convex, non-smooth optimization, suffix averaging, non-uniform averaging, Lacoste-Julien, Rakhlin, Generalized Freedman inequality, martingale concentration, total conditional variance, high-probability bounds, subgaussian noise
