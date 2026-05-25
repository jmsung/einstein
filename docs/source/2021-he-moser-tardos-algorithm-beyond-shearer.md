---
type: source
kind: paper
title: "Moser-Tardos Algorithm: Beyond Shearer's Bound"
authors: Kun He, Qian Li, Xiaoming Sun
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2111.06527
source_local: ../raw/2021-he-moser-tardos-algorithm-beyond-shearer.pdf
topic: general-knowledge
cites:
---

# Moser-Tardos Algorithm: Beyond Shearer's Bound

**Authors:** Kun He, Qian Li, Xiaoming Sun  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2111.06527

## One-line
Proves that the Moser-Tardos resampling algorithm converges efficiently on probability vectors strictly beyond Shearer's bound whenever the dependency graph contains a chordless cycle.

## Key claim
For any non-chordal dependency graph $G_D$, $\mathcal{I}_{MT}(G_D) \supsetneq \mathcal{I}_a(G_D)$: there exists $\boldsymbol{p}$ with $L_1$-gap $d(\boldsymbol{p}, G_D) \geq 2^{-20} K^{-3}$ beyond Shearer's bound (where $K$ is the shortest chordless cycle length) for which MT still terminates in expected polynomial time. For chordal $G_D$, equality $\mathcal{I}_{MT}(G_D) = \mathcal{I}_a(G_D)$ holds, completely resolving the open problem.

## Method
"Intersection LLL" — a new convergence criterion that subtracts $\tfrac{1}{171}\delta_{i,i'}^2$ from event probabilities when matched dependent events $A_i, A_{i'}$ have intersection probability at least $\delta_{i,i'}$, then checks Shearer's bound on the reduced vector. Proof uses witness-DAG (wdag) analysis from Kolipaka-Szegedy: groups proper wdags by sink label and label-multiplicity, uses an auxiliary table of fair coins on *reversible arcs* to partition the consistency event into nearly-disjoint pieces, then constructs an injective map from wdags of $G_D$ to wdags of a "split" graph $G_{\mathcal{M}}$ whose weight sum coincides with the reduced Shearer condition.

## Result
For non-chordal $G_D$ with disjoint chordless cycles $C_1, \ldots, C_\ell$, MT is efficient if $d(\boldsymbol{p}, G_D) < \tfrac{1}{545} \sum_i |C_i| (\min_j p_j) (4 \max_j \sqrt{p_j})^{-2|C_i|}$. Concrete symmetric-probability gaps over Shearer's bound on infinite lattices: square lattice $+1.858 \times 10^{-22}$ above $0.1193$; hexagonal $+2.597 \times 10^{-25}$ above $0.1547$; simple cubic $+7.445 \times 10^{-23}$ above $0.0744$. Gaps are existence-only — tiny but constant.

## Why it matters here
General background; no direct arena tie. The intersection-LLL technique could inform any arena problem framed as a constraint-satisfaction LLL instance (hypergraph coloring, $k$-SAT-style), but none of the 23 Einstein problems are currently posed in that form.

## Open questions / connections
- Szegedy's conjecture $\mathcal{I}_{MT}(G_D) = \mathcal{I}_v(G_D)$ remains open; this paper is only the first step beyond Shearer's bound.
- Can the matching restriction in intersection LLL be lifted to use *all* dependent-event intersections, giving exponentially larger gaps?
- Connection to the Repulsive Lattice Gas / hard-core lattice model in statistical mechanics (Shearer's bound = independence polynomial root) — does going beyond Shearer correspond to a known phase-transition phenomenon?

## Key terms
Moser-Tardos algorithm, Lovász Local Lemma, Shearer's bound, variable LLL, dependency graph, chordal graph, chordless cycle, witness DAG, resampling table, intersection LLL, hard-core lattice gas, extremal instances, Kolipaka-Szegedy
