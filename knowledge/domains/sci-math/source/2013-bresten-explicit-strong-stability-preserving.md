---
type: source
kind: paper
title: Explicit strong stability preserving multistep Runge-Kutta methods
authors: Christopher Bresten, S. Gottlieb, Zachary J. Grant, Daniel Higgs, D. Ketcheson, A. Németh
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1307.8058
source_local: ../raw/2013-bresten-explicit-strong-stability-preserving.pdf
topic: general-knowledge
cites:
---

# Explicit strong stability preserving multistep Runge-Kutta methods

**Authors:** Christopher Bresten, S. Gottlieb, Zachary J. Grant, Daniel Higgs, D. Ketcheson, A. Németh  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1307.8058

## One-line
Constructs and analyzes explicit multistep Runge–Kutta (MSRK) time integrators that preserve forward-Euler strong stability properties (TVD, positivity) under the largest possible CFL-like time-step.

## Key claim
For any $s \geq 0$, $k > 1$, the optimal SSP threshold factor for explicit $s$-stage, $k$-step, second-order general linear methods is exactly $R_{s,k,2} = \frac{(k-2)s + \sqrt{(k-2)^2 s^2 + 4 s(s-1)(k-1)}}{2(k-1)}$, and optimized MSRK methods up to 5 steps / 8 stages / order 10 are tabulated, surpassing the order-8 barrier for two-step methods.

## Method
Writes MSRK methods in the Spijker matrix form $w = Sx + \Delta t\, T f$ and characterizes SSP via componentwise nonnegativity of $R = (I+rT)^{-1}S$ and $P = r(I+rT)^{-1}T$. Derives Albrecht-style order conditions exploiting stage-order $\geq \lfloor (p-1)/2 \rfloor$ to reduce variables, then runs MATLAB `fmincon` on the resulting nonconvex constrained optimization. The sharp second-order upper bound is proved by reducing to a quadratic in the radius of absolute monotonicity of stability polynomials and showing extremal weight concentration at $(1,s)$ and $(k,0)$.

## Result
Optimal closed-form $R_{s,k,2}$ established and shown tight within the MSRK class. Tables of effective SSP coefficients $C_{\text{eff}} = C/s$ for orders 2–10, steps $k=2..5$, stages $s$ up to ~20; many entries match certified upper bounds. Numerical tests on linear advection and Buckley–Leverett confirm observed TVD/positivity time-steps exceed theoretical SSP bounds and grow with $s$ as predicted; positivity time-step consistently exceeds TVD time-step.

## Why it matters here
General background; no direct arena tie — SSP time integration is for hyperbolic PDE numerics, unrelated to the discrete-geometry / packing / extremal-combinatorics problems on Einstein Arena. The only transferable idea is the radius-of-absolute-monotonicity reformulation as a constrained quadratic, which is a generic LP/quadratic-relaxation pattern already covered elsewhere in the wiki.

## Open questions / connections
- Whether the odd-order saturation in $k_0$ (steps stop helping past some threshold) persists for $p > 5$ — paper leaves this empirically open.
- Optimizer gets stuck in local minima for high-order, many-stage cases; certified global optima missing for several table entries.
- Extends Spijker's [34] monotonicity theory and two-step work of Ketcheson–Gottlieb–Macdonald [22] to arbitrary $k$.

## Key terms
strong stability preserving, SSP coefficient, multistep Runge-Kutta, MSRK, radius of absolute monotonicity, threshold factor, TVD time discretization, positivity preserving, forward Euler convex combination, Shu-Osher, Spijker theory, hyperbolic conservation laws
