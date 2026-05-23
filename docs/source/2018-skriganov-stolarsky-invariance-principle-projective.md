---
type: source
kind: paper
title: Stolarsky's invariance principle for projective spaces
authors: M. Skriganov
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1805.03541
source_local: ../raw/2018-skriganov-stolarsky-invariance-principle-projective.pdf
topic: general-knowledge
cites:
---

# Stolarsky's invariance principle for projective spaces

**Authors:** M. Skriganov  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1805.03541

## One-line
Extends Stolarsky's identity — linking spherical-cap quadratic discrepancy to pairwise Euclidean distances — from Euclidean spheres to all compact rank-one Riemannian symmetric manifolds (real, complex, quaternionic projective spaces and the octonionic projective plane).

## Key claim
For any $Q = Q(d,d_0) \in \{S^d, \mathbb{R}P^n, \mathbb{C}P^n, \mathbb{H}P^n, \mathbb{O}P^2\}$ and any $N$-point set $D_N \subset Q$, the $L^2$-invariance identity $\gamma(Q)\lambda[\xi_\natural, D_N] + \tau[D_N] = \bar\tau N^2$ holds, with explicit constant $\gamma(Q(d,d_0)) = \tfrac{\sqrt\pi}{4}(d+d_0)\,\Gamma(d_0/2)/\Gamma((d_0+1)/2)$.

## Method
Proposition 1.1 first establishes an $L^1$-invariance principle on any distance-invariant compact metric measure space via the symmetric-difference metric $\theta_\Delta$. Theorem 1.1 then shows $\tau(x_1,x_2) = \gamma(Q)\theta_\Delta(\xi_\natural, x_1, x_2)$ on rank-one symmetric spaces by embedding $\mathbb{F}P^n$ into Hermitian-matrix-projector models $\{\Pi : \Pi^2=\Pi, \mathrm{Tr}\,\Pi=1\}$ inside the Hilbert-Schmidt unit sphere, exploiting two-point homogeneity to reduce the integrand to an inner product against antipodal projectors. Theorem 1.2 computes $\gamma(Q)$ via zonal spherical function (Jacobi-polynomial) expansions of both $\tau$ and $\theta_\Delta$, matching coefficients at the $l=1$ mode.

## Result
Closed-form constants: $\gamma(\mathbb{R}P^n) = \tfrac{\pi}{4}(n+1)$, $\gamma(\mathbb{C}P^n) = n+1$, $\gamma(\mathbb{H}P^n) = \tfrac{4}{3}(n+1)$, $\gamma(\mathbb{O}P^2) = 192/35$. The invariance principle yields sharp orders $\bar\tau N^2 - \tau_N(Q) \asymp N^{1-1/d}$ and $\lambda_N(Q) \asymp N^{1-1/d}$ for extremal chordal-distance sums and quadratic discrepancies. As a byproduct, explicit integral formulas (4.27) for Jacobi-polynomial weighted integrals fall out.

## Why it matters here
Directly informs **discrete-geometry / packing problems** in the arena that involve point distributions on projective spaces or Grassmannians (e.g., line/plane packings via Fubini-Study / chordal distance), giving a tight duality between *minimize discrepancy* and *maximize pairwise distance* — two faces of the same objective. The constants $\gamma(Q)$ are computable, so the identity is usable as a triple-verify cross-check (sum-of-distances ↔ quadratic discrepancy).

## Open questions / connections
- Does an analogous $L^2$-invariance principle hold on Grassmannian manifolds $\mathrm{Gr}(k,n,\mathbb{F})$ (rank $>1$ symmetric spaces) — and what replaces the chordal metric?
- Can the $l=1$ matching trick be replaced by a direct combinatorial proof of integral identities (4.27), giving an alternative route promised for "the second part of this work"?
- Connects to Bilyk–Dai–Matzke energy-optimization-on-the-sphere and Cohn–Kumar–Minton optimal simplices/codes in projective spaces — bridging discrepancy theory and universally optimal configurations.

## Key terms
Stolarsky invariance principle, spherical cap discrepancy, chordal metric, Fubini-Study metric, projective space, rank-one symmetric space, two-point homogeneous space, zonal spherical functions, Jacobi polynomials, sum of pairwise distances, octonionic projective plane, quadratic discrepancy
