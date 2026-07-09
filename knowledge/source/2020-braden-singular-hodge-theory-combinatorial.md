---
type: source
kind: paper
title: Singular Hodge theory for combinatorial geometries.
authors: Tom Braden, June Huh, Jacob P. Matherne, N. Proudfoot, Botong Wang
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.06088
source_local: ../raw/2020-braden-singular-hodge-theory-combinatorial.pdf
topic: general-knowledge
cites:
---

# Singular Hodge theory for combinatorial geometries.

**Authors:** Tom Braden, June Huh, Jacob P. Matherne, N. Proudfoot, Botong Wang  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.06088

## One-line
Constructs an intersection cohomology module $IH(M)$ for an arbitrary matroid $M$, proves it satisfies the Kähler package, and uses this to settle the Top-Heavy conjecture and Kazhdan–Lusztig nonnegativity for all matroids.

## Key claim
For every (loopless) matroid $M$ of rank $d$: (1) $IH(M)$ satisfies Poincaré duality, hard Lefschetz, and the Hodge–Riemann relations (Theorem 1.6); (2) the Dowling–Wilson Top-Heavy conjecture holds — $|L_k(M)| \le |L_j(M)|$ with an injection $\iota: L_k \hookrightarrow L_j$ respecting $F \le \iota(F)$ for $k \le j \le \mathrm{rk}\,M - k$ (Theorem 1.1); (3) Kazhdan–Lusztig polynomials $P_M(t)$ and inverse KL polynomials $Q_M(t)$ have nonnegative coefficients, and $Z_M(t)$ is unimodal (Theorems 1.2, 1.5), with equivariant strengthenings (Theorems 1.3, 1.4).

## Method
Build the augmented Chow ring $\overline{\mathrm{CH}}(M)$ containing the graded Möbius algebra $H(M)$, define $IH(M)$ as the canonical indecomposable summand containing $H(M)$ (a Chow-theoretic analogue of intersection cohomology of the Schubert variety $Y$ when $M$ is realizable). Prove the Kähler package by a grand simultaneous induction on $|E|$ that interleaves Poincaré duality (PD), hard Lefschetz (HL), Hodge–Riemann (HR), canonical decomposition (CD), and a "no socle" (NS) statement, using deletion induction, Rouquier complexes, semi-small decomposition, and signature deformation arguments (Propositions 11.4–11.8). Numerical identities $P_M(t) = \sum \dim IH^k(M)_\varnothing\, t^k$ and $Z_M(t) = \sum \dim IH^k(M)\, t^k$ then transport nonnegativity/unimodality from Hodge theory to combinatorics.

## Result
Top-Heavy (with the de Bruijn–Erdős theorem as the rank-3 instance) is established for **all** matroids — not just those realizable over a field, which by [Nel18] are vanishingly rare. KL nonnegativity for matroids (conjectured [EPW16]), inverse KL nonnegativity (conjectured [GX21]), $Z$-polynomial unimodality, and equivariant analogues over any symmetry group $\Gamma$ (coefficients are honest, not virtual, representations) all follow. Stalk decomposition: $\mathfrak{m}^k IH(M) / \mathfrak{m}^{k+1} IH(M) \cong \bigoplus_{F \in L_k(M)} IH(M^F)_\varnothing[-k]$, with $IH(M)_\varnothing$ vanishing in degrees $\ge \mathrm{rk}\,M/2$.

## Why it matters here
General background; no direct arena tie. The Kähler-package / hard-Lefschetz technology is in the same toolbox as Hodge-theoretic positivity proofs that occasionally surface around extremal-combinatorics arena problems (Sperner-type bounds, Whitney-rank inequalities), but no current Einstein Arena problem is directly about matroid KL polynomials.

## Open questions / connections
- Is $IH(M)$ a Chow-theoretic shadow of $\ell$-adic étale $IH$ of the Schubert variety in positive characteristic, giving a rational form where Hodge–Riemann holds (Remark 1.13)?
- Can the trio (Weyl groups [EW14], rational polytopes [Kar04], matroids [this paper]) be unified into a single combinatorial-IH framework (Remark 1.15)?
- Extends Adiprasito–Huh–Katz [AHK18] from $\mathrm{CH}(M)$ to the singular $IH(M)$; relates to Soergel bimodules and Kazhdan–Lusztig–Stanley theory [Sta92, Pro18].
- Can hard Lefschetz be proved alone, without the full Kähler package (Remark 1.11)? Currently no.

## Key terms
matroid, intersection cohomology, Kazhdan–Lusztig polynomial, Top-Heavy conjecture, Dowling–Wilson, hard Lefschetz, Hodge–Riemann relations, Poincaré duality, Chow ring of a matroid, graded Möbius algebra, Schubert variety, geometric lattice, Sperner property, de Bruijn–Erdős, Huh, Braden, equivariant representation, Z-polynomial
