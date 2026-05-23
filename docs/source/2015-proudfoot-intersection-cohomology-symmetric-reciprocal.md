---
type: source
kind: paper
title: Intersection cohomology of the symmetric reciprocal plane
authors: N. Proudfoot, Max Wakefield, Ben Young
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1504.07348
source_local: ../raw/2015-proudfoot-intersection-cohomology-symmetric-reciprocal.pdf
topic: general-knowledge
cites:
---

# Intersection cohomology of the symmetric reciprocal plane

**Authors:** N. Proudfoot, Max Wakefield, Ben Young  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1504.07348

## One-line
Computes the Kazhdan–Lusztig polynomial of the rank-$(n-1)$ uniform matroid on $n$ elements and identifies the intersection cohomology of the associated symmetric reciprocal plane as a specific irreducible $S_n$-representation.

## Key claim
For $n \geq 2$ and $i \geq 0$, $c_{n,i} := \dim IH^{2i}(X_n) = \frac{1}{i+1}\binom{n-i-2}{i}\binom{n}{i}$ (the Cayley count of $i$ non-intersecting chords in an $(n-i+1)$-gon), and as an $S_n$-representation $IH^{2i}(X_n) \cong V_{[n-2i,\,2^i]}$; the coefficient sequence is strictly log-concave.

## Method
Two-pronged: (1) generating-function manipulation — verify Beckwith's polygon-dissection series $f(t,u)$ satisfies the EPW functional equation in Theorem 1.1(3); (2) categorification — build a weight-pure subquotient of a mixed-Hodge spectral sequence on the stratification of $X_n$ by coordinate-vanishing loci $Y(S)$, lifting the integer recursion to virtual $S_n$-representations, then solve via Littlewood–Richardson / hook-length on the irreducible decomposition.

## Result
Closed-form $c_{n,i} = \tfrac{1}{i+1}\binom{n-i-2}{i}\binom{n}{i}$, vanishing for $i \geq (n-1)/2$. Strict log-concavity $c_{n,i}^2 > c_{n,i-1}c_{n,i+1}$ on the support (Corollary 2.1, settling the EPW log-concavity conjecture in the uniform rank-$(n-1)$ case). Representation-theoretic lift: $IH^{2i}(X_n)$ is the *irreducible* $V_{[n-2i,2^i]}$ — giving a new geometric construction of these two-row-plus-hook irreducibles.

## Why it matters here
General background; no direct arena tie. Possible tangential relevance to extremal combinatorics / log-concavity (matroid-coefficient log-concavity is in the same family as Lorentzian polynomial / Mason-conjecture machinery occasionally invoked for extremal-graph or sieve bounds), but the symmetric reciprocal plane and Kazhdan–Lusztig matroid polynomials are not in the current Einstein Arena problem set.

## Open questions / connections
- Generalizes to arbitrary-rank uniform matroids on $n$ elements (deferred by the authors to a future paper) — only the rank-$(n-1)$ case admits the $S_n$-action used here.
- Extends to general arrangements via Remark 3.6: $IH^{2i}(X_A) \cong \bigoplus_{[F]\in L/W,\,j}(-1)^j \mathrm{Ind}^W_{W(F)}\!\bigl(H^j(U_{A_F})\otimes IH^{2(\mathrm{crk}\,F - i + j)}(X_{A^F})\bigr)$ — but the stabilizer-product simplification fails in general (e.g. braid arrangement).
- Why is $IH^{2i}(X_n)$ irreducible? No a priori reason given — open conceptual question.
- Settles the Elias–Proudfoot–Wakefield log-concavity conjecture only for uniform rank-$(n-1)$; the general matroid case remains.

## Key terms
Kazhdan-Lusztig polynomial, uniform matroid, reciprocal plane, intersection cohomology, symmetric group representation, Littlewood-Richardson, log-concavity, polygon dissection, non-intersecting chords, Catalan-like, mixed Hodge structure, hook-length formula, Cayley, Beckwith, Proudfoot
