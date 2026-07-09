---
type: source
kind: paper
title: Effective Results on the Size and Structure of Sumsets
authors: A. Granville, G. Shakan, A. Walker
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2105.09181
source_local: ../raw/2021-granville-effective-results-size-structure.pdf
topic: general-knowledge
cites:
---

# Effective Results on the Size and Structure of Sumsets

**Authors:** A. Granville, G. Shakan, A. Walker  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2105.09181

## One-line
First effective (computable) upper bounds on the threshold $N$ beyond which the iterated sumset $NA \subset \mathbb{Z}^d$ has polynomial size and predictable cone-minus-exceptional structure, for arbitrary finite $A$.

## Key claim
For any finite $A \subset \mathbb{Z}^d$ with $\ell = |A|$: Khovanskii's theorem $|NA| = P_A(N)$ holds for all $N \geq (2\ell \cdot w(A))^{(d+4)\ell}$, and the structural identity $NA = (NH(A) \cap (a_0 N + \Lambda_{A-A})) \setminus \bigcup_{a \in \mathrm{ex}(H(A))} (aN - E(a-A))$ holds for all $N \geq (d\ell \cdot w(A))^{13 d^6}$, where $w(A) = \max_{a_1,a_2 \in A} \|a_1 - a_2\|_\infty$.

## Method
Reworks the Nathanson–Ruzsa proof as a chain of quantitative linear-algebra problems, bypassing the ineffective Mann–Dickson lemma. The simplex case ($H(A)$ a $d$-simplex) uses "$B$-minimal elements" and a refined Davenport-constant bound $k(G,H) \leq |G|-|H|$ on subsum-free sequences. The general structural theorem proceeds by induction on $\dim \mathrm{span}(A)$, using Siegel's lemma (Bombieri–Vaaler) to build small-norm bases of separating hyperplanes and a quantitative Khovanskii "interior representable" lemma.

## Result
Effective Khovanskii: $N_{Kh}(A) \leq (2\ell w(A))^{(d+4)\ell}$ in general; in the simplex case $N_{Kh}(A) \leq (d+1)! \mathrm{vol}(H(A)) - (d+1)(|A|-d) - d + 1$. Effective structure: $N_{\mathrm{Str}}(A) \leq (d\ell w(A))^{13 d^6}$ generally, $\leq (d+1)! \mathrm{vol}(H(A)) - (d+1)(|A|-d)$ in the simplex case; improves Curran–Goldmakher [3] for $|A| \geq d+3$. Speculation: $N_{\mathrm{Str}}(A) \leq N_{Kh}(A) \leq d! \mathrm{vol}(H(A))$.

## Why it matters here
General background; no direct arena tie. Closest indirect relevance is to discrete combinatorics / extremal additive structure — useful if a problem reduces to counting or describing $NA$ for some explicit lattice set $A$, but no current Einstein Arena problem in the wiki inventory is framed this way.

## Open questions / connections
- Is the speculated bound $N_{\mathrm{Str}}(A), N_{Kh}(A) \leq d! \mathrm{vol}(H(A))$ true for $d \geq 2$? (Unproven even for $d=1$.)
- Tighten the $13 d^6$ exponent in the general structure bound — large gap to expected truth.
- Can one directly deduce Khovanskii's theorem from the structural identity (1.5), or vice versa? Authors could not find a direct route.
- Extends [Curran–Goldmakher 2021] (generating-function / Ehrhart approach) with additive-combinatorial language; the two methods coincide on "$B$-minimal" elements.

## Key terms
Khovanskii's theorem, sumset, iterated sumset $NA$, Davenport constant, Mann–Dickson lemma, Freiman isomorphism, convex polytope, extremal points, lattice cone, Siegel's lemma, Bombieri–Vaaler, Ehrhart polynomial, Frobenius postage stamp, simplex hull, additive combinatorics
