---
type: source
kind: paper
title: Asymptotic Preserving Implicit-Explicit Runge-Kutta Methods for Nonlinear Kinetic Equations
authors: G. Dimarco, L. Pareschi
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1205.0882
source_local: ../raw/2012-dimarco-asymptotic-preserving-implicit-explicit-runge-k.pdf
topic: general-knowledge
cites:
---

# Asymptotic Preserving Implicit-Explicit Runge-Kutta Methods for Nonlinear Kinetic Equations

**Authors:** G. Dimarco, L. Pareschi  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1205.0882

## One-line
Constructs IMEX Runge-Kutta time integrators for stiff nonlinear kinetic (Boltzmann/BGK) equations that remain stable and accurate uniformly across the Knudsen number $\varepsilon$, including a penalization trick that sidesteps inverting the full Boltzmann collision operator.

## Key claim
For systems $Y' = F(Y) + \varepsilon^{-1} R(Y)$, IMEX-RK schemes of **type A** (with invertible implicit matrix $A$) are asymptotic preserving (AP), and if additionally globally stiffly accurate (GSA) they are asymptotically accurate (AA) — degenerating in the limit $\varepsilon \to 0$ to the explicit RK scheme applied to the compressible Euler system. Type CK / ARS variants achieve AP under consistent initial data or the extra condition $w_1 = \hat{w}^T \hat{A}^{-1} a$. The penalized decomposition $R(Y) = N(Y) + L(Y)$ with $L(Y) = \mu(M[f]-f)$ inherits these properties without inverting the Boltzmann gain term.

## Method
Splits the stiff relaxation operator into a nonlinear non-dissipative part $N(Y)$ treated explicitly and a linear BGK-like penalization $L(Y) = \mu(M[f]-f)$ treated implicitly — linearization is on the *asymptotically long* time scale (Jacobian at equilibrium), not the short relaxation scale. The two-tableau Butcher representation $(\tilde A, \tilde w, \tilde c)$ / $(A, w, c)$ is analyzed for AP, AA, monotonicity (region of absolute monotonicity $z = \mu\Delta t/\varepsilon$), and strong-stability-preserving explicit parts. New 2nd/3rd-order GSA penalized schemes (DP1-A, DP2-A, DP-ARS families) are tabulated.

## Result
First full third-order IMEX implementation for the space-inhomogeneous Boltzmann equation validated numerically (WENO-3 in space, fast spectral collision integral, $N_v=32$). Convergence experiments at $\varepsilon \in \{10^{-1}, 10^{-3}, 10^{-6}\}$ show prescribed order under equilibrium initial data; schemes lacking AA degrade to first order in stiff regimes; DP1-A(2,4,2) and DP2-A(2,4,2) hold second order *uniformly* in $\varepsilon$ for non-equilibrium data. Sufficient conditions for positivity in the homogeneous case are derived via the stability function $R(z) = 1 - z w^T(I+zA)^{-1}e$.

## Why it matters here
General background; no direct arena tie. The paper is numerical-analysis machinery for stiff PDE/ODE integration (Boltzmann fluid limit) — not relevant to sphere packing, autocorrelation inequalities, kissing numbers, Sidon sets, or any of the 23 Einstein Arena problem categories. Tangentially, the IMEX/operator-splitting idea (treat the stiff "easy" part implicitly, the hard part explicitly) is a generic optimizer pattern but the wiki already has stronger pointers for that under `techniques/`.

## Open questions / connections
- Monotonicity in the *non-homogeneous* case (with transport $v\cdot\nabla_x f$) left open; only the spatially homogeneous case is analyzed.
- Extension to Landau-Fokker-Planck and other collisional kinetic operators flagged as future work.
- Connection to micro-macro decomposition schemes (Lemou [27], Bennoune-Lemou-Mieussens [2]) — penalization vs explicit splitting trade-off not resolved.

## Key terms
IMEX Runge-Kutta, asymptotic preserving, Boltzmann equation, BGK relaxation, Knudsen number, stiff ODE, DIRK, globally stiffly accurate, penalization, Chapman-Enskog, compressible Euler limit, fluid-kinetic coupling
