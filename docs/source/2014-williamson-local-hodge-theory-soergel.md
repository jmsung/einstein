---
type: source
kind: paper
title: Local Hodge theory of Soergel bimodules
authors: G. Williamson
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1410.2028
source_local: ../raw/2014-williamson-local-hodge-theory-soergel.pdf
topic: general-knowledge
cites:
---

# Local Hodge theory of Soergel bimodules

**Authors:** G. Williamson  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1410.2028

## One-line
Proves the local hard Lefschetz theorem and local Hodge–Riemann bilinear relations for Soergel bimodules, yielding an algebraic route to the Jantzen conjectures.

## Key claim
For an indecomposable self-dual Soergel bimodule $B$, element $x \in W$, and dominant $\rho^\vee \in h$ specialising $R \to R[z]$, the cokernel $H$ of $i_x: R[z] \otimes_R B^x_! \hookrightarrow R[z] \otimes_R B^x$ satisfies hard Lefschetz ($z^i: H^{-i} \xrightarrow{\sim} H^i$) and the induced forms on primitive subspaces $P^{-i} \subset H^{-i}$ have signature $(-1)^{\ell(x)}(-1)^d$ with $d = (-i - \min)/2$.

## Method
Algebraic Hodge theory via induction on Bruhat order, combined with the theory of "P¹-sheaves" developed in §5 — an elementary algebraic abstraction of the geometric Gysin sequence over a weighted-projective $\mathbb{P}^1$. Builds local intersection forms on stalks $B^x$ via Soergel calculus / light-leaf morphisms, then uses adjoint maps $d, d^*$ with explicit $d^* \circ d = $ multiplication-by-polynomial relations to propagate hL and HR across the induction. Follows the de Cataldo–Migliorini strategy [dCM02, dCM05] reformulated algebraically, extending [EW12a].

## Result
Establishes (Thm 1.1) local hard Lefschetz, (Thm 1.2) local Hodge–Riemann bilinear relations, and (Thm 1.3) that the canonical lowest-degree entry $\langle c_{x,y}, c_{x,y} \rangle^x_{B(y)} = \gamma e_{x,y}$ with $\gamma > 0$, where $e_{x,y}$ is the equivariant multiplicity from the nil Hecke ring. Combined with Soergel–Kübel, yields an algebraic proof of the Jantzen conjectures. The §8 $\mathfrak{sl}_4$ calculation (for $x = sutsu$) exhibits a regular non-dominant $\gamma^\vee$ where local hL **fails** and the Jantzen filtration on $\Delta(su)$ has layers $7,2,4,0$ instead of the dominant-direction layers $7,3,2,1$ — answering Deodhar's question negatively.

## Why it matters here
General background; no direct arena tie — Soergel bimodules / Kazhdan–Lusztig theory are far from the optimization-flavored Einstein Arena problems (sphere packing, kissing numbers, autocorrelation). The one transferable idea is the **induction-on-rank Hodge-theoretic argument**: hard Lefschetz + Hodge–Riemann signatures of a smaller object force the same on the next layer via an adjoint $d^* \circ d$ identity — a pattern that occasionally appears in extremal-combinatorics SDP proofs but is not currently used in any wiki concept.

## Open questions / connections
- Does local hL hold for arbitrary regular non-dominant $\gamma^\vee$ for non-Weyl-group Coxeter systems, or is the $\mathfrak{sl}_4$ obstruction generic?
- Can the P¹-sheaf machinery of §5 be axiomatised to apply outside Soergel bimodules (e.g., to other categorified Hecke-like settings)?
- Stronger characterisation of when Soergel's conjecture follows from local hL on $B(x)B(s)$ — Prop 7.19 is not stated as iff.

## Key terms
Soergel bimodules, local hard Lefschetz, Hodge–Riemann bilinear relations, Jantzen filtration, Jantzen conjectures, Kazhdan–Lusztig polynomials, Coxeter group, reflection representation, nil Hecke ring, equivariant intersection cohomology, Schubert variety, P¹-sheaf, Williamson, Elias, Soergel, de Cataldo–Migliorini
