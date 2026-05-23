---
type: source
kind: paper
title: Implicit and Implicit–Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order
authors: S. Conde, S. Gottlieb, Zachary J. Grant, J. Shadid
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1702.04621
source_local: ../raw/2017-conde-implicit-implicit-explicit-strong.pdf
topic: general-knowledge
cites:
---

# Implicit and Implicit–Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order

**Authors:** S. Conde, S. Gottlieb, Zachary J. Grant, J. Shadid  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1702.04621

## One-line
Constructs optimal implicit and IMEX strong-stability-preserving (SSP) Runge–Kutta methods that achieve high *linear* order ($p_{\text{lin}}\le 9$ implicit, $p_{\text{lin}}\le 7$ IMEX) while keeping modest nonlinear order, breaking the classical sixth-order SSP barrier on linear problems.

## Key claim
The nonlinear SSP order barrier ($p\le 6$ implicit, $p\le 4$ explicit) does **not** apply to linear order: optimal implicit SSP RK methods exist with $p_{\text{lin}}$ up to $9$ at $p=2,3,4$ with SSP coefficient $C$ essentially unaffected by raising $p$ from $2$ to $4$ (e.g., $s=p_{\text{lin}}=6$, $p=4$ gives $C=5.138$ vs $C=0.18$ for the standard $s=p=p_{\text{lin}}=6$ method). Implicit SSP coefficients run up to $\sim 6\times$ the corresponding explicit ones; pushing $p$ to $5$ or $6$ collapses $C$ sharply.

## Method
Formulates the SSP optimization in Butcher form as maximizing $r$ subject to $(I+rA)^{-1}$ being entrywise nonnegative with row sums $\le 1$, plus a reduced linear-order condition set $\tau_q^{\text{lin}}(A,b)=b^T A^{q-1}e=1/q!$ for $q\le p_{\text{lin}}$ alongside the full nonlinear order conditions up to $p$. Solves via Ketcheson-style numerical optimization in MATLAB, restricting to diagonally-implicit (DIRK) forms (which match fully-implicit optima). For IMEX, co-optimizes a paired DIRK + explicit SSPRK around the ratio $K=\Delta t_{FE}^{(G)}/\Delta t_{FE}^{(F)}$ of forward-Euler step sizes of the two components.

## Result
Tabulates $C$ for $s\le 11$, $p\in\{2,3,4,5,6\}$, $p_{\text{lin}}\le 9$: e.g., $(s,p,p_{\text{lin}})=(6,4,6)$ has $C=5.14$, $(8,4,9)$ has $C=4.735$, $(10,2,11)$ has $C=5.23$. IMEX pairs constructed for $p_e=3,4$ with $p_i=2,3,4$ and $p_{\text{lin}}$ up to $7$, parametrized by $K\in\{1,10,100,\infty\}$. Numerical tests on advection–diffusion and Burgers'+linear-advection confirm the design orders and sharpness of the predicted TVD time-step; IMEX allows $\sim 1.5$–$2\times$ the explicit time-step, fully-implicit up to $\sim 5\times$.

## Why it matters here
General background; no direct arena tie — this is a numerical-PDE time-integration result, orthogonal to the Einstein Arena problem set (sphere packing, autocorrelation, kissing numbers, etc.). The only faint connection is methodological: it's another instance of "the linear-only restriction lifts a nonlinear order barrier," a pattern that occasionally appears in extremal problems (LP relaxation outperforming the original combinatorial bound).

## Open questions / connections
- Extends [Gottlieb–Grant–Higgs 2015] explicit LNL methods to the implicit and IMEX settings; whether the same $\sim 6\times$ implicit-to-explicit $C$ ratio holds at higher $p_{\text{lin}}>9$ is open.
- Co-optimization for additional properties (imaginary-axis inclusion, large real-axis stability) is sketched but not systematized.
- The sharp $C\le 2s$ implicit empirical bound (vs $C\le s$ proven for explicit) remains unproven in general.

## Key terms
strong stability preserving, Runge–Kutta, SSP coefficient, implicit-explicit IMEX, DIRK, linear order barrier, Shu–Osher form, Butcher tableau, total variation diminishing TVD, forward Euler condition, hyperbolic conservation law, Ketcheson optimization
