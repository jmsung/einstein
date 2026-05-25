---
type: source
kind: paper
title: The equivariant Kazhdan-Lusztig polynomial of a matroid
authors: Katie R. Gedeon, N. Proudfoot, Benjamin Young
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1605.01777
source_local: ../raw/2016-gedeon-equivariant-kazhdan-lusztig-polynomial-matroid.pdf
topic: general-knowledge
cites:
---

# The equivariant Kazhdan-Lusztig polynomial of a matroid

**Authors:** Katie R. Gedeon, N. Proudfoot, Benjamin Young  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1605.01777

## One-line
Defines an equivariant refinement of the Kazhdan-Lusztig polynomial of a matroid, with coefficients living in virtual representations of a symmetry group $W$, and computes it explicitly for uniform matroids and small braid matroids.

## Key claim
For the uniform matroid $U_{m,d}$ with its natural $S_{m+d}$-action, the coefficient of $t^i$ ($i>0$) in the equivariant KL polynomial is the multiplicity-free sum $C_{m,d,i} = \bigoplus_{b=1}^{\min(m,d-2i)} V[d+m-2i-b+1, b+1, 2^{i-1}]$ (Theorem 3.1), confirming the non-negativity conjecture $P_M^W(t) \in \mathrm{grRep}(W)$ for all uniform matroids (Corollary 3.2).

## Method
Categorifies the recursive definition of $P_M(t)$ from Elias-Proudfoot-Wakefield by replacing integer coefficients with virtual $W$-representations, using the equivariant characteristic polynomial $H_M^W(t)$ built from Orlik-Solomon algebra pieces. Translates everything to symmetric functions via the Frobenius characteristic and proves Theorem 3.1 by manipulating three-variable generating functions $P(t,u,x)$ until verification reduces to repeated applications of the Pieri rule (avoiding the harder Littlewood-Richardson rule). A novel exact-sequence argument (Lemma 2.4) replaces Möbius inversion, which fails equivariantly because the equivariant Möbius algebra is non-associative.

## Result
Closed-form multiplicity-free formula for all $C_{m,d,i}$ of uniform matroids; explicit computations of $D_{n,i}$ for braid matroids $B_n$ up to $n=9$, $i \le 3$; formula for the linear-coefficient $D_{n,1}$ for all $n$ (Proposition 4.4, showing it is *not* representation stable). Introduces equivariant log concavity (Conjecture 5.3) and proves it for the equivariant characteristic polynomial of uniform matroids (Proposition 5.7) via Remmel's Schur tensor-product formula. Also establishes representation stability in the Church-Farb sense for $(C_{m,d,i})_{d \in \mathbb{N}}$ with stable range $d \ge m+2i$.

## Why it matters here
General background; no direct arena tie. The techniques (Pieri-rule generating-function bookkeeping, Frobenius characteristic, equivariant log concavity, representation stability) are deep symmetric-function and matroid machinery far from the optimization / packing / autocorrelation problems on Einstein Arena. Possible distant relevance: matroid log-concavity (Adiprasito-Huh-Katz) sits adjacent to the extremal-combinatorics findings the wiki tracks.

## Open questions / connections
- No philosophical explanation for the symmetry $C_{m,d,i} = C_{d-2i, m+2i, i}$ (Remark 3.5) — first observed empirically.
- No general closed form for the braid matroid equivariant KL polynomial $Q_n(t)$; only a recursion (Equation 6) and SAGE computations are available.
- Conjecture 2.13 (positivity $P_M^W(t) \in \mathrm{grRep}(W)$) and Conjecture 5.3 (equivariant log concavity of both $H_M^W$ and $P_M^W$) remain open in general; the uniform case provides the only non-realizable evidence.

## Key terms
Kazhdan-Lusztig polynomial, matroid, equivariant, uniform matroid, braid matroid, Orlik-Solomon algebra, Frobenius characteristic, symmetric functions, Pieri rule, Schur functions, representation stability, log concavity, Church-Farb, Adiprasito-Huh-Katz, Remmel formula, intersection cohomology, reciprocal plane, Proudfoot
