---
type: source
kind: paper
title: Explicit and implicit error inhibiting schemes with post-processing
authors: Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1910.02937v2
source_local: ../raw/2019-ditkowski-explicit-implicit-error-inhibiting.pdf
topic: general-knowledge
cites: 
---

# Explicit and implicit error inhibiting schemes with post-processing

**Authors:** Adi Ditkowski, Sigal Gottlieb, Zachary J. Grant  ·  **Year:** 2019  ·  **Source:** http://arxiv.org/abs/1910.02937v2

## One-line
Extends the Error Inhibiting Scheme (EIS) framework for ODE time integrators so that the leading error term has a known closed form and can be filtered by a post-processor, yielding solutions two orders higher than predicted by truncation-error analysis.

## Key claim
For general linear methods $V^{n+1} = DV^n + \Delta t\,AF(V^n) + \Delta t\,RF(V^{n+1})$ with $D$ a rank-one consistent matrix, if the order conditions $\tau_j=0$ ($j=1,\dots,p$) plus the EIS+ conditions $D\tau_{p+1}=0$, $D\tau_{p+2}=0$, and $D(A+R)\tau_{p+1}=0$ hold, then the global error has the explicit form $E^n = \Delta t^{p+1}\tau^n_{p+1} + \Delta t^{p+2}\tau^n_{p+2} + \Delta t^{p+2}(A+R)\tau^n_{p+1}F_u^n + O(\Delta t^{p+3})$, and a Vandermonde-based post-processor $\Phi$ removes the leading term to give an $O(\Delta t^{p+2})$ final solution.

## Method
General linear methods (block one-step / peer-style) with both explicit and implicit variants, analyzed via Taylor expansion of the local truncation error vectors $\tau_j$ and induction on the error recursion. The post-processor is constructed as $\Phi = T\,\mathrm{diag}(0,1,\dots,1,*,\dots,*)\,T^{-1}$ where $T$ is a modified Vandermonde matrix on the last two time-levels' abscissas with its top-order column replaced by the truncation-error vector $\tilde\tau$. Methods are found by Matlab optimization over coefficient space subject to order + EIS+ constraints; stability regions and SSP coefficients are then characterized.

## Result
Concrete schemes constructed: explicit eEIS+(2,4), SSP variants eSSP-EIS(3,4) and eSSP-EIS(4,5), and implicit iEIS+(2,3), iEIS+(3,4), iEIS+(4,5). Numerical tests on advection-diffusion and Burgers confirm gains of 2 orders (e.g. iEIS+(2,3): truncation order 2, observed $\sim$3 unprocessed, $\sim$3 post-processed; iEIS+(3,4) hits order $\approx 4$ post-processed; iEIS+(4,5) hits $\approx 5$). eSSP-EIS(3,4) preserves TVD up to CFL $\lambda\approx 1.2$ (vs predicted 0.75); eSSP-EIS(4,5) up to $\lambda\approx 1.16$ (vs 0.63). Prothero–Robinson shows the expected order reduction at $a=1000$ but error magnitudes remain small.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems are time-evolution PDE/ODE problems, and the project's compute-router never invokes ODE integrators of this form. Possibly relevant only as conceptual analogy: "structurally constrain the iteration so the leading error term has a known form, then subtract it" mirrors Remez-style residue cancellation and could inform an as-yet-unwritten meta-technique page.

## Open questions / connections
- Extends quasi-consistency theory of Skeel (1978), Kulikov, and Weiner et al. on superconvergent peer methods — the EIS+ conditions strictly weaken the conditions in Kulikov–Weiner (2010, 2018).
- Authors flag future work: multi-derivative methods, IMEX schemes, variable step-size EIS — none yet adapted to non-temporal settings.
- Open: whether the "post-processor removes a known leading error term" idea generalizes to non-temporal iterations (Krylov, fixed-point optimization loops) — not addressed in the paper.

## Key terms
error inhibiting schemes, EIS, general linear methods, quasi-consistency, Runge-Kutta, linear multistep, peer methods, post-processing, superconvergence, Vandermonde filter, SSP, Ditkowski, Gottlieb, Kulikov, Weiner
