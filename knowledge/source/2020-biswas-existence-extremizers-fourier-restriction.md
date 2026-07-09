---
type: source
kind: paper
title: Existence of extremizers for Fourier restriction to the moment curve
authors: Chandan Biswas, Betsy Stovall
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2012.01528
source_local: ../raw/2020-biswas-existence-extremizers-fourier-restriction.pdf
topic: general-knowledge
cites:
---

# Existence of extremizers for Fourier restriction to the moment curve

**Authors:** Chandan Biswas, Betsy Stovall  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2012.01528

## One-line
Proves that the Fourier restriction/extension operator associated to the moment curve $\gamma(t)=(t,t^2,\ldots,t^d)$ admits extremizers, and that $L^p$-normalized extremizing sequences are precompact modulo the operator's symmetries.

## Key claim
For $d\ge 2$ and every $(p,q)$ with $1\le p < \frac{d^2+d+2}{2}$ and $q = \frac{d^2+d}{2}p'$ (Drury's full range), there exists a nonzero $f\in L^p$ with $\|Ef\|_q = \|E\|_{L^p\to L^q}\|f\|_p$; for $p>1$, every normalized extremizing sequence has a subsequence converging in $L^p$ to an extremizer after applying dilations, translations (boosts), and modulations.

## Method
Lions-style concentration-compactness combined with Lieb's missing-mass method, adapted from Stovall's paraboloid work [18]. Two new ingredients: (1) a $d$-linear-to-linear refinement extending Tao–Vargas–Vega's bilinear-to-linear argument, requiring a novel Whitney decomposition on $d$-tuples of dyadic intervals (with off-diagonal annular tubes $T_r$ and a $\mathrm{GL}(d)$-equivariant partition of unity); (2) a Marcinkiewicz-interpolation-style trick to push the multilinear range $p<d+2$ up to the full Drury range $p<\frac{d^2+d+2}{2}$. The endgame is an $L^p$ profile decomposition (Prop. 5.1) with $L^q$ almost-orthogonality from curvature/stationary phase.

## Result
Refined extension estimate (Prop. 3.1): $\|Ef\|_q \lesssim \big(\sup_{k,n,I}2^{-c_p n}\|f_I^n\|_p\big)^{1-\theta}\|f\|_p^\theta$ with $f_I^n := f\chi_I\chi_{\{|f|<2^n\|f\|_p|I|^{-1/p}\}}$. This is iterated to extract finitely many well-localized pieces (Lemma 4.2), upgraded to compact support + boundedness modulo symmetries (Prop. 4.1), then promoted to $L^p$ convergence via profile decomposition (Prop. 5.1) yielding Theorem 1.1. Corollary 1.2 transfers the result to the dual restriction operator $Rg(t) = \hat g(\gamma(t))$.

## Why it matters here
General background; no direct arena tie. Concentration-compactness for higher-codimension Fourier restriction is methodology-adjacent to functional inequalities and uncertainty/autocorrelation problems, but moment-curve extremizers are not a known ingredient in any of the 23 Einstein Arena problems.

## Open questions / connections
- Extension to general curves with comparable torsion — flagged by authors as forthcoming; Whitney decomposition uses moment-curve symmetries fundamentally.
- Intermediate-dimension manifolds (codim > 1 and dim > 1) — authors call this "extremely interesting" and entirely open.
- Sublevel sets of Gaussian curvature on higher-order hypersurfaces naturally reduce to lower-dimensional manifold restriction (cf. [16]); concrete extremizer shapes / sharp constants are not computed here.

## Key terms
Fourier restriction, Fourier extension, moment curve, Drury's theorem, concentration-compactness, profile decomposition, missing mass method, Tao-Vargas-Vega bilinear-to-linear, Whitney decomposition, extremizer existence, Lieb, Lions, stationary phase
