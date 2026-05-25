---
type: source
kind: paper
title: Dual linear programming bounds for sphere packing via modular forms
authors: Henry Cohn, Nicholas Triantafillou
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1909.04772v2
source_local: ../raw/2019-cohn-dual-linear-programming-bounds.pdf
topic: general-knowledge
cites: 
---

# Dual linear programming bounds for sphere packing via modular forms

**Authors:** Henry Cohn, Nicholas Triantafillou  ·  **Year:** 2019  ·  **Source:** http://arxiv.org/abs/1909.04772v2

## One-line
Constructs feasible points in the *dual* of the Cohn–Elkies linear program using modular forms, producing rigorous lower bounds on the LP bound itself in dimensions 12, 16, 20, 28, 32 — proving the LP bound cannot be sharp there.

## Key claim
The Cohn–Elkies LP bound for sphere packing in $\mathbb{R}^{16}$ exceeds $1.7 \times$ the Barnes–Wall density, and in $\mathbb{R}^{12}$ exceeds $1.686 \times$ the Coxeter–Todd density — so neither lattice can be proven optimal by LP alone. Analogous separations are obtained in dimensions 20, 28, 32.

## Method
A Voronoi-style summation formula (Prop. 2.2) shows that for $g \in M_k(\Gamma_1(N))$ with $q$-expansion $\sum a_n q^n$ and its Atkin–Lehner image $\tilde g = \sum b_n q^n$, the distributions $\sum a_n \delta_{\sqrt n}$ and $(2/\sqrt N)^{d/2}\sum b_n \delta_{2\sqrt{n/N}}$ are Fourier duals. Plugging these into Cohn's dual formulation (Prop. 2.1) reduces the dual LP to a finite LP over $M_k(\Gamma_0(N))$ with constraints $a_0=1$, $b_0>0$, $a_n=0$ for $1\le n<T$, and $a_n,b_n\ge 0$. Nonnegativity of the full $q$-series is certified by an Eisenstein-vs-cusp split using Deligne/Weil bounds $|c_n|\le n^{k/2}\sum|x_h|$ against Eisenstein lower bounds $e_n\ge n^{k-1} r_g$.

## Result
Rigorous center-density lower bounds on the LP bound (Table 6.1): dim 12 → 0.062446 (vs LP upper 0.062742, record 0.037037), dim 16 → 0.106284 (vs 0.107059, record 0.0625), dim 20 → 0.260996, dim 28 → 4.591741, dim 32 → 28.086665. The dim-16 $N=4$, $T=3$ case recovers the extremal theta series $1+7680q^3+4320q^4+\dots$, giving lower bound $38/2^{16}\approx 0.10011$; pushing to $N=96$ corresponds to "minimal norm 3.022" vs conjectured true LP optimum of minimal norm $\approx 3.02525931\dots$.

## Why it matters here
Directly informs LP-duality / Cohn–Elkies / Viazovska modular-form territory — relevant to any arena problem framed as an LP-bound on packing/kissing/autocorrelation (P1 sphere packing, kissing-number problems, and any Cohn–Elkies-style auxiliary-function setups). Adds the dual-LP perspective: how to *certify* that an LP bound is *not* tight, which is the inverse of the usual "find a better magic function" direction the wiki tends to cover.

## Open questions / connections
- Closing the primal–dual gap to $1+10^{-10}$ may require $N\sim 10^{10}$ — modular forms may not be the right tool; cf. Torquato–Stillinger [33] and Scardicchio–Stillinger–Torquato [30] for alternative high-dim dual approaches.
- Extension to odd dimensions / dimensions $\not\equiv 0 \pmod 4$ via half-integral weight forms on $\Gamma_1(N)$ — outlined but not implemented.
- Could one prove LP non-sharpness in $d=3$? Would just need any dual bound exceeding $\pi/\sqrt{18}$ — none known. Also: dual bounds for the de Laat–Oliveira–Vallentin [22] refinement of LP.

## Key terms
Cohn–Elkies linear programming bound, dual LP, sphere packing, modular forms, Atkin–Lehner involution, Voronoi summation, Eisenstein series, Barnes–Wall lattice, Coxeter–Todd lattice, Viazovska, $\Gamma_0(N)$, extremal theta series, Hecke L-function, Deligne–Weil bound
