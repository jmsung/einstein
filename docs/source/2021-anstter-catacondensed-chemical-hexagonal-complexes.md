---
type: source
kind: paper
title: Catacondensed Chemical Hexagonal Complexes: A Natural Generalisation of Benzenoids
authors: Cate S. Anstöter, Nino Bašić, Patrick W. Fowler, Tomaž Pisanski
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.13290v2
source_local: ../raw/2021-anstter-catacondensed-chemical-hexagonal-complexes.pdf
topic: general-knowledge
cites: 
---

# Catacondensed Chemical Hexagonal Complexes: A Natural Generalisation of Benzenoids

**Authors:** Cate S. Anstöter, Nino Bašić, Patrick W. Fowler, Tomaž Pisanski  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2104.13290v2

## One-line
Generalises catacondensed benzenoids to flat hexagonal polygonal complexes on arbitrary (possibly non-planar, possibly non-orientable) surfaces and proves all such complexes admit Kekulé (perfect matching) structures.

## Key claim
Every catacondensed flat hexagonal complex $B$ is Kekulean, with a constructive lower bound $K(B) \geq 4^p \cdot 2^q \cdot \prod_{i=1}^{k}(l_i + 1)$ where $p,q$ count untwisted/twisted cyclacenes and $l_i$ are linear-chain lengths after removing $A_3$/$A_2$ hexagons.

## Method
A scheme-based combinatorial language (extending Ringel's scheme for cellular embeddings) describing polygonal complexes via words over labelled literals with properties S1–S9 (flat, closed, chemical, catacondensed, hexagonal, oriented). A constructive proof deletes branching ($A_3$) and connecting ($A_2$) hexagons leaving a disjoint union of polyacene chains, untwisted/twisted cyclacenes, and $K_2$ fragments — each of which is independently Kekulean. Explicit Kekulé-counting polynomials in $(l+1)$ are derived via three "forcing rules" (linear-forcing, crossover, pairing) on branching hexagon bond-pair combinations.

## Result
Closed-form Kekulé counts as polynomials in $(l+1)$ for complexes built by inflating cubic graph edges with linear polyacenes of length $l$: e.g., $K(\Sigma_0; l) = (l+1)^{12} + 8(l+1)^9 + 32(l+1)^6 + 64(l+1)^3 + 64$ for the standard cube embedding, $K(D_0; 0) = 12500$ recovers the $C_{60}$ icosahedral fullerene Kekulé count via leapfrog; $k$-prism formula $((l+1)^3+2)^k - 2^k$ (odd $k$). DFT/B3LYP optimization on $C_{42}H_{18}$, $C_{84}H_{36}$, $C_{168}H_{72}$, $C_{420}H_{180}$ examples confirms all are potential-surface minima; phenanthrene (kinked) motifs preferred over anthracene (linear) by ~1.14 eV per 3-copy isomer.

## Why it matters here
General background; no direct arena tie — this is mathematical chemistry / topological graph theory on hexagonal tilings of surfaces, far from sphere-packing / kissing / autocorrelation problems. Tangentially relevant to any combinatorics problem involving perfect matchings on planar/toroidal hexagonal structures or fullerene-like enumeration.

## Open questions / connections
- Which toroidal polyhexes are uniquely determined by their skeleton graph?
- Kekulé-count formulas for Möbius-twisted catafusene motifs on higher-genus cubic-graph inflations.
- Fibonacene chains give $(F_{l+2})^m$ leading term and fully-Fries structures — possible connection to Fibonacci-extremal combinatorics.

## Key terms
catacondensed benzenoid, polygonal complex, Kekulé structure, perfect matching, hexagonal tiling, polyacene, fibonacene, cubic graph, leapfrog transformation, toroidal polyhex, Möbius cyclacene, fullerene, Fries number, Clar sextet, scheme (Ringel), HOMO-LUMO gap, DFT B3LYP
