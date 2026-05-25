---
type: source
kind: paper
title: High order strong stability preserving multi-derivative implicit and IMEX Runge--Kutta methods with asymptotic preserving properties
authors: Sigal Gottlieb, Zachary J. Grant, Jingwei Hu, Ruiwen Shu
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2102.11939v3
source_local: ../raw/2021-gottlieb-high-order-strong-stability.pdf
topic: general-knowledge
cites: 
---

# High order strong stability preserving multi-derivative implicit and IMEX Runge--Kutta methods with asymptotic preserving properties

**Authors:** Sigal Gottlieb, Zachary J. Grant, Jingwei Hu, Ruiwen Shu  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2102.11939v3

## One-line
Constructs unconditionally strong-stability-preserving (SSP) implicit and IMEX multi-derivative Runge–Kutta time integrators of order up to $p=4$ (implicit) and $p=3$ (IMEX), enabled by a new "backward derivative" condition on $\dot G = G'G$.

## Key claim
Under a forward-Euler condition on $G$ (or on the explicit part $F$) and a *backward* second-derivative condition $\|u - \Delta t^2 \dot G(u)\| \le \|u\|$ for $\Delta t^2 \le \dot k\,\Delta t_{FE}^2$, there exist implicit two-derivative RK schemes that are unconditionally SSP up to order $p=4$, and IMEX multi-derivative RK schemes SSP up to order $p=3$ with step restriction depending only on $F$. Order $p=5$ under the same conditions could not be found. A no-go result (Appendix A) shows the analogous result is impossible under the *forward* second-derivative or Taylor-series conditions.

## Method
Write methods in a Shu–Osher form (11)/(14) with matrices $R, P, W, D, \dot D$ such that all explicit pieces enter via convex combinations and the implicit second-derivative coefficients $\dot D \le 0$ (negative on purpose, exploiting the backward derivative condition (6)). SSP is then proved stage-by-stage by adding slack multiples $\alpha,\beta$ of $\|u^{(i)}\|$ and using the forward-Euler + backward-derivative inequalities. Order conditions for multi-derivative IMEX RK schemes are derived (new) up to $p=3$; concrete coefficient tableaux are reported (2-stage $p=3$ implicit, 5-stage $p=4$ implicit, 3-stage $p=2$ IMEX with $r=1$, 6-stage $p=3$ IMEX with $r\approx 0.9044$).

## Result
Theorem 1 / Theorem 2 give clean componentwise SSP conditions $Re\ge0,\ P\ge0,\ W\ge0,\ D\ge0,\ \dot D\le0$. Proposition 1 adds: if every stage has $d_{ii}+|\dot d_{ii}|>0$, the IMEX scheme is asymptotic-preserving (AP) and positivity-preserving for stiff systems $u_t = T(u)+\tfrac1\varepsilon Q(u)$ with conservative dissipative $Q$ satisfying $\dot Q(u) = -C_{Ru} Q(u)$ (verified for a hyperbolic relaxation system, the Broadwell model, and the BGK kinetic equation). Numerical tests confirm design order in kinetic ($\varepsilon=O(1)$) and fluid ($\varepsilon\ll1$) regimes, with the expected order-reduction plateau at $O(\varepsilon)$ in the intermediate regime.

## Why it matters here
General background; no direct arena tie. Closest adjacent topics in this wiki are convex-functional / monotonicity-preserving optimization analysis and stiff-ODE handling — useful only if the agent ever needs SSP/AP discretizations for a PDE-discretization-based arena problem (none of the 23 are currently of that kind).

## Open questions / connections
- Does a $p\ge 5$ unconditionally SSP implicit multi-derivative RK scheme exist under the backward-derivative condition, or is there a structural obstruction?
- Can the order-reduction plateau in the intermediate $\varepsilon$ regime be characterized via higher-order asymptotic expansion (authors flag this as future work)?
- Extension to operators where $\dot Q(u) = -C_{Ru} Q(u)$ fails (e.g., full Boltzmann collision) — what weaker dissipation condition still buys AP?

## Key terms
strong stability preserving, SSP Runge–Kutta, multi-derivative Runge–Kutta, IMEX schemes, asymptotic preserving, positivity preserving, backward derivative condition, Shu–Osher form, BGK kinetic equation, Broadwell model, hyperbolic relaxation, stiff ODE, Gottlieb, Ketcheson
