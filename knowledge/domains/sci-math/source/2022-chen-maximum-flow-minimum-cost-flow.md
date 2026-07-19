---
type: source
kind: paper
title: Maximum Flow and Minimum-Cost Flow in Almost-Linear Time
authors: L. Chen, Rasmus Kyng, Yang P. Liu, Richard Peng, Maximilian Probst Gutenberg, Sushant Sachdeva
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.00671
source_local: ../raw/2022-chen-maximum-flow-minimum-cost-flow.pdf
topic: general-knowledge
cites:
---

# Maximum Flow and Minimum-Cost Flow in Almost-Linear Time

**Authors:** L. Chen, Rasmus Kyng, Yang P. Liu, Richard Peng, Maximilian Probst Gutenberg, Sushant Sachdeva  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.00671

## One-line
First algorithm computing exact max-flow and min-cost flow on directed graphs in $m^{1+o(1)}$ time, essentially optimal up to subpolynomial factors.

## Key claim
On a directed graph with $m$ edges, integral demands/costs/capacities bounded by $U,C$, exact min-cost flow is computable in $m^{1+o(1)} \log U \log C$ time w.h.p. (Theorem 1.1); max-flow in $m^{1+o(1)} \log U$ (Corollary 1.2). Extends to edge-separable convex objectives (entropy-regularized OT, matrix scaling, $p$-norm flows, $p$-norm isotonic regression on DAGs) at high accuracy in $m^{1+o(1)}$ time.

## Method
A new **potential-reduction IPM** (à la Karmarkar, but with a power barrier $x^{-\alpha}$ instead of $\log x$) reduces min-cost flow to $m^{1+o(1)}$ slowly-changing **undirected minimum-ratio cycle** subproblems $\min_{B^\top \Delta = 0} g^\top \Delta / \|L\Delta\|_1$, each solved to $m^{o(1)}$ approximation. The subproblems are solved by a recursive dynamic data structure maintaining a chain of vertex-reduced (low-stretch tree embeddings, $j$-tree style) and edge-reduced (dynamic spanners with explicit path embeddings) graphs, all in $m^{o(1)}$ amortized time per update. A "rebuilding game" handles adaptive (non-oblivious) updates from the IPM.

## Result
Almost-linear-time exact algorithms for: min-cost flow, max-flow, bipartite matching, worker assignment, optimal transport (with entropic regularization), matrix scaling, $p$-norm flows for all $p\in[1,\infty]$, $p$-norm isotonic regression on DAGs, single-source shortest paths and negative-cycle detection with negative weights ($m^{1+o(1)}\log W$), Gomory–Hu trees in unweighted graphs (and $(1+\varepsilon)$-approx in weighted), global vertex connectivity, Steiner min-cut, and directed expander decomposition. Improves prior $m^{3/2-1/58}$, $m^{4/3+o(1)}$, $O(mn)$, $O(m^{1.5})$ bounds by polynomial factors.

## Why it matters here
General background; no direct arena tie. The convex-flow extension (entropy-regularized OT, matrix scaling, $p$-norm minimization on graphs) is the only thread that could touch Einstein Arena work — relevant for any problem expressible as an LP / convex program on a graph structure where current optimizer cost dominates wall-clock (e.g. if an LP relaxation of a packing/combinatorial problem fit this template). Likely *not* a fit for the current 23 problems, which are mostly continuous Euclidean optimization, not network-structured.

## Open questions / connections
- Does any Einstein problem admit a graph/network reformulation where almost-linear flow solvers would dominate HiGHS? Unclear; most arena problems are geometric.
- The IPM's $\ell_1$ subproblem perspective ("potential-reduction tolerates large $m^{o(1)}$ approximation per step") may inform agent's understanding of when crude inner-solver accuracy is acceptable in path-following methods.
- Extends [WZ92] $\ell_1$ min-ratio-cycle IPM; supersedes the robust-IPM line ([CLS19], [BLNPSSSW20], [BGS21], [GLP21]).

## Key terms
maximum flow, minimum-cost flow, interior point method, potential reduction IPM, undirected minimum-ratio cycle, low-stretch spanning tree, dynamic spanner, path embedding, $j$-tree, Laplacian paradigm, entropy-regularized optimal transport, matrix scaling, $p$-norm flow, isotonic regression, Gomory-Hu tree, bipartite matching, negative cycle detection, Karmarkar, $\ell_1$ minimization
