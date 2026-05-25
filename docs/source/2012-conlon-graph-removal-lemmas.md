---
type: source
kind: paper
title: Graph removal lemmas
authors: D. Conlon, J. Fox
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1211.3487
source_local: ../raw/2012-conlon-graph-removal-lemmas.pdf
topic: general-knowledge
cites:
---

# Graph removal lemmas

**Authors:** D. Conlon, J. Fox  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1211.3487

## One-line
A survey of the graph removal lemma and its variants, focusing on recent quantitative improvements that escape tower-type bounds inherent in regularity-based proofs.

## Key claim
The graph removal lemma (Theorem 1.1) states: for any graph $H$ and $\epsilon>0$, $\exists\delta>0$ such that any $n$-vertex graph with at most $\delta n^{v(H)}$ copies of $H$ can be made $H$-free by removing at most $\epsilon n^2$ edges. Fox's improvement gives $\delta^{-1} = T(a_H \log\epsilon^{-1})$ (tower in $\log\epsilon^{-1}$), vs the regularity-based $T(\epsilon^{-c_H})$; Conlon–Fox improve induced removal from wowzer to $T(a_H \epsilon^{-c})$.

## Method
Standard proof uses Szemerédi's regularity lemma plus a counting lemma; iterating a density-increment via convex $q(x)=x^2$ on irregular pairs forces tower-type partition sizes. Fox's improved proof bypasses full regularity by exploiting the structural consequences of "few copies of $H$" — closer to the weak (Frieze–Kannan) regularity lemma. Lower bounds on $\delta^{-1}$ come from Behrend's AP-free construction transferred via Ruzsa–Szemerédi: $\delta^{-1} \geq \epsilon^{-c\log\epsilon^{-1}}$.

## Result
Upper bound: $\delta^{-1} \leq T(a_H \log\epsilon^{-1})$ for graph removal; $\delta^{-1} \leq T(a_H \epsilon^{-c})$ for induced removal (tower vs prior wowzer). Lower bound for triangle removal: quasi-polynomial $\delta^{-1} \geq \epsilon^{-c\log\epsilon^{-1}}$ via Behrend. Hypergraph removal (Theorem 1.2) holds via Gowers / Nagle–Rödl–Schacht–Skokan hypergraph regularity but with Ackermann-type bounds; for linear hypergraphs, tower bounds suffice.

## Why it matters here
General background; no direct arena tie. Relevant to extremal-graph and combinatorics problems via the regularity/removal toolkit, and to property-testing framings, but the Einstein Arena problems are mostly geometric/analytic optimization rather than dense extremal graph theory.

## Open questions / connections
- Can the triangle-removal upper bound be pushed to match Behrend's quasi-polynomial lower bound $\epsilon^{-c\log\epsilon^{-1}}$?
- Primitive-recursive (or tower-type) bounds for hypergraph removal — would yield first such bound for multidimensional Szemerédi.
- Characterize easily-testable hereditary properties (open for induced $C_4$); Erdős–Rothschild $h(n,c)$ true growth rate between $e^{a\log^* n}$ and $n^{1/\log\log n}$.

## Key terms
graph removal lemma, triangle removal lemma, Szemerédi regularity lemma, hypergraph removal, induced removal lemma, Ruzsa–Szemerédi, Behrend construction, Roth's theorem, property testing, Frieze–Kannan weak regularity, tower function, wowzer function, induced matchings, pseudorandom graphs, Cayley graph jumbledness
