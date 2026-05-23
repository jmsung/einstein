---
type: source
kind: paper
title: "Make Up Your Mind: The Price of Online Queries in Differential Privacy"
authors: Mark Bun, T. Steinke, Jonathan Ullman
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1604.04618
source_local: ../raw/2016-bun-make-your-mind-price.pdf
topic: general-knowledge
cites:
---

# Make Up Your Mind: The Price of Online Queries in Differential Privacy

**Authors:** Mark Bun, T. Steinke, Jonathan Ullman  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1604.04618

## One-line
Proves that the offline, online-non-adaptive, and online-adaptive query models in differential privacy are all strictly distinct, with exponential separations between each pair.

## Key claim
Three exponential separations: (1) a statistical-query family answerable for $k=2^{\Omega(\sqrt{n})}$ offline queries but only $k=O(n^2)$ online; (2) a search-query family answerable for $k=2^{\Omega(n)}$ online but only $k=O(1)$ adaptive; (3) for pure-DP threshold queries, $k=2^{\Omega(n)}$ offline vs $k=O(n)$ online. Conversely, approximate-DP can answer $k=2^{\Omega(n)}$ adaptive threshold queries via a new "BetweenThresholds" mechanism with sample complexity $n=O(\log k / \alpha\varepsilon)$.

## Method
Lower bounds use fingerprinting-code arguments (Tardos / [BUV14]) embedded into online query sequences, plus a randomized-response + majority-correlation attack for the online-vs-adaptive separation. Upper bounds: in the offline case, reduce the effective data universe to $\mathrm{poly}(nk)$ given the queries and apply the BLR mechanism; in the adaptive-threshold case, extend the sparse-vector technique to a two-threshold "BetweenThresholds" primitive with a propose-test-release stability argument, then partition the sorted dataset into $O(1/\alpha)$ chunks and run parallel online-interior-point solvers.

## Result
Theorems 1.1–1.4 establish the four separations above. BetweenThresholds (Theorem 5.8) is $(\varepsilon,\delta)$-DP and handles $k$ adaptive sensitivity-$1/n$ queries returning $\{L, R, \perp\}$ with $n=O(\sqrt{c\log(k/\varepsilon\delta)}/\varepsilon\alpha)$ where $c$ bounds the number of $\perp$ outputs. Corollary 5.17: adaptive thresholds released with $(\alpha,\beta)$-accuracy at $n=O((\log k+\log^{2.5}(1/\alpha)+\log(1/\beta\varepsilon\delta))/\alpha\varepsilon)$. Appendix A reproves the fingerprinting lemma $\mathbb{E}[f(x)\cdot\sum_i(x_i-p)+2|f(x)-x|]\geq 1/3$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the fingerprinting-lemma machinery and propose-test-release stability arguments are tools from extremal analysis / adaptive-data-analysis that could inform agent-side guards against verifier-overfitting, but none of the 23 Einstein Arena problems are differential-privacy problems.

## Open questions / connections
- Are the online and adaptive models equivalent for *statistical* queries (as opposed to the search-query separation shown here)? Left open.
- Tight sample complexity for adaptively-chosen threshold queries under approximate DP — gap between $O(\log k)$ upper bound and $2^{O(\log^* k)}$ offline bound of [BNSV15].
- Extends fingerprinting-code lower bounds of [BUV14, Tar08] and sparse-vector technique of [DNPR10, RR10, HR10]; connects to adaptive data analysis line [DFH+15, BNS+16].

## Key terms
differential privacy, fingerprinting codes, sparse vector technique, BetweenThresholds, propose-test-release, threshold queries, statistical queries, adaptive data analysis, randomized response, BLR mechanism, online vs offline separation, sample complexity
