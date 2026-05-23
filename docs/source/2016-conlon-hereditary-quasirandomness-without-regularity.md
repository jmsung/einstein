---
type: source
kind: paper
title: Hereditary quasirandomness without regularity
authors: D. Conlon, J. Fox, B. Sudakov
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.02099
source_local: ../raw/2016-conlon-hereditary-quasirandomness-without-regularity.pdf
topic: general-knowledge
cites:
---

# Hereditary quasirandomness without regularity

**Authors:** D. Conlon, J. Fox, B. Sudakov  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.02099

## One-line
A regularity-lemma-free proof of the Simonovits–Sós hereditary quasirandomness theorem, giving polynomial (linear for cliques) rather than tower-type dependence between the local-count parameter $\delta$ and the quasirandomness parameter $\epsilon$.

## Key claim
If an $n$-vertex graph $G$ satisfies $P^*_{H,p}(\delta)$ — every subset $S$ contains $p^{e(H)}|S|^{v(H)} \pm \delta n^{v(H)}$ labeled copies of $H$ — then $G$ satisfies $P^*_{2,p}(\epsilon)$ (edges are quasirandomly distributed) with $\delta = c(r)p^{2r^2}\epsilon$ when $H = K_r$ (Thm 1.1, linear, optimal), and $\delta = c'(p,r)\epsilon^{c(p,r)}$ with $c(p,r) = 10r^4 p^{1-m}$ for general $H$ (Thm 1.2, polynomial).

## Method
Clique case (Thm 1.1): a Vandermonde-inversion lemma estimates clique counts in subset pairs $(X,Y)$, a Kruskal–Katona density bound, an Erdős–Goldberg–Pach–Spencer halving lemma, and Azuma–Hoeffding concentration to extract balanced subsets witnessing edge-discrepancy. General case (Thm 1.2): a density-increment argument using a lower-regularity counting lemma (telescoping over edges), iterating Lemma 3.5 which converts any density-deviating pair $(A,B)$ into a pair $(A',B')$ with strictly larger deviation, then closing via an $\epsilon$-regular subset (Conlon–Fox) and counting too-many copies of $H$.

## Result
For cliques $K_r$, $\delta = O(p^{2r^2}\epsilon)$ — linear in $\epsilon$, matching the trivial lower bound from $G(n,p+\epsilon)$. For general $H$ on $r$ vertices, $\delta = \Omega(\epsilon^{10r^4 p^{1-m}})$ — polynomial, vastly better than the tower-of-twos bound of height $\mathrm{poly}(\epsilon^{-1})$ from the original regularity-lemma proof of Simonovits–Sós (1997). Independent contemporaneous work by Reiher–Schacht proves a variant under stronger hypotheses with weaker quantitative control.

## Why it matters here
General background; no direct arena tie. Closest relevance is extremal/quasirandomness machinery (density-increment, counting lemmas, Kruskal–Katona, Azuma–Hoeffding) that could inform discrete-combinatorics or extremal-graph arena problems, but no specific arena problem is currently mapped to hereditary-quasirandomness.

## Open questions / connections
- Conjecture 4.1: for bipartite $H$ of girth $g$, $P_{H,p}(\delta)$ with $\delta = \Omega(\epsilon^g)$ should imply $P^*_{2,p}(\epsilon)$ — a quantitative "second-order" strengthening of the forcing conjecture; tight girth-dependence example given.
- Can Theorem 1.1 extend to all $H$ with linear $\epsilon$-dependence, even just for $H = C_4$? Authors flag this as open.
- Parallels Sidorenko's conjecture program: progress on either should transfer.

## Key terms
quasirandom graphs, hereditary quasirandomness, Simonovits–Sós theorem, Chung–Graham–Wilson, regularity lemma, density increment, counting lemma, Kruskal–Katona, Azuma–Hoeffding, forcing conjecture, Sidorenko's conjecture, lower-regular pair, clique counts, extremal graph theory
