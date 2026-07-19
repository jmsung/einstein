---
type: source
kind: paper
title: Graphs that are cospectral for the distance Laplacian
authors: Boris Brimkov, Ken Duna, L. Hogben, Kate J. Lorenzen, Carolyn Reinhart, Sung Y. Song, Mark Yarrow
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1812.05734
source_local: ../raw/2018-brimkov-graphs-cospectral-distance-laplacian.pdf
topic: general-knowledge
cites:
---

# Graphs that are cospectral for the distance Laplacian

**Authors:** Boris Brimkov, Ken Duna, L. Hogben, Kate J. Lorenzen, Carolyn Reinhart, Sung Y. Song, Mark Yarrow  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1812.05734

## One-line
Constructs infinite families of non-isomorphic graphs sharing the same distance Laplacian spectrum, and proves the coefficients of the distance Laplacian characteristic polynomial are decreasing in absolute value.

## Key claim
Twin-vertex and "cousin"-vertex constructions yield infinite families of $D^L$-cospectral pairs (including bipartite pairs on $2k+5$ vertices), and the coefficients $\delta^L_k$ of $p_{D^L(G)}(x)$ satisfy $|\delta^L_1| \geq |\delta^L_2| \geq \cdots \geq |\delta^L_n| = 1$ for every connected graph $G$.

## Method
Combinatorial/linear-algebraic: identify vertex quadruples $\{\{v_1,v_2\},\{v_3,v_4\}\}$ ("cousins") with matching row-sum and induced-subgraph conditions, then exhibit an explicit Hadamard-style orthogonal similarity $S_i$ block-diagonal with $I_{n-4}$ that conjugates $D^L(G+v_1v_2)$ to $D^L(G+v_3v_4)$. For transmission-regular graphs, exploit $\partial^L_k = t(G) - \partial_k$ to transfer $D$-cospectrality results (strongly regular, distance-regular, Paley/circulant). Unimodality uses positive semidefiniteness of $D^L$ plus the real-rooted ⇒ log-concave ⇒ unimodal chain, sharpened by the Aouchiche–Hansen lower bound $\partial^L_2 \geq n$.

## Result
DL-cospectrality fails to preserve degree sequence, transmission sequence, edge count, girth, distance multiset, diameter, leaves, dominating vertices, cut-vertices, nontrivial automorphisms, clique/independence number, circulant-ness, and planarity (concrete small examples given). The Shrikhande graph and $K_4 \square K_4$ are DL-cospectral with spectrum $\{0, 24^{(9)}, 28^{(6)}\}$; the 41 SRGs with parameters $(29,14,6,7)$ form a mutually DL-cospectral family. Smallest DL-cospectral circulant pair: $\mathrm{Circ}_{16}(\{1,2,8\})$ vs $\mathrm{Circ}_{16}(\{1,6,8\})$. An infinite transmission-regular but not regular family $H_n$ ($n \geq 3$ odd) has $t(H_n) = (3n^2+1)/2$.

## Why it matters here
General background; no direct arena tie. Touches extremal graph theory / spectral graph theory tooling (cospectrality obstructions, unimodality of characteristic-polynomial coefficients) that could inform graph-based problems if any arena task reduces to spectrum recovery or transmission-regular structure.

## Open questions / connections
- Are acyclicity, bipartiteness, (transmission) regularity, and strong regularity preserved by $D^L$-cospectrality? Trees are conjectured DL-spectrally determined.
- Extends Aalipour et al. (2018) unimodality result for the distance characteristic polynomial of trees to the distance Laplacian for arbitrary connected graphs.
- Builds on Godsil–McKay (adjacency cospectral switching) and Heysse (distance cospectral) constructions; cousin sets generalize twin-vertex toggling.

## Key terms
distance Laplacian, cospectral graphs, transmission regular, twin vertices, cousin vertices, strongly regular graphs, Shrikhande graph, Paley graph, circulant graph, Hadamard matrix similarity, unimodality, log-concavity, characteristic polynomial coefficients, Wiener index, distance-regular graphs
