---
type: source
kind: paper
title: Global Maximizers for the Sphere Adjoint Fourier Restriction Inequality
authors: Damiano Foschi
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1310.2510
source_local: ../raw/2013-foschi-global-maximizers-sphere-adjoint.pdf
topic: general-knowledge
cites:
---

# Global Maximizers for the Sphere Adjoint Fourier Restriction Inequality

**Authors:** Damiano Foschi  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1310.2510

## One-line
Proves that constant functions are the global maximizers of the Stein–Tomas adjoint Fourier restriction inequality on the unit sphere $S^2 \subset \mathbb{R}^3$, and computes the sharp constant $R = 2\pi$.

## Key claim
A nonneg $f \in L^2(S^2)$ maximizes $\|\widehat{f\sigma}\|_{L^4(\mathbb{R}^3)} / \|f\|_{L^2(S^2)}$ iff $f$ is a nonzero constant, with sharp ratio $R = \|\widehat{1\sigma}\|_{L^4} / \|1\|_{L^2} = 2\pi$. Combined with Christ–Shao, all complex maximizers are $f(\omega) = k e^{i\theta} e^{i\xi\cdot\omega}$.

## Method
Rewrites $\|\widehat{f\sigma}\|_{L^4}^4$ via Plancherel as a quadrilinear form $Q(f,f^\star,f,f^\star)$ supported on the submanifold $\Gamma = \{\omega_1+\omega_2+\omega_3+\omega_4 = 0\} \subset (S^2)^4$. Three reduction steps: (i) antipodal rearrangement $f^\sharp$ via Cauchy–Schwarz collapses to nonneg antipodally-symmetric $f$; (ii) a key geometric identity (Lemma 4.2: $|\omega_1+\omega_2|^2+|\omega_1+\omega_3|^2+|\omega_2+\omega_3|^2 = 4$ when $\sum\omega_i$ is unit) neutralizes the convolution singularity; (iii) spherical-harmonic spectral decomposition of $H(g) = \iint g(\omega)g(\nu)|\omega-\nu|\,d\sigma d\sigma$ with Funk–Hecke + Legendre-polynomial coefficients $\Lambda_k < 0$ for $k \geq 1$ forces the maximizer to be the constant ($k=0$) mode.

## Result
Sharp inequality $\|\widehat{f\sigma}\|_{L^4(\mathbb{R}^3)}^4 \leq 16\pi^4 \|f\|_{L^2(S^2)}^4$, i.e. $R = 2\pi$, with equality iff $f$ is constant (up to the modulation/phase symmetries of the complex case). Auxiliary computations: $\sigma * \sigma(x) = (2\pi/|x|)\chi_{|x| \leq 2}$, $\|\sigma*\sigma\|_{L^2} = 2^{5/2}\pi^{3/2}$, $H(1) = (64/3)\pi^2$.

## Why it matters here
General background; no direct arena tie — this is sharp-constant analysis for a Strichartz/restriction inequality on $S^2$. Methodologically relevant as a template for **sharp-constant proofs via spectral decomposition on the sphere** (Funk–Hecke, Legendre polynomials, sign-of-eigenvalue arguments), which echoes the LP-bound / SDP / spherical-harmonic toolkit used for sphere packing and kissing-number problems (Cohn–Elkies, Viazovska).

## Open questions / connections
- Extends Foschi's earlier sharp-constant work on paraboloid and cone Strichartz (J. Eur. Math. Soc. 2007) to the sphere; analogous problems for $S^{n-1}$ at other Stein–Tomas exponents remain.
- Companion to Christ–Shao existence-of-extremizers results, which left the explicit identification open until this paper.
- The Lemma 4.2 geometric identity (sum of three unit vectors equal to a unit vector ⇒ pairwise-sum-squared identity) may generalize to other extremal sphere-configuration problems.

## Key terms
Fourier restriction, Stein–Tomas inequality, adjoint restriction, sphere $S^2$, sharp constants, global maximizers, extremizers, spherical harmonics, Funk–Hecke formula, Legendre polynomials, Cauchy–Schwarz, antipodal symmetrization, Foschi, Christ–Shao
