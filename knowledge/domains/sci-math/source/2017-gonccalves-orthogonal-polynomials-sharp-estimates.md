---
type: source
kind: paper
title: Orthogonal Polynomials and Sharp Estimates for the Schr\"odinger Equation
authors: F. Gonccalves
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1702.08510
source_local: ../raw/2017-gonccalves-orthogonal-polynomials-sharp-estimates.pdf
topic: general-knowledge
cites:
---

# Orthogonal Polynomials and Sharp Estimates for the Schr\"odinger Equation

**Authors:** F. Gonccalves  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1702.08510

## One-line
Uses Hermite, Laguerre, and Gegenbauer polynomial expansions to give a new proof that Gaussians maximize the Strichartz inequality at even exponents and to sharpen a weighted Schrödinger estimate.

## Key claim
For the Strichartz estimate $\|e^{it\Delta}f\|_{L^p_x L^q_t} \le C\|f\|_{L^2}$ with even exponents $p=2k$, $q=2k\ell$, sharpness reduces to an operator-norm question for a projection $P$ on a sequence space; the projection condition $(k-1)\ell d/2 = 1$ characterizes exactly the three known Gaussian-maximizer cases $(p,q,d)\in\{(6,6,1),(4,8,1),(4,4,2)\}$. A separate sharpened weighted bound $\int_{\mathbb{R}}\int_{\mathbb{R}^d}|e^{it\Delta}f|^2 \|x\|^{-2}\,dx\,dt \le \tfrac{\pi}{d-2}\|f\|_2^2 - \tfrac{2}{d}\operatorname{Dist}(f,\text{Radial})^2$ holds for $d\ge 3$, with equality iff $f$ is radial.

## Method
Expand initial data in the orthogonal basis $\Phi_m(x)=H_m(\sqrt{4\pi}x)e^{-\pi\|x\|^2}$ (Hermite) or $\Psi_n=L_n^{(\nu)}(2\pi\|x\|^2)e^{-\pi\|x\|^2}$ (Laguerre, radial); use the explicit Schrödinger evolution of these eigenfunctions plus Fourier-series orthogonality in $t$ to turn the Strichartz norm into a bilinear form on a Hilbert space of matrix-indexed sequences. The resulting kernel is summed via the Mehler kernel for Hermite polynomials, yielding $\|P_S\|=(\mu)_{\lfloor S/2\rfloor}/\lfloor S/2\rfloor!$ with $\mu=(k-1)\ell d/2$. The weighted inequality is diagonalized on $L^2(S^{d-1})$ via the Funk–Hecke formula and Gegenbauer polynomial eigenvalues $\tfrac{d-2}{2n+d-2}|S^{d-1}|$.

## Result
- Theorem 3: $P$ is a projection iff $\mu=(k-1)\ell d/2 = 1$; for $\mu>1$, $\|P_S\|\sim S^{\mu-1}/(2^{\mu-1}\Gamma(\mu))$, so $P$ is unbounded — recovering Foschi/Hundertmark–Zharnitsky cases via a unified mechanism.
- Theorem 6: for $(p,q,d)=(4,4,2)$ radial, the matrix $Q_S=[Q(a,S-a,c,S-c)]$ is positive semidefinite and doubly stochastic with strictly positive entries; the radial Strichartz inequality $\|e^{it\Delta}f\|_{L^4(\mathbb{R}^3)}\le 2^{-1/2}\|f\|_{L^2(\mathbb{R}^2)}$ has Gaussians as the unique extremizers.
- Theorem 9 / Cor. 10: sharpened weighted estimate with explicit deficit $\tfrac{2}{d}\operatorname{Dist}(f,\text{Radial})^2$ and an interpolated $L^p$-weighted family for $2\le p\le 2+4/d$.
- Theorem 14 (appendix): the coefficient $Q(a,b,c,d) = 2^{-N}(\#W_{\text{even}}-\#W_{\text{odd}})$ counts signed permutations of 4-letter words at given Hamming distance from $1^a 2^b 3^c 4^d$.

## Why it matters here
General background; no direct arena tie — closest hooks are uncertainty/functional-inequality problems and the Cohn–Elkies/Beckner lineage of sharp-inequality techniques. The orthogonal-polynomial-expansion + finite-dimensional-block-diagonalization strategy is a transferable template for problems where extremizers are conjecturally Gaussian and the objective decomposes over Hermite/Laguerre/Gegenbauer levels.

## Open questions / connections
- Conjecture 1 (Strichartz maximizers are Gaussians) remains open for non-even exponents; the paper explicitly flags "find a special way of discretizing the time variable" within Beckner's CLT framework as the missing piece.
- Connects to Beckner [2] (sharp Hausdorff–Young via Hermite semigroup + CLT) and Gonçalves [10] (CLT for operators with Gaussian kernels) — both candidates for ingestion if uncertainty-inequality problems surface.
- The Laguerre Poisson kernel involves Bessel $I_\nu$; the author notes this blocks the Hermite-style projection argument outside $\mu=1$ — open obstruction worth a finding if encountered.

## Key terms
Strichartz inequality, Schrödinger equation, Hermite polynomials, Laguerre polynomials, Gegenbauer polynomials, spherical harmonics, Funk–Hecke formula, Mehler kernel, Gaussian extremizers, sharp constants, Foschi, Hundertmark–Zharnitsky, Beckner, weighted Strichartz estimate, four-letter-word combinatorics
