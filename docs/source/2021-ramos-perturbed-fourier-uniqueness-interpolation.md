---
type: source
kind: paper
title: Perturbed Fourier uniqueness and interpolation results in higher dimensions
authors: João P. G. Ramos, Martin Stoller
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.12015
source_local: ../raw/2021-ramos-perturbed-fourier-uniqueness-interpolation.pdf
topic: general-knowledge
cites:
---

# Perturbed Fourier uniqueness and interpolation results in higher dimensions

**Authors:** João P. G. Ramos, Martin Stoller  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.12015

## One-line
Extends Radchenko–Viazovska-style Fourier interpolation/uniqueness to $\mathbb{R}^d$ with *perturbed* nodes: Schwartz functions vanishing (with their Fourier transforms) on surfaces close to the spheres of radius $\sqrt{n}$ must be zero.

## Key claim
For $d \geq 2$, there is $\delta_d > 0$ such that if $\varepsilon_n, \hat{\varepsilon}_n : S^{d-1} \to \mathbb{R}$ satisfy $\sup |\varepsilon_n(\zeta)| + \sup |\hat{\varepsilon}_n(\zeta)| \leq \delta\, n^{-10n - (5/2)d - c}$, then any $f \in \mathcal{S}(\mathbb{R}^d)$ vanishing on the perturbed surfaces $\{\sqrt{n}\zeta + \varepsilon_n(\zeta)\zeta\}$ and whose $\hat{f}$ vanishes on the dual perturbed surfaces is identically zero (Theorem 2). Radial perturbed interpolation (Theorem 1) needs only polynomial-decay perturbations $|\varepsilon_n| + |\hat{\varepsilon}_n| \leq \delta(1+n)^{-d - s/2 - 2 - \eta}$.

## Method
Builds dimension-explicit Schwartz eigenbasis $b^{\pm}_{k,n}$ of the Fourier transform from Bondarenko–Radchenko–Seip modular kernels on the theta group $\Gamma_\theta$, with sharp bounds $\sup_r |(1+r^\beta) b^{\epsilon}_{k,n}(r)|$ controlled in $(\beta, n, k)$ (Theorem A). Treats the perturbed interpolation operator $T$ as identity-plus-small on Banach spaces $V^s(\mathbb{R}^d) = \{f : (1+|x|^s)f, (1+|\xi|^s)\hat{f} \in L^1\}$; invertibility by Neumann series gives uniqueness. Non-radial case uses spherical-harmonic kernels $K_n^d(x,y) = \sum_{m \leq 4n+1} a_{d/2+m,n}(|x|) n^{-m/2} Z_m^d(x,y)$ — the finite sum (because $a_{d/2+m,n}$ vanishes for $m > 4n+1$) is what makes the formal manipulation rigorous.

## Result
(i) Perturbed radial interpolation $f = \sum f(\sqrt{n+\varepsilon_n}) h_{d,n} + \hat{f}(\sqrt{n+\hat{\varepsilon}_n}) \tilde{h}_{d,n}$ converges in $V^s_{\rm rad}$. (ii) Non-radial uniqueness with perturbations as small as double-exponential in $n$. (iii) Corollary 4.1: discrete Fourier uniqueness pairs on $\bigcup_n \sqrt{n} S^{d-1}$ with $O(n^{\alpha_d n + \beta_d})$ points per sphere — a positive counterpart to Radchenko–Stoller non-uniqueness results. (iv) Theorem 3: partial answer to Hedenmalm–Montes-Rodríguez open problem — $(\Gamma, \Lambda)$ with hyperbola $\Gamma$ and perturbed lattice cross $\Lambda$ ($\alpha = \beta = 1$) is a weak Heisenberg uniqueness pair when $|\varepsilon_n| + |\hat{\varepsilon}_n| \leq \delta n^{-7}$.

## Why it matters here
General background; no direct arena tie. Closest adjacency is to **sphere-packing / kissing-number** problems where Cohn–Elkies / Viazovska magic-function machinery (modular forms, Fourier interpolation on $\sqrt{n}$ nodes) drives the SOTA — this paper sharpens the interpolation toolkit those LP-bound constructions sit inside.

## Open questions / connections
- Can the double-exponential perturbation tolerance $n^{-10n - O(d)}$ in Theorem 2 be improved to polynomial (matching the radial case)? Authors suggest no due to absence of free-interpolation structure off the radial axis.
- Theorem 3 only handles $\alpha\beta = 1$ on the hyperbola and the technical class $\{\mu_f : f \in V^{s_0}(\mathbb{R}) \text{ odd}\}$; full answer to Hedenmalm–Montes-Rodríguez open problem for $0 < \alpha\beta \leq 1$ remains open.
- Extends Ramos–Sousa [11] (1D perturbed RV) and Stoller [12] (higher-dim unperturbed) — natural next step is perturbed Cohn–Kumar–Miller–Radchenko–Viazovska universal-optimality interpolation on $E_8$, $\Lambda_{24}$.

## Key terms
Fourier interpolation, Fourier uniqueness pair, Radchenko–Viazovska, Bondarenko–Radchenko–Seip, modular forms, theta group, magic function, Heisenberg uniqueness pair, Cohn–Elkies, sphere packing, Schwartz space, spherical harmonics, perturbation theory, Viazovska, Hedenmalm–Montes-Rodríguez
