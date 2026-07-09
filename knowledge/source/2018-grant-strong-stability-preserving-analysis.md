---
type: source
kind: paper
title: A Strong Stability Preserving Analysis for Explicit Multistage Two-Derivative Time-Stepping Schemes Based on Taylor Series Conditions
authors: Zachary J. Grant, S. Gottlieb, David C. Seal
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.10526
source_local: ../raw/2018-grant-strong-stability-preserving-analysis.pdf
topic: general-knowledge
cites:
---

# A Strong Stability Preserving Analysis for Explicit Multistage Two-Derivative Time-Stepping Schemes Based on Taylor Series Conditions

**Authors:** Zachary J. Grant, S. Gottlieb, David C. Seal  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.10526

## One-line
Develops explicit multistage two-derivative Runge–Kutta time integrators that preserve strong-stability (TVD/positivity) under a forward-Euler + Taylor-series pair of base conditions, expanding the class of usable spatial discretizations for hyperbolic PDEs.

## Key claim
Under base conditions $\|u^n+\Delta t F(u^n)\|\le\|u^n\|$ for $\Delta t\le\Delta t_{FE}$ and $\|u^n+\Delta t F(u^n)+\tfrac12\Delta t^2\tilde F(u^n)\|\le\|u^n\|$ for $\Delta t\le K\Delta t_{FE}$, explicit two-derivative multistage methods admit positive SSP coefficients $C_{TS}$ up to a **maximum order $p=6$** (proven order barrier), beating the $p=4$ barrier for explicit SSP Runge–Kutta.

## Method
Rewrite the multistage two-derivative scheme in Shu–Osher matrix-vector form $y = e u^n + \Delta t S F(y) + \Delta t^2 \hat S \tilde F(y)$, then derive component-wise non-negativity conditions (Theorem 1, eqs 23a–c) sufficient for convex-combination decomposition into forward-Euler and Taylor-series base steps. Cast the search for optimal $S,\hat S$ as a constrained optimization maximizing $r$ subject to order conditions (Appendix A, up to $p=6$) and SSP positivity. Three sub-families (M1/M2/M3) reflect different simplifying ansatz.

## Result
- Proves explicit SSP-TS methods cannot exceed $p=6$.
- Establishes Lemma 1: any SSP-TS method is also SSP-SD (subset relation), but SSP-SD ⊄ SSP-TS (e.g., the classic two-stage 4th-order method (15) is SSP-SD but not SSP-TS).
- Optimized methods presented up to $p=6$; e.g., M2(4,5,1) has $C_{TS}=2.18648$, M3(8,6,1) has $C_{TS}=1.7369$. Numerical tests on advection / Buckley–Leverett / shallow water confirm observed TVD/positivity time-steps match or exceed predicted $\lambda = C_{TS}\Delta t_{FE}$; non-SSP methods (Dormand–Prince, RK(8,6)) fail positivity entirely.

## Why it matters here
General background; no direct arena tie — this is numerical analysis for hyperbolic PDE time-stepping (SSP Runge–Kutta theory), orthogonal to the Einstein Arena problems (sphere packing, autocorrelation, kissing numbers, extremal combinatorics). The convex-combination / monotonicity framework is methodologically adjacent to positivity-preserving LP arguments but does not contribute concept content to current wiki problems.

## Open questions / connections
- Are the sufficient SSP-TS conditions (23a-c) also *necessary*? Paper proves sufficiency only, unlike the RK case where Ferracina–Spijker / Higueras showed necessity.
- Extends the SSP-SD framework of Christlieb–Gottlieb–Grant–Seal (2016, ref [5]); leaves open whether a different base-condition pair could break the $p=6$ barrier.
- Identification of the spatial-discretization scaling factor $K$ (Taylor-series stability ratio) is left empirical; theoretical bounds on $K$ for WENO / DG schemes remain open.

## Key terms
strong stability preserving, SSP Runge-Kutta, multiderivative methods, two-derivative Runge-Kutta, Taylor series condition, Shu-Osher form, TVD, monotonicity preservation, hyperbolic conservation laws, WENO, order barrier, convex combination decomposition, forward Euler base condition, Gottlieb, Seal
