---
type: source
kind: paper
title: From sphere packing to Fourier interpolation
authors: Henry Cohn
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2407.14999v1
source_local: ../raw/2024-cohn-sphere-packing-fourier-interpolation.pdf
topic: general-knowledge
cites: 
---

# From sphere packing to Fourier interpolation

**Authors:** Henry Cohn  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2407.14999v1

## One-line
An expository account of how Viazovska's modular-form construction of the $E_8$ magic function led to the Radchenko–Viazovska Fourier interpolation theorem, with a full sketch of the latter's proof.

## Key claim
Every even Schwartz function $f:\mathbb{R}\to\mathbb{R}$ is reconstructible from $\{f(\sqrt{n}),\hat f(\sqrt{n})\}_{n\ge 0}$ via an explicit interpolation basis $\{a_n,\tilde a_n\}$ built from modular forms (Radchenko–Viazovska, 2019); the second-order radial analogue in dimensions $n=8,24$ on points $\sqrt{2k}$ underlies the $E_8$/Leech magic functions.

## Method
Cohn–Elkies LP-bound + Poisson summation reduce optimality of $E_8/\Lambda_{24}$ to constructing radial Schwartz $f$ vanishing on prescribed lattice-length sets with matching sign conditions on $f$ and $\hat f$. The interpolation theorem is proved by building generating functions $F(\tau,x)=\sum a_n(x)e^{n\pi i\tau}$ as contour integrals $\int_{-1}^{1} K(\tau,z)e^{\pi i z x^2}\,dz$, where the kernels $K,\tilde K$ are meromorphic on $\mathbb{H}\times\mathbb{H}$ assembled from $\theta(z)$, $\lambda(z)$, and the $\Gamma_\theta$-Hauptmodul $J=\lambda(1-\lambda)/16$. Three functional equations ($\tau\!\to\!\tau+2$ in $F$ and $\hat F$ plus $F(\tau,x)+(-i\tau)^{-1/2}\hat F(-1/\tau,x)=e^{\pi i\tau x^2}$) together with Gaussians being dense in even Schwartz space close the argument; the inhomogeneous Gaussian term arises from a residue at $z=\tau$ of $K$.

## Result
Explicit closed forms: $K(\tau,z)=\theta(\tau)\theta(z)^3\,[J(z)(1-2\lambda(\tau))+J(\tau)(1-2\lambda(z))]/[4(J(z)-J(\tau))]$ and a sign-flipped variant for $\tilde K$; equivalently in $h=1-2\lambda$, $K=\theta(\tau)\theta(z)^3(1-h(\tau)h(z))/[4(h(\tau)-h(z))]$. With the redundancy $a_0=\tilde a_0$ imposed (from Poisson over $\mathbb{Z}$), the basis is unique and the interpolation series converges absolutely; the $n=8,24$ second-order theorem (Cohn–Kumar–Miller–Radchenko–Viazovska 2022) is structurally analogous and yields universal optimality of $E_8,\Lambda_{24}$.

## Why it matters here
Direct context for the **Cohn–Elkies magic-function** framework that drives sphere-packing/kissing/autocorrelation LP-bound problems on the arena (P1, P6, P15, P16, P17). Clarifies the *algebraic mechanism* — interpolation points $\sqrt{n}$ are forced because $e^{\pi i\tau x^2}|_{x=\sqrt{n}}=e^{n\pi i\tau}$ — explaining why magic-function root patterns are not negotiable and where LP sharpness can/can't occur (known sharp only at $n=1,2,8,24$; provably non-sharp at $n=3{-}6,12,16$).

## Open questions / connections
- Density/perturbation of admissible interpolation point sets (Adve; Kulikov–Nazarov–Sodin; Ramos–Sousa).
- Klein–Gordon uniqueness ↔ Fourier interpolation duality (Hedenmalm–Montes-Rodríguez; Bakan et al.).
- Conformal-bootstrap connection: Mazáč–Paulos bases ↔ Fourier interpolation bases, equivalence of LP bounds with spinless modular bootstrap (Hartman–Mazáč–Rastelli).
- Nonradial / higher-dim / zeta-zero interpolation extensions (Stoller; Bondarenko–Radchenko–Seip; Sardari).

## Key terms
Fourier interpolation, Radchenko–Viazovska theorem, Cohn–Elkies LP bound, magic function, $E_8$ lattice, Leech lattice, modular forms, theta function, Hauptmodul, Poisson summation, $\Gamma_\theta$, sphere packing, uncertainty principle, Schwartz functions, conformal bootstrap
