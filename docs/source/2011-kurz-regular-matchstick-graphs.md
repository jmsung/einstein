---
type: source
kind: paper
title: Regular Matchstick Graphs
authors: Sascha Kurz, R. Pinchasi
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.4372
source_local: ../raw/2011-kurz-regular-matchstick-graphs.pdf
topic: general-knowledge
cites:
---

# Regular Matchstick Graphs

**Authors:** Sascha Kurz, R. Pinchasi  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1401.4372

## One-line
Proves no finite 5-regular matchstick graph exists and establishes a lower bound of 20 vertices for any 4-regular matchstick graph.

## Key claim
**Theorem 2.1:** No finite 5-regular matchstick graph exists. **Theorem 3.6:** Every 4-regular matchstick graph has $n \geq 20$ vertices (closing part of the gap to the Harborth graph upper bound $m(4) \leq 52$).

## Method
Discharging method on the planar map of the graph. Starting charge $-\tfrac{1}{2}$ per vertex and $k-3$ per $k$-face (or $-1$ / $r-3$ in the 4-regular case), summing to $-6$ via Euler's formula. Charges flow from faces to vertices through internal angles $>\pi/3$ at a rate chosen so every vertex and bounded face ends non-negative, forcing a contradiction. The 4-regular bound also combines isoperimetric-style estimates: max area of a unit equilateral $k$-gon is $\tfrac{k}{4}\cot(\pi/k)$, and min area of an odd equilateral polygon is $\tfrac{\sqrt 3}{4}$ (Böröczky–Kertész–Makai).

## Result
- $m(5) = \infty$: no finite 5-regular matchstick graph; infinite examples exist (uncountably many, by row-shifting Fig. 1's construction).
- $m(4) \geq 20$ via Lemma 3.1: $n \geq (3k - 2l + 12)/2$ where $k$ = unbounded-face edges, $l \leq k-3$ = flat ($\pi$) outer angles.
- Auxiliary: $k \geq 11$ for the outer face (Lemma 3.5), using $f_3 \geq k+4$ from $\sum(4-r)f_r = 8$.

## Why it matters here
General background; no direct arena tie. Matchstick graphs (planar unit-distance, non-crossing edges, regular degree) are adjacent to no listed arena problem, but the **discharging method** and the **equilateral-polygon area bounds** are reusable for planar combinatorial-geometry problems should any arise (extremal graph / discrete geometry families).

## Open questions / connections
- Tightening $m(4)$: gap remains $20 \leq m(4) \leq 52$ (Harborth graph); Kurz [7] reaches $m(4) \geq 34$ via heavy computer search.
- Can the discharging weights here be re-tuned to improve $m(4)$ without massive case enumeration?
- Extension: characterize the uncountable family of infinite 5-regular matchstick graphs (combinatorial classification).
- Connects to Brass–Moser–Pach unit-distance bounds $u(n) = n^{1+O(1/\log\log n)}$.

## Key terms
matchstick graph, unit-distance graph, regular planar graph, discharging method, Euler formula, Harborth graph, equilateral polygon area, isoperimetric inequality, planar combinatorial geometry, Kurz, Pinchasi, Böröczky–Kertész–Makai
