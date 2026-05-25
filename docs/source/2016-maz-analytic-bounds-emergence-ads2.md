---
type: source
kind: paper
title: Analytic bounds and emergence of AdS2 physics from the conformal bootstrap
authors: D. Mazáč
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.10060
source_local: ../raw/2016-maz-analytic-bounds-emergence-ads2.pdf
topic: general-knowledge
cites:
---

# Analytic bounds and emergence of AdS2 physics from the conformal bootstrap

**Authors:** D. Mazáč  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.10060

## One-line
Constructs analytic extremal functionals for the 1D conformal bootstrap that prove the optimal gap bound $\tilde\Delta = 2\Delta_\psi + 1$ and lift to a twist bound in 2D, with a large-$\Delta_\psi$ limit recovering massive AdS$_2$ scattering physics.

## Key claim
For unitary 1D CFTs with global $SL(2)$ symmetry, the leading non-identity operator in the $\psi\times\psi$ OPE satisfies $\Delta \le 2\Delta_\psi + 1$ — proven analytically for $\Delta_\psi \in \mathbb{N}/2$ by explicit construction of extremal functionals. In 2D (no Virasoro assumed), the minimal non-identity twist obeys $\tau \le 2\Delta_\phi + 2$.

## Method
Introduces a new basis of bootstrap functionals: integrals of the discontinuity of conformal blocks across the branch cut $z\in(1,\infty)$ against integral kernels expanded in Legendre polynomials of $x=(z-1)/z$, rather than $z$-derivatives at $z=1/2$. The Zhukovsky map $z(y)=(1+y)^2/[2(1+y^2)]$ exposes why derivative functionals fail (coefficients diverge as $N^{j-1}$). Extremal kernels $\tilde h(x)$ are fixed analytically via overlaps with Legendre-$Q$ and resonantly-forced Legendre solutions, with closed forms involving $\log(1-x)$ and $\text{Li}_2$.

## Result
The optimal 1D gap bound $\tilde\Delta = 2\Delta_\psi + 1$ is saturated by the generalized free fermion (boundary of free massive Majorana in AdS$_2$), with spectrum $\Delta_j = 2\Delta_\psi + 2j+1$ at second-order zeros of $\omega_{\Delta_\psi}$. At large $\Delta_\psi$, the functional reproduces (i) exponential suppression $(c_{\psi\psi O})^2 \sim [v(\mu)]^{-\Delta_\psi}$ with $v(\mu) = 4^{2+\mu}|\mu-2|^{2-\mu}(\mu+2)^{-(2+\mu)}$ for bound states, (ii) universal two-particle spectral density, and (iii) the sum rule $\sum_{\mu_O=2}(c_{\psi\psi O})^2 = (2\alpha/\sqrt\pi)\Delta_\psi^{-\delta_O+1/2}/[\Gamma(\frac{1-\delta_O}{2})\Gamma(\frac{3-\delta_O}{2})]$ tying CFT data to flat-space S-matrix analyticity.

## Why it matters here
General background; no direct arena tie. The technical engine — replacing derivative functionals at $z=1/2$ with integral-kernel functionals on the branch cut, indexed by orthogonal polynomials — is methodologically suggestive for LP-bound problems (Cohn–Elkies sphere packing, kissing, autocorrelation) where the choice of dual basis controls bound tightness; the Zhukovsky-conformal-map perspective on radius-of-convergence limits of derivative-at-a-point bases is the transferable lesson.

## Open questions / connections
- Generalization of the kernel construction to $d>2$ where bootstrap bounds show kinks at interacting CFTs (3D Ising).
- Does the analytic structure of extremal functionals for OPE-coefficient bounds match the S-matrix bootstrap bounds of Paulos–Penedones–Toledo–van Rees–Vieira?
- Can the same machinery prove the analogous bounds for non-integer/half-integer $\Delta_\psi$, where double zeros need non-equally-spaced placements?
- Application to mixed-correlator bootstrap and modular bootstrap (cf. Collier–Lin–Yin).

## Key terms
conformal bootstrap, extremal functional, crossing symmetry, 1D CFT, AdS2/CFT1, Zhukovsky transformation, Legendre polynomial basis, integral kernel functional, conformal block discontinuity, generalized free fermion, S-matrix bootstrap, twist gap, OPE coefficient, Mazáč, Paulos, hypergeometric block
