---
type: source
kind: paper
title: On the variational problem for upper tails in sparse random graphs
authors: E. Lubetzky, Yufei Zhao
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1402.6011
source_local: ../raw/2014-lubetzky-variational-problem-upper-tails.pdf
topic: general-knowledge
cites:
---

# On the variational problem for upper tails in sparse random graphs

**Authors:** E. Lubetzky, Yufei Zhao  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1402.6011

## One-line
Solves the asymptotic variational problem governing the upper-tail rate function for triangle (and $k$-clique) counts in sparse Erdős–Rényi random graphs $G_{n,p}$.

## Key claim
For $n^{-1/2} \ll p \ll 1$ and fixed $\delta>0$, $\varphi(n,p,\delta) \sim \min\{\tfrac{1}{2}\delta^{2/3},\tfrac{1}{3}\delta\}\, n^2 p^2 \log(1/p)$; for $n^{-1} \ll p \ll n^{-1/2}$, the minimum collapses to $\tfrac{1}{2}\delta^{2/3} n^2 p^2 \log(1/p)$ (the bipartite construction becomes infeasible).

## Method
Reduce the discrete problem on weighted graphs $G_n$ to a continuous graphon variational problem $\varphi(p,\delta)$ via Chatterjee–Varadhan/Lovász graph-limit machinery. Decompose $W = p + U$ and split $t(W)-p^3 = t(U) + 3p\,s(U) + 3p^2\mathbb{E}U$; bound each piece using Cauchy–Schwarz ($t(U) \le \|U\|_2^3$), Taylor expansion of $I_p$ near $p$, and a high-degree-vertex isolation argument controlling $\lambda(B)$ where $B=\{x: f(x)>b\}$. Generalizes to $k$-cliques via Finner's generalized Hölder inequality; for arbitrary subgraphs uses a spanning-subgraph lemma with $\Delta(H') \le 2$.

## Result
Two competing extremal constructions: a planted clique on $\delta^{1/3}np$ vertices (cost $\tfrac{1}{2}\delta^{2/3}$) vs a planted hub of $\tfrac{1}{3}\delta n p^2$ vertices connected to all others (cost $\tfrac{1}{3}\delta$); crossover at $\delta = 27/8$. For $K_k$: rate is $\min\{\tfrac{1}{2}\delta^{2/k}, \delta/k\}\, n^2 p^{k-1}\log(1/p)$. For general $H$ with max degree $\Delta$: rate $\asymp n^2 p^\Delta \log(1/p)$ when $p \ge n^{-\alpha(H)}$. Combined with Chatterjee–Dembo gives $-\log P(t(G_{n,p}) \ge 2p^3) \sim \tfrac{1}{3}n^2p^2\log(1/p)$.

## Why it matters here
General background; no direct arena tie. Tangentially relevant to extremal-graph / subgraph-density problems if any arena task involves graph homomorphism counts or large-deviation analysis of random configurations.

## Open questions / connections
- Behavior at the boundary $p \asymp n^{-1/2}$ where integrality forces deviation from the graphon minimizer.
- Whether the Chatterjee–Dembo nonlinear large deviation reduction extends throughout $\log n / n \ll p \ll 1$.
- Generalization to arbitrary $H$ via independence polynomials (followed up in Bhattacharya–Ganguly–Lubetzky–Zhao 2015), with dichotomy in $\delta$ iff $H$ is regular.
- Replica-symmetry-breaking phase for dense $p$ remains largely open.

## Key terms
upper tail, large deviations, Erdős-Rényi random graph, triangle counts, $k$-clique counts, variational problem, graphon, relative entropy, Chatterjee-Varadhan, Chatterjee-Dembo, Szemerédi regularity, Frieze-Kannan weak regularity, replica symmetry, Hölder inequality, planted clique, planted hub
