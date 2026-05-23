---
type: source
kind: paper
title: A Two-Stage Fourth Order Time-Accurate Discretization for Lax-Wendroff Type Flow Solvers I. Hyperbolic Conservation Laws
authors: Jiequan Li, Zhifang Du
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1512.03664
source_local: ../raw/2015-li-two-stage-fourth-order-time-accurate.pdf
topic: general-knowledge
cites:
---

# A Two-Stage Fourth Order Time-Accurate Discretization for Lax-Wendroff Type Flow Solvers I. Hyperbolic Conservation Laws

**Authors:** Jiequan Li, Zhifang Du  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1512.03664

## One-line
A new two-stage temporal scheme that achieves fourth-order accuracy in time for hyperbolic conservation laws by building on Lax-Wendroff (L-W) type solvers instead of Runge-Kutta's four-stage approach.

## Key claim
Using a second-order L-W type solver (specifically the GRP solver) as a building block, only **two stages** are required to obtain fourth-order temporal accuracy, vs. four stages for classical R-K — saving ~20% cost in 1-D and ~30% in 2-D. The parameter set $A=1/2$, $B_0=1$, $B_1=0$, $C_0=1/3$, $C_1=2/3$ is uniquely determined by the accuracy conditions.

## Method
Two-stage Hermite-type quadrature of $u_{n+1} = u_n + \int_{t_n}^{t_n+\Delta t} L(u)\,dt$ using both $L(u)$ and $\partial_t L(u)$ at $t_n$ and at the midpoint $t_n + \Delta t/2$, where $\partial_t L = (\partial L/\partial u) \cdot L$ comes from the Cauchy-Kovalevskaya / chain rule. Spatial reconstruction via fifth-order HWENO; instantaneous values $(u, \partial_t u)$ at cell boundaries supplied by an analytic GRP (generalized Riemann problem) solver. Extends to 2-D rectangular finite volume via a quasi-1-D GRP treating tangential flux as source.

## Result
Numerical experiments (scalar conservation laws, 1-D/2-D compressible Euler — isentropic vortex, shock-turbulence interaction, Woodward-Colella, large pressure ratio, 2-D Riemann problems, double Mach reflection, shock-vortex interaction) confirm fourth-order convergence and demonstrate that GRP4-HWENO5 matches or exceeds RK4-WENO5 sharpness, sometimes succeeding where RK4-WENO5 fails (e.g., large pressure ratio with 400 cells). CFL number can exceed $1/2$ for non-strong waves without losing accuracy.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems involve time-dependent PDEs or CFD; this paper concerns finite-volume hyperbolic solver design, orthogonal to sphere packing / kissing numbers / autocorrelation / extremal combinatorics. Possible distant analogy: the Hermite-vs-Simpson framing (use derivative info to halve the stages) might inspire optimization-iteration design, but the connection is speculative.

## Open questions / connections
- Numerical stability theory for the two-stage L-W scheme is left open.
- Extension to DG formulation and Navier-Stokes promised in companion paper (Du & Li, in prep) — viscous compressible flow.
- Whether the "use derivative to halve stages" idea generalizes outside PDE time-stepping to other iterative numerical procedures.

## Key terms
Lax-Wendroff scheme, generalized Riemann problem, GRP solver, Cauchy-Kovalevskaya, Runge-Kutta, HWENO, WENO, hyperbolic conservation laws, finite volume method, compressible Euler equations, two-stage fourth-order, ADER solver
