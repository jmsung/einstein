---
type: source
kind: paper
title: Step Sizes for Strong Stability Preservation with Downwind-Biased Operators
authors: D. Ketcheson
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1105.5798
source_local: ../raw/2011-ketcheson-step-sizes-strong-stability.pdf
topic: general-knowledge
cites:
---

# Step Sizes for Strong Stability Preservation with Downwind-Biased Operators

**Authors:** D. Ketcheson  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1105.5798

## One-line
Establishes tight bounds on the maximum stable step size (SSP coefficient $\tilde{C}$) for time integrators that combine upwind- and downwind-biased spatial discretizations of hyperbolic PDEs.

## Key claim
For explicit downwind Runge–Kutta methods $\tilde{C} \le s$ (number of stages); for linear multistep methods of order $> 1$, $\tilde{C} \le 2$; but implicit two-stage second-order downwind RK methods can achieve **arbitrarily large** $\tilde{C}$ — a class with $\tilde{C} = r$ is constructed explicitly for any finite $r > 2 + \sqrt{2}$.

## Method
Shu–Osher form analysis: rewrite each method as a convex-combination of forward-Euler steps applied to $F$ and $\tilde{F}$ with non-negative coefficients, then combine the positivity conditions with the order-of-accuracy conditions. The upper bounds (Theorems 2.1, 2.2) drop out of inequalities on $\sum \gamma_{jl}(j-2l)$ and a quadratic-in-$(k-j)$ identity; the unbounded family (Theorem 2.3) is proved by explicit construction (eq. 22) and shown to be A-stable.

## Result
Three theorems: (1) explicit downwind RK has $\tilde{C} \le s$; (2) order-$\ge 2$ downwind linear multistep has $\tilde{C} \le 2$; (3) a two-parameter family of two-stage, second-order, A-stable implicit downwind RK methods attains any $\tilde{C} = r$. Numerical tests (WENO5 + advection, Burgers) at $\mathrm{CFL}=6.5$–$8$ confirm second-order convergence and demonstrate the method outperforms backward Euler and trapezoidal RK on shocks, provided $r \Delta x^q \ll \Delta t$ to avoid a diffusive $O(r \Delta x^q \Delta t)$ one-step error from $L - \tilde{L} \approx \Delta x\, \partial_{xx}$.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems involves time-stepping hyperbolic PDEs — the SSP framework is for numerical PDE integrators, not the kinds of static optimization (sphere packing, autocorrelation, kissing numbers, extremal combinatorics) the agent works on.

## Open questions / connections
- Do higher-than-second-order downwind RK methods with large $\tilde{C}$ exist? (Author reports preliminary affirmative evidence.)
- Do diagonally implicit (DIRK) downwind methods with large $\tilde{C}$ exist? (A search by the author found none for 2-stage 2nd-order.)
- Efficient nonlinear solves for implicit WENO at large CFL remain open — the Newton-Krylov / fsolve approach used here limited tests to $\mathrm{CFL} \approx 6.5$.

## Key terms
strong stability preserving, SSP coefficient, downwind biased discretization, Runge-Kutta methods, linear multistep methods, total variation diminishing, TVD, Shu-Osher form, CFL number, WENO, hyperbolic conservation laws, A-stability, monotonicity, Ketcheson, Lenferink, Spijker
