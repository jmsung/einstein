---
type: source
kind: paper
title: Fourier interpolation on the real line
authors: D. Radchenko, M. Viazovska
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1701.00265
source_local: ../raw/2017-radchenko-fourier-interpolation-real-line.pdf
topic: general-knowledge
cites:
---

# Fourier interpolation on the real line

**Authors:** D. Radchenko, M. Viazovska  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1701.00265

## One-line
Constructs an explicit Fourier interpolation formula recovering any even Schwartz function on $\mathbb{R}$ from its values and Fourier-transform values at $\pm\sqrt{n}$, $n \in \mathbb{Z}_{\geq 0}$.

## Key claim
For every even Schwartz $f:\mathbb{R}\to\mathbb{R}$ and every $x\in\mathbb{R}$, $f(x) = \sum_{n\geq 0} a_n(x) f(\sqrt n) + \sum_{n\geq 0} \widehat{a_n}(x)\widehat f(\sqrt n)$, where $\{a_n\}$ is an explicit basis built from weakly holomorphic modular forms of weight $3/2$ for the theta group $\Gamma_\theta$. The map $\Psi(f) = (f(\sqrt n),\widehat f(\sqrt n))_{n\geq 0}$ is an isomorphism onto $\ker L$, where $L$ is the single linear relation imposed by Poisson summation; an analogous theorem holds for odd Schwartz functions using weight $1/2$ forms.

## Method
Define generating kernels $K^\pm(\tau,z) = \theta(\tau)(\cdots)\theta^3(z)J(z)/(J(z)-J(\tau))$ where $J$ is the Hauptmodul for $\Gamma_\theta$ and $\lambda$ the modular lambda; expand to obtain modular forms $g_n^\pm$ with prescribed $q$-expansions. The basis functions are contour integrals $b_n^\pm(x) = \tfrac12\int_{-1}^{1} g_n^\pm(z) e^{i\pi x^2 z}\,dz$ over a semicircle in $\mathbb{H}$, with $\pm 1$-Fourier eigenvalue inherited from the modular transformation $\theta(-1/z) = \sqrt{-iz}\,\theta(z)$ matching $\widehat{e_z} = (-iz)^{-1/2} e_{-1/z}$. Density of Gaussians $\{e_\tau\}_{\tau\in\mathbb{H}}$ in $\mathcal{S}_{\text{even}}$, plus growth bound $|b_n^\pm(x)| \ll n^2$ via Eichler-cohomology-style cocycle estimates near the cusps, gives convergence.

## Result
Theorem 1 (even) and Theorem 7 (odd) give the interpolation formulas; Theorem 2 identifies image of $\Psi$ as $\ker L$ with $L((x_n),(y_n)) = \sum_n x_{n^2} - \sum_n y_{n^2}$ — a single Poisson-summation obstruction. Corollary: if $f$ even Schwartz vanishes with $\widehat f$ at all $\pm\sqrt n$, then $f\equiv 0$ (a rigidity / uniqueness statement). Explicit closed form $d_0^+(x) = \sin(\pi x^2)/\sinh(\pi x)$ — Fourier self-dual function vanishing at $\pm\sqrt n$ for all $n\geq 0$, unique up to scalar (the Ramanujan / Mordell sine-sinh ratio).

## Why it matters here
Direct ancestor of the Cohn–Kumar–Miller–Radchenko–Viazovska sphere-packing solutions in dimensions 8 and 24 — the magic functions there are solutions to a *first-derivative* interpolation problem of exactly this modular-form-on-$\Gamma_\theta$ type. Relevant to **P1 (sphere packing)**, Cohn–Elkies LP bound construction, and any extremal/uncertainty problem where a Fourier-eigenfunction with prescribed roots/values is needed (Beurling–Selberg, autocorrelation problems P14/P15/P16).

## Open questions / connections
- Q1 in paper: does (2) hold whenever the RHS converges absolutely, not just for Schwartz? Sharp growth of $b_n^\pm(x)$ unknown (bound $O(n^2)$ not believed optimal).
- Generates crystalline measures $\mu_x$ — connects to Meyer's quasicrystal theory (ref [11]).
- The $+1$-derivative variant is the engine of Viazovska's $E_8$ proof and CKMRV's Leech-lattice proof; this paper is the function-theoretic backbone.
- Eichler cohomology framing (refs [6],[9],[10]) — alternative organizational principle the authors deliberately avoid for explicitness.

## Key terms
Fourier interpolation, weakly holomorphic modular forms, theta group $\Gamma_\theta$, Hauptmodul $J$, weight 3/2, weight 1/2, Poisson summation, Cohn-Elkies, magic function, sphere packing dimension 8, Leech lattice dimension 24, crystalline measure, Eichler cohomology, Mordell integral, Ramanujan sine-sinh, Viazovska, Radchenko, Schwartz function rigidity, Gaussian density, $\pm\sqrt n$ nodes
