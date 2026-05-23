---
type: source
kind: paper
title: Bounds on density of states and spectral gap in CFT$_{2}$
authors: Shouvik Ganguly, Sridip Pal
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.12636
source_local: ../raw/2019-ganguly-bounds-density-states-spectral.pdf
topic: general-knowledge
cites:
---

# Bounds on density of states and spectral gap in CFT$_{2}$

**Authors:** Shouvik Ganguly, Sridip Pal  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.12636

## One-line
Sharpens upper/lower bounds on the $O(1)$ correction to the Cardy formula for the density of states in 2D CFT, and proves the conjectured optimal asymptotic gap of 1 between consecutive Virasoro primaries via bandlimited "magic" functions borrowed from sphere-packing.

## Key claim
The asymptotic gap between consecutive Virasoro primaries (for $c>1$) is bounded above by $1$ — matching Monster CFT and ruling out Hadamard-type spectral gaps. The lower bound $c_- = 0.5$ on the $O(1)$ correction is optimal as $\delta \to 1^-$, saturated by Monster CFT.

## Method
Convolve the partition function with bandlimited minorants/majorants $\phi_\pm(\Delta')$ of the indicator $\Theta(\Delta' \in [\Delta-\delta, \Delta+\delta])$, whose Fourier transforms have support in $[-2\pi, 2\pi]$ (the heavy-state suppression window). Optimize $\phi_\pm(0)$ subject to sign and support constraints, using sinc-product test functions and — crucially — Cohn–Elkies-style 1D sphere-packing magic functions (eq. 2.12) plus a $\sigma$-deformed family (eq. 2.13). "Bound on bounds" obtained by enforcing positive-definiteness of $\widehat{(\phi_\pm - \Theta)}$ via Bochner's theorem on $n\times n$ sample matrices (analytical + MATLAB).

## Result
Improved bounds: $\exp[s_+(\delta)] = \frac{3\pi(11\delta^2\Lambda_+^2 + 180)}{20\delta^3\Lambda_+^3}$ with $\Lambda_+ = \min(2\pi, 4.9323/\delta)$, giving $\exp[s_+] \le 1.7578$ for $\delta > 0.785$. Lower bound reaches $c_- = 0.5$ for $\delta \ge 1$ (sphere-packing magic function). Optimality proven at $\delta \to 1^-$ via Monster CFT saturation. Bound-on-bounds: $2\pi\widetilde{\phi_-}(0) \le \phi_-(0) \le 1$ for $\delta \le 1$ (Cohn corollary 3.2 modified).

## Why it matters here
General background — connects the Cohn–Elkies LP/magic-function machinery (central to sphere packing, kissing numbers, Cohn–Elkies bounds in this wiki) to Beurling–Selberg extremal-function problems and Tauberian estimates. Directly relevant to any Einstein Arena problem using bandlimited minorant/majorant construction (LP duality, autocorrelation inequalities, uncertainty-principle problems) and the positive-definiteness/Bochner trick for bound-on-bounds.

## Open questions / connections
- Closing the gap between achievable bound and "bound on bounds" for $\delta \neq 1$ — fully resolved later in Mukhametzhanov–Pal arXiv:2003.14316 via Beurling–Selberg extremization.
- Extension to off-diagonal three-point coefficients and ETH-relevant quantities (Pal–Sun arXiv:1910.07727; Collier et al. arXiv:1912.00222).
- Higher-dimensional analogues: bandlimited minorants are tight only in $n=1$; for $n \ge 2$ the sphere-packing optimum departs from the bandlimited extremum.

## Key terms
Cardy formula, Tauberian theorem, bandlimited function, Beurling–Selberg extremal problem, Cohn–Elkies magic function, sphere packing 1D, modular bootstrap, Virasoro primary gap, Monster CFT, Bochner positive-definite, Poisson summation, density of states, indicator minorant/majorant
