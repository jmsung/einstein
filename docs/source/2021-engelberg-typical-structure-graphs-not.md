---
type: source
kind: paper
title: On the typical structure of graphs not containing a fixed vertex‐critical subgraph
authors: Oren Engelberg, Wojciech Samotij, L. Warnke
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.10931
source_local: ../raw/2021-engelberg-typical-structure-graphs-not.pdf
topic: general-knowledge
cites:
---

# On the typical structure of graphs not containing a fixed vertex‐critical subgraph

**Authors:** Oren Engelberg, Wojciech Samotij, L. Warnke  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.10931

## One-line
Determines the sharp threshold at which a uniformly random $H$-free graph with $n$ vertices and $m$ edges becomes "almost $(\chi(H)-1)$-partite" for $H$ in a broad class of vertex-critical graphs.

## Key claim
For every simple vertex-critical $H$ with $\chi(H)=r+1\ge 3$ and criticality $k+1$, there are constants $c_H, C_H>0$ and a threshold $m_H(n)$ such that a uniform random $F_{n,m}\in\mathcal{F}_{n,m}(H)$ lies in $\mathcal{G}(r,k)$ (admits an $r$-colouring with each colour class inducing max-degree $\le k$) w.h.p. when $m\ge C_H m_H$, and w.h.p. fails to when $n\ll m\le c_H m_H$ (the lower direction requires $H$ plain vertex-critical). The threshold is $m_H = n^{2-1/m_2(H)}$ if $m_2(H)>\eta(H)$, else $n^{2-1/\eta(H)}(\log n)^{1/(\zeta(H)-k-1)}$.

## Method
Two-sided threshold analysis: 0-statement via Hypergeometric Harris inequality counting $H$-free graphs "one edge away" from $\mathcal{G}(r,k)$; 1-statement via the Balogh–Morris–Samotij container/independent-sets-in-hypergraphs framework to get approximate $r$-colourability, then a delicate enumeration splitting into sparse/dense and low-degree/high-degree (regular/irregular) sub-cases. Core technical tool is the Hypergeometric Janson Inequality applied to families of critical-star extensions $H\setminus K_{1,k+1}$, with Lemma 3.3 (a hypergraph-container-style correlation bound) handling the irregular case.

## Result
Resolves Conjecture 1.3 of Balogh–Morris–Samotij–Warnke (2016) for all strictly 2-balanced, non-bipartite, edge-critical $H$, with sharp constants $c_H, C_H$ around $m_H = n^{2-1/m_2(H)}(\log n)^{1/(e_H-1)}$. Extends from edge-critical to the broader family of simple/plain vertex-critical graphs (1-statement only for plain; 0-statement also holds in that case). Generalises both Osthus–Prömel–Taraz (odd cycles) and the $K_{r+1}$ case.

## Why it matters here
General background; no direct arena tie — extremal graph theory on threshold phenomena for $H$-free graph structure, relevant only obliquely to discrete-combinatorics / extremal-graph arena problems (e.g. Turán-type density questions). Adds context on how sharp thresholds at $n^{2-1/m_2(H)}$ are derived via container method + Janson inequalities, which is a possible toolkit for any future arena problem cast as "typical structure of sparse forbidden-subgraph graphs."

## Open questions / connections
- What is the threshold $m_H$ for a *generic* vertex-critical $H$ (not just simple/plain)? Authors conjecture $m_H$ as defined here is not necessarily right.
- Between the approximate-colourability threshold $n^{2-1/m_2(H)}$ and the exact threshold $n^{2-1/\eta(H)}(\log n)^{1/(\zeta(H)-k-1)}$, what does the typical structure look like for plain vertex-critical $H$ with $\eta(H)>m_2(H)$ (e.g. $H=K_{1,2,3}$)?
- Extends Balogh–Morris–Samotij–Warnke (2016) $K_{r+1}$ result and Prömel–Steger (1992) edge-critical asymptotic enumeration; connects to Balogh–Samotij efficient container lemma (2020).

## Key terms
H-free graphs, vertex-critical, edge-critical, 2-density, strictly 2-balanced, chromatic threshold, Turán-type extremal, Hypergeometric Janson Inequality, hypergraph containers, asymptotic enumeration, critical star, Erdős–Kleitman–Rothschild, Prömel–Steger, Balogh–Morris–Samotij–Warnke
