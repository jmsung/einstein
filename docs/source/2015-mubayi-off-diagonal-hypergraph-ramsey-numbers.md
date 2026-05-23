---
type: source
kind: paper
title: Off-diagonal hypergraph Ramsey numbers
authors: D. Mubayi, Andrew Suk
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1505.05767
source_local: ../raw/2015-mubayi-off-diagonal-hypergraph-ramsey-numbers.pdf
topic: general-knowledge
cites:
---

# Off-diagonal hypergraph Ramsey numbers

**Authors:** D. Mubayi, Andrew Suk  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1505.05767

## One-line
Determines the correct tower growth rate of off-diagonal hypergraph Ramsey numbers $r_k(s,n)$ for all $s \geq k+3$, nearly settling a 1972 conjecture of Erdős–Hajnal.

## Key claim
For $k \geq 4$ and $n > 3k$, $r_k(k+3,n) \geq \mathrm{twr}_{k-1}(cn)$, $r_k(k+2,n) \geq \mathrm{twr}_{k-1}(c\log^2 n)$, and $r_k(k+1,n) \geq \mathrm{twr}_{k-2}(cn^2)$ for some absolute $c>0$; moreover $r_k(P_{k+1},n)$ has the same tower growth rate as the diagonal $r_k(n,n)$, so Conjecture 1.1 $\iff$ Conjecture 1.7.

## Method
Two novel ingredients: (i) reduce $r_k(P_{s_1},\dots,P_{s_t},n)$ (tight-path vs. clique) sandwiched between $(k{-}1)$-uniform multicolor diagonal Ramsey numbers via a length-tracking coloring $\varphi(v_1,\dots,v_{k-1})=(a_1,\dots,a_t)$ of longest tight-paths in each color; (ii) use $(k{-}1)$-uniform multicolor diagonal lower bounds to drive $k$-uniform two-color off-diagonal lower bounds — reversing the usual stepping-up paradigm where colors stay constant. Probabilistic arguments with partial Steiner $(n,k,2)$-systems handle the small cases ($r_3(P_4,n) > 2^{\Omega(n)}$).

## Result
Main inequality (Theorem 1.4): for $q = \prod(s_i-k+1)$, $r_{k-1}(\lfloor n/q\rfloor;q) \leq r_k(P_{s_1},\dots,P_{s_t},n) \leq r_{k-1}(n;q)$. Corollary 1.5 improves the upper bound to $r_k(P_s,n) \leq \mathrm{twr}_{k-1}(O(sn\log s))$. Side result: $f_2(n;2) \leq (2+\sqrt{2})^n \approx (3.414)^n$, yielding $r_3(P_4,n) \leq (3.414)^n$. Also $r(B^{(k)},K_n^{(k)}) \leq (n!)^{k-1}$ with matching $2^{\Omega(n)}$ lower bound for the $k$-half-graph.

## Why it matters here
General background; no direct arena tie — extremal combinatorics / Ramsey theory is adjacent to the discrete-geometry and extremal-graph arena problems but this paper does not give optimization-ready bounds for any specific Einstein Arena problem.

## Open questions / connections
- Conjecture 1.7 (new): $r_k(P_{k+1},n) \geq \mathrm{twr}_{k-1}(\Omega(n))$ — equivalent to the $500-Erdős–Hajnal–Rado diagonal conjecture.
- Gap remains between $\mathrm{twr}_{k-1}(c\log^2 n)$ and conjectured $\mathrm{twr}_{k-1}(\Omega(n))$ for $r_k(k+2,n)$, and between $\mathrm{twr}_{k-2}$ and $\mathrm{twr}_{k-1}$ for $r_k(k+1,n)$.
- Constructions may transfer to partition relations for ordinals (infinite Ramsey theory) — not explored.

## Key terms
hypergraph Ramsey number, off-diagonal Ramsey, tight path, stepping-up lemma, Erdős-Hajnal conjecture, Erdős-Hajnal-Rado, tower function, multicolor Ramsey, Erdős-Szekeres, partial Steiner system, half-graph, Spencer independent set lemma, Mubayi, Suk, Conlon-Fox-Sudakov
