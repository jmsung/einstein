---
type: source
kind: paper
title: Convex optimization
authors: Stephen P. Boyd, L. Vandenberghe
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.01946
source_local: ../raw/2010-boyd-convex-optimization.pdf
topic: general-knowledge
cites:
---

# Convex optimization

**Authors:** Stephen P. Boyd, L. Vandenberghe  ·  **Year:** 2010  ·  **Source:** https://arxiv.org/abs/2106.01946

## One-line
A graduate textbook (MIPT lecture notes, Vorontsova–Hildebrand–Gasnikov–Stonyakin 2021, arXiv:2106.01946 — note: metadata-attributed to Boyd/Vandenberghe but contents are the Russian MIPT text) covering convex analysis, conic/robust optimization, and modern accelerated first-order and interior-point methods.

## Key claim
Convex optimization stands on three legs — convex analysis, problem modeling, and numerical methods — and within that frame the book consolidates: KKT/Lagrange duality, Farkas-type alternative theorems, conic programming (LP/SOCP/SDP and non-symmetric cones), robust optimization (matrix-cube theorem), self-concordant barriers (interior-point with $O(\sqrt{\nu}\log(1/\varepsilon))$ iteration complexity), and the accelerated meta-algorithm / inexact-oracle theory for first-order methods with $(\delta, L)$-models.

## Method
Standard convex-analytic toolkit (separation theorems, Demyanov–Danskin, Schur complement, implicit function theorem) used to derive duality; conic representation + Yannakakis-type lifts for modeling; self-concordant barrier theory for interior-point; black-box oracle model with $(\delta, L)$-inexact gradient/model for first-order complexity; ellipsoid / center-of-gravity / Frank–Wolfe / proximal / Catalyst / tensor methods for specific regimes.

## Result
Compendium rather than single result: $\nu$-self-concordant barrier gives polynomial IPM; universal accelerated method achieves optimal rates across Hölder classes; tensor methods with order-$p$ derivatives reach $O(k^{-(3p+1)/2})$ on smooth convex problems; semidefinite-representable approximations of transcendental constraints; matrix-cube theorem bounds tractability of robust SDP. SOS / moment relaxations (Lasserre) framed as the convex-lift route to polynomial optimization; Goemans–Williamson 0.878 MaxCut SDP cited.

## Why it matters here
General background; broad reference rather than a single arena-targeted result. Directly informs: SDP/SOS/moment relaxations (P1 sphere-packing LP-bound family, P15/P16 autocorrelation), conic-programming framing for `findings/sdp-relaxation-uselessness`, accelerated-method choice in `techniques/compute-router`, and inexact-oracle reasoning when local evaluators diverge from arena truth (triple-verify backbone).

## Open questions / connections
- Yannakakis / cone-factorization lower bounds — when is a convex set NOT SDP-representable? Relevant if SDP lifts of arena problems hit lift-rank walls.
- $(\delta, L)$-inexact model: quantitative gap between local-evaluator inexactness and arena verifier — formal route to bound triple-verify drift.
- Tensor methods and contracting proximal — untested in this repo; potential lever for problems where Hessian is cheap but gradient noisy.
- Lasserre hierarchy convergence rate vs degree — practical cutoff for moment relaxations on arena polynomial problems.

## Key terms
convex optimization, KKT conditions, Lagrange duality, Farkas lemma, conic programming, semidefinite programming, SDP, robust optimization, matrix cube theorem, self-concordant barrier, interior-point method, accelerated gradient method, Frank–Wolfe, ellipsoid method, inexact oracle, Lasserre hierarchy, sum of squares, moment relaxation, Yannakakis, Wasserstein, Goemans–Williamson, Nesterov, Nemirovski, Boyd, Vandenberghe
