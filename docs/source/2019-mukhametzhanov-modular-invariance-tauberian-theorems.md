---
type: source
kind: paper
title: Modular invariance, tauberian theorems and microcanonical entropy
authors: Baur Mukhametzhanov, Alexander Zhiboedav
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.06359
source_local: ../raw/2019-mukhametzhanov-modular-invariance-tauberian-theorems.pdf
topic: general-knowledge
cites:
---

# Modular invariance, tauberian theorems and microcanonical entropy

**Authors:** Baur Mukhametzhanov, Alexander Zhiboedav  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.06359

## One-line
Rigorous derivation of the Cardy formula for microcanonical entropy in 2d CFTs via complex tauberian theorems applied to the modular invariance condition, with explicit error estimates tracking the averaging window $\delta$.

## Key claim
For a modular-invariant unitary partition function with positive spectral density, $S_\delta(\Delta) = 2\pi\sqrt{c\Delta/3} + \tfrac{1}{4}\log(c\delta^4/3\Delta^3) + s(\delta,\Delta)$ as $\Delta\to\infty$, where $s(\delta,\Delta)$ has explicit upper/lower bounds $s_\pm(\delta)$ for $\delta > \delta_{\rm gap} = \sqrt{3}/\pi \approx 0.55$; consequently Virasoro-primary spacings cannot exceed $2\delta_{\rm gap}\approx 1.1$ at large $\Delta$ when $c>1$.

## Method
Apply tauberian-style linear functionals to the modularity condition $Z(\beta)=Z(4\pi^2/\beta)$, bounding the indicator of $(\Delta-\delta,\Delta+\delta)$ by band-limited functions $\phi_\pm(\Delta')$ whose Fourier transforms have bounded support $\Lambda$. Combine with the Hartman–Keller–Stoica (HKS) bound to control heavy-operator contributions at finite $\Delta$, and contour-deform kernel integrals (estimates $|G_\pm(\nu)|\le 2e^{-\beta\nu}\min[1,(\Lambda\nu)^{-2}]$) to extract optimal $\Delta^{-1/2}$ error rates.

## Result
Generalized Ingham's tauberian theorem: $F_\rho(\Delta) = (\tfrac{1}{2\pi})(3/c\Delta)^{1/4} e^{2\pi\sqrt{c\Delta/3}}(1+O(\Delta^{-1/2}))$. For holographic CFTs at large $c$ with $\Delta>c/6$ and $\delta\sim c^\alpha$ ($0\le\alpha<1$), $S_\delta(\Delta)=2\pi\sqrt{(c/3)(\Delta+\delta-c/12)}-\tfrac{1}{2}\log c+O(1)$, extending HKS to $\alpha\le 1/2$ and yielding a universal logarithmic correction matching Sen/Carlip after averaging. Bounds verified numerically against the 2d Ising model and the Monster CFT.

## Why it matters here
General background; no direct arena tie — but the *technique* (tauberian functionals with explicit error estimates on Laplace-transform asymptotics, bounding indicator functions by band-limited Fourier-support functions) is a methodological cousin to Cohn–Elkies magic-function constructions and LP-dual bounds used in sphere packing and autocorrelation problems on the wiki.

## Open questions / connections
- Optimal $\phi_\pm$ functions giving sharpest $\delta_{\rm gap}$ and $s_\pm(\delta)$ — left open, in the spirit of Mazac–Paulos analytic functional bootstrap.
- Extension to non-zero angular potential (2d tauberian problem with $\rho(\Delta,J)$).
- Application to thermal two-point functions, ETH in 2d CFT, and higher-d modular-bootstrap setups.

## Key terms
modular invariance, Cardy formula, microcanonical entropy, tauberian theorem, Ingham theorem, HKS bound, Hartman-Keller-Stoica, 2d CFT, Virasoro primaries, spectral density, band-limited functions, holographic CFT, Monster CFT, central charge, partition function, crossing kernel, complex tauberian, modular bootstrap
