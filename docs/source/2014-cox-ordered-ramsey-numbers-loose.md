---
type: source
kind: paper
title: Ordered Ramsey numbers of loose paths and matchings
authors: Christopher Cox, Derrick Stolee
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1411.4058
source_local: ../raw/2014-cox-ordered-ramsey-numbers-loose.pdf
topic: general-knowledge
cites:
---

# Ordered Ramsey numbers of loose paths and matchings

**Authors:** Christopher Cox, Derrick Stolee  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1411.4058

## One-line
Determines the asymptotic growth of ordered Ramsey numbers for loose $(k,\ell)$-uniform paths under the monotone ordering and gives upper bounds for $k$-uniform matchings under "nestable" orderings.

## Key claim
For $k > \ell \geq 1$ with intersection number $i = i(k,\ell)$, $\mathrm{OR}(P_{e_1}^{k,\ell},\dots,P_{e_t}^{k,\ell}) = (k-\ell)\,\mathrm{OR}(P_{e_1}^{i,i-1},\dots,P_{e_t}^{i,i-1}) + \ell - (k-\ell)(i-1)$, so $\mathrm{OR}_t(P_e^{k,\ell})$ grows as a tower of height $i(k,\ell)-1$.

## Method
Two proofs of the path reduction: (i) a poset-theoretic construction $Q_m(e_1,\dots,e_t)$ via iterated down-set lattices $J(\cdot)$, building the extremal $t$-coloring from descent-free lists and a projection/reduction map; (ii) a direct "rational reduction" $r$ mapping $k$-uniform edges in $[N']$ to $i$-uniform edges in $[N]$ via $\lceil x/(k-\ell)\rceil$, transferring colorings between tight-$i$-path and loose-$(k,\ell)$-path avoidance. For matchings, blow-up/concatenation construction of auxiliary graph $G_s^k$ plus induction on $k$-nestability.

## Result
Exact formula $\mathrm{OR}(M_{e_1}^{k,r},\dots,M_{e_t}^{k,r}) = k(1 + \sum_i (e_i-1))$ for nested matchings (Thm 3.2). For $k$-nestable (incl. simply-interlacing) matchings $M$ with $e$ edges, $\mathrm{OR}_t(M) \leq (ek)^{(2e-1)^{t-1}} = 2^{(2e-1)^{t-1}\lg(ek)}$ (Thm 3.6). Corollary 1.2: when $2\ell \leq k$, $\mathrm{OR}(P_{e_1}^{k,\ell},\dots,P_{e_t}^{k,\ell}) = (k-\ell)\sum_i e_i + \ell$ exactly.

## Why it matters here
General background; no direct arena tie. The Erdős–Szekeres-type tower bounds and Dedekind/antichain connections may inform discrete extremal/combinatorics problems, but no current Einstein Arena problem appears to be a hypergraph Ramsey question.

## Open questions / connections
- Upper bounds on $\mathrm{OR}_t(P_e^{k,\ell})$ for *arbitrary* (non-monotone) orderings remain open for $k \geq 3$; conjecturally much larger than the monotone case when $i(k,\ell)=2$.
- Asymptotic growth of $\mathrm{OR}_t(D_r)$ for the generalized diamond $D_r$ — captures "wider" rather than "longer" graphs; only $\mathrm{OR}_2(D_2)=11$ known (Balko et al.).
- Extends Conlon–Fox–Lee–Sudakov [arXiv:1410.5292] and Moshkovitz–Shapira (Adv. Math. 2014) on tight paths; relates to Dedekind's problem via $|Q_3(2,\dots,2)|$ counting antichains in the boolean lattice $2^{[t]}$.

## Key terms
ordered Ramsey number, loose path, tight path, $k$-uniform hypergraph, nested matching, $k$-nestable, simply-interlacing, Erdős–Szekeres, Dedekind problem, down-set lattice, tower function, monotone ordering, Moshkovitz–Shapira, Conlon–Fox–Lee–Sudakov
