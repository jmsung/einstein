---
type: source
kind: paper
title: Module Structure on Invariant Jacobians
authors: N. Xi
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.6131
source_local: ../raw/2012-xi-module-structure-invariant-jacobians.pdf
topic: general-knowledge
cites:
---

# Module Structure on Invariant Jacobians

**Authors:** N. Xi  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.6131

## One-line
Proves Stephen Yau's 1985 conjecture (originally for $SL_2(K)$) for arbitrary connected semisimple algebraic groups: when the Jacobian ideal $J(f)$ of a homogeneous polynomial of degree $>2$ is $G$-invariant, $J(f)$ is a quotient module of the defining representation $V$.

## Key claim
For $G$ connected semisimple over an algebraically closed field of characteristic 0, with rational representation on $V = K^n$ and induced action $\tau$ on $A = K[x_1,\dots,x_n]$: (a) the map $A \otimes V \to A$, $f \otimes e_i \mapsto \partial f/\partial x_i$ is a $G$-module homomorphism; (b) if $f$ is invariant, $J(f)$ is a quotient of $V$; (c) if $\deg f > 2$ and $J(f)$ is invariant, $J(f)$ is a quotient of $V$. Yau's original conjecture (highest weights of $J(f)$ ⊂ highest weights of $A_1$ for $SL_2$) follows as a corollary since $A_1 \cong V^*$.

## Method
Direct representation-theoretic computation: verify on a monomial basis $f = x_1^{a_1}\cdots x_n^{a_n}$ that the partial-derivative map intertwines the $G$-action, using the dual relationship between the action on $V$ (matrix $a_{ji}(t)$) and on coordinates (matrix $a_{kj}(t^{-1})$), so that $\sum_j a_{kj}(t^{-1}) a_{ji}(t) = \delta_{ki}$ collapses the sum. Then invokes Kempf's Theorem 13 ([K] 1993) to reduce the $\deg f > 2$ case to the invariant-$f$ case.

## Result
Full theorem above; settles Yau's conjecture in full generality, superseding the prior partial results: $n \leq 5$ [Y4], $A_1$ irreducible [SYY], scattered cases for $n = 6, 8$ [Yu, YYZ], and Kempf's projectively-smooth / irreducible-$\rho$ cases [K]. The proof is short (≈ 2 pages) once the module-homomorphism observation is made.

## Why it matters here
General background; no direct arena tie — this is pure invariant theory / singularity theory, not extremal combinatorics or packing. Marginal relevance only if a future Einstein problem invokes invariant polynomial ideals or $G$-module decompositions of Jacobians.

## Open questions / connections
- Extends/completes the line [Y1–Y5, SYY, Yu, YYZ, K] classifying $SL_2$-invariant Jacobian ideals from singularity theory.
- The degree-2 case is not covered (and is genuinely different — quadratic $f$ can have $J(f) = V^*$ without $f$ invariant).
- Connection back to Yau's original motivation: classification of isolated hypersurface singularities via their moduli/gradient algebras [NY].

## Key terms
invariant Jacobian, Yau conjecture, semisimple algebraic group, rational representation, highest weight, quotient module, $SL_2(K)$-action, Kempf theorem, gradient space, moduli algebra, isolated hypersurface singularity, invariant theory
