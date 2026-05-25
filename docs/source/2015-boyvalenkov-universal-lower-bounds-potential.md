---
type: source
kind: paper
title: Universal Lower Bounds for Potential Energy of Spherical Codes
authors: P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1503.07228
source_local: ../raw/2015-boyvalenkov-universal-lower-bounds-potential.pdf
topic: general-knowledge
cites:
---

# Universal Lower Bounds for Potential Energy of Spherical Codes

**Authors:** P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1503.07228

## One-line
Derives universal lower bounds (ULB) on the $h$-energy of $N$-point spherical codes on $S^{n-1}$ for any absolutely monotone potential $h$, via Levenshtein-type quadrature plus Hermite interpolation, plus a test-function criterion for when those bounds can be improved.

## Key claim
For fixed $(n,N)$, let $\tau=\tau(n,N)$ with $N\in(D(n,\tau),D(n,\tau+1)]$ and let $\{(\alpha_i,\rho_i)\}_{i=1}^{k}$, $k=\lceil(\tau+1)/2\rceil$, be Levenshtein's $1/N$-quadrature nodes/weights (roots of an adjacent Jacobi polynomial, independent of $h$). Then for every absolutely monotone $h$, $E(n,N;h) \ge R_\tau(n,N;h) := N^2 \sum_{i=1}^{k} \rho_i\, h(\alpha_i)$, and this bound is the unique optimum of the Delsarte–Yudin LP restricted to $\mathcal P_\tau$ (Theorem 3.1). A test-function criterion $Q_j(n,s) := 1/N + \sum_i \rho_i P_j^{(n)}(\alpha_i)$ governs whether higher-degree polynomials improve it (Theorem 4.1).

## Method
Delsarte–Yudin LP framework: bound $E(n,N;h)$ from below by $N(Nf_0-f(1))$ for polynomials $f\le h$ with non-negative Gegenbauer coefficients. The optimal degree-$\tau$ polynomial $f$ is constructed as the Hermite interpolant $H(h;(t-s)f_\tau(n,s)(t))$ to $h$ at Levenshtein's quadrature nodes; absolute monotonicity of $h$ plus interlacing of Jacobi roots forces $f\le h$ and non-negative Gegenbauer expansion. The same nodes give a $1/N$-quadrature exact on $\mathcal P_\tau$, collapsing $f_0-f(1)/N$ to $\sum\rho_i h(\alpha_i)$. Improvability is decided by signs of test functions $Q_j(n,s)$.

## Result
The ULB $R_\tau(n,N;h)$ is tight for all "sharp configurations" (Cohn–Kumar) and for the $600$-cell; numerical tables for $n=4$, $N=5,\dots,64$ show small gaps vs. Ballinger et al.'s best-known Newton- and Gauss-potential minimizers, exact at $N=5,8$. Theorem 4.3: $R_\tau$ cannot be improved by degree $\tau{+}1$ or $\tau{+}2$ polynomials. Theorem 4.4: for $k\ge \sqrt{n-2}$ (even $\tau$) or $k\ge k_2(n)$ (odd $\tau$), degree $2k{+}3$ improves $R_\tau$ on the open Levenshtein interval. Theorem 4.11: the codes $(n,N)=(10,40)$, $(14,64)$, $(15,128)$ are *not* LP-universally optimal — refuting LP-route proofs of two universal-optimality conjectures of Ballinger et al. Corollary 4.6: for each $n\ge3$, only finitely many sharp configurations exist.

## Why it matters here
Direct framework for any arena problem of form "minimize $\sum_{x\ne y} h(\langle x,y\rangle)$ on $S^{n-1}$ with $|C|=N$ fixed" — gives a *potential-agnostic* lower bound computable from a small Jacobi-root quadrature, plus a test-function diagnostic that tells you whether to invest in higher-degree LP polynomials before running expensive optimizers. Sharpens the Cohn–Elkies / Delsarte–Yudin toolkit already in the wiki and supplies a concrete "is this code LP-extremal?" test relevant to kissing/sphere-packing/code problems.

## Open questions / connections
- Conjecture 4.7: if $Q_j\ge 0$ for $j=\tau{+}3,\tau{+}4$, then $Q_j\ge 0$ for all $j>\tau$ — would make Corollary 4.2 a finite check.
- Numerical algorithm for the "four-touching-points" improving polynomial in $\mathcal P_{2k+3}$ (sketched for $D_4$ kissing, full treatment deferred).
- Extends Levenshtein [1992, 1998] (cardinality bounds) and Cohn–Kumar [2007] (universal optimality) — bridges the two via a single quadrature.
- Leaves open whether $(10,40)$ and $(14,64)$ are universally optimal by *non-LP* routes (e.g., 600-cell-style ad-hoc arguments are ruled out).

## Key terms
universal lower bound, absolutely monotone potential, Delsarte–Yudin linear programming, Gegenbauer polynomials, Levenshtein bound, Jacobi polynomial quadrature, Hermite interpolation, spherical code, spherical design, sharp configuration, test functions $Q_j(n,s)$, LP-universally optimal, 600-cell, $D_4$ root system, Cohn–Kumar, Boyvalenkov
