---
type: source
kind: paper
title: Coronoids, patches and generalised altans
authors: N. Bašić, P. Fowler, T. Pisanski
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.08547
source_local: ../raw/2015-bai-coronoids-patches-generalised-altans.pdf
topic: general-knowledge
cites:
---

# Coronoids, patches and generalised altans

**Authors:** N. Bašić, P. Fowler, T. Pisanski  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.08547

## One-line
Formalises coronoids (benzenoids with holes) and perforated patches purely via hexagon-incidence in the hexagonal grid, then defines a generalised altan operation that expands multiple perimeters simultaneously and gives closed-form Kekulé counts.

## Key claim
For a perforated patch $G$ with $K$ Kekulé structures, every iterated generalised altan $G' = A^{\mathbf{n}}(G;C_1,\dots,C_k)$ satisfies $K(G') = 2^{|\mathbf{n}|} K(G)$ where $|\mathbf{n}| = n_1+\cdots+n_k$; spokes have Pauling Bond Order $0$ and the other new edges have order $1/2$.

## Method
Combinatorial / topological formalisation: hexagonal systems as subsets of the infinite hex grid $H$, equipped with an adjacency-induced equivalence relation that yields connected-component decomposition (Lemma 6, Theorem 9) and a benzenoid closure operator (Definition 10, Lemmas 11–14). Patches are then recast as connected proper subsets of faces in a finite plane cubic graph; the altan operation is generalised by attaching a $2d$-cycle around each chosen perimeter $C_j$ (with $d$ = number of degree-2 vertices on $C_j$). Kekulé-count and bond-order results follow from the structural fact that spokes are forced single bonds, decoupling the new annulus from $G$.

## Result
- (Theorem 9 / Lemma 11) The complement $\bar K$ of any coronoid decomposes uniquely as $B_\infty \sqcup B_1 \sqcup \cdots \sqcup B_d$ where each finite $B_i$ is a benzenoid (corona hole) and $\bar{B_\infty}$ is the benzenoid closure $\hat K$.
- (Proposition 18) The hexagonal lattice has girth 6, and every 6-cycle is the border of a unique hexagonal face.
- (Theorem 43 / Corollary 44) The generalised altan of a (perforated) patch is again a (perforated) patch; 2-connectedness is preserved.
- (Theorem 47 / Corollaries 48–49) Kekulé multiplier is exactly $2^{|\mathbf{n}|}$; on the new perimeter every edge lies in $K/2$ Kekulé structures; altan-Kekuleanness $\iff$ original Kekuleanness.

## Why it matters here
General background; no direct arena tie. The paper is chemical graph theory (carbon nanostructure enumeration) and does not touch sphere packing, kissing numbers, autocorrelation, LP duality, or any of the 23 Einstein Arena problem families.

## Open questions / connections
- Extends Gutman's single-perimeter altan theory [19, 20] and the iterated-altan paper [1] to multi-perimeter / coronoid settings.
- Generalises Graver et al.'s fullerene-patch program [11–16] from simply-connected patches to perforated patches.
- Leaves open: when does a perforated fullerene patch (only 5- and 6-gons) extend to a closed fullerene? Characterisation of admissible boundary codes is non-trivial (cf. [2, 3, 18]).
- Bipartite-extension result (Proposition 41) hints at a constructive boundary-code completion algorithm not fully developed here.

## Key terms
coronoid, benzenoid, perforated patch, fullerene patch, generalised altan, iterated altan, Kekulé structure, Pauling bond order, hexagonal lattice, binary boundary code, corona hole, plane cubic graph
