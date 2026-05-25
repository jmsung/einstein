---
type: source
kind: paper
title: The work of Maryna Viazovska
authors: Henry Cohn
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2207.06913
source_local: ../raw/2022-cohn-work-maryna-viazovska.pdf
topic: general-knowledge
cites:
---

# The work of Maryna Viazovska

**Authors:** Henry Cohn  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2207.06913

## One-line
Expository account of Viazovska's Fields-medal proof that $E_8$ is the densest sphere packing in $\mathbb{R}^8$, built via a modular-form construction of the Cohn–Elkies magic function.

## Key claim
The $E_8$ root lattice achieves the optimal sphere packing density in $\mathbb{R}^8$, namely $\pi^4/384 \approx 0.2536$ (Viazovska 2017); the Leech lattice $\Lambda_{24}$ achieves the optimum $\pi^{12}/12!$ in $\mathbb{R}^{24}$ (Cohn–Kumar–Miller–Radchenko–Viazovska 2017); both lattices are furthermore *universally optimal* (CKMRV).

## Method
Apply the Cohn–Elkies LP bound: find an even radial Schwartz $f$ with $f(0)=\hat f(0)=1$, $f\le 0$ for $|x|\ge\sqrt 2$, $\hat f\ge 0$; sharpness forces $f$ and $\hat f$ to vanish (with double roots) on the lattice radii $\sqrt{2n}$. Split $f = f_+ + f_-$ into Fourier $\pm 1$ eigenfunctions and represent each as a Laplace-transform / contour integral of a (quasi)modular form on $\Gamma(2)$ — $f_-$ uses $\psi = W^3(5U^2-5UW+2W^2)/\Delta$ (weight $-2$ on $\Gamma(2)$), $f_+$ uses a weakly *quasimodular* form $\chi = (E_2 E_4 - E_6)^2/\Delta$ of weight $0$, depth $2$ on $\mathrm{SL}_2(\mathbb{Z})$. Required inequalities reduce to $\phi(it)\pm\psi(it)$ sign control, checkable via asymptotics + interval arithmetic.

## Result
The constructed magic function $f$ has $\hat r = \sqrt 2$, double roots at $\sqrt{2n}$ for $n\ge 2$, single sign change at $\sqrt 2$, yielding the LP bound that matches the $E_8$ density exactly. Extension via radial Fourier interpolation (Radchenko–Viazovska, then CKMRV) shows radial Schwartz functions on $\mathbb{R}^8$ (resp. $\mathbb{R}^{24}$) are uniquely determined by $f(\sqrt{2n}), f'(\sqrt{2n}), \hat f(\sqrt{2n}), \hat f'(\sqrt{2n})$ for $n\ge 1$ (resp. $n\ge 2$), and gives a +1 *universal optimality* (any completely monotonic pair-potential energy is minimized).

## Why it matters here
Anchors the **Cohn–Elkies magic function** approach used across multiple Einstein Arena problems (sphere packing, kissing number, autocorrelation, uncertainty); demonstrates concretely that *modular forms + Laplace contour integrals* are a viable construction technique for magic functions, and that the right ansatz lives in the **quasimodular** (not just modular) world. Adds Viazovska persona seed and the explicit $\Gamma(2)$ identities $U=V+W$, $U|_2 T = W$, etc.

## Open questions / connections
- Two-dimensional magic function: numerics agree with optimal density to >1000 decimals at $r=(4/3)^{1/4}$, but no proof; what function space supports the analogous interpolation theory?
- Conformal-bootstrap / quantum-gravity reformulation (Hartman–Mazáč–Rastelli): LP bound = spinless modular bootstrap on $d/2$ free bosons — generalizations to higher-spin bootstrap unmapped to discrete geometry.
- Bourgain–Clozel–Kahane sign uncertainty principle is the obstruction; how tight is it beyond $d=8,24$?
- Klein–Gordon uniqueness connections via Bakan–Hedenmalm–Montes-Rodríguez–Radchenko–Viazovska.

## Key terms
sphere packing, $E_8$ lattice, Leech lattice, Cohn–Elkies linear programming bound, magic function, modular forms, quasimodular forms, Eisenstein series $E_2 E_4 E_6$, modular discriminant $\Delta$, $\Gamma(2)$ congruence subgroup, Poisson summation, Fourier eigenfunction, radial Schwartz interpolation, Bourgain–Clozel–Kahane uncertainty, universal optimality, Viazovska, Radchenko, theta series, Laplace transform contour integral
