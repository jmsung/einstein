---
type: source
kind: paper
title: Extragradient Method with Variance Reduction for Stochastic Variational Inequalities
authors: A. Iusem, A. Jofré, R. Oliveira, Philip Thompson
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.00260
source_local: ../raw/2017-iusem-extragradient-method-variance-reduction.pdf
topic: general-knowledge
cites:
---

# Extragradient Method with Variance Reduction for Stochastic Variational Inequalities

**Authors:** A. Iusem, A. Jofré, R. Oliveira, Philip Thompson  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.00260

## One-line
An extragradient stochastic-approximation method for pseudo-monotone stochastic variational inequalities (SVI) that uses iterative variance reduction (mini-batch averaging with growing sample size $N_k$) to achieve $O(1/K)$ convergence with near-optimal $O(\epsilon^{-2})$ oracle complexity.

## Key claim
For pseudo-monotone Lipschitz SVIs — even with unbounded feasible set $X$, unbounded operator, and non-uniform oracle variance — the method attains $E[r_\alpha(x^K)^2] \le Q/K$ in the squared natural residual (and D-gap), versus the prior best $O(1/\sqrt{K})$ rate, while keeping oracle complexity $O(\epsilon^{-2})$ up to a log factor and producing iterates uniformly bounded in $L^p$ when the stochastic error has finite $p$-th moment.

## Method
Korpelevich-style extragradient with two projections per iteration, but each operator evaluation is replaced by an empirical average of $N_k$ i.i.d. oracle samples: $z^k = \Pi[x^k - (\alpha_k/N_k)\sum_j F(\xi^k_j, x^k)]$ then $x^{k+1} = \Pi[x^k - (\alpha_k/N_k)\sum_j F(\eta^k_j, z^k)]$. Stepsizes $\alpha_k$ are bounded away from zero (unlike classical SA's diminishing $\alpha_k$); sample rate grows as $N_k = O(k (\ln k)^{1+b})$. Analysis uses Burkholder–Davis–Gundy martingale moment inequalities and the Robbins–Siegmund supermartingale convergence theorem.

## Result
Under pseudo-monotonicity + Lipschitz + finite-variance oracle (possibly $x$-dependent variance $\sigma(x)$), the algorithm achieves: (i) a.s. convergence of $d(x^k, X^*) \to 0$ and $r_\alpha(x^k) \to 0$ in $L^2$; (ii) rate $E[r_\alpha(x^K)^2] \le Q(x^*)/K$ with constants depending on the $x^* \in X^*$ minimizing the trade-off between $\sigma(x^*)^2$ and $\|x^0-x^*\|$; (iii) total oracle complexity $\sum_{k=1}^K 2N_k = O(\epsilon^{-(2+a)} \ln(\epsilon^{-1})^{1+b})$ for any $a>0$; (iv) sharper constants under uniform variance over $X^*$ or $X$, with bounds depending on $d(x^0, X^*)$ rather than $\mathrm{diam}(X)$. Extends to distributed Cartesian SVIs (multi-agent Nash / multi-user optimization) with linear-in-$m$ oracle scaling.

## Why it matters here
General background; no direct arena tie. Stochastic VI / extragradient theory is far from the deterministic geometric-optimization problems (sphere packing, kissing, autocorrelation) on Einstein Arena; the agent's optimizers (L-BFGS, NM, SLSQP, basin-hopping, parallel tempering, mpmath polish) operate on deterministic non-convex objectives, not noisy expected-value operators.

## Open questions / connections
- Sharp exponential-convergence complexity under non-uniform tail bounds (paper flags as future work).
- Whether plain (extra)gradient methods with robust stepsizes — without explicit variance reduction — can match the accelerated stochastic rate.
- Error-bound conditions (semi-stable VIs, polyhedral strongly monotone, linear-cone) under which $r_\alpha$ controls $d(x, X^*)$, extending the $O(1/K)$ rate to mean-squared distance for new SVI classes.

## Key terms
stochastic variational inequality, extragradient method, Korpelevich, variance reduction, stochastic approximation, pseudo-monotone operator, natural residual, D-gap function, oracle complexity, mini-batch SA, Burkholder-Davis-Gundy, Cartesian variational inequality
