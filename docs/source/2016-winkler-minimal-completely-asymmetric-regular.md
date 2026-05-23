---
type: source
kind: paper
title: Minimal completely asymmetric (4; n)-regular matchstick graphs.
authors: Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1609.06972
source_local: ../raw/2016-winkler-minimal-completely-asymmetric-regular.pdf
topic: general-knowledge
cites:
---

# Minimal completely asymmetric (4; n)-regular matchstick graphs.

**Authors:** Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1609.06972

## One-line
Constructs the smallest known completely asymmetric (4;n)-regular matchstick graphs for $4 \le n \le 11$, where every vertex has degree 4 or $n$, edges are unit length, and no symmetry of any kind is present.

## Key claim
For each $n \in \{4,\ldots,11\}$, explicit completely asymmetric (4;n)-regular matchstick graphs exist with edge counts 132, 125, 128, 189, 176, 277, 231, 771 respectively (vertex counts 66, 62, 63, 93, 87, 136, 114, 382); the $n=10$ (231 edges) and $n=11$ (771 edges) examples are also the smallest known overall, beating or matching prior symmetric records.

## Method
Construction-based: builds graphs from two rigid planar subgraphs — the "kite" ((2;4)-regular, 12 vertices, 21 edges, vertical symmetry) and the "triplet kite" ((2;3;4)-regular, 22 vertices, 41 edges) — combined via "double kite" / "reverse double kite" clasp connectors that join degree-2 vertices at variable distances. Rigidity and unit-edge feasibility are verified numerically with Stefan Vogel's Matchstick Graphs Calculator (MGC), a web-based computer algebra tool; the $n=11$ centerpiece requires solving an 11-angle constraint problem around a single degree-11 vertex with explicit angles given to ~16 digits (e.g., $32.362519660072210°$, $40.49207000332465°$, …).

## Method definitions
"Completely asymmetric" means: (i) rigid; (ii) no point/rotational/mirror symmetry; (iii) asymmetric outer shape; (iv) cannot be decomposed into rigid subgraphs and rearranged into a graph violating (i)–(iii). The fourth condition rules out, e.g., a 6-kite asymmetric layout that rearranges to a $C_3$-symmetric graph (Fig. 2).

## Result
Edge counts for completely asymmetric (4;n)-regular matchstick graphs: $n=4$: 132 (66 v); $n=5$: 125 (62 v); $n=6$: 128 (63 v, two variants); $n=7$: 189 (93 v); $n=8$: 176 (87 v); $n=9$: 277 (136 v); $n=10$: 231 (114 v); $n=11$: 771 (382 v). Geometries split into triplet-kite-based ($n=4{-}7$), kite+double-kite-based ($n=8{-}10$), and a special design for $n=11$ whose degree-11 vertex sits in a locally flexible subgraph stabilized by one critical edge.

## Why it matters here
General background; no direct arena tie. Relevant only as adjacent discrete-geometry / unit-distance literature — rigidity arguments and clasp-based modular construction may inform extremal planar configurations, but no Einstein Arena problem currently targets matchstick graphs or (m;n)-regular unit-distance graphs.

## Open questions / connections
- Open: the true minimum number of vertices for (4;n)-regular matchstick graphs for any $4 \le n \le 11$ — lower bounds remain absent (Kurz–Mazzuoccolo quote: "really hard task is to rigidly prove that no smaller example can exist").
- Open: does a symmetric (4;10)-regular matchstick graph with $\le 231$ edges exist? (Currently the asymmetric 231-edge example ties or beats all known symmetric versions.)
- Extends prior Winkler–Dinkelacker–Vogel work on symmetric (4;n)-regular graphs (arXiv:1604.07134) and the classical Harborth graph (52 vertices, 104 edges, 4-regular).

## Key terms
matchstick graph, unit-distance graph, (4;n)-regular, completely asymmetric, rigid planar graph, Harborth graph, kite subgraph, triplet kite, double kite, clasp construction, Matchstick Graphs Calculator, discrete geometry
