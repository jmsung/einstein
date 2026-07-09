---
type: source
kind: paper
title: Number of 1-Factorizations of Regular High-Degree Graphs
authors: Asaf Ferber, Vishesh Jain, B. Sudakov
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.10360
source_local: ../raw/2018-ferber-number-1-factorizations-regular-high-degree.pdf
topic: general-knowledge
cites:
---

# Number of 1-Factorizations of Regular High-Degree Graphs

**Authors:** Asaf Ferber, Vishesh Jain, B. Sudakov  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.10360

## One-line
Asymptotically tight lower bound on the number of 1-factorizations (edge-partitions into perfect matchings) of every $d$-regular graph on $n$ vertices with $d \geq n/2 + \varepsilon n$.

## Key claim
For sufficiently large even $n$ and $d \geq (1/2 + n^{-1/C})n$, every $d$-regular graph $G$ on $n$ vertices has at least $\left((1 - n^{-1/C})\, d/e^2\right)^{dn/2}$ distinct 1-factorizations, matching the Kahn–Lovász / Alon–Friedland upper bound $\left((1+o(1))d/e^2\right)^{dn/2}$ asymptotically.

## Method
Three-stage construction: (1) extract a "good" sparse $r$-regular bipartite subgraph $H \subseteq G$ (via random bipartition + Gale–Ryser $r$-factor existence + edge-sampling $G_p$) such that any near-regular supergraph of $H$ admits a 1-factorization, proved by iteratively pulling perfect matchings via Hall's theorem. (2) Partition $G' = G \setminus H$ into $K^3$ edge-disjoint subgraphs and apply a Rödl-nibble edge-coloring algorithm (Dubhashi–Grable–Panconesi) to produce the "correct" count of almost-1-factorizations. (3) Add the uncovered residual edges back into $H$ and complete via the good-subgraph property. Counting tracks the branching process of the nibble: probability $Q$ of any good leaf and overcounting factor $R$ per partial coloring, with $QR \leq (e^2/d)^{m}\cdot e^{O(\tau \log(m/\tau) m)}$.

## Result
Theorem 1.2: there exists universal $C > 0$ such that for $d \geq (1/2 + n^{-1/C})n$, $F(n,d) \geq \left((1 - n^{-1/C}) d/e^2\right)^{dn/2}$. Combined with Bregman/Kahn–Lovász upper bound, this is asymptotically optimal. Improves prior bounds: Cameron 1976 gave $((1+o(1))n/(4e^2))^{n^2/2}$ for $K_n$ (off by $4^{-n^2/2}$); Ferber–Jain improved to $((1+o(1))n/(2e^2))^{n^2/2}$; earlier general bounds were only $n^{(1-o(1))dn/2}$.

## Why it matters here
General background; no direct arena tie — this is extremal graph counting / combinatorial designs, not optimization. Closest arena adjacency is **extremal_graph** category problems and Rödl-nibble methodology (probabilistic packing/covering), which could inform problems involving edge-disjoint structure counting or packing.

## Open questions / connections
- Extend the asymptotic count from $d \geq n/2 + \varepsilon n$ down to the Csaba–Kühn–Lo–Osthus–Treglown existence threshold $d \geq 2\lceil n/4 \rceil - 1$.
- Use the explicit $(1+o(1))$-polynomial term to study typical 1-factorizations (e.g., rainbow Hamilton path in a typical 1-factorization of $K_n$), à la Kwan on Steiner triple systems.
- Counting 1-factorizations in regular hypergraphs — currently wide open; possibly via reduction to graph case + nibble completion.

## Key terms
1-factorization, perfect matching, regular graph, Rödl nibble, edge coloring, Bregman bound, permanent, Kahn-Lovász, Hall's marriage theorem, Gale-Ryser, Latin square enumeration, Dirac conjecture, extremal graph theory, probabilistic method, Chernoff bound
