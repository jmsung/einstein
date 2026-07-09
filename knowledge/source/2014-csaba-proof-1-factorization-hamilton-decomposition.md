---
type: source
kind: paper
title: Proof of the 1-factorization and Hamilton Decomposition Conjectures
authors: Béla Csaba, D. Kuhn, A. Lo, Deryk Osthus, Andrew Treglown
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.4183
source_local: ../raw/2014-csaba-proof-1-factorization-hamilton-decomposition.pdf
topic: general-knowledge
cites:
---

# Proof of the 1-factorization and Hamilton Decomposition Conjectures

**Authors:** Béla Csaba, D. Kuhn, A. Lo, Deryk Osthus, Andrew Treglown  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.4183

## One-line
Paper IV of a four-part series proving the 1-factorization and Hamilton decomposition conjectures for all sufficiently large $n$; this installment handles the "two cliques" extremal case via decomposition into exceptional path systems.

## Key claim
For large $n$: (i) every $D$-regular graph on even $n$ with $D \geq 2\lceil n/4 \rceil - 1$ has a 1-factorization (so $\chi'(G) = D$); (ii) every $D$-regular graph with $D \geq \lfloor n/2 \rfloor$ decomposes into Hamilton cycles plus at most one perfect matching. Both bounds are tight. This paper supplies the exceptional-system decomposition lemmas for the case where $G$ is $\varepsilon$-close to $K_{n/2} \sqcup K_{n/2}$.

## Method
The argument splits $V(G)$ into clusters $A_1,\dots,A_K, B_1,\dots,B_K$ plus small exceptional sets $A_0, B_0$, then decomposes the "exceptional edges" (those incident to $A_0 \cup B_0$ or crossing $A' = A \cup A_0$ to $B' = B \cup B_0$) into localized "exceptional (path) systems" that later extend to Hamilton cycles or perfect matchings. Three regimes are handled separately: non-critical with $e(A',B') \geq D$, critical with $e(A',B') \geq D$ (where a few high-degree vertices $W$ absorb most cross-edges), and $e(A',B') < D$. The "robust decomposition lemma" of Kühn-Osthus [8] then absorbs the leftover after an approximate Hamilton decomposition.

## Result
Lemmas 4.2, 4.10, 4.14 give decompositions of $G^\diamond := G - G[A] - G[B] - G_0$ into $(D - \phi n)/2$ edge-disjoint exceptional systems, with all but $\lambda n$ of them localized to a single $(A_i, B_{i'})$ cluster pair. In the critical case the high-degree set $W$ has $|W| \leq 3$ and must be $D = (n-1)/2, n \equiv 1 \pmod 4$ or $D = n/2-1, n \equiv 0 \pmod 4$. Combined with companion papers I-III, this proves the optimal $D \geq 2\lceil n/4 \rceil - 1$ threshold conjectured by Dirac (1950s) and Nash-Williams (1970).

## Why it matters here
General background; no direct arena tie. Extremal graph decomposition and the "absorber + approximate decomposition + robust completion" template could inform combinatorics problems involving graph decompositions or matching/covering structures, but none of the 23 current arena problems map directly.

## Open questions / connections
- Extends Kühn-Osthus [8] on Hamilton decompositions of robust expanders to non-expander regimes via case analysis on near-extremal structure.
- Settles Nash-Williams 1970 questions on Hamilton decomposition and edge-disjoint Hamilton cycles at minimum degree.
- The "absorbing" methodology (robustly decomposable graph $G^{\text{rob}}$ + approximate decomposition + completion) is the key transferable technique.

## Key terms
1-factorization, Hamilton decomposition, edge chromatic number, perfect matching, regular graph, robust expander, exceptional system, absorbing method, Nash-Williams conjecture, Chetwynd-Hilton, Kühn-Osthus, extremal graph theory
