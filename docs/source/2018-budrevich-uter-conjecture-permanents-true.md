---
type: source
kind: paper
title: Kräuter conjecture on permanents is true
authors: M. Budrevich, A. Guterman
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1810.04439
source_local: ../raw/2018-budrevich-uter-conjecture-permanents-true.pdf
topic: general-knowledge
cites:
---

# Kräuter conjecture on permanents is true

**Authors:** M. Budrevich, A. Guterman  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1810.04439

## One-line
Proves the 1985 Kräuter conjecture: the permanent of an $n\times n$ $(\pm 1)$-matrix of rank $r+1$ is bounded sharply by $\operatorname{per} D(n,r)$, settling Wang's 1974 problem.

## Key claim
For $A \in M_n(\pm 1)$ with $n \geq 5$ and $\operatorname{rk} A = r+1$, $0 \leq r \leq n-1$: $|\operatorname{per} A| \leq \operatorname{per} D(n,r)$, with equality iff $A$ reduces to $D(n,r)$ via row/column permutations, transposition, or $\pm 1$ row/column scaling. The case $n=4$ has a single exception: $D(4,4)$ with $\operatorname{per} = 8 > 4 = \operatorname{per} D(4,3)$.

## Method
Induction on $n$ with two arms: (i) nonsingular case — reduce $A$ via standard transformations to a normal form ($D(n,n-1)$, $D(n,n)$, exceptional $P_1$/$P_2$ of order 6, or a "condition A" matrix), using block-diagonal $Q_k$ decompositions of rows with exactly two $-1$s; (ii) singular case — use a generalized Laplace expansion combined with a rank-vector majorization order $\leq^*$ on multisets $K(A)$ of $k\times k$ submatrices, proving $R(D(n,k,k-1)) \leq^* R(A)$ for any full-rank rectangular $A$, then chaining $\operatorname{mper}$ inequalities via bijections that lower rank.

## Result
Sharp bound $|\operatorname{per} A| \leq \operatorname{per} D(n,r)$ established for all $n\geq 5$ and all ranks $r+1 \in [1,n]$, with full equality classification. Auxiliary identities: $\operatorname{per} D(n,k-1) = \operatorname{per} D(n,k) + 2\operatorname{per} D(n-1,k-1)$ and $\operatorname{per} D(n,n) = (n-2)\operatorname{per} D(n-1,n-1) + (2n-2)\operatorname{per} D(n-2,n-2)$. Small values tabulated: $\operatorname{per} D(5,5)=8$, $\operatorname{per} D(6,6)=112$, $\operatorname{per} D(4,4)=8$, $\operatorname{per} D(4,3)=4$.

## Why it matters here
General background; no direct arena tie. Permanent-of-$\pm 1$-matrix bounds don't overlap the current 23-problem inventory (sphere packing, kissing, autocorrelation, etc.), but the **rank-vector majorization** technique — turning a combinatorial extremal problem into a partial order on multisets of submatrices, then proving the extremal object is $\leq^*$-minimal — is a transferable proof pattern for extremal-combinatorics problems where direct optimization fails.

## Open questions / connections
- Extension to permanents over other entry sets (e.g. roots of unity, integer-valued matrices) — the rank-vector framework is entry-agnostic in spirit.
- Sharper bounds on $\operatorname{per} D(n,k)$ asymptotics and ratios $\operatorname{per} D(n,k-1)/\operatorname{per} D(n,k)$ for use in related extremal questions (e.g. Hadamard-matrix permanent maxima).
- Open conjectures listed in Minc / Cheon–Wanless [3,15] surveys on permanents of $(\pm 1)$-matrices remain — Kräuter is one of several.

## Key terms
permanent, $\pm 1$-matrix, Kräuter conjecture, Wang problem, rank-vector majorization, generalized Laplace expansion, $D(n,k)$ family, mper, standard transformations, Minc survey, extremal combinatorics, sharp upper bound
