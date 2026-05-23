---
type: source
kind: paper
title: The History of Degenerate (Bipartite) Extremal Graph Problems
authors: Z. Furedi, M. Simonovits
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1306.5167
source_local: ../raw/2013-furedi-history-degenerate-bipartite-extremal.pdf
topic: general-knowledge
cites:
---

# The History of Degenerate (Bipartite) Extremal Graph Problems

**Authors:** Z. Furedi, M. Simonovits  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1306.5167

## One-line
Comprehensive survey of Turán-type extremal problems for graphs excluding bipartite subgraphs, where the extremal edge count is $o(n^2)$ ("degenerate" regime).

## Key claim
The degenerate Turán problem — maximizing $e(G_n)$ subject to forbidding a bipartite $L$ — is governed by the Kővári–Sós–Turán bound $\mathrm{ex}(n, K_{a,b}) \le \tfrac{1}{2}(b-1)^{1/a} n^{2-1/a} + O(n)$, matched up to constants by algebraic constructions (Kollár–Rónyai–Szabó norm graphs for $b > (a-1)!$, finite-geometry constructions for $C_4$), and the Erdős–Simonovits rational-exponents conjecture predicts $\mathrm{ex}(n,\mathcal{L})/n^{1+\alpha} \to c$ for some rational $\alpha \in [0,1)$ whenever some $L \in \mathcal{L}$ is bipartite.

## Method
Survey synthesizing: (i) double counting / Jensen / Kővári–Sós–Turán-style convexity for upper bounds; (ii) finite-geometry incidence constructions (projective planes, generalized polygons) and their commutative-algebra generalizations (Lazebnik–Ustimenko, Wenger, Benson) for lower bounds; (iii) random-graph constructions; (iv) dependent random choice for more delicate cases; (v) Erdős–Simonovits stability/product reductions linking non-degenerate to degenerate problems. Eigenvalue bounds ($\lambda(G_n) \ge 2e(G_n)/n$) provide sharper variants.

## Result
For $K_{a,b}$: $\mathrm{ex}(n,K_{a,b}) = \Theta(n^{2-1/a})$ when $b > (a-1)!$. For even cycles: $\mathrm{ex}(n, C_{2k}) \le 100k\, n^{1+1/k}$ (Bondy–Simonovits), with matching constructions only for $C_4, C_6, C_{10}$ (Benson, Wenger). Exact: $\mathrm{ex}(n,C_4) = \tfrac{1}{2}q(q+1)^2$ at $n = q^2+q+1$ for prime-power $q$ (Füredi). Cube: $\mathrm{ex}(n, Q_8) = O(n^{8/5})$. The Erdős–Simonovits reduction shows non-degenerate extremal graphs decompose as products $G_1 \otimes \cdots \otimes G_p$ where each $G_i$ is extremal for a degenerate problem. Ruzsa–Szemerédi $(6,3)$-theorem: 3-uniform hypergraph with no 6 vertices spanning 3 edges has $o(n^2)$ edges.

## Why it matters here
General background for extremal combinatorics and incidence-counting bounds; the Kővári–Sós–Turán bound is the standard tool behind unit-distance and incidence problems in discrete geometry (Section 13), which connects to packing / kissing / autocorrelation problems via the same algebraic-construction lineage (finite geometries, Ramanujan graphs, norm graphs). Most relevant to any arena problem requiring sharp bounds on bipartite-incidence structures or where extremal configurations come from projective-plane / generalized-polygon constructions.

## Open questions / connections
- Erdős–Simonovits rational-exponents conjecture: is $\mathrm{ex}(n,\mathcal{L}) \sim c\, n^{1+\alpha}$ with $\alpha \in \mathbb{Q}$ for every finite bipartite family?
- Exact value of Zarankiewicz $Z(m,n,2,2)$ in the asymmetric / non-square case.
- Erdős conjecture: $\mathrm{ex}(n,\{C_3,C_4\}) = \tfrac{1}{2\sqrt{2}} n^{3/2} + o(n^{3/2})$.
- Sidorenko's conjecture on supersaturation densities for bipartite $H$ (partially proven by Conlon–Fox–Sudakov for graph-norm classes).
- Erdős–Simonovits product conjecture reducing non-degenerate extremal structure to degenerate building blocks.

## Key terms
Turán-type extremal problem, Kővári–Sós–Turán bound, Zarankiewicz problem, complete bipartite $K_{a,b}$, even cycle $C_{2k}$, Erdős–Simonovits stability, rational exponents conjecture, norm graphs Kollár–Rónyai–Szabó, finite-geometry construction, Ramanujan graphs Lubotzky–Phillips–Sarnak, Lazebnik–Ustimenko, dependent random choice, Sidorenko conjecture, Ruzsa–Szemerédi (6,3)-theorem, cube $Q_8$ extremal, supersaturated graphs
