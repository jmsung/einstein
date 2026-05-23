---
type: source
kind: paper
title: Spherical Harmonics
authors: Feng Dai, Yuan Xu
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1304.2585
source_local: ../raw/2013-dai-spherical-harmonics.pdf
topic: general-knowledge
cites:
---

# Spherical Harmonics

**Authors:** Feng Dai, Yuan Xu  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1304.2585

## One-line
Self-contained introduction (Chapter 1 of a Springer monograph) to spherical harmonics on $S^{d-1}$ — orthogonal bases, zonal/reproducing kernels, the Laplace–Beltrami operator, and angular derivatives.

## Key claim
The reproducing kernel of $\mathcal{H}_n^d$ is the zonal harmonic $Z_n(x,y) = \frac{n+\lambda}{\lambda} C_n^\lambda(\langle x,y\rangle)$ with $\lambda = (d-2)/2$ (the **addition formula**, Theorem 2.6); and on $S^{d-1}$, $\Delta_0 = \sum_{1\le i<j\le d} D_{i,j}^2$ where $D_{i,j} = x_i\partial_j - x_j\partial_i$ (Theorem 8.2).

## Method
Classical exposition: build $\mathcal{H}_n^d$ via the decomposition $\mathcal{P}_n^d = \bigoplus_j \|x\|^{2j} \mathcal{H}_{n-2j}^d$, use Maxwell's representation $p_\alpha(x) \propto \|x\|^{2|\alpha|+d-2}\partial^\alpha \|x\|^{-d+2}$ for monic bases, derive Gegenbauer-polynomial form of the reproducing kernel via the differential inner product $\langle p,q\rangle_\partial = p(\partial)q$, and obtain the Funk–Hecke formula for zonal-convolution eigenvalues.

## Result
$\dim \mathcal{H}_n^d = \binom{n+d-1}{n} - \binom{n+d-3}{n-2}$; Funk–Hecke: $\int_{S^{d-1}} f(\langle x,y\rangle) Y_n(y)\,d\sigma(y) = \lambda_n(f) Y_n(x)$ with $\lambda_n(f) = \omega_{d-1}\int_{-1}^1 f(t)\frac{C_n^\lambda(t)}{C_n^\lambda(1)}(1-t^2)^{(d-3)/2}dt$; $|Z_n(x,y)| \le \dim\mathcal{H}_n^d$, $Z_n(x,x) = \dim\mathcal{H}_n^d$; representation $T_{n,d}$ of $SO(d)$ on $\mathcal{H}_n^d$ is irreducible (Theorem 7.2).

## Why it matters here
Spherical harmonics + Gegenbauer/Funk–Hecke machinery is the analytical backbone of the **Cohn–Elkies LP** for sphere packing and kissing numbers (problems involving $S^{d-1}$ — kissing $\kappa(d)$, spherical codes, sphere-packing densities). The addition formula is exactly what turns radial test functions into positive-semidefinite spherical kernels — the move that makes the LP bound work.

## Open questions / connections
- Connects to Cohn–Elkies magic-function constructions: the LP dual variables live in expansions $\sum c_n C_n^\lambda(t)$ with $c_n \ge 0$ (PSD on the sphere by Funk–Hecke).
- Foundation for the Bochner / positive-definite-function characterization on $S^{d-1}$ used in semidefinite programming bounds for kissing numbers and energy minimization.
- $D_{i,j}$ angular derivatives + $\Delta_0$ decomposition feeds approximation-theory results on $S^{d-1}$ relevant to discretizing optimization problems on spheres.

## Key terms
spherical harmonics, zonal harmonics, Gegenbauer polynomials, Funk-Hecke formula, addition formula, reproducing kernel, Laplace-Beltrami operator, ultraspherical polynomials, $SO(d)$ representation, Cohn-Elkies, sphere packing, kissing number
