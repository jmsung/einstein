---
type: source
kind: paper
title: A note on geometric 3-hypergraphs
authors: Andrew Suk
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1010.5716v3
source_local: ../raw/2010-suk-note-geometric-3-hypergraphs.pdf
topic: general-knowledge
cites: 
---

# A note on geometric 3-hypergraphs

**Authors:** Andrew Suk  ·  **Year:** 2010  ·  **Source:** http://arxiv.org/abs/1010.5716v3

## One-line
Proves two Turán-type bounds for geometric 3-hypergraphs: $O(n^2)$ edges in the plane with no three strongly crossing edges, and $O(n^2)$ edges in 3-space with no two disjoint edges.

## Key claim
$\mathrm{ex}_2(SC_3^3, n) = \Theta(n^2)$ (settles Dey–Pach conjecture for $d=2$, $k=3$); $\mathrm{ex}_3(D_2^3, n) = \Theta(n^2)$ (settles Akiyama–Alon conjecture for $d=3$, $k=2$); and $\mathrm{ex}_2(SC_k^3, n) \le O(n^{3-1/k})$ for $k \ge 4$.

## Method
Reduce hypergraph extremal problems to geometric-graph extremal problems by fixing an apex vertex $v$ and looking at "base edges" of triangles containing $v$. Then apply Ackerman's theorem (geometric graphs with no 4 pairwise crossing edges have $O(n)$ edges), Valtr's lemma on segments crossing a line, Kővári–Sós–Turán bipartite bound, and Helly's theorem on the top-level of arrangements. For 3-space, use a spherical analogue of Pinchasi/Katchalski–Last (two "avoiding" arcs exist when edge count exceeds $2n-2$) on a small sphere around a high-degree vertex.

## Result
Plane, no 3 strongly crossing edges: $\Theta(n^2)$ — matching the trivial star lower bound, confirming Dey–Pach for this case. Plane, no $k \ge 4$ strongly crossing edges: $O(n^{3-1/k})$, improving prior $O(n^{3 - 1/((2k-1)\cdot 2)})$ from colored Tverberg. 3-space, no 2 disjoint edges: $\Theta(n^2)$. Convex-position 3-hypergraphs avoiding $k$ strongly crossing edges: $O(n^2)$ via Marcus–Klazar.

## Why it matters here
General background for discrete-geometry and extremal-hypergraph reasoning; the bridging technique (project hypergraph to apex-indexed geometric graphs, then apply known graph bounds) is a transferable proof pattern. No direct arena problem matches Turán-type 3-hypergraph thresholds, but the toolkit (Helly, Kővári–Sós–Turán, top-level arrangements, Tverberg) overlaps with the agent's discrete-geometry stack.

## Open questions / connections
- Dey–Pach conjecture $\mathrm{ex}_d(SC_k^{d+1}, n) = \Theta(n^d)$ remains open for $d \ge 2$, $k \ge 4$ (gap from $O(n^{3-1/k})$ to $n^2$).
- Akiyama–Alon conjecture $\mathrm{ex}_d(D_k^d, n) = \Theta(n^{d-1})$ open for $(d,k) \ne (2,\cdot), (3,2)$.
- Suk's plane bound implies $\Omega(|E|^5/n^{12})$ point-in-many-edges via Abstract Crossing Lemma + fractional Helly, but is weaker than Nivasch–Sharir's $\Omega(|E|^3 / (n^6 \log^2 n))$ — gap unexplained.

## Key terms
geometric hypergraph, Turán-type extremal, strongly crossing edges, Dey-Pach conjecture, Akiyama-Alon conjecture, colored Tverberg, Kővári-Sós-Turán, Helly theorem, Ackerman geometric graph, Pinchasi avoiding edges, fractional Helly, Marcus-Klazar, convex position, top level arrangement
