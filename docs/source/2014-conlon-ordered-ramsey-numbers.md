---
type: source
kind: paper
title: Ordered Ramsey numbers
authors: D. Conlon, J. Fox, Choongbum Lee, B. Sudakov
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1410.5292
source_local: ../raw/2014-conlon-ordered-ramsey-numbers.pdf
topic: general-knowledge
cites:
---

# Ordered Ramsey numbers

**Authors:** D. Conlon, J. Fox, Choongbum Lee, B. Sudakov  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1410.5292

## One-line
Initiates a systematic study of ordered Ramsey numbers $r_<(H)$ — Ramsey numbers for vertex-labeled graphs where the monochromatic copy must respect the labeling order — and shows they can be vastly larger than ordinary Ramsey numbers even for matchings.

## Key claim
There exist ordered matchings $M$ on $n$ vertices with $r_<(M) \geq n^{c \log n / \log \log n}$ (superpolynomial), while every ordered graph $H$ on $n$ vertices satisfies $r_<(H) \leq r(H)^{c \log^2 n}$ — so the ordered and unordered worlds diverge sharply for sparse graphs but stay close for dense ones.

## Method
Lower bounds use probabilistic constructions: random matchings (Lemma 2.2: random matchings hit any two intervals of length $\geq 4\sqrt{n \log n}$) combined with recursive blow-up of Ramsey-extremal colorings, plus the van der Corput low-discrepancy permutation for the $\chi_<(M)=2$ case. Upper bounds use greedy interval-partition embeddings ($r_<(M) \leq n^{\lceil \log n \rceil}$ via halving the interval chromatic number) and a degeneracy-driven density-increment argument à la Conlon for the $2^{cd \log^2(2n/d)}$ bound. An Erdős–Rado-style stepping-up reduces 3-uniform hypergraph Ramsey numbers to ordered graph Ramsey numbers of a derived family $S_H$.

## Result
- $r_<(P_n) = (n-1)^2 + 1$ (Erdős–Szekeres restated); $r_<(P_m, K_n) = (m-1)(n-1)+1$.
- Matchings: $n^{c \log n / \log \log n} \leq r_<(M) \leq n^{\lceil \log n \rceil}$ for some $M$; for $\chi_< = 2$, $\Omega(n^2 / (\log^2 n \log \log n)) \leq r_<(M) \leq n^2$.
- Degeneracy bound: $r_<(H) \leq n^{cd \log \chi}$ and $r_<(H) \leq 2^{cd \log^2(2n/d)}$.
- Off-diagonal: $r_<(M, K_3) \geq c (n/\log n)^{4/3}$ for some matching $M$.
- Characterization: $r_<(G) = O(n)$ in every ordering iff vertex cover number $\tau(G) = O(1)$.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein problems are graph-Ramsey problems. Potentially informs extremal-combinatorics framing for problems involving forbidden ordered patterns (sequences, autocorrelation supports) and the meta-technique of low-discrepancy permutations (van der Corput) as adversarial constructions.

## Open questions / connections
- Close the matching gap between $n^{c \log n / \log \log n}$ lower and $n^{\log n}$ upper bound (Problem 6.2).
- Off-diagonal: is $r_<(M, K_3) \leq O(n^{2-\epsilon})$? (Problem 6.1).
- Ordered Ramsey number of the $d$-cube $Q_d$: current $2^{cd^3}$ upper vs $2^{c'd^2/\log d}$ lower (Problem 6.4); does a linear ordering exist (Problem 6.6)?
- Extends Burr–Erdős, Chvátal–Rödl–Szemerédi–Trotter, and Lee's degenerate-graph Ramsey results into the ordered setting.

## Key terms
ordered Ramsey number, ordered matching, interval chromatic number, degeneracy, van der Corput permutation, monotone path, Erdős–Szekeres, vertex cover, bandwidth, hypergraph Ramsey, off-diagonal Ramsey, Burr–Erdős conjecture
