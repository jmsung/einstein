---
type: source
kind: paper
title: Extremal functions in de Branges and Euclidean spaces, II
authors: E. Carneiro, Friedrich Littmann
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1508.02436
source_local: ../raw/2015-carneiro-extremal-functions-branges-euclidean.pdf
topic: general-knowledge
cites:
---

# Extremal functions in de Branges and Euclidean spaces, II

**Authors:** E. Carneiro, Friedrich Littmann  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1508.02436

## One-line
Constructs optimal one-sided entire majorants/minorants of exponential type for the multidimensional Gaussian $x \mapsto e^{-\pi\lambda|x|^2}$ on $\mathbb{R}^N$ under weighted $L^1$ error with weight $|x|^{2\nu+2-N}$, then lifts the construction by parameter integration to a broad class of radial functions.

## Key claim
For $\nu > -1$, $\lambda > 0$, $\delta > 0$ there exist radial entire functions $L_{\nu,N}, M_{\nu,N}$ of exponential type $\le \delta$ that minorize/majorize $F_\lambda(x)=e^{-\pi\lambda|x|^2}$ on $\mathbb{R}^N$ with extremal weighted $L^1$-error $U^{N\pm}_\nu(\delta,\lambda) = \tfrac12 \omega_{N-1} U^{1\pm}_\nu(\delta,\lambda)$, where the 1D extremum is given explicitly by an interpolation sum over zeros of $A_\nu/B_\nu$ (Bessel-type companions), e.g. $U^{1-}_\nu(2,\lambda) = \Gamma(\nu+1)/(\pi\lambda)^{\nu+1} - \sum_{A_\nu(\xi)=0} e^{-\pi\lambda\xi^2}/(c_\nu K_\nu(\xi,\xi))$.

## Method
Gaussian-subordination: reduce the multidim radial problem to a 1D weighted problem in a homogeneous de Branges space $\mathcal{H}(E_\nu)$ with $E_\nu = A_\nu - iB_\nu$ (Bessel-type Hermite–Biehler function). Build extremal interpolants at zeros of a Laguerre–Pólya function via Laplace-transform representations $1/F(z) = \int g_c(t) e^{-zt}\,dt$, decompose $L^1(|E|^{-2}dx)$ functions of type $2\tau(E)$ as differences of squares in $\mathcal{H}(E)$, and apply Plancherel in $\mathcal{H}(E)$. Then integrate the base parameter $\lambda$ against a nonneg Borel measure $\mu$ on $(0,\infty)$ to cover broad radial classes.

## Result
Theorem 1 gives sharp 1D weighted bounds in any de Branges space $\mathcal{H}(E)$ satisfying (P1)–(P4). Theorem 2 transfers to $\mathbb{R}^N$ with explicit scaling $U^{N\pm}_\nu(\delta,\lambda)=\kappa^{2\nu+2}U^{N\pm}_\nu(\kappa\delta,\kappa^2\lambda)$ and the angular reduction $\tfrac12\omega_{N-1}$. Theorem 3 extends to any radial $G_{\mu,N}(x)=g_\mu(|x|)$ whose Fourier transform (in dimension $N_\nu=\lceil 2\nu+2\rceil$) matches $\int_0^\infty \lambda^{-N_\nu/2} e^{-\pi|t|^2/\lambda}\,d\mu(\lambda)$ under moment conditions (1.23)/(1.24); Theorem 16 yields Hilbert-type inequalities for well-spaced point sets; Theorems 18–19 give periodic (trig-polynomial) analogues via Jacobi $\theta_3$. The Gaussian-subordination class strictly contains the earlier exponential-subordination class (the Gaussian itself is not in the exponential class).

## Why it matters here
Direct relevance to Einstein Arena problems framed via Beurling–Selberg / Cohn–Elkies / LP-bound machinery — particularly sphere packing, kissing-number, autocorrelation inequalities, and uncertainty problems where one needs sharp band-limited (exponential-type) one-sided approximants of radial Gaussians under power-weighted $L^1$ metrics. Provides the most general construction currently available and underlies bounds for $\zeta$, Hilbert-type inequalities, and large-sieve type estimates that recur across the arena's analytic-number-theory-flavored problems.

## Open questions / connections
- Uniqueness of multidim extremizers outside the radial class (only known under extra conditions on $E$; cf. Gonçalves [21]).
- Whether Gaussian subordination can solve extremal problems for non-radial multidim targets, or for non-power weights beyond the homogeneous de Branges spaces.
- Quantitative arena applications: plugging the explicit $U^{N\pm}_\nu(\delta,\lambda)$ into Cohn–Elkies-type LP bounds for sphere packing and into discrete Hardy–Littlewood–Sobolev (eq. 6.12, valid for $\sigma>-N$ minorant, $\sigma>0$ majorant — improves prior $-N<\sigma<1$).
- Extends Holt–Vaaler [27] (characteristic functions of balls) and Carneiro–Littmann [11] (exponential subordination).

## Key terms
Beurling–Selberg extremal problem, Gaussian subordination, de Branges spaces, Hermite–Biehler function, Laguerre–Pólya function, exponential type, Paley–Wiener, Bessel functions $J_\nu$, reproducing kernel Hilbert space, radial majorant/minorant, Hilbert-type inequality, large sieve, Cohn–Elkies LP bound, Jacobi theta function, Hardy–Littlewood–Sobolev, Holt–Vaaler
