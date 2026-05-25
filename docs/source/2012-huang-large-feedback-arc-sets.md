---
type: source
kind: paper
title: Large feedback arc sets, high minimum degree subgraphs, and long cycles in Eulerian digraphs
authors: Hao Huang, Jie Ma, Asaf Shapira, Benny Sudakov, Raphael Yuster
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1202.2602v1
source_local: ../raw/2012-huang-large-feedback-arc-sets.pdf
topic: general-knowledge
cites: 
---

# Large feedback arc sets, high minimum degree subgraphs, and long cycles in Eulerian digraphs

**Authors:** Hao Huang, Jie Ma, Asaf Shapira, Benny Sudakov, Raphael Yuster  ·  **Year:** 2012  ·  **Source:** http://arxiv.org/abs/1202.2602v1

## One-line
Establishes a tight quadratic lower bound on the minimum feedback arc set of Eulerian digraphs and uses it to derive short-cycle, long-cycle, and high-minimum-degree subgraph existence results.

## Key claim
Every Eulerian digraph $G$ with $n$ vertices and $m$ arcs satisfies $\beta(G) \geq m^2/(2n^2) + m/(2n)$, and this is tight for infinitely many $(m,n)$ (Cayley digraph construction).

## Method
Linear-order / backward-arc counting: fix any vertex order, partition arcs into short ($\leq n/2$) and long via an integer optimization. Bound short-arc length sums using the 2-cycle-free structure ($\binom{s_i+1}{2}$ per vertex), bound long arcs via cut-crossing counts using Lemma 2.1 (Eulerian cuts are balanced), and average over pairs of cuts $(C_i, C_{i+\lfloor n/2 \rfloor})$. The resulting minimization $F(m,n) = tm - (t^2-t)n/2$ with $t = \lceil m/n \rceil$ yields the bound.

## Result
Three corollaries follow: (i) girth $g(G) \leq 6n^2/m$ (combining with Fox–Keevash–Sudakov bound, tight up to constant); (ii) $G$ has an Eulerian subgraph with minimum degree $\geq m^2/(24n^3)$, tight up to constant via a blowup construction $H(s,2s,\delta)$; (iii) $G$ has a cycle of length $\geq 1 + \max\{m^2/(24n^3), \lfloor m/n \rfloor\}$, partially verifying the Bollobás–Scott conjecture in the dense regime $m = \Theta(n^2)$.

## Why it matters here
General background for extremal digraph theory — feedback arc set lower bounds, Eulerian-digraph cycle existence, and the Caccetta–Häggkvist / Bollobás–Scott circle. Tangential to Einstein Arena combinatorics problems (extremal graph theory, discrete geometry); no direct arena tie unless a problem reduces to feedback arc sets or cycle existence in Eulerian digraphs.

## Open questions / connections
- Bollobás–Scott conjecture (cycle of length $\Omega(m/n)$ in Eulerian digraphs) remains open for sparse regime $m = o(n^{3/2})$.
- Caccetta–Häggkvist conjecture for Eulerian digraphs — short-cycle bound here is a partial step.
- Does some DFS tree of an Eulerian digraph have depth $\Omega(m/n)$? Proposition 4.1 rules out a naive DFS bound but leaves the path-existence variant open.

## Key terms
feedback arc set, Eulerian digraph, girth, Bollobás-Scott conjecture, Caccetta-Häggkvist conjecture, minimum degree subgraph, cycle length, backward arc, cut counting, Cayley digraph, DFS depth, extremal digraph
