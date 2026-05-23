---
type: source
kind: paper
title: "Extremal bootstrapping: go with the flow"
authors: S. El-Showk, M. Paulos
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1605.08087
source_local: ../raw/2016-elshowk-extremal-bootstrapping-flow.pdf
topic: general-knowledge
cites:
---

# Extremal bootstrapping: go with the flow

**Authors:** S. El-Showk, M. Paulos  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1605.08087

## One-line
Shows that CFT correlators saturating conformal-bootstrap bounds satisfy a system of Karush-Kuhn-Tucker extremality equations whose linearization lets one *flow* continuously along the bound, replacing repeated expensive optimization with cheap ODE integration.

## Key claim
Extremal solutions to crossing symmetry are characterized by **crossing + saturation + tangency** conditions (eqs. 3.12a-c); perturbing a single seed solution along these equations reproduces full exclusion-plot boundaries at ~100× speedup (40 min seed → 25 s per subsequent point) and extends bootstrap to non-unitary CFTs (first high-precision bootstrap of the generalized free fermion with negative $\Delta_\phi$, first 20 operators correct to 1 part in $10^6$).

## Method
Reformulates the bootstrap as a linear semi-infinite program; at the optimum, KKT conditions force the extremal functional $\Lambda$ to satisfy $\Lambda\cdot v_j = c_{O_j}$ and tangency $\Lambda\cdot\partial_\Delta v_j = 0$ for interior vectors. Linearizing these algebraic equations in a deformation parameter (e.g., external dimension $\Delta_\phi$) yields ODE-like flow equations such as $\delta\Delta_1 = (\Lambda\cdot\delta T)/(\Lambda\cdot\partial_\Delta v_1)$. Error-correction iterations restore extremality; an "upgrading" variant grows a solution from a single random operator up to 75 operators without LP/SDP.

## Result
Three deliverables: (i) flow equations giving locally unique extremal continuations along bound boundaries; (ii) drastic compute reduction — cluster-scale problems become laptop-scale; (iii) extension to non-unitary regime via Gliozzi's determinant method recovered as a special case (no tangency needed when only doubled vectors appear). Convergence analysis: with truncation size $N$, only $\sim N^{1/\alpha}$ operators are reliably recovered, where the operator count grows as $\Delta_*^\alpha$ (e.g., $\alpha=2$ for generalized free fields).

## Why it matters here
General background; no direct arena tie. Most relevant as a **methodology analogue** — the KKT-tangency framing of "saturating bounds → sparse spectrum + functional tangent to active constraints" is structurally identical to equioscillation/Cohn-Elkies LP duality already in the wiki, and the "seed-once, flow-many" pattern could inform how arena solutions are continued across parameter sweeps (e.g., $n$-dependence in packing/kissing families).

## Open questions / connections
- Can the "flow from a seed" pattern (single expensive optimum + cheap continuation) be transplanted to arena LP/SDP problems where each $n$ is currently re-optimized from scratch?
- Singularities along flows (kinks, operator-decoupling discontinuities) signal "interesting" extremal points — analogous diagnostic for arena problems hitting walls?
- Relation to Gliozzi determinant method (§6.1) — extremality without positivity may apply to non-unitary / signed problems where strict LP duality fails.
- Extension to multiple correlators and SDP (deferred to follow-up [29]).

## Key terms
conformal bootstrap, extremal functional method, KKT conditions, semi-infinite programming, LP duality, tangency condition, crossing symmetry, sparse spectrum, generalized free fermion, non-unitary CFT, determinant method, Gliozzi, OPE convergence, kink singularity
