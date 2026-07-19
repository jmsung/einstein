---
type: source
kind: paper
title: The Size of a Hypergraph and its Matching Number
authors: Hao-wei Huang, Po-Shen Loh, B. Sudakov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1107.5544
source_local: ../raw/2011-huang-size-hypergraph-its-matching.pdf
topic: general-knowledge
cites:
---

# The Size of a Hypergraph and its Matching Number

**Authors:** Hao-wei Huang, Po-Shen Loh, B. Sudakov  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1107.5544

## One-line
Verifies Erdős's 1965 conjecture on the maximum edge count of a $k$-uniform hypergraph with no $t$-matching, extending the known range by a factor of $k$.

## Key claim
For all $t < n/(3k^2)$, every $k$-uniform hypergraph on $n$ vertices with matching number $\nu(H) < t$ satisfies $e(H) \le \binom{n}{k} - \binom{n-t+1}{k}$ — the second Erdős extremal (all edges hitting a fixed $(t-1)$-set).

## Method
Shifting (the $(i,j)$-shift in extremal set theory) combined with induction on $t$ and $n$. The key new ingredient is a multicolored / rainbow-matching lemma (Lemma 3.1): if $|\mathcal{F}_i| > (t-1)\binom{n-1}{k_i-1}$ for each $i$, then a rainbow $t$-matching exists, proved by a uniform-random-permutation expectation argument plus shifting. This sharpens Erdős's degree-counting step from "max degree" to "$t$-th largest degree."

## Result
Theorem 1.2 extends the verified range from $t = O(n/k^3)$ (Bollobás–Daykin–Erdős 1976) to $t < n/(3k^2)$ — a factor-$k$ improvement. Corollary 3.2: any $k$-uniform hypergraph with $t$ vertices of degree $> 2(t-1)\binom{n-2}{k-2}$ and $kt \le n$ contains a $t$-matching. Theorem 3.3 establishes the multicolored analogue (Conjecture 1.3) in the same range, generalizing Kleitman.

## Why it matters here
General extremal-combinatorics background; no direct arena tie to the 23 problems currently mapped. Closest relevance is to Sidon-set / packing-style counting bounds where extremal set theory and the shifting technique inform upper-bound arguments. Potentially useful for sieve_theory / extremal_graph problems if any arena task reduces to "max edges with bounded matching."

## Open questions / connections
- Conjecture remains open in the wider range $n/(3k^2) \le t \le n/k$; tightening to $t < O(n/k)$ is the explicit next target.
- Fractional version (with Samuels-style probability conjecture) ties to perfect-matching minimum-degree thresholds (Alon–Frankl–Huang–Rödl–Ruciński–Sudakov) and Manickam–Miklós–Singhi nonnegative-$k$-sums.
- Question 4.1: multicolor product-type analogue of Pyber's extension of Erdős–Ko–Rado — maximize $\prod |\mathcal{F}_i|$ with no rainbow $t$-matching.

## Key terms
Erdős matching conjecture, hypergraph matching, $k$-uniform hypergraph, shifting technique, rainbow matching, Erdős-Ko-Rado, extremal set theory, fractional matching, Frankl, Kleitman, Bollobás-Daykin-Erdős, Samuels conjecture
