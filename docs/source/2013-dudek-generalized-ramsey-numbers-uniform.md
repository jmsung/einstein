---
type: source
kind: paper
title: On Generalized Ramsey Numbers for 3‐Uniform Hypergraphs
authors: A. Dudek, D. Mubayi
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.4518
source_local: ../raw/2013-dudek-generalized-ramsey-numbers-uniform.pdf
topic: general-knowledge
cites:
---

# On Generalized Ramsey Numbers for 3‐Uniform Hypergraphs

**Authors:** A. Dudek, D. Mubayi  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.4518

## One-line
Bounds the Erdős–Rogers function $f^{(3)}_{s,s+1}(n)$ for 3-uniform hypergraphs: the largest guaranteed $K^{(3)}_s$-free subset inside any $K^{(3)}_{s+1}$-free 3-graph on $n$ vertices.

## Key claim
For all $s \ge 3$, there exist constants $c_1, c_2 = c(s)$ with
$$c_1 (\log n)^{1/4} \left(\tfrac{\log\log n}{\log\log\log n}\right)^{1/2} < f^{(3)}_{s,s+1}(n) < c_2 \log n.$$
More generally, Theorem 1.1: $f^{(2)}_{s-1,t-1}(\lfloor\sqrt{\log n}\rfloor) \le f^{(3)}_{s,t}(n) \le C \log n$.

## Method
**Upper bound:** random construction. Color all $(k-1)$-tuples uniformly from $[s-k+2]$; include a $k$-edge $\{u_1<\dots<u_k\}$ iff $\chi(e\setminus u_k)=\chi(e\setminus u_{k-1})$. Pigeonhole forbids $K^{(k)}_{s+1}$; union bound over Rödl-packing-independent $s$-subsets ($c(k-1,s,W)=\Theta(|W|^{k-1})$) shows every set of size $\Omega((\log n)^{1/(k-2)})$ contains $K^{(k)}_s$. **Lower bound:** Erdős–Rado-style greedy halving: extract a sequence $v_1,\dots,v_{m+1}$ of size $m \approx \sqrt{\log n}$ where each pair's triples-to-the-right are monochromatic in $\{E, E^c\}$; project to a $K_{t-1}$-free auxiliary graph and apply the graph-level Erdős–Rogers bound.

## Result
Concrete numerical gap: lower bound $(\log n)^{1/4+o(1)}$ vs upper bound $(\log n)^1$ — a power gap of 4. For general $k$-uniform: $c_1(\underbrace{\log\log\cdots\log}_{k-2} n)^{1/4} \le f^{(k)}_{s,s+1}(n) \le c_2(\log n)^{1/(k-2)}$ (eq. 5); subsequently improved to $1/3-o(1)$ exponent by Conlon–Fox–Sudakov.

## Why it matters here
General background; no direct arena tie. Closest relevance is to extremal-graph / Ramsey-style problems in the inventory — provides a template for "random coloring with pigeonhole-forced clique-freeness + Rödl packing for independence" constructions, and the Erdős–Rado halving trick for lifting $k$-graph bounds from $(k-1)$-graph bounds.

## Open questions / connections
- Can the upper bound $(\log n)^{1/(k-2)}$ be lowered to match the iterated-log lower bound? Stepping-up lemma of Erdős–Hajnal is the natural tool but its application is unclear.
- Lower bound subsequently improved by Conlon–Fox–Sudakov (2013) to $(\log\log\cdots\log n)^{1/3-o(1)}$; gap with upper bound remains huge.
- Extends Erdős–Rogers 1962 (graphs, $k=2$) and Dudek–Rödl, Sudakov, Wolfovitz lines of work to hypergraphs.

## Key terms
Erdős–Rogers function, generalized Ramsey number, 3-uniform hypergraph, $K_s$-free subgraph, Erdős–Rado tree argument, Rödl packing, Shearer independence bound, stepping-up lemma, random coloring construction, pigeonhole clique-freeness, hypergraph Ramsey, Dudek–Mubayi
