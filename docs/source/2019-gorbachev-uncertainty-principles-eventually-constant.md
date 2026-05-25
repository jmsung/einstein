---
type: source
kind: paper
title: Uncertainty Principles for Eventually Constant Sign Bandlimited Functions
authors: D. Gorbachev, V. Ivanov, S. Tikhonov
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.11328
source_local: ../raw/2019-gorbachev-uncertainty-principles-eventually-constant.pdf
topic: general-knowledge
cites:
---

# Uncertainty Principles for Eventually Constant Sign Bandlimited Functions

**Authors:** D. Gorbachev, V. Ivanov, S. Tikhonov  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.11328

## One-line
Solves the generalized multivariate Logan extremal problem: for positive-definite bandlimited functions on $\mathbb{R}^d$ with vanishing low-order moments, finds the sharp product of "eventually-sign radius" times "spectral support radius."

## Key claim
For $d \in \mathbb{N}$, $m \in \mathbb{Z}_+$, $\inf \lambda((-1)^m f) \cdot \tau(f) = 2 q_{d/2-1, m+1}$, where $q_{\alpha,k}$ is the $k$-th positive zero of $J_\alpha$, with unique extremizer $f_{d/2-1,m}(|x|) = j_{d/2-1}^2(|x|) / \prod_{k=1}^{m+1}(1 - |x|^2/q_{d/2-1,k}^2)$.

## Method
Reduces the multivariate Dunkl/Fourier problem to a 1D Hankel-transform problem in $(\mathbb{R}_+, t^{2\alpha+1} dt)$. Key tools: Gauss/Radau quadrature with Bessel zeros as nodes, Sturm–Liouville Chebyshev-system theory for $\{j_\alpha(q_k t)\}$, and positive-definiteness of $g_{\alpha,m}(t) = j_\alpha(t)/\prod(1 - t^2/q_{\alpha,k}^2)$ via Mehler–Heine + Jacobi polynomial nonnegativity (Cohn–de Courcy-Ireland).

## Result
Theorem 1.1 gives the sharp bound $2 q_{d/2-1, m+1}$ with explicit extremizer. Theorem 1.2 extends to bandlimited functions with both $f$ and $\hat{f}$ moment conditions: $\inf \lambda((-1)^m f)\tau(f) = 2 q_{d/2+s, m+1}$, with extremizers of form $r(x) f_{d/2+s,m}(|x|)$ where $r$ decomposes via harmonic polynomials. For $d=1, m=0,1$ recovers Logan's $\lambda_0 = \pi$, $\lambda_1 = 3\pi$.

## Why it matters here
Directly informs sphere-packing LP-bound and kissing-number magic-function constructions: connects to Bourgain–Clozel–Kahane uncertainty principle $A_d^\pm$, Cohn–Elkies linear programming bounds, and the Viazovska $d=8,24$ proofs. Provides explicit positive-definite bandlimited test functions $f_{\alpha,m}$ usable as feasible points / duals for arena problems in autocorrelation, packing, and uncertainty-principle families.

## Open questions / connections
- Tight relation between $A_d^\pm$ (Bourgain–Clozel–Kahane) and the bandlimited bound $A_d^\pm \leq \pi^{-1} q_{d/2,1}$ — closing the asymptotic gap $d/(2\pi e) \leq A_d^+ \leq d/(2\pi)(1+o(1))$.
- Lattice covering/successive-minima inequality $\mu(L)\lambda_1(L^*) \geq d/(2\pi e)$ (Yudin/Banaszczyk) via the same extremizers — geometry-of-numbers transfer.
- Whether $f_{d/2-1,m}$ extremizers extend to non-radial Dunkl reflection groups beyond $\mathbb{Z}_2^d$.

## Key terms
Logan problem, positive definite functions, bandlimited, Hankel transform, Dunkl transform, Bessel function zeros, Cohn–Elkies, sphere packing LP bound, uncertainty principle, Bourgain–Clozel–Kahane, Gauss quadrature, Sturm–Liouville, Chebyshev system, Mehler–Heine, Jacobi polynomials, Viazovska
