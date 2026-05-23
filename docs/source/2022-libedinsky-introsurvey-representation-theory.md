---
type: source
kind: paper
title: IntroSurvey of Representation Theory
authors: Nicolás Libedinsky
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.07082
source_local: ../raw/2022-libedinsky-introsurvey-representation-theory.pdf
topic: general-knowledge
cites:
---

# IntroSurvey of Representation Theory

**Authors:** Nicolás Libedinsky  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.07082

## One-line
A personal, three-tier survey of representation theory (classical → quantum → categorical) culminating in Schur–Weyl duality, Kazhdan–Lusztig theory, Soergel bimodules, the $p$-canonical basis, and 20 open problems.

## Key claim
Representation theory of $S_n$ and $GL_n(\mathbb{F}_q)$ are two faces of one structure unified by Schur–Weyl duality $\mathrm{End}_{\mathbb{C}[S_n]}(V^{\otimes n}) \cong \mathbb{C}[GL(V)]$ and $\mathrm{End}_{\mathbb{C}[GL(V)]}(V^{\otimes n}) \cong \mathbb{C}[S_n]$; the modern frontier is computing the $p$-canonical basis (categorified via Soergel bimodules) where Kazhdan–Lusztig polynomials and their positive-characteristic deformations encode deep combinatorial/Hodge-theoretic structure.

## Method
Expository synthesis organized around three structural unifications: (i) $S_n = GL_n(\mathbb{F}_1)$ — the "field with one element" analogy via $q$-deformation of $[n]_q = 1+q+\cdots+q^{n-1}$; (ii) Bruhat decomposition $GL_n(\mathbb{F}_p) = \bigsqcup_{w \in S_n} B\dot w B$ reducing $GL_n$ to $S_n$; (iii) Schur–Weyl duality on tensor space $V^{\otimes n}$. Specht modules are constructed from flag varieties $FL(\lambda)$ indexed by partitions. The quantum tier deforms $\mathbb{C}[S_n]$ to the Iwahori–Hecke algebra; the categorical tier replaces it with Soergel bimodules, with Kazhdan–Lusztig and $p$-canonical bases encoded diagrammatically via Soergel calculus.

## Result
Establishes a unified narrative: (a) classical representation theory of $S_n$ via Specht modules indexed by partitions of $n$; (b) Iwahori–Hecke algebra $H$ as a $q$-deformation with the Kazhdan–Lusztig basis $\{b_w\}$ giving polynomials $p_{x,y}(v) \in \mathbb{N}[v]$; (c) Soergel bimodules $B(W)$ categorify $H$ with indecomposables $B_w$ realizing the $p$-canonical basis. Lists 20 open problems with difficulty ratings, including: combinatorial invariance of KL polynomials (Lusztig–Dyer), log-concavity of $R$-polynomials, combinatorial formula for KL coefficients, computing the $p$-canonical basis for affine Weyl groups (estimated 30-year problem), and Relative Hard Lefschetz for tensor products of Soergel bimodules.

## Why it matters here
General background; no direct arena tie. Representation theory and Hecke algebras do not appear in the current 23-problem set (sphere packing, autocorrelation, Sidon sets, kissing, etc.), but the paper's Hodge-theoretic / log-concavity threads (June Huh's work, hard Lefschetz) and the symmetric-group combinatorics on Young diagrams could inform extremal-combinatorics problems if they arise.

## Open questions / connections
- Combinatorial invariance conjecture for KL polynomials — recently attacked via DeepMind/Williamson collaboration ([BBD+21], Nature paper), exemplifying AI-assisted intuition in pure math.
- Log-concavity of $R$-polynomials as a Hodge-theoretic signature — connects to Huh's combinatorial Hodge theory, potentially relevant if any arena problem reduces to log-concave sequences.
- $\mathbb{F}_1$ ("field with one element") program — Manin/Deninger/Soulé/Connes-Consani direction toward Riemann hypothesis; Williamson's speculation that $p$-canonical basis may be understood via stable homotopy categories.
- Schur–Weyl duality as a template for "do procedure to $A$ get $B$; do it to $B$ get $A$" — same pattern as Poincaré/Koszul duality.

## Key terms
representation theory, symmetric group $S_n$, general linear group $GL_n$, Schur-Weyl duality, Specht modules, Bruhat decomposition, Iwahori-Hecke algebra, Kazhdan-Lusztig polynomials, Soergel bimodules, $p$-canonical basis, Coxeter groups, quantum groups, categorification, field with one element $\mathbb{F}_1$, Hodge theory, Libedinsky, Williamson, flag varieties, Young diagrams, combinatorial invariance
