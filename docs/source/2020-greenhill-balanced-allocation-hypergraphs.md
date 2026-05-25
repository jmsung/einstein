---
type: source
kind: paper
title: Balanced allocation on hypergraphs
authors: Catherine S. Greenhill, B. Mans, Ali Pourmiri
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.07588
source_local: ../raw/2020-greenhill-balanced-allocation-hypergraphs.pdf
topic: general-knowledge
cites:
---

# Balanced allocation on hypergraphs

**Authors:** Catherine S. Greenhill, B. Mans, Ali Pourmiri  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.07588

## One-line
Extends the power-of-$d$-choices paradigm to balls-into-bins where each ball's available choice set is restricted to a (dynamically changing) hyperedge, and quantifies how a "pair visibility" parameter controls the maximum load.

## Key claim
For $s$-uniform dynamic hypergraphs $(H(1),\ldots,H(n))$ that are $\beta$-balanced, $\varepsilon$-visible (every pair of bins co-occurs in at most $sn^{1-\varepsilon}$ rounds), and satisfy a polynomial size property, the $d$-choice balanced allocation achieves maximum load $\log_d \log n + O(1/\varepsilon)$ with very high probability after $m = \Theta(n)$ balls, for any $2 \le d = o(\varepsilon \log n)$.

## Method
Generalized **witness-tree technique** adapted to dynamically changing hypergraphs: if max-load exceeds threshold, recursively construct a $c$-loaded $d$-uniform witness hypergraph in the "conflict graph" $C_m$, then bound its existence via a **blue-red coloring** of an ordered spanning tree (blue = hyperedge sharing exactly one bin with predecessors, red = sharing $\geq 2$). The visibility condition $\varepsilon$ bounds the probability of red edges, while Catalan-number tree enumeration and a uniformity lemma on the allocation process combine to give an exponentially small total probability.

## Result
Upper bound: max load $\le \log_d \log n + O(1/\varepsilon)$ w.v.h.p. (Theorem 5); for $\gamma m \le n$ balls, the bound scales linearly to $\gamma(\log_d \log n + O(1/\varepsilon))$. Companion lower bound (Theorem 7): on some $\varepsilon$-visible balanced hypergraph, max load $\geq \min\{\Omega(1/\varepsilon), \Omega(\log n / \log\log n)\}$, showing visibility is the right parameter. Graph case (Theorem 9): for regular dynamic graphs with $\varepsilon$-visibility, max load is $\log_2 \log n + O(1/\varepsilon)$. Examples: dynamic cycle (degree 2, $\mathrm{vis}=\sqrt n$) achieves $\log_2 \log n + O(1)$; dynamic modular hypergraph $\mathrm{vis} = O(n^{3/4})$; geometric mobile-network communication graphs have $\mathrm{vis} = O(n^{1-\varepsilon})$.

## Why it matters here
General background; no direct arena tie. Power-of-$d$-choices and witness-tree techniques are tangential to the current 23 arena problems (sphere packing, autocorrelation, kissing numbers, etc.); could conceivably inform load-balancing heuristics for parallel multistart optimizer schedulers, but that is a meta-engineering connection, not a math-wisdom one.

## Open questions / connections
- Can the size assumption $|E_t| \ge n^{c_0}$ be relaxed using extra structural information about sparse $H(t)$?
- Can $s$ be allowed to grow with $d$ rather than being fixed independent of $d$?
- Extension of Bansal–Feldheim (2022) graphical allocation gap $O(d/k)\log^4 n \log\log n$ to the hypergraph / visibility regime.
- Tighter integration with Los–Sauerwald–Sylvester (2022) general framework (caching/packing/twinning/thinning).

## Key terms
balanced allocation, balls-into-bins, power of d choices, witness tree technique, hypergraph, pair visibility, conflict graph, blue-red coloring, dynamic graph, Kenthapadi-Panigrahy, Godfrey hypergraph model, maximum load, ordered tree Catalan, load balancing
