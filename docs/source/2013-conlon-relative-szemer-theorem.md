---
type: source
kind: paper
title: A relative Szemerédi theorem
authors: D. Conlon, J. Fox, Yufei Zhao
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1305.5440
source_local: ../raw/2013-conlon-relative-szemer-theorem.pdf
topic: general-knowledge
cites:
---

# A relative Szemerédi theorem

**Authors:** D. Conlon, J. Fox, Yufei Zhao  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1305.5440

## One-line
Proves that a single weak linear-forms pseudorandomness condition on a measure $\nu$ on $\mathbb{Z}_N$ is sufficient to guarantee that any positive-density subset contains $k$-term arithmetic progressions, drastically simplifying the Green–Tao framework.

## Key claim
For every $k \ge 3$ and $\delta>0$, if $\nu:\mathbb{Z}_N\to\mathbb{R}_{\ge 0}$ satisfies the $k$-linear forms condition (eq. (2): the $2^k\cdot k$ shifted product expectation equals $1+o(1)$, including all sub-products) and $0\le f\le \nu$ with $\mathbb{E}[f]\ge \delta$, then $\mathbb{E}[f(x)f(x+d)\cdots f(x+(k-1)d)]\ge c(k,\delta)>0$. The correlation condition and dual-function condition of Green–Tao/Tao are eliminated; the theorem now applies down to densities $N^{-c_k}$ (vs. only $N^{-o(1)}$ before).

## Method
Reduces the relative Szemerédi theorem to a **relative hypergraph removal lemma** via the standard Ruzsa–Szemerédi/Solymosi-type encoding. The removal lemma is proved by combining (i) a **sparse weak (Frieze–Kannan-type) hypergraph regularity lemma** with exponential complexity bounds and (ii) a new **sparse counting lemma** for subgraphs of pseudorandom hypergraphs. The technical core is a **densification** argument: iteratively replace one sparse edge by a $1$-bounded dense approximation using a strong linear forms inequality (Lemma 6.3), proved by repeated Cauchy–Schwarz / Gowers–Cauchy–Schwarz over the 2-blow-up of $H$.

## Result
The relative Szemerédi theorem (Thm 2.4), a relative multidimensional Szemerédi theorem (Thm 3.1, generalizing Furstenberg–Katznelson), a relative arithmetic removal lemma (Thm 3.3) for arbitrary linear systems, a sparse weak hypergraph regularity lemma (Thm 2.16, complexity $\le 2^{20r/\epsilon^2}$), and a sparse counting lemma (Thm 2.17) saying that for $0\le g\le \nu$, $0\le \tilde g\le 1$ on an $\epsilon$-discrepancy pair, hypergraph homomorphism densities of $g$ and $\tilde g$ agree up to $\gamma(\epsilon)$. Yields corner-free subset bound $o(|S|^2)$ in $S\times S$ for pseudorandom $S\subset \mathbb{Z}_N$ (Prop 7.1).

## Why it matters here
General background; no direct arena tie. Closest contact is with extremal-graph / additive-combinatorics problems involving pseudorandom hosts (sparse regularity, removal lemmas), which could inform any future problem touching arithmetic progressions, Sidon sets, or corner/extremal configurations in sparse subsets.

## Open questions / connections
- Is a single Gowers $U^s$-norm bound $\|\nu-1\|_{U^s}=o(1)$ sufficient for a relative Szemerédi theorem for $(r+1)$-APs (Gowers/Green question)? Bennett–Bohman show $s(2)>2$; lower bound $s(r)>1+\log_2 r$ is known.
- Develop sparse-graph-limit theory (Bollobás–Riordan conjectures); transfer Lovász–Szegedy graphon limits and Chung–Graham–Wilson quasirandomness to the sparse regime via this counting lemma.
- Replace Green–Tao transference in Conlon–Gowers random-graph KŁR-type theorems with the densification technique; extend to polynomial progressions (Tao–Ziegler) and Gaussian-prime constellations without correlation/dual-function conditions.

## Key terms
relative Szemerédi theorem, Green-Tao theorem, linear forms condition, pseudorandom measure, hypergraph removal lemma, Frieze-Kannan weak regularity, sparse regularity lemma, counting lemma, densification, Gowers uniformity norms, 2-blow-up, arithmetic progressions, corner-free sets, transference principle, Conlon, Fox, Zhao, Tao
