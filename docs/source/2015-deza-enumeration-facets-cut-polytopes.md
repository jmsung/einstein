---
type: source
kind: paper
title: Enumeration of the facets of cut polytopes over some highly symmetric graphs
authors: M. Deza, M. D. Sikiric
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.05407
source_local: ../raw/2015-deza-enumeration-facets-cut-polytopes.pdf
topic: general-knowledge
cites:
---

# Enumeration of the facets of cut polytopes over some highly symmetric graphs

**Authors:** M. Deza, M. D. Sikiric  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1501.05407

## One-line
Complete facet enumeration of cut polytopes $\mathrm{CUTP}(G)$ for ~20 highly symmetric graphs with 15–30 edges, including $K_8$, $K_{3,3,3}$, $K_{4,4}$, and Petersen.

## Key claim
The Christof–Reinelt list of 147 facet orbits (217,093,472 facets) of $\mathrm{CUTP}_8 = \mathrm{CUTP}(K_8)$ is complete; the conjecture that every facet of $\mathrm{CUTP}_n$ is adjacent to a triangle-inequality facet is confirmed for $n=8$ (so the ridge graph of $\mathrm{CUTP}_8$ and $\mathrm{CUT}_8$ has diameter 4, and the subgraph of triangle facets has diameter 2).

## Method
Recursive adjacency decomposition method: start from one facet via LP, walk to adjacent facets, test equivalence under the restricted symmetry group $A_{\mathrm{Res}}(\mathrm{CUTP}(G))$ of order $2^{|V|-1}|\mathrm{Aut}(G)|$ using GAP partition backtrack, and recurse into high-incidence facets that themselves carry large symmetry. Completion is certified via Balinski's $m$-connectivity of skeleta plus a face-removal connectivity lemma (Theorem 1), letting small partial orbit-sets prove enumeration is complete without exhausting all orbits.

## Result
Facet counts (orbits): $K_8$: 217,093,472 (147); $K_{3,3,3}$: 624,406,788 (2015); $K_{1,4,4}$: 36,391,264 (175); $K_{5,5}$: 16,482,678,610 (1282); $K_{4,7}$: 271,596,584 (15); Petersen: 3,614 (4); Dodecahedron: 23,804 (5); Heawood: 5,361,194 (9); Möbius ladder $M_{14}$: 369,506 (9). For $K_5$-minor-free $G$ (Barahona–Mahjoub / Seymour), only chordless-cycle and non-triangle-edge inequalities are facets — verified across the polyhedra in the table.

## Why it matters here
General background on polyhedral combinatorics of cut/metric polytopes — the structural ancestor of Cohn–Elkies-style LP duality and SDP relaxations; relevant if any arena problem reduces to a max-cut, correlation, or $\ell_1$-embeddability question. The $\mathrm{CORP}(K_{n,m}) \cong \mathrm{CUTP}(K_{1,n,m})$ equivalence and the tight-Bell-inequality enumerations are tangentially relevant to autocorrelation / extremal-correlation problems.

## Open questions / connections
- Does the triangle-adjacency conjecture hold for all $n$? (Sampling at $n=10,11,12$ found only confirming simplicial facets.)
- Three-party Bell inequalities via $\mathrm{CUTP}(K_{1,n,m,l})$ — explicit facet lists still open beyond small $(n,m,l)$.
- Hypermetric polytope on 8 vertices (Deza–Sikiric, in prep) — a tighter relaxation between $\mathrm{CUT}_n$ and $\mathrm{MET}_n$.
- Extends Barahona–Mahjoub (1986) and Seymour (1981) characterizations of $K_5$-minor-free cut polytopes.

## Key terms
cut polytope, cut cone, metric polytope, facet enumeration, adjacency decomposition, $\ell_1$-embeddability, triangle inequality, Bell inequality, correlation polytope, Boolean quadric polytope, max-cut, $K_5$-minor-free, Balinski theorem, Petersen graph, Leggett–Garg
