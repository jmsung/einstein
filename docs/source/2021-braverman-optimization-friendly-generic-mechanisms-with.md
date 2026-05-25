---
type: source
kind: paper
title: Optimization-friendly generic mechanisms without money
authors: Mark Braverman
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2106.07752v1
source_local: ../raw/2021-braverman-optimization-friendly-generic-mechanisms-with.pdf
topic: general-knowledge
cites: 
---

# Optimization-friendly generic mechanisms without money

**Authors:** Mark Braverman  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2106.07752v1

## One-line
Introduces APEX, a meta-algorithm that converts local-search optimization heuristics into incentive-compatible mechanisms without money by combining VCG pricing, bandits-with-knapsacks, and adaptive utility reweighing.

## Key claim
For one-sided assignment of $n$ items to $n$ unit-demand players, there always exist scalars $\lambda_i \geq 0$ such that running unit-demand VCG on reweighed utilities $u'_{ij} = \lambda_i u_{ij}$ yields prices $C_j$ and allocation $X$ forming a Hylland–Zeckhauser competitive equilibrium from equal incomes (CEEI) — strengthening [HZ79], with a new proof using only Brouwer's fixed-point theorem (not Kakutani).

## Method
APEX (Adaptive Pricing Equalizing Externalities) iterates: at round $t$, the principal locally optimizes $\sum_i \lambda_{i,t} f_i(x) + F_0(x)$ via heuristic $H$, computes VCG prices in tokens, and charges players against a fixed token budget $B$; players adapt $\lambda_{i,t}$ via bandits-with-knapsacks to maximize utility subject to budget. The HZ-strengthening theorem is proved directly via Brouwer on a continuous map combining VCG-price computation and budget-balancing. A strictly concave regularizer $f_0(x) = -\beta/x$ ensures unique best-responses and converts low-regret executions into approximate CEEI.

## Result
Theorem 5: scaled-utility VCG prices always support an HZ equilibrium (but not all HZ equilibria arise from VCG prices — strict containment). Theorem 13: with regularizer $f_0(x_{ij}) = -\bar\lambda^{-3} n^{-4}/x_{ij}$ and per-player strong regret $\varepsilon T$ with $\varepsilon = o(\bar\lambda^{-12} n^{-22})$, any feasible execution produces a $\delta$-approximate CEEI for $\delta = 10\bar\lambda^{-1}$. Lemma 4: truthful reporting is a $(2\varepsilon)$-dominant strategy when heuristic $H$ is locally correct and player regret is $\leq \varepsilon$.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are extremal-mathematics optimization (sphere packing, kissing numbers, autocorrelation, extremal graphs), not mechanism design — this paper's regret/VCG/CEEI machinery does not inform any of the 23 problems.

## Open questions / connections
- Convergence of APEX is left open in full generality (heuristic $H$ is treated as a black box).
- The "externality" notion for two-sided matching with cardinal preferences appears non-canonical — Gale-Shapley extension flagged as the most interesting application but unresolved.
- Voting with cardinal preferences via APEX is mentioned as ongoing work, beyond scope.
- Extends/relates to [HZ79], [Bud11] (combinatorial CEEI), [GTV20], [VY20] (HZ complexity), [BKS13b] (BwK).
- Whether low-regret BwK against best-sequence-in-hindsight is attainable in this hybrid online-knapsack setting remains open.

## Key terms
APEX, mechanism design without money, VCG, competitive equilibrium from equal incomes, CEEI, Hylland-Zeckhauser, bandits with knapsacks, swap regret, correlated equilibrium, Brouwer fixed point, one-sided assignment, regularized optimization, follow-the-regularized-leader, Braverman
