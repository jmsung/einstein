---
type: source
kind: paper
title: A hierarchy of maximal intersecting triple systems
authors: J. Polcyn, A. Rucinski
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.06114
source_local: ../raw/2016-polcyn-hierarchy-maximal-intersecting-triple.pdf
topic: general-knowledge
cites:
---

# A hierarchy of maximal intersecting triple systems

**Authors:** J. Polcyn, A. Rucinski  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.06114

## One-line
Classifies all maximal intersecting 3-uniform hypergraphs on $n$ vertices and organizes them as a finite hierarchy of higher-order Turán numbers for the matching $M_2^3$.

## Key claim
For every $n \geq 7$ there are exactly 15 pairwise non-isomorphic maximal intersecting triple systems (13 for $n = 6$), and the Turán hierarchy $\mathrm{ex}^{(s)}(n; M_2^3)$ terminates at $s = 6$ with values $\binom{n-1}{2},\ 3n-8,\ 2n-2,\ n+4,\ 10,\ 7$.

## Method
Structural / combinatorial: define a heart of $H$ as a vertex subset on which every pair of edges intersects, and show (Fact 2) that a heart of size $\geq 2k$ induces a maximal intersecting sub-hypergraph. Split cases on whether $H$ contains a triangle $C_3$ (Lemma 1 handles triangle-free via a small auxiliary 3-graph $H_0(n)$); when $C_3 \subset H$, either $C_3$ is a triangular heart and $H[U]$ is one of the 11 maximal intersecting 6-vertex configurations enumerated in Proposition 1, or $H$ is forced to be Fano-like ($F_7$ or $F_{10}$). The 6-vertex enumeration proceeds by counting minimal 2-covers (size of $\tau$).

## Result
For $n \geq 7$: $\mathrm{ex}^{(1)} = \binom{n-1}{2}$ (full star $S_n$); $\mathrm{ex}^{(2)} = 3n - 8$ (two extremals $H_1, H_2$, recovering Hilton–Milner); $\mathrm{ex}^{(3)} = 2n - 2$ (unique $H_3$, recovering Han–Kohayakawa); $\mathrm{ex}^{(4)} = n + 4$ (three extremals $H_4, H_5, H_6$); $\mathrm{ex}^{(5)} = 10$ (including $K_5 \cup (n-5)K_1$, $F_{10}$, and five 10-edge 6-vertex configs $H_7,\dots,H_{11}$); $\mathrm{ex}^{(6)} = 7$ (Fano plane $F_7$ alone); no $\mathrm{ex}^{(s)}$ for $s \geq 7$. Along the way: the largest triangle-free intersecting non-star triple system on $n \geq 6$ vertices has $\max\{10, n\}$ edges.

## Why it matters here
General background for extremal hypergraph / intersecting-family questions; touches Einstein Arena indirectly via combinatorics problems involving intersecting set families, Turán-type counts, and triangle-/matching-free constraints. No direct tie to a specific listed arena problem — useful as a reference if a problem reduces to "count or classify intersecting triples with a forbidden configuration."

## Open questions / connections
- Generalize the heart-based unified approach from $k=3$ to all $k \geq 4$ (Kostochka–Mubayi handled only the large-$n$, large-edge regime).
- Length of the Turán hierarchy for $M_2^k$ at general $k$ — does it always terminate, and what is the terminal value?
- Connection to 1-special 3-graphs of Henning–Yeo (transversals/matchings in 3-uniform hypergraphs) and to Kostochka–Mubayi's structure theorem for large intersecting families.

## Key terms
intersecting hypergraph, maximal intersecting family, Turán number hierarchy, Erdős-Ko-Rado, Hilton-Milner, Han-Kohayakawa, triple system, 3-uniform hypergraph, Fano plane, vertex cover, triangle $C_3$, matching $M_2$, extremal combinatorics
