---
type: source
kind: paper
title: Universality of the Wigner-Gurau limit for random tensors
authors: Remi Bonnin
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2404.14144
source_local: ../raw/2024-bonnin-universality-wigner-gurau-limit-random.pdf
topic: general-knowledge
cites:
---

# Universality of the Wigner-Gurau limit for random tensors

**Authors:** Remi Bonnin  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2404.14144

## One-line
Generalizes Wigner's semicircle law to random symmetric $p$-tensors: the moments of Gurau's resolvent trace converge universally to Fuss–Catalan numbers via a hypergraph/melonic-graph combinatorial argument.

## Key claim
For a Wigner tensor $W_N \in S_p(\mathbb{R}^N)$ (independent up to symmetry, centered, off-diagonal variance $1/(p-1)!$, normalization $T/N^{(p-1)/2}$), the $n$-th balanced single trace invariant satisfies $\frac{1}{N}\mathbb{E}\,I_n(W_N) = \mathbb{1}_{n\text{ even}}\, F_p(n/2) + O(1/N)$ where $F_p(k) = \frac{1}{pk+1}\binom{pk+1}{k}$ are Fuss–Catalan numbers, with variance $O(1/N^2)$.

## Method
Combinatorial moment method on hypergraphs/combinatorial maps: trace invariants $\mathrm{Tr}_b(T)$ are indexed by $p$-regular combinatorial maps $b$, partitioned over edge-merging $\pi$; only "melonic" maps (dual to $p$-uniform double hypertrees) survive at leading order $N$. Counting argument uses bijection between rooted planar melonic maps, $p$-uniform plane hypertrees, $(p-1)$-Dyck paths, and non-crossing partitions with block sizes divisible by $p-1$ — all Fuss–Catalan-counted. Universality is extended to entries with only $p$ finite moments via a truncation + de la Vallée Poussin uniform integrability argument.

## Result
The limit law $\mu_\infty^{(p)}$ is a free Bessel law with compact support $[-p^{p/2}/(p-1)^{(p-1)/2},\, p^{p/2}/(p-1)^{(p-1)/2}]$, density $\mu_\infty(y) = |y| P_p(y^2)$ expressible via ${}_{p-1}F_{p-2}$ hypergeometric functions, and Cauchy–Stieltjes transform $R_\infty(z)$ satisfying $z^{p-2}R_\infty(z)^p - zR_\infty(z) + 1 = 0$ (generalizing the matrix semicircle equation). Theorem 3: under GOTE, the $k$-fold contraction $W \cdot u^k$ (deterministic unit $u$, $k \le p-2$) rescaled by $N^{k/2}$ yields moments of a dilated Wigner-Gurau law of order $p-k$ with scale $\sqrt{(p-1)/k}$ — recovering Couillet–Comon–Goulart's matrix-contraction result at $k=p-2$.

## Why it matters here
General background; no direct arena tie. Closest leverage: provides a rigorous moment-method template for tensor spectral problems should any Einstein Arena problem reduce to extremal questions on $p$-tensors or contracted-tensor matrices (none of the 23 currently do). The melonic/hypertree counting and Fuss–Catalan duality (planar melonic ↔ $(p-1)$-Dyck paths ↔ non-crossing partitions with block size divisible by $p-1$) is the most reusable combinatorial fact.

## Open questions / connections
- Free probability theory for random tensors — author flags as in-progress; would give a noncommutative-probability calculus for trace invariants.
- CLT and concentration inequalities for $\mathrm{Tr}_b(T)$ left open.
- Relation between the Wigner–Gurau limit measure and $z$-eigenvalues of tensors (number is exponential in dimension; spectral interpretation unknown).
- Connection to product of $p-1$ Ginibre matrices and Muttalib–Borodin gas (same free Bessel law appears) — mechanism not understood.
- Non-Gaussian / distinct-vector contraction case (extending Au–Garza-Vargas matrix result).

## Key terms
random tensors, Wigner-Gurau law, Fuss-Catalan numbers, free Bessel law, melonic graphs, combinatorial maps, hypertrees, trace invariants, Cauchy-Stieltjes transform, semicircle law generalization, GOTE, $(p-1)$-Dyck paths, non-crossing partitions, tensor contraction, hypergraph moment method
