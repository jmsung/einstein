---
type: source
kind: paper
title: On the existence of 4-regular matchstick graphs
authors: Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1705.00293
source_local: ../raw/2017-winkler-existence-4-regular-matchstick-graphs.pdf
topic: general-knowledge
cites:
---

# On the existence of 4-regular matchstick graphs

**Authors:** Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1705.00293

## One-line
Proves that a 4-regular matchstick graph (planar unit-distance graph with every vertex of degree 4) exists for every integer $n \geq 63$.

## Key claim
**Theorem 1:** For every integer $n \geq 63$, there exists a 4-regular matchstick graph on $n$ vertices. Combined with sporadic small examples at $n \in \{52, 54, 57, 60\}$, this leaves only $n \in \{53, 55, 56, 58, 59, 61, 62\}$ as the (still open) excluded set above 51.

## Method
Constructive / building-block assembly. The authors fix a catalog of eleven $(2;4)$-regular matchstick graphs (every vertex degree 2 or 4, with exactly two degree-2 "ports") of orders 5–49, then glue three of them at their degree-2 vertices using Proposition 1 ($|V(G)| = \sum |V(G_i)| - k$ for $k$ blocks) to cover $63 \leq n \leq 120$. The flexible 5-vertex block (Fig. 4b) is then inserted into the $n \in \{94,95,96\}$ seed graphs to add 3 vertices per insertion, yielding all residues mod 3 from 97 onward. Geometric realizability/rigidity is verified by Vogel's Matchstick Graphs Calculator (MGC).

## Result
Existence for all $n \geq 63$, with $|E| = 2|V|$ (Prop. 2). The range $63 \leq n \leq 120$ minus $\{64,65,67,69,73,74\}$ is covered by 3-block combinations (Table 1, 120 distinct realizations); the six gaps are filled by explicit constructions (Fig. 3). The three seed graphs at $n = 94, 95, 96$ plus the 3-vertex flexible insertion close the tail $n \geq 97$. Tables 2 and 3 enumerate the smallest known $(2;4)$-regular and 4-regular examples up to isomorphism.

## Why it matters here
General background; no direct arena tie. Closest relevance is to discrete-geometry / unit-distance / packing problems where "exists for all sufficiently large $n$ via flexible building-block insertion" is a recurring proof pattern — potentially a template for constructive existence arguments on Einstein Arena combinatorial problems.

## Open questions / connections
- Does a 4-regular matchstick graph exist for any $n < 52$, or a non-isomorphic example at $n = 52$? (Open.)
- The seven values $n \in \{53,55,56,58,59,61,62\}$ remain open; only approximate (near-unit-length) solutions are known [Winkler 2020, arXiv:1906.11908].
- Extends Harborth's earlier $n \geq 63$ result by filling the omitted cases $\{65,67,73,74,77,85\}$; full catalog in Winkler 2021 (arXiv:1705.04715).
- The flexible "3-vertex insertion" trick is reminiscent of additive-basis / amalgamation arguments in extremal combinatorics — potential cross-pollination to other "exists for all large $n$" problems.

## Key terms
matchstick graph, 4-regular graph, planar unit-distance graph, (2;4)-regular graph, rigid graph, flexible graph, Harborth, building-block construction, vertex-to-vertex packing, equilateral triangle packing, discrete geometry, combinatorial geometry
