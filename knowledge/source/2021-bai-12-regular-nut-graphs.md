---
type: source
kind: paper
title: On 12-regular nut graphs
authors: N. Bašić, M. Knor, R. Škrekovski
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.04418
source_local: ../raw/2021-bai-12-regular-nut-graphs.pdf
topic: general-knowledge
cites:
---

# On 12-regular nut graphs

**Authors:** N. Bašić, M. Knor, R. Škrekovski  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.04418

## One-line
Characterizes exactly which orders $n$ admit a 12-regular nut graph (singular adjacency matrix with 1-dim kernel spanned by a nowhere-zero eigenvector), extending the prior $d \le 11$ classification.

## Key claim
A 12-regular nut graph of order $n$ exists if and only if $n \ge 16$. Additionally: no circulant nut graph exists when degree $d \equiv 2 \pmod 4$, while infinitely many exist for $d \equiv 0 \pmod 4$.

## Method
Combines the Fowler construction (extending an $n$-vertex $d$-regular nut graph to $n+2d$) with explicit constructions on $2d=24$ consecutive orders $\{16,\dots,39\}$. For even orders, uses circulant graphs $C(n,\{1,2,\dots,d/2\})$ with a closed-form nut criterion (Theorem 8: nut iff $d/2+1$ coprime to $n$ and $d/4$ coprime to $n/2$); for odd orders, computer search with edge rewiring from a seed circulant. Negative side ruled out by exhaustive enumeration on $n \in \{13,14,15\}$ via SageMath.

## Result
Theorem 3: 12-regular nut graphs exist exactly for $n \ge 16$. Theorem 7: $d \equiv 2 \pmod 4$ admits no circulant nut graph (parity obstruction from eigenvector $(1,-1,1,-1,\dots)$). Theorem 8: explicit coprimality condition gives infinitely many circulant nut graphs at $d \equiv 0 \pmod 4$. Lemma 5: any 0-eigenvector of a regular singular graph sums to zero.

## Why it matters here
General background; no direct arena tie. Spectral/combinatorial graph theory with extremal-graph flavor — peripherally relevant to discrete combinatorics or extremal graph problems if a future arena problem touches singular adjacency matrices, kernel structure of regular graphs, or vertex-transitive constructions on $\mathbb{Z}/n$.

## Open questions / connections
- Conjecture 9: for every even $n \ge 16$, some 6-set $\{a_1,\dots,a_6\}$ gives a circulant 12-regular nut graph (stronger than Theorem 8's restricted family).
- Conjecture 10: for every $d \equiv 0 \pmod 4$ and every even $n \ge d+4$, a $d/2$-connection circulant nut graph exists.
- Extends Fowler et al. 2020 (degrees 3–11); the $d \equiv 2 \pmod 4$ negative result suggests non-circulant constructions are needed for those degrees.

## Key terms
nut graph, adjacency matrix kernel, singular graph, 1-dimensional nullspace, regular graph, circulant graph, vertex-transitive, Fowler construction, spectral graph theory, eigenvector, coprimality condition, extremal combinatorics
