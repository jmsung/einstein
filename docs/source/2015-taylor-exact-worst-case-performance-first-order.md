---
type: source
kind: paper
title: Exact Worst-Case Performance of First-Order Methods for Composite Convex Optimization
authors: Adrien B. Taylor, J. Hendrickx, François Glineur
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1512.07516
source_local: ../raw/2015-taylor-exact-worst-case-performance-first-order.pdf
topic: general-knowledge
cites:
---

# Exact Worst-Case Performance of First-Order Methods for Composite Convex Optimization

**Authors:** Adrien B. Taylor, J. Hendrickx, François Glineur  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1512.07516

## One-line
Reduces the computation of the exact worst-case behavior of fixed-step first-order methods for composite convex optimization to a tractable SDP, producing both tight guarantees and explicit worst-case instances.

## Key claim
For any fixed-step linear first-order method (FSLFOM) — projected, proximal, conditional, inexact (sub)gradient — the worst-case performance on classes of convex functions (smooth/strongly convex/bounded-domain/bounded-gradient, including indicator and support functions) can be computed exactly as a semidefinite program in the Gram matrix $G_N$ and function values $F_N$, provided dimension $d \ge (n+1)(N+2)$.

## Method
Performance Estimation Problem (PEP) framework: encode iterates, subgradients, and function values via a Gram matrix $G_N \succeq 0$; eliminate the infinite-dimensional function variables using *first-order convex interpolation conditions* — necessary-and-sufficient linear constraints in $G_N, F_N$ characterizing when a triple set $\{(x_i, g_i, f_i)\}$ extends to a function in the target class. Primal-feasible SDP solutions give worst-case instances; dual-feasible solutions give certified upper bounds expressible as combinations of valid inequalities.

## Result
New analytical bounds: (i) proximal point algorithm — guarantee twice better than previously known (proved analytically via dual flow construction with diagonally-dominant Schur complement); (ii) conditional gradient (Frank–Wolfe) — improved by more than factor of 2 over $F(x_N)-F^* \le 2LD^2/(N+2)$; (iii) new POGM (proximal extension of Kim–Fessler OGM) converges ~2× faster worst-case than FISTA/FPGM; (iv) new FPGM2 variant fixes infeasibility/unboundedness pathologies of FISTA's secondary sequence in constrained/proximal settings. Tight worst-case functions identified as Huber-shaped (unconstrained) or 1-D linear $\min_{x\ge 0} cx$ (constrained).

## Why it matters here
General background; no direct arena tie. Relevant if any arena problem uses fixed-step first-order optimization (e.g., gradient/proximal/projected methods on smooth convex objectives) — gives exact achievable worst-case rates rather than loose textbook bounds, and the PEP→SDP→dual-certificate methodology is a template for "automated proof of optimization bound via SDP," conceptually adjacent to LP/SDP-bound techniques already in the wiki (Cohn–Elkies, flag algebras).

## Open questions / connections
- Extension to dynamic step-size rules and line-search (backtracking, Armijo–Wolfe) — currently restricted to fixed-step methods.
- Convex relaxations for the nonconvex rank-constrained PEP when $d < (n+1)(N+2)$ (small-dimension regime).
- Refining analyses of randomized coordinate-descent and stochastic methods via PEP.
- Connection to Lessard–Recht–Packard IQC/dynamical-systems framework — PEP is tighter (per-iteration) but IQC gives single-SDP global rates.
- Algorithmic design: PEP as a tool to *discover* optimal-rate methods (as Kim–Fessler did for OGM, this paper for POGM).

## Key terms
performance estimation problem, PEP, semidefinite programming, SDP, first-order methods, composite convex optimization, proximal gradient, FISTA, optimized gradient method, OGM, POGM, conditional gradient, Frank-Wolfe, proximal point algorithm, convex interpolation, Gram matrix, worst-case analysis, fixed-step linear first-order method, FSLFOM, Taylor-Hendrickx-Glineur, Drori-Teboulle, Kim-Fessler, alternate projections, Dykstra, subgradient method
