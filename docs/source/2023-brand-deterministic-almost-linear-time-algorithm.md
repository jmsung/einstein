---
type: source
kind: paper
title: A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow
authors: Jan van den Brand, L. Chen, Rasmus Kyng, Y. Liu, Richard Peng, Maximilian Probst Gutenberg, Sushant Sachdeva, Aaron Sidford
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2309.16629
source_local: ../raw/2023-brand-deterministic-almost-linear-time-algorithm.pdf
topic: general-knowledge
cites:
---

# A Deterministic Almost-Linear Time Algorithm for Minimum-Cost Flow

**Authors:** Jan van den Brand, L. Chen, Rasmus Kyng, Y. Liu, Richard Peng, Maximilian Probst Gutenberg, Sushant Sachdeva, Aaron Sidford  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2309.16629

## One-line
Gives the first deterministic $m^{1+o(1)}$ algorithm for exact max-flow and min-cost flow on directed graphs with polynomially bounded integer capacities, costs, and demands.

## Key claim
There is a deterministic algorithm computing exact min-cost flow in time $m^{1+o(1)} \log U \log C$ (Theorem 1.1), matching the randomized [CKLPPS22] runtime and giving the first deterministic improvement over Goldberg–Rao's $O(m \cdot \min\{m^{1/2}, n^{2/3}\})$ since 1998. As a byproduct, a deterministic dynamic low-stretch tree under edge insertions/deletions with average stretch $n^{o(1)}$ and worst-case $n^{o(1)}$ update time (Theorem 1.2).

## Method
Builds on the [CKLPPS22] $\ell_1$-IPM framework that reduces min-cost flow to a dynamic sequence of $m^{1+o(1)}$ approximate undirected minimum-ratio cycle problems, then derandomizes the two random components. (1) **Vertex sparsification:** instead of sampling $O(1)$ of the $O(k)$ partial low-stretch forests to recurse on, recurse on *one* forest at a time, switching when it fails — analyzed via a new "shift-and-rebuild game." (2) **Edge sparsification:** replaces random subsampling in expander pieces with a deterministic spanner-with-embedding built by embedding $G$ into a deterministic expander $W$ and embedding $W$ back into $G$ via Chuzhoy–Saranurak decremental shortest paths [CS21] over a deterministic expander decomposition [CGLNPS20].

## Result
Deterministic exact min-cost flow in $m^{1+o(1)} \log U \log C$ time (Theorem 1.1), extending to high-accuracy convex-edge-cost flows (matrix scaling, entropy-regularized OT, $p$-norm flows, $p$-norm isotonic regression). Deterministic fully dynamic low-stretch tree on graphs with $\exp((\log n)^{O(1)})$ edge lengths in $n^{o(1)}$ worst-case time per update with $n^{o(1)}$ amortized recourse (Theorem 1.2). Dynamic spanner with bounded edge-congestion $m^{o(1)} k / 2^j$ per stretch bucket (Theorem 8.2).

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are continuous optimization / discrete geometry / extremal combinatorics — not graph-flow LPs. Tangential interest only: the $\ell_1$-IPM-via-min-ratio-cycles paradigm is conceptually adjacent to LP-bound techniques (Cohn–Elkies, Delsarte LP) but the algorithmic machinery doesn't transfer.

## Open questions / connections
- Deterministic algorithms for $1/\text{poly}\log$-accurate effective-resistance estimation and dynamic spectral vertex sparsifiers remain open (left unresolved here; would unlock derandomization of [LS19; BLLSSSW21; GLP22; BGJLLPS22]).
- Extends [CKLPPS22] $\ell_1$-IPM framework and the [GKKLP18; Mąd10] partial-trees lineage; resolves the partial-tree-subsampling randomness barrier specifically.
- Shift-and-rebuild game analysis (Section 7) is a new adaptive-adversary tool potentially applicable to other dynamic graph data structures.

## Key terms
minimum-cost flow, maximum flow, deterministic algorithm, interior point method, $\ell_1$-IPM, minimum-ratio cycle, low-stretch spanning tree, dynamic spanner, expander decomposition, vertex sparsifier, derandomization, shift-and-rebuild game
