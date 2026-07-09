---
type: source
kind: paper
title: Implicit-Explicit Linear Multistep Methods for Stiff Kinetic Equations
authors: G. Dimarco, L. Pareschi
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.00102
source_local: ../raw/2016-dimarco-implicit-explicit-linear-multistep-methods.pdf
topic: general-knowledge
cites:
---

# Implicit-Explicit Linear Multistep Methods for Stiff Kinetic Equations

**Authors:** G. Dimarco, L. Pareschi  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.00102

## One-line
Develops high-order Implicit-Explicit (IMEX) linear multistep schemes for stiff kinetic equations (BGK and Boltzmann) that remain accurate uniformly across the full range from kinetic to Navier-Stokes regimes.

## Key claim
IMEX multistep schemes (BDF and TVB families) up to order 5 are asymptotic-preserving (AP) and asymptotically accurate (AA) for kinetic equations $\partial_t f + v\cdot\nabla_x f = Q(f)/\varepsilon$, including capture of the $O(\varepsilon)$ Navier-Stokes correction; they outperform IMEX Runge-Kutta methods by avoiding coupling order conditions and reducing per-step cost.

## Method
Combines $s$-step explicit linear multistep on the transport term $v\cdot\nabla_x f$ with implicit linear multistep on the stiff collision term $Q(f)/\varepsilon$. For full Boltzmann, uses BGK-style penalization $Q(f) = [Q(f) - \mu(M[f]-f)] + \mu(M[f]-f)$ so the implicit step is a linear projection toward equilibrium. Theorem 3.3/3.4: with well-prepared initial data (or after $s$ steps for BDF), the scheme reduces to the explicit multistep method on the limiting Euler/Navier-Stokes system. Stability analyzed via characteristic polynomial $\rho(\zeta) - z_E\sigma_E(\zeta) - z_I\sigma_I(\zeta) = 0$ with penalization factor $\xi = (\eta-\mu)/\mu$.

## Result
Numerical experiments on non-homogeneous BGK and full Boltzmann (Maxwell molecules, fast spectral method) confirm theoretical convergence rates 2–5 across $\varepsilon \in \{10^{-1},10^{-2},10^{-5}\}$. Order-4 and order-5 BDF schemes show greater sensitivity to the penalization factor $\xi$ — IMEX-BDF5 degrades for small $\varepsilon$, signaling that high-order penalized methods need accurate stiff-eigenvalue estimates. Per Theorem 3.1: $s$-step IMEX scheme can reach order $p=s$ at most, with $s$ free parameters at order $s$.

## Why it matters here
General background; no direct arena tie. The 23 Einstein Arena problems are static optimization (sphere packing, autocorrelation, kissing numbers), not time-stepping of PDEs — IMEX multistep theory has no obvious mapping to mpmath polish, basin-hopping, Remez exchange, or LP/SDP bounds.

## Open questions / connections
- Can high-order IMEX multistep be made robust to penalization-factor choice without resolving $\varepsilon$ — e.g., velocity-dependent BGK frequencies or ES-BGK as penalization operator?
- Is there a non-penalized high-order alternative based on direct inversion of $Q(f,f)$ at each step?
- Extends Ascher-Ruuth-Wetton (1995) IMEX-multistep theory and Filbet-Jin (2010) penalization to higher order and to the Navier-Stokes asymptotic regime — a regime where analogous theory for IMEX-RK is still lacking per the authors.

## Key terms
IMEX multistep, BDF, Boltzmann equation, BGK model, asymptotic-preserving, Chapman-Enskog expansion, Navier-Stokes limit, Knudsen number, penalization, stiff collision operator, Maxwellian equilibrium, fast spectral method
