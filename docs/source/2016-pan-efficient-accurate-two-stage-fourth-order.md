---
type: source
kind: paper
title: An efficient and accurate two-stage fourth-order gas-kinetic scheme for the Euler and Navier-Stokes equations
authors: L. Pan, K. Xu, Qibing Li, Jiequan Li
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1602.05803
source_local: ../raw/2016-pan-efficient-accurate-two-stage-fourth-order.pdf
topic: general-knowledge
cites:
---

# An efficient and accurate two-stage fourth-order gas-kinetic scheme for the Euler and Navier-Stokes equations

**Authors:** L. Pan, K. Xu, Qibing Li, Jiequan Li  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1602.05803

## One-line
Constructs a fourth-order-in-time, fifth-order-in-space gas-kinetic scheme (GKS) for the compressible Euler/Navier-Stokes equations by combining a second-order time-accurate BGK flux with a two-stage Lax-Wendroff temporal discretization.

## Key claim
A two-stage time-stepping that uses both the flux $F(W^n,t)$ and its time derivative $\partial_t F$ achieves fourth-order temporal accuracy with only two flux evaluations (vs four RK stages), runs at CFL $\approx 0.5$, and remains as robust as the underlying second-order GKS from subsonic boundary layers to Mach 20 hypersonic viscous flow.

## Method
Semi-discrete finite-volume form $\partial_t w_i = L_i(w)$ is integrated by a two-stage Lax-Wendroff update: intermediate state $w^* = w^n + \tfrac{1}{2}\Delta t\, L(w^n) + \tfrac{1}{8}\Delta t^2 \partial_t L(w^n)$, then $w^{n+1} = w^n + \Delta t\, L(w^n) + \tfrac{1}{6}\Delta t^2[\partial_t L(w^n) + 2\partial_t L(w^*)]$. The time-accurate flux is obtained from the integral solution of the BGK equation (Xu 2001), with $F$ and $\partial_t F$ recovered by linear fit through $F(W^n,\Delta t/2)$ and $F(W^n,\Delta t)$. Spatial reconstruction uses 5th-order WENO on characteristic variables plus 3-point Gauss quadrature along cell interfaces. The appendix extends to fifth-order in time using third-order GKS flux with $\partial_{tt} F$ and intermediate stage at $t^* = t^n + (2/5)\Delta t$.

## Result
Density-advection test confirms 5th-order convergence down to $L_1 \sim 10^{-11}$ on $N=640$; the second-order GKS at the same CFL degrades to 2nd order. Isentropic vortex, Sedov, shock-vortex interaction, double Mach reflection (Mach 10), hypersonic cylinder (Ma = 8.03 viscous, Ma = 20 inviscid, no carbuncle), Blasius boundary layer (matches exact profile with 4 cells in layer), lid-driven cavity (Re = 1000, 3200), and viscous shock-tube (Re = 200, 1000) all reproduce reference data; primary vortex height 0.171 matches AUSMPW+ family.

## Why it matters here
General background; no direct arena tie. CFD / kinetic-equation methods do not connect to the sphere-packing, autocorrelation, kissing-number, or extremal-combinatorics problems in the einstein wiki — this is fluid-dynamics numerical analysis, not extremal geometry or analytic number theory.

## Open questions / connections
- Two-stage L-W framework (Li-Du 2015, arXiv:1512.03664) is the general meta-recipe being instantiated here — generic to any solver with a time-accurate flux.
- Extension to compact schemes that also update interface conservative variables (Pan-Xu 2015, 2016) for higher-order reconstructions on smaller stencils.
- Whether the same two-stage idea reduces stage count for higher-order DG / WENO solvers built on Riemann (not GRP/GKS) fluxes — paper argues first-order Riemann solvers are the bottleneck.

## Key terms
gas-kinetic scheme, BGK equation, two-stage Lax-Wendroff, generalized Riemann problem, Navier-Stokes, Euler equations, WENO reconstruction, Chapman-Enskog expansion, time-accurate flux, finite volume, hypersonic viscous flow, Pan Xu Li
