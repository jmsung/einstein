---
type: source
kind: paper
title: "Variable-Version Lovász Local Lemma: Beyond Shearer's Bound"
authors: Kun He, Liangpan Li, Xingwu Liu, Yuyi Wang, Mingji Xia
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1709.05143
source_local: ../raw/2017-he-variable-version-lov-local-lemma.pdf
topic: general-knowledge
cites:
---

# Variable-Version Lovász Local Lemma: Beyond Shearer's Bound

**Authors:** Kun He, Liangpan Li, Xingwu Liu, Yuyi Wang, Mingji Xia  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1709.05143

## One-line
Gives the first tight necessary-and-sufficient criterion for the variable-version Lovász Local Lemma (variable-LLL), showing when and how it can beat Shearer's classical bound by exploiting the event-variable bipartite structure.

## Key claim
For any bigraph $H=([n],[m],E)$, a probability vector $\lambda q$ lies on the variable-LLL boundary $B(H)$ iff $\lambda$ solves an explicit discrete optimization program over $d_j$-valued variables (where $d_j$ is the right-degree). Using this, the authors fully determine the boundary for cyclic and treelike bigraphs, and prove that a graph $G$ is *strongly a-gapful* (every bigraph with base $G$ is gapful) iff $G$ is chordal, and *a-gapless* iff $G$ is a tree — closing a 6-year open problem of Kolipaka–Szegedy.

## Method
Recasts variable-LLL geometrically (GLLL): events become cylinders in $[0,1]^m$ with Lebesgue measure replacing probability. The core technical move is a four-step discretization argument showing that boundary-witnessing cylinder sets can be taken $d$-discrete (each axis $j$ partitioned into $d_j$ intervals), reducing an infinite-dimensional problem to a finite combinatorial program. Reduction rules (Delete-Event, Duplicate-Variable, etc.) propagate gapful/gapless status between bigraphs; chordal-graph induction proves the strong characterization.

## Result
- Theorem 3: discrete program characterizes $B(H)$ exactly.
- Theorem 4: $n$-cyclic bigraph boundary computable via an $(n-1)$-degree polynomial system $b_1=\lambda p_i,\ b_k=\lambda p_{i-1+k}\cdot b_{k-1}^{1-k},\ b_{n-1}=1-\lambda p_{i-1}$.
- Theorems 6–9: treelike bigraphs gapless; cyclic bigraphs gapful; a-gapless ⇔ tree; strongly a-gapful ⇔ chordal.
- Theorems 47–48: deciding the variable-LLL boundary (MUP, INT) is #P-hard, via reduction from Rtw-Opp-#3SAT.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the discretization-to-finite-program trick mirrors LP/SDP relaxation patterns the agent already uses, and the chordal/tree characterization is a clean structural-vs-numerical-bound dichotomy worth knowing when probabilistic existence arguments are invoked for combinatorial problems (e.g., extremal-graph or hypergraph-coloring framings).

## Open questions / connections
- Does Moser–Tardos resampling converge efficiently beyond Shearer's bound, up to the variable-LLL tight bound? (Left explicitly open.)
- Tight algorithmic conditions for constructive variable-LLL — Harris's lopsided extension uses strictly more info than the event-variable graph.
- Partial-only resolution when the base graph has only 3-cliques (gap question still open there).
- Connections to partition-function zeros / hard-core lattice gas (Scott–Sokal, Bissacot et al. cluster expansion).

## Key terms
Lovász local lemma, Shearer's bound, variable-LLL, event-variable bigraph, dependency graph, chordal graph, independent-set polynomial, Moser–Tardos algorithm, cluster expansion, lopsidependency, #P-hardness, cylinder discretization
