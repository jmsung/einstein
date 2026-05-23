---
type: source
kind: paper
title: A Birthday Repetition Theorem and Complexity of Approximating Dense CSPs
authors: Pasin Manurangsi, P. Raghavendra
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1607.02986
source_local: ../raw/2016-manurangsi-birthday-repetition-theorem-complexity.pdf
topic: general-knowledge
cites:
---

# A Birthday Repetition Theorem and Complexity of Approximating Dense CSPs

**Authors:** Pasin Manurangsi, P. Raghavendra  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1607.02986

## One-line
Proves that the value of a two-prover game decays exponentially in $\Omega(kl/n)$ under $(k\times l)$-birthday repetition, and uses this to nail down the tight time-vs-approximation tradeoff for dense Max k-CSP.

## Key claim
For a two-prover game $G$ with $\mathrm{val}(G) = 1-\varepsilon$ (uniform $Q$, biregular support graph, constant alphabet), $\mathrm{val}(G_{k\times l}) \le 2(1-\varepsilon/2)^{\Omega(\varepsilon^5 kl/n)}$ — resolving the Aaronson–Impagliazzo–Moshkovitz [AIM14] conjecture that birthday repetition reduces value at the birthday-paradox rate $\Theta(kl/n)$.

## Method
Reduce birthday repetition to standard parallel repetition by a chain of five distributional comparisons: $G^{\otimes r} \to G^{\otimes r}_{\mathrm{set}} \to G^{\mathrm{em}}_{k\times l} \to G^{\mathrm{em},[s_1,s_2]}_{k\times l} \to G^{[s_1,s_2]}_{k\times l} \to G_{k\times l}$, each step controlled by either a no-collision argument, an embedding of parallel repetition, or a Bernstein-type concentration bound on the number of edges in a random bipartite subgraph. Algorithmic side uses conditioning-based rounding of Sherali-Adams (BRS/RT/YZ-style), with a sharpened total-correlation bound for conditioned SA solutions. Lasserre integrality gap is transported from Schoenebeck's random Max-3XOR via a clause/variable reduction.

## Result
Three matching results for dense Max k-CSP at alphabet size $q$: (i) $O(q^{1/i})$-approximation via $O_{k,\varepsilon}(i/\Delta)$-level Sherali-Adams; (ii) integrality gap of $q^{1/i}$ for $\tilde\Omega_k(i)$-level Lasserre on fully-dense instances; (iii) under ETHA (Max-3SAT has no sub-exp $(1-\varepsilon)$-approx), no $(nq)^{\tilde O_k(i)}$ algorithm achieves $(nq)^{1/i}$-approximation. Corollaries: $\mathrm{NTIME}(n) \subseteq \mathrm{AM}_{\tilde O(\sqrt n)}(2)$, and an $n^{O(i)}$-time $\Omega(n^{-1/i})$-density algorithm for Densest k-Subhypergraph on $O(1)$-uniform hypergraphs with constant-density optimum.

## Why it matters here
General background on hardness-of-approximation machinery; no direct arena tie. The conditioning-based SA rounding and the "subsample then exhaustive enumerate" template behind dense-CSP algorithms could inform combinatorial relaxations of arena CSP-shaped problems (extremal graph, Sidon-like, autocorrelation as quadratic CSP), but the regime here is large-$n$ asymptotic, not the small-$n$ ulp-polish regime of Einstein Arena.

## Open questions / connections
- Can birthday repetition with value-decay be used to amplify hardness for problems beyond free games / Nash / DkS (e.g., small-set expansion)?
- Tightening the $\varepsilon^5$ dependence in the exponent — likely loose, possibly $\varepsilon^{O(1)}$ with a sharper concentration step.
- Closes the gap to Aaronson–Impagliazzo–Moshkovitz [AIM14] (no value decay) and extends Raz/Holenstein parallel repetition technology to the unstructured birthday setting.

## Key terms
birthday repetition, parallel repetition, two-prover game, free game, dense CSP, Max k-CSP, Sherali-Adams hierarchy, Lasserre hierarchy, sum-of-squares, Exponential Time Hypothesis, ETH, Densest k-Subhypergraph, AM(2) protocol, integrality gap, Manurangsi, Raghavendra, Aaronson, conditioning rounding, total correlation, label cover
