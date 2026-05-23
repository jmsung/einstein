---
type: source
kind: paper
title: An Extension of the Moser-Tardos Algorithmic Local Lemma
authors: W. Pegden
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.2853
source_local: ../raw/2011-pegden-extension-moser-tardos-algorithmic-local.pdf
topic: general-knowledge
cites:
---

# An Extension of the Moser-Tardos Algorithmic Local Lemma

**Authors:** W. Pegden  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.2853

## One-line
Gives an algorithmic analog of the Bissacot et al. cluster-expansion improvement to the Lovász Local Lemma, showing the Moser-Tardos resampling algorithm still runs in expected $\sum_A \mu_A$ steps under a weaker hypothesis.

## Key claim
Theorem 1.4: if $0 < \mu_A < \infty$ satisfy $P(A) \le \mu_A / \sum_{I \subset \bar{\Gamma}(A),\ I\ \text{indep}} \prod_{B \in I} \mu_B$, then the Moser-Tardos algorithm finds an assignment avoiding all events in $\mathcal{A}$, resampling each $A$ at most $\mu_A$ times in expectation. The sum-over-independent-sets condition is strictly weaker than the classical $P(A) \le x_A \prod_{B \sim A}(1-x_B)$ (recovered by $\mu_A = x_A/(1-x_A)$ dropping the independence restriction).

## Method
Re-runs the Moser-Tardos witness-tree analysis with a sharper observation: any witness tree arising from the algorithm log is *strongly proper* — children of a common vertex carry labels forming an independent set in the dependency graph, not merely distinct labels. A modified branching process resamples each subprocess until its child labels form an independent set, yielding a tighter per-tree probability $p'_T = \mu_{A_0}^{-1} \prod_{v \in T} \mu_{A_v} / \sum_{I \subset \bar{\Gamma}(A_v),\ I\ \text{indep}} \prod_{A \in I} \mu_A$. Summing $\sum_T p'_T \le 1$ over strongly proper trees gives the bound.

## Result
The same expected runtime bound as Moser-Tardos ($\sum_A \mu_A$ resamplings, equivalent to $\sum_A x_A/(1-x_A)$) holds under the weaker independent-set condition. Provides an algorithmic proof of Bissacot-Fernández-Procacci-Scoppola (2010) independent of Shearer's theorem and cluster-expansion machinery, and extends to the lopsided dependency-graph setting of Erdős-Spencer.

## Why it matters here
General background; no direct arena tie. LLL/Moser-Tardos are foundational for probabilistic-combinatorics existence proofs (hypergraph colorings, Latin transversals, extremal constructions); the stronger independent-set condition could in principle tighten existence bounds for combinatorial Einstein Arena problems (extremal graph theory, Sidon-like constructions) where dependency graphs are dense but local independent sets are small.

## Open questions / connections
- Kolipaka-Szegedy (2010) directly tie Shearer's tight condition to the Moser-Tardos framework — relationship to this paper's intermediate strengthening.
- Concrete combinatorial applications where the independent-set sum is materially smaller than the unrestricted sum (Ndreca-Procacci-Scoppola graph coloring is one example cited).
- Whether further structural restrictions on witness trees (beyond strongly-proper) yield additional algorithmic gains.

## Key terms
Lovász Local Lemma, Moser-Tardos algorithm, algorithmic LLL, witness tree, dependency graph, cluster expansion, Bissacot-Fernández-Procacci-Scoppola, Shearer's condition, independent-set polynomial, lopsided LLL, resampling, probabilistic combinatorics, hypergraph coloring
