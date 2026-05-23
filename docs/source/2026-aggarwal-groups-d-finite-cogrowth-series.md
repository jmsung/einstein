---
type: source
kind: paper
title: On groups with D-finite cogrowth series
authors: Mudit Aggarwal, Murray Elder, Andrew Rechnitzer
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2605.12793v1
source_local: ../raw/2026-aggarwal-groups-d-finite-cogrowth-series.pdf
topic: general-knowledge
cites: 
---

# On groups with D-finite cogrowth series

**Authors:** Mudit Aggarwal, Murray Elder, Andrew Rechnitzer  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2605.12793v1

## One-line
Proves that an infinite family of one-relator groups $\langle a_1,\ldots,a_k \mid a_1^{p_1}=\cdots=a_k^{p_k}\rangle$ (plus several braid-group presentations of $B_3$) have D-finite but non-algebraic cogrowth series, expanding the known catalogue of groups with computable cogrowth.

## Key claim
For $G(p_1,\ldots,p_k) = \langle a_1,\ldots,a_k \mid a_1^{p_1}=\cdots=a_k^{p_k}\rangle$ with $k\ge 2$, $p_i\ge 2$, the cogrowth series is D-finite (as the constant term in $q$ of an algebraic bivariate $F_k(z;q)$) and non-algebraic. For the all-$p_i=2$ case the cogrowth equals $4\sqrt{k-1}$ with explicit asymptotic $\sim C \mu^n n^{-2}$ (or $n^{-1}$ for $k=2$). For $B_3 = \langle c,d \mid c^3=d^2\rangle$ the cogrowth is the largest root of $m^4-2m^3-11m^2+12m+4$ ($\approx 3.9506$); for $B_3=\langle a,b\mid aba=bab\rangle$ it is $1+2\sqrt{2}\approx 3.8284$, with $[z^n]\sim n^{-2}$ confirming non-algebraicity.

## Method
Pick a central element $\Delta=a_i^{p_i}$ and a normal form $\Delta^m v$; build a bivariate generating function $F_k(z;q)=\sum z^{|w|}q^m$ over closed walks, where $q$ tracks the $\Delta$-exponent ("winding number"). Decompose walks on the Schreier graph $G_k/\langle\Delta\rangle$ (which is a tree or finite-tree-width graph) at last-exit times to get an algebraic system; the cogrowth series is $[q^0]F_k$, D-finite by Lipshitz's diagonal theorem. Non-algebraicity is proved by factoring asymptotics into a Schreier-tree factor ($\mu^n n^{-3/2}$, algebraic-type) times a 1D random walk in $\Delta$-exponent ($n^{-1/2}$ Gaussian), giving $n^{-2}$ overall — incompatible with algebraic generating functions (Jungen / Flajolet-Sedgewick VII.7). Tools include Drmota's systems of functional equations, Goüezel's local limit theorem for hyperbolic groups, and a pattern theorem bounding winding-number variance.

## Result
Theorem 2.8: closed form $F_k(z;q)=2(k-1)/[k-2+k\sqrt{1-4(k-1)(q+2+q^{-1})z^2}]$ for $p_i=2$, with explicit coefficient sums. Theorem 4.6 + Section 7: full asymptotic expansion $\sim C\mu^n n^{-2}$ for general $G(p_1,\ldots,p_k)$. Appendix gives explicit polynomial equations and numerics for $B_3$ in three presentations. All examples support the folklore conjecture that algebraic cogrowth $\Leftrightarrow$ virtually free (none of these groups are virtually free, and none has algebraic cogrowth).

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — analytic combinatorics on Schreier-graph walks, last-exit decomposition into algebraic systems, and the "algebraic × Gaussian → $n^{-2}$ forbids algebraicity" diagnostic, which can be repurposed for any extremal-combinatorial enumeration problem (autocorrelation, Sidon-set counts, walk-counting on structured graphs).

## Open questions / connections
- Folklore conjecture (Conjecture 1.2): algebraic cogrowth iff virtually free — still open; this paper adds confirming negative examples but no proof.
- $\text{BS}(M,N)$ with $M\ne N$ conjectured to have non-D-finite cogrowth (Elder–Rechnitzer–JvR–Wong [15]) — open.
- Authors could not reduce the $B_3=\langle a,x\mid axa=x^2\rangle$ system to a single polynomial in $F_{00}(z,q)$; computer-algebra elimination timed out — leaves an explicit-form gap.
- Extends Bishop [5] ($\mathbb{Z}^d\times F_k$-by-finite ⇒ diagonal-of-rational cogrowth) and Bell–Mishna [3] (D-finiteness obstructions for amenable super-polynomial-growth groups).

## Key terms
cogrowth series, D-finite, holonomic, P-recursive, algebraic generating function, Schreier graph, virtually free group, central element, winding number, last-exit decomposition, Drmota systems, Lipshitz diagonal theorem, braid group $B_3$, Baumslag-Solitar, analytic combinatorics, singularity analysis, pattern theorem, Goüezel local limit theorem, finite tree-width, random walk on group
