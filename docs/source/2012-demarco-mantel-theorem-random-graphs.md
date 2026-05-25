---
type: source
kind: paper
title: Mantel's theorem for random graphs
authors: B. DeMarco, J. Kahn
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1206.1016
source_local: ../raw/2012-demarco-mantel-theorem-random-graphs.pdf
topic: general-knowledge
cites:
---

# Mantel's theorem for random graphs

**Authors:** B. DeMarco, J. Kahn  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1206.1016

## One-line
Establishes the sharp threshold above which every maximum triangle-free subgraph of the Erdős–Rényi random graph $G_{n,p}$ is bipartite, extending Mantel's 1907 theorem to the sparse random setting.

## Key claim
There exists a constant $C$ such that if $p > C n^{-1/2} \log^{1/2} n$, then w.h.p. every maximum triangle-free subgraph of $G_{n,p}$ is bipartite (i.e., $t(G) = b(G)$). This is best possible up to $C$: for $p = 0.1\, n^{-1/2}\log^{1/2} n$, $G_{n,p}$ typically contains a 5-cycle of edges not lying in any triangle, breaking the equality.

## Method
Reduces the question to two structural lemmas about balanced cuts $\Pi=(A,B)$ of $G_{n,p}$: (i) any near-maximum triangle-free $F$ which avoids a "bad-pair" set $Q(\Pi)$ satisfies $\varphi(F,\Pi) := 2|F[A]|+|F[A,B]| < |\Pi|$; (ii) the max-cut $b(G)$ already exceeds $|\Pi| + 2|Q|$ for any $Q \subseteq G \cap Q(\Pi)$ obeying a degree constraint. Combined with the Kohayakawa– Łuczak–Rödl sparse-stability theorem (every large triangle-free subgraph is $o(n^2 p)$-close to bipartite) plus Chernoff tail bounds for degrees and codegrees, this forces $F_0 \subseteq \Pi$.

## Result
For $p > C n^{-1/2}\log^{1/2} n$, $t(G_{n,p}) = b(G_{n,p})$ w.h.p., with the stronger conclusion that the maximizer is itself bipartite. This closes the gap between Babai–Simonovits–Spencer ($p > 1/2$, 1990) and Brightwell–Panagiotou–Steger ($p > n^{-1/250}$, 2009), confirming the conjectured exponent $-1/2$. The threshold window is sharp: probability tends to 0 for $p \in [n^{-1}, 0.1 n^{-1/2}\log^{1/2} n]$.

## Why it matters here
General background for the extremal-graph / random-graph machinery: sparse-stability via Kohayakawa– Łuczak–Rödl, Chernoff codegree control, and "auxiliary bad-pair" $Q(\Pi)$ as a structural obstruction. No direct arena tie to a specific problem, but the sparse-regularity + max-cut framework informs extremal_graph and combinatorics problems where the random/extremal interaction matters.

## Open questions / connections
- Conjecture 1.2 (DeMarco–Kahn): the $K_r$ generalization with threshold $p > C n^{-2/(r+1)} \log^{2/((r+1)(r-2))} n$ — open at time of writing.
- Whether Theorem 1.1 can be proved without invoking the KLR/sparse-regularity Theorem 2.1.
- Connection to M. Kahle's conjecture on vanishing $k$-th homology of clique complexes $X(G_{n,p})$ — the $k=1, \Gamma=\mathbb{Z}_2$ case relates to even-intersection edge sets with triangles.
- Whether $f(p) = \Pr(t(G_{n,p}) = b(G_{n,p}))$ has a single local minimum in $p$ (unresolved guess).

## Key terms
Mantel's theorem, Turán theorem, triangle-free subgraph, max cut, bipartite subgraph, Erdős–Rényi random graph, $G_{n,p}$ threshold, Kohayakawa– Łuczak–Rödl theorem, sparse regularity, KLR conjecture, Chernoff inequality, extremal graph theory, clique complex homology, DeMarco–Kahn, Brightwell–Panagiotou–Steger
