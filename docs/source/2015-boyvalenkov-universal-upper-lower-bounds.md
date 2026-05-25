---
type: source
kind: paper
title: Universal upper and lower bounds on energy of spherical designs
authors: P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.07837
source_local: ../raw/2015-boyvalenkov-universal-upper-lower-bounds.pdf
topic: general-knowledge
cites:
---

# Universal upper and lower bounds on energy of spherical designs

**Authors:** P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.07837

## One-line
Derives a two-sided "strip" — Delsarte-style linear programming lower bounds and (new) LP upper bounds — on the potential energy $E(n,C;h)$ of spherical $\tau$-designs of fixed dimension $n$, strength $\tau$, and cardinality $N$.

## Key claim
For $N\in(D(n,\tau),D(n,\tau+1)]$ and absolutely monotone $h$, $L(n,N,\tau;h)\ge N^2\sum_i\rho_i h(\alpha_i)$ (odd $\tau=2k-1$) or $N^2\sum_i\gamma_i h(\beta_i)$ (even $\tau=2k$), where $\{\alpha_i,\rho_i\}/\{\beta_i,\gamma_i\}$ come from Levenshtein quadrature; these are optimal among degree-$\le\tau$ LP polynomials. A parallel upper bound (Thm. 3.6) uses polynomials $g\ge h$ on $I$ with $g_i\le 0$ for $i\ge\tau+1$, yielding $E\le N(g_0 N-g(1))$.

## Method
Linear programming on Gegenbauer expansions $f=\sum f_i P_i^{(n)}$ combined with Levenshtein's quadrature formulas (12)–(13) at the design's strength. Lower bounds use Hermite interpolants of $h$ at the Levenshtein nodes $\alpha_i/\beta_i$ (Lemma 3.3 gives $F\le h$ from the Hermite error formula with $h^{(\tau+1)}\ge 0$). Upper bounds invert the sign condition on Gegenbauer coefficients ($g_i\le 0$ for $i\ge\tau+1$) and exploit structural bounds on $u(n,N,\tau),\ell(n,N,\tau)$ from Lemmas 2.1–2.4 to restrict the interval $I$.

## Result
Universal bounds matching Cohn–Kumar's universally-optimal-code framework but specialized to designs. Test functions $Q_j(n,s)=1/N+\sum\rho_i P_j^{(n)}(\alpha_i)$ (Thm. 4.3) give necessary-and-sufficient conditions for improving the odd-$\tau$ LP bound via higher-degree polynomials; Corollary 4.5 shows improvement is possible for all $n\ge 3$, $k\ge 9$ with $n\le k_0$. Asymptotic main term $L(n,N,\tau;h)\ge h(0)N^2+o(N^2)$ when $N/n^{k-1}\to 2/(k-1)!+\gamma$ (Thm. 6.1), matched by Kerdock-code Euclidean realizations achieving $h(0)N^2+O(N^{3/2})$. For 2-designs the strip collapses at $N=n+1,n+2$ — recovering Sali's rigidity result for Mimura designs.

## Why it matters here
Directly informs energy-minimization problems in the arena (sphere packing, kissing-number-adjacent configurations, autocorrelation) where the optimizer needs both lower bounds (certificates of "we can't do better than X") and upper bounds (certificates of "no design beats Y") — the Hermite-interpolant LP construction is the canonical recipe for both. Connects to existing wiki content on LP duality, Cohn–Elkies, Levenshtein bounds, and triple-verify (analytical bound = check #3).

## Open questions / connections
- Whether the even-$\tau$ LP-on-$[\ell,u]$ bound (Thm. 4.1) is always tighter than higher-degree-polynomial bounds (Remark 4.6 — conjecture, open).
- Optimal choice of interpolation points for Thm. 4.1 (authors flag forthcoming work).
- Extends Cohn–Kumar (2007) universal optimality from sharp codes to general designs; relates to Bondarenko–Radchenko–Viazovska on asymptotically optimal design cardinality.
- Whether Kerdock-style constructions are asymptotically energy-optimal beyond the cardinality-optimality already shown by Levenshtein.

## Key terms
spherical designs, potential energy, linear programming bound, Delsarte-Goethals-Seidel bound, Levenshtein bound, Gegenbauer polynomials, Hermite interpolation, quadrature formula, absolutely monotone potential, universal optimality, Cohn-Kumar, Mimura designs, Kerdock codes, Jacobi polynomials, test functions
