---
type: source
kind: paper
title: The multipartite Ramsey number for the 3-path of length three
authors: T. Luczak, J. Polcyn
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1706.08937
source_local: ../raw/2017-luczak-multipartite-ramsey-number-3-path.pdf
topic: general-knowledge
cites:
---

# The multipartite Ramsey number for the 3-path of length three

**Authors:** T. Luczak, J. Polcyn  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1706.08937

## One-line
Improves the multicolor Ramsey upper bound for the loose 3-uniform path $P_3^3$ of length three from roughly $2n$ to $\lambda_0 n + 7\sqrt{n}$ with $\lambda_0 \approx 1.97466$.

## Key claim
$R(P_3^3; n) \le \lambda_0 n + 7\sqrt{n}$, where $\lambda_0 = 1.97466\ldots$ is the root in $(1.9, 2)$ of $f(\gamma) = (\gamma^3 - 3\gamma^2 + 6\gamma - 6)^2 - 72\gamma(2-\gamma)(\gamma-1)^2 = 0$. The conjectured truth is $R(P_3^3; n) = n + 6$.

## Method
Uses a structural decomposition lemma (from companion paper arXiv:1706.08465) splitting any $P_3^3$-free 3-graph $H$ into three parts $H_R, H_T, H_S$ — a residual piece, a quasi-bipartite piece (edge density $\le |V_T|^2/8$), and a disjoint union of stars. For each color class apply the decomposition, define an auxiliary forest-of-stars graph $G_i$ on pairs lying in $\ge 2$ hyperedges, classify edges as private/public, and bound the total weight $w(G_i) = e_i + e'_i/2$. A pigeonhole + double-counting argument over "rich" colors yields the polynomial inequality $f(\gamma) < 0$, forcing $\gamma < \lambda_0$.

## Result
Concrete bound $R(P_3^3; n) \le 1.97466 n + 7\sqrt{n}$ for all $n \ge 41$, improving the authors' earlier $2n + \sqrt{18n+1} + 2$ (arXiv:1701, EJC 2017) and the trivial $3n$. The fraction $\beta = (\gamma^3 - 3\gamma^2 + 6\gamma - 6)/(6(\gamma-1))$ lower-bounds the density of "rich" colors (those with $|H_i| \ge \binom{n+6\sqrt{n}-1}{2} + \binom{N-n-6\sqrt{n}}{2}$). Still a factor $\sim 2$ above the conjectured $n+6$.

## Why it matters here
General background for extremal/Ramsey-type hypergraph problems; no direct Einstein Arena problem ties to a loose-path Ramsey number, but the **decomposition + rich-color pigeonhole technique** is a transferable extremal-combinatorics tool for any arena problem requiring upper bounds on the size of a hypergraph avoiding a fixed substructure (relevant template for sphere-packing-as-hypergraph and discrete-geometry packing bounds).

## Open questions / connections
- Conjecture $R(P_3^3; n) = n + 6$ remains open; verified only $n \le 10$. Closing the $\sim 0.97n$ gap requires a fundamentally different argument (the forest-of-stars bound is tight at $\lambda_0$).
- Method depends critically on the rescaling decomposition of Luczak–Polcyn arXiv:1706.08465 — that paper is the load-bearing reference.
- Analogous 2-graph result is $2n + O(1)$ (Irving 1974); hypergraph version's true constant is unknown but believed to be 1.

## Key terms
Ramsey number, 3-uniform hypergraph, loose path $P_3^3$, multicolor Ramsey, quasi-bipartite hypergraph, hypergraph Turán number, forest of stars decomposition, rich color, pigeonhole double-counting, extremal hypergraph theory, Luczak, Polcyn
