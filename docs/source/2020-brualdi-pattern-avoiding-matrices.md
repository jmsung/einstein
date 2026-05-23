---
type: source
kind: paper
title: Pattern-Avoiding (0,1)-Matrices
authors: R. Brualdi, Lei Cao
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2005.00379
source_local: ../raw/2020-brualdi-pattern-avoiding-matrices.pdf
topic: general-knowledge
cites:
---

# Pattern-Avoiding (0,1)-Matrices

**Authors:** R. Brualdi, Lei Cao  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2005.00379

## One-line
Determines the exact maximum number of 1's in an $m \times n$ (0,1)-matrix avoiding the patterns $12\cdots k$ or $312$, with constructive characterizations of extremal matrices.

## Key claim
For $12\cdots k$-avoiding $m \times n$ (0,1)-matrices, the maximum number of 1's is $c_{m,n}(12\cdots k) = (k-1)(m+n-(k-1))$ when $m,n \geq k-1$; for $312$-avoiding matrices, an analogous exact bound holds with a greedy construction. Conjecture 16 extends this to $k12\cdots(k-1)$-avoiding matrices with the same bound $(k-1)(m+n-(k-1))$.

## Method
Direct combinatorial / staircase-matrix arguments — partition the matrix into Toeplitz (left-to-right) diagonals, bound 1's per diagonal under the avoidance constraint, and exhibit extremal matrices via Ferrers / reverse-Ferrers arrays plus zigzag paths. A greedy algorithm constructs all extremal matrices when iterated over all choices. Avoids the asymptotic / probabilistic machinery (Marcus–Tardos, Füredi–Hajnal) used in prior $O(n)$-style bounds in favor of exact equality.

## Result
- $c_{m,n}(12) = m+n-1$, achieved by trivial 12-avoiding matrix (first row + first column all 1's).
- $c_{m,n}(12\cdots k) = (k-1)(m+n-(k-1))$ with full characterization of extremals.
- $312$-avoiding case: parallel exact result with explicit greedy / iterative construction (illustrated for $10 \times 10$).
- Conjecture 16: same bound $(k-1)(m+n-(k-1))$ for $k12\cdots(k-1)$-avoidance, verified in special case (single 0 in upper-right corner).
- Catalan tie: $\operatorname{per}_{\bar\sigma}(J_n) = C_n = \binom{2n}{n}/(n+1)$ for $\sigma \in \{123, 312\}$.

## Why it matters here
General background; no direct arena tie. Closest relevance is to extremal-combinatorics problems on the arena (discrete-geometry / extremal-graph / autocorrelation families) — the staircase + diagonal-counting style is a transferable extremal technique, and the $\sigma$-avoiding permanent is a nontrivial combinatorial counting object.

## Open questions / connections
- Conjecture 16: prove $(k-1)(m+n-(k-1))$ bound for $k12\cdots(k-1)$-avoidance in full generality.
- Question 17–19: max 1's / max permanent in $\sigma$-permutation-avoiding fully-indecomposable $n \times n$ matrices.
- Question 20: extendability of partial $\sigma$-avoiding permutations on subsets of $\{1,\ldots,n\}$.
- Extends Füredi–Hajnal (1992) conjecture and Marcus–Tardos (2004) Stanley-Wilf resolution from asymptotic $cn$ bounds to exact equalities for specific patterns.

## Key terms
pattern-avoiding permutation, (0,1)-matrix, 123-avoiding, 312-avoiding, permutation matrix, Stanley-Wilf conjecture, Füredi-Hajnal, Marcus-Tardos, Catalan number, staircase matrix, Ferrers array, zigzag path, extremal combinatorics, $\sigma$-avoiding permanent, Brualdi
