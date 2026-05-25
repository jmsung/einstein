---
type: source
kind: paper
title: Asymptotic-Preserving and Positivity-Preserving Implicit-Explicit Schemes for the Stiff BGK Equation
authors: Jingwei Hu, Ruiwen Shu, Xiangxiong Zhang
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.06279
source_local: ../raw/2017-hu-asymptotic-preserving-positivity-preserving-implicit.pdf
topic: general-knowledge
cites:
---

# Asymptotic-Preserving and Positivity-Preserving Implicit-Explicit Schemes for the Stiff BGK Equation

**Authors:** Jingwei Hu, Ruiwen Shu, Xiangxiong Zhang  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.06279

## One-line
A second-order IMEX Runge–Kutta time-discretization for the stiff BGK kinetic equation that is simultaneously asymptotic-preserving (captures the Euler limit as Knudsen number $\varepsilon \to 0$) and positivity-preserving (keeps the PDF $f \geq 0$) under a $\varepsilon$-independent CFL.

## Key claim
Adding a single explicit correction step $f^{n+1} = \tilde f^{n+1} - \alpha \Delta t^2 \varepsilon^{-2} Q'(f^*) Q(f^{n+1})$ to a standard IMEX-RK scheme yields the first second-order scheme that is AP, positivity-preserving, and entropy-decaying for BGK; minimum stages are $\nu=3$ (type A) and $\nu=4$ (type ARS), with explicit coefficient sets (e.g., type ARS: $\alpha=0.8$, CFL constant $c_{\text{sch}}=0.8125$).

## Method
Standard IMEX-RK (explicit transport, implicit collision) is augmented with a quadratic-in-$\Delta t$ correction exploiting the BGK structure $Q(f)=\tau_f(M[f]-f)$, where moments are conserved so $M[f]$ can be computed by taking moments of the scheme first. Order conditions (modified by an $\alpha$ term) and positivity inequalities on the Butcher-tableau coefficients are derived in Shu–Osher convex-combination form; coefficients are searched numerically to maximize CFL. Spatial discretization uses positivity-preserving finite-volume / WENO with Gauss–Legendre quadrature in $x$ to preserve AP at the fully-discrete level.

## Result
Two concrete coefficient sets are constructed (type A GSA, $\nu=3$, $c_{\text{sch}}\approx 0.525$; type ARS GSA, $\nu=4$, $c_{\text{sch}}=0.8125$). Formal analysis proves second-order accuracy for $\varepsilon=O(1)$, AP reduction to a second-order explicit RK for compressible Euler as $\varepsilon\to 0$ (type A unconditionally; type ARS for consistent initial data $f_0=M[f_0]$), entropy decay $S[f^{n+1}]\le S[f^n]$ with upwind spatial discretization, and unconditional preservation of $f\ge 0$. Numerics on Sod-type and mixed-regime problems confirm convergence rates and show ARS(2,2,2) produces hundreds of negative cells where the new scheme produces none. Extension to the Broadwell hyperbolic relaxation model and to third order is sketched.

## Why it matters here
General background; no direct arena tie. The paper is numerical analysis of stiff kinetic PDEs — orthogonal to the Einstein Arena problem families (sphere packing, autocorrelation, kissing, extremal combinatorics) currently catalogued in the wiki.

## Open questions / connections
- Uniform accuracy of IMEX schemes in the intermediate regime $\varepsilon = O(\Delta t)$ remains open (order reduction is observed but not analyzed).
- Generalization to other kinetic models (full Boltzmann, Fokker–Planck) where the $Q'(g)Q(f)=-\tau_g Q(f)$ identity does not hold is open.
- Connects to SSP-RK theory (Gottlieb–Shu–Tadmor non-existence of unconditional SSP implicit RK beyond order 1) and to Chertock–Cui–Kurganov–Wu sign-preserving semi-implicit schemes for stiff damping.

## Key terms
BGK equation, implicit-explicit Runge-Kutta, IMEX-RK, asymptotic-preserving, positivity-preserving, Knudsen number, compressible Euler limit, strong stability preserving, Shu-Osher form, Broadwell model, hyperbolic relaxation, entropy decay, kinetic equations, Maxwellian, stiff ODE
