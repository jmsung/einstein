---
type: source
kind: paper
title: On the size of Bruhat intervals
authors: Federico Castillo, Damian de la Fuente, Nicolás Libedinsky, D. Plaza
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2309.08539
source_local: ../raw/2023-castillo-size-bruhat-intervals.pdf
topic: general-knowledge
cites:
---

# On the size of Bruhat intervals

**Authors:** Federico Castillo, Damian de la Fuente, Nicolás Libedinsky, D. Plaza  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2309.08539

## One-line
Gives a convex-geometry formula expressing the cardinality of lower Bruhat intervals $[id,\theta(\lambda)]$ in affine Weyl groups as a weighted sum of volumes of faces of the orbit polytope $\mathrm{Conv}(W_f\cdot\lambda)$.

## Key claim
**Theorem A (Lattice Formula):** for every dominant coweight $\lambda$, $|\!\le\!\theta(\lambda)| = |W_f|\cdot|\mathrm{Conv}(W_f\cdot\lambda)\cap(\lambda+\mathbb{Z}\Phi^\vee)|$. **Theorem B (Geometric Formula):** there exist unique constants $\mu^\Phi_J\in\mathbb{R}$ (independent of $\lambda$) such that $|\!\le\!\theta(\lambda)| = \sum_{J\subseteq\{1,\dots,n\}} \mu^\Phi_J\,\mathrm{Vol}(F_J)$, where $F_J=\mathrm{Conv}(W_J\cdot\lambda)$ is the face of the orbit polytope. Some $\mu^\Phi_J$ can be negative (e.g. in $A_4$).

## Method
Identifies $\le\theta(\lambda)$ with a union of $W_f$-translates of the fundamental Weyl chamber tile to bring in lattice-point counting of the orbit (generalized permutohedron) polytope. Then applies the Berline–Vergne / Pommersheim–Thomas local Euler–Maclaurin formula, which writes $|P\cap\Gamma|$ as a sum over faces $F$ of $\nu(t(F,P))\cdot\mathrm{relVol}(F)$, exploiting that $\nu$ on transverse cones is invariant under lattice translation and orthogonal symmetry, hence constant on $W_f$-orbits of faces. Quasi-polynomiality (McMullen) is upgraded to polynomiality via a vanishing lemma. For $A_n$ with connected $J$, closed forms are extracted using Ferroni's hypersimplex Ehrhart coefficients and Stirling numbers.

## Result
For type $A_n$ and the connected block $J=\{1,\dots,l\}$, $\mu^{A_n}_J = \tfrac{l!\sqrt{l+1}}{(n+1)}\genfrac{[}{]}{0pt}{}{n+1}{l+1}$ (Stirling number of the first kind). Extremes: $\mu^\Phi_\varnothing = |W_f|$ and $\mu^\Phi_{I_n} = 1/\mathrm{Vol}(A_{id})$, with values tabulated for $A_n,B_n,C_n,D_n,E_6,E_7,E_8,F_4,G_2$. Consequence: $|\!\le\!\theta(\lambda)|$ is an honest polynomial of degree $n$ in the coweight coordinates $(m_1,\dots,m_n)$.

## Why it matters here
General background; no direct arena tie — affine Weyl combinatorics / Kazhdan–Lusztig theory sit outside the current 23 Einstein Arena problems (sphere packing, autocorrelation, kissing, etc.). The polytope-faces ↔ lattice-points bridge (Berline–Vergne, Pick generalization) and the permutohedron face decomposition are reusable conceptual tools, but not load-bearing for present problems.

## Open questions / connections
- Conjectured extension: a partition of $W_a$ such that *every* lower Bruhat interval has a face-volume formula with different $\mu_J$ per block.
- Formula for $|\not\ge x|$ (non-convex star-shaped complement) would, with Theorem B, yield $|[x,y]|=|\!\le y|-|\!\not\ge x|+P(x,y)$ — a full interval cardinality formula.
- Extends Postnikov's permutohedra-of-general-type program (lattice points of non-regular permutohedra had no prior combinatorial interpretation).
- Connects strong vs weak Bruhat order to lattice points vs vertices of the orbit polytope (heuristic dual).

## Key terms
affine Weyl group, Bruhat interval, lower interval cardinality, orbit polytope, permutohedron, dominant coweight, $\theta(\lambda)$, Berline–Vergne local Euler–Maclaurin, transverse cone, normal cone, Pommersheim–Thomas, Pick's theorem generalization, hypersimplex Ehrhart polynomial, Stirling numbers of the first kind, Eulerian numbers, Kazhdan–Lusztig polynomial, Soergel bimodules, Postnikov permutohedra, lattice point counting, quasi-polynomial, Coxeter combinatorics
