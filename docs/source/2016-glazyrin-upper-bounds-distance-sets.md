---
type: source
kind: paper
title: Upper bounds for $s$-distance sets and equiangular lines
authors: A. Glazyrin, Wei-Hsuan Yu
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.09479
source_local: ../raw/2016-glazyrin-upper-bounds-distance-sets.pdf
topic: general-knowledge
cites:
---

# Upper bounds for $s$-distance sets and equiangular lines

**Authors:** A. Glazyrin, Wei-Hsuan Yu  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.09479

## One-line
Proves that the maximum spherical two-distance set in $\mathbb{R}^n$ has size $n(n+1)/2$ for all $n\ge 7$ (with rare exceptions $n=(2k+1)^2-3$), and gives the first universal bound on equiangular lines with common angle $1/a$ that holds for all $(a,n)$.

## Key claim
Three main bounds: (1) $g(n)=n(n+1)/2$ for $n\ge 7$ except possibly $n=(2k+1)^2-3$; (2) for $n\ge 359$, $M(n)\le (a^2-2)(a^2-1)/2$ where $a$ is the unique odd integer with $a^2-2\le n\le (a+2)^2-3$ — strictly improves Gerzon's $n(n+1)/2$ except at $n=a^2-2$; (3) the universal bound $M_{1/a}(n)\le n(a^2/2 + a/4 + 7/3) + 2$ valid for all $a\ge 3$ and all $n$.

## Method
A new zonal-spherical-function method on compact two-point homogeneous spaces: form a positive-semidefinite combination of Gegenbauer polynomials evaluated on a derived two-distance set, then take a non-negative linear combination of the row-sum inequalities ($k=1,3$) to extract the bound. Combined with the polynomial method (Lemmens–Seidel, Musin) and the "derived set" trick $Z_{x,\alpha}=\{(y-\alpha x)/\sqrt{1-\alpha^2}\}$ that drops dimension by one. Extremal-set analysis identifies the contact graph as a strongly regular graph with parameters $(N,k,(3k-N-1)/2,k/2)$.

## Result
Two-distance: $g(n)=n(n+1)/2$ achieved by simplex face-center construction, for all $n\ge 7$ outside the $(2k+1)^2-3$ family. Equiangular: improves Gerzon's bound for almost all $n\ge 359$; gives $M_{1/a}(n)\le n(a^2/2+a/4+7/3)+2$, which beats SDP bounds when $a$ is small vs $n$ and complements Balla–Dräxler–Keevash–Sudakov's $\le 1.93n$ for $a=1/3$ (asymptotically inferior but valid for all $n$, not only $n$ large). Classifies extremals (Theorem 4 / Corollary 1): any set achieving the new bound lies in an $(a^2-2)$-dim subspace, propagating non-existence results like $M(n)\le 1127$ for $47\le n\le 75$, $M(n)\le 3159$ for $79\le n\le 116$, $M(n)\le 14027$ for $167\le n\le 221$.

## Why it matters here
Direct ammunition for any arena problem on equiangular lines, spherical codes, or maximum two/few-distance sets — the Gegenbauer + derived-set + SRG-extremal pipeline is reusable. Concrete numerical ceilings ($1127, 3159, 14027$) in stated dimension ranges are immediately citable upper bounds; the universal $M_{1/a}(n)$ formula provides a valid bound where SDP solvers struggle (small $a$, moderate $n$).

## Open questions / connections
- Exact value of $\limsup_n M(n)/n^2$ between de Caen's $2/9$ and Gerzon's $1/2$ — analogous bracket $1/3 \le \limsup_n \max_a M_{1/a}(n)/(na^2) \le 2/3$.
- Conjecture: in non-exceptional dimensions, all near-maximal two-distance sets are subsets of the simplex face-center configuration (no intermediate sets).
- Conjecture: in exceptional $n=(2k+1)^2-3$, either a tight spherical 4-design exists or the maximum drops to $n(n+1)/2$ — no in-between.
- Define $M^*(n)$ = max equiangular set of *exact* dimension $n$: non-monotone (e.g. $M^*(21)<M^*(22)>M^*(23)$); even a quadratic lower bound is open.
- Connects to: Bachoc–Vallentin SDP kissing bounds [4], Bukh's $cn$ bound [17], BDKS $1.93n$ [5], tight spherical $2s$-design non-existence [9], Viazovska $E_8$ [60].

## Key terms
equiangular lines, spherical two-distance set, Gerzon bound, zonal spherical function, Gegenbauer polynomial, derived set, strongly regular graph, equiangular tight frame, polynomial method, harmonic bound, tight spherical design, Lemmens-Seidel, two-point homogeneous space, de Caen construction
