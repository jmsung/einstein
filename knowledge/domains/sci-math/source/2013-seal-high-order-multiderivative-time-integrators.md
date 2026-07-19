---
type: source
kind: paper
title: High-Order Multiderivative Time Integrators for Hyperbolic Conservation Laws
authors: David C. Seal, Y. Güçlü, A. Christlieb
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1304.2817
source_local: ../raw/2013-seal-high-order-multiderivative-time-integrators.pdf
topic: general-knowledge
cites:
---

# High-Order Multiderivative Time Integrators for Hyperbolic Conservation Laws

**Authors:** David C. Seal, Y. Güçlü, A. Christlieb  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1304.2817

## One-line
Constructs explicit multistage two-derivative Runge-Kutta time integrators for hyperbolic PDEs, unifying classical Runge-Kutta and Lax-Wendroff (Taylor) methods within a single framework applied to DG and finite-difference WENO spatial discretizations.

## Key claim
Multistage two-derivative Runge-Kutta (TDRK) schemes — requiring only the flux Jacobian (not higher tensors) — achieve high-order accuracy (demonstrated through 4th and 5th order) competitive with popular SSP-RK integrators, while reducing memory footprint and communication overhead relative to multistage Runge-Kutta and improving portability relative to pure Lax-Wendroff/ADER methods.

## Method
General class: multiderivative Runge-Kutta update $y^{n+1} = y^n + \sum_m \Delta t^m \sum_i b_i^{(m)} L^{(m-1)}(y^{(i)})$ with higher time derivatives obtained via Cauchy-Kowalewski $q_{,tt} = \nabla_x \cdot (R'(q) \cdot \nabla_x \cdot R(q))$. Two spatial discretizations are integrated: DG uses generalized Riemann solver techniques (after Dumbser-Munz) to evaluate $\dot L$ at interfaces; FD-WENO constructs the higher spatial derivatives via central differences on reconstructed fluxes. Restricting to $r=2$ derivatives keeps only the flux Jacobian in play, retaining portability.

## Result
Presents and tests explicit TDRK3, TDRK4 (two-stage), and TDRK5 schemes on advection, Buckley-Leverett, shallow-water dam break, Lax shock tube, and Shu-Osher shock-entropy problems. Numerical experiments confirm designed orders of accuracy, stability under CFL numbers comparable to SSP-RK3/RK4 (e.g. $\nu = 0.4$ for WENO, $\nu = 0.08$ for DG-P3), and solution quality indistinguishable from established SSP integrators at the same resolution, while using fewer stages.

## Why it matters here
General background; no direct arena tie — this is a numerical-PDE time-integration paper for hyperbolic conservation laws (DG/WENO), which sits outside the einstein-arena problem families (sphere packing, autocorrelation, kissing, extremal combinatorics). The closest tangential relevance is the general principle of trading memory for FLOPs via higher derivatives, which mirrors how mpmath polish and higher-precision evaluators trade compute for accuracy in our optimizer pipelines.

## Open questions / connections
- Extension to multi-dimensional unstructured meshes and to parabolic PDEs (authors flag both as future work).
- Whether SSP variants of multiderivative RK exist, and what their optimal CFL coefficients are.
- GPU/modern-architecture implementations — authors note the memory-bandwidth motivation but defer empirical timing.
- Relation to ADER schemes (Toro-Titarev) and Lax-Wendroff DG (Qiu-Dumbser-Shu), which this work generalizes.

## Key terms
multiderivative Runge-Kutta, two-derivative Runge-Kutta, TDRK, Lax-Wendroff, Cauchy-Kowalewski, discontinuous Galerkin, WENO, hyperbolic conservation laws, Taylor methods, ADER, strong stability preserving, generalized Riemann solver, Butcher tableau, Obreshkoff, flux Jacobian
