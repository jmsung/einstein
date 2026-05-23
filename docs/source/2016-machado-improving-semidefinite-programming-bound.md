---
type: source
kind: paper
title: Improving the Semidefinite Programming Bound for the Kissing Number by Exploiting Polynomial Symmetry
authors: Fabrício Caluza Machado, F. M. D. O. Filho
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1609.05167
source_local: ../raw/2016-machado-improving-semidefinite-programming-bound.pdf
topic: general-knowledge
cites:
---

# Improving the Semidefinite Programming Bound for the Kissing Number by Exploiting Polynomial Symmetry

**Authors:** Fabrício Caluza Machado, F. M. D. O. Filho  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1609.05167

## One-line
Sharpens the Bachoc–Vallentin SDP upper bounds for the kissing number $\tau_n$ in dimensions $n=9,\dots,23$ by exploiting $S_3$-symmetry of the underlying sum-of-squares formulation, enabling higher-degree polynomials at tractable cost.

## Key claim
New rigorously-verified upper bounds for $\tau_n$ at $n=9,\dots,23$, improving on Mittelmann–Vallentin (2010); e.g. $\tau_9 \le 363.675$, $\tau_{10} \le 553.827$, $\tau_{11} \le 869.245$, $\tau_{12} \le 1356.604$, $\tau_{23} \le 123328.397$ (at $d=16$).

## Method
Reformulate Bachoc–Vallentin's three-point SDP bound: the relevant polynomials in the $S_k^n(u,v,t)$ matrices are $S_3$-invariant under permutation of coordinates, and the domain $\Delta$ of feasible inner-product triples is rewritten using $S_3$-invariant generators $s_1=g_1+g_2+g_3$, $s_2=\sum g_ig_j$, $s_3=g_1g_2g_3$, $s_4=g_4$. By Gatermann–Parrilo, any invariant SoS polynomial of degree $\le 2d$ decomposes via three smaller PSD blocks $(V_d^{trv},V_d^{alt},V_d^{std})$ corresponding to the trivial, alternating, and standard irreps of $S_3$, replacing one $\binom{d+3}{3}\times\binom{d+3}{3}$ matrix (816 at $d=15$) by blocks of size $174,102,270$. Solved with SDPA-GMP at 200-bit precision, then verified rigorously via Cholesky + interval arithmetic (MPFI) à la Dostert–Guzmán–Oliveira–Vallentin.

## Result
Bounds tighten monotonically with $d$ (degrees 14, 15, 16 tabled). Symmetry reduction cut the $n=12,d=11$ runtime from 9 days to <12 hours. Computations went up to $d=16$ in ~6 weeks. Underlined improvements over [10] across all $n\in\{9,\dots,23\}$; rigorous certification means the objective value is a provable upper bound on $\tau_n$.

## Why it matters here
Direct content for the kissing-number problem family: this is the strongest practically computable SDP upper bound and the template for SoS+symmetry reduction on spherical codes — a technique transferable to any Einstein Arena problem framed as polynomial optimization on $S^{n-1}$ with permutation symmetry (autocorrelation inequalities, packing, extremal graph density).

## Open questions / connections
- Extends Bachoc–Vallentin 2008 SDP and Mittelmann–Vallentin 2010 high-precision numerics; companion technique to Gatermann–Parrilo SoS symmetry reduction and Bachoc–Gijswijt–Schrijver–Vallentin invariant SDPs.
- Whether further degree $d>16$, multi-point ($k$-point with $k\ge 4$) extensions, or stronger semialgebraic representations of $\Delta$ close the gap to known lattice lower bounds.
- Rigorous-verification recipe (PD slack via $X\to X'+\lambda_{\min}I$, Cholesky over $\mathbb{Q}$, interval-arithmetic residual bound) generalizes to certifying any SDP-derived extremal bound — relevant to triple-verify discipline.

## Key terms
kissing number, spherical codes, semidefinite programming bound, Bachoc-Vallentin, Delsarte LP bound, sum-of-squares, $S_3$ symmetry reduction, Gatermann-Parrilo, invariant polynomials, Jacobi polynomials, SDPA-GMP, rigorous verification, interval arithmetic, three-point bound
