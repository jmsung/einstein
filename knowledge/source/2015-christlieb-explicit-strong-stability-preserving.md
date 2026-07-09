---
type: source
kind: paper
title: Explicit Strong Stability Preserving Multistage Two-Derivative Time-Stepping Schemes
authors: A. Christlieb, S. Gottlieb, Zachary J. Grant, David C. Seal
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1504.07599
source_local: ../raw/2015-christlieb-explicit-strong-stability-preserving.pdf
topic: general-knowledge
cites:
---

# Explicit Strong Stability Preserving Multistage Two-Derivative Time-Stepping Schemes

**Authors:** A. Christlieb, S. Gottlieb, Zachary J. Grant, David C. Seal  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1504.07599

## One-line
Constructs explicit strong-stability-preserving (SSP) time integrators that use two derivatives ($F$ and $\dot F$) per stage, breaking the fourth-order barrier that limits explicit SSP Runge–Kutta methods.

## Key claim
Explicit multistage two-derivative SSP methods can achieve order $p=5$ in just three stages, exceeding the well-known $p \le 4$ ceiling for explicit SSP Runge–Kutta methods. Sufficient SSP conditions are derived, and optimal methods up to order 5 are tabulated with SSP coefficients $C$ depending on the second-derivative constant $K$ (e.g., a 3-stage 5th-order method exists with $C>0$).

## Method
Given a forward-Euler base condition $\|u^n + \Delta t F(u^n)\| \le \|u^n\|$ for $\Delta t \le \Delta t_{FE}$ and a second-derivative condition $\|u^n + \Delta t^2 \dot F(u^n)\| \le \|u^n\|$ for $\Delta t \le K\Delta t_{FE}$, the multistage two-derivative scheme is rewritten as a convex combination of forward Euler and Taylor building blocks. The SSP coefficient $C = \max r$ is obtained by solving an optimization with componentwise nonnegativity constraints on $(I + rS + (r^2/K^2)\hat S)^{-1}$ acted on $e$, $S$, $\hat S$. A Lax–Wendroff approach replaces $\dot F = F_u F$ with a separate spatial discretization of $U_{tt}$.

## Result
- Unique 2-stage 4th-order method (eq. 10) with $C \approx 0.6788$ at $K=\sqrt{2}/2$ (sharp vs. direct TVD bound $\sqrt{3}-1$).
- 2-stage 3rd-order family with closed-form coefficients parameterized by $(r,K)$; e.g., $C\approx 1.04$ at $K=\sqrt{1/2}$, growing to $C\approx 1.56$ at $K=4$.
- 3-stage 4th-order methods with $C$ from $1.146$ ($K=1/2$) up to $1.62$ ($K=1$).
- 3-stage 5th-order SSP method exists — first explicit SSP scheme of order $>4$ in this class.
- Numerical convergence (WENO5/7/9 + pseudospectral) verifies design order despite $\dot F \ne F_t$, provided spatial error stays subdominant.

## Why it matters here
General background; no direct arena tie. The paper is on time-integration for hyperbolic PDEs, not on the combinatorial / packing / extremal-graph problems Einstein Arena targets — it would only be relevant if a future arena problem required ODE/PDE simulation as a sub-routine.

## Open questions / connections
- Can the SSP order barrier be pushed further (order 6+) with three or four derivatives?
- Alternative base conditions (Taylor-series condition (15) of Nguyen-Ba et al.) yield more restrictive but possibly simpler optimization landscapes — when is each preferable?
- Designing spatial discretizations that natively satisfy the second-derivative condition (12) with large $K$ remains open (WENO+/WENO− cascade is a heuristic).

## Key terms
strong stability preserving, SSP coefficient, multistage two-derivative methods, Runge-Kutta, Taylor series method, Lax-Wendroff, WENO, hyperbolic conservation laws, total variation diminishing, order barrier, convex combination decomposition, Shu-Osher form
