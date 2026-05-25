---
type: source
kind: paper
title: Generalizations of Tucker–Fan–Shashkin Lemmas
authors: O. Musin
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1409.8637
source_local: ../raw/2014-musin-generalizations-tucker-fan-shashkin.pdf
topic: general-knowledge
cites:
---

# Generalizations of Tucker–Fan–Shashkin Lemmas

**Authors:** O. Musin  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1409.8637

## One-line
Extends the classical Tucker, Ky Fan, and Shashkin combinatorial lemmas (discrete analogs of Borsuk–Ulam) from spheres/balls to a broader class of "BUT-manifolds," using a generalized odd-mapping theorem and a doubling construction.

## Key claim
For any $d$-dimensional BUT-manifold $(M,A)$ with antipodal triangulation $T$ and antipodal labelling $L : V(T) \to \Pi_{d+1} = \{\pm 1, \ldots, \pm(d+1)\}$ with no complementary edges, the number of $d$-simplices in $T$ labelled by any prescribed sign-pattern $\Lambda = \{\ell_1, \ldots, \ell_{d+1}\}$ with $|\ell_i| = i$ is odd (Theorems 3.1–3.4). Companion result: every odd continuous map $f : M_1 \to M_2$ between $d$-dimensional BUT-manifolds has odd degree (Theorem 2.1).

## Method
Proof goes through a generalization of the odd-mapping theorem: composing an odd $f : M_1 \to M_2$ with an antipodal transversal-to-zeros map $g : M_2 \to \mathbb{R}^d$ with $|Z_g| \equiv 2 \pmod 4$ forces $\deg_2 f = 1$. For manifolds with boundary, a doubling lemma (Lemma 3.1) embeds $M$ into $\mathbb{R}^q_+$ centrally-symmetrically along $\partial M$ and glues with its reflection to produce a BUT double $\tilde{M}$, reducing the boundary case to the boundary-free case. The labelling-to-simplicial-map construction $f_L : T \to \partial C_{d+1}$ (crosspolytope boundary) converts combinatorial complementary-edge statements into degree statements.

## Result
Four extensions: Theorem 3.1 (Tucker for closed BUT-manifolds — complementary edge exists for labellings into $\Pi_d$); Theorem 3.2 (Shashkin/Fan for closed BUT-manifolds — odd count of $\Lambda$-labelled $d$-simplices); Theorems 3.3–3.4 (the same for manifolds whose boundary $\partial M$ is BUT). Two covering corollaries (Theorems 4.1–4.2, Corollary 4.1) follow: $M$ cannot be covered by $d+1$ closed sets none of which contains an antipodal pair (Lusternik–Schnirelmann–type), and any $d+2$ such cover has forced intersection structure.

## Why it matters here
General background; no direct arena tie. The Borsuk–Ulam / Tucker / odd-mapping circle is the topological backbone behind combinatorial fair-division and discrete-geometry lower bounds, so this paper is a reference if a problem ever reduces to antipodal-labelling parity on a non-spherical configuration manifold (e.g., flag-algebra or configuration-space SDP setups).

## Open questions / connections
- Which other "natural" manifolds beyond $S^d$, connected sums $N \# N$, even-genus orientable surfaces, and non-orientable surfaces with even Möbius count are BUT? A constructive catalog would clarify reach.
- Can BUT-manifold Tucker/Shashkin lemmas yield sharper discrete bounds for any of the Einstein Arena packing/kissing problems where the natural configuration space is not a sphere (e.g., quotients, moduli)?
- Relation to Schwarz genus and Yang's cohomological index (cited but not exploited here) — whether either gives strictly stronger covering theorems on BUT-manifolds.

## Key terms
Tucker lemma, Ky Fan lemma, Shashkin lemma, Borsuk–Ulam theorem, BUT-manifold, odd mapping theorem, degree of mapping, antipodal labelling, complementary edge, crosspolytope, simplicial map, Lusternik–Schnirelmann covering, free involution, doubling of manifolds with boundary
