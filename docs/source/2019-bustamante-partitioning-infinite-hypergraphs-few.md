---
type: source
kind: paper
title: Partitioning Infinite Hypergraphs into Few Monochromatic Berge-Paths
authors: Sebastián Bustamante, J. Corsten, Nóra Frankl
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.05100
source_local: ../raw/2019-bustamante-partitioning-infinite-hypergraphs-few.pdf
topic: general-knowledge
cites:
---

# Partitioning Infinite Hypergraphs into Few Monochromatic Berge-Paths

**Authors:** Sebastián Bustamante, J. Corsten, Nóra Frankl  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.05100

## One-line
Extends Rado's 1978 monochromatic-path-partition theorem from graphs to $k$-uniform hypergraphs using $t$-tight Berge-paths, showing $s$ paths suffice when colours number $r=s(k-t+1)$.

## Key claim
For all $s,k,t\in\mathbb{N}$ with $k\geq t\geq 2$ and every $r=s(k-t+1)$-edge-colouring of the countably infinite complete $k$-graph $K_{\mathbb{N}}^{(k)}$, the vertices can be core-partitioned into $s$ monochromatic $t$-tight Berge-paths of distinct colours (Theorem 1.5). A matching construction with $r=s(k-t+1)+1$ colours shows this is tight (Theorem 1.6).

## Method
Apply Ramsey's theorem for infinite hypergraphs to build a $(t-1)$-clique-chain $\{K_i\}$ whose induced clique-colouring uses at most $s$ colours (Lemma 3.1, the core lemma — built via a maximally-monochromatic clique selection argument). Then greedily extend $s$ Berge-paths in parallel, picking the smallest uncovered vertex of each colour class and exploiting the clique-chain to find valid edges of the required colour for each $t$-consecutive window. The lower-bound construction generalises the Erdős–Gyárfás–Pyber [6] block construction: partition $\mathbb{N}$ into blocks $B_I$ indexed by $s$-subsets $I\subseteq[r]$ with rapidly growing sizes, and colour each edge by an element of $[r]\setminus\bigcup_{i\leq k-t+1} I(x^e_i)$.

## Result
Theorem 1.5: $s$ monochromatic $t$-tight Berge-paths core-partition the vertex set of $K_{\mathbb{N}}^{(k)}$ under any $s(k-t+1)$-colouring; this unifies and extends Rado [18] ($k=2$), Gyárfás–Sárközy [10] (loose paths), and Elekes–Soukup–Soukup–Szentmiklóssy [5] ($k=t$, tight paths). Theorem 1.6 establishes optimality: with one extra colour, $s$ paths cannot cover $\mathbb{N}$. The special case $t=2$ (Theorem 1.4) gives the clean bound $\lceil r/(k-1)\rceil$ Berge-paths suffice.

## Why it matters here
General background; no direct arena tie. The Ramsey-theoretic clique-chain + greedy-extension scheme is a clean template for "decompose an infinite structure into few monochromatic substructures," which could marginally inform extremal-graph or combinatorial-design problems if such appear, but no current Einstein Arena problem is about hypergraph path partitions.

## Open questions / connections
- Conjectures 4.1 and 4.2: finite analogues — every $s(k-t+1)$-coloured $K_n^{(k)}$ admits at most $s$ monochromatic $t$-tight Berge-cycles covering all but $c(s,k,t)$ vertices.
- Can paths be replaced by cycles in Theorem 1.5 for $2<t<k$ with full coverage (not just cofinite)?
- Extends Pokrovskiy's [17] $k=2$ cycle-partition conjecture and Omidi's [16] proof of the Gyárfás–Lehel–Sárközy–Schelp Hamiltonian Berge-cycle conjecture; Gerbner–Methuku–Omidi–Vizer [7] reportedly have partial progress.

## Key terms
Berge-path, tight path, loose path, $t$-tight, monochromatic partition, hypergraph Ramsey, clique-chain, edge-colouring, Lehel conjecture, Rado theorem, Erdős–Gyárfás–Pyber, Pokrovskiy, infinite complete $k$-graph, core-partition
