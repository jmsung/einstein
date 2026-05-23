---
type: source
kind: paper
title: Which nonnegative matrices are slack matrices
authors: J. Gouveia, R. Grappe, V. Kaibel, Kanstantsin Pashkovich, Richard Z. Robinson, Rekha R. Thomas
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1303.5670
source_local: ../raw/2013-gouveia-which-nonnegative-matrices-slack.pdf
topic: general-knowledge
cites:
---

# Which nonnegative matrices are slack matrices

**Authors:** J. Gouveia, R. Grappe, V. Kaibel, Kanstantsin Pashkovich, Richard Z. Robinson, Rekha R. Thomas  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1303.5670

## One-line
Characterizes which nonnegative matrices arise as slack matrices of polyhedral cones and polytopes, and reduces the recognition problem to the polyhedral verification problem.

## Key claim
A nonnegative matrix $M \in \mathbb{R}_+^{p\times q}$ is a slack matrix of a polyhedral cone iff $\mathbb{R}_+^p \cdot M = \mathbb{R}^p \cdot M \cap \mathbb{R}_+^q$ (the row cone equals the nonnegative part of the row span, RCGC); it is a slack matrix of a polytope iff additionally $\mathrm{rank}(M)\geq 2$ and $\mathbf{1} \in M \cdot \mathbb{R}^q$. Equivalently (combinatorial form, Thm 22/24): $M$ is a polytope slack matrix iff $M^{\mathrm{inc}}$ is the incidence matrix of some $(\mathrm{rank}(M)-1)$-dimensional polytope and $\mathbf{1}$ lies in the column span.

## Method
Linear-algebraic: factor $M = AB$ (rank factorization), interpret rows of $A$ as cone generators and columns of $B$ as facet normals, then use cone duality (RCGC $\Leftrightarrow$ CCGC via Proposition 2) and the homogenization cone $P_h$ to bridge polytope/cone cases. Combinatorial direction uses nerves of polyhedral complexes and homotopy-equivalence to a $(d-1)$-sphere (Björner) to show $F = \partial Q$.

## Result
(i) Theorems 1 and 6 give the linear-algebraic characterizations (RCGC/CCGC + $\mathbf{1}$ in column span). (ii) An explicit algorithm checks CCGC by H-to-V conversion of the cone $M\cdot\mathbb{R}^q \cap \mathbb{R}_+^p$; polynomial time for fixed rank (Theorem 20). (iii) Theorem 21: slack-matrix recognition (cones, polytopes, RCGC/CCGC) is polynomial-time equivalent to the polyhedral verification problem (complexity open; in coNP). (iv) Combinatorial characterizations (Thms 22, 24); polygons admit the cyclic-band Corollary 23.

## Why it matters here
General background; no direct arena tie. Closest relevance is to LP-bound / SDP-bound machinery (Yannakakis factorization, nonnegative/PSD rank of slack matrices) that underlies extension-complexity arguments — potentially adjacent to autocorrelation/sphere-packing LP duality but no direct numerical bound for any of the 23 problems.

## Open questions / connections
- Is there a family of polytope slack matrices with exponential gap between nonnegative rank and PSD rank? (Would demonstrate SDP > LP power for lifts.)
- Complexity of polyhedral verification problem itself remains open — equivalent to output-sensitive facet enumeration.
- Extends Yannakakis (1991) factorization theorem and Gouveia-Parrilo-Thomas (cone factorizations of convex sets).
- For $d \geq 4$, recognizing incidence matrices of $d$-polytopes is NP-hard (Richter-Gebert), bounding combinatorial-side tractability.

## Key terms
slack matrix, nonnegative rank, polyhedral cone, polytope, extension complexity, Yannakakis factorization, RCGC, CCGC, polyhedral verification, incidence matrix, positive semidefinite rank, cone lift, homogenization cone, Steinitz theorem
