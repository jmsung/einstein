---
type: source
kind: paper
title: "PENLAB: A MATLAB solver for nonlinear semidefinite optimization"
authors: J. Fiala, Michal Kovcvara, M. Stingl
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1311.5240
source_local: ../raw/2013-fiala-penlab-matlab-solver-nonlinear.pdf
topic: general-knowledge
cites:
---

# PENLAB: A MATLAB solver for nonlinear semidefinite optimization

**Authors:** J. Fiala, Michal Kovcvara, M. Stingl  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1311.5240

## One-line
PENLAB is an open-source MATLAB solver for nonlinear semidefinite programs (NLP-SDP) — a teaching/research-oriented sibling of PENNON using the same augmented-Lagrangian / penalty-barrier algorithm.

## Key claim
A modified augmented-Lagrangian method with reciprocal-barrier matrix penalty $\Phi_\Pi(A) = -\Pi^2(A-\Pi I)^{-1} - \Pi I$ solves the general NLP-SDP class $\min f(x,Y)$ s.t. $g_i \le 0$, $h_i = 0$, $A_i(x,Y) \succeq 0$, $\underline{\lambda}_i I \preceq Y_i \preceq \overline{\lambda}_i I$ in pure MATLAB, handling linear SDP, BMI, PMI, and AMPL-NLP inputs through a unified interface.

## Method
Outer loop = nonlinear-rescaling / Polyak modified-barrier augmented Lagrangian; inner loop = damped Newton on the augmented Lagrangian with `ldl`/MA57 factorization + inertia correction, Armijo line-search via an augmented-Lagrangian merit function. Inequalities use the Ben-Tal/Zibulevsky $\varphi_{\bar\tau}$ penalty; matrix inequalities use $\Phi_\Pi(A) = -\Pi^2(A-\Pi I)^{-1} - \Pi I$ which yields closed-form first/second derivatives. Penalty parameters $\pi,\Pi \to 0$ geometrically while Lagrange multipliers $u, \Xi, U, \overline U$ are updated by the derivative-rescaling formula $u^{\ell+1} = u^\ell \varphi'_{\pi^\ell}(g)$.

## Result
PENLAB solves the same problem classes as PENNON (C) and the NAG implementation with comparable iteration counts but slower wall-clock due to MATLAB overhead. Demonstrated on (i) nearest-correlation-matrix with bounded condition number $\kappa$ (reformulated via $X = \zeta\tilde X$, $I \preceq \tilde X \preceq \kappa I$); (ii) truss topology optimization with global linear-buckling stability constraint $K(x) + G(x) \succeq 0$; (iii) static output feedback via polynomial matrix inequality $H(k) \succ 0$ on COMPlib (solved 30+ small instances, n<10, mp<20). Pre-programmed interfaces for AMPL NLP, SDPA linear SDP, BMI, and PMI.

## Why it matters here
General background for SDP/NLP-SDP tooling; no direct Einstein-Arena tie — the wiki's existing LP/SDP work (Cohn–Elkies, flag-algebra) is linear-SDP territory where PENLAB has no advantage over HiGHS/MOSEK/SDPA. Potentially relevant if any arena problem ever needs *nonlinear* matrix inequalities (truss-style buckling, polynomial MI from polynomial feasibility), but not for current 23-problem inventory.

## Open questions / connections
- Could the $\Phi_\Pi(A) = -\Pi^2(A-\Pi I)^{-1} - \Pi I$ matrix-barrier idea be repurposed as a smooth surrogate for spectral constraints in problems where mpmath polish currently dominates?
- PMI formulation (Section 6.4, 7.3) — does any arena problem admit a polynomial-matrix-inequality lift cheaper than its native form?
- Extends Polyak (1992) modified-barrier theory and Ben-Tal/Zibulevsky (1997) penalty/barrier multiplier method to matrix variables; same lineage as augmented-Lagrangian SDP work by Sun/Sun/Zhang.

## Key terms
nonlinear semidefinite programming, augmented Lagrangian, modified barrier method, penalty function, matrix inequality, PENNON, PENLAB, NLP-SDP, polynomial matrix inequality, bilinear matrix inequality, nearest correlation matrix, truss topology optimization, static output feedback, Polyak nonlinear rescaling, Ben-Tal Zibulevsky penalty
