---
type: source
kind: paper
title: Regular finite planar maps with equal edges
authors: A. Blokhuis
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.1799
source_local: ../raw/2014-blokhuis-regular-finite-planar-maps.pdf
topic: general-knowledge
cites:
---

# Regular finite planar maps with equal edges

**Authors:** A. Blokhuis  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.1799

## One-line
Proves no finite planar graph that is 5-regular can be drawn in the plane with straight equal-length edges (no 5-regular matchstick graph exists).

## Key claim
**Theorem 1:** There is no finite planar map with straight edges of equal length that is regular of degree 5. The proof extends to minimum-degree-5 planar maps with equal edges as well.

## Method
Discharging / Euler-formula combinatorics. Starting from $|V|-|E|+|F|=2$ and $5|V|=2|E|$, derive the face identity $\sum_i(10-3i)|F_i|=20$ and assign a charge $f(v)=\sum_i(10-3i)f_i(v)/i$ summing to 20. Equal-edge geometry caps a vertex at $\le 4$ surrounding triangles, restricting positive-charge configurations to "four triangles + pentagon/tetragon"; diagonal-insertion in diamonds and a local analysis on each pentagon $P\in F_5$ show $\sum_{v\in P} f(v)/f_5(v)\le 0$, contradicting the global sum.

## Result
Settles Harborth's 1981 Oberwolfach question for $k=5$: no 5-regular matchstick graph exists (smallest 5-regular planar graph — the icosahedron — cannot be straightened to unit edges). For $k\ge 6$ nonexistence is immediate from Euler; for $k=2,3,4$ small examples exist. The strengthened version rules out any finite planar map of minimum degree 5 with equal-length edges, via the inequality $|F_3|-2|F_4|-5|F_5|-8|F_6|-\cdots = 20 + \sum_{i\ge 6}2(i-5)v_i$.

## Why it matters here
General background on Euler-discharging arguments for planar/unit-distance configurations; potentially relevant to Einstein Arena problems on unit-distance graphs, discrete geometry, and rigid planar packings. No direct arena tie to a specific problem in the current inventory.

## Open questions / connections
- For $k=4$, the minimum-size 4-regular matchstick graph is still open (Harborth's example may not be minimal).
- Independently re-proved by Kurz & Pinchasi, *Amer. Math. Monthly* 118(3) (2011) 264–267 — comparing the two discharging schemes may yield sharper local lemmas.
- Discharging + equal-edge-length angle constraints is a transferable template for planar unit-distance extremal problems.

## Key terms
matchstick graph, unit-distance graph, planar regular graph, Euler formula, discharging method, 5-regular, icosahedron, Harborth problem, face-degree inequality, equilateral edge length, pentagon configuration, Blokhuis
