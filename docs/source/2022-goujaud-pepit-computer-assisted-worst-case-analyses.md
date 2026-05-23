---
type: source
kind: paper
title: "PEPit: computer-assisted worst-case analyses of first-order optimization methods in Python"
authors: Baptiste Goujaud, Céline Moucer, François Glineur, J. Hendrickx, Adrien B. Taylor, Aymeric Dieuleveut
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2201.04040
source_local: ../raw/2022-goujaud-pepit-computer-assisted-worst-case-analyses.pdf
topic: general-knowledge
cites:
---

# PEPit: computer-assisted worst-case analyses of first-order optimization methods in Python

**Authors:** Baptiste Goujaud, Céline Moucer, François Glineur, J. Hendrickx, Adrien B. Taylor, Aymeric Dieuleveut  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2201.04040

## One-line
A Python package that automates worst-case convergence analysis of first-order optimization methods by recasting performance estimation problems (PEPs) as semidefinite programs (SDPs) solved numerically.

## Key claim
For a wide family of first-order methods (gradient, proximal, Bregman, linear-optimization, splitting, stochastic), tight worst-case rates can be computed automatically: the user writes the algorithm "as they would implement it," and PEPit handles the SDP modeling. The illustrative result is the tight gradient-descent contraction factor $\tau(\mu,L,\gamma) = \max\{(1-L\gamma)^2,(1-\mu\gamma)^2\}$ on $\mathcal F_{\mu,L}$.

## Method
Cast worst-case computation as a maximization over functions in a class $\mathcal F$ subject to algorithmic update equations and an initial condition. Replace the infinite-dimensional function variable by a finite set of sampled $(x_i, g_i, f_i)$ triples constrained by *interpolation conditions* (e.g. Theorem 1 for smooth strongly convex functions: $f_i \ge f_j + \langle g_j, x_i - x_j\rangle + \tfrac{1}{2L}\|g_j-g_i\|^2 + \tfrac{\mu}{2(L-\mu)}\|x_i-x_j-\tfrac{1}{L}(g_i-g_j)\|^2$). Convexify by Gram-matrix lifting $G \succeq 0$ over inner products of iterates/gradients → an SDP solved by CVXPY/MOSEK/SCS.

## Result
PEPit ships ~75 worked examples spanning unconstrained / composite / stochastic / monotone-inclusion settings. Case studies show PEPit recovering and *improving* published bounds: accelerated gradient under $\mathcal F_{\mu,L}$ (tightens [d'Aspremont–Scieur–Taylor]), accelerated Douglas-Rachford splitting (tightens the quadratic-case bound of Patrinos–Stella–Bemporad to the full $L$-smooth $\mu$-strongly convex case), and point-SAGA Lyapunov contraction (slight tightening over Defazio's $1/(1+\mu\gamma)$).

## Why it matters here
General background; no direct arena tie. PEPs are an SDP-based methodology specific to first-order optimization analysis, not to the geometric/extremal/sphere-packing problems on Einstein Arena. The closest indirect link is the *interpolation-conditions trick* (characterize a function class by pairwise inequalities so the worst-case problem becomes finite-dimensional), which is a useful abstract template if a future arena problem demands tight rates for an iterative scheme.

## Open questions / connections
- Could the interpolation-conditions trick be adapted to give SDP-tight bounds on iterative refinement loops we use (e.g. SLSQP active-pair polish, mpmath ulp polish convergence)?
- Authors flag future extensions: automated Lyapunov-function search, automated *disproofs* of convergence, distributed/decentralized PEPs — relevant if we ever build agentic optimizer-verifier loops.
- Relation to IQC / dissipativity (Lessard–Recht–Packard) — alternative control-theoretic route to the same worst-case rates.

## Key terms
performance estimation problem, PEP, semidefinite programming, SDP, interpolation conditions, smooth strongly convex, gradient descent contraction, Gram matrix lifting, accelerated gradient method, Douglas-Rachford splitting, point-SAGA, Lyapunov function, IQC, Taylor-Hendrickx-Glineur, first-order methods
