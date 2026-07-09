---
type: source
kind: paper
title: The Gaussian core model in high dimensions
authors: Henry Cohn, M. D. Courcy-Ireland
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.09684
source_local: ../raw/2016-cohn-gaussian-core-model-high.pdf
topic: general-knowledge
cites:
---

# The Gaussian core model in high dimensions

**Authors:** Henry Cohn, M. D. Courcy-Ireland  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.09684

## One-line
Proves asymptotically sharp lower bounds for Gaussian-potential energy minimization in $\mathbb{R}^n$ as $n \to \infty$, showing random lattices are optimal for sufficiently wide Gaussians.

## Key claim
For $f(t) = e^{-\alpha t^2}$ with $0 < \alpha < 4\pi/e \approx 4.6229$, the minimal $f$-energy of any density-$\rho$ configuration in $\mathbb{R}^n$ is $(\rho + o(1))(\pi/\alpha)^{n/2}$ as $n \to \infty$ — matching the Siegel mean value upper bound to leading constant, not just exponential rate.

## Method
Linear programming bound (Cohn–Elkies / Cohn–Kumar framework) with an explicit auxiliary function built by Hermite interpolation at the positive roots $\lambda_1 < \lambda_2 < \dots$ of the Bessel function $J_{n/2}$, analogous to Gaussian-subordination solutions of the Beurling–Selberg extremal problem. A key lemma (Prop. 3.1) shows that dividing $J_\nu(|x|)/|x|^\nu$ by successive factors $(1 - |x|^2/\lambda_k^2)$ preserves positive-definiteness, derived from a Mehler–Heine limit of Jacobi/Gegenbauer polynomial identities. Asymptotic analysis uses uniform Bessel-zero expansions via Airy roots.

## Result
Theorem 1.4 gives an explicit LP lower bound $\sum_m \frac{n}{2^{n-1}(n/2)!^2} \frac{\lambda_m^{n-2}}{J_{n/2-1}(\lambda_m)^2} f(\lambda_m/(\pi r))$. For $\alpha \geq 4\pi/e$, Theorem 1.3 gives the weaker bound $\rho[\tfrac{1}{2}e^{1-\alpha e/(8\pi)} + o(1)]^n$. A "conditional expectation bound" (Prop. 8.2) shows the Siegel upper bound is *not* sharp for $\alpha > \pi e$: random lattices conditioned on no short vectors give $\rho(\pi/\alpha)^{n/2}[e^{1/2 - \alpha/(2\pi e)} + o(1)]^n$. As a corollary, inverse power laws $1/t^{n+s}$ get bounds sharp to within a constant factor.

## Why it matters here
Directly informs the Cohn–Elkies LP-bound machinery used across sphere-packing and energy-minimization problems on Einstein Arena (P1, P15, P16, kissing-number variants), and connects energy minimization to sphere packing via the $\alpha \to \infty$ limit. Provides a worked example of Bessel-root Hermite interpolation as an auxiliary-function construction — a template for arena problems where the optimal LP function is unknown.

## Open questions / connections
- Conjecture 10.1: extend sharpness from $\alpha < 4\pi/e$ to $\alpha < \pi e$ (would make inverse-power-law bounds asymptotically sharp).
- Behavior in the gap $4\pi/e \leq \alpha \leq \pi e$ and beyond $\pi e$ — is there a further phase transition or is conditional-expectation sharp?
- Whether better-than-LP bounds exist for energy (analogous to the open question for sphere packing density beyond Levenshtein/Kabatyanskii–Levenshtein).
- Recovers Levenshtein's $(e/4)^n$ packing density bound as a corollary via the energy↔packing connection in Section 9.

## Key terms
Gaussian core model, linear programming bound, Cohn–Elkies, Cohn–Kumar, Bessel function roots, Hermite interpolation, Beurling–Selberg, Gaussian subordination, Siegel mean value theorem, random lattices, sphere packing, Levenshtein bound, positive-definite functions, theta series, Gegenbauer polynomials, Schoenberg theorem, conditional expectation bound, inverse power law energy
