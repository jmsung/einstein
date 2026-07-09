---
type: source
kind: paper
title: Lifting for Simplicity: Concise Descriptions of Convex Sets
authors: Hamza Fawzi, João Gouveia, Pablo A. Parrilo, James Saunderson, Rekha R. Thomas
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2002.09788v2
source_local: ../raw/2020-fawzi-lifting-simplicity-concise-descriptions.pdf
topic: general-knowledge
cites: 
---

# Lifting for Simplicity: Concise Descriptions of Convex Sets

**Authors:** Hamza Fawzi, João Gouveia, Pablo A. Parrilo, James Saunderson, Rekha R. Thomas  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2002.09788v2

## One-line
A selective survey of lifts of convex sets — expressing a complicated convex set as the linear projection of a simpler higher-dimensional convex set (polyhedral, second-order, or spectrahedral) — covering existence, construction via sums-of-squares, and obstructions.

## Key claim
A convex set $C \subset \mathbb{R}^n$ admits a $K$-lift (for a closed convex cone $K$) iff its slack operator factorizes through $K$ and $K^*$. The inclusion chain polyhedral $\subsetneq$ second-order cone $\subsetneq$ spectrahedral $\subsetneq$ convex semialgebraic is strict (Scheiderer [Sch18]: the cone $C_{n,2d}$ of degree-$2d$ nonneg polynomials in $n$ variables has no spectrahedral lift for sufficiently large $n,d$).

## Method
Unifies polyhedral and spectrahedral lifts under the conic framework $C = \pi(K \cap L)$. The core tool is Yannakakis' slack-matrix theorem, generalized to a slack-operator factorization for arbitrary convex bodies. Construction proceeds via sums-of-squares certificates (Lasserre/Parrilo hierarchies); obstructions come in two flavors — facial-structure (long chains of faces) and algebraic (degree of algebraic boundary, semialgebraic-function smoothness arguments).

## Result
- Permutahedron $\Pi_n$: linear extension complexity $O(n \log n)$ via sorting networks (Goemans).
- Any 0/1 polytope in $\mathbb{R}^n$ has a polyhedral lift of size $\le \frac{6}{n^2} \cdot 5 \cdot 2^n$ (via OBDDs).
- Odd parity polytope: lift of size $4n-2$.
- Cut and TSP polytopes have super-polynomial semidefinite extension complexity [LRS15].
- Matching polytope has no small polyhedral lift [Rot17].
- Nonneg-polynomial cone $C_{n,2d}$ has no spectrahedral lift (Theorem 5.16) — proved via semialgebraic smoothness + a polynomial-is-SOS-of-smooth-functions reduction.

## Why it matters here
Directly relevant to **P1 (sphere packing via Cohn–Elkies LP)** and any SDP-relaxation strategy: the paper formalizes when SDP lifts exist and gives algebraic obstructions, complementing the wiki's `findings/sdp-relaxation-uselessness`. The Lovász theta body discussion (§2.2) and theta-bodies hierarchy ground extremal-graph approaches; the conic factorization view informs LP-duality and dual-bound work across arena problems.

## Open questions / connections
- Does the matching polytope have small *semidefinite* extension complexity? (Open.)
- Concrete polytope families exhibiting large gap between linear and semidefinite extension complexity (only mild gaps known [FSP16]).
- Complexity of *deciding* whether a given convex set $C$ admits a $K$-lift — open under V/H-representation when $P=Q$.
- Connection to hyperbolicity cones and relative entropy cones as alternative lift targets.
- Extends Yannakakis [Yan91]; generalized by Scheiderer [Sch18], Fawzi [Faw19, Faw21].

## Key terms
extension complexity, slack matrix, slack operator, spectrahedral lift, polyhedral lift, Yannakakis factorization, sum of squares, Lasserre hierarchy, Sherali-Adams, Lovász theta body, semidefinite programming, conic programming, nonnegative rank, psd rank, Birkhoff polytope, permutahedron, cut polytope, Parrilo, Scheiderer, semialgebraic
