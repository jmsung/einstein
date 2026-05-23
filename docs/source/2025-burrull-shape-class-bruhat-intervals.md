---
type: source
kind: paper
title: Shape and class of Bruhat Intervals
authors: Gastón Burrull, Nicolás Libedinsky, Rodrigo Villegas
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.14033
source_local: ../raw/2025-burrull-shape-class-bruhat-intervals.pdf
topic: general-knowledge
cites:
---

# Shape and class of Bruhat Intervals

**Authors:** Gastón Burrull, Nicolás Libedinsky, Rodrigo Villegas  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.14033

## One-line
Bruhat intervals in affine Weyl groups (type $A_2$, partial $A_n$) are described as Euclidean regions — convex polygons minus star-shaped polygons — and isomorphisms between them are (conjecturally) realized by piecewise isometries.

## Key claim
For affine type $A_2$ and any $x,y \in W$: $z \in [x,y]$ iff $\mathrm{cen}(z) \in C_y \setminus \mathrm{St}^\circ(x)$ (Theorem A). For dominant thick intervals: $[x,y] \cong [x',y']$ as posets iff the associated polygons $\mathrm{Pgn}_{x,y}$ and $\mathrm{Pgn}_{x',y'}$ are isometric (Theorem C).

## Method
Geometric/combinatorial: identify $W$ with alcoves in Euclidean space, build the hexagon $C_y = \mathrm{Conv}(W_f \cdot y)$ and the star $\mathrm{St}(x)$ from two equilateral triangles, then define the gray-zone polygon $\mathrm{Pgn}_{x,y} := \mathrm{Gray} \cap (\mathrm{cen}(x) + \mathrm{cone}(\alpha_1,\alpha_2)) \cap (\mathrm{cen}(y) - \mathrm{cone}(\alpha_1,\alpha_2))$. Poset isomorphisms are tracked via piecewise translations $\tau_\lambda$, dihedral subintervals $D_x, D_y$ (which encode approximate Euclidean distances to polygon vertices), and length-counting invariants. SageMath verification for $A_2, A_3, A_4, B_2, B_3, C_3, G_2$.

## Result
Theorem A: full Euclidean description of all $A_2$ Bruhat intervals as $C_y \setminus \mathrm{St}^\circ(x)$. Theorem C: thick dominant intervals in $A_2$ classified up to poset iso by polygon isometry — only nontrivial isos are Dynkin flips ($\sigma$) and piecewise translations. Proposition B: $A_n$ generalization via parallelotopes $\mathrm{Par}^i_{x,y}$ on the dominant chamber. Proposition 7.7: non-recursive proof of CIC for thick $A_2$ intervals. Proposition 7.10: stabilization of $[x+N\lambda, y+N\lambda]$ for large $N$. Verified ~500 full intervals, ~$100^2$ pairs.

## Why it matters here
General background; no direct arena tie. The paper concerns affine Weyl group combinatorics / Kazhdan–Lusztig theory, not Einstein Arena's continuous-optimization problems (sphere packing, autocorrelation, kissing, etc.). The only loose connection is the broader Lie-theoretic / discrete-geometry milieu — translating combinatorial structure into convex polytope geometry — which is structurally reminiscent of LP-bound / Cohn-Elkies polytope intuitions but with no transferable technique.

## Open questions / connections
- Conjecture E: classify full Bruhat-interval isomorphisms in arbitrary affine Weyl groups via translations modulo Dynkin/inversion symmetries.
- Conjecture 8.2 / Approximate Miracle F: does the tiny subposet $D_x \cup D_y$ (dihedral neighbors) determine $[x,y]$? If true, gives a practical computational route to Kazhdan–Lusztig polynomials.
- Extends Björner–Ekedahl (shape of lower intervals) and Burrull–Libedinsky–Plaza (recursive CIC for $A_2$); leaves higher-rank polytope description $\mathrm{Pgn}^i_{x,y}$ open.

## Key terms
Bruhat interval, affine Weyl group, type $A_2$, type $A_n$, alcove geometry, generalized permutohedron, piecewise isometry, piecewise translation, Kazhdan–Lusztig polynomial, Combinatorial Invariance Conjecture, dihedral interval, dominant chamber, Hecke algebra, Coxeter system, weight polytope, coweight lattice, Björner–Ekedahl, Lusztig
