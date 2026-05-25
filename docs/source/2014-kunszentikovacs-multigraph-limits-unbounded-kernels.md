---
type: source
kind: paper
title: Multigraph limits, unbounded kernels, and Banach space decorated graphs
authors: D'avid Kunszenti-Kov'acs, L. Lov'asz, B. Szegedy
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.7846
source_local: ../raw/2014-kunszentikovacs-multigraph-limits-unbounded-kernels.pdf
topic: general-knowledge
cites:
---

# Multigraph limits, unbounded kernels, and Banach space decorated graphs

**Authors:** D'avid Kunszenti-Kov'acs, L. Lov'asz, B. Szegedy  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.7846

## One-line
Develops a graph-limit theory for multigraphs with unbounded edge multiplicities by treating edges as decorated by elements of a Banach space and testing with predual elements.

## Key claim
Every node-and-edge convergent multigraph sequence $(G_n)$ admits a limit object: a $J_\rho$-graphon $W : [0,1]^2 \to J_\rho$ (probability distributions on $\mathbb{N}$ under a weight $\rho$) such that $t(F, G_n) \to t(F', W)$ for every multigraph test $F$, and the space of such graphons is closed under this convergence.

## Method
Edges of "big" graphs decorated by a Banach dual $Z$, test ("small") graphs decorated by the predual $B$, with homomorphism density $t(F,G) = \mathbb{E} \prod_e \langle f(e), g(\varphi(e))\rangle$. Replaces the cut norm with a **jumble norm** $\|u\|_\boxtimes = \sup_{S,T} \frac{1}{\lambda(S)\lambda(T)} |\int_{S\times T} u|$ suited to unbounded kernels, and proves matching Weak Regularity and Counting Lemmas. Multigraphs encoded via polynomial decorations $X^m$ vs. moment-sequence duals; moment-bounded edge-multiplicity families are shown to be $\rho$-smooth for some weight $\rho \in J^+$.

## Result
For node-and-edge convergence, the limit is a sequence $(W_0, W_1, \dots)$ of symmetric measurable functions where each $(W_0(x,y), W_1(x,y), \dots)$ is an $\mathbb{N}$-moment sequence, and $t(F, G_n) \to \int \prod W_{f(ij)}$. Node-and-edge convergence is shown **strictly stronger** than node-homomorphism (compactification) convergence; the gap is exactly Stieltjes/Hamburger moment indeterminacy (Examples 4.8, 4.9, 4.11). $W$-random sampling $G_R(n,W)$ realizes every $J_\rho$-graphon as a limit a.s.

## Why it matters here
General background; no direct arena tie. Possible relevance to extremal/multigraph combinatorics problems where bounded-graphon theory fails and one needs unbounded $L^p$-graphon machinery; complements the Borgs–Chayes–Cohn–Zhao $L^p$ theory.

## Open questions / connections
- Common generalization of jumble-norm Banach-decorated theory and BCCZ $L^p$-graphon theory (different test-graph families: arbitrary multigraphs vs. bounded-degree simple).
- Uniqueness of Banach-space-valued graphons beyond moment-indeterminacy obstructions (handled in Kunszenti-Kovács 2019).
- Extending homomorphism-function characterizations (à la Lovász) to Banach/compact decorated case.
- Sharper density bounds via the generalized Hölder of BCCZ (max-degree exponent $\Delta(F)$).
- Sample-convergence ↔ density-convergence equivalence fails for unbounded edge multiplicities; conditions restoring equivalence are open.

## Key terms
graph limits, graphon, multigraph, unbounded kernels, Banach space decorated graphs, jumble norm, cut norm, Weak Regularity Lemma, Counting Lemma, homomorphism density, moment problem, Stieltjes indeterminacy, $L^p$-graphon, Lovász, exchangeability
