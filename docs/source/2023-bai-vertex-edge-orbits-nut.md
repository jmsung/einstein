---
type: source
kind: paper
title: Vertex and Edge Orbits in Nut Graphs
authors: N. Bašić, Patrick W. Fowler, Toma Z Pisanski
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2312.03149
source_local: ../raw/2023-bai-vertex-edge-orbits-nut.pdf
topic: general-knowledge
cites:
---

# Vertex and Edge Orbits in Nut Graphs

**Authors:** N. Bašić, Patrick W. Fowler, Toma Z Pisanski  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2312.03149

## One-line
Proves that every nut graph has strictly more edge orbits than vertex orbits, ruling out edge-transitive nut graphs, and constructs infinite families realizing the small $(o_v, o_e)$ regimes.

## Key claim
For any nut graph $G$, $o_e(G) \geq o_v(G) + 1$ (Theorem 1). Corollary: no edge-transitive nut graph exists. This contrasts with Buset's general bound $o_e \geq o_v - 1$ for connected graphs — nut graphs are forced two steps above the generic floor.

## Method
Spectral/combinatorial argument on the one-dimensional kernel eigenvector $x \in \ker A(G)$: since the kernel is a 1D irrep of $\mathrm{Aut}(G)$, automorphisms act on $x$ with trace $\pm 1$, so $|x_i|$ is constant on each vertex orbit (Lemma 6). The vertex-orbit graph $\mathcal{G}(G)$ is analyzed; a sign-reversing automorphism is forced when an orbit-graph leaf (or odd cycle) has no intra-orbit edges, splitting inter-orbit edges into "like" $(+,+)/(-,-)$ vs "unlike" $(+,-)/(-,+)$ orbits — yielding the extra edge orbit. Constructions (bridge, subdivision, Fowler, multiplier $M_k$) are tracked for their effect on $\mathrm{Aut}$ and orbit counts.

## Result
Theorem 1: $o_e \geq o_v + 1$ for all nut graphs. Theorem 10: vertex-transitive nut graphs with $(o_v, o_e) = (1, 2)$ exist for every even $n \geq 8$, via antiprisms $A_\ell$, cartesian products $C_3 \square C_\ell$, and twisted products $C_k \tau C_\ell$. Theorem 22: nut graphs with $o_v = 2$ exist for all composite $n \geq 9$. Theorem 31: for every even $r \geq 2$ and $k \geq r+1$, infinitely many nut graphs with $(o_v, o_e) = (r, k)$. Lemma 5: every vertex-transitive nut graph has even degree $d$ and even order $n$, with kernel entries in $\{+1, -1\}$.

## Why it matters here
General background; no direct arena tie. Closest connection: P10 / extremal-graph problems involving symmetry-constrained spectra — but this is a structural result on a niche graph class (nut graphs / chemical graph theory), not an optimization tool the arena solver currently uses.

## Open questions / connections
- Conjecture 23 / Question 24: do $(o_v, o_e) = (2, 3)$ nut graphs exist for $n \in \{35, 55, 77, 95, \ldots\}$? Open for non-prime $n$ that are not even, not multiples of 3, and not perfect squares.
- Characterize all $(o_v, o_e)$ pairs realizable by nut graphs of given order; the odd-$o_v$ case is open.
- Cubic ($d = 3$) version of Theorem 10 is flagged as the next target (chemical-graph relevance).
- Most-symmetric nut graph on $n$ vertices is open; the $n=10$ champion (288 automorphisms) is not vertex-transitive.

## Key terms
nut graph, core graph, nullity one, kernel eigenvector, vertex orbit, edge orbit, edge-transitive, vertex-transitive, automorphism group, circulant graph, antiprism, cartesian product, Sciriha graph, Fowler construction, multiplier construction, Rose Window graph, GRR, graph spectra, sign-reversing automorphism
