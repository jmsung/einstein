---
type: source
kind: paper
title: Large matchings in uniform hypergraphs and the conjectures of Erdos and Samuels
authors: Noga Alon, Peter Frankl, Hao Huang, Vojtech Rodl, Andrzej Rucinski, Benny Sudakov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1107.1219v2
source_local: ../raw/2011-alon-large-matchings-uniform-hypergraphs.pdf
topic: general-knowledge
cites: 
---

# Large matchings in uniform hypergraphs and the conjectures of Erdos and Samuels

**Authors:** Noga Alon, Peter Frankl, Hao Huang, Vojtech Rodl, Andrzej Rucinski, Benny Sudakov  ·  **Year:** 2011  ·  **Source:** http://arxiv.org/abs/1107.1219v2

## One-line
Reduces the problem of finding minimum $d$-degree thresholds for perfect matchings in $k$-uniform hypergraphs to the (easier) fractional version, and resolves several new asymptotic cases via a probabilistic inequality of Samuels.

## Key claim
If $f_d(k,n) \sim c^* \binom{n-d}{k-d}$ for some $c^* > 0$, then $m_d(k,n) \sim \max(c^*, 1/2)\binom{n-d}{k-d}$; combined with new bounds on $f_d$, this yields asymptotics like $m_1(4,n) \sim \tfrac{37}{64}\binom{n-1}{3}$, $m_1(5,n) \sim \tfrac{369}{625}\binom{n-1}{4}$, $m_2(5,n) \sim \tfrac12\binom{n-2}{3}$, $m_2(6,n) \sim \tfrac{671}{1296}\binom{n-2}{4}$, $m_3(7,n) \sim \tfrac12\binom{n-4}{3}$.

## Method
Three ingredients: (1) a duality/weight-shifting argument showing $f_d(k,n) \le f_0^{n/k}(k-d,n-d)$, reducing Dirac-type fractional thresholds to an Erdős-type edge-vs-matching-number problem; (2) Samuels' conjecture on $P(X_1+\cdots+X_l < 1)$ for independent nonnegative variables with prescribed means (proven for $l \le 4$), giving the bound $f_0^{xm}(l,m) \sim (1 - (1-x)^l)\binom{m}{l}$ when $x \le 1/(l+1)$; (3) the Strong Absorbing Lemma plus a two-round random-sampling construction (random vertex subsets $R_i$ of size $\sim n^{0.1}$, then random selection by fractional matching weights) feeding the Frankl–Rödl near-perfect-matching theorem to convert fractional matchings into integer ones.

## Result
Confirms Conjecture 1.1 (Dirac-type matching threshold) for $(k,d) \in \{(4,1),(5,1),(5,2),(6,2),(7,3)\}$, and confirms the fractional Erdős conjecture asymptotically for $l \in \{3,4\}$ in the range $x \le 1/(l+1)$ (extendable via Mathematica to $x \le 0.277$ for $l=3$ and $x \le 0.217$ for $l=4$). Establishes Theorem 1.2: $f_d(k,n) \sim (1 - ((k-1)/k)^{k-d})\binom{n-d}{k-d}$ for $k-4 \le d \le k-1$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological — the geometric–arithmetic mean inequality manipulation in Proposition 2.1, the duality between $\nu^*$ and $\tau^*$, and the absorbing-method + random-rounding pipeline are general extremal-combinatorics tools that could inform discrete-geometry or extremal-graph arena problems involving packing/matching structure.

## Open questions / connections
- Samuels' conjecture for $l \ge 5$ with equal means $\mu_i = x \le 1/(l+1)$ remains open; resolving it would extend Theorem 1.2 to all $(k,d)$ and asymptotically settle Conjecture 1.1.
- Erdős' 1965 conjecture on $m_0^s(k,n) = \max\{\binom{ks-1}{k}, \binom{n}{k} - \binom{n-s+1}{k}\}$ is still wide open in general; proven for $k=2$ (Erdős–Gallai) and $k=3, n \ge 4s$ (Frankl–Rödl–Ruciński).
- Application to distributed storage allocation (Leong–Dimakis–Ho): the optimal-allocation problem $F_T(r,n)$ is asymptotically equivalent to the fractional Erdős problem; binomial-access model variant remains open.

## Key terms
perfect matching, fractional matching, uniform hypergraph, minimum d-degree, Dirac-type threshold, Erdős matching conjecture, Samuels conjecture, absorbing lemma, fractional vertex cover, LP duality, Chernoff inequality, Frankl-Rödl, extremal hypergraph, distributed storage allocation
