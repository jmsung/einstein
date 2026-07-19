---
type: source
kind: paper
title: 1-Factorizations of Pseudorandom Graphs
authors: Asaf Ferber, Vishesh Jain
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.10361
source_local: ../raw/2018-ferber-1-factorizations-pseudorandom-graphs.pdf
topic: general-knowledge
cites:
---

# 1-Factorizations of Pseudorandom Graphs

**Authors:** Asaf Ferber, Vishesh Jain  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.10361

## One-line
Proves that sufficiently good spectral expanders (and hence typical random $d$-regular graphs for all $d$) admit a 1-factorization — a decomposition of edges into perfect matchings — and gives a near-tight lower bound on the count.

## Key claim
For every $\varepsilon > 0$ there exist $d_0, n_0$ such that every $(n,d,\lambda)$-graph with $n \geq n_0$ even, $d_0 \leq d \leq n-1$, and $\lambda \leq d^{1-\varepsilon}$ (in particular $\lambda \leq d^{0.9}$) has chromatic index $\chi'(G) = d$, i.e. admits a 1-factorization. The number of such 1-factorizations is at least $\big((1-\varepsilon)\,d/(2e^2)\big)^{nd/2}$, off by a factor of $2$ in the exponent base from the Linial–Luria upper bound $\big(d/e^2\big)^{nd/2}\cdot(1+o(1))$.

## Method
Probabilistic edge-decomposition: partition $E(G)$ into $t \ll d$ edge-disjoint "almost-balanced-bipartite" pieces $H_i$ via a random balanced bipartition (Lemma 3.1) using Chernoff in the dense case and the asymmetric Lovász Local Lemma in the sparse case. Each $H_i$ is shown to be a "good" expander via the Expander Mixing Lemma, then enlarged with a 2-factor slice $G'_i$ from Petersen's theorem so that the residue induced on each side $A_i, B_i$ can be absorbed: decompose $R_i[A_i]$ and $R_i[B_i]$ into matched matching-pairs (via Vizing) and complete each pair to a perfect matching of $R_i$. The leftover is a regular balanced bipartite graph, which 1-factorizes by Hall + Schrijver counting.

## Result
- $\chi'(G) = d$ for all $(n,d,\lambda)$-graphs with $\lambda \leq d^{1-\varepsilon}$, $d \geq d_0$, $n$ even (Theorem 1.1).
- Corollary: a typical $G_{n,d}$ admits a 1-factorization a.a.s. for all $d_0 \leq d \leq n-1$, closing the range left open by Janson and Molloy–Robalewska–Robinson–Wormald (fixed-$d$ only).
- 1-factorization count $\geq \big((1-\varepsilon)\,d/(2e^2)\big)^{nd/2}$ (Theorem 1.6), beating the previous lower bound — even for $K_n$ — by a multiplicative factor of $2^{nd/2}$.
- Proofs are constructive and yield randomized polynomial-time algorithms.

## Why it matters here
General background; no direct Einstein Arena problem tie — none of the 23 problems are about edge-colorings of pseudorandom graphs. Useful as a methodology exemplar for the agent: combining the Expander Mixing Lemma + asymmetric Lovász Local Lemma + random partitioning to convert a non-bipartite combinatorial-design problem into many bipartite sub-problems is a transferable pattern relevant whenever extremal-graph or packing problems sit near a spectral-expander regime.

## Open questions / connections
- Can $\lambda$ be pushed from $d^{1-\varepsilon}$ down to $d/\mathrm{polylog}\,n$, or even $\lambda \leq d - C$ (matching Krivelevich–Sudakov / Cioabă–Gregory–Haemers for perfect matchings)?
- Does $G_{n,d}$ admit a Hamilton-cycle decomposition for all $d$, not just fixed $d$ (Kim–Wormald)?
- Can the lower bound be tightened to match the Linial–Luria upper bound $(d/e^2)^{nd/2}$ — Ferber–Jain–Sudakov forthcoming work does this for $d \geq n/2 + \varepsilon n$.
- Extension to $k$-uniform $d$-regular hypergraphs $H^k_{n,d}$ — no non-trivial lower bound is known even for the complete hypergraph.

## Key terms
1-factorization, perfect matching, chromatic index, $(n,d,\lambda)$-graph, spectral expander, pseudorandom graph, random regular graph $G_{n,d}$, Expander Mixing Lemma, Lovász Local Lemma, Vizing's theorem, Petersen 2-factor theorem, Hall's marriage theorem, Schrijver permanent bound, Linial–Luria, edge coloring
