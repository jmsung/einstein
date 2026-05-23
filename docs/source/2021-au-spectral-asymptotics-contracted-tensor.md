---
type: source
kind: paper
title: Spectral asymptotics for contracted tensor ensembles
authors: Benson Au, Jorge Garza-Vargas
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.01652
source_local: ../raw/2021-au-spectral-asymptotics-contracted-tensor.pdf
topic: general-knowledge
cites:
---

# Spectral asymptotics for contracted tensor ensembles

**Authors:** Benson Au, Jorge Garza-Vargas  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.01652

## One-line
Shows that contracting a random symmetric Wigner-type $d$-tensor against $d-2$ unit vectors yields a random matrix whose spectrum is asymptotically semicircular, with variance determined by a rescaled symmetrized inner product of the contracting tensors.

## Key claim
For a Wigner tensor $T_{d,N}$ and unit vectors $(u_N^{(i,j)})_{i\in I, j\in[d-2]}$, the family $\{N^{-1/2} T_{d,N}[u_N^{(i,1)}\otimes\cdots\otimes u_N^{(i,d-2)}]\}_{i\in I}$ converges in noncommutative distribution a.s. to a semicircular family with covariance $K_{i,i'} = \tfrac{1}{d(d-1)}\langle u_N^{(i,1)}\cdots u_N^{(i,d-2)}, u_N^{(i',1)}\cdots u_N^{(i',d-2)}\rangle$, and $K_{i,i}\in[1/d!,\, 1/(d(d-1))]$ with extremes characterized.

## Method
Tensorial extension of the RMT graphical/moment method: bipartite graphs with vertex classes for indices vs. tensors (diamonds for $d$-tensors, boxes for contracting vectors), letting the diagram track the dependence introduced by contraction while preserving access to independence in the underlying tensor. Quotient graphs $G_\pi$ over index partitions are bounded via a "double tree" criterion adapted from Wigner's classical argument; the permanental representation of symmetrized inner products and Marcus's permanent inequality pin down the extremal variances.

## Result
Theorem 1.6 gives a quantitative moment-method approximation: for any finite $I_0$, $m_0$, $M,\varepsilon>0$, $\mathbb{P}\big(\max |\tfrac{1}{N}\mathrm{Tr}\, P_N - \varphi(s\cdots s)| > \varepsilon\big) \le CN^{-M}$, with $C$ independent of the contracting vectors. The single-matrix ESD converges in Kolmogorov–Smirnov distance to the semicircle of variance $K^{(N)} = \tfrac{1}{d(d-1)}\|u_N^{(1)}\cdots u_N^{(d-2)}\|_2^2$. Upper bound $1/(d(d-1))$ attained iff the contraction is symmetric ($u^{(j)}=\pm u^{(j')}$); lower bound $1/d!$ attained iff the contracting vectors are orthonormal.

## Why it matters here
General background; no direct arena tie. Touches problems involving symmetric-tensor spectral methods or high-order Wigner-type random structures (none of the 23 arena problems map to this directly), and could inform later concept pages on tensor eigenvalues / free probability / semicircle universality if such material is ever ingested.

## Open questions / connections
- Extensions to general variance profiles $\sigma_\lambda^2$ produce a covariance formula via uniform block permutations and Möbius inversion — what closed forms exist beyond $d=3,4$?
- Behavior under localized vs. delocalized contracting vectors (sparse vs. dense) yields different limit covariances; what does this imply for tensor-PCA-style spiked models?
- Relation to traffic probability [Mal20, ACD+21] and to existing dependent-Wigner schemes ([BMP15], [GNT15], [HKW16], [BBvH]) — the contracted-tensor dependence falls outside all of them.

## Key terms
Wigner tensor, contracted tensor ensemble, semicircle law, free probability, semicircular family, symmetric tensor, Z-eigenvalue, GOTE, traffic probability, uniform block permutation, permanent inequality, moment method, double tree, Au, Garza-Vargas
