---
type: source
kind: paper
title: Partitioning Edge-Colored Hypergraphs into Few Monochromatic Tight Cycles
authors: Sebastián Bustamante, J. Corsten, Nóra Frankl, A. Pokrovskiy, J. Skokan
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.04471
source_local: ../raw/2019-bustamante-partitioning-edge-colored-hypergraphs-few.pdf
topic: general-knowledge
cites:
---

# Partitioning Edge-Colored Hypergraphs into Few Monochromatic Tight Cycles

**Authors:** Sebastián Bustamante, J. Corsten, Nóra Frankl, A. Pokrovskiy, J. Skokan  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.04471

## One-line
Proves that any $r$-edge-colored complete $k$-uniform hypergraph can be vertex-partitioned into a bounded number $c(k,r)$ of monochromatic tight cycles, confirming Gyárfás's conjecture.

## Key claim
For all $k,r,\alpha \in \mathbb{N}$, there exists $c=c(k,r,\alpha)$ such that every $r$-edge-colored $k$-graph $G$ with independence number $\alpha(G) \le \alpha$ can be partitioned into at most $c$ monochromatic tight cycles (Theorem 1.4). Corollary: same holds for $p$-th powers of tight cycles, settling Problem 6.4 of Elekes–Soukup–Soukup–Szentmiklóssy.

## Method
Combines the absorption method (Erdős–Gyárfás–Pyber style) with the strong hypergraph regularity lemma of Rödl–Schacht. Builds a monochromatic "crown" $T_t^{(k)}$ — a tight cycle base plus rim — that acts as a universal absorber, then greedily covers the remainder with vertex-disjoint monochromatic tight cycles. Key technical step (Lemma 2.10): in a $k$-partite $k$-graph where every $v$ in the small part has a link-graph of density $\ge \varepsilon$, the small part can be covered by boundedly many monochromatic tight cycles via Pósa's circuit theorem and a "blocks of 4 link-graphs with common intersection" argument.

## Result
$c(k,r,\alpha)$ exists and is independent of $|V(G)|$; the proof iterates the absorb-and-cover step $\alpha$ times, with termination guaranteed by Lemma 2.14 (an independent-transversal lemma with $\varepsilon(k,m) = m^{-(k-1)^2}$). No explicit numerical bound on $c$ is computed — the paper emphasizes existence and boundedness, not quantitative control. Extends Sárközy's $50rk\log(rk)$ loose-cycle bound to the tight-cycle regime.

## Why it matters here
General background; no direct arena tie. Pure extremal combinatorics / Ramsey-type partitioning — not relevant to any of the 23 arena problems (sphere packing, autocorrelation, kissing, sieve, etc.). Could marginally inform Problem 21/extremal-graph framings if any arena problem involves monochromatic-cycle-covers, but none currently do.

## Open questions / connections
- Pokrovskiy's Conjecture 1.1: can $r$ monochromatic cycles cover all but $c_r$ vertices of any $r$-edge-colored $K_n$? Still open.
- Explicit quantitative bounds on $c(k,r,\alpha)$ — proof gives only existence via regularity, so the constants are tower-type.
- Extension to $k$-graphs with $\alpha(G)$ growing with $n$ (current result requires bounded $\alpha$).

## Key terms
monochromatic tight cycle, edge-colored hypergraph, absorption method, hypergraph regularity lemma, Rödl–Schacht, independence number, Gyárfás conjecture, Lehel conjecture, Pokrovskiy, $p$-th power of cycle, crown hypergraph, link graph, independent transversal, Ramsey partition
