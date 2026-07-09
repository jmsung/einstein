---
type: source
kind: paper
title: Optimization-Aided Construction of Multivariate Chebyshev Polynomials
authors: Mareike Dressler, Simon Foucart, Mioara Joldes, Etienne de Klerk, Jean Bernard Lasserre, Yuan Xu
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2405.10438v3
source_local: ../raw/2024-dressler-optimization-aided-construction-multivariate-c.pdf
topic: general-knowledge
cites: 
---

# Optimization-Aided Construction of Multivariate Chebyshev Polynomials

**Authors:** Mareike Dressler, Simon Foucart, Mioara Joldes, Etienne de Klerk, Jean Bernard Lasserre, Yuan Xu  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2405.10438v3

## One-line
Uses the Moment-SOS / SDP hierarchy to compute best uniform approximants to monomials by lower-degree polynomials over the simplex, cross-polytope, euclidean ball, and hypercube — producing both numerical tables and a few new closed-form multivariate Chebyshev polynomials.

## Key claim
For $d=3$ and degrees $n\le 6$, the authors tabulate $E(k,\Omega) := \min_{p\in P^d_{n-1}} \|m_k - p\|_\Omega$ on $\Omega\in\{B,C,S\}$ — most values previously unknown — and derive two new explicit Chebyshev polynomials: for $m_{(2,2,1)}=x_1^2x_2^2x_3$ on $B$, $E=a\approx 3.630\times 10^{-2}$ with extremizer $m_{(2,2,1)}+a\,T_3(x_3)$; for $m_{(2,1,1)}=x_1^2x_2x_3$ on $S$, $E=1/(2c^2)$ where $c=-3/\tau$ and $\tau$ solves $\max_{y\in[0,1/2]} y(1-2y)(y-\tau)^2 = \tau^2/18$.

## Method
Reformulates the convex program $\min_p \|m_k-p\|_\Omega$ as a Generalized Moment Problem (GMP) using strong duality and the notion of an **extremal signature** (a $\pm 1$-valued function on extremal points of $f-v^*$ that annihilates $V$). The dual is solved via the **Moment-SOS hierarchy** (Lasserre / Putinar Positivstellensatz): primal cone $Q(g_1,\dots,g_H)_t$ truncated to degree $2t$ becomes an SDP, dual gives pseudo-moment Hankel matrices $\text{Hank}_t(y)\succeq 0$. Implemented in GloptiPoly 3 (matlab); atomic measure extraction recovers candidate signature points, which are then verified analytically via the Hahn-Banach / Krein-Milman characterization (Rivlin Thm 2.6).

## Result
Complete $3$-variable tables of best-approximation errors up to degree 6 on $B$, $C$, $S$ (Tables 1-3). All cross-polytope values are new. The two new analytic Chebyshev polynomials are verified by exhibiting an explicit signature support (boundary points of $B$ / face $x_1+x_2+x_3=1$ of $S$) and showing $|m_k - p^*|$ attains its maximum on $S$ and is bounded by the claimed value throughout $\Omega$. **Conjecture:** for the euclidean ball, extremal signatures live on the sphere boundary in all monomial cases.

## Why it matters here
General background for SDP/Moment-SOS machinery — the same Lasserre hierarchy underlies LP/SDP bounds in arena problems (sphere packing P1, kissing-number bounds, autocorrelation extremals). The dual-via-signatures viewpoint and GloptiPoly-style atomic-measure extraction are directly transferable to verifier-design and equioscillation-style certificate construction (cf. wiki/concepts/equioscillation, findings/equioscillation-active-triple-diagnostic); no direct arena-problem tie but a useful tooling reference.

## Open questions / connections
- Does the conjecture "signatures live on $\partial B$ (the sphere)" extend to all monomials and all $d$? Would mirror the boundary-localization of equioscillation extrema.
- Companion paper (arXiv:2405.19219, ref [5]) treats interpretation (3) — sum-of-coefficients monic — with explicit formulas; useful contrast.
- Extension to $L^1, L^{2m}$ norms, unions of domains, shape constraints (Basc-style) — proposed in §5 as the multivariate analog of the constrained-approximation toolbox.
- Connection between best approximants on $S$ to $m_k$ and on $B$ to $m_{2k}$ (Xu 2004) — a square-root reduction that could compress wiki problem mappings.

## Key terms
Chebyshev polynomials, multivariate approximation, best approximation, Moment-SOS hierarchy, Lasserre hierarchy, semidefinite programming, sum-of-squares, Putinar Positivstellensatz, extremal signature, GloptiPoly, simplex, cross-polytope, euclidean ball, quadratic module, Hankel matrix, pseudo-moments
