---
type: source
kind: paper
title: Faster Sparse Minimum Cost Flow by Electrical Flow Localization
authors: Kyriakos Axiotis, Aleksander Mkadry, Adrian Vladu
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2111.10368
source_local: ../raw/2021-axiotis-faster-sparse-minimum-cost.pdf
topic: general-knowledge
cites:
---

# Faster Sparse Minimum Cost Flow by Electrical Flow Localization

**Authors:** Kyriakos Axiotis, Aleksander Mkadry, Adrian Vladu  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2111.10368

## One-line
First minimum-cost-flow algorithm to break the $O(m^{3/2})$ barrier on sparse graphs with general capacities, costs, and demands, running in $\tilde O(m^{3/2-1/762}\log(U+W))$ time.

## Key claim
Theorem 1.1: given $G(V,E)$ with integer costs $c\in[-W,W]^m$, demand $d\in\mathbb{R}^n$, and capacities $u\in(0,U]^m$, min-cost flow is solved w.h.p. in $\tilde O(m^{3/2-1/762}\log(U+W))$ time, improving on the long-standing $\tilde O(m^{3/2}\log^{O(1)}(U+W))$ bound of Daitch–Spielman (2008).

## Method
Extends the Gao–Liu–Peng (2021) max-flow framework — an interior-point method whose per-iteration electrical-flow solve is accelerated by a dynamic Schur-complement / vertex sparsifier so only a sublinear vertex set $C$ is touched — to the min-cost-flow IPM of Axiotis–Mądry–Vladu (2020). Removes the GLP preconditioning step by switching from $\ell_\infty$ to energy-norm error bounds on demand projections $\pi_C(B^\top q/\sqrt r)$, decomposes the general (full-support) demand into a $C$-supported part plus a low-congestion residual (Lemma 4.3), and introduces "$\varepsilon$-important" edges — those with $R_{\text{eff}}(C,e)\le r_e/\varepsilon^2$ — proving a localization lemma (4.9) showing non-important edges cannot be congested.

## Result
Concretely shaves $m^{1/762}$ off the sparse min-cost-flow exponent. New machinery: a resistance-stability bound along the central path generalizing GLP; Lemma 4.6 bounding projection entries $|\pi_{C\cup\{v\}}^v(B^\top 1_e/\sqrt r)|\le (p^v_{C\cup\{v\}}(u)+p^v_{C\cup\{v\}}(w))\cdot\min(\sqrt{r_e/R_{\text{eff}}(v,e)},1/\sqrt{R_{\text{eff}}(v,e)})$; and Lemma 4.12 controlling demand-projection drift under terminal insertions and resistance updates, so $\pi_C(d)$ only needs occasional exact recomputation.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein problems are min-cost-flow LPs, and the speedup is asymptotic ($m^{1/762}$, irrelevant at problem sizes here). Only tangential relevance: effective-resistance localization and IPM-step stability are the same toolkit used to argue about LP-bound conditioning in sphere-packing / Cohn–Elkies duals, but the paper itself sits in TCS / graph-algorithms territory.

## Open questions / connections
- Can the $1/762$ exponent be pushed toward $1/2$ (closing the gap to nearly-linear), matching the dense-instance $\tilde O(m+n^{1.5})$ of vdBLL+21?
- Extends GLP21 (max flow with $s$-$t$ demand) and DS08 (IPM baseline); cousins to AMV20 ($m^{4/3}$ unit-capacity min-cost flow) and KLS20 (unit-capacity max flow).
- Open: deterministic version (current bound is high-probability via random walks); removal of the oblivious-adversary assumption in the underlying dynamic sparsifier (BBG+20).

## Key terms
minimum cost flow, electrical flow, interior point method, Schur complement, vertex sparsifier, effective resistance, congestion reduction subset, demand projection, important edges, Laplacian solver, central path stability, sparse graph algorithms, Axiotis, Mądry, Vladu, Gao-Liu-Peng
