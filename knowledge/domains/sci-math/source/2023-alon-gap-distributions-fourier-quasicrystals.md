---
type: source
kind: paper
title: Gap distributions of Fourier quasicrystals via Lee-Yang polynomials
authors: Lior Alon, C. Vinzant
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2307.13498
source_local: ../raw/2023-alon-gap-distributions-fourier-quasicrystals.pdf
topic: general-knowledge
cites:
---

# Gap distributions of Fourier quasicrystals via Lee-Yang polynomials

**Authors:** Lior Alon, C. Vinzant  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2307.13498

## One-line
Characterizes when the Kurasov-Sarnak construction of N-valued Fourier quasicrystals from Lee-Yang polynomials yields non-periodic FQs with unit coefficients and uniformly discrete support, and proves existence of a well-defined gap distribution for every $\mathbb{N}$-FQ.

## Key claim
For $p \in \mathrm{LY}_d(n)$ with $n \geq 2$ and $\mathbb{Q}$-linearly independent $\ell \in \mathbb{R}^n_+$, the FQ $\mu_{p,\ell}$ is non-periodic with unit coefficients and uniformly discrete support iff (i) $\nabla p \neq 0$ on the torus zero set and (ii) $p$ has a non-binomial factor — and these conditions cut out a semi-algebraic open dense subset of $\mathrm{LY}_d(n)$. Every $\mathbb{N}$-FQ has a well-defined gap distribution $\rho_{p,\ell}$ with finitely many atoms plus an absolutely continuous part (which vanishes iff $\mu$ is periodic).

## Method
Reduces to torus zero sets $\Sigma_p \subset \mathbb{T}^n$ of Lee-Yang polynomials (no zeros in $\mathbb{D}^n$ nor in $(\mathbb{C}\setminus\overline{\mathbb{D}})^n$); uses Borcea-Brändén stability preservers, Möbius transfer to real-stable polynomials, and Hurwitz's theorem for the genericity / perturbation argument. Gap distribution existence comes from an ergodic dynamical system $T_\ell$ on $\Sigma_p$ whose invariant measure $m_\ell$ pushes forward under the first-return-time map $\tau_\ell$ to give $\nu_{p,\ell}$; atoms classified via factorization of $p$, and absolute continuity uses the co-area formula on $\mathrm{reg}(\Sigma_p)$. Lang's $G_m$ theorem bounds intersections of $\Lambda$ with arithmetic progressions / low-$\dim_\mathbb{Q}$ sets.

## Result
Density: $\mu_{p,\ell}([x,x+T]) = \tfrac{\langle d,\ell\rangle}{2\pi}T + \mathrm{err}$ with $|\mathrm{err}| \leq |d|$, and every gap $\leq \tfrac{2\pi|d|}{\langle d,\ell\rangle}$ (tight, achieved by $p = \prod (1-z_j)^{d_j}$). Atom count: if $p$ has $N$ non-binomial and $M$ binomial distinct irreducible factors, $\rho_{p,\ell}$ has at most $\binom{N}{2} + M + 1$ atoms; irreducible non-binomial $p$ gives purely absolutely continuous $\rho_{p,\ell}$. Two limit regimes (Theorem 1.18, $\ell \to \mathbf{1}$): $p(z)=\prod_{j=1}^n(1-z_j)$ → Poisson gap statistics as $n\to\infty$; $p_u(z)=\det(1-\mathrm{diag}(z)u)$ with $u \sim \mathrm{Haar}(U(n))$ → CUE gap distribution.

## Why it matters here
General background; no direct arena tie — Fourier quasicrystals, Lee-Yang / real-stable polynomials, and CUE-vs-Poisson gap statistics aren't on the current 23-problem inventory. Closest weak ties are to autocorrelation / uncertainty problems (Fourier-side structure) and to discrete-geometry problems where uniformly discrete point sets appear; the stability-preserver machinery (Borcea-Brändén) is a potential cross-pollination tool if any arena problem reduces to real-stable polynomials.

## Open questions / connections
- Extends Kurasov-Sarnak ([16]) by characterizing the generic locus and giving an explicit perturbation $p_\lambda = p + \sum \lambda_j q_j$ achieving condition (i).
- Generalizes quantum-graph gap-distribution results ([4,7,12]) to arbitrary $\mathbb{N}$-FQs including the non-$\mathbb{Q}$-linearly-independent edge-length case.
- Leaves open: explicit rate of convergence to Poisson / CUE; multivariate ($n$-dimensional) Fourier quasicrystals with the same structural inverse theorem; characterizing $\rho_{p,\ell}$ atom locations beyond the counting bound.

## Key terms
Fourier quasicrystal, Lee-Yang polynomial, real-stable polynomial, Kurasov-Sarnak construction, torus zero set, gap distribution, CUE, Poisson statistics, Borcea-Brändén, crystalline measure, Meyer quasicrystal, Lang $G_m$ theorem
