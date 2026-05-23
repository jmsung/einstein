---
type: source
kind: paper
title: The Ramsey number of loose cycles versus cliques
authors: Arès Méroueh
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1504.03668
source_local: ../raw/2015-mroueh-ramsey-number-loose-cycles.pdf
topic: general-knowledge
cites:
---

# The Ramsey number of loose cycles versus cliques

**Authors:** Arès Méroueh  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1504.03668

## One-line
Improves upper bounds on the hypergraph Ramsey number $R(C_l^r, K_n^r)$ for loose cycles versus cliques, breaking the "graph bound" for 3-uniform hypergraphs.

## Key claim
For any fixed $l \geq 3$: $R(C_l^3, K_n^3) = O(n^{1+1/\lfloor (l+1)/2 \rfloor})$; in particular $R(C_5^3, K_n^3) = O(n^{4/3})$, sharpening the prior $O(n^2)$ bound of Collier-Cartaino–Graber–Jiang. Also, for $r \geq 4$ and odd $l \geq 5$: $R(C_l^r, K_n^r) = O(n^{1+1/\lfloor l/2 \rfloor})$.

## Method
Bounds the independence number of $C_l^3$-free 3-graphs by partitioning edges into "light" (pair in $<2l-2$ edges) and "heavy" pairs, then forming a reduced $[2,3]$-graph $H^*$. Introduces **extenders** — pairs $(X,Y)$ where any two $X$-vertices are joined by many simple length-2 paths — as the 3-graph analogue of vertex neighborhoods, and shows large extenders or their $i$-th neighborhoods contain large independent sets via Pluhár's path-coloring lemma and Spencer's hypergraph Turán bound. A greedy procedure either finds large independent sets inside extender neighborhoods or applies Spencer to a low-degree residual.

## Result
$R(C_5^3, K_n^3) \leq c_{3,5} n^{4/3}$; general $R(C_l^3, K_n^3) \leq c_{3,l} n^{1+1/\lfloor(l+1)/2\rfloor}$ (Theorem 1.5). For $r \geq 3$, odd $l \geq 5$: $R(C_l^r, K_n^r) \leq c_{r,l} n^{1+1/\lfloor l/2\rfloor}$ (Theorem 1.6), completing the graph-bound analogue for odd $l$. Equivalently: every $C_l^3$-free 3-graph on $n$ vertices has independence number $\Omega(n^{(m+1)/(m+2)})$ with $m=\lfloor(l-1)/2\rfloor$.

## Why it matters here
General background; no direct arena tie. Possibly informs extremal-graph / Ramsey-flavored problems if any arena problem reduces to bounding independence numbers in forbidden-subhypergraph settings.

## Open questions / connections
- For $r \geq 4$, $l \geq 4$: can the graph bound be beaten? Author's methods fail on the $\{i,i+n,j,j+n\}$ construction with no useful extenders.
- First open case: $R(C_5^4, K_n^4)$, where $O(n^{3/2})$ graph bound is not improved.
- Kostochka–Mubayi–Verstraëte conjecture $R(C_5^r, K_n^r) = O(n^{5/4})$ remains open; this paper closes the gap from $O(n^2)$ to $O(n^{4/3})$ for $r=3$.
- Extends ideas of Sudakov, Li–Zang (odd cycle vs clique in graphs) and Collier-Cartaino–Graber–Jiang (linear Turán).

## Key terms
Ramsey number, loose cycle, hypergraph Ramsey, $C_l^r$, $K_n^r$, independence number, extender, light pair, heavy pair, Spencer's theorem, Pluhár's lemma, Sunflower lemma, Erdős–Rado, Kostochka–Mubayi–Verstraëte, Collier-Cartaino, Sudakov, simple hypergraph, linear cycle, extremal hypergraph
