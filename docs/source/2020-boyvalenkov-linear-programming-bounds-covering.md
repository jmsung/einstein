---
type: source
kind: paper
title: Linear Programming Bounds for Covering Radius of Spherical Designs
authors: P. Boyvalenkov, Maya M. Stoyanova
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2007.05599
source_local: ../raw/2020-boyvalenkov-linear-programming-bounds-covering.pdf
topic: general-knowledge
cites:
---

# Linear Programming Bounds for Covering Radius of Spherical Designs

**Authors:** P. Boyvalenkov, Maya M. Stoyanova  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2007.05599

## One-line
Sharpens lower and upper bounds on the covering radius $\rho(C)$ of spherical $\tau$-designs $C \subset S^{n-1}$ as a function of dimension, strength, and cardinality, improving the cardinality-blind Fazekas–Levenshtein bound.

## Key claim
For a spherical $2k$-design $C$ with $|C| > D(n,2k)$ and any $y$ realizing the covering radius, $\rho(C) \ge t^{0,\ell}_{k,k}$ — the largest zero of a new orthogonal polynomial $P^{0,\ell}_k(t)$ built from a signed measure $d\mu_\ell(t) = -\ell^{-1}(t-\ell)\,d\mu(t)$ positive-definite up to degree $k-1$; this strictly improves Fazekas–Levenshtein $t^{0,1}_k$ whenever $\ell > -1$.

## Method
Polynomial / linear-programming techniques on the Gegenbauer side: introduce a signed measure $d\mu_\ell$ that is positive-definite up to degree $k-1$, derive a finite orthogonal sequence $P^{0,\ell}_i(t)$ via the Christoffel–Darboux kernel, prove interlacing of their zeros with those of $P^{(n)}_i$ and $P^{(n)}_{i+1}$, and build a Gauss–Jacobi quadrature exact to degree $2k$ with positive weights. Lower bounds split into cases $t_1(y) \ge \ell$ vs. $t_1(y) \in [-1,\ell]$ and iterate via Lemmas 4.5/4.6; upper bounds use $f(t) = (t+1)^e A(t)^2$ in identity (14), exploiting the geometric fact (Lemma 2.1) that the $n$ largest inner products $t_{|C|-n+1}(y), \dots, t_{|C|}(y)$ all equal $\rho(C)$.

## Result
For $(n,\tau,|C|)=(3,4,10)$ at $\ell=-0.97$: lower bound improves from FL's $0.689897$ to $0.724753$; upper bound (Theorem 5.4 with $b_0=(\sqrt{69}-7)/30$) is $\approx 0.754443$. Tables give comparable gains for $(3,4,10)$–$(10,4,67)$, $(3,6,17)$, $(4,6,31)$, $(3,8,26)$. Closed-form for antipodal designs: $\tau=3$ gives $1/\sqrt{n} \le \rho(C) \le \sqrt{|C|/2}/n$; $\tau=5$ gives an explicit bound involving $\sqrt{(n-1)(|C|-2n)/(n(n+2))}$.

## Why it matters here
Directly relevant to Einstein Arena problems involving spherical configurations and LP-bound techniques — kissing numbers, sphere packing, and any problem framed as "place points on $S^{n-1}$ minimizing maximum-coverage gap." Adds a cardinality-dependent LP refinement to the Fazekas–Levenshtein toolkit already used in council dispatch (Cohn–Elkies / Levenshtein lineage).

## Open questions / connections
- Identifying the *optimal* polynomial $A(t)$ in Theorem 5.3 for general $\tau$; paper only solves $\tau=4$ explicitly.
- Whether the iterative procedure (§4.3) divergence can be turned into nonexistence proofs for designs near $D(n,2k)$.
- Extension to $\tau$ odd via the signed-measure machinery (currently lower bounds are even-$\tau$ only).
- Connection to tight $2k$-designs ($n=(2m+1)^2-3$ for $k=2$): paper notes attainment of FL only at tight designs.

## Key terms
spherical design, covering radius, linear programming bound, Fazekas-Levenshtein bound, Gegenbauer polynomial, Jacobi polynomial, Christoffel-Darboux kernel, signed measure, positive definite, Gauss-Jacobi quadrature, Delsarte-Goethals-Seidel bound, antipodal design, Levenshtein, Boyvalenkov, kissing number, sphere packing
