---
type: source
kind: paper
title: "Spectra of Variants of Distance Matrices of Graphs and Digraphs: A Survey"
authors: L. Hogben, Carolyn Reinhart
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.00647
source_local: ../raw/2021-hogben-spectra-variants-distance-matrices.pdf
topic: general-knowledge
cites:
---

# Spectra of Variants of Distance Matrices of Graphs and Digraphs: A Survey

**Authors:** L. Hogben, Carolyn Reinhart  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.00647

## One-line
Survey comparing four distance-related matrices ($D, D^Q, D^L, \mathcal{D}^L$) of graphs and digraphs, unifying spectral results on cospectrality, spectral radii, and characteristic-polynomial unimodality, with several new results filling gaps.

## Key claim
For any positive semidefinite matrix $M$, the characteristic polynomial coefficient sequence is log-concave and the absolute-value sequence is unimodal — extending the resolved Graham–Lovász unimodality conjecture (for trees, distance matrix) to $D^Q$ and $\mathcal{D}^L$ of any graph. Plus: $\rho(D), \rho(D^Q), \rho(D^L)$ are *strictly* edge-monotonically decreasing (sharpening prior "decreasing" results), and for transmission-regular graphs $D$-cospectrality forces equal transmission and equal Wiener index.

## Method
Spectral-graph-theory toolkit: Perron–Frobenius theory for $D$ (nonneg irreducible) and $D^Q$ (positive); Geršgorin disk theorem for digraph bounds; Jordan canonical form for non-symmetric digraph matrices (their eigenvalues can be complex). Coefficient unimodality is proved via the elementary-symmetric-function expansion $m_k = (-1)^{n-k} S_{n-k}(\mu_1,\dots,\mu_n)$ applied to PSD spectra, using the known log-concavity of characteristic-polynomial coefficients of real symmetric matrices and the sign-alternation–to–unimodality lemma from Brimkov et al. Twin-vertex partitions and equitable-partition / quotient matrices generate explicit eigenvectors; cousins generalize twins for cospectral constructions.

## Result
(i) Theorem 2.14: any PSD $M$ has log-concave coefficient sequence and unimodal $|m_k|$; applies to $D^Q$ and $\mathcal{D}^L$ of every graph. (ii) Twin theorem (Thm 3.1): if $v_k, v_{k+i}$ are twins, then $e_k - e_{k+i}$ is an eigenvector of $D^*$ for explicit $\lambda$ — e.g. $\lambda = (t+2)/t$ for independent twins under $\mathcal{D}^L$, giving multiplicity $\ge r-1$ for $r$ mutual twins. (iii) Spectral-radii strict edge-monotonicity for $D, D^Q, D^L$ (graphs); for digraphs, $\rho(D^L(\Gamma)) \le 2\max_v t(v)$ and $\rho(\mathcal{D}^L(\Gamma)) \le 2$ via Geršgorin. (iv) For $t$-transmission-regular graphs, $D$-cospectral $\Rightarrow$ equal $t$ and equal $W$ (since $t = \rho(D)$). (v) Cousin-based $D^L$-cospectral constructions (Thms 7.11, 7.12) generalizing twin-based ones; these do **not** extend directly to $\mathcal{D}^L$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems (sphere packing, autocorrelation, kissing, Sidon, extremal-graph) is a distance-spectrum problem on a finite graph. Weak indirect relevance: the unimodality-via-PSD argument (sign-alternation of elementary symmetric functions of nonnegative spectra) is a reusable lemma pattern for *any* PSD context the agent encounters (Gram matrices in sphere-packing LP/SDP duality, kernel positivity in Cohn–Elkies). Twin/quotient-matrix symmetry reduction is a generic technique for any structured eigenvalue problem.

## Open questions / connections
- Is $\rho(D^L(\Gamma)) \ge \rho(D^L(\Gamma + (u,v)))$ for *all* digraphs? (Question 8.12; verified for $n \le 5$.)
- Extend cousin constructions to give $\mathcal{D}^L$-cospectral families (open — known cousin recipe fails for normalized variant).
- Peak location of normalized distance-polynomial coefficients for trees: between $n/2$ and $(1-1/\sqrt 5)n$ (Shor / Collins conjecture); proven log-concave + unimodal in 2015, peak interval still open.
- Graham–Lovász question "does $n_+(G) > n_-(G)$ ever happen?" — answered yes by Azarija via strongly regular graphs, but full inertia classification remains open.

## Key terms
distance matrix, distance Laplacian, distance signless Laplacian, normalized distance Laplacian, Graham-Lovász conjecture, unimodality, log-concavity, characteristic polynomial coefficients, Perron-Frobenius, transmission regular, Wiener index, twin vertices, cousin vertices, cospectral construction, equitable partition, quotient matrix, Geršgorin disk theorem, Jordan canonical form, spectral radius, digraph distance spectrum, directed strongly regular graph, Cartesian product spectrum, lexicographic product spectrum, Hogben, Reinhart, Graham, Pollak, Lovász, addressing problem, squashed cube conjecture
