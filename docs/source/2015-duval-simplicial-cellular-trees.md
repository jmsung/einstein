---
type: source
kind: paper
title: Simplicial and Cellular Trees
authors: Art M. Duval, Caroline J. Klivans, Jeremy L. Martin
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1506.06819
source_local: ../raw/2015-duval-simplicial-cellular-trees.pdf
topic: general-knowledge
cites:
---

# Simplicial and Cellular Trees

**Authors:** Art M. Duval, Caroline J. Klivans, Jeremy L. Martin  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1506.06819

## One-line
A survey of the theory of spanning trees in higher-dimensional cell complexes, extending graph-theoretic trees, the matrix-tree theorem, and algebraic graph theory (critical groups, cuts/flows, matroids) to arbitrary dimension while accounting for torsion homology.

## Key claim
The "right" enumerator of $d$-dimensional spanning trees of a cell complex $X$ is the torsion-weighted count $\tau(X) = \sum_{T \in \mathcal{T}(X)} |H_{d-1}(T;\mathbb{Z})|^2$, which satisfies a cellular matrix-tree theorem $\tau_d(X) = c \cdot \det \tilde{L}$ generalizing Kirchhoff's theorem, and yields Kalai's formula $\tau(K_{n,d}) = n^{\binom{n-2}{d}}$ for the $d$-skeleton of the $n$-simplex (generalizing Cayley's $n^{n-2}$).

## Method
Homological/linear-algebraic: define a $d$-spanning tree of $X^d$ (with $\beta_{d-1}(X)=0$) as a subcomplex $T$ with $\beta_d(T) = \beta_{d-1}(T) = 0$, equivalently a column basis of the boundary matrix $\partial_d$. Apply Binet–Cauchy to the reduced combinatorial Laplacian $\tilde{L} = \partial_d \partial_d^* $ to expand $\det \tilde{L}$ as a sum over column bases, where each summand naturally carries the factor $|H_{d-1}(T;\mathbb{Z})|^2$ from the Smith normal form.

## Result
For Cohen–Macaulay-type complexes the correction factor $c=1$ and $\tau_d(X)$ is given exactly by a determinant or an alternating product of Laplacian-eigenvalue products $\prod \lambda_i^{(d)} / \prod \lambda_i^{(d-1)} \cdots$. Closed-form tree counts exist for complete simplicial skeletons (Kalai), complete colorful complexes (Adin, generalizing $\tau(K_{m,n}) = m^{n-1}n^{m-1}$), shifted complexes, matroid complexes, chessboard complexes, and hypercubes, all of which have integer Laplacian spectra. Critical-group / cut-lattice / flow-lattice theory extends with short exact sequences whose error term is $\mathrm{Tor}(H_{d-1}(X;\mathbb{Z}))$.

## Why it matters here
General background; no direct arena tie. Closest relevance is to the algebraic-combinatorics toolkit (Laplacian spectra, matroid duality, determinantal enumeration) that occasionally surfaces in extremal-graph / discrete-geometry problems, but the paper does not address sphere packing, kissing, autocorrelation, or any specific arena problem family.

## Open questions / connections
- Efficient sampling of random cellular spanning trees (Lyons, Pak): extending Wilson's loop-erased random walk beyond graphs; no known polynomial algorithm for sampling matroid bases in general.
- Combinatorial explanation of the cancellation of excess orientations of rooted forests down to $|\mathrm{Tor}(H_{d-1})|$ (Bernardi–Klivans).
- Stanley's $k$-uply-acyclic decomposition conjecture (refining the partitionability conjecture, the latter disproved in [DGKM15] using spanning-tree machinery); connection to Katthän's reduction of the depth conjecture to lattices on simplicial trees.
- Higher-dimensional Riemann–Roch / Baker–Norine theory: parallels between critical/cocritical groups on complexes and Picard/Jacobian groups of algebraic varieties.

## Key terms
spanning trees, cell complex, simplicial complex, matrix-tree theorem, combinatorial Laplacian, Cayley's formula, Kalai, torsion homology, critical group, sandpile, chip-firing, cellular matroid, cuts and flows, Tutte polynomial, arithmetic matroid, Cohen-Macaulay, Reisner, Binet-Cauchy, real projective plane, Krushkal-Renardy
