---
type: source
kind: paper
title: A Constrained Optimization Approach for Constructing Rigid Bar Frameworks with Higher-order Rigidity
authors: Xuenan Li, Christian D. Santangelo, Miranda Holmes-Cerfon
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2509.23072v2
source_local: ../raw/2025-li-constrained-optimization-approach-constructing.pdf
topic: general-knowledge
cites:
---

# A Constrained Optimization Approach for Constructing Rigid Bar Frameworks with Higher-order Rigidity

**Authors:** Xuenan Li, Christian D. Santangelo, Miranda Holmes-Cerfon  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2509.23072v2

## One-line
A systematic method to generate prestress-stable (and third-order rigid) bar frameworks by solving a constrained optimization problem that maximizes or minimizes one edge length while holding all other edge lengths fixed.

## Key claim
Local optima of the edge-length objective $f_k(p) = |p_{k,1}-p_{k,2}|^2$ subject to the remaining length constraints are, under LICQ plus the standard second-order sufficient conditions, prestress-stable frameworks (Theorems 3.3, 3.5); conversely, any edge carrying nonzero self-stress $\omega_k$ in a prestress-stable framework is at a local min ($\omega_k>0$) or local max ($\omega_k<0$) of its squared length on the constraint manifold (Theorem 3.6).

## Method
Reformulate rigidity in optimization language: the KKT Lagrange multiplier $\lambda^*$ of $(P_k^\pm)$ equals (up to scaling) a self-stress $\omega \in \ker R(p)^T$ (Lemma 3.1), and the second-order sufficient condition $v^T \nabla_p^2 \mathcal{L}(p^*,\lambda^*) v > 0$ on the critical cone $C_k(p^*) = \ker R(p^*)\cap T(p^*)^\perp$ coincides with the prestress-stability inequality $\omega^T R(v) v > 0$. Numerically, projected-gradient descent with Newton projection back to the constraint manifold (Algorithm 1, after Zappa–Holmes-Cerfon–Goodman 2018) finds the optima from a perturbed first-order rigid seed. Third-order rigidity is engineered via bifurcation: vary a second edge length until a local min and local max of $f_1$ merge into a cubic critical point with $\dim K(p^*)=1$ (Theorem 5.4).

## Result
Theorems 3.3/3.5 guarantee prestress stability with no first-order rigidity at isostatic/under-constrained solutions; Theorem 3.6 inverts the construction (every $\omega_k\neq 0$ edge is at an optimum). A force-density-style generalization lets one prescribe either edge length or stress component on chosen edges. The bifurcation scheme is demonstrated on a 6-vertex, 9-edge 2D two-triangle framework where tuning $|P_1P_4|$ collapses a max/min pair on the $|P_2P_5|(\alpha)$ curve to a cubic critical point (second-order stress test $\approx -7.9\times 10^{-5}$, residual derivative $\sim 10^{-8}$), yielding a third-order rigid framework. Limitation: produces only 1-dimensional self-stress spaces (forced by LICQ); multi-self-stress constructions require simultaneous critical points of multiple $f_k$ and appear to need special symmetry (illustrated in fig. 7 with $\angle ACB = \angle DCE$).

## Why it matters here
Directly informs the basin-rigidity / contact-graph-rigidity machinery used in sphere/disk packing problems (P11 kissing, P17/P18 disk-in-rectangle, P23 kissing $d=16$): prestress stability is precisely what stabilizes near-isostatic packings without first-order rigidity, and the KKT↔self-stress duality gives a constructive recipe for generating non-symmetric test configurations and for interpreting "stuck" SLSQP/active-pair polishes as critical points of a length-extremization problem on the contact manifold. Connects to the equioscillation/active-triple diagnostic by reframing it through Lagrange multipliers.

## Open questions / connections
- How to construct frameworks with $\geq 2$ linearly independent self-stresses without imposing symmetry (open per Section 6) — relevant when contact graphs in P11/P17 have multiple dependencies.
- Extension to inequality constraints (tensegrity / one-sided contacts) — would directly model sphere packings where edges are contact distances rather than fixed lengths.
- Higher-order ($k>3$) rigid frameworks via richer catastrophe-theory bifurcations (cusp, swallowtail) when multiple edges are tuned.
- Relation to Gortler–Holmes-Cerfon–Theran 2025 (arXiv:2506.03108) on $(1,k)$-flexes and the Heaton–Timme numerical-algebraic-geometry catastrophe approach.

## Key terms
prestress stability, first-order rigidity, second-order rigidity, third-order rigidity, bar framework, self-stress, rigidity matrix, KKT conditions, Lagrange multiplier, LICQ, critical cone, bifurcation theory, isostatic framework, tensegrity, force-density method, Holmes-Cerfon, Connelly–Whiteley, contact graph, basin rigidity
