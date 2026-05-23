---
type: source
kind: paper
title: Ramsey numbers of ordered graphs
authors: M. Balko, Josef Cibulka, Karel Král, J. Kynčl
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1310.7208
source_local: ../raw/2013-balko-ramsey-numbers-ordered-graphs.pdf
topic: general-knowledge
cites:
---

# Ramsey numbers of ordered graphs

**Authors:** M. Balko, Josef Cibulka, Karel Král, J. Kynčl  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1310.7208

## One-line
Introduces Ramsey numbers for vertex-ordered graphs and shows that vertex ordering can change Ramsey growth from linear to superpolynomial, while sparse-ordered classes (bounded bandwidth, bounded degeneracy + interval chromatic number) retain polynomial bounds.

## Key claim
Ordered matchings $M_n$ on $n$ vertices exist with $R(M_n) \geq n^{\log n / (5 \log \log n)}$ (superpolynomial), yet ordered graphs of bandwidth $k$ satisfy $R(G) \leq C_k \cdot n^{128k}$ (polynomial). Monotone-cycle ordered Ramsey numbers are computed exactly: $R((C_r,\text{mon}),(C_s,\text{mon})) = 2rs - 3r - 3s + 6$.

## Method
Lower bound on matchings uses a recursive product construction seeded by the probabilistic Ramsey bound $R(K_r) \geq 2^{r/2}$, layering colorings across $r$-tuples of intervals. Upper bounds combine the Kővári–Sós–Turán bipartite extremal bound, Erdős–Szekeres off-diagonal Ramsey, and an interval-decomposition / common-neighborhood induction on $(k,q)$-decomposable graphs. The degeneracy bound uses a greedy embedding into candidate intervals with set-shrinkage by factor $t$ per update.

## Result
- $R((P_n,\text{alt})) \leq 2n - 3 + \sqrt{2n^2 - 8n + 11}$ (linear), via reduction to {0,1}-matrix Turán extremal theory.
- Every $(k,q)$-decomposable $G$ on $n$ vertices: $R(G) \leq C_k \cdot n^{128k(q-1)}$ with $C_k \leq 2^{O(k \log k)}$.
- $k$-degenerate, interval-chromatic-number $p$: $R(G) \leq n^{(1+2/k)(k+1)\lceil \log p\rceil - 2/k}$.
- Color-number dichotomy: $R(G;c)$ is either $\leq (2cn)^{n+1}$ (when $G \subseteq n \cdot K_{n,n}$) or $> 2^c$ (when $G$ contains one of 9 listed nonseparable interval-chromatic-3 graphs).
- Corollary: geometric and convex-geometric Ramsey numbers of $C_n$ equal $R((C_n,\text{mon})) = 2n^2 - 6n + 6$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems is an ordered-Ramsey instance. Tangentially relevant to discrete combinatorics / extremal-graph problems by supplying the ordered-Erdős–Szekeres framing and the Kővári–Sós–Turán + interval-chromatic decomposition toolkit, which is the same machinery used in autocorrelation and Sidon-set extremal arguments.

## Open questions / connections
- Problem 1: lower bounds for bounded-degree ordered graphs with interval chromatic number 2 — is $R(G_n) \geq n^{c\Delta}$ achievable?
- Problem 4: growth of $R_{nc}(n)$ (noncrossing ordered Ramsey) — currently only $n^{O(\log n)}$ known; polynomial would give polynomial convex-geometric Ramsey for outerplanar graphs.
- Conlon–Fox–Lee–Sudakov [15] independently improved the degeneracy bound to $n^{ck \log p}$, beating Theorem 8 here.

## Key terms
ordered Ramsey number, ordered graph, monotone path, monotone cycle, alternating path, interval chromatic number, bandwidth, degeneracy, Erdős–Szekeres, Kővári–Sós–Turán, geometric Ramsey number, ordered matching, Conlon–Fox–Lee–Sudakov, separable ordered graph, extremal {0,1}-matrix
