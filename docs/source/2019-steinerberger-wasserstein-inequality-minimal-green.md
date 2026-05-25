---
type: source
kind: paper
title: A Wasserstein Inequality and Minimal Green Energy on Compact Manifolds
authors: S. Steinerberger
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1907.09023
source_local: ../raw/2019-steinerberger-wasserstein-inequality-minimal-green.pdf
topic: general-knowledge
cites:
---

# A Wasserstein Inequality and Minimal Green Energy on Compact Manifolds

**Authors:** S. Steinerberger  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1907.09023

## One-line
Bounds the $W_2$ Wasserstein distance between an $n$-point empirical measure and the uniform measure on a compact $d$-manifold by the square root of the discrete Green energy plus $n^{-1/d}$, giving optimal $W_2$ convergence rates for minimal-energy point configurations.

## Key claim
For a smooth compact $d$-manifold $M$ ($d \geq 3$) without boundary with Green's function $G$ (mean 0), any $n$ points satisfy $W_2\!\left(\tfrac{1}{n}\sum_k \delta_{x_k}, dx\right) \lesssim n^{-1/d} + \left(\tfrac{1}{n^2}\sum_{k\neq\ell} G(x_k,x_\ell)\right)^{1/2}$; with corollary $\sum_{k\neq\ell} G(x_k,x_\ell) \gtrsim -n^{2-2/d}$, hence Green-energy minimizers achieve the optimal rate $W_2 \asymp n^{-1/d}$. A parallel result holds for the Coulomb kernel $1/\|x-y\|^{d-2}$ on $S^d$ ($d\geq 3$), recovering Marzo–Mas as a corollary. In $d=2$ the bound carries an extra $\sqrt{\log n}$.

## Method
Heat-kernel smoothing: triangle-split $W_2(\mu, dx) \leq W_2(\mu, e^{t\Delta}\mu) + W_2(e^{t\Delta}\mu, dx)$. First term bounded by $\sqrt{t}$ via Aronson's heat-kernel Gaussian bound interpreted as a transport plan. Second term controlled via Peyré's inequality $W_2(\nu, dx) \leq \|\nu\|_{\dot H^{-1}}$, expanding $\|e^{t\Delta}\mu\|_{\dot H^{-1}}^2$ as $\iint G\, e^{t\Delta}\delta_{x_k}\, e^{t\Delta}\delta_{x_\ell}$ and splitting diagonal (Aronson + $G \lesssim 1/r^{d-2}$ gives $t^{1-d/2}/N$) vs off-diagonal (time derivative collapses via $\Delta_y G = 1/\mathrm{vol}(M) - \delta_x$). Optimizing $t = n^{-2/d}$ closes the bound. For $S^d$, the Funk–Hecke formula gives Green-energy/Riesz-kernel equivalence and the Laplacian of the Coulomb kernel keeps a bootstrap argument feasible.

## Result
Theorem 1 (manifolds, $d\geq 3$): $W_2 \lesssim n^{-1/d} + (\tfrac{1}{n^2}\sum_{k\neq\ell}G(x_k,x_\ell))^{1/2}$. Theorem 2 (Coulomb on $S^d$): same with $G$ replaced by $|x_k-x_\ell|^{-(d-2)} - c_d$. Corollary: $\sum_{k\neq\ell}G(x_k,x_\ell) \gtrsim -n^{2-2/d}$ via the inequality $\|e^{t\Delta}\mu\|_{\dot H^{-1}}^2 \geq 0$ combined with the upper expansion. Bounds are sharp for $d\geq 3$, sharp up to $\sqrt{\log n}$ for $d=2$. Application: on $\mathbb{T}^1$, identifies Zinterhof's diaphony $F_N$ with the Green-energy square root, giving $W_2(\mu, dx) \lesssim F_N(\mu)$.

## Why it matters here
General background — relates discrete energy minimization (Coulomb/Green/Riesz on $S^d$ and compact manifolds) to equidistribution rates. Useful for any arena problem involving sphere-distributed points (Thomson-type, Fekete, logarithmic-energy, Riesz-energy configurations) where one wants to translate "low energy" into "uniformly distributed" with a quantitative rate. Connects to potential theory, $\dot H^{-1}$ duality, and the Wagner lower bound for Coulomb sums on $S^d$.

## Open questions / connections
- Is $W_2$ the endpoint, or does the optimal rate hold in $W_{2+\varepsilon}$ for some $\varepsilon > 0$?
- Can the Chafaï–Hardy–Maïda and García-Zelada $W_1$-style bounds be promoted to $W_2$ for general two-measure setups (posed problem in [11])?
- Extends Beltrán–Corral–Criado del Rey weak equidistribution to a quantitative rate; refines Criado del Rey separation bound.
- Recovers Marzo–Mas (arXiv:1907.04814) on Coulomb-energy minimizer rates on $S^d$ as a corollary; complements Wagner's lower bound.
- Suggests existing diaphony bounds on number-theoretic sequences (irrational rotations, finite-field constructions) immediately yield Green-energy bounds.

## Key terms
Wasserstein distance, Green energy, Coulomb kernel, Riesz energy, $\dot H^{-1}$ Sobolev norm, Peyré inequality, heat kernel, Aronson bound, Funk-Hecke formula, spherical harmonics, Thomson problem, Fekete points, diaphony, equidistribution, Steinerberger, Marzo-Mas, Wagner, compact manifold, sphere $S^d$
