---
type: source
kind: paper
title: The Number of Small-Degree Vertices in Matchstick Graphs
authors: J'er'emy Lavoll'ee, K. Swanepoel
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2206.03956
source_local: ../raw/2022-lavollee-number-small-degree-vertices-matchstick.pdf
topic: general-knowledge
cites:
---

# The Number of Small-Degree Vertices in Matchstick Graphs

**Authors:** J'er'emy Lavoll'ee, K. Swanepoel  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2206.03956

## One-line
Proves that any matchstick graph (crossing-free unit-distance graph in the plane) on $n$ vertices must contain $\Omega(\sqrt{n})$ vertices of degree at most 4, strengthening Blokhuis's non-existence theorem for 5-regular matchstick graphs.

## Key claim
**Theorem 1:** For any matchstick graph on $n$ vertices with no isolated vertices and $n_i$ vertices of degree $i$, $4n_1 + 3n_2 + 2n_3 + n_4 > \sqrt{\pi\sqrt{3} \cdot n}$. **Corollary 2:** the number of vertices of degree $\leq 4$ exceeds $\tfrac{1}{4}\sqrt{\pi\sqrt{3} \cdot n}$. The $\sqrt{n}$ rate is asymptotically tight (matched by hexagonal-lattice construction with $n=3k^2+3k$).

## Method
Combines the Kurz–Pinchasi (2011) **discharging method** with the **isoperimetric inequality**. Initial charges: $i-6$ per vertex of degree $i$ and $2k-6$ per $k$-gon face. A geometry-aware redistribution rule transfers charge from face to vertex as a piecewise-linear function of the incident angle $\alpha$ (zero for $\alpha\leq\pi/3$, linear up to $2\pi/3$, capped at 1). A key lemma proves $b^2 > \pi\sqrt{3}\, f_3$ (boundary length $b$, triangular faces $f_3$) via isoperimetry on the polygonal boundary, extended to non-2-connected graphs by induction on cut-points.

## Result
After discharging, vertices of degree $\geq 5$ and all faces end up with non-negative charge, while low-degree vertices absorb the $-12$ Euler deficit. Combined with Euler's formula $2e \geq 4n - 8 + f_3$ and the isoperimetric lemma, one derives $b > \sqrt{\pi\sqrt{3} \cdot n} - \sqrt{\pi\sqrt{3}\cdot n + 8}$, yielding the $\Omega(\sqrt{n})$ bound on $4n_1 + 3n_2 + 2n_3 + n_4$.

## Why it matters here
General background for discrete-geometry / unit-distance problems; no direct Einstein Arena tie unless a problem targets matchstick or penny-graph structure. The **isoperimetric-bound-on-triangle-count** lemma and the **angle-weighted discharging rule** are reusable templates for any planar packing/extremal-graph problem where boundary length controls interior face count.

## Open questions / connections
- The constant $\pi\sqrt{3}$ is not tight — example construction gives $2\sqrt{3}(1+1/k)$; what is the true asymptotic constant?
- How to incorporate **quadrilateral** (rhombus) faces into the area lower bound when the matchstick graph has many non-triangular bounded faces?
- Extends Kurz–Pinchasi (2011) and the authors' prior edge-count paper (SIAM J. Discrete Math. 2022); related to Pach–Sharir / Radoičić–Tóth discharging surveys.

## Key terms
matchstick graph, penny graph, unit-distance graph, discharging method, isoperimetric inequality, Euler formula, planar graph, 5-regular graph, extremal combinatorics, Blokhuis, Kurz-Pinchasi, Harborth
