---
type: source
kind: paper
title: Fast regocnition of planar non unit distance graphs
authors: Sascha Kurz
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.4375
source_local: ../raw/2014-kurz-fast-regocnition-planar-non.pdf
topic: general-knowledge
cites:
---

# Fast regocnition of planar non unit distance graphs

**Authors:** Sascha Kurz  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.4375

## One-line
Develops fast, coordinate-free necessary conditions to certify that a planar graph cannot be realized as a matchstick graph (planar unit-distance embedding with non-crossing straight edges).

## Key claim
Combining area, perimeter, and angle arguments — culminating in a linear program over local angle constraints — suffices to rule out every 3-connected 4-regular planar graph on $n \leq 33$ vertices as a matchstick graph, proving any such matchstick graph needs $n \geq 34$.

## Method
Three linear-time necessary criteria: (1) **area argument** — bound inner-face area using $A_{\max}(k) = \tfrac{k}{4}\cot(\pi/k)$ and $A_{\min}(s) = \sqrt{3}/4$ for odd $s$, combined with a BLP packing face-disjoint $\{3,3,4,4\}$/$\{3,4,4,4\}$ vertex configurations; (2) **perimeter argument** via triangle chains (Corollary 5: $k(M) \geq 2s+2$ for chains of length $s$ unless $M$ is a triangulation); (3) **angle argument** as an LP (4) enforcing $\pi/3$ at triangles, $\pi$ at quadrangle-adjacent pairs, $\geq \pi/2$ at $s\geq 5$ neighbors, and Euler face-angle sums $(|f|\pm 2)\pi$.

## Result
Filters of 3-connected 4-regular planar graphs (counts: 16387852863, 59985464681, 220320405895, 811796327750 for $n=30,31,32,33$) reduce to only 5, 50, 279, 5051 survivors after linear-time checks; all survivors are killed by LP (4), establishing the smallest 3-connected 4-regular matchstick graph has $\geq 34$ vertices. Existence at $n=52$ (Harborth graph) is known; the gap remains.

## Why it matters here
General background for discrete-geometry feasibility problems; the LP-based local-angle certificate and area/perimeter packing tricks are reusable patterns for **infeasibility certificates** in matchstick / unit-distance / planar-embedding Arena problems, complementing the SDP/LP-bound toolkit already in the wiki.

## Open questions / connections
- Smallest 4-regular matchstick graph: lower bound 34 here, smallest known is Harborth's at 52 — gap [34, 52].
- Smallest 3-regular matchstick graph with girth 5: smallest known has 180 vertices [Kurz–Mazzuoccolo].
- Maximum edge count $\tilde u(n)$: bounds $3n - \sqrt{12n-3} \leq \tilde u(n) \leq 3n - O(\sqrt n)$; lower bound conjectured tight.
- Exhaustive enumeration of matchstick graphs at moderate $n$ remains open.
- Connects to chromatic number of the plane (Hadwiger–Nelson).

## Key terms
matchstick graph, unit distance graph, planar embedding, 4-regular, Harborth graph, Euler formula, equilateral polygon area, triangle chain, binary linear program, angle argument LP, NP-hard recognition, chromatic number of the plane
