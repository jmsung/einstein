---
type: source
kind: paper
title: Singular Rouquier complexes
authors: Leonardo Patimo
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1908.10966
source_local: ../raw/2019-patimo-singular-rouquier-complexes.pdf
topic: general-knowledge
cites:
---

# Singular Rouquier complexes

**Authors:** Leonardo Patimo  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1908.10966

## One-line
Extends Rouquier's categorification of braid groups from Soergel bimodules to *singular* Soergel bimodules (parabolic setting) and uses it to establish Hodge theory (hard Lefschetz + Hodge–Riemann) for singular Soergel bimodules.

## Key claim
Singular Rouquier complexes $F_w^I$ — defined as minimal complexes of restricted ordinary Rouquier complexes — are $\Delta$-split, satisfy the vanishing $\mathrm{Hom}(F_w^I, E_v^I[i]) = k$ iff $v=w, i=0$ (else $0$), and when Soergel's conjecture holds they are perverse and categorify the inverse parabolic Kazhdan–Lusztig polynomials $g^I_{x,y}(v)$, whose coefficients are therefore non-negative.

## Method
Restrict ordinary Rouquier complexes $F_w \in K^b(\mathrm{SBim})$ to complexes of $(R, R^I)$-bimodules and take minimal complexes in $K^b(\mathrm{SBim}^I)$. The key technical input is a *termwise-split* lemma: short exact sequences from the support filtration become split after restriction to $R\text{-Mod-}R^I$, giving distinguished triangles. Hodge theory then transfers from the non-singular case [EW14] almost verbatim, using a perverse $t$-structure on $K^b(\mathrm{SBim}^I)$.

## Result
Theorem 5.1 (Hard Lefschetz for $B_x^I$): for ample $\rho \in (\mathfrak h^*)^I$, $\rho^i : (\overline{B_x^I})^{-i} \to (\overline{B_x^I})^i$ is an isomorphism for all $i>0$. Theorem 5.2 (Hodge–Riemann): the Lefschetz form on the primitive subspace $P_\rho^{-i}$ is $(-1)^{(-\ell(x)+i)/2}$-definite. Corollary: an alternative proof of Soergel's conjecture closer to de Cataldo–Migliorini's geometric proof of the decomposition theorem.

## Why it matters here
General background; no direct arena tie. Representation-theoretic Hodge theory and Soergel-bimodule combinatorics are far from sphere packing / autocorrelation / kissing / extremal-graph problems on the Einstein Arena slate.

## Open questions / connections
- Extends [LW14] (standard/costandard objects in 2-braid groups) to the parabolic / singular setting.
- Companion paper [Pat19, arXiv:1908.11606] applies these complexes to Grassmannian Schubert varieties via Dyck-partition combinatorics to construct explicit bases of intersection cohomology.
- Example 5.6 ($A_3$, $I=\{s,t\}$) shows $(B_{stu})_I$ is not perverse — no ample $\rho \in (\mathfrak h^*)^I$ gives hard Lefschetz on $B_{stu}$; characterizing when "on-the-wall" Lefschetz survives remains open.

## Key terms
Soergel bimodules, singular Soergel bimodules, Rouquier complexes, 2-braid group, Hecke algebra, Kazhdan–Lusztig polynomials, parabolic Kazhdan–Lusztig, hard Lefschetz, Hodge–Riemann bilinear relations, perverse t-structure, Coxeter group, Schubert varieties, Soergel's conjecture, Williamson, Elias
