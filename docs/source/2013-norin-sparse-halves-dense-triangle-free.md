---
type: source
kind: paper
title: Sparse halves in dense triangle-free graphs
authors: S. Norin, Liana Yepremyan
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1311.5818
source_local: ../raw/2013-norin-sparse-halves-dense-triangle-free.pdf
topic: general-knowledge
cites:
---

# Sparse halves in dense triangle-free graphs

**Authors:** S. Norin, Liana Yepremyan  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1311.5818

## One-line
Advances Erdős's $\beta(1/2,2)=1/50$ conjecture by proving every triangle-free graph contains an $n/2$-vertex set spanning $\le n^2/50$ edges under weaker degree hypotheses and near the known extremal blowups.

## Key claim
Erdős's sparse-half conjecture holds: (1) for triangle-free graphs with minimum degree $\ge 5n/14$ (improving Krivelevich's $2n/5$); (2) for some absolute $\gamma>0$, for graphs with $\ge (1/5-\gamma)n^2$ edges (improving Keevash–Sudakov's average-degree $2n/5$); (3) for all triangle-free graphs in an edit-distance neighborhood of the Petersen graph (and of $C_5$).

## Method
Reduce to weighted graphs via a homomorphism-lifting lemma, then exploit Chen–Jin–Koh's structural theorem that triangle-free graphs with $\delta(G)\ge 5n/14$ admit a homomorphism into the Woodall graph $F_d$ for $d\le 5$; case analysis on $F_d$ constructs explicit sparse-half distributions and uses Jensen's inequality. For the edit-distance results, introduce "$\varepsilon$-disturbed subgraph", "$c$-uniform sparse half" (distribution over halves with $E[s(e)]\ge c\,\omega(e)$), and "$c$-maximal triangle-free" — show a $c$-uniform sparse half on a graph $H^*$ lifts to a sparse half on any close $G$. Combine with a Keevash–Sudakov-style second-moment argument on degree sequences for the average-degree case.

## Result
Theorem 1.1: $\delta(G)\ge 5n/14 \Rightarrow$ sparse half exists. Theorem 1.2: $\exists \gamma>0$ such that $e(G)\ge (1/5-\gamma)n^2 \Rightarrow$ sparse half. Theorem 6.3: graphs $\delta$-close to Petersen in edit distance have sparse halves. Tightness witnessed by uniform blowups of $C_5$ and Petersen (both attain $n^2/50$ exactly).

## Why it matters here
General background; no direct arena tie — sparse-half / Erdős-conjecture style extremal combinatorics is not among the 23 Einstein Arena problems. Useful as methodology: the homomorphism-to-$F_d$ + weighted-graph reduction and the "uniform sparse half = distribution over halves" trick parallel LP-duality / parametrization-selection patterns used in arena problems (extremal_graph, combinatorics categories).

## Open questions / connections
- Full Erdős conjecture $\beta(1/2,2)=1/50$ remains open — only known extremal examples are blowups of $C_5$ and Petersen; are there others?
- General $\beta(\alpha,r)$ for $\alpha\ne 1/2$ or $r\ge 3$ (Erdős–Faudree–Rousseau–Schelp framework).
- Local-version program (Lovász, Razborov) — can edit-distance-local proofs be combined to cover the full conjecture, or is there a triangle-free graph far from both known extremal blowups violating the bound?

## Key terms
sparse half, Erdős conjecture, triangle-free graph, edit distance, Petersen graph blowup, $C_5$ blowup, Andrásfai–Erdős–Sós, Chen–Jin–Koh, Woodall graph $F_d$, homomorphism lifting, weighted graph, extremal graph theory, Keevash–Sudakov, Krivelevich
