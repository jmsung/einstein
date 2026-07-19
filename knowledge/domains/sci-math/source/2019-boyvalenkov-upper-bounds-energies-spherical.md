---
type: source
kind: paper
title: Upper bounds for energies of spherical codes of given cardinality and separation
authors: P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.00981
source_local: ../raw/2019-boyvalenkov-upper-bounds-energies-spherical.pdf
topic: general-knowledge
cites:
---

# Upper bounds for energies of spherical codes of given cardinality and separation

**Authors:** P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.00981

## One-line
Develops a Delsarte–Yudin-style linear programming framework that produces *universal upper bounds* (UUB) on the potential energy of spherical codes with prescribed cardinality $M$ and maximum inner product $s$, valid simultaneously for all absolutely monotone potentials.

## Key claim
For $n \ge 2$, $M \ge 2$, $s \in [-1,1)$, $h \in \mathrm{AM}([-1,1])$, and $m = m(n,s)$ the Levenshtein interval index, if $f \in U^{n,s}_h$ is the feasible polynomial built by Hermite interpolation of $h$ on the Levenshtein nodes plus a $-\lambda f_m^{(n,s)}$ correction with $\lambda = \max_i g_i/\ell_i$, then $G_h(n,M,s) \le M\bigl(\tfrac{M}{L_m(n,s)} - 1\bigr) f_m^{(h)}(1) + M^2 \sum_{i=0}^{k-1+\varepsilon} \rho_i h(\alpha_i)$ (Theorem 3.2). The nodes $\{\alpha_i\}$ and weights $\{\rho_i\}$ are the Levenshtein 1/$L_m$-quadrature data — **independent of $h$**, hence "universal".

## Method
LP duality in the Delsarte–Yudin spirit: search for a polynomial $f$ with $f(t) \ge h(t)$ on $[-1,s]$ and non-positive Gegenbauer coefficients $f_i \le 0$ for $i \ge 1$; then $E_h(C) \le M(f_0 M - f(1))$ via positive-definiteness of $P_i^{(n)}$. Feasible $f$ is constructed as $f = -\lambda f_m^{(n,s)} + H_{h,T}$ where $f_m^{(n,s)}$ is the Levenshtein polynomial (roots = quadrature nodes $T$) and $H_{h,T}$ is Hermite interpolation of $h$ at $T$; absolute monotonicity + $f_m^{(n,s)} \le 0$ on $[-1,s]$ + Hermite remainder $h-g_T = h^{(m)}(\xi) f_m^{(n,s)}$ give (F1), while $\ell_i > 0$ lets large enough $\lambda$ enforce (F2).

## Result
Tight for orthonormal-basis code $C \in \mathcal{C}(n,n,0)$ (recovers $E_h(C)=n(n-1)h(0)$ exactly). Coincides with the universal lower bound (ULB) — collapsing the "energy strip" to a point — exactly when $M = L_m(n,s)$, i.e. on **universally optimal / sharp configurations** (simplex $C(n,n+1,-1/n)$, cross-polytope $C(n,2n,0)$, 600-cell, $E_8$, Leech, etc.). Numerical tables for kissing configurations $s=1/2$ in dimensions $n=2$–$10$ give ULB/UUB pairs (e.g. $n=4$: 333 / 344; $n=8$: 17721 / 17721 — tight; $n=5$: 765–947 / 840–989). Theorem 3.10 gives a sufficient optimality test via the sign of test functions $R_j^{(n)}(s)$ for $j \ge 2k+\varepsilon$.

## Why it matters here
Directly relevant to Einstein Arena problems in the **sphere-packing / kissing-number / spherical-code family** (P1, P2-class) — provides a *certified two-sided* energy interval for any code with given $(n,M,s)$, which is the structural envelope an LP-based agent should target. The "ULB ⟂ UUB collapse iff $M = L_m(n,s)$" criterion is a clean detector for universally optimal configurations, complementing the Cohn–Elkies / Cohn–Kumar machinery already in the wiki.

## Open questions / connections
- Is the optimality condition $f_1 = 0$ (Remark 3.6) universal across all $h \in \mathrm{AM}$? Authors conjecture yes — links to Bannai–Okuda–Tagami harmonic-index designs.
- "Next-level" UUBs via the Levenshtein-framework-lifted machinery of [arXiv:1906.03062] — analogue of the ULB extension by the same authors.
- Extends Wagner '92 (upper bounds for mean distances on $S^2$) and Yudin '92 (min potential energy); dual to the ULB of Boyvalenkov–Dragnev–Hardin–Saff–Stoyanova (Constr. Approx. 2016).
- Application to structural classification / nonexistence proofs for putative codes whose conjectured energy falls outside the $[\text{ULB}, \text{UUB}]$ strip.

## Key terms
spherical codes, potential energy, Delsarte-Yudin LP, Levenshtein polynomial, Gegenbauer expansion, Hermite interpolation, absolutely monotone potential, universal upper bound, kissing number, universally optimal configuration, 1/N-quadrature, Boyvalenkov-Dragnev-Hardin-Saff-Stoyanova
