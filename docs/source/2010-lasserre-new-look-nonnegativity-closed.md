---
type: source
kind: paper
title: A New Look at Nonnegativity on Closed Sets and Polynomial Optimization
authors: J. Lasserre
year: 2010
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1009.0125
source_local: ../raw/2010-lasserre-new-look-nonnegativity-closed.pdf
topic: general-knowledge
cites:
---

# A New Look at Nonnegativity on Closed Sets and Polynomial Optimization

**Authors:** J. Lasserre  ·  **Year:** 2010  ·  **Source:** https://arxiv.org/abs/1009.0125

## One-line
Characterizes nonnegativity of a continuous function $f$ on a closed set $K \subseteq \mathbb{R}^n$ via positive semidefiniteness of moment matrices of the signed measure $f\,d\mu$, yielding a hierarchy of single-variable SDPs giving monotone *upper* bounds on $\min_K f$.

## Key claim
$f$ is nonnegative on $K$ iff $\int h^2 f\, d\mu \geq 0$ for all polynomials $h$, where $\mu$ is any finite Borel measure with $\mathrm{supp}\,\mu = K$ (with explicit weight $e^{-\sum|x_i|}$ in the noncompact case). Equivalently, all localizing matrices $M_d(fy) \succeq 0$ for $d=0,1,\ldots$. This gives the first explicit *outer* SDP hierarchy of the nonneg-polynomial cone $C_d$ **with no lifting** (each approximation is a spectrahedron in the coefficient vector alone).

## Method
Combines Lemma 3.1 (Radon-Nikodym + support arguments: $f\geq 0$ on $K$ iff $\nu(B)=\int_B f\,d\mu$ is a positive measure) with Berg/Nussbaum multivariate Carleman conditions for moment determinacy. For optimization, define $\lambda_d = \sup\{\lambda : M_d((f-\lambda)y) \succeq 0\}$ — a single-variable SDP that reduces to a generalized eigenvalue problem on the pair $(M_d(fy), M_d(y))$. Choice of $\mu$ tailored to $K$: Gaussian on $\mathbb{R}^n$, exponential on $\mathbb{R}^n_+$, uniform on box/simplex/ball, counting measure on $\{-1,1\}^n$.

## Result
The sequence $\lambda_d$ is monotone nonincreasing with $\lambda_d \downarrow f^*$ as $d\to\infty$, even when $f^*$ is not attained (e.g., $K=\mathbb{R}^n$). Convergence is asymptotic in general but **finite** when $K$ is discrete (Cor. 4.3 — applies to MAXCUT/0-1 programs). Numerical examples show rapid decrease in first iterations with a long tail near $f^*$; numerical issues kick in around $d \approx 14$–$15$. Dual SDP yields an s.o.s. density $\sigma^*d\mu$ concentrating near global minimizers.

## Why it matters here
Provides a complementary upper-bound hierarchy to the standard Lasserre lower-bound SDP relaxations — useful for any arena problem cast as polynomial optimization over simple sets (box, simplex, sphere, orthant, $\{-1,1\}^n$). The single-variable generalized-eigenvalue form is computationally cheap and could complement existing SDP/LP bounds on autocorrelation, packing-density, and extremal-graph problems where $K$ is simple enough that moments of a chosen $\mu$ are closed-form.

## Open questions / connections
- How does convergence rate of $\lambda_d \downarrow f^*$ depend on choice of $\mu$? (Author flags this as open.)
- Can the orthogonal-polynomial reformulation (making $M_d(y)=I$, reducing to standard eigenvalue problem) be exploited for large-$n$ arena instances?
- Tie-in to copositive programming: yields outer SDP approximations $\mathrm{COP}_d$ of the copositive cone — relevant wherever quadratic-form-on-orthant constraints appear (e.g., correlation-inequality problems).
- Complements gradient-tentacle (Schweighofer) and tangency-variety (Ha-Pham) lower-bound methods when $f^*$ is unattained.

## Key terms
moment matrix, localizing matrix, Lasserre hierarchy, sums of squares, semidefinite programming, generalized eigenvalue problem, Carleman condition, Putinar Positivstellensatz, Stengle Nichtnegativstellensatz, polynomial optimization, copositive cone, MAXCUT, spectrahedron, nonnegative polynomials cone, Berg moment problem
