---
type: source
kind: paper
title: Fourier interpolation from spheres
authors: Martin Stoller
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.11627
source_local: ../raw/2020-stoller-fourier-interpolation-spheres.pdf
topic: general-knowledge
cites:
---

# Fourier interpolation from spheres

**Authors:** Martin Stoller  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.11627

## One-line
Extends the Radchenko–Viazovska 1D Fourier interpolation formula to all dimensions $d \geq 2$, reconstructing any Schwartz function on $\mathbb{R}^d$ from the restrictions of $f$ and $\hat{f}$ to spheres of radius $\sqrt{n}$.

## Key claim
For $d \geq 5$ and every Schwartz $f : \mathbb{R}^d \to \mathbb{C}$, there exist explicit smooth kernels $A_n, \tilde{A}_n : \mathbb{R}^d \times S^{d-1} \to \mathbb{C}$ such that $f(x) = \sum_{n=1}^\infty \int_S A_n(x,\zeta) f(\sqrt{n}\zeta)\,d\zeta + \sum_{n=1}^\infty \int_S \tilde{A}_n(x,\zeta) \hat{f}(\sqrt{n}\zeta)\,d\zeta$ with absolute convergence (Theorem 1); analogous result with boundary data at $0$ for $d = 2,3,4$.

## Method
Two-step reduction: (1) a harmonic-analysis "lift" $L_u^p$ (generalizing $S_{\text{odd}}(\mathbb{R}) \cong S_{\text{rad}}(\mathbb{R}^3)$) decomposes any $f \in S(\mathbb{R}^d)$ via spherical-harmonic expansion into radial functions on higher-dimensional spaces $\mathbb{R}^{d+2m}$, intertwining Fourier transforms up to $i^m$; (2) the radial interpolation problem in $\mathbb{R}^p$ ($p \geq 5$) is solved by a Poincaré-series construction — averaging Gaussians $e^{\pi i r^2 \tau}$ under the slash action of $\Gamma(2)$ rather than the contour-integral / modular-form approach of Viazovska. For $d \in \{2,3,4\}$, supplements with Bondarenko–Radchenko–Seip's results.

## Result
Theorem 2 produces radial generating-function coefficients $b_{p,n}, \tilde{b}_{p,n}$ with explicit polynomial bounds $\max(|b_{p,n}|, |\tilde{b}_{p,n}|) \leq C_1 (47/p)^{p/4} n^{p/2}$ (constant $47 \geq 2\pi e^2$) and decay $\lesssim n^{p/4+1+\varepsilon}|r|^{-p/2+2(1+\varepsilon)}$ away from origin. Corollary 1.1: only Schwartz function with $f$ and $\hat{f}$ vanishing on all $\sqrt{n} S^{d-1}$ is zero. Proposition 8.1: unlike Radchenko–Viazovska's case, infinitely many $b_{p,n}$ are not of rapid decay — the basis functions equal Poincaré-series Fourier coefficients on $\Gamma_0(4)$ up to constants.

## Why it matters here
General background; no direct arena tie. Tangentially relevant to sphere packing and modular-form / magic-function techniques (P1 sphere-packing wiki content on Cohn–Elkies / Viazovska), as a methodological cousin to the magic-function interpolation toolkit; useful as reference for uniqueness/sampling arguments on sphere-supported data.

## Open questions / connections
- Free interpolation in the non-radial setting is open — Proposition 7.1 shows the image of the restriction map has infinite-dimensional cokernel, unlike the radial 1D case.
- Whether bounds on $b_{p,n}$ can be improved to rapid decay by a different construction (current Poincaré-series method provably cannot).
- Extends Radchenko–Viazovska [15] and connects to Bondarenko–Radchenko–Seip [3]; Ramos–Sousa [16] address denser-than-$\sqrt{n}$ node sequences in the radial case.

## Key terms
Fourier interpolation, Schwartz functions, spherical harmonics, Poincaré series, modular forms, $\Gamma(2)$, $\Gamma_0(4)$, Kloosterman sums, Bessel functions, Radchenko-Viazovska, Bochner periodicity, sphere packing, uniqueness pairs, magic function
