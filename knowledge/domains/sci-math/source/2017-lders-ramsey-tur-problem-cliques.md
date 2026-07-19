---
type: source
kind: paper
title: The Ramsey–Turán problem for cliques
authors: C. Lüders, Christian Reiher
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.03352
source_local: ../raw/2017-lders-ramsey-tur-problem-cliques.pdf
topic: general-knowledge
cites:
---

# The Ramsey–Turán problem for cliques

**Authors:** C. Lüders, Christian Reiher  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.03352

## One-line
Determines the exact asymptotic Ramsey–Turán edge density $f_t(\delta)$ for cliques $K_t$ when the independence-set parameter $\delta$ is sufficiently small relative to $t$.

## Key claim
For every $r \ge 2$ and $\delta \ll r^{-1}$: $f_{2r}(\delta) = \tfrac{3r-5}{3r-2} + \delta - \delta^2$ (even cliques) and $f_{2r+1}(\delta) = \tfrac{r-1}{r} + \delta$ (odd cliques), closing the gap left by Fox–Loh–Zhao's bounds $\tfrac{1}{4}+\delta-\delta^2 \le f_4(\delta) \le \tfrac{1}{4}+3\delta$.

## Method
Odd-clique case: edge-coloring argument splitting $G$ into a "red" $K_{r+1}$-free part (controlled by Turán) and a "green" low-degree part, with an averaging lemma forcing one of the two regimes per edge. Even-clique case: Szemerédi regularity → stability version of the Erdős–Hajnal–Sós–Szemerédi reduced-graph lemma → an iterative vertex-moving procedure producing an $(r,\varepsilon)$-exact partition $V(G)=B_1\sqcup\cdots\sqcup B_r$ satisfying ten precise size/density/local-degree conditions, then refined edge counting using a no-short-odd-cycle lemma ($e(G)\le \alpha(G)^2$ for $C_3,C_5,C_7$-free graphs).

## Result
The hard direction (Theorem 1.2): for $r \ge 2$ there exists $\delta^* > 0$ such that any $n$-vertex graph $G$ with $\alpha(G) < \delta n$ and $e(G) > \big(\tfrac{3r-5}{3r-2}+\delta-\delta^2\big)\tfrac{n^2}{2}$ contains $K_{2r}$. Matching lower bound via blow-up of Bollobás–Erdős $K_4$-construction on two classes plus Brandt-type triangle-free regular graphs on remaining $r-2$ classes. Recovers the Erdős–Hajnal–Sós–Szemerédi density $\varrho(K_{2r}) = \tfrac{3r-5}{3r-2}$ as $\delta \to 0$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the stability-plus-iterative-repartition pattern and the $C_3/C_5/C_7$-free $\Rightarrow e \le \alpha^2$ lemma are reusable extremal-graph techniques for problems involving forbidden substructures with independence-set side constraints.

## Open questions / connections
- Quantitative threshold: how small must $\delta$ be in terms of $r$? Paper requires $\delta \ll r^{-1}$ but explicit constants ($\delta < \tfrac{1}{289 r^5}$ for odd case) are likely far from tight.
- Extends Fox–Loh–Zhao (2015) by removing the $\Theta(\delta)$ gap; leaves the regime $\delta = \Theta(r^{-1})$ open.
- Hypergraph Ramsey–Turán analogues remain wide open (Turán for 3-uniform hypergraphs unsolved).

## Key terms
Ramsey-Turán, extremal graph theory, clique density, $K_t$-free, independence number, Szemerédi regularity lemma, stability method, Bollobás-Erdős construction, Brandt triangle-free regular graphs, Erdős-Hajnal-Sós-Szemerédi, Fox-Loh-Zhao, exact partition, odd-girth, Turán density
