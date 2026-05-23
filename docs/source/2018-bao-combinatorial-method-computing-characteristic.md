---
type: source
kind: paper
title: A combinatorial method for computing characteristic polynomials of starlike hypergraphs
authors: Yan-Hong Bao, Yi-Zheng Fan, Yi Wang, Ming Zhu
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1806.06199
source_local: ../raw/2018-bao-combinatorial-method-computing-characteristic.pdf
topic: general-knowledge
cites:
---

# A combinatorial method for computing characteristic polynomials of starlike hypergraphs

**Authors:** Yan-Hong Bao, Yi-Zheng Fan, Yi Wang, Ming Zhu  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1806.06199

## One-line
Gives explicit and recursive formulas for the characteristic polynomial of the adjacency tensor of starlike $k$-uniform hypergraphs (hyperpaths, hyperstars, and their common-vertex amalgams) via the Poisson resultant formula combined with a chip-firing/dollar-game model on hypergraphs.

## Key claim
For the starlike hypergraph $S^k_{n_1,\dots,n_m}$ (and its specializations $P^k_n$, $S^k_m$), the characteristic polynomial $\phi(\lambda)$ factors explicitly: each factor $\lambda - g_{s-1}(1)/\lambda^{k-1}$ appears with multiplicity $\mu_{n,k}(s)$, where $g_i$ is a rational recursion (4.1) and $\mu_{n,k}(s)$ counts stable configurations of a specific stratum $B_s$ in the dollar game on $P^k_n$ (Theorems 4.6, 5.1).

## Method
Apply the Poisson product formula (Lemma 2.4) for resultants to factor $\phi_H(\lambda)$ as $\phi_{\hat H}(\lambda)^{k-1} \cdot \det(m_{f_w})$, with $w$ a cut/cored bank vertex. Then evaluate the determinant of multiplication by $f_w$ on the quotient algebra $A = \mathbb{C}[x_v]/\langle f_v\rangle$ combinatorially: identify a monomial basis with stable configurations of a hypergraph dollar game, build a "firing graph" $G(c_0)$ whose directed cycles correspond to critical configurations, and successively erase non-stable conﬁgurations by edge re-weighting to produce a triangular matrix whose diagonal entries give the eigenvalue factors.

## Result
Explicit closed-form characteristic polynomials are obtained for $P^k_n$, $S^k_m$, $S^k_{1,1,2}$, etc. Examples include $\phi_{P^3_1}(\lambda) = \lambda^3(\lambda^3-1)^3$, $\phi_{P^3_3}(\lambda) = \lambda^{151}(\lambda^3-1)^{27}(\lambda^3-2)^{18}(\lambda^6-3\lambda^3+1)^{27}$, and a degree-2294 formula for $S^3_{1,1,2}$. The structural count $\mu_{n,k}(s) = k^{s(k-2)}((k-1)^{k-1}-k^{k-2})(k-1)^{(n-s-1)(k-1)}$ for $s<n$, with $\mu_{n,k}(n) = k^{n(k-2)}$, comes from spanning-tree / critical-configuration counts on $K_k$ (Biggs' theorem 6.2, giving $k^{k-2}$).

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are hypergraph-spectral; this is a niche algebraic-combinatorics result on resultants of polynomial systems associated with hypergraph adjacency tensors. The chip-firing/sandpile group ↔ spanning trees correspondence (Lemma 2.7) and Poisson-formula resultant evaluation might marginally inform combinatorial counting problems but are not on any current solve path.

## Open questions / connections
- Extends Cooper–Dutle [3,4] (single-edge spectra, "all-ones" tensors) to richer hypergraph classes via the same Poisson lemma toolkit.
- Algebraic multiplicities of zero and nonzero eigenvalues for general power hypergraphs $G^k$ remain open even after Zhou–Sun–Wang–Bu [16] characterized which $\lambda^{2/k}$ lift.
- Whether the firing-graph technique generalizes beyond starlike topology (cycles, trees with non-cored cut vertices, dense hypergraphs) is not addressed.

## Key terms
hypergraph adjacency tensor, characteristic polynomial, resultant, Poisson formula, chip-firing game, dollar game, critical configuration, sandpile group, starlike hypergraph, hyperpath, hyperstar, spectral hypergraph theory
