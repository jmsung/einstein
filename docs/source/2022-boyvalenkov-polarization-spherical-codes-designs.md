---
type: source
kind: paper
title: On polarization of spherical codes and designs
authors: P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2207.08807
source_local: ../raw/2022-boyvalenkov-polarization-spherical-codes-designs.pdf
topic: general-knowledge
cites:
---

# On polarization of spherical codes and designs

**Authors:** P. Boyvalenkov, P. Dragnev, D. Hardin, E. Saff, Maya M. Stoyanova  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2207.08807

## One-line
Derives universal lower and upper bounds (Delsarte-Yudin/LP type) on max-min and min-max polarization of spherical $\tau$-designs via Gauss-Jacobi quadrature with Hermite interpolants, and proves the 600-cell is universally optimal for min-max polarization.

## Key claim
For any spherical $\tau$-design $C \subset S^{n-1}$ of cardinality $N$ with $\tau = 2k-1+\epsilon$, and any potential $h$ with $h^{(\tau+1)}(t) \geq 0$ on $(-1,1)$: $Q^{(h)}(n,\tau,N) \geq N \sum_{i=1-\epsilon}^{k} \rho_i h(\alpha_i)$ and the same bound holds for $R^{(h)}(n,\tau,N)$, where $\{\alpha_i\}$ are roots of $(1+t)^\epsilon P_k^{(0,\epsilon)}(t)$ and $\{\rho_i\}$ are positive Gauss-Jacobi quadrature weights summing to 1 — independent of $h$.

## Method
Delsarte-Yudin LP framework: find polynomials $f \leq h$ of degree $\leq \tau$ with maximal $f_0$ (Gegenbauer constant term); the design property forces $U_f(x,C) = f_0 |C|$ to be constant on $S^{n-1}$. The optimum is the Hermite interpolant of $h$ at Gauss-Jacobi nodes (roots of adjacent Gegenbauer polynomials $P_k^{(a,b)}$), with the error term controlled by the sign of $h^{(\tau+1)}$. A dual upper-bound construction uses degree-$m$ positive definite signed measures.

## Result
- Universal polarization lower bounds (PULB), eqs. (16), (17), (23), (24) — convex combinations of $h$ at Gegenbauer quadrature nodes.
- Recovers the Fazekas-Levenshtein covering-radius bound $\ell_{\tau,N} \geq t^0_{k,\epsilon}$ as a corollary via the Riesz-potential limit $s \to \infty$.
- 600-cell (the unique 120-point 11-design on $S^3$) is universally optimal for min-max polarization for absolutely monotone potentials of order 16.
- Cross-polytope ($N=2n$) is max-min optimal among spherical 2-designs for $n=2,3,4$ (and for all $n$ conditional on the covering-radius conjecture $s_{2n}=1/\sqrt{n}$); also optimal among all centered codes.
- New examples attaining Fazekas-Levenshtein: cube on $S^2$ ($\tau=3, N=8$), 24-cell on $S^3$ ($\tau=5, N=24$).
- Alternative proofs for $N \leq n$ (any 1-design) and $N = n+1$ (regular simplex, Borodachov 2022).

## Why it matters here
Direct relevance to **kissing numbers** (24-cell, 600-cell, cross-polytope, sphere-packing-adjacent configurations) and **discrete geometry / covering** problems on the arena: the PULB gives a universal certificate against which to test candidate codes, and the Hermite-interpolant construction is a concrete LP recipe complementary to Cohn-Elkies and Levenshtein bounds already in the wiki.

## Open questions / connections
- Conjecture $s_{2n} = 1/\sqrt{n}$ (best covering radius for $2n$ points on $S^{n-1}$) — open for $n \geq 5$; would close the cross-polytope max-min optimality.
- Extends Borodachov's m-stiff configuration framework (ESI Vienna 2022) and Cohn-Kumar universal optimality to polarization duals of energy minimization.
- Polarization-vs-energy duality (mirroring covering-vs-packing) — which other sharp/strongly-sharp codes attain both PULB and energy ULB?
- Adapt to other polynomial metric spaces (Hamming, Johnson, projective) per Levenshtein framework.

## Key terms
spherical designs, polarization, max-min polarization, min-max polarization, Delsarte-Yudin LP bound, Gegenbauer polynomials, Jacobi polynomials, Hermite interpolation, Gauss-Jacobi quadrature, Fazekas-Levenshtein bound, covering radius, 600-cell, cross-polytope, 24-cell, universal lower bound, sharp codes, Cohn-Kumar universal optimality, absolutely monotone potentials, Levenshtein, Borodachov
