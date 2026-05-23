---
type: source
kind: paper
title: Perfect Matchings in 3-Uniform Hypergraphs with Large Vertex Degree
authors: Imdadullah Khan
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1101.5830
source_local: ../raw/2011-khan-perfect-matchings-3-uniform-hypergraphs.pdf
topic: general-knowledge
cites:
---

# Perfect Matchings in 3-Uniform Hypergraphs with Large Vertex Degree

**Authors:** Imdadullah Khan  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1101.5830

## One-line
Settles the exact minimum vertex-degree threshold guaranteeing a perfect matching in a 3-uniform hypergraph on $n=3k$ vertices.

## Key claim
If $H$ is a 3-uniform hypergraph on $n=3k$ vertices (large $n$) with $\delta_1(H) \geq \binom{n-1}{2} - \binom{2n/3}{2} + 1$, then $H$ contains a perfect matching; an explicit construction shows this bound is tight.

## Method
Two-case dichotomy by closeness to the extremal example. In the non-extremal case, an absorbing lemma (Hàn–Person–Schacht) reserves a small matching $M$ that can absorb any small leftover set; the almost-perfect matching on $V\setminus V(M)$ is built by iteratively growing a cover of disjoint balanced complete 3-partite subhypergraphs $K^{(3)}(t)$, using Erdős's hypergraph extremal lemma and a "link graph" analysis of pairs of tripartite graphs (forcing either matching-extending structure $B_{320}$ or the extremal-flag $B_{311}$). In the extremal case, exceptional vertices in $A$ and $B$ are greedily matched first, then a König–Hall argument on good pairs in $B$ closes out.

## Result
Proves $m_1(3,n) = \binom{n-1}{2} - \binom{2n/3}{2} + 1$, confirming the Hàn–Person–Schacht conjecture for $(r,d)=(3,1)$ exactly (asymptotically $\sim \tfrac{5}{9}\binom{n}{2}$). The matching lower bound is realized by the construction $V = A \cup B$ with $|A|=n/3-1$, $|B|=2n/3+1$, edges = all triples meeting $A$. Proved independently and in parallel by Kühn–Osthus–Treglown.

## Why it matters here
General background; no direct arena tie — extremal hypergraph theory and absorbing-method techniques are adjacent to the arena's discrete-combinatorics problems but this exact threshold result does not map onto any current Einstein Arena problem. The absorbing-lemma + iterative cover-growth pattern could conceivably inform extremal-graph problems if one arises.

## Open questions / connections
- Extends to $r=4$, $d=1$ in Khan's follow-up; Conjecture 2 of Hàn–Person–Schacht remains open for general $1 \leq d < r/2$.
- Pikhurko's codegree threshold result ($d \geq r/2$) and Rödl–Ruciński–Szemerédi's $d=r-1$ resolution bracket this; the middle regime is the hard one.
- The "link graph" $B_{311}$ flag-as-extremal-signature trick may generalize to other density-dichotomy proofs.

## Key terms
perfect matching, 3-uniform hypergraph, vertex degree threshold, absorbing lemma, extremal hypergraph theory, Dirac-type theorem, complete 3-partite 3-graph, König–Hall, Hàn–Person–Schacht conjecture, Rödl–Ruciński–Szemerédi, Khan, Erdős extremal lemma
