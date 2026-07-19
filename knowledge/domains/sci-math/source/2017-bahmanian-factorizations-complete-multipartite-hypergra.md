---
type: source
kind: paper
title: Factorizations of complete multipartite hypergraphs
authors: M. A. Bahmanian
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.02869
source_local: ../raw/2017-bahmanian-factorizations-complete-multipartite-hypergra.pdf
topic: general-knowledge
cites:
---

# Factorizations of complete multipartite hypergraphs

**Authors:** M. A. Bahmanian  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/2102.02869

## One-line
Proves a Baranyai-type factorization theorem for a non-standard "multipartite" 3-uniform hypergraph $K^3_{m \times n}$ in which edges contain two vertices from one part and one from another.

## Key claim
$\lambda K^3_{m \times n}$ admits an $(r_1, \ldots, r_k)$-factorization whenever (S1) $3 \mid r_i m$, (S2) $2 \mid r_i mn$, and (S3) $\sum_{i=1}^k r_i = 3\lambda(n-1)\binom{m}{2}$ — solving the "mathematicians collaboration" scheduling problem for $\lambda=1$ and $r_1 = \cdots = r_k = r$.

## Method
Hypergraph amalgamation–detachment: start from a small "amalgamated" hypergraph $\lambda m \binom{m}{2} K_n^*$ (where each vertex carries multiplicity $m$), then iteratively detach one vertex at a time, splitting incident hinges using Nash-Williams' laminar-family lemma to preserve degree, multiplicity, and color-balance conditions $(C1)$–$(C4)$. Induction on the number of vertices $\ell$ from $n$ up to $mn$ produces the final factorization, leveraging the $\lambda$-fold factorization of $K_n$ (Bahmanian–Rodger).

## Result
Theorem 1.1 / 3.1 establishes existence of the factorization under the three divisibility/sum conditions; Corollary 1.2 yields $r$-factorability of $\lambda K^3_{m \times n}$ when $3 \mid rm$, $2 \mid rnm$, $r \mid 3\lambda(n-1)\binom{m}{2}$. Conjecture 4.1 extends to unequal part sizes $m_1, \ldots, m_n$ but shows necessity forces $m_i = m_j$, so equal parts are unavoidable.

## Why it matters here
General background; no direct arena tie. Closest relevance is to combinatorial-design / extremal-graph problems where structured edge partitions or balanced colorings appear; the amalgamation–detachment + Nash-Williams laminar-family technique is a generic combinatorial tool potentially useful for explicit constructions in discrete-geometry problems.

## Open questions / connections
- Conjecture 4.1: does the equal-part requirement plus divisibility suffice for $\lambda K^3_{m_1, \ldots, m_n}$ in full generality? Author notes the detachment approach is unclear for remaining cases.
- Extends Baranyai's theorem [8, 9] to a non-standard multipartite notion (two vertices from one part allowed per edge), distinct from Baranyai's 1979 multipartite definition.
- Connects to Hilton–Rodger amalgamation lineage and earlier hypergraph detachment work [1, 2, 3, 4, 7]; open whether higher uniformities ($h \geq 4$) admit analogous theorems.

## Key terms
Baranyai's theorem, hypergraph factorization, amalgamation-detachment, Nash-Williams lemma, laminar family, complete multipartite hypergraph, 3-uniform hypergraph, edge coloring, Kirkman schoolgirl problem, Hilton-Rodger, $r$-factorization, combinatorial design
