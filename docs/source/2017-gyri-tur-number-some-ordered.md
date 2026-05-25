---
type: source
kind: paper
title: On the Turán number of some ordered even cycles
authors: E. Györi, Dániel Korándi, Abhishek Methuku, István Tomon, C. Tompkins, Máté Vizer
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1710.07664
source_local: ../raw/2017-gyri-tur-number-some-ordered.pdf
topic: general-knowledge
cites:
---

# On the Turán number of some ordered even cycles

**Authors:** E. Györi, Dániel Korándi, Abhishek Methuku, István Tomon, C. Tompkins, Máté Vizer  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1710.07664

## One-line
Determines the extremal edge-count for ordered graphs avoiding "bordered" even cycles, matching the Bondy–Simonovits $O(n^{1+1/k})$ bound for all $k$ in the ordered setting.

## Key claim
$\mathrm{ex}_<(n, \{C_4^B, C_6^B, \ldots, C_{2k}^B\}) = \Theta(n^{1+1/k})$ for every fixed $k>1$, where $C_{2k}^B$ is the set of ordered $2k$-cycles (interval chromatic number 2) containing both an inner and an outer border edge. For $k=3$, forbidding only bordered 6-cycles already gives $\Theta(n^{4/3})$.

## Method
Lower bound: explicit construction via $B_k$-sets (generalized Sidon sets) from Bose–Chowla, defining a bipartite adjacency matrix $A_G(i,j)=1$ iff $i-j+n\in S$; the $B_k$-property forces any short cycle's edge-coordinates to match as multisets, but a border edge uniquely extremizes $i_s-j_s$, contradiction. Upper bound: a "$k$-zigzag path" counting argument — at most one zigzag path between any vertex pair (else a bordered cycle appears), and a greedy left/right-trimming on neighborhoods gives $\ge m^k/(k^k(3n)^{k-1})$ zigzag paths, forcing $m<3kn^{1+1/k}$. Theorem 4 uses Gallai–Roy on an auxiliary DAG of bordered-cycle border-edge pairs to extract a $C_{2l}^B$-free subgraph keeping a $\tfrac{l-1}{k-1}$ fraction of edges.

## Result
Theorem 2: $\Theta(n^{1+1/k})$ for the family of bordered cycles up to length $2k$. Theorem 3: $\mathrm{ex}_<(n, C_6^B) = \Theta(n^{4/3})$ — only 3 of 6 ordered hexagons need forbidding. Theorem 6: even 2 ordered hexagons (e.g., $\{C_6^2, C_6^1\}$) suffice for $\Theta(n^{4/3})$. Theorem 7: $\mathrm{ex}_<(n, C_{2k}^B) = O(n^{1+\lambda_k})$ with $\liminf \lambda_k = 0$ (via $k=(m-1)!+1$, $\lambda_k=1/m$).

## Why it matters here
General background; no direct arena tie. Closest hooks are Sidon/$B_k$-set constructions (used in autocorrelation/additive-combinatorics problems) and extremal-graph edge bounds — the $B_k$-set $\to$ ordered-bipartite-adjacency construction may inspire combinatorial constructions for problems requiring near-Sidon-like multiplicity control.

## Open questions / connections
- Does $\mathrm{ex}_<(n, C_{2k}^B) = O(n^{1+1/k})$ hold for the single bordered family (not just up-to-$2k$)? Open for $k\ge 4$.
- Pach–Tardos conjecture: does forbidding *any* single ordered 6-cycle of interval chromatic number 2 give $\Theta(n^{4/3})$? (Conjecture 2.)
- Extends Kühn–Osthus (2005) on $C_4$-free subgraphs of $C_{2k}$-free graphs via the Gallai–Roy DAG trick.

## Key terms
Turán number, ordered graphs, bordered cycles, even cycles, $B_k$-sets, Sidon sets, Bose–Chowla, Bondy–Simonovits, interval chromatic number, zigzag path, Gallai–Roy theorem, forbidden 0-1 submatrices, Kühn–Osthus, hexagon extremal number, bipartite adjacency matrix
