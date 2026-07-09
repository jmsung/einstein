---
type: source
kind: paper
title: Structure and properties of large intersecting families
authors: A. Kupavskii
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1710.02440
source_local: ../raw/2017-kupavskii-structure-properties-large-intersecting.pdf
topic: general-knowledge
cites:
---

# Structure and properties of large intersecting families

**Authors:** A. Kupavskii  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1710.02440

## One-line
Sharp structural and extremal theorems for large intersecting $k$-uniform families, controlling size via diversity and giving degree/subset-degree versions of Erdős–Ko–Rado, Hilton–Milner, and the Erdős Matching Conjecture.

## Key claim
A conclusive diversity version of Frankl's theorem: for an intersecting $\mathcal{F}\subset\binom{[n]}{k}$, the maximum $|\mathcal{F}|$ is determined exactly by a lower bound on the diversity $\gamma(\mathcal{F})=|\mathcal{F}|-\Delta(\mathcal{F})$, with sharp bounds at every "resistant" cascade-form value $\gamma_l$; this strictly strengthens the Kupavskii–Zakharov bound $|\mathcal{F}|\le\binom{n-1}{k-1}+\binom{n-u-1}{n-k-1}-\binom{n-u-1}{k-1}$ from Theorem 2.

## Method
Reduction from intersecting to cross-intersecting families via the standard $\mathcal{F}(1),\mathcal{F}(\bar 1)$ split, followed by Kruskal–Katona shifting to lexicographic (lex) families. Core technical device: bipartite biregular "shifting" graphs on pairs $(\mathcal{P}_a,\mathcal{P}_b)$ of sets with prescribed intersection pattern, where cross-intersection forces an independent set, and the larger part of the biregular graph dominates — giving a computation-free monotonicity argument over "resistant pairs" $(S,T)$ of characteristic sets that strongly intersect in their last element.

## Result
Theorem 6/7: exact $|\mathcal{F}|\le\binom{n-a_1}{n-k}+\cdots+\binom{n-a_{s_a}}{n-s_a}+\gamma_l$ whenever $\gamma_{l-1}<\gamma(\mathcal{F})\le\gamma_l$, sharp at every resistant $\gamma_l$. Theorem 22: for $n\ge 2k^2$ and $k\ge 5st$ (or $k\ge 3s$ when $t=1$), any $\mathcal{F}\subset\binom{[n]}{k}$ with matching number $\nu(\mathcal{F})\le s$ satisfies $\delta_t(\mathcal{F})\le\binom{n-t}{k-t}-\binom{n-s-t}{k-t}=\delta_t(A_0(n,k,s))$, with equality only for $A_0$ — extending Huang–Zhao's $n\ge 3k^2(s+1)$ to $n\ge 2k^2$ and to general $t$-degree.

## Why it matters here
General background; no direct arena tie — the 23 Einstein Arena problems do not currently include $k$-uniform extremal set theory in the EKR/Hilton–Milner regime. Provides reusable infrastructure (Kruskal–Katona shifting + biregular bipartite reduction) that could inform discrete-combinatorics problems if they arise, and supplies sharp diversity-based bounds for cross-intersecting set systems.

## Open questions / connections
- Structure of intersecting families with diversity $>\binom{n-3}{k-2}$ in the range $2k<n<3k$ (Kupavskii [23] shows none exist for $n>Ck$; conjectured threshold $n>3k-2$).
- Problem 4: does a non-trivial intersecting family at $n=2k+1$ (or $n=2k+ct$) beat the Hilton–Milner minimum $t$-degree?
- Problem 5: for disjoint cross-intersecting $\mathcal{A},\mathcal{B}\subset\binom{[n]}{k}$, is $\min(|\mathcal{A}|,|\mathcal{B}|)\le\tfrac12\binom{n-1}{k-1}$?

## Key terms
intersecting families, Erdős–Ko–Rado, Hilton–Milner, diversity, Frankl degree theorem, Kruskal–Katona, cross-intersecting, lexicographic shifting, Erdős matching conjecture, cascade form, resistant pair, Kupavskii
