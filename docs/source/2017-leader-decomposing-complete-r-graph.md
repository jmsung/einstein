---
type: source
kind: paper
title: Decomposing the complete r-graph
authors: I. Leader, Luka Milićević, T. S. Tan
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1701.08335
source_local: ../raw/2017-leader-decomposing-complete-r-graph.pdf
topic: general-knowledge
cites:
---

# Decomposing the complete r-graph

**Authors:** I. Leader, Luka Milićević, T. S. Tan  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1701.08335

## One-line
Breaks the long-standing "easy" asymptotic upper bound for partitioning the complete $r$-uniform hypergraph into complete $r$-partite $r$-graphs, for all even $r \geq 4$.

## Key claim
For all even $r \geq 4$, $f_r(n) \leq \tfrac{14}{15}(1+o(1))\binom{n}{r/2}$, where $f_r(n)$ is the minimum number of complete $r$-partite $r$-graphs needed to partition $E(K_n^{(r)})$. This refutes the conjecture that Alon's $(1-o(1))\binom{n}{\lfloor r/2 \rfloor}$ upper bound was asymptotically sharp.

## Method
Introduce auxiliary function $g(n) = g(K_n, K_n)$, the minimum number of "blocks" (products $E(K_{a,b}) \times E(K_{c,d})$) partitioning $E(K_n) \times E(K_n)$. Show via a "blow-up" induction (Proposition 2) that any single improvement $g(K_a, K_b) < (a-1)(b-1)$ yields an asymptotic improvement of $g(n) \leq \beta n^2$ with $\beta < 1$ — a sub-multiplicativity / product-structure argument. Then construct an explicit decomposition of $E(K_4) \times E(K_6)$ into 14 < 15 blocks using an odd-cover of $K_6$ derived from a known odd cover of $K_8$ by four $K_{3,3}$'s (delete two vertices to break symmetry). Lift via Proposition 1 (splitting $V$ into halves and recursing on $f_4, f_3, g$).

## Result
$f_4(n) \leq \tfrac{14}{15}(1+o(1))\binom{n}{2}$ (Theorem 11), extended to all even $r \geq 4$ via $f_{2k+2}(n) \leq \sum_i f_{2k}(n-i)$. Lower bound $g(n) \geq \tfrac{(n-1)^2+1}{2}$ via reduction to weak-product graphs (Reznick–Tiwari–West). Auxiliary: $\tfrac{9}{5}(n-1) \leq g(K_3, K_n) \leq 2(n-1)$ via a weighted Graham–Pollak theorem.

## Why it matters here
General background; no direct arena tie. Useful as a methodological exemplar for **extremal combinatorics** problems: shows how an "obvious" greedy/star construction can hide an asymptotic gap, and how reducing to a *product question* with sub-multiplicative structure can turn a single small-case improvement into an asymptotic win — a pattern relevant to packing/covering problems where local constructions seem tight.

## Open questions / connections
- Is $g(n) = \tfrac{4}{5}(1+o(1))n^2$? (Question 14 — would give the conjectured tight constant.)
- Is $\alpha_5 < 1$, i.e., does the improvement extend to odd $r$? (Question 17; would imply $\alpha_r \to 0$ via Conjecture 16.)
- Extends Graham–Pollak ($f_2(n) = n-1$, 1971) and Alon's hypergraph generalization (1986); leaves open the analog of Alon–Bohman–Holzman–Kleitman product theorem for odd-box / uniform-cover partitions (Questions 3, 4).

## Key terms
Graham-Pollak theorem, hypergraph decomposition, complete r-partite r-graph, complete bipartite partition, weighted decomposition, weak product graph, odd cover, extremal combinatorics, blow-up construction, Alon hypergraph bound, $K_{3,3}$ odd cover of $K_8$, product partition theorem
