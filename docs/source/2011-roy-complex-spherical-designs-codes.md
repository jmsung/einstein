---
type: source
kind: paper
title: Complex Spherical Designs and Codes
authors: Aidan Roy, Sho Suda
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1104.4692
source_local: ../raw/2011-roy-complex-spherical-designs-codes.pdf
topic: general-knowledge
cites:
---

# Complex Spherical Designs and Codes

**Authors:** Aidan Roy, Sho Suda  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1104.4692

## One-line
Develops the theory of complex spherical $T$-designs on the complex unit sphere $\Omega(d) \subset \mathbb{C}^d$ — using full inner products $a^*b$ rather than $|a^*b|$ — and shows that many such designs carry (nonsymmetric) association schemes.

## Key claim
Complex spherical designs are a genuine extension of complex projective designs and real spherical designs; with the right Delsarte-style LP machinery built from Jacobi polynomials $g_{k,l}(x)$, one obtains absolute bounds, LP bounds (Thm 5.2), and sufficient conditions (Thms 6.1, 8.1, 9.1) for the inner-product relations on a $T$-design to define a *nonsymmetric* association scheme.

## Method
Extends Delsarte's harmonic / zonal-polynomial framework to $\Omega(d)$ via bivariate Jacobi polynomials $g_{k,l}$ orthogonal on the spaces $\mathrm{Harm}(k,l) \subset \mathrm{Hom}(k,l)$, with Koornwinder's addition theorem $\sum_i e_i(a)\overline{e_i(b)} = g_{k,l}(a^*b)$ giving positive-semidefiniteness. Lower sets $T \subset \mathbb{N}^2$ under the product order index design strength; an $S$-code has an annihilator polynomial in $\mathrm{span}\{x^k\bar{x}^l : (k,l)\in S\}$. Constructions go through $n$-antipodal covers of projective designs, orbits of finite subgroups $G \le U(d)$ (with Molien-series generating functions for $\dim \mathrm{Harm}(k,l)^G$), Singer difference sets, MUBs in $\mathbb{C}^p$ ($p$ odd prime), and orthogonal arrays.

## Result
Establishes (i) absolute bounds and Delsarte LP bounds for $T$-designs; (ii) Thm 6.1: small-degree $T$-designs whose inner products take few values carry nonsymmetric association schemes; (iii) Thm 8.1(2): sufficient conditions for $n$-antipodal $T$-designs to carry a scheme; (iv) Thm 9.1: parameters of a nonsymmetric scheme are characterized by complex designs built from scheme idempotents treated as Gram matrices; (v) explicit constructions from MUBs, Singer sets, Pauli-group orbits, and OAs, with derived-code/design transfer results.

## Why it matters here
General background for sphere-packing / kissing-number / lattice work: the Cohn–Elkies LP-bound program lives in essentially this Delsarte-LP/zonal-polynomial world, so this paper provides a complex-sphere analogue of the same machinery (LP bounds, tight-design characterizations, association-scheme structure). It is closest in spirit to problems where projective / unitary symmetry already appears; no direct single-problem arena tie, but informs the LP-bound and equiangular-lines/MUB strands.

## Open questions / connections
- Can the complex-spherical LP bounds give nontrivial improvements over Cohn–Elkies-type bounds for any arena problem (e.g., kissing numbers in even dimensions via the $\mathbb{C}^d \hookrightarrow \mathbb{R}^{2d}$ embedding $\phi$ of Lemma 3.6)?
- Extends Delsarte–Goethals–Seidel [14,15] to the complex sphere; nontrivial nonsymmetric schemes raise the question of which arena configurations sit naturally on $\Omega(d)$ but not on $\mathbb{CP}^{d-1}$.
- Tight-design existence on $\Omega(d)$ (analogue of Bannai–Damerell [3,4]) — for which $(d, T)$ are absolute bounds achieved?

## Key terms
complex spherical design, Delsarte LP bound, Jacobi polynomial, zonal polynomial, Koornwinder addition theorem, harmonic space, nonsymmetric association scheme, antipodal cover, mutually unbiased bases, Singer difference set, Molien series, complex projective design
