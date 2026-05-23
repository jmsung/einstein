---
type: source
kind: paper
title: A Faster Cutting Plane Method and its Implications for Combinatorial and Convex Optimization
authors: Y. Lee, Aaron Sidford, S. Wong
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1508.04874
source_local: ../raw/2015-lee-faster-cutting-plane-method.pdf
topic: general-knowledge
cites:
---

# A Faster Cutting Plane Method and its Implications for Combinatorial and Convex Optimization

**Authors:** Y. Lee, Aaron Sidford, S. Wong  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1508.04874

## One-line
A new cutting plane method for convex feasibility with a separation oracle, improving Vaidya's 25-year-old running time and yielding faster algorithms for SDP, submodular minimization, matroid intersection, and submodular flow.

## Key claim
Given a separation oracle for a convex $K \subset \mathbb{R}^n$ in a box of radius $R$, the algorithm finds a point in $K$ or certifies $K$ contains no ball of radius $\epsilon$ in expected $O(n \log(nR/\epsilon))$ oracle calls plus $O(n^3 \log^{O(1)}(nR/\epsilon))$ additional time — replacing Vaidya's $n^{\omega+1}$ overhead with $n^3$ when $R/\epsilon = \mathrm{poly}(n)$.

## Method
A hybrid barrier (volumetric + logarithmic) center is maintained, à la Vaidya/Atkinson-Vaidya, but updates tolerate noisy leverage scores. The core new tool is a low-variance unbiased estimator for changes in leverage scores (Section 7.1) combined with a "stochastic chasing-0 game" (Section 7.2), letting each iteration avoid the $n^\omega$ inverse-maintenance cost. Reductions then port this to SDP duality, intersection-of-convex-sets (matroid intersection, submodular flow), and submodular function minimization via the Lovász extension.

## Result
- Cutting plane: $O(n \cdot SO \log\kappa + n^3 \log^{O(1)} \kappa)$, $\kappa = nR/\epsilon$.
- SDP ($m \times m$, $n$ constraints, $S$ nonzeros): $\tilde{O}(n(n^2 + m^\omega + S))$.
- Submodular minimization: weakly poly $O(n^2 \log nM \cdot EO + n^3 \log^{O(1)} nM)$; strongly poly $O(n^3 \log^2 n \cdot EO + n^4 \log^{O(1)} n)$ — both ~$\Omega(n^2)$ faster than prior best.
- Matroid intersection: first quadratic query complexity, $O(n^2 T_{ind} \log nM)$ / $O(nr T_{rank} \log n \log nM)$.

## Why it matters here
General background; no direct arena tie. Relevant only as a theoretical reference for LP/SDP solver complexity — could inform routing decisions for SDP-bound problems (e.g. flag-algebra SDPs on extremal-graph problems like P-family), but the existing wiki finding `findings/sdp-relaxation-uselessness` already argues SDP relaxations are typically loose for the geometric arena problems regardless of solver speed.

## Open questions / connections
- Can the weakly polynomial SFM bound be tightened to $O(n^2 \log M \cdot EO + n^3 \log^{O(1)} n \cdot \log M)$?
- Is $\Theta(n^2)$ oracle calls the true optimum for SFM (lower bound from duality already gives $n^2$)?
- Does the noise-tolerant leverage-score estimator transfer to interior-point LP solvers (Lee-Sidford follow-ups)?
- Can the hybrid-barrier idea improve practical analytic-center cutting plane (ACCPM) used in non-smooth convex optimization?

## Key terms
cutting plane method, separation oracle, Vaidya, volumetric barrier, hybrid barrier, leverage scores, feasibility problem, semidefinite programming, submodular function minimization, matroid intersection, submodular flow, Lovász extension, convex optimization, interior point method
