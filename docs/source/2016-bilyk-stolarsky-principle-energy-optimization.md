---
type: source
kind: paper
title: The Stolarsky Principle and Energy Optimization on the Sphere
authors: D. Bilyk, F. Dai, Ryan W. Matzke
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.04420
source_local: ../raw/2016-bilyk-stolarsky-principle-energy-optimization.pdf
topic: general-knowledge
cites:
---

# The Stolarsky Principle and Energy Optimization on the Sphere

**Authors:** D. Bilyk, F. Dai, Ryan W. Matzke  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.04420

## One-line
Extends the classical Stolarsky invariance principle (which links $L^2$ spherical-cap discrepancy to pairwise Euclidean-distance energy) to hemispheres, slices, wedges, general measures, and arbitrary positive-definite potentials, and characterizes maximizers of geodesic-distance energy on $S^d$.

## Key claim
A hemisphere analog of Stolarsky's identity holds: $[D_{L^2,\text{hem}}(Z)]^2 = \tfrac12 - \tfrac{1}{N^2}\sum_{i,j} d(z_i,z_j)$, and for the geodesic energy $I_g(\mu) = \iint d(x,y)^\delta\,d\mu\,d\mu$ on $S^d$ the maximizer transitions at $\delta=1$: uniform $\sigma$ for $\delta\in(0,1)$, any centrally symmetric measure at $\delta=1$, and $\mu = \tfrac12(\delta_p + \delta_{-p})$ for $\delta>1$ — sharply different from the Euclidean case where Björck's threshold is $\delta=2$.

## Method
Squares out the $L^2$ discrepancy integrand so cross-terms $1_A(z_i)1_A(z_j)$ yield an interaction potential expressible as intersection-volume of test sets; for hemispheres this gives $\sigma(H(x)\cap H(y)) = \tfrac12(1 - d(x,y))$ via a one-line geometric picture. For the generalized version, uses Schoenberg's characterization of positive-definite functions on $S^d$ (non-negative Gegenbauer coefficients) and the convolution square-root $F = f * f$ to construct an $L^2_f$ discrepancy satisfying $I_F(\mu) - I_F(\sigma) = D^2_{L^2,f}(\mu)$. Combinatorial geometry (spherical Sylvester–Gallai) handles the odd-$N$ maximizer characterization.

## Result
(i) Hemisphere Stolarsky identity (Thm 3.3); (ii) for even $N$, the maximum $\tfrac{1}{N^2}\sum d(z_i,z_j) = \tfrac12$ is attained iff $Z$ is centrally symmetric; for odd $N$ the max is $\tfrac12 - \tfrac{1}{2N^2}$, attained iff $Z = Z_1 \cup Z_2$ with $Z_1$ symmetric and $Z_2$ a great-circle maximizer (Thm 3.5); (iii) generalized Stolarsky $I_F(\mu)-I_F(\sigma)=D^2_{L^2,f}(\mu)$ for $F\in\Phi_d$ (Thm 5.10); (iv) $\sigma$ is the unique minimizer of $I_F$ iff $\widehat{F}(n,\lambda)>0$ for all $n\ge1$ (Thm 5.13); (v) Stolarsky identities for slices and wedges with potentials $(1-d(x,y))^2$ and $(\tfrac12 - d(x,y))^2$ (Thms 6.1, 6.4); (vi) closed form for $V_d = \iint d(x,y)^2 d\sigma\,d\sigma \to 1/4$ as $d\to\infty$.

## Why it matters here
Directly relevant to autocorrelation / extremal-energy problems and any arena problem framed as "maximize pairwise distance / minimize discrete energy on a sphere": gives the dictionary between an $L^2$-discrepancy minimization and an energy maximization, and warns that geodesic-vs-Euclidean choice changes the optimal configuration qualitatively (uniform → antipodal-pair). The positive-definite/Gegenbauer-coefficient criterion (Thm 5.13) is a sharper version of the LP / Cohn–Elkies style argument the agent already uses for sphere-packing bounds.

## Open questions / connections
- Sharp asymptotics for $E_F(Z) - I_F(\sigma)$ as $N\to\infty$ for geodesic Riesz energy $d(x,y)^\delta$ (handled in companion [Bilyk–Dai], including $\delta<0$ and logarithmic case).
- Extends Björck (1956) Euclidean-energy maximizers and Fejes Tóth / Sperling / Larcher distance-sum results to all dimensions; spherical Sylvester–Gallai reused in odd-$N$ case.
- Connections to one-bit compressed sensing / random tessellations (Plan–Vershynin, Bilyk–Lacey) via wedge discrepancy and frame potential.

## Key terms
Stolarsky invariance principle, $L^2$ spherical cap discrepancy, hemisphere discrepancy, geodesic distance energy, Euclidean distance energy, positive definite functions on sphere, Schoenberg theorem, Gegenbauer coefficients, Funk–Hecke formula, spherical Sylvester–Gallai, Björck antipodal measure, frame potential, wedge and slice discrepancy, one-bit compressed sensing, Bilyk, Dai, Matzke
