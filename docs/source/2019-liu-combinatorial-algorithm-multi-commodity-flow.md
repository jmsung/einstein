---
type: source
kind: paper
title: A Combinatorial Algorithm for the Multi-commodity Flow Problem
authors: Pengfei Liu
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.09397
source_local: ../raw/2019-liu-combinatorial-algorithm-multi-commodity-flow.pdf
topic: general-knowledge
cites:
---

# A Combinatorial Algorithm for the Multi-commodity Flow Problem

**Authors:** Pengfei Liu  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.09397

## One-line
Proposes the first non-LP combinatorial algorithm for the multi-commodity flow problem by relaxing capacity constraints into arc penalty functions and solving for an "equilibrium pseudo-flow."

## Key claim
The multi-commodity flow problem (MFP) has a feasible solution iff there exists a zero-equilibrium pseudo-flow; equivalently, the non-linear program $\min \sum_a \int_0^{f_a} h(\omega)\,d\omega$ (subject to flow conservation only) attains objective value $0$ iff MFP is feasible. The KKT conditions of this program coincide with Wardrop-style equilibrium conditions (all used $s_k$-$t_k$ paths have equal minimum length under penalty weights).

## Method
Replace hard capacity $f_{ij}\le u_{ij}$ with a penalty $h(f_{ij}) = \max(0, f_{ij}-u_{ij})$ on each arc; minimize $\sum_a \int_0^{f_a} h(\omega)\,d\omega$ over pseudo-flows satisfying only conservation + nonnegativity. The convex program is solved by the Frank–Wolfe algorithm: at each iteration use $\{h(f_{ij,n})\}$ as arc weights, route all $s_k$-$t_k$ demand on shortest paths, then line-search. Infeasibility detection uses Lemma 1 (Onaga–Kakusho / Iri / Matula–Shahrokhi cut condition $\sum_k l^{s\mu}_{k,t_k} d_k \le \sum_{(i,j)} \mu_{ij} u_{ij}$).

## Result
Theorems 1–3 establish the equivalence: equilibrium pseudo-flow is zero $\Leftrightarrow$ MFP feasible (zero-equilibrium *is* a feasible flow); nonzero $\Leftrightarrow$ MFP infeasible. The Frank–Wolfe iteration converges sublinearly at rate $O(1/k)$ in objective error. Remark 4 extends the framework to minimum-cost MFP by setting $h(f_{ij}) = c_{ij}$ if $f_{ij}\le u_{ij}$, else $c_{ij} + M(f_{ij}-u_{ij})$ for large $M$.

## Why it matters here
General background; no direct arena tie. The Wardrop / Beckmann equilibrium framing and the penalty-relaxation-of-hard-constraints pattern are methodologically reusable (penalty-as-Lagrangian for capacity, KKT-equilibrium correspondence), but no current Einstein problem is multi-commodity flow.

## Open questions / connections
- Faster Frank–Wolfe variants (Lacoste-Julien & Jaggi 2015; Pena & Rodriguez 2019) for linear-rate convergence — could the equilibrium pseudo-flow be found in $O(\log 1/\epsilon)$ iterations rather than $O(1/\epsilon)$?
- Quantitative complexity bound is absent: paper gives no polynomial-time guarantee competitive with LP-based MFP solvers.
- Connection to LP duality / cut-condition (Lemma 1) suggests a primal-dual reading; whether equilibrium pseudo-flow gives a constructive certificate of infeasibility (the violating $\mu$) is not developed.

## Key terms
multi-commodity flow, equilibrium pseudo-flow, Frank-Wolfe algorithm, penalty function, Wardrop equilibrium, Beckmann formulation, KKT conditions, convex programming, flow conservation, max-flow min-cut, Onaga-Kakusho, network optimization
