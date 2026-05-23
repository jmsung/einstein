---
type: source
kind: paper
title: A Localized Method for the Multi-commodity Flow Problem
authors: Pengfei Liu
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.07549v7
source_local: ../raw/2021-liu-localized-method-multi-commodity-flow.pdf
topic: general-knowledge
cites: 
---

# A Localized Method for the Multi-commodity Flow Problem

**Authors:** Pengfei Liu  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2108.07549v7

## One-line
Reformulates the multicommodity flow (MCF) feasibility problem as an edge-separable convex equilibrium search and gives three GPU-parallel "potential difference reduction" (PDR) algorithms.

## Key claim
A flow is MCF-feasible iff it is a zero-stable pseudo-flow — i.e., a pseudo-flow with vertex height $h_{ik} = \Delta_{ik}/\delta_i$ and edge congestion $\psi_{ij} = \max(0, f_{ij} - u_{ij})$ both identically zero, with potential difference $\phi_{ij,k} = h_{ik} - h_{jk} - \psi_{ij} = 0$ on used edges and $\le 0$ on unused edges.

## Method
Relax both capacity and conservation constraints into a convex objective $z = \sum_{ij}\!\int_0^{f_{ij}}\!\psi_{ij} + \sum_{i,k}\!\int_0^{\Delta_{ik}}\!h_{ik}$, then rewrite as a sum of per-edge quadratics using Jensen's inequality on the height term. KKT stationarity recovers exactly the stable-pseudo-flow conditions, so feasibility ⇔ optimum is zero. The three algorithms (PDR-ESO exact QP per edge, PDR-AGD adaptive projected gradient, PDR-GDM with momentum $\gamma=0.9$) all use the negative gradient $\phi_{ij,k}$ as the local update direction and run each edge subproblem in parallel on GPU.

## Result
Convergence (monotone non-increasing $z$) is proved for PDR-ESO via a Jensen-based surrogate-majorization argument; convergence rate is left open. On 28 standard benchmarks (Planar / Grid / Telecom up to $|E|=12{,}990$, $|K|=81{,}430$, ~152M flow variables on Cgd15), PDR-GDM is fastest — e.g., Cpl1000 in 2298 iter vs 10695 for PDR-AGD (4.6×), Cgd15 in 24.45s on an A100. Counter-intuitively, the exact per-edge solver (PDR-ESO) typically needs *more* iterations than the cheap momentum heuristic.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the edge-separable surrogate-majorization + Jensen trick is a generic pattern for parallelizing convex problems with vertex/edge coupling, and could inform GPU parallelization of LP/SDP-style relaxations the agent uses (Cohn–Elkies, flag-algebra) — though MCF feasibility itself is not on any of the 23 arena problems.

## Open questions / connections
- Formal worst-case convergence rate of PDR-* — conjectured to depend on graph spectral/topological properties (algebraic connectivity, conductance).
- Why does aggressive-but-inexact (PDR-GDM) beat per-edge-optimal (PDR-ESO)? Suggests local greedy optimality can be globally anti-correlated — relevant heuristic for the agent's own optimizer choices.
- Extends the Awerbuch–Leighton (1993/94) local-control / edge-balancing line and the Goldberg–Tarjan push-relabel pseudo-flow line; relates to electric-flow max-flow (Christiano–Kelner–Madry–Spielman–Teng, Chen–Kyng–Liu–Peng–Sachdeva 2022 almost-linear-time min-cost flow).

## Key terms
multicommodity flow, MCF feasibility, pseudo-flow, potential difference reduction, PDR, edge-separable convex optimization, surrogate majorization, Jensen inequality, projected gradient descent, momentum, KKT conditions, parallel GPU algorithms, push-relabel, electric flow, Awerbuch-Leighton, Goldberg-Tarjan
