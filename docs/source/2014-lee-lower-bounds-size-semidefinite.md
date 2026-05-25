---
type: source
kind: paper
title: Lower Bounds on the Size of Semidefinite Programming Relaxations
authors: James R. Lee, P. Raghavendra, David Steurer
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1411.6317
source_local: ../raw/2014-lee-lower-bounds-size-semidefinite.pdf
topic: general-knowledge
cites:
---

# Lower Bounds on the Size of Semidefinite Programming Relaxations

**Authors:** James R. Lee, P. Raghavendra, David Steurer  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1411.6317

## One-line
Proves the first super-polynomial lower bounds on the size of general (non-symmetric) SDP relaxations for explicit combinatorial polytopes (cut, TSP, stable set) and for approximating max-CSPs.

## Key claim
The cut, TSP, and stable set polytopes on $n$ vertices have positive-semidefinite rank $\geq 2^{n^\delta}$ for some constant $\delta > 0$; specifically $\mathrm{rk}_{\mathrm{psd}}(\mathrm{corr}_n) \geq 2^{\Omega(n^{2/13})}$, $\mathrm{rk}_{\mathrm{psd}}(\mathrm{cut}_n) \geq 2^{\Omega(n^{2/13})}$, $\mathrm{rk}_{\mathrm{psd}}(\mathrm{tsp}_n) \geq 2^{\Omega(n^{1/13})}$. Polynomial-size SDP relaxations cannot beat a $7/8$-approximation for max 3-SAT.

## Method
General technique for lower-bounding the *psd rank* of a matrix by relating arbitrary SDP factorizations to those arising from the sum-of-squares (Lasserre) hierarchy. The core machinery uses **quantum entropy maximization** and **matrix multiplicative weights** (online convex optimization) to "learn" an approximate low-degree sos formulation on a subset of variables from any given small SDP factorization. A degree-reduction argument then converts general PSD factorizations into low-degree sos certificates, so sos-degree lower bounds (Grigoriev–Schoenebeck) transfer to general SDP size lower bounds.

## Result
Main bridge theorem: for $f:\{0,1\}^m \to \mathbb{R}_+$ with $\deg_{\mathrm{sos}}(f) = d+2$, the lifted matrix $M^n_f(S,x) := f(x_S)$ satisfies $\mathrm{rk}_{\mathrm{psd}}(M^n_f) \geq C \cdot (n/\log n)^{d/4}$. Consequence (Thm 6.2/6.4): for any boolean CSP, if degree-$d$ sos fails a $(c,s)$-approximation, no SDP of size $o((n/\log n)^{d/4})$ achieves it. Yields $7/8$ optimality for max 3-SAT under SDP of size $n^{\alpha \log n / \log \log n}$, and conditional ($\alpha_{GW} \approx 0.878$) optimality of Goemans–Williamson for max-cut among polynomial-size SDPs.

## Why it matters here
General background; no direct arena tie. Relevant only as theoretical context for why SDP/sos relaxations have fundamental limits — informs the wiki's `findings/sdp-relaxation-uselessness` line of reasoning for problems where SDP bounds appear loose (P1 sphere packing, autocorrelation problems where Cohn–Elkies-style LPs dominate).

## Open questions / connections
- Extends Yannakakis (LP extension complexity) and Fiorini et al. / Rothvoß (LP lower bounds for TSP/matching) to the SDP setting via psd rank.
- Does the $2^{\Omega(n^{2/13})}$ bound for $\mathrm{corr}_n$ tighten toward the conjectured $2^{\Omega(n)}$ matching the nonnegative-rank bound?
- Does the sos-optimality theorem extend beyond boolean CSPs to continuous optimization (e.g., the polynomial-optimization problems arising in arena packing/autocorrelation)?
- Connection to quantum communication complexity: psd rank equals a model of one-way quantum communication (Fiorini et al.) — potential cross-application.

## Key terms
positive semidefinite rank, psd rank, sum-of-squares hierarchy, Lasserre hierarchy, semidefinite extension complexity, spectrahedral lift, correlation polytope, cut polytope, TSP polytope, stable set polytope, max-CSP approximation, max 3-SAT 7/8 barrier, Goemans-Williamson, matrix multiplicative weights, quantum entropy maximization, Yannakakis factorization, nonnegative rank, unique disjointness, Grigoriev-Schoenebeck, pseudo-density, junta degree, Positivstellensatz, Lee Raghavendra Steurer
