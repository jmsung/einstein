---
type: source
kind: paper
title: The first 128 digits of an autoconvolution inequality
authors: Andrew Rechnitzer
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2602.07292v1
source_local: ../raw/2026-rechnitzer-first-128-digits-autoconvolution.pdf
ingested_for_concept: mpmath-ulp-polish.md
cites: 
---

# The first 128 digits of an autoconvolution inequality

**Authors:** Andrew Rechnitzer  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2602.07292v1

## One-line
Computes rigorous bounds pinning down the first 128 digits of the autoconvolution constant $\nu_2^2 = \inf_{f\in\mathcal{F}} \|f*f\|_2^2 / \|f\|_1^2$ on $(-1/2,1/2)$, a constant central to Sidon-set / $B_2[g]$-set asymptotics.

## Key claim
$\nu_2^2 = 0.574639607151519592727255427527052971437026369373156611630876\ldots$ with rigorous upper/lower bounds agreeing to 128 digits (gap $\le 1.2 \times 10^{-129}$), vastly improving White's prior 4-digit bracket $0.574636 < \nu_2^2 < 0.574643$.

## Method
Two-stage ansatz on the Fourier side: (1) fit White's near-optimal coefficients to $\hat f(k) \sim (-1)^k k^{-1/2}\sum_j a_j k^{-j}$, then recognize the optimal $f(x)$ has an inverse-square-root singularity at $x=\pm 1/2$; (2) parameterize $f(x) = \sum_j a_j \binom{j-1/2}{j}(1-4x^2)^{j-1/2}$, giving $\hat F(k)$ as a finite sum of Bessel $J_p(\pi k/2)$. Minimize via Newton–Raphson with Lagrange multipliers; sum Bessel series via Kummer's transform + Hurwitz-zeta tails + ball-arithmetic (FLINT) for rigorous error control. Lower bound via Hölder's inequality applied to a dual $G(x)$ whose Fourier coefficients are tuned to match $\hat F(k)^3$ asymptotically.

## Result
Theorem 1 gives $c_\ell \le \nu_2^2 \le c_u$ with both bounds matching for 128 digits, computed at $P=101$ ansatz terms, $N=8192$ summation cutoff, $K=128$ asymptotic terms, 384-digit precision. The optimal $f$ has an inverse-square-root singularity at the endpoints, with leading behavior $\approx \frac{2}{\pi\sqrt{1-4x^2}}$. Via the Green–White connection, this tightens $\sigma_2(g) \le \sqrt{(2-1/g)/\nu_2^2}$ for $B_2[g]$-sets.

## Why it matters here
Direct rigorous-high-precision pipeline (FLINT ball-arithmetic + Kummer transform + Bessel asymptotics + Hurwitz-zeta tails) that is highly transferable to Einstein Arena problems involving autocorrelation, Sidon-like extremal constants, and any constant defined by an $L^p$ variational principle with smooth optimizer up to boundary singularities. Concept-anchor: singularity-aware ansatz + Hölder dual lower bound is a recipe for converting near-optimal upper-bound solutions into matching rigorous lower bounds.

## Open questions / connections
- Extend to $\nu_p^2$ for general $p \ge 2$ (Problem 35 in Tao–Vu unsolved book) — does the same singularity ansatz $(1-4x^2)^{c}$ work?
- The $\nu_\infty$ constant of Schinzel–Schmidt remains stubbornly second-digit-only; can the same machinery break that barrier, or does $L^\infty$ require a different ansatz?
- $b$-coefficients stabilize around $b_{70}$ — suggests the lower-bound ansatz could be made more efficient; not explored.
- Connection to $\sigma_2(g) = \lim_N R_2[g](N)/\sqrt{gN}$: the new $\nu_2^2$ value tightens upper bounds for small $g$ but $\sigma_2(g)$ existence for $g \ne 1$ still open.

## Key terms
autoconvolution inequality, Sidon sets, $B_2[g]$-sets, $\nu_2$ constant, Fourier coefficients, Bessel functions, Hölder inequality lower bound, Kummer series transform, Hurwitz zeta, FLINT ball arithmetic, ansatz singularity boundary, Rechnitzer, White, Green, Martin–O'Bryant, additive combinatorics
