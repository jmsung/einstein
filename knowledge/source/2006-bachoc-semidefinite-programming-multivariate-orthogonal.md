---
type: source
kind: paper
title: Semidefinite programming, multivariate orthogonal polynomials, and codes in spherical caps
authors: Christine Bachoc, Frank Vallentin
year: 2006
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/math/0610856v2
source_local: ../raw/2006-bachoc-semidefinite-programming-multivariate-orthogonal.pdf
topic: general-knowledge
cites: 
---

# Semidefinite programming, multivariate orthogonal polynomials, and codes in spherical caps

**Authors:** Christine Bachoc, Frank Vallentin  ·  **Year:** 2006  ·  **Source:** http://arxiv.org/abs/math/0610856v2

## One-line
Extends the SDP method of Bachoc–Vallentin from full-sphere kissing bounds to codes in spherical caps, producing new upper bounds on the one-sided kissing number $B(n)$ including a tight $B(8)=183$.

## Key claim
The SDP relaxation built from $H$-isotypic decomposition of $\mathrm{Pol}_{\le d}(S^{n-1})$ under $H=\mathrm{Stab}(O(\mathbb{R}^n),e)$ yields strict improvements on $B(n)$ for $n=5,6,7,8,9$, and in particular proves $B(8)=183$ (matching the hemispheric subset of $E_8$).

## Method
Decompose $\mathrm{Pol}_{\le d}(S^{n-1})$ under the cap-stabilizer $H$; each multiplicity-$m$ isotypic component yields an $m\times m$ matrix $Y^n_k(u,v,t)$ in three variables $(u,v,t)=(e\cdot x, e\cdot y, x\cdot y)$ with explicit Gegenbauer-polynomial entries. Positivity $\sum_{(c,c')\in C^2} Y^n_k(e\cdot c, e\cdot c', c\cdot c')\succeq 0$ gives an SDP whose dual is relaxed to a finite SDP via Putinar's Positivstellensatz (sum-of-squares multipliers $p_i$ encoding $\Delta$). Solved with CSDP at parameters $d=N=10$.

## Result
Table of $B(n)$ upper bounds: $B(3)\le 9$ (tight, recovers Fejes Tóth), $B(4)\le 18$ (tight, recovers Musin), $B(5)\le 33$ (down from 35), $B(6)\le 61$ (from 64), $B(7)\le 105$ (from 110), $B(8)\le 183$ (tight, new), $B(9)\le 297$ (from 309), $B(10)\le 472$. Section 4 reformulates the dual as a polynomial-positivity statement, proves a product rule for positive-definite polynomials in $R_d$, and derives an analytic Rankin-type cap bound $A(n,\theta,\phi)\le (1-\cos\theta)/(\cos^2\phi-\cos\theta)$.

## Why it matters here
Direct methodological scaffold for SDP-based extremal bounds: spherical-cap codes generalize the kissing-number SDP that already underlies wiki entries on Cohn–Elkies, Viazovska, and the SDP-relaxation-uselessness dead-end finding. Relevant to any arena problem in the sphere-packing / kissing / spherical-code family where the symmetry group is a point-stabilizer rather than the full orthogonal group.

## Open questions / connections
- Is the optimal 183-point hemispheric $E_8$ configuration unique up to isometry? (Authors conjecture yes; proof open.)
- Can the analytic LP-bound-via-$w(\theta,\phi)$ Rankin construction (Example 1) be lifted to higher degree using the matrix coefficients $F_0$, not just polynomial perturbation?
- Extends Delsarte LP method (symmetric two-point homogeneous spaces) to non-symmetric homogeneous spaces — same template may apply to Grassmannian-with-base-flag, projective caps, etc.
- Product rule (Cor. 4.14) suggests an algebra of positive-definite kernels usable in multi-step SDP hierarchies.

## Key terms
semidefinite programming, one-sided kissing number, spherical cap code, Gegenbauer polynomials, zonal matrices, isotypic decomposition, Delsarte LP method, Putinar Positivstellensatz, sum of squares, Bachoc, Vallentin, E8 lattice, reproducing kernel, positive definite polynomial
