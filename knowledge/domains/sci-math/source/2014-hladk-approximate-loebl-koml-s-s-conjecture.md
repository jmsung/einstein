---
type: source
kind: paper
title: The approximate Loebl-Komlós-Sós Conjecture II: The rough structure of LKS graphs
authors: Jan Hladký, János Komlós, Diana Piguet, Miklós Simonovits, Maya J. Stein, Endre Szemerédi
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1408.3871v4
source_local: ../raw/2014-hladk-approximate-loebl-koml-s-s-conjecture.pdf
topic: general-knowledge
cites: 
---

# The approximate Loebl-Komlós-Sós Conjecture II: The rough structure of LKS graphs

**Authors:** Jan Hladký, János Komlós, Diana Piguet, Miklós Simonovits, Maya J. Stein, Endre Szemerédi  ·  **Year:** 2014  ·  **Source:** http://arxiv.org/abs/1408.3871v4

## One-line
Paper II of a four-part series proving the approximate Loebl–Komlós–Sós conjecture: extracts a "rough" combinatorial structure (a well-connected regularized matching plus auxiliary sets) from the sparse decomposition built in Paper I.

## Key claim
For every $\alpha>0$ and large enough $k$, every $n$-vertex graph with at least $(\tfrac12+\alpha)n$ vertices of degree $\geq (1+\alpha)k$ admits, via its sparse decomposition, a rough structure (Lemma 5.4): two compatible regularized matchings $M_A,M_B$ on cluster pairs, plus partitioned vertex sets $X_A,X_B,X_C$ controlling captured edges into the low-degree side $S_0$, sufficient (after refinement in Papers III–IV) to embed any tree $T$ of order $k$.

## Method
Sparse-graph analogue of the dense regularity + cluster-matching approach: starting from the sparse decomposition (huge-degree set $\mathbb{H}$, regular pairs $G_{\text{reg}}$, expanding subgraph $G_{\text{exp}}$, avoiding set $\mathbb{E}$), the authors build "regularized matchings" — matchings of $\varepsilon$-regular dense pairs — and augment them using a Gallai–Edmonds-style separator/factor-critical decomposition plus alternating-path arguments (Lemma 4.8). A double-counting argument under the LKS degree hypothesis forces either a large matching covering $L$ or a large captured-edge bound into $S_0$.

## Result
Lemma 5.4 produces $(\varepsilon,\beta,\pi c)$-regularized matchings $M_A,M_B$ with: $V_1(M_B)\subseteq S_0$; controlled captured-edge counts $e_{G_\nabla}(X_A,S_0\setminus V(M_A))$ bounded by $\gamma kn$; uncaptured-edge bound $e_{G_{\text{reg}}}(V(G)\setminus V(M_A\cup M_B))<\varepsilon\Omega^*kn$; and at least one of two structural alternatives (K1) sufficient $X_A$-degree, or (K2) a large "good" sub-matching with both endpoints in $X_A$. This is the rough structure consumed by Paper III.

## Why it matters here
General background; no direct arena tie. Methodological interest only: the regularized-matching + sparse-decomposition framework is a template for handling sparse extremal problems where the classical Szemerédi regularity lemma is too weak — potentially relevant if any arena problem reduces to extremal-graph or tree-packing structure, but none currently do.

## Open questions / connections
- Extends Ajtai–Komlós–Szemerédi's unpublished Erdős–Sós work and Piguet–Stein 2012 (approximate LKS in dense setting) to the sparse regime.
- Full LKS conjecture (exact, not approximate) for general $k,n$ remains open; this series only handles $k>k_0(\alpha)$ with slack $\alpha$.
- The "regularized matching" + "avoiding set" toolkit may transfer to other sparse tree-embedding problems (Erdős–Sós, Komlós's tree-packing conjectures).

## Key terms
Loebl-Komlós-Sós conjecture, tree embedding, sparse regularity, regularized matching, sparse decomposition, dense spot, avoiding set, factor-critical, Gallai-Edmonds separator, regularity lemma, extremal graph theory, Szemerédi
