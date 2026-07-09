---
type: source
kind: paper
title: Convergence in $\C$ of series for the Lambert $W$ Function
authors: G. Kalugin, D. J. Jeffrey
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1208.0754
source_local: ../raw/2012-kalugin-convergence-series-lambert-function.pdf
topic: general-knowledge
cites:
---

# Convergence in $\C$ of series for the Lambert $W$ Function

**Authors:** G. Kalugin, D. J. Jeffrey  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1208.0754

## One-line
Establishes precise real and complex domains of convergence for three asymptotic series of the Lambert $W$ function, and introduces a one-parameter invariant transformation that enlarges those domains.

## Key claim
For $y^\alpha e^y = x$ (so $y = \alpha W(x^{1/\alpha}/\alpha)$), the Comtet–de Bruijn double series (1.3) in $(\sigma,\tau) = (1/\ln x,\;\alpha\ln\ln x/\ln x)$ converges iff $\Re W_{-1}(-e^{\tau/\sigma - 1}) > \tau/\sigma - 1 - \ln\sigma$; for $W$ itself ($\alpha=1$) this collapses to $x > e$. The Stirling-2nd-kind series (1.5) converges on the much larger region $x > x_1 = e^{1/\sigma_1} \approx 1.004458$ with $\sigma_1 \approx 224.79$, and the Wright-$\omega$ series (1.6) converges on $e^{-\sqrt{1+\pi^2}} < x < e^{\sqrt{1+\pi^2}}$.

## Method
Implicit-function theorem applied to the fundamental relation $1 - e^{-u} + \sigma u - \tau = 0$: critical points where $\partial_u G = 0$ give $\sigma_m = 1/W_m(-e^{\lambda-1})$, and the nearest singularity to the origin sets the radius of convergence. Weierstrass preparation theorem identifies square-root branch points at $\tau_*^{(0,1)} = 1+\sigma-\sigma\ln\sigma \pm i\pi\sigma$; Darboux's theorem then extracts asymptotics of expansion coefficients. Lagrange inversion on $W(e^t) + \ln W(e^t) = t$ produces three equivalent representations of the coefficients in terms of second-order Eulerian numbers, associated Stirling numbers of the 1st kind, and 2-associated Stirling subset numbers.

## Result
Series (1.3) converges for $x > x_\alpha$ with $x_\alpha = (e/\alpha)^\alpha$ for $0<\alpha\le 1$ and $x_\alpha = e^\alpha \eta_0 \csc\eta_0$ (where $\eta_0\cot\eta_0 = 1-\ln\alpha$) for $\alpha>1$; the complex domain is split by branch choice $W_{-1}$ vs $W_1$ across $\arg z = 0$. An invariant transformation $W(z) = [\ln z + p] - [\ln(\ln z + p) + \ldots]$ adds a free parameter $p$ that monotonically widens the convergence domain as $p$ increases but with non-monotone effect on convergence rate; numerical experiments suggest optimal $p \approx -0.5$ to $-0.75$ at fixed truncation depth. The three coefficient representations yield the Carlitz–Riordan identities and a closed-form alternating sum $\sum_{p=0}^{m-1}(-1)^{p+m-1}\langle\!\langle{p+m-1\atop p}\rangle\!\rangle_{\ge 2} = (m-1)!$.

## Why it matters here
General background; no direct arena tie. The branch-point asymptotics and Weierstrass-preparation technique for locating square-root singularities of implicitly-defined functions could inform parameterization choice when an arena optimizer's objective has implicit-equation structure, but the immediate subject (Lambert-$W$ series) is not among the 23 problem families.

## Open questions / connections
- Optimal-$p$ selection: is there a closed-form or cheap predictor for the $p$ maximizing accuracy at fixed truncation $N$? Paper observes $p\approx -0.5$ empirically but offers no theory.
- Extension to other branches: section 5 sketches $W_{-1}$ with complex $p = i\pi$ but leaves the general $W_k$ case untreated.
- Convergence-acceleration via the invariant transformation could be tested on other transcendental series with branch-point-limited radius (e.g., Wright $\omega$, generalized Lambert).

## Key terms
Lambert W function, Wright omega function, asymptotic series, radius of convergence, Weierstrass preparation theorem, implicit function theorem, Lagrange inversion, Stirling cycle numbers, 2-associated Stirling subset numbers, second-order Eulerian numbers, Carlitz-Riordan identities, branch points, Darboux theorem, Comtet, de Bruijn
