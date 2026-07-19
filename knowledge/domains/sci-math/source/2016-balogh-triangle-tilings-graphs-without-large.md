---
type: source
kind: paper
title: Triangle-Tilings in Graphs Without Large Independent Sets
authors: J. Balogh, Andrew McDowell, T. Molla, Richard Mycroft
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1607.07789
source_local: ../raw/2016-balogh-triangle-tilings-graphs-without-large.pdf
topic: general-knowledge
cites:
---

# Triangle-Tilings in Graphs Without Large Independent Sets

**Authors:** J. Balogh, Andrew McDowell, T. Molla, Richard Mycroft  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1607.07789

## One-line
Determines the minimum-degree threshold for (almost-)perfect triangle-tilings in $n$-vertex graphs with sublinear independence number, lowering the classical Corrádi–Hajnal $2n/3$ bound to $n/3 + o(n)$.

## Key claim
If $\delta(G) \geq n/3 + \omega n$ and $\alpha(G) \leq \gamma n$, then $G$ has a triangle-tiling covering all but at most $4$ vertices; if additionally $3 \mid n$ and $G$ has no divisibility barrier, the tiling is perfect. For $r \geq 5$ and $K_r$-free $G$ with $3 \mid n$, the asymptotic threshold is $\tfrac{1}{2} f_{RT}(r)\, n + o(n)$ where $f_{RT}(r) = (r-3)/(r-1)$ (odd $r$) or $(3r-10)/(3r-4)$ (even $r$).

## Method
Szemerédi regularity lemma applied to the host graph, producing a reduced graph $R$; spanning trees of bounded degree in $R$ via Win's theorem ($\delta(R) \geq (|R|-1)/k \Rightarrow \Delta(T) \leq k$). Core technical device: $(\eta,\xi)$-weighted fractional matchings in a directed reduced graph, where unequal head/tail weights lower the matching-existence threshold from $n/2$ to $\sim n/3$; existence proved via Farkas' lemma. Robustly-matchable "core" sets absorb leftover vertices; case split on whether $G$ admits a large sparse cut (reduces to Balogh–Molla–Sharifzadeh's $n/2 + \omega n$ theorem on each side).

## Result
- Theorem 1.2: $\delta(G) \geq n/3 + \omega n$, $\alpha(G) \leq \gamma n$ $\Rightarrow$ triangle-tiling missing $\leq 4$ vertices; perfect if no divisibility barrier and $3 \mid n$.
- Corollary 1.4: for $r \geq 7$, $K_r$-free $\delta(G) \geq \tfrac{1}{2} f_{RT}(r) n + \omega n$, $\alpha(G) \leq \gamma n$, $3 \mid n$ $\Rightarrow$ perfect triangle-tiling.
- Both the $4$-vertex slack and the $\omega n$ error are shown tight by explicit constructions (two disjoint $K_{3m+2}$; Erdős-graph blow-ups).

## Why it matters here
General background; no direct arena tie. Relevant if a problem reduces to triangle-packing / $K_k$-tiling on sparse-independence graphs; the $(\eta,\xi)$-weighted fractional matching LP trick (Lemma 2.10) is a transferable technique for any extremal packing problem where the natural LP relaxation has asymmetric vertex demands.

## Open questions / connections
- Conjecture 5.3: $K_4$-free with $\delta(G) \geq n/6 + \omega n$, $\alpha(G) = o(n)$ $\Rightarrow$ perfect triangle-tiling (open; lower bound from modified Bollobás–Erdős graph).
- Question 5.4: best minimum-degree for perfect $K_k$-tiling in $K_{k+1}$-free graphs with $\alpha(G) = o(n)$; only partial bounds known.
- Extends Corrádi–Hajnal (1963) and Balogh–Molla–Sharifzadeh ($n/2 + \omega n$ threshold for perfect triangle-tiling under sublinear $\alpha$).

## Key terms
triangle-tiling, perfect tiling, Corrádi-Hajnal theorem, Ramsey-Turán, independence number, divisibility barrier, space barrier, Szemerédi regularity lemma, fractional matching, Farkas' lemma, Bollobás-Erdős graph, Erdős-Sós, $K_r$-free, minimum degree threshold, extremal graph theory
