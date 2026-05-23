---
type: source
kind: paper
title: Fourier interpolation with zeros of zeta and $L$-functions
authors: Andriy Bondarenko, Danylo Radchenko, Kristian Seip
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2005.02996v3
source_local: ../raw/2020-bondarenko-fourier-interpolation-zeros-zeta.pdf
topic: general-knowledge
cites: 
---

# Fourier interpolation with zeros of zeta and $L$-functions

**Authors:** Andriy Bondarenko, Danylo Radchenko, Kristian Seip  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2005.02996v3

## One-line
Constructs Fourier interpolation bases in which a function analytic in a strip is recovered from its values at $\log n/(4\pi)$ and from values (and derivatives) of its Fourier transform at the imaginary parts of the nontrivial zeros of $\zeta(s)$ (and analogous $L$-functions).

## Key claim
For every even $f$ in the strip-analytic class $H^1$ and every $z$ with $|\mathrm{Im}\,z|<1/2$,
$f(z)=\sum_{n\ge1}\widehat f\!\left(\tfrac{\log n}{4\pi}\right)U_n(z)+\lim_{k\to\infty}\sum_{0<\gamma\le T_k}\sum_{j=0}^{m(\rho)-1}f^{(j)}\!\left(\tfrac{\rho-1/2}{i}\right)V_{\rho,j}(z)$,
with explicit rapidly-decaying entire $U_n,V_{\rho,j}$ satisfying biorthogonal interpolatory conditions (1.3); the formula is non-redundant — removing a single $\log n/(4\pi)$ or a single zero $\rho$ destroys it.

## Method
Build a two-variable Dirichlet-series kernel $D(w,s)=\sum_n\beta_n(s)n^{-w/2}$ from Fourier coefficients of modular integrals $F_k^{\pm}(\tau,s)$ for the theta group $\Gamma_\theta$; show $H(w,s)=\zeta(s)/\zeta(w)\cdot D(w,s)$ obeys the functional equations $H(1-w,s)=-H(w,s)$, $H(w,1-s)=H(w,s)$. Contour-integrate $\tfrac{1}{2\pi i}\int H(w,iz+1/2)\widehat f(\tfrac{w-1/2}{i})dw$ to extract a weighted sum of $\widehat f$-values at $\log n/(4\pi)$ versus a sum of $f$-derivatives at zeta zeros. Strengthens Knopp's abundance principle to generate modular integrals with prescribed functional equations.

## Result
Theorem 1.1 and Corollary 1.1: any even $f\in H^1$ vanishing at all $\log n/(4\pi)$ and all $f^{(j)}((\rho-1/2)/i)$ must vanish identically; an $f$ divisible by $\zeta(1/2+is)$ is determined by $\{f(\log n/(4\pi))\}$. Section 5 extends to nontrivial zeros of Dirichlet $L$-functions with even/odd primitive characters and other Dirichlet series with functional equations. Section 7 sharpens Radchenko–Viazovska (Theorem A): the $\pm\sqrt n$ interpolation holds under the mild condition $\int|f'(x)|(1+|x|)^{1/2}\log^3(e+|x|)dx<\infty$ (and same for $\widehat f$), replacing the prior $(1+|x|)^{-13}$ decay assumption.

## Why it matters here
General background; no direct arena tie. Relevant tangentially to **Fourier interpolation / magic-function** machinery (Cohn–Elkies, Viazovska sphere packing in $d=8,24$) — establishes a duality framework and Dirichlet-series-kernel viewpoint that may inform any P-problem leveraging Poisson/Cohn–Elkies-style $f$-and-$\widehat f$ value constraints (kissing numbers, autocorrelation, uncertainty-principle problems).

## Open questions / connections
- Whether RH must hold for (1.2) to be useful (formula is unconditional; under RH the nodes $(\rho-1/2)/i$ are real, giving a true Fourier-pair interpolation).
- Whether Kulikov's uncertainty-density theorem and Riemann–von Mangoldt zero density match more sharply for other $L$-function families (raised in §2.4).
- Crystalline measures: the framework generates new examples in the Guinand / Kurasov–Sarnak / Lev–Olevskii / Meyer line.
- Extends Radchenko–Viazovska 2019; uses Knopp's abundance principle (1994, 2000); Bochner-type modular relations.

## Key terms
Fourier interpolation, Riemann zeta zeros, Dirichlet $L$-functions, Riemann–Weil explicit formula, Radchenko–Viazovska, theta group $\Gamma_\theta$, modular integrals, weakly holomorphic modular forms, Dirichlet series kernel, functional equation, Knopp abundance principle, Poisson summation, crystalline measures, magic function, Cohn–Elkies, uncertainty principle
