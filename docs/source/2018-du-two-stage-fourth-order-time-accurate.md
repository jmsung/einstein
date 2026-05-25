---
type: source
kind: paper
title: A two-stage fourth order time-accurate discretization for Lax-Wendroff type flow solvers II. High order numerical boundary conditions
authors: Zhifang Du, Jiequan Li
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1801.00990
source_local: ../raw/2018-du-two-stage-fourth-order-time-accurate.pdf
topic: general-knowledge
cites:
---

# A two-stage fourth order time-accurate discretization for Lax-Wendroff type flow solvers II. High order numerical boundary conditions

**Authors:** Zhifang Du, Jiequan Li  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1801.00990

## One-line
Constructs fourth-order-accurate numerical boundary conditions for the two-stage fourth-order finite-volume scheme (based on Lax–Wendroff/GRP flow solvers) for hyperbolic conservation laws.

## Key claim
A fourth-order boundary treatment can be built using only the Jacobian $\partial f/\partial u$ (a single application of the inverse Lax–Wendroff substitution $\partial u/\partial x = -(\partial f/\partial u)^{-1}\partial u/\partial t$), avoiding the high-rank tensor differentiations of the original ILW; the theoretical boundary data $g(t)$ must be modified at intermediate stages of the two-stage scheme to preserve full fourth-order accuracy.

## Method
Cubic polynomial $p(x)=\alpha_3 x^3+\alpha_2 x^2+\alpha_1 x+\alpha_0$ over $I_{-2}\cup I_{-1}\cup I_0\cup I_1$ interpolates cell averages and is constrained by $p(0)=g(t)$ and $p'(0)=-f'(g)^{-1}g'(t)$ (inverse LW with only first derivatives) to give ghost-cell averages $\bar u_{-1},\bar u_{-2}$ and differences $\Delta u_{-1},\Delta u_{-2}$; WENO-type stencil selection with smoothness indicators $\beta^{(r)}$ on three sub-stencils $S^{(0)},S^{(1)},S^{(2)}$ handles discontinuities. For outflow, WENO extrapolation as in Tan–Shu. The two-stage Lax–Wendroff scheme of Li–Du 2016 (with HWENO5 reconstruction and GRP Riemann solver) is corrected so the intermediate-stage boundary value uses a modified $g$ rather than the literal $g(t^{n+1/2})$.

## Result
Demonstrated fourth-order convergence in $L^1$ and $L^\infty$ for: linear scalar advection with smooth/discontinuous boundary data; linearized Euler with subsonic in/out flow (orders ~3.9–4.5 at $m=160$–$640$); quasi-1D nozzle flow with momentum errors converging at order ~4 (Table 4); the Woodward–Colella blast-wave, double Mach reflection ($960\times240$), and forward-facing step ($960\times320$) match traditional reflective treatments while validating the solid-wall boundary procedure.

## Why it matters here
General background; no direct arena tie. Numerical PDE / hyperbolic-conservation-law boundary treatment is outside the Einstein Arena problem set (sphere packing, autocorrelation, kissing, extremal graphs, sieves, functional inequalities).

## Open questions / connections
- Extension to moving boundaries, curved-geometry solid walls, and small cut-cell problems (deferred by authors).
- Generalization beyond the two-stage scheme to higher-order multi-stage Lax–Wendroff variants (e.g., Pan–Xu–Li–Li 2016 gas-kinetic scheme).
- Stability analysis of the modified intermediate-stage boundary condition, in the spirit of Li–Shu–Zhang 2016 for ILW.

## Key terms
Lax-Wendroff, inverse Lax-Wendroff, GRP solver, HWENO reconstruction, two-stage fourth-order scheme, hyperbolic conservation laws, ghost cells, numerical boundary conditions, WENO smoothness indicators, compressible Euler equations, double Mach reflection, nozzle flow
