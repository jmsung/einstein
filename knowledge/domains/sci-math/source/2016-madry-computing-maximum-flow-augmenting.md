---
type: source
kind: paper
title: Computing Maximum Flow with Augmenting Electrical Flows
authors: A. Ma̧dry
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.06016
source_local: ../raw/2016-madry-computing-maximum-flow-augmenting.pdf
topic: general-knowledge
cites:
---

# Computing Maximum Flow with Augmenting Electrical Flows

**Authors:** A. Ma̧dry  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.06016

## One-line
A new $\tilde{O}(m^{10/7} U^{1/7})$-time algorithm for max $s$-$t$ flow / min $s$-$t$ cut in directed graphs, built from electrical-flow-driven augmenting paths instead of interior-point methods.

## Key claim
Max $s$-$t$ flow (and min cut) in a directed graph with $m$ arcs and largest integer capacity $U$ can be computed in $\tilde{O}(m^{10/7} U^{1/7})$ time; equivalently, max-cardinality bipartite $b$-matching with largest demand $B$ runs in $\tilde{O}(m^{10/7} B^{1/7})$. This matches Mądry'13 at $U{=}1$, beats his $\tilde{O}(mU)^{10/7}$ for $U>1$, and beats Lee–Sidford's $\tilde{O}(m\sqrt{n}\log U)$ on sparse graphs with moderate $U$.

## Method
Primal–dual augmenting-path framework: each iteration computes an electrical flow on a *symmetrization* of the current residual graph to obtain an augmenting $s$-$t$ flow, and simultaneously updates dual vertex potentials. A carefully maintained "well-coupling" condition between primal flow $f$ and dual $y$ (an interior-point-method-style centrality analog, expressed via residual capacities $u_e^\pm(f)$) plus an $s$-$t$ preconditioning arc set guarantees the symmetrized graph still carries an $\Omega(F)$-fraction of residual capacity. An $\ell_3$-norm congestion bound (24) combined with an electrical-flow perturbation breaks the $\sqrt{m}$ iteration barrier; Laplacian solvers give $\tilde{O}(m)$ per iteration.

## Result
Basic framework yields $\tilde{O}(m^{3/2} \log U)$; with $\ell_p$-geometric refinement and the perturbation technique, $\tilde{O}(m^{10/7} U^{1/7})$. Energy decreases per progress step by at most $1 + O(\|\rho\|_3^3/\|\rho\|_2^2) = 1 + O(m^{-2\eta})$ under the $\ell_3$ congestion condition (Lemma 4.4). Algorithm is conceptually simpler than Mądry'13 / Lee–Sidford — it lives entirely in the classical Ford–Fulkerson augmenting-path setting rather than inside an IPM.

## Why it matters here
General background; no direct arena tie. The augmenting-electrical-flow + primal/dual coupling pattern is a useful analogy for any iterative optimizer that must trade off "size of step" vs "stay near a feasibility manifold," but the Einstein Arena problems (sphere packing, autocorrelation, kissing, extremal graph) are not max-flow / matching instances.

## Open questions / connections
- Can the augmenting-electrical-flow framework be pushed past $m^{10/7}$ toward $m^{4/3}$ or near-linear for directed exact max flow?
- Extends Christiano–Kelner–Mądry–Spielman–Teng (electrical flows + multiplicative weights, undirected approximate) to directed exact setting.
- Relationship to Lee–Sidford IPM ($\tilde{O}(m\sqrt{n}\log U)$): when does simpler combinatorial framing win on sparse graphs vs. dense regime?
- Whether the well-coupling / centrality condition has analogs for other primal–dual combinatorial problems (min-cost flow, submodular flow).

## Key terms
maximum flow, minimum cut, electrical flow, Laplacian solver, augmenting path, residual graph, interior-point method, primal-dual coupling, bipartite matching, $b$-matching, $\ell_3$ norm congestion, Mądry, Ford-Fulkerson, Goldberg-Rao, Lee-Sidford
