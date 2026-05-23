---
type: source
kind: paper
title: Eigenvariety of nonnegative symmetric weakly irreducible tensors associated with spectral radius and its application to hypergraphs
authors: Yi-Zheng Fan, Yan-Hong Bao, Tao Huang
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1707.07414
source_local: ../raw/2017-fan-eigenvariety-nonnegative-symmetric-weakly.pdf
topic: general-knowledge
cites:
---

# Eigenvariety of nonnegative symmetric weakly irreducible tensors associated with spectral radius and its application to hypergraphs

**Authors:** Yi-Zheng Fan, Yan-Hong Bao, Tao Huang  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1707.07414

## One-line
Characterizes the set of eigenvectors at the spectral radius of a nonnegative symmetric weakly-irreducible tensor as a $\mathbb{Z}_m$-module determined by the Smith normal form of an incidence matrix, then applies this to count "extremal eigenvectors" of uniform hypergraphs.

## Key claim
For a nonnegative combinatorial-symmetric weakly-irreducible tensor $A$ of order $m$ and dimension $n$, the projective eigenvariety $V_{\rho(A)}(A)$ is finite and carries a $\mathbb{Z}_m$-module isomorphic to $S_0(A) = \{x \in \mathbb{Z}_m^n : B_A x = 0,\ x_1 = 0\}$, where $B_A$ is the tensor's incidence matrix. Consequently the *stabilizing index* $s(A) = |V_{\rho(A)}|$ divides $m^{n-1}$ and equals $m^{n-1-r}\prod_{i: d_i \ne 1} d_i$ where the $d_i$ are the invariant divisors of $B_A$ over $\mathbb{Z}_m$.

## Method
Build the abelian group $\mathcal{D}(A)$ of diagonal similarities $D$ with $A = e^{-i2\pi j/\ell}D^{-(m-1)}AD$ and its stabilizer subgroup $\mathcal{D}^{(0)}$; show $\mathcal{D}^{(0)}$ depends only on $\mathrm{supp}(A)$. Convert the multiplicative group via $D = \mathrm{diag}(e^{i2\pi\phi_k/m})$ into an additive $\mathbb{Z}_m$-module, identifying it with $\{x \in \mathbb{Z}_m^n : B_A x \equiv 0\}$. Decompose via Smith normal form over $\mathbb{Z}_m$ to get explicit invariants $s(A)$ (cardinality) and $\gamma(A)$ (composition length).

## Result
For a connected $m$-uniform *cored* hypergraph $H$ on $n$ vertices with $t$ edges: $s(H) = m^{n-1-t}$, $\gamma(H) = (n-1-t)\,\mathrm{cl}(m)$. For the $m$-th power $G^m$ of a simple graph $G$ ($n$ vertices, $t$ edges): $s(G^m) = m^{n-1+t(m-3)}$. The hyperpath $P_n^m$ achieves $s(P_n^m) = m^{(n-1)(m-2)}$; the complete hypergraph $K_n^{[m]}$ ($n \ge m+1$) has $s = 1$. General bounds: $s(G) \le m^{\mathrm{pc}(G)-1}$, $s(G) \le m^{n-\mu(G)-2}$, $s(G) \le m^{n-d(G)-1}$ where $\mathrm{pc}, \mu, d$ are path-cover number, matching number, and longest-path length. A subpattern relation $\mathrm{supp}(\hat A) \le \mathrm{supp}(A)$ implies $s(A) \mid s(\hat A)$ and $\gamma(A) \le \gamma(\hat A)$.

## Why it matters here
General background; no direct arena tie. Tensor spectral theory and uniform-hypergraph adjacency tensors don't currently surface in the 23 Einstein problems, though the Smith-normal-form reduction technique (combinatorial structure → algebraic invariants via integer-matrix canonical forms) is a general extremal-combinatorics tool that could touch extremal-graph or sieve-like problems if they reappear.

## Open questions / connections
- Tightness of the path-cover/matching/longest-path upper bounds for composite $m$ (the prime-$m$ case is exact via $\mathrm{rank}\,B_A$); when do the inequalities $s(G) \le m^{\mathrm{pc}(G)-1}$ etc. become strict?
- Extends Perron-Frobenius for nonnegative tensors (Chang-Pearson-Zhang, Friedland-Gaubert-Han, Yang-Yang) by counting all spectral-radius eigenvectors, not just the Perron one.
- Leaves open: characterizing the stabilizing index/dimension for non-combinatorial-symmetric tensors, and structural meaning of $\gamma(G) > 0$ beyond the 3-uniform tripartition criterion (Prop. 4.7).

## Key terms
nonnegative tensor, weakly irreducible tensor, Perron-Frobenius theorem, spectral radius, projective eigenvariety, Smith normal form, incidence matrix, $\mathbb{Z}_m$-module, stabilizing index, stabilizing dimension, cyclic index, uniform hypergraph, adjacency tensor, path cover number, cored hypergraph
