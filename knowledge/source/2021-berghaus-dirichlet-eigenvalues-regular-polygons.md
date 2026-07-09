---
type: source
kind: paper
title: On Dirichlet eigenvalues of regular polygons
authors: D. Berghaus, B. Georgiev, H. Monien, D. Radchenko
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.01057
source_local: ../raw/2021-berghaus-dirichlet-eigenvalues-regular-polygons.pdf
topic: general-knowledge
cites:
---

# On Dirichlet eigenvalues of regular polygons

**Authors:** D. Berghaus, B. Georgiev, H. Monien, D. Radchenko  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.01057

## One-line
Proves the first Dirichlet eigenvalue $\lambda_1(P_N)$ of a regular $N$-gon of area $\pi$ admits an asymptotic expansion in $1/N$ whose coefficients are polynomials in $\lambda_1(D)$ with multiple-zeta-value coefficients, and computes these polynomials explicitly through $n \le 14$.

## Key claim
$\lambda_1(P_N)/\lambda_1 \sim 1 + \sum_{n \ge 3} C_n(\lambda_1)/N^n$ where $C_n \in \mathcal{Z}_n[\lambda]$ (polynomials with weight-$n$ MZV coefficients); first nonzero terms are $4\zeta(3)/N^3 + (12-2\lambda_1)\zeta(5)/N^5 + (8+4\lambda_1)\zeta(3)^2/N^6 + (36-12\lambda_1-12\lambda_1^2)\zeta(7)/N^7 + \cdots$. Theorems 2–3 give a closed generating-function identity for $C_n(0), C_n'(0)$ via $\Gamma(1+z)^2\Gamma(1-2z)/[\Gamma(1-z)^2\Gamma(1+2z)]$ and prove these are rational polynomials in odd zeta values; Conjecture 1 claims $C_n \in \mathcal{Z}_n^{sv}[\lambda]$ (single-valued MZVs), verified for $n \le 14$.

## Method
Asymptotic version of the "method of particular solutions": represent the eigenfunction on $P_N$ via Vekua's integral formula with a holomorphic density $U$, conformally map disk-to-polygon by $f$, and expand the boundary condition $\psi(z)=0$ on $|z|=1$ as a power series in $1/N$. The recursion is closed algebraically using a shuffle-algebra identity (Proposition 1) that decomposes $\mathrm{Li}_u(z)\mathrm{Li}_v(z^{-1})$ into MZV constants plus convergent polylog pieces, which solves the harmonic Dirichlet problem for boundary data of polylog form. Implemented symbolically in SAGE ($n \le 12$) and parallel Julia ($n \le 14$); MZV Datamine used to simplify.

## Result
The first 10 coefficients $C_1, \ldots, C_{10}$ involve only odd zeta values $\zeta(2m+1)$ and their products; $C_{11}$ introduces the single-valued MZV $\zeta^{sv}_{3,5,3} := 2\zeta(3,5,3) - 2\zeta(3)\zeta(3,5) - 10\zeta(3)^2\zeta(5)$, and assuming standard algebraic-independence conjectures this is genuinely outside the odd-zeta-polynomial ring. Confirms the conjectural $C_7, C_8$ from [Jones, arXiv:1712.06082]. As corollary: since $\zeta(3)>0$, the Pólya–Szegő-type monotonicity conjecture $\lambda_1(P_N) > \lambda_1(P_{N+1})$ holds for all sufficiently large $N$. The normalizing factor coincides with Virasoro's closed bosonic string amplitude.

## Why it matters here
General background; no direct arena tie. Relevant only as a methodology exemplar — high-precision symbolic asymptotics + numerical linear-regression conjecture (here for $C_7, C_8$) being later proved is the same pattern that could close arena problems like P5/P11/P14 where high-dps polish reveals algebraic structure. The MZV/single-valued-MZV machinery may be a research seed if any arena problem reduces to integrals over harmonic polylog boundary data.

## Open questions / connections
- Prove Conjecture 1: $C_n \in \mathcal{Z}_n^{sv}[\lambda]$ for all $n$ (numerically verified through $n=16$).
- Explain the appearance of Virasoro's closed bosonic string amplitude in the generating function — coincidence or structural?
- Extend to non-radial eigenvalues ($J_m(x)$ roots for $m \ne 0$) and to other regular-domain perturbations (e.g., regular polytopes in higher dimensions).
- Tighten the Pólya–Szegő monotonicity conjecture for small $N$ (asymptotic argument only handles $N$ large).

## Key terms
Dirichlet eigenvalue, regular polygon, Bessel function $J_0$, multiple zeta values, single-valued MZV, asymptotic expansion, method of particular solutions, Vekua representation, shuffle algebra, polylogarithm, Faber-Krahn, Pólya-Szegő conjecture, Wilf-Zeilberger, Ramanujan-Dougall
