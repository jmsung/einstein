---
type: source
kind: paper
title: Composite Sorting
authors: J. Boerma, A. Tsyvinski, Ruodu Wang, Zhenyuan Zhang
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2303.06701
source_local: ../raw/2023-boerma-composite-sorting.pdf
topic: general-knowledge
cites:
---

# Composite Sorting

**Authors:** J. Boerma, A. Tsyvinski, Ruodu Wang, Zhenyuan Zhang  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.06701

## One-line
An assignment/optimal-transport model where mismatch cost is concave in the worker–job skill gap, $c(x,z)=|x-z|^\zeta$ with $\zeta\in(0,1)$, producing a new "composite" sorting pattern that is neither purely positive nor purely negative.

## Key claim
With concave skill-gap costs, optimal assignments obey two structural laws — maximize perfect pairs and forbid intersecting arcs — which decompose the problem into independent "layers" of an underqualification measure $H$; when $F,G$ are mixtures of $n$ and $m$ normals, each layer contains at most $n+m-1$ pairs (Theorem 1), and the dual potentials admit a regional hierarchical construction (Theorems 2–4) computable in $O(N^{2.5}(\log\log N)^{3/2})$ for empirical uniform measures.

## Method
Optimal transport (Monge–Kantorovich) with the non-supermodular, non-submodular cost $c(x,z)=\tfrac{1}{\zeta_p}(z-x)_+^{\zeta_p}+\tfrac{1}{\zeta_u}(x-z)_+^{\zeta_u}$ derived from a Stigler/Laffont–Tirole fixed-investment model. The primal analysis uses cyclical monotonicity → no-intersecting-pairs → layer decomposition via $H(t)=F(t)-G(t)$, then a Bellman recursion $V_{i,j}=\min_k c(s_i,s_k)+V_{i+1,k-1}+V_{k+1,j}$ on alternating worker/job sequences (Aggarwal–Bar-Noy–Khuller–Kravets–Schieber 1995; Nechaev–Sobolevski–Valba 2013). The complexity reduction for normal mixtures invokes Pólya frequency functions and variation-diminishing transforms (Schoenberg, Karlin); the empirical-measure runtime bound uses Brownian-bridge local-time estimates (Khoshnevisan 1992; Bass–Khoshnevisan 1995; Csörgő–Shi–Yor 1999).

## Result
Layer-bound: for normal-mixture $F$ (n components) and $G$ (m components), each layer has $\le n+m-1$ pairs, making large-type assignment tractable. Dual: equilibrium wages decompose into nested skill regions where relative wages depend only on local output and matches; the hierarchical assembly preserves global feasibility. Comparative statics (Theorem 5): less-concave cost ⇒ sorting more positive in concordance order; (Theorem 6) a threshold concavity yields "layered positive sorting" inside each layer, distinct from overall positive sorting. Anderson–Smith (2024) up-crossing summed rectangular synergy fails here (counterexample with synergies $\{0.09,-0.19,0.30\}$ at $\zeta\in\{0.2,0.5,0.8\}$).

## Why it matters here
General background; no direct arena tie. The concave-distance OT framework, no-intersecting-arc lemma, and layer decomposition via $H=F-G$ are structurally analogous to 1D matching/transport heuristics that appear in discrete-geometry packing arguments and could inform thinking about constraints with concave-cost penalties, but no Einstein Arena problem currently maps to it.

## Open questions / connections
- Extension of the layer/no-crossing structure to higher-dimensional concave OT (Gangbo–McCann 1996, McCann 1999) — does the $n+m-1$ bound generalize?
- Connection to Ottolini–Steinerberger (2023) random-assignment scaling for concave costs — could similar scaling constants bound average mismatch on random configurations?
- When do the cyclical-monotonicity + no-intersection conditions yield closed-form dual potentials beyond normal mixtures (e.g., heavy-tailed $F,G$)?
- Relation to Echenique–Root–Sandomirskiy (2025) stable NTU matching and Pomatto–Strack–Tamuz (2020) variation-diminishing methods for stochastic dominance.

## Key terms
optimal transport, concave cost, Monge-Kantorovich duality, composite sorting, assignment problem, cyclical monotonicity, no intersecting pairs, Pólya frequency functions, variation diminishing, layer decomposition, underqualification measure, Brownian bridge local time, Gangbo-McCann, Schoenberg, Karlin
