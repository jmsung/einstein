---
type: source
kind: paper
title: On the Adjacency Spectra of Hypertrees
authors: Gregory J. Clark, Joshua N. Cooper
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.01466
source_local: ../raw/2017-clark-adjacency-spectra-hypertrees.pdf
topic: general-knowledge
cites:
---

# On the Adjacency Spectra of Hypertrees

**Authors:** Gregory J. Clark, Joshua N. Cooper  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.01466

## One-line
Characterizes the full homogeneous adjacency spectrum of a $k$-uniform hypertree ($k \geq 3$) via matching polynomials of induced sub-hypertrees, and uses this to spectrally characterize "power" hypertrees.

## Key claim
**Theorem 2:** For a $k$-uniform hypertree $H$ with $k \geq 3$, $\lambda \neq 0$ is an eigenvalue of $H$ iff there exists an induced sub-hypertree $H' \subseteq H$ such that $\lambda$ is a root of the matching polynomial $\varphi(H') = \sum_{i=0}^{m}(-1)^i |M_i| x^{(m-i)k}$. **Theorem 9:** A $k$-tree $H$ has spectrum $\sigma(H) \subseteq \mathbb{R}[\zeta_k]$ (cyclotomic) iff $H$ is a power tree.

## Method
Extends Zhang-Kang-Shan-Bai's result (which only captured eigenvalues with totally-nonzero eigenvectors) by projecting any eigenpair $(\lambda, x)$ onto $\text{supp}(x)$ to obtain a totally-nonzero eigenpair of the induced sub-hypergraph $H[\text{supp}(x)]$. Multiplicativity of $\varphi$ over connected components (Claim 5) plus a pendant-edge induction (Claim 6) reduces the disconnected case to Theorem 1. For Theorem 9, the obstruction to cyclotomicity is located in the $k$-comb subgraph, whose matching polynomial $\varphi(\text{comb}_k) = (1-\alpha)^k - \alpha^{k-1}$ (with $\alpha = x^k$) provably has non-real roots outside $\mathbb{R}[\zeta_k]$.

## Result
The eigenvalue set of a $k$-hypertree equals $\bigcup_{H' \in s(H)} \{\text{roots of } \varphi(H')\}$, where $s(H)$ is all induced sub-hypertrees. This is *strictly stronger* than the 2-uniform case (Cauchy interlacing fails to give equality for graphs). Power trees are exactly the $k$-trees whose spectra lie in the $k$-th cyclotomic extension of $\mathbb{R}$; non-power trees must contain a $k$-comb sub-hypergraph with $\geq 3$ disjoint edges off a central edge, forcing a root outside $\mathbb{R}[\zeta_k]$. Worked 11-vertex 3-uniform non-power example exhibited with explicit characteristic polynomial factorization.

## Why it matters here
General background; no direct arena tie. Hypergraph spectral theory and matching polynomials sit adjacent to but outside the current arena problem set (sphere packing, autocorrelation, kissing numbers, Sidon, LP/SDP duality). Could become relevant if a future problem involves tensor eigenvalues, hypergraph extremal combinatorics, or H-eigenvalue Laplacian bounds.

## Open questions / connections
- **Conjecture 14:** For $k$-trees $H' \subseteq H$ with $k \geq 3$, does $\varphi(H') \mid \phi(H)$ and $\phi(H') \mid \phi(H)$? Would explain the observed clean factorizations in the 11-vertex example.
- Extends Zhang-Kang-Shan-Bai 2017 (which gave only the totally-nonzero eigenvalue subset); related to Cooper-Dutle 2012 on hypergraph spectra and Hu-Qi-Shao 2013 on power hypergraphs.
- Sharp contrast with 2-uniform case (Cauchy interlacing) — a rare instance where spectral hypergraph theory has cleaner structure than graph theory; what other graph-theoretic obstructions vanish at $k \geq 3$?

## Key terms
hypertree spectrum, matching polynomial, k-uniform hypergraph, homogeneous adjacency tensor, power hypergraph, k-comb, cyclotomic spectrum, Qi eigenvalues, Cooper-Dutle, induced subtree, pendant edge, Heilmann-Lieb
