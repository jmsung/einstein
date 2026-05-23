---
type: source
kind: paper
title: The sphere packing problem in dimension 24
authors: Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, Maryna Viazovska
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1603.06518v3
source_local: ../raw/2016-cohn-sphere-packing-problem-dimension.pdf
topic: general-knowledge
cites: 
---

# The sphere packing problem in dimension 24

**Authors:** Henry Cohn, Abhinav Kumar, Stephen D. Miller, Danylo Radchenko, Maryna Viazovska  ·  **Year:** 2016  ·  **Source:** http://arxiv.org/abs/1603.06518v3

## One-line
Constructs the Cohn–Elkies magic function in $\mathbb{R}^{24}$ from quasimodular forms, proving the Leech lattice is the densest sphere packing — and the unique optimal periodic packing — in 24 dimensions.

## Key claim
The Leech lattice attains the optimal sphere packing density $\pi^{12}/12! \approx 0.0019295743$ in $\mathbb{R}^{24}$, and it is the unique densest periodic packing up to scaling and isometry (Theorem 1.1).

## Method
Linear programming bounds of Cohn–Elkies [2]: build a Schwartz radial $f:\mathbb{R}^{24}\to\mathbb{R}$ with $f(0)=\hat f(0)=1$, $f\le 0$ outside $|x|\ge 2$, and $\hat f\ge 0$. Following Viazovska's $\mathbb{R}^8$ construction, the authors assemble $f$ as a linear combination of two radial Fourier eigenfunctions: a $+1$-eigenfunction $a(r)$ built from a weakly holomorphic quasimodular form $\varphi$ of weight $-8$, depth $2$ for $SL_2(\mathbb{Z})$, and a $-1$-eigenfunction $b(r)$ built from a weakly holomorphic modular form $\psi_I$ of weight $-10$ for $\Gamma(2)$. The required sign inequalities on $[0,\infty)$ are verified via Sturm's theorem on truncated $q$-series with explicit polynomial coefficient bounds (replacing the interval arithmetic used in dim 8).

## Result
The function $f = -\tfrac{\pi i}{113218560}a - \tfrac{i}{262080\pi}b$ has $f$ and $\hat f$ vanishing (to order $\ge 2$) exactly at the Leech vector lengths $\sqrt{2k}$, $k\ge 2$, matching the Cohn–Miller conjectured Taylor coefficients $-14347/5460$ and $-205/156$ [4]. This forces equality in the LP bound at the Leech density, and the simple-root condition at $r=2$ gives uniqueness among periodic packings (Section 8 of [2]). Three appendix lemmas establish $\varphi(it)<0$, $\varphi(it)-432\psi_S(it)/\pi^2>0$, and an asymptotic-corrected positivity for $B(t)$ on $t\ge 1$.

## Why it matters here
Canonical second example (after dim 8) of the **Cohn–Elkies magic function** program — directly relevant to any Einstein Arena problem framed as LP bounds with radial Fourier sign conditions; supplies the modular-forms / quasimodular-forms toolkit (Eisenstein/theta Ansatz → contour-shift → eigenfunction). Extends prior wiki content on Viazovska's dim-8 proof to the $\Gamma(2)$ / depth-2 quasimodular setting.

## Open questions / connections
- What dimensions admit an analogous Cohn–Elkies optimal auxiliary function? Only $n=1,8,24$ are known; the construction depends on a sharp lattice (Leech / $E_8$).
- Extension to universally optimal energy minimization in dim 24 (followed up by Cohn–Kumar–Miller–Radchenko–Viazovska 2019).
- The Ansatz space ($\Delta^2\varphi$ holomorphic quasimodular of weight 16, depth 2; 5-dimensional) is determined by asymptotic constraints (2.3)–(2.4) — does the same recipe identify candidate magic functions in other dimensions?
- Sturm's-theorem + truncated $q$-series with polynomial coefficient bounds is a reusable computer-algebra verification pattern (no interval arithmetic needed).

## Key terms
Leech lattice, sphere packing, Cohn–Elkies linear programming bound, magic function, Fourier eigenfunction, quasimodular form, weakly holomorphic modular form, Eisenstein series, theta functions, $\Gamma(2)$, Sturm's theorem, Viazovska, dimension 24
