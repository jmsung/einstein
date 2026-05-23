---
type: source
kind: paper
title: A 3-regular matchstick graph of girth 5 consisting of 54 vertices
authors: Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.04304
source_local: ../raw/2019-winkler-3-regular-matchstick-graph-girth.pdf
topic: general-knowledge
cites:
---

# A 3-regular matchstick graph of girth 5 consisting of 54 vertices

**Authors:** Mike Winkler, Ph.D., P. Dinkelacker, Stefan Vogel  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.04304

## One-line
Constructs a 54-vertex 3-regular planar unit-distance (matchstick) graph of girth 5, slashing the prior smallest-known example from 180 vertices.

## Key claim
A 3-regular matchstick graph of girth 5 with only 54 vertices exists (vs. the Kurz–Mazzuoccolo 2010 lower bound of 30 and their 180-vertex example), realized as a point-symmetric planar graph in which all edges have unit length.

## Method
Explicit geometric construction: vertices are placed sequentially via 13 specified angles ($\alpha=102°, \beta=67°, \gamma=74°, \delta=81°, \epsilon=24°, \zeta=69°, \eta=106°, \theta=3°, \iota=61°, \kappa=85°, \lambda=91°, \mu\approx38.067°, \nu=65°$) and isosceles unit triangles, then mirrored via point symmetry. Correctness is verified by a continuity argument: holding subgraph $G_1$ fixed and varying $\mu$ from $39°$ to $37°$, the closing distance $|P_{53}P_{54}|$ sweeps continuously through unit length (from $\approx 0.991$ to $\approx 1.012$), so by IVT a $\mu$ realizing unit length exists. Verified interactively via the authors' Matchstick Graphs Calculator (MGC) software.

## Result
The construction yields a 54-vertex point-symmetric 3-regular planar girth-5 unit-distance graph; the bridging edge $P_{53}P_{54}$ attains exactly unit length at $\mu \approx 38.067338069376°$. This is a 3.33× improvement over the previous smallest known example (180 vertices) and approaches the Kurz–Mazzuoccolo lower bound of 30.

## Why it matters here
General background for discrete-geometry / planar unit-distance problems; informs construction-by-continuity techniques (vary one parameter, close a unit edge via IVT) and point-symmetry reductions that may transfer to Einstein Arena packing / contact-graph problems where unit-distance constraints close cycles. No direct arena tie — but the IVT-on-closure trick is a transferable specialization heuristic.

## Open questions / connections
- Does a 3-regular matchstick graph of girth 5 with fewer than 54 vertices exist? (Gap to the 30-vertex lower bound remains open.)
- Find 4-regular matchstick graphs for the missing vertex counts 53, 55, 56, 58, 59, 61, 62 — or below 52.
- Is there an efficient algorithm/elegant proof to decide whether a planar graph on <10 vertices is realizable as a matchstick graph?
- Companion paper [5] catalogs further examples at 58, 60, 64, 66, 68 vertices.

## Key terms
matchstick graph, unit-distance graph, 3-regular graph, girth 5, planar graph, point symmetry, isosceles triangle construction, intermediate value theorem closure, Kurz–Mazzuoccolo bound, Harborth graph, rigid subgraph, discrete geometry
