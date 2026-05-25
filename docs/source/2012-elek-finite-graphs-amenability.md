---
type: source
kind: paper
title: Finite graphs and amenability
authors: G. Elek
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1204.0449
source_local: ../raw/2012-elek-finite-graphs-amenability.pdf
topic: general-knowledge
cites:
---

# Finite graphs and amenability

**Authors:** G. Elek  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1204.0449

## One-line
A unified deterministic framework for hyperfiniteness (amenability) of bounded-degree graphs and graphings, recovering and extending theorems of Schramm, Lovász, Newman–Sohler, and Ornstein–Weiss.

## Key claim
Hyperfiniteness is a local (Benjamini–Schramm) property: a convergent bounded-degree graph sequence $\{G_n\}$ is hyperfinite iff its limit graphing $\mathcal{G}$ is hyperfinite (Thm 1); equivalently, weakly equivalent graphings share hyperfiniteness (Thm 2), and weakly equivalent hyperfinite graphings are strongly equivalent (Thm 3).

## Method
Introduces the "Oracle Method": Bernoulli-randomize vertex colors to break symmetries, then encode subgraphings of the canonical limit $\mathcal{G}_{\hat{G}}$ via finite color patterns on $r$-balls, allowing transfer between finite graphs and graphings. Combined with a revisited Kaimanovich theorem (hyperfinite ⟺ all sub-graphings have a.e. zero isoperimetric constant) and a Borel proper edge-coloring trick of Kechris–Solecki–Todorcevic to realize colorless graphings as factors of $\Gamma$-actions, where $\Gamma$ is a free product of $\binom{d+1}{2}$ order-2 cyclic groups.

## Result
Establishes: (1) the Transfer Theorem — every subgraphing of the canonical limit lifts to subgraphs of the approximating sequence; (2) the Uniformicity Theorem — a hyperfinite family $\mathcal{P}$ admits a single $K(\epsilon)$ working for the whole limit class $L_\mathcal{P}$; (3) the Equipartition Theorem — statistically close graphs in $\mathcal{P}$ admit matching partitions (component-count differences $<\delta$, edge removals $<2\epsilon|E|$); (4) Newman–Sohler testability for hyperfinite families (Thm 5: $dstat<f(\delta)\Rightarrow$ $\delta$-edit-close); (5) local-global ≡ Benjamini–Schramm convergence on hyperfinite sequences (Thm 8); (6) a non-free Rokhlin lemma for amenable $F_n$-actions with equal type (IRS) (Thm 9).

## Why it matters here
General background; no direct arena tie. Hyperfiniteness / property testing on bounded-degree graphs is adjacent to the agent's extremal-graph and discrete-geometry problems, but the techniques (graphings, IRS, Bernoulli marker graphs) are functional-analytic and don't directly produce optimizer signals for any of the 23 problems.

## Open questions / connections
- Aldous–Lyons conjecture (every unimodular measure is a graph-sequence limit) is left open and is the bottleneck for converting these graphing-side theorems into purely combinatorial statements.
- Gives an alternative to Ornstein–Weiss quasi-tiling for amenable group actions — a possible cleaner route if any arena problem reduces to Følner averaging.
- Quantitative dependence $K(\epsilon)$ in the Uniformicity / Equipartition theorems is left implicit; effective bounds would matter for any testing-based optimizer.

## Key terms
hyperfiniteness, amenability, graphing, Benjamini-Schramm convergence, unimodular measure, invariant random subgroup, Kaimanovich theorem, isoperimetric constant, Ornstein-Weiss, Schramm, Lovász, Newman-Sohler, property testing, bounded degree graph, equipartition, Rokhlin lemma, Følner sequence, Borel chromatic number
