---
type: source
kind: paper
title: On the probability of nonexistence in binomial subsets
authors: Frank Mousset, Andreas Noever, K. Panagiotou, Wojciech Samotij
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1711.06216
source_local: ../raw/2017-mousset-probability-nonexistence-binomial-subsets.pdf
topic: general-knowledge
cites:
---

# On the probability of nonexistence in binomial subsets

**Authors:** Frank Mousset, Andreas Noever, K. Panagiotou, Wojciech Samotij  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1711.06216

## One-line
Generalises Janson's inequality to give a hierarchy of upper/lower bounds on $\mathbb{P}[X=0]$ — the probability that a $p$-random subset avoids all edges of a hypergraph — in terms of joint cumulants of edge-indicator variables over connected clusters in the dependency graph.

## Key claim
For a hypergraph $\Gamma=(\Omega,X)$ with $p$-random subset $\Omega_p$, under mild conditions ($\max_\omega p_\omega = o(1)$, bounded dependency-graph expansion $\Lambda_k = O(1)$), for every fixed $k$:
$$\mathbb{P}[X=0] = \exp\!\big(-\kappa_1 + \kappa_2 - \cdots + (-1)^k\kappa_k + O(\delta_1 + \Delta_{k+1})\big),$$
where $\kappa_i = \sum_{V\in C_i}\kappa(\{X_j : j\in V\})$ sums joint cumulants over connected $i$-vertex subsets of the dependency graph. $k{=}1$ recovers Janson's inequality.

## Method
Cluster expansion of $\log\mathbb{P}[X=0]$ via joint cumulants, using only the Harris/FKG inequality (following Boppana–Spencer's proof of Janson). The expansion is organised by connected subsets in the dependency graph: $\kappa(A)=0$ whenever $A$ decomposes into independent parts, so only connected "clusters" contribute. Truncating at level $k$ leaves a controllable error governed by $\Delta_{k+1}$ (sum of joint moments over $(k{+}1)$-clusters) and $\delta_1$ (sum of $\mathbb{E}[X_i]^2$).

## Result
A specialised Theorem 10 gives a verifiable sparsity condition $D(\Gamma,p)=\max_{\Omega'}\sum_j d_j(\Omega')p^j = O(1)$, plus $D \le |\Omega|^{-\varepsilon}$ to force $\Delta_{k+1}=o(1)$ at some finite $k$. Applications: for $G_{n,p}$ with $p=o(n^{-7/11})$,
$$\mathbb{P}[\text{triangle-free}] = \exp\!\big(-\tfrac{n^3p^3}{6} + \tfrac{n^4p^5}{4} - \tfrac{7n^5p^7}{12} + \tfrac{n^2p^3}{2} - \tfrac{3n^4p^6}{8} + \tfrac{27n^6p^9}{16} + o(1)\big);$$
for $\{K_3,C_4\}$-free $G_{n,p}$ with $p=o(n^{-4/5})$, and for 3-AP-free $[n]_p$ with $p=o(n^{-4/7})$: $\exp(-n^2p^3/4 + 7n^3p^5/24)$.

## Why it matters here
General background; no direct arena tie. The cumulant-expansion framework is potentially relevant to problems involving rare-event probabilities or independent-set counting in structured hypergraphs (e.g. Sidon-set / autocorrelation / AP-avoidance problems), but the arena problems are deterministic extremal, not probabilistic.

## Open questions / connections
- Can the binomial-model results be transferred to the uniform model (e.g. $G_{n,m}$) via the conditioning identity sketched in §1.7?
- Could the framework count independent sets of bounded size in general hypergraphs, complementing the hypergraph container method (Balogh–Morris–Samotij; Saxton–Thomason)?
- Whether the bounded-expansion condition $\Lambda_k=O(1)$ is essential or can be relaxed.
- Extends Janson (1990), Suen (1990), Wormald (1996), Stark–Wormald (2018), Riordan–Warnke (2015).

## Key terms
Janson inequality, Harris-FKG inequality, joint cumulants, cluster expansion, dependency graph, binomial random subset, $G_{n,p}$, triangle-free random graph, arithmetic progression avoidance, Erdős-Rényi, hypergraph independent set, Stark-Wormald, Boppana-Spencer, $r$-balanced hypergraph
