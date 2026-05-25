---
type: source
kind: paper
title: The Graovac–Pisanski index of zig-zag tubulenes and the generalized cut method
authors: Niko Tratnik
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1702.04252
source_local: ../raw/2017-tratnik-graovac-pisanski-index-zig-zag.pdf
topic: general-knowledge
cites:
---

# The Graovac–Pisanski index of zig-zag tubulenes and the generalized cut method

**Authors:** Niko Tratnik  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1702.04252

## One-line
Generalizes the cut method for the Graovac–Pisanski (modified Wiener) index to any partition coarser than the $\Theta^*$-partition, then applies it to derive closed-form formulas for zig-zag carbon-nanotube graphs $ZT(n,h)$.

## Key claim
For any connected graph $G$ with orbits $V_1,\dots,V_t$ under $\mathrm{Aut}(G)$ and any edge partition $\{F_1,\dots,F_k\}$ coarser than the $\Theta^*$-partition, $\widehat{W}(G) = |V(G)| \sum_{j=1}^{k} \sum_{i=1}^{t} \frac{1}{|V_i|} W(G/F_j, w_{ij})$, where $w_{ij}(C)=|V_i \cap C|$. For odd $n$, $\mathrm{Aut}(ZT(n,h)) \cong D_h \times \mathbb{Z}_2$, and closed formulas for $\widehat{W}(ZT(n,h))$ are given in all four parity cases of $(n,h)$.

## Method
Combines orbit decomposition of the Graovac–Pisanski index (sum of Wiener indices over Aut-orbits) with a generalized quotient-graph cut method: every shortest-path distance $d_G(x,y)$ equals the sum of quotient-graph distances $\sum_j d_{G/F_j}(\ell_j(x),\ell_j(y))$ when the edge partition is coarser than $\Theta^*$. Automorphisms of zig-zag tubulenes are characterized by reducing to isomorphisms of the two boundary cycles $C_1,C_2$ (each of length $2h$), then extending uniquely layer-by-layer.

## Result
The cut-method generalization (Theorem 3.3) reduces $\widehat{W}(G)$ to weighted Wiener indices of quotient graphs over any $\Theta^*$-coarser partition (not only $\Theta^*$-classes themselves), broadening Ghorbani–Klavžar's 2016 result. For zig-zag tubulenes $ZT(n,h)$, $n \ge 1$, $h \ge 2$, eight explicit polynomial closed forms in $(n,h)$ are tabulated, split by parities of $n,h$ and by $n$ vs $h$ regime — e.g. for $h,n$ both odd with $n<h-2$: $\widehat{W}(ZT(n,h)) = \frac{h}{6}(n+1)^2(6h^2 + 3hn + 3h + n^2 + 2n - 3)$.

## Why it matters here
General background; no direct arena tie — chemical graph theory of carbon nanotubes is outside the current 23 Einstein Arena problem set (sphere packing, autocorrelation, kissing numbers, etc.). The cut method / $\Theta^*$-relation machinery is a generic distance-decomposition technique that could conceivably inform graph-distance combinatorial problems, but not the metric-geometry or analytic-LP problems that dominate the arena.

## Open questions / connections
- Can the generalized cut method extend to other symmetry-weighted topological indices beyond Wiener / Graovac–Pisanski?
- Does the $\mathrm{Aut}(ZT(n,h)) \cong D_h \times \mathbb{Z}_2$ result extend to chiral $(n,m)$-tubulenes with $n,m \ne 0$?
- Relation to topological efficiency / fullerene stability classifications (Cataldo–Ori, Ashrafi et al.) — does the index correlate with arena-relevant extremal configurations on hexagonal lattices?

## Key terms
Graovac-Pisanski index, modified Wiener index, cut method, Djokovic-Winkler relation, Theta-star partition, zig-zag tubulene, automorphism group, dihedral group, quotient graph, vertex-weighted Wiener index, hexagonal lattice, carbon nanotube
