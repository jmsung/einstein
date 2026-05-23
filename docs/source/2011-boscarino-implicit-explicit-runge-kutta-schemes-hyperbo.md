---
type: source
kind: paper
title: Implicit-Explicit Runge-Kutta Schemes for Hyperbolic Systems and Kinetic Equations in the Diffusion Limit
authors: S. Boscarino, L. Pareschi, G. Russo
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1110.4375
source_local: ../raw/2011-boscarino-implicit-explicit-runge-kutta-schemes-hyperbo.pdf
topic: general-knowledge
cites:
---

# Implicit-Explicit Runge-Kutta Schemes for Hyperbolic Systems and Kinetic Equations in the Diffusion Limit

**Authors:** S. Boscarino, L. Pareschi, G. Russo  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1110.4375

## One-line
Constructs IMEX Runge-Kutta time-integrators for stiff hyperbolic relaxation systems that remain stable and accurate in the diffusion limit $\varepsilon\to 0$ without a parabolic $\Delta t=O(\Delta x^2)$ restriction.

## Key claim
By reformulating the stiff hyperbolic system $u_t+v_x=0$, $\varepsilon^2 v_t+p(u)_x=-(v-q(u))$ as $u_t=-(v+\mu p(u)_x)_x+\mu p(u)_{xx}$ (with $\mu(0)=1$) and applying IMEX-RK schemes of type A / CK / ARS, the resulting scheme is asymptotic-preserving and reduces, in the limit, to an IMEX scheme for the convection-diffusion equation $u_t+q(u)_x=p(u)_{xx}$ with diffusion treated **implicitly** — yielding a hyperbolic CFL $\Delta t=O(\Delta x)$ uniformly in $\varepsilon$.

## Method
Partitioned IMEX Runge-Kutta time discretization combined with a *reformulation trick*: add and subtract $\mu p(u)_{xx}$ so the explicit flux $v+\mu p(u)_x\to q(u)$ vanishes nicely as $\varepsilon\to 0$, while the diffusion term $\mu p(u)_{xx}$ is kept on the implicit side. Index-1 DAE analysis (via power-series expansion in $\varepsilon$) gives additional "algebraic order conditions" ($\tilde c_s=1$ for 2nd order, $e_s^T\tilde A\tilde c=1/2$ for 3rd) and motivates **globally stiffly accurate** schemes ($b^T=e_s^TA$, $\tilde b^T=e_s^T\tilde A$) so the numerical solution lands on the equilibrium manifold $g(u,v)=0$. Space discretization uses conservative finite differences with WENO reconstruction.

## Result
Fourier stability analysis of the first-order scheme with $\mu=1$ yields the bound $\xi^2\Delta t<\tfrac{1}{4}(1-4\xi^2\varepsilon^2)/(\varepsilon^2\xi^2)$, which becomes *less* restrictive as $\varepsilon\to 0$ — opposite of the classical parabolic trap. A non-existence theorem (Thm 8.1) shows no second-order stiffly accurate type-A IMEX scheme with $s=3$ stages exists, forcing either more stages or sacrificing FSAL. Numerical tests on 1D neutron transport (slab geometry, $\varepsilon=10^{-8}$ to $10^{-2}$) show 2–4× speedup over the Jin–Pareschi–Toscani explicit-limit scheme while matching reference solutions in transient, steady, two-material, and boundary-layer regimes.

## Why it matters here
General background; no direct arena tie. The 23 Einstein Arena problems are static optimization / extremal problems (sphere packing, autocorrelation, Sidon sets, kissing numbers), not time-dependent PDEs with stiff relaxation — IMEX time-integrators do not appear in the current optimizer toolkit. Could be peripherally relevant if a problem ever needed gradient flow with a stiff projection step, but nothing in the wiki currently points there.

## Open questions / connections
- Extension to general additive Runge-Kutta schemes for "highly stiff" $g(u,v)$ + "mildly stiff" $f_2(u)$ splitting (authors flag as future work).
- Order reduction for the differential variable when $b=\tilde b$ — quantifying it for $p\geq 3$ schemes remains partly open.
- Connection to Boltzmann compressible Navier–Stokes asymptotics (Bennoune–Lemou–Mieussens) and micro-macro formulations (Lemou–Mieussens) — different splittings of the same AP problem.

## Key terms
IMEX Runge-Kutta, asymptotic preserving, diffusion limit, hyperbolic relaxation, stiffly accurate, DIRK, ESDIRK, ARS scheme, CK scheme, neutron transport, convection-diffusion, parabolic CFL, index-1 DAE, WENO, Boscarino, Pareschi, Russo, Jin
