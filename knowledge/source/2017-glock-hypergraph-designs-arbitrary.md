---
type: source
kind: paper
title: Hypergraph $F$-designs for arbitrary $F$
authors: Stefan Glock, D. Kuhn, A. Lo, Deryk Osthus
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1706.01800
source_local: ../raw/2017-glock-hypergraph-designs-arbitrary.pdf
topic: general-knowledge
cites:
---

# Hypergraph $F$-designs for arbitrary $F$

**Authors:** Stefan Glock, D. Kuhn, A. Lo, Deryk Osthus  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1706.01800

## One-line
Proves that for any $r$-uniform hypergraph $F$, the trivially necessary divisibility conditions suffice to guarantee an $(F,\lambda)$-design of the complete $r$-graph $K_n^{(r)}$ for all sufficiently large $n$.

## Key claim
For any fixed $r$-graph $F$ on $f$ vertices and any $\lambda \le \gamma n$, every sufficiently large $(F,\lambda)$-divisible $(c,h,p)$-typical $r$-graph $G$ admits an $(F,\lambda)$-design, with explicit thresholds $c \le 0.9(p/2)^{h/(qr 4^q)}$ where $q = 2^f f!$ and $h = 2r\binom{q+r}{r}$. This generalizes Wilson's 1975 theorem ($r=2$) and Keevash's existence-of-designs theorem (case $F = K_f^{(r)}$) to arbitrary $F$.

## Method
Iterative absorption: build an approximate $F$-packing in stages along a nested "vortex" of vertex subsets, with an absorbing structure set aside in advance to soak up the residual leftover. The argument is by induction on $r$, working in the weaker quasi-random framework of *supercomplexes* (regularity in the count of $f$-cliques), and reduces arbitrary $F$ to the weakly-regular case by explicitly packing $F$ into a weakly-regular auxiliary $r$-graph $F^*$ built via Cauchy-matrix constructions over finite fields.

## Result
For $F$ weakly regular, every $F$-divisible $r$-graph $G$ on $n$ vertices with $\delta(G) \ge (1 - c_F^\diamond)n$ has an $F$-decomposition, where $c_F^\diamond = r!/(3 \cdot 14^r f^{2r})$ — giving an explicit upper bound $\delta_F \le 1 - c_F^\diamond$ on the decomposition threshold. Also yields near-optimal $F$-packings with $\Delta(L) \le C$ in non-divisible typical $r$-graphs, and resolvable clique decompositions of complete partite $r$-graphs as a byproduct.

## Why it matters here
General background; no direct arena tie. Closest contact is conceptual — iterative-absorption and supercomplex regularity are extremal-combinatorics tools that may inform thinking on extremal-graph and combinatorial-design problems in the arena, but no current Einstein problem invokes hypergraph $F$-designs directly.

## Open questions / connections
- Establish a graph-case-style connection $\delta_F \le \max\{\delta_F^*, 1 - 1/(\chi(F)+1)\}$ between integer and fractional decomposition thresholds in the hypergraph setting.
- Determine $\delta_F$ for $r$-partite $r$-graphs $F$, generalizing the bipartite-graph result of [11].
- Extend the explicit resolvable clique decomposition (complete partite case via Cauchy matrices) to general complete $r$-graphs $K_n^{(r)}$ — the Ray-Chaudhuri–Wilson analogue for $r \ge 3$.
- Decomposition threshold of a graph triangle (Nash-Williams' $3/4$ conjecture) remains open even at $r=2$.

## Key terms
hypergraph design, $F$-decomposition, Steiner system, block design, Wilson's theorem, Keevash existence conjecture, iterative absorption, supercomplex, quasirandom hypergraph, decomposition threshold, Rödl nibble, divisibility conditions, weakly regular hypergraph, resolvable design, Cauchy matrix
