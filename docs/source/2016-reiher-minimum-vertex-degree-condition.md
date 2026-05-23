---
type: source
kind: paper
title: Minimum vertex degree condition for tight Hamiltonian cycles in 3‐uniform hypergraphs
authors: Christian Reiher, V. Rödl, A. Ruci'nski, M. Schacht, Endre Szemer'edi
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.03118
source_local: ../raw/2016-reiher-minimum-vertex-degree-condition.pdf
topic: general-knowledge
cites:
---

# Minimum vertex degree condition for tight Hamiltonian cycles in 3‐uniform hypergraphs

**Authors:** Christian Reiher, V. Rödl, A. Ruci'nski, M. Schacht, Endre Szemer'edi  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.03118

## One-line
Proves the asymptotically optimal minimum vertex degree threshold guaranteeing a tight Hamiltonian cycle in a 3-uniform hypergraph.

## Key claim
For every $\alpha > 0$ and $n$ sufficiently large, every 3-uniform hypergraph $H$ on $n$ vertices with $\delta(H) \ge (5/9 + \alpha)\binom{n}{2}$ contains a tight Hamiltonian cycle; the constant $5/9$ is optimal, matched by three classical partition constructions.

## Method
Refined **absorption method** (Rödl–Ruciński–Szemerédi) adapted from pair-degree to vertex-degree regime. Three new ingredients: (1) a Robust Subgraph Lemma extracting a $(\beta,\ell)$-robust induced subgraph $R_v$ of density $\ge 5/9 + \alpha/2$ inside each link graph $L_v$, via an $\alpha/72$-inseparability argument; (2) a restricted Connecting Lemma for "$\zeta$-connectable" pairs (pairs lying in many robust subgraphs), giving $\Omega(n^{3\ell+1})$ tight paths of length $3(\ell+1)$ between any two such pairs; (3) a two-part absorber design — an absorbable vertex $z$ in a 2-edge path $xyy'x'$ plus a 3-edge path $abzcd$ — yielding $\Omega(n^9)$ absorbers per vertex. An almost-spanning tight cycle is then built using a reservoir set and a Faudree–Schelp long-path bound.

## Result
Establishes Theorem 1.1: $\delta(H) \ge (5/9 + o(1))\binom{n}{2}$ suffices for a tight Hamiltonian cycle, closing the gap left by the suboptimal upper bounds in Glebov–Person–Weps and Rödl–Ruciński–Schacht–Szemerédi. Matches the lower bound from three partition constructions ($|X| \approx n/3$, $|X| \approx 2n/3$, $|X| = \lfloor n/3 \rfloor - 1$ matching-blocker) all achieving $\delta \ge (5/9 - o(1))n^2/2$.

## Why it matters here
General background; no direct arena tie. The robust-subgraph + connectability framework is a generic structural template for extremal-degree spanning-substructure problems, potentially relevant if any Einstein Arena problem reduces to extremal hypergraph density (none of the 23 currently do as far as the wiki indexes).

## Open questions / connections
- Extension to $k$-uniform hypergraphs ($k \ge 4$): vertex-degree threshold for tight Hamiltonian cycles is open in general (see Rödl–Ruciński survey [16]).
- Exact (non-asymptotic) version for large $n$ — this paper is asymptotic only.
- Whether the absorption + connectability scaffolding generalizes to other spanning structures (perfect $F$-tilings, powers of Hamilton cycles) under vertex-degree conditions.
- Sidorenko-type input (Blakley–Roy inequality for paths) is used; relevance to autocorrelation/Sidon-set extremal problems is a possible cross-pollination thread.

## Key terms
tight Hamiltonian cycle, 3-uniform hypergraph, minimum vertex degree, Dirac-type theorem, absorption method, robust subgraph, connecting lemma, link graph, reservoir lemma, inseparability, Faudree–Schelp, Blakley–Roy, Sidorenko, extremal hypergraph
