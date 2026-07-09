---
type: source
kind: paper
title: Dual Linear Programming Bounds for Sphere Packing via Discrete Reductions
authors: Rupert Li
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2206.09876
source_local: ../raw/2022-li-dual-linear-programming-bounds.pdf
topic: general-knowledge
cites:
---

# Dual Linear Programming Bounds for Sphere Packing via Discrete Reductions

**Authors:** Rupert Li  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2206.09876

## One-line
A general method to lower-bound the Cohn–Elkies LP for sphere packing by restricting feasible functions $f:\mathbb{R}^d\to\mathbb{R}$ to a finite torus $\mathbb{Z}_m^d$, yielding a tractable finite-dimensional dual whose feasible points prove non-sharpness of Cohn–Elkies in dimensions $d=3,4,5$.

## Key claim
The Cohn–Elkies LP bound is **provably not sharp** in $d=3,4,5$ (new) — joining the previously-known non-sharp dimensions $\{12,16\}$. For $6\le d\le 13$ except $d=8$, the dual bound also exceeds the best known packing densities (a weaker but still informative result).

## Method
**Discrete reduction by composed restrictions.** Given a Cohn–Elkies feasible $f:\mathbb{R}^d\to\mathbb{R}$, restrict $f\mapsto g=f|_{\mathbb{Z}^d}$ (via Poisson summation on $\widehat f$ over $\mathbb{T}^d$), then restrict $\widehat g \mapsto \widehat g_m = \widehat g|_{(1/m)\mathbb{Z}^d/\mathbb{Z}^d}$, yielding $g_m:\mathbb{Z}_m^d\to\mathbb{R}$ with weakly-decreased objective (Theorem 3.2, requires $m\ge 2r$). The resulting **discrete Cohn–Elkies LP on $\mathbb{Z}_m^d$** is finite-dimensional, so classical strong LP duality applies; feasible duals are found numerically, rounded to rationals (with $\widehat\lambda(y)\ge\varepsilon\approx 10^{-10}$ buffer), then verified exactly via rational + interval arithmetic. $G_d=\mathbb{Z}_2^d\rtimes S_d$-symmetrization (sign-flip + permutation) reduces variables to $\mathbb{Z}_m^d/G_d$.

## Result
Specific dual bounds on $\delta_d$:
- $d=3$: bound $>$ Cohn–de Laat–Salmon UB (non-sharp); $d=4$: $>0.12914461$ (m=30, r=√66); $d=5$: $>0.09826308$ (m=24, r=√34).
- $d=6$: $>0.07632412$; $d=7$: $>0.06374745$; $d=9$: $\ge 1/20=0.05$ (m=4, r=2, closed-form); $d=10,11,12$: $\ge 1/24 \approx 0.04167$ (all m=4, r=2).
- **General closed-form (Cor 9.2):** for odd $d=2k+1\ge 5$, dual bound $\ge \frac{1}{2(d+1)}$ via an explicit five-support $\widehat\lambda$ on $\mathbb{Z}_4^d/G_d$ involving Krawtchouk polynomials $K_b(k;2k)$; gives $d=13$: $\ge 1/28 > 0.0357$.

## Why it matters here
Direct relevance to **Einstein Arena P1 / P2 (sphere-packing-family)** — supplies an exact-arithmetic *dual* certificate construction that *complements* the primal magic-function approach. Adds a technique the wiki's Cohn–Elkies / equioscillation pages don't currently cover: discrete reduction is computer-tractable in low $d$ where the modular-form method of Cohn–Triantafillou struggles, so it's the natural low-$d$ companion to those concepts. Also: the rational-rounding + interval-verification recipe (ε-buffered LP solution → exact rational µ → certified $\widehat\lambda\ge 0$) is a reusable verification pattern for any "LP-bound is real" question — fits triple-verify.

## Open questions / connections
- Does the discrete Cohn–Elkies bound on $\mathbb{Z}_m^d$ **converge** to the continuous Cohn–Elkies bound as $m,r\to\infty$? Rate of convergence?
- Can discrete dual solutions on $\mathbb{Z}_m^d$ be **lifted** back to continuous dual measures on $\mathbb{R}^d$, suggesting structured ansätze for the (otherwise intractable) continuous dual?
- Extends Cohn–Triantafillou (2021) modular-form duals (good for high $d$, multiples of 4) to a method impartial to $d\bmod 4$ — complementary; modular forms scale better in high $d$, discrete reduction wins in low $d$.
- Relates to author's own work [19] on unique optima of the Delsarte LP; $m=2$ case recovers binary Delsarte.

## Key terms
Cohn-Elkies linear program, sphere packing, dual linear programming bound, discrete reduction, Poisson summation, Fourier transform on $\mathbb{Z}_m^d$, LP duality, Krawtchouk polynomial, Delsarte bound, modular forms, $G_d$-invariance, magic function, non-sharpness, Viazovska, interval arithmetic verification, center density
