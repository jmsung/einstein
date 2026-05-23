---
type: source
kind: paper
title: Sphere packing and quantum gravity
authors: Thomas Hartman, D. Mazáč, L. Rastelli
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1905.01319
source_local: ../raw/2019-hartman-sphere-packing-quantum-gravity.pdf
topic: general-knowledge
cites:
---

# Sphere packing and quantum gravity

**Authors:** Thomas Hartman, D. Mazáč, L. Rastelli  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1905.01319

## One-line
Establishes an exact equivalence between the 2D CFT spinless modular bootstrap with $U(1)^c$ chiral algebra and the Cohn–Elkies linear-programming bound for sphere packing in $d=2c$ dimensions, identifying Viazovska's "magic functions" as analytic extremal bootstrap functionals.

## Key claim
The $U(1)^c$ modular bootstrap maps exactly onto the Cohn–Elkies LP for sphere packing in $\mathbb{R}^{2c}$; the optimal extremal functionals at $c=4,12$ reproduce the Viazovska / Cohn–Kumar–Miller–Radchenko–Viazovska magic functions proving optimality of $E_8$ and Leech. For Virasoro modular bootstrap at large $c$, this yields the first analytic improvement over Hellerman: $\Delta_0(c) \lesssim c/8.503$ (vs Hellerman's $c/6$).

## Method
Reformulates the spinless modular bootstrap S-invariance constraint as a linear-programming problem over $-1$ eigenfunctions of the $d=2c$-dimensional Fourier transform (radial Laguerre basis). Imports the analytic extremal functionals $\alpha_n^\pm$, $\beta_n^\pm$ originally constructed by Mazáč (2016) for the 1D CFT four-point bootstrap with $\mathfrak{sl}(2,\mathbb{R})$ symmetry, translating them via $\Delta(x)=x^2/2$ (for $U(1)^c$) into Schwartz functions on $\mathbb{R}^{2c}$ with the prescribed double-zero structure at $r_n=\sqrt{d/8+2n+1}$. Large-$c$ asymptotic bound obtained by saddle-point evaluation of a one-parameter family of improved functionals.

## Result
Three concrete bounds: (i) at $c=4,12$ the functionals are optimal and exactly reproduce Viazovska's $E_8$ proof and Cohn et al.'s Leech-lattice proof; (ii) for $c\in(1,4)\cup(12,\infty)$ a rigorous (but suboptimal) bound $\Delta_{U,V}(c)\le c/8+1/2$ for both $U(1)^c$ and Virasoro; (iii) at large $c$, $\Delta_V(c)\lesssim c/8.503$ — still weaker than the conjectured $c/9.08$ numerics and the Kabatianski–Levenshtein $c/9.796$ implied bound. Also generalizes the Cohn–Kumar–Miller–Radchenko–Viazovska Fourier-interpolation theorem to all dimensions $d$ via a complete basis $\{a_n^\pm,b_n^\pm\}$ of radial Schwartz functions.

## Why it matters here
Directly informs P1 (sphere packing) and any kissing-number / lattice-energy problem in the arena by making explicit the Cohn–Elkies LP machinery, the magic-function construction, and the dimension-by-dimension Fourier-interpolation basis. The dictionary "LP bound $\leftrightarrow$ extremal functional with double zeros at $r_n$" is a transferable optimization recipe: it is the same Remez-equioscillation pattern the wiki already documents for autocorrelation/Cohn–Elkies problems.

## Open questions / connections
- Is the Kabatianski–Levenshtein $\rho \le 2^{-0.599 d + o(d)}$ the true LP asymptote, or can the Cohn–Elkies LP itself be pushed further? (Implies Virasoro $\Delta_V \lesssim c/9.796$.)
- Can the Virasoro bound be tightened to the conjectured $c/9.08$ via compactly-Fourier-supported functionals (Levenshtein 1979; Cohn–Elkies)?
- Is there an analogue of the modular bootstrap that maps to $d=3$ (Kepler) sphere packing? Currently no.
- Are the additional CFT constraints beyond spinless modular bootstrap (spinning bootstrap, four-point crossing) related to the gap between LP bounds and true $\rho_{\max}$ in dimensions $d\ne 1,2,8,24$?

## Key terms
sphere packing, Cohn-Elkies linear programming, magic function, Viazovska, modular bootstrap, $E_8$ lattice, Leech lattice, analytic extremal functional, $U(1)^c$ chiral algebra, Virasoro, Fourier interpolation, Kabatianski-Levenshtein, AdS3 quantum gravity, BTZ black hole, theta function
