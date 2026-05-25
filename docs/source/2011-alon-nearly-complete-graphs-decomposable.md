---
type: source
kind: paper
title: Nearly complete graphs decomposable into large induced matchings and their applications
authors: N. Alon, Ankur Moitra, B. Sudakov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1111.0253
source_local: ../raw/2011-alon-nearly-complete-graphs-decomposable.pdf
topic: general-knowledge
cites:
---

# Nearly complete graphs decomposable into large induced matchings and their applications

**Authors:** N. Alon, Ankur Moitra, B. Sudakov  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1111.0253

## One-line
Constructs nearly-complete graphs on $N$ vertices that can be partitioned into very large pairwise edge-disjoint induced matchings, disproving Meshulam's conjecture and yielding new bounds for shared-channel communication, linearity testing, and directed Steiner tree rounding.

## Key claim
There exist $(r,t)$-Ruzsa–Szemerédi graphs on $N$ vertices with edge density $1-o(1)$ (i.e., $rt = \binom{N}{2} - o(N^2)$) and matching size $r = N^{1-o(1)}$; and a covering of $K_N$ by two graphs each decomposable into at most $N^{2-\delta}$ induced matchings for $\delta > 0.058$.

## Method
Two constructions: (1) a **geometric** one — take $V=[C]^n$, connect pairs within $\|x-y\|_2^2$ close to the mean $\mu$, cover edges by induced subgraphs $G_z$ indexed by midpoints; use parallelogram-law / antipodal-ball volume to bound max degree by $10.5^n$, then decompose bounded-degree subgraphs into $O(d^2)$ induced matchings (inspired by Fox–Loh). (2) a **coding-theoretic** one — vertices $[C]^n$, edges when Hamming distance $> n-d$; equivalence classes under "$x$-flips" by codewords of proper Gilbert–Varshamov codes give induced matchings of size $2^{k-1}$. Lower bounds use entropy/Chain Rule arguments (Han-type) and a two-way counting argument on $F=\{(v,e)\}$.

## Result
Geometric: for any $\epsilon>0$, an $(r,t)$-RS graph with $r=N^{1-\epsilon-\delta}$ and missing edges $\le 2N^{2-\delta}$ where $\delta=e^{-O(1/\epsilon)}$. Coding: missing edges $\le N^e$ with $e=1+\frac{H(d/n)+(1-d/n)\log_2(C-1)}{\log_2 C}+o(1)$. Lower bound (Thm 3.8): any graph decomposable into induced matchings of size $r\ge 2$ has $\binom{N}{2}-|E|\ge (\frac{1}{2\sqrt{2}}-o(1))r^{1/2}N^{3/2}$; refined counting (Thm 3.12) gives $\binom{d}{2}\ge(r-1)(N-1-d)$ for min complement-degree $d$.

## Why it matters here
General background; no direct arena tie — this is extremal combinatorics on induced-matching decompositions of dense graphs, used in property testing / PCP / communication. It could inform Einstein Arena problems in **extremal graph theory** or **combinatorial design** families if any arise, and the entropy/counting lower-bound techniques are reusable as triple-verify cross-checks for combinatorial bounds.

## Open questions / connections
- Determine the full $(r,t)$ feasibility region for RS graphs on $N$ vertices; closing the gap for $r=N/(\log N)^g$, $g>1$ would improve Behrend-type bounds on 3-AP-free sets.
- Best $\delta$ for two-graph $K_{N,N}$ decomposition lies between $0.058$ and $2/3$ — open.
- Can these graphs yield integrality-gap constructions for the LP relaxation of directed Steiner tree (not just defeat candidate rounding schemes)?

## Key terms
Ruzsa–Szemerédi graph, induced matching decomposition, Behrend construction, 3-term arithmetic progression, Gilbert–Varshamov bound, proper linear code, Fox–Loh, Hoeffding inequality, parallelogram law, Hastad–Wigderson linearity test, Samorodnitsky–Trevisan, directed Steiner tree, shared directional multichannel, entropy chain rule, regularity lemma
