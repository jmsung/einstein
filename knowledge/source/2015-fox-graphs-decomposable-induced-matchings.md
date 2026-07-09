---
type: source
kind: paper
title: On graphs decomposable into induced matchings of linear sizes
authors: Jacob Fox, Hao Huang, Benny Sudakov
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1512.07852v1
source_local: ../raw/2015-fox-graphs-decomposable-induced-matchings.pdf
topic: general-knowledge
cites: 
---

# On graphs decomposable into induced matchings of linear sizes

**Authors:** Jacob Fox, Hao Huang, Benny Sudakov  ·  **Year:** 2015  ·  **Source:** http://arxiv.org/abs/1512.07852v1

## One-line
Determines the maximum number $t$ of induced matchings of linear size $r = cn$ that can edge-partition an $n$-vertex Ruzsa–Szemerédi graph, sharply for $c > 1/4$ and up to constants for $c = 1/4$.

## Key claim
For $(r,t)$-RS graphs: when $r = cn$ with $c > 1/4$, $r \le (n/4)(1 + 1/t)$ for odd $t$ and $(n/4)(1 + 1/(t+1))$ for even $t$ (tight); when $r = n/4$, $t \le (6+o(1))\log_2 n$; when $1/5 + \varepsilon \le c < 1/4$, $t = O(n/\log n)$; and for $c \ge 1/4 - b$ with $b > 0$ absolute, $t = n/((\log n) 2^{\Omega(\log^* n)}) = o(n/\log n)$.

## Method
Upper bound for $c > 1/4$ uses a Plotkin-style coding argument: characteristic vectors $v_i$ of matching vertex sets have Hamming distance $\ge 2r$, then double-count via Cauchy–Schwarz. The $n/4$ case builds an auxiliary subgraph $H$ on edges with high degree-sum, derives expansion via an inductive distance-set argument $|N_k| \ge \binom{s}{k}$, then sums to $n \ge 2^s$. The sub-$1/4$ regime greedily extracts a high-degree vertex sequence, applies Markov plus the triangle removal lemma (Fox 2011) to find a large RS-subgraph that violates Theorem 1.3.

## Result
Tight bound $r \le (n/4)(1 + 1/t)$ for odd $t$, matched by the Kneser graph $KG(2k+1, k)$ construction giving an $(n/4 + \Theta(n/\log n), \log_2 n + \Theta(\log\log n))$-RS graph. For $r = n/4$ exactly: hypercube gives $t \ge 2\log_2 n$ lower bound, matched up to factor 3 by the $(6+o(1))\log_2 n$ upper bound (and $t \le 2(\log_2 n + 1)$ for regular graphs). For $c$ slightly below $1/4$: $t = o(n/\log n)$, strictly improving the regularity-lemma bound.

## Why it matters here
General background; no direct arena tie. The Plotkin/Cauchy–Schwarz technique used here on characteristic-vector Hamming distances is the same kit that appears in coding-theoretic bounds for sphere packing and kissing-number arguments — potentially useful as a framing template for "edge-disjoint structure with linear-size pieces" counting problems.

## Open questions / connections
- Close the constant gap between $2\log_2 n$ (hypercube) and $(6+o(1))\log_2 n$ at $r = n/4$; conjectured $t \le 2\log_2 n + 2$.
- Bridge the Kneser graph ($r > n/4$, $t \sim \log n$) and hypercube ($r = n/4$, $t = 2\log n$) constructions parametrically.
- For $c < 1/4$ fixed, close the huge $O(n/\log n)$ vs $n^{\Omega(1/\log\log n)}$ (Fischer et al.) gap.
- Whether a Sanders-style $O(n/\log^{1-o(1)} n)$ bound (as known for Roth) holds for the Ruzsa–Szemerédi theorem itself.

## Key terms
Ruzsa-Szemerédi graph, induced matching, Plotkin bound, Hamming distance, Kneser graph KG(2k+1,k), hypercube construction, Roth's theorem, Behrend construction, 3-term arithmetic progression, triangle removal lemma, Szemerédi regularity lemma, bipartite double cover, Fox, Huang, Sudakov, extremal graph theory
