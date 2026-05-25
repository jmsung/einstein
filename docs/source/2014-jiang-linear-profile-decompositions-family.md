---
type: source
kind: paper
title: Linear profile decompositions for a family of fourth order Schrödinger equations
authors: Jin-Cheng Jiang, Shuanglin Shao, Betsy Stovall
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1410.7520
source_local: ../raw/2014-jiang-linear-profile-decompositions-family.pdf
topic: general-knowledge
cites:
---

# Linear profile decompositions for a family of fourth order Schrödinger equations

**Authors:** Jin-Cheng Jiang, Shuanglin Shao, Betsy Stovall  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1410.7520

## One-line
Establishes linear profile decompositions for the fourth-order Schrödinger equation $iu_t + \Delta^2 u - \mu\Delta u = 0$ in dimensions $d \geq 2$, and uses them to prove dichotomy results for existence of extremizers to the associated Strichartz/Stein–Tomas inequalities.

## Key claim
Any $L^2_x$-bounded sequence of initial data for (1) admits (after subsequence) a decomposition into asymptotically orthogonal profiles $\phi^j_n = g^j_n \phi^j$ that are compact modulo symmetries, plus a small-dispersion error; consequently, extremizers for $\|D_\mu^{d/(d+2)} S_\mu(t)f\|_{L^{2(d+2)/d}_{t,x}} \leq C_{d,\mu}\|f\|_{L^2}$ either exist or the extremizing sequence concentrates into a free Schrödinger or free $S_0$ wave (giving lower bounds on the operator norm).

## Method
Refined Strichartz/Stein–Tomas inequality (Proposition 2.2) at the scale of $\mu$-caps, proved by reduction to dyadic annuli $\{|\xi|\sim 1\}$ where the quartic surface $\mu|\xi|^2 + |\xi|^4$ is elliptic, then Tao's bilinear restriction theorem for elliptic hypersurfaces. Inductive profile extraction follows the Bahouri–Gérard / Bégout–Vargas template; phase shifts $f\mapsto e^{i(\cdot)a}f$ serve as a stand-in for the missing Galilei boosts (since $\mu>0$ breaks scaling). Stationary-phase asymptotics + dominated convergence reduce the fourth-order propagator to either a free $e^{it\Delta^2}$ or a free Schrödinger $e^{-it\Delta}$ profile depending on the limit regime of $(h_n,\xi_n)$.

## Result
Refined Strichartz exponent $q = 2(d^2+3d+1)/d^2$ with $\theta=(d+2)^2/2$. Operator norm $A_\mu$ for (2) admits dichotomy: either an $L^2$-extremizer exists, or $A_0 = 3^{-1/(2(d+2))}2^{-d/(2(d+2))} B$ (with $B$ the free Schrödinger Strichartz constant), and analogous comparison for $\mu=1$ gives $A_1 \geq \max(A_0,B)$. This extends Jiang–Pausader–Shao (2010) from $d=1$ to all $d\geq 2$.

## Why it matters here
General background for harmonic-analysis / Fourier-restriction techniques; no direct Einstein Arena tie. Could marginally inform Hilbert/uncertainty-type problems via the refined Stein–Tomas machinery, but the application is to PDE extremizer theory, not extremal combinatorics or sphere packing.

## Open questions / connections
- Extension to general dispersive perturbations $|\nabla|^\alpha$, $\alpha>0$: authors note the argument seems amenable but did not verify.
- Sharp constants and explicit extremizer characterization (Gaussian-type vs free-wave) for $\mu>0$ remain open.
- Connection to Tao's bilinear restriction for elliptic surfaces (Tao 2003) and Guth's polynomial-partitioning restriction estimate (Guth 2016) — extends the toolkit beyond paraboloid case.

## Key terms
linear profile decomposition, fourth-order Schrödinger equation, Strichartz inequality, Stein–Tomas inequality, refined Strichartz, bilinear restriction, Tao, Guth, elliptic hypersurface, extremizers, Bahouri–Gérard, Littlewood–Paley, Fourier extension operator
