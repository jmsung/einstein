---
type: source
kind: paper
title: Band-limited maximizers for a Fourier extension inequality on the circle
authors: Diogo Oliveira e Silva, Christoph Thiele, Pavel Zorin-Kranich
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1806.06605v2
source_local: ../raw/2018-silva-band-limited-maximizers-fourier-extension.pdf
topic: general-knowledge
cites: 
---

# Band-limited maximizers for a Fourier extension inequality on the circle

**Authors:** Diogo Oliveira e Silva, Christoph Thiele, Pavel Zorin-Kranich  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1806.06605v2

## One-line
Numerical verification that, among real-valued functions on $S^1$ with Fourier modes up to degree $30$, constants uniquely maximize the endpoint Tomas–Stein adjoint restriction functional $\Phi(f) = \|\widehat{f\sigma}\|_{L^6(\mathbb{R}^2)}^6 / \|f\|_{L^2(S^1)}^6$.

## Key claim
**Theorem 1:** if $f \in L^2(S^1)$ is nonnegative, antipodally symmetric, and band-limited to $|\hat f(n)| = 0$ for $|n| > 30$, then $\Phi(f) \le \Phi(1)$, with equality iff $f$ is constant. The constant $\Phi(1) = (2\pi)^4 \int_0^\infty J_0(r)^6 r\,dr$ (the 5-step uniform random-walk return density $p_5(1)$).

## Method
Plancherel + Foschi's symmetric weight insertion reduces the sharpness inequality to positive semi-definiteness of a Hermitian quadratic form $Q_{m,n}$ on $\mathrm{Sym}((2\mathbb{Z}\cap[-30,30])^3)$. A change-of-variables symmetry $Q_{m,n} = \omega^{d(m)-d(n)} Q_{m,n}$ block-diagonalizes the matrix by $D = m_1+m_2+m_3$. Each block is evaluated via Bessel integrals $I_k = \int_0^\infty \prod_j J_{k_j}(r)\, r\, dr$, computed by Newton–Cotes quadrature on $[0,S]$ and $[S,R]$ (20-digit Mathematica tables) plus an analytic asymptotic tail on $[R,\infty)$; rigorous error bounds (Schur test, operator norm $<10^{-5}$) verify each block's minimum eigenvalue exceeds the error.

## Result
All $46$ blocks $D \in \{0,2,\dots,90\}$ have minimum eigenvalue $\ge 3.5\times 10^{-4}$, with $\lambda_{\min}$ monotonically increasing in $D$ (e.g. $D=0$: $0.00035$; $D=90$: $0.20081$). Constants are the unique real-valued maximizer in the bandwidth-30 antipodally-symmetric class; the kernel direction $\delta_{(0,0,0)}$ exactly accounts for the constant function.

## Why it matters here
Worked example of the "reduce a sharp extension/restriction inequality to positive-semidefiniteness of a finite-rank Hermitian block-diagonal form, then certify numerically with rigorous error bounds" pipeline — directly transferable to sphere-packing / autocorrelation / uncertainty-principle problems where a Cohn–Elkies-style magic function is conjectured optimal. The Bessel-integral asymptotic-tail-plus-quadrature scheme with Schur-test error control is a reusable recipe for any radial-Fourier sharp-constant problem.

## Open questions / connections
- Extend the certificate to unbounded bandwidth (full $L^2(S^1)$); the cluster of small eigenvalues in the $D=0$ block is tied to antipodally-concentrated near-competitors that must be analytically separated.
- Find an analytic explanation for monotonicity of $\lambda_{\min}(D)$ in $D$, and for the circular/hexagonal patterns visible in rows of $Q$.
- Exact closed form for $\int_0^\infty J_0(r)^6 r\,dr$ ($= p_5(1)$) is open, while $p_4(1)$ has a striking modular-form evaluation [Borwein–Straub–Wan–Zudilin].
- Parallels Gonçalves's analogous program for the paraboloid (arXiv:1702.08510) and Foschi's program for the 2-sphere.

## Key terms
Tomas–Stein inequality, Fourier extension, adjoint restriction, sharp constants, band-limited functions, antipodal symmetry, Foschi program, positive semi-definite quadratic form, Bessel integrals, Newton–Cotes quadrature, Schur test, uniform random walk, magic function, Carneiro–Foschi–Oliveira-e-Silva–Thiele, Gonçalves paraboloid
