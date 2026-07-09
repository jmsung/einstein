---
type: source
kind: paper
title: Free partition functions and an averaged holographic duality
authors: N. Afkhami-Jeddi, Henry Cohn, Thomas Hartman, Amirhossein Tajdini
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.04839
source_local: ../raw/2020-afkhamijeddi-free-partition-functions-averaged.pdf
topic: general-knowledge
cites:
---

# Free partition functions and an averaged holographic duality

**Authors:** N. Afkhami-Jeddi, Henry Cohn, Thomas Hartman, Amirhossein Tajdini  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.04839

## One-line
Averages the partition function of free-boson CFTs over Narain moduli, shows the average equals a sum over 3d topologies (a U(1)-gravity Poincaré series), and uses the spinning modular bootstrap to bound the spectral gap of Narain lattices.

## Key claim
The averaged free CFT in 2d is holographically dual (at the torus level) to an exotic 3d "U(1) gravity" with $U(1)^c \times U(1)^c$ symmetry, and via Siegel averaging there exist Narain lattices with spectral gap $\Delta_1 \geq c/(2\pi e) + o(c)$ as $c \to \infty$ (a weaker $c/(4\pi e)$ bound holds even with zero flux $M=0$).

## Method
Two prongs: (1) spinning modular bootstrap — semidefinite programming (SDPB) over derivative functionals at $\tau=-\bar\tau=i$, with eigenfunctions built from generalized Laguerre polynomials $L^{(c/2-1)}_m(4\pi h)$, giving numerical upper bounds on $\Delta_1$ for $c \leq 15$; (2) Siegel–Weil — average over the Narain moduli space $O(c)\times O(c)\backslash O(c,c)/O(c,c,\mathbb{Z})$ using Siegel's measure, identify the result with an Eisenstein series / Poincaré sum, then evaluate the bulk side via the Hardy–Littlewood circle method (major arcs + Chinese remainder + local densities $\sigma_p$ from counting $x\cdot y \equiv \ell \pmod{p^n}$).

## Result
Spinning bootstrap bound matches $\Delta_1 = (c+2)/6$ at $c=1,2,4$ (saturated by $SU(2)_1$, $SU(3)_1$, $SO(8)_1$ WZW models). An **analytic functional** for $c=1$ is constructed: take $g=\chi_R * \chi_R$ with $R$ the square at $(\pm 1/\sqrt{2},0),(0,\pm 1/\sqrt{2})$; then $f = g - \hat g$ is a $-1$-eigenfunction of the Fourier transform proving $\Delta_1 \leq 1/2$ for the self-dual boson — this $g$ is essentially two orthogonal copies of the 1d Cohn–Elkies sphere-packing auxiliary function at $45°$. Putative optimal Narain lattices tabulated for $c\leq 8$: $SU(2)_1, SU(3)_1, SU(4)_1, SO(8)_1, SO(10)_1$, Coxeter–Todd ($c=6$), a new $c=7$ lattice with $\Delta_1=4/3$, and Barnes–Wall ($c=8$, $\Delta_1=\sqrt{2}$). Lemma B.1 gives an exact verification test $(GH^{-1})^2 = I$ for Narain lattices from floating-point Gram data.

## Why it matters here
Direct anchor for sphere-packing problems and the Cohn–Elkies LP-bound family: the $c=1$ analytic functional is the **first exact spin-dependent bootstrap functional** and is a structural cousin of the 1d sphere-packing magic function — a template for constructing optimal auxiliary functions in higher $c$. The verification lemma (B.1) is directly reusable for any Narain-style lattice solution. Identifies Coxeter–Todd ($K_{12}$) and Barnes–Wall ($BW_{16}$) as optimal Narain lattices, tying our sphere-packing wiki to CFT moduli geometry.

## Open questions / connections
- Is there an analytic bootstrap functional for $c=2$ saturating $\Delta_1 = 2/3$ (the $SU(3)_1$ point)? Authors flag this as an open problem; analogous to the open sharpness of the spinless $c=1$ bound.
- Whether the $c=2$ optimal eigenfunction is related to a 2d sphere-packing auxiliary function the same way $c=1$ relates to 1d — authors conjecture yes but cannot pin down a specific relationship.
- Gap between bootstrap upper bound and lattice lower bound: spinning bootstrap gives only constant bounds at large $c$, while averaging gives linear $c/(2\pi e)$ — does a stronger averaging argument (or non-Narain dual) close this?
- Extension of the Siegel–Weil identification to higher-genus boundaries and multi-boundary wormholes (analog of JT/random-matrix).

## Key terms
Narain lattice, modular bootstrap, spinning bootstrap, Cohn–Elkies, sphere packing, Siegel–Weil formula, Eisenstein series, Poincaré series, U(1) gravity, holographic duality, Coxeter–Todd lattice, Barnes–Wall lattice, $E_8$ lattice, self-dual boson, WZW model, analytic functional, SDPB, Hardy–Littlewood circle method, Laguerre polynomial, spectral gap
