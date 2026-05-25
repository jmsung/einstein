---
type: source
kind: paper
title: The existence of designs II
authors: Peter Keevash
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1802.05900
source_local: ../raw/2018-keevash-existence-designs.pdf
topic: general-knowledge
cites:
---

# The existence of designs II

**Authors:** Peter Keevash  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1802.05900

## One-line
Extends Keevash's existence-of-designs framework to lattices of subset sums indexed by labelled faces of simplicial complexes, solving a wide class of partite, resolvable, and large-set hypergraph decomposition problems.

## Key claim
Under extendability + regularity (or typicality) and the appropriate fractional/integral lattice obstructions vanishing, the relevant hypergraph decomposition exists for all large $n$ — yielding resolvable $(n,q,r,\lambda)$-designs (Thm 1.1), large sets of designs (Thm 1.2), complete resolutions of $K_n^q$ (Thm 1.3), partite/typical $H$-decompositions (Thm 1.5, 1.7), and rainbow $K_q^r$-decompositions (Thm 1.11, 1.12).

## Method
General framework of vectors in $\mathbb{Z}^D$ indexed by injective functions on labelled $[q]$-complexes, decomposed by "elementary" generators $\gamma$. Proof strategy mirrors Keevash 2014: Randomised Algebraic Construction template + nibble + Clique Exchange Algorithm + integral-decomposition lattice analysis + randomised rounding (the local-decoding shortcut from designs is not available here). Key new ingredient: characterising the decomposition lattice in partite/coloured settings, where vertex-label-induced obstructions (e.g. the "twisted octahedron" in rainbow $K_4^3$) can appear beyond standard divisibility.

## Result
Resolves several longstanding open problems: existence of large sets of $(n,q,r,\lambda)$-designs for all valid $\lambda$ (extending Teirlinck, Lovett–Rao–Vardy); complete resolutions of $K_n^q$ when $n \equiv q \pmod{\mathrm{lcm}([q])}$; the Tryst Table Problem (Thm 1.10); rainbow clique decompositions. Also yields approximate counting: number of $r$-dimensional permutations of order $n$ is $(n/e^r + o(n))^{n^r}$ (Thm 1.8); number of generalized Sudoku squares with $n^2$ boxes of order $n$ is $(n^2/e^3 + o(n^2))^{n^4}$ (Thm 1.9).

## Why it matters here
General background; no direct arena tie. Design-existence machinery is adjacent to sphere-packing / kissing-number combinatorics but the arena problems here are continuous-geometry / autocorrelation, not block-design existence. Potentially relevant as a meta-lesson on lattice obstructions in integer relaxations of decomposition problems.

## Open questions / connections
- Full characterisation of when "additional" lattice obstructions beyond divisibility arise in partite / coloured settings (the twisted-octahedron phenomenon).
- Necessary divisibility conditions for fixed-rainbow $[q]^r$-decompositions when $r > q/2$ (Gottlieb's theorem fails to give full row rank).
- Extends Glock–Kühn–Lo–Osthus supercomplex framework to partite/coloured regimes they did not cover.
- Generalisation to non-vertex-regular $H$ in resolvable decompositions left to reader.

## Key terms
combinatorial design, hypergraph decomposition, resolvable design, large set of designs, Baranyai-type, Kirkman schoolgirl problem, partite decomposition, rainbow clique, Steiner system, Latin hypercube, Sudoku square, randomised algebraic construction, clique exchange algorithm, decomposition lattice, Keevash, Glock-Kühn-Lo-Osthus
