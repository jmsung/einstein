---
type: source
kind: paper
title: Iterative Universal Rigidity
authors: R. Connelly, S. Gortler
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.7029
source_local: ../raw/2014-connelly-iterative-universal-rigidity.pdf
topic: general-knowledge
cites:
---

# Iterative Universal Rigidity

**Authors:** R. Connelly, S. Gortler  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.7029

## One-line
A complete necessary-and-sufficient characterization of universal rigidity for any bar framework $(G,p)$ in any dimension, via an iterated sequence of PSD stress matrices on nested affine subsets of configuration space.

## Key claim
A framework $(G,p)$ is universally rigid iff it admits a finite sequence of PSD equilibrium "restricted stress matrices" $\Omega_1^*, \Omega_2^*, \ldots, \Omega_k^*$ (each PSD on the affine set carved out by its predecessors) whose ranks sum to $n-d-1$, AND the edge directions do not lie on a conic at infinity. This extends the classical single-stress sufficient condition of Connelly (1982) and the generic necessary condition of Gortler–Thurston (2014) to all (non-generic) frameworks.

## Method
Iterated facial reduction of the PSD cone applied to the framework's measurement set $M(G) \subset \mathbb{R}^m$. At each step, find a PSD stress matrix $\Omega_i$ whose restriction $\Omega_i^* = B_{i-1}\Omega_i B_{i-1}^t$ to the current affine set $A_{i-1}$ is nonzero, satisfying the restricted equilibrium constraint $P\Omega_i B_{i-1}^t = 0$; update the basis $B_i$ to the cokernel; repeat until either $\sum \text{rank}(\Omega_i^*) = n-d-1$ (dimensionally rigid) or no further PSD stress exists. Posed as an SDP feasibility problem, often solvable exactly when the space of candidate $\Omega_i^*$ is one-dimensional or rank-1.

## Result
Theorem 8.1: $(G,p)$ is dimensionally rigid in $\mathbb{R}^d$ iff this iteration terminates with $\sum \text{rank}(\Omega_i^*) = n-d-1$; combined with the conic-at-infinity check (Corollary 5.1.1) this gives universal rigidity. The certificate is verifiable in polynomial time in the BSS real computation model, placing universal rigidity in NP ∩ co-NP under that model. Worked examples (ladder, 4-pole, hidden-stress framework) show frameworks needing 2-3 iteration levels with no single-stress certificate.

## Why it matters here
General background for any Einstein Arena problem cast as a distance-geometry / framework rigidity certificate — particularly relevant to sphere-packing contact graphs, kissing configurations, and Hardin-Sloane-style discrete-geometry problems where local-optimality proofs hinge on stress matrices. The iterated PSD-stress idea parallels SDP-hierarchy / facial-reduction techniques that may apply when single-shot SDP relaxations are degenerate (cf. wiki's `sdp-relaxation-uselessness` finding on P1).

## Open questions / connections
- Complexity of universal rigidity over integer input remains open (no hardness; no provably correct algorithm).
- How to systematically search for the PSD certificate when the cone of restricted equilibrium stresses is lower-dimensional than the full equilibrium space ("hidden stress" case, §15.4).
- Connection to body-and-bar generic global rigidity (Connelly–Jordán–Whiteley) and weavings/polarity (Whiteley) left as future directions.
- Extends Alfakih's dimensional rigidity framework; subsumed under Borwein–Wolkowicz facial reduction for conic programs.

## Key terms
universal rigidity, dimensional rigidity, stress matrix, PSD equilibrium stress, facial reduction, conic at infinity, super stability, bar framework, tensegrity, semidefinite programming, measurement set, Connelly, Gortler, Alfakih, affine flex, restricted equilibrium
