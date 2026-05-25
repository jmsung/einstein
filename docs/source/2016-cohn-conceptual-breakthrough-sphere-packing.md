---
type: source
kind: paper
title: A conceptual breakthrough in sphere packing
authors: Henry Cohn
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.01685
source_local: ../raw/2016-cohn-conceptual-breakthrough-sphere-packing.pdf
topic: general-knowledge
cites:
---

# A conceptual breakthrough in sphere packing

**Authors:** Henry Cohn  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.01685

## One-line
Expository account of Viazovska's 2016 proof that $E_8$ is the densest sphere packing in $\mathbb{R}^8$ (and the Cohn–Kumar–Miller–Radchenko–Viazovska extension to the Leech lattice in $\mathbb{R}^{24}$), explaining how modular forms produce the long-conjectured Cohn–Elkies "magic" auxiliary function.

## Key claim
The Cohn–Elkies linear-programming bound is sharp in $n=8$ and $n=24$: explicit Schwartz functions $f$ with $f(0)=\widehat f(0)$, $\widehat f \ge 0$, and $f(x)\le 0$ for $|x|\ge r$ exist with $r=\sqrt 2$ (matching $E_8$, density $\pi^4/384 \approx 0.2536$) and $r=2$ (matching $\Lambda_{24}$, density $\pi^{12}/12! \approx 0.001929$), proving optimality of these lattices among all sphere packings.

## Method
Cohn–Elkies LP framework: apply Poisson summation $\sum_\Lambda f(x) = \tfrac{1}{\mathrm{vol}(\mathbb{R}^n/\Lambda)}\sum_{\Lambda^*}\widehat f(y)$ to a radial Schwartz $f$; the bound becomes sharp iff $f$ vanishes on $\Lambda\setminus\{0\}$ and $\widehat f$ on $\Lambda^*\setminus\{0\}$. Viazovska's innovation: insert the required double roots by force via a factor $\sin^2(\pi|x|^2/2)$, then express both Fourier eigenfunctions as Laplace transforms $\int_0^\infty g(t)e^{-\pi|x|^2 t}\,dt$ where $g$ is built from (quasi)modular forms — the $+1$ eigenfunction from a weakly holomorphic quasimodular form of weight 0 depth 2 for $SL_2(\mathbb{Z})$ involving $E_2,E_4,E_6$, and the $-1$ eigenfunction from a weight $-2$ weakly holomorphic modular form for $\Gamma(2)$ in $\Theta^4_{\mathbb{Z}}$ and its translate. Contour integration verifies the eigenvalue relations; sign inequalities $t^2\varphi(i/t)\pm\psi(it) \gtrless 0$ reduce to a finite check.

## Result
Explicit closed-form magic functions: $f_8(x)=\sin^2(\pi|x|^2/2)\int_0^\infty[t^2\varphi(i/t)+\psi(it)]e^{-\pi|x|^2 t}\,dt$ with $\varphi=-4\pi(E_2E_4-E_6)^2/[5(E_6^2-E_4^3)]$ and an analogous $\psi$ built from $\Theta^4_{\mathbb{Z}}|T$. The same scheme, with more elaborate modular-form choices guided by Cohn–Miller's conjectured rational Taylor coefficients (e.g. $f_8: 1-\tfrac{27}{10}|x|^2+\dots$, $\widehat f_8: 1-\tfrac{3}{2}|x|^2+\dots$), gives the $\Lambda_{24}$ magic function. These are the only $n>2$ where LP bounds are sharp; in $n=16$ the optimal $r^2\approx 3.0252593\dots$ is not a clean number.

## Why it matters here
Core wisdom for any wiki page on Cohn–Elkies LP bounds, modular-form magic functions, and the role of Poisson summation in extremal lattice problems — directly relevant to einstein arena problems in the sphere-packing / kissing-number / autocorrelation family that use LP duality on the Fourier side. Adds the conceptual scaffolding (why LP is sharp only in $n=8,24$, what "magic function" means structurally, how forced roots + Laplace transform of modular forms produce Fourier eigenfunctions with prescribed zeros) that anchors deeper distillations of Viazovska 2016 and Cohn–Kumar–Miller–Radchenko–Viazovska 2016.

## Open questions / connections
- Is there a conceptual reason (beyond classification-of-finite-simple-groups-style sporadicness) that LP is sharp in exactly $n=8,24$? No heuristic rules out further sharp dimensions.
- Can the de Laat–Vallentin SDP hierarchy (LP = level 1) close the $D_4$ case in $\mathbb{R}^4$, where LP is provably not sharp?
- Are the higher Taylor coefficients of $f_8,f_{24}$ irrational, and what arithmetic structure governs them? Cohn–Miller verified rationality only at order $|x|^2$.
- No simple proof of the positivity inequalities $t^2\varphi(i/t)\pm\psi(it)\gtrless 0$ is known — current verification is a finite computation.
- Lower-bound side: Venkatesh's $2^{-n}\cdot n^{\log\log n}$ (special cases) vs Kabatyanskii–Levenshtein $2^{-0.599n}$ upper bound remain exponentially apart.

## Key terms
Cohn-Elkies linear programming bound, magic function, Viazovska, $E_8$ lattice, Leech lattice $\Lambda_{24}$, Poisson summation, modular forms, quasimodular form, Eisenstein series $E_2 E_4 E_6$, theta series, Laplace transform of modular form, Fourier eigenfunction, sphere packing density, $\Gamma(2)$ modular forms, $D_4$ lattice
