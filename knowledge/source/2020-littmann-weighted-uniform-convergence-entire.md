---
type: source
kind: paper
title: Weighted uniform convergence of entire Grünwald operators on the real line
authors: Friedrich Littmann, Mark Spanier
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2011.09910v1
source_local: ../raw/2020-littmann-weighted-uniform-convergence-entire.pdf
topic: author-sweep
cites: 
---

# Weighted uniform convergence of entire Grünwald operators on the real line

**Authors:** Friedrich Littmann, Mark Spanier  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2011.09910v1

## One-line
Extends Fejér's classical Hermite-Fejér interpolation convergence theorem to entire functions of exponential type on $\mathbb{R}$ with homogeneous weights $w_\nu(x) = |x|^{2\nu+1}$, using Bessel-function zeros as interpolation nodes.

## Key claim
For $\nu > -1$, $\nu \neq -\tfrac{1}{2}$, and $\tau > 0$: the entire Grünwald operators $G_{\nu,\tau}f$ (using zeros of $J_\nu$) and $H_{\nu,\tau}f$ (using zeros of $J_{\nu+1}$) — formed from squared Lagrange-type kernels $A_\nu^2(\tau z)/[A'_\nu(t)^2(\tau z - t)^2]$ — define entire functions of exponential type $2\tau$, and $\|(G_{\nu,\tau}f - f)w_\nu\|_\infty \to 0$ as $\tau \to \infty$ for $\nu > -\tfrac{1}{2}$ (resp. $H_{\nu,\tau}$ for $-1 < \nu < -\tfrac{1}{2}$), provided $fw_\nu$ has a uniformly continuous extension to $\mathbb{R}$ vanishing at $0$.

## Method
Departs from the usual "denser auxiliary weight + density argument" route and instead emulates Fejér's original proof. Constructs an extremal $L^1(w_\nu)$-minorant $L_{\nu,\tau}$ of $1/w_\nu$ of exponential type $2\tau$ (via Pólya-Laguerre theory: a Laplace-transform representation $A_{\lambda,\nu}(z) = e^{-\lambda z} - F_\nu(z)\int_0^\lambda e^{-wz}g_\nu(w-\lambda)dw$ with $g_\nu \geq 0$), shows $L_{\nu,\tau} = G_{\nu,\tau}(1/w_\nu)$ via an interpolation identity at Bessel zeros, then splits the error $(G_{\nu,\tau}f - f)w_\nu = (G_{\nu,\tau}f - fL_{\nu,\tau}w_\nu)w_\nu + fw_\nu(L_{\nu,\tau}w_\nu - 1)$ and controls each piece using Laplace-transform $L^\infty$ bounds.

## Result
Theorem 1 establishes uniform weighted convergence under sharp conditions: condition $f(x)w_\nu(x) \to 0$ as $x \to 0$ is shown necessary (fails for $f = 1/w_\nu$ at $\nu = \tfrac{1}{2}$). Theorem 2 generalizes to de Branges spaces $\mathcal{H}^2(E_\tau)$: if $E_\tau$ is Hermite-Biehler with $|\varphi'_\tau(x) - \tau| \leq C$ uniformly, the same Grünwald operator on $T_{A_\tau}$ converges in the weight $|E_\tau|^{-2}$. Corollary 1 covers weights $w = |W|^{-2}$ (e.g. Poisson $dx/(1+x^2)$).

## Why it matters here
General background; no direct arena tie. The Bessel-zero quadrature/interpolation framework and extremal one-sided approximations on $\mathbb{R}$ relate tangentially to Cohn-Elkies-style auxiliary functions used in sphere-packing and autocorrelation bounds, but the paper itself targets approximation theory, not extremal LP bounds.

## Open questions / connections
- Characterize entire functions $A_\tau$ that yield uniformly convergent Grünwald operators for a given weight — even for $w(x) = x^2+1$ the criterion is unclear; dilations of generic Pólya-Laguerre $A$ can make $G_{A_\tau}(1/w)(0) \to \infty$.
- Extends Gervais-Rahman-Schmeisser (1978) entire analog of Fejér beyond $\nu = -\tfrac{1}{2}$ (unweighted, $\sin^2$ kernel) to all homogeneous weights.
- Builds on Carneiro-Littmann (2017) extremal minorants in de Branges spaces, and Gonçalves (2017) derivative interpolation formulas — connects extremal-function theory to uniform interpolation convergence.

## Key terms
Grünwald operator, Hermite-Fejér interpolation, Bessel function zeros, de Branges space, Hermite-Biehler function, entire functions of exponential type, extremal minorant, Pólya-Laguerre, homogeneous weights, reproducing kernel, weighted uniform approximation, Laplace transform representation
