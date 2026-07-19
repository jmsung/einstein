---
type: source
kind: paper
title: "Maxima of log-correlated fields: some recent developments"
authors: E. Bailey, J. Keating
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.15141
source_local: ../raw/2021-bailey-maxima-log-correlated-fields-some.pdf
topic: general-knowledge
cites:
---

# Maxima of log-correlated fields: some recent developments

**Authors:** E. Bailey, J. Keating  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.15141

## One-line
A colloquium-level review of progress toward the Fyodorov–Hiary–Keating and Fyodorov–Keating conjectures on extreme values of characteristic polynomials of random matrices from the classical compact groups and of $\zeta(1/2+it)$, framed through the theory of logarithmically-correlated Gaussian fields.

## Key claim
For $A\in U(N)$, $\log|P_N(A,\theta)|$ behaves as a log-correlated Gaussian field, predicting $\max_\theta \log|P_N(A,\theta)| = \log N - \tfrac{3}{4}\log\log N + \mathcal{M}_N$ with $\mathcal{M}_N$ a random $O(1)$ correction; the analogous prediction for $\max_{h\in[0,1]}\log|\zeta(\tfrac12+i(t+h))|$ over $t\in[T,2T]$ is $\log\log T - \tfrac{3}{4}\log\log\log T + \mathcal{M}_T$. The third FK conjecture predicts the "moments of moments" $\mathrm{MoM}_{U(N)}(k,\beta)\sim c(k,\beta)\,N^{k^2\beta^2-k+1}$ for integer $k,\beta$, and the survey reviews its proof and number-theoretic analogue.

## Method
Hybrid of analytic number theory (Selberg integral, Toeplitz/Hankel determinants with Fisher–Hartwig singularities, Riemann–Hilbert), probability of branching random walks / GREMs / Gaussian multiplicative chaos (Kahane's GMC, freezing transitions), and symmetric-function theory (Schur functions, Gelfand–Tsetlin patterns, ratios conjecture). Moments are computed via Weyl integration, Heine–Szegő identities, and contour-integral representations; the "moments of moments" polynomial in $N$ is extracted by phase-transition analysis of multi-singularity Toeplitz asymptotics.

## Result
Confirmed leading-order maximum for the CUE characteristic polynomial (Arguin–Belius–Bourgade) and tight bounds for $\zeta$ on short intervals (Arguin–Belius–Bourgade–Radziwiłł–Soundararajan; Najnudel; Harper). The MoM polynomial degree $k^2\beta^2 - k + 1$ exhibits a phase transition: the leading exponent is $k\beta^2$ for $k\leq 1/\beta^2$ (GMC/$L^2$-phase) and $k^2\beta^2-k+1$ for $k\geq 1/\beta^2$, with the boundary matching the $L^2$ critical point of GMC on the circle. Explicit polynomial formulas are given, e.g. $\mathrm{MoM}_{U(N)}(2,2)$ is a degree-15 polynomial in $N$ with leading coefficient $298/163459296000$.

## Why it matters here
General background; no direct arena tie. The log-correlated-field framework, GMC, and freezing-transition picture are mathematical infrastructure underlying extreme-value behavior of many discrete-geometry and analytic objects, and could in principle inform autocorrelation/uncertainty problems where extreme values of structured random-like sums appear — but none of the 23 arena problems directly invoke $\zeta$ moments or CUE statistics.

## Open questions / connections
- Full FHK conjecture (the random $O(1)$ correction term $\mathcal{M}_N$, $\mathcal{M}_T$, and its conjectured Gumbel-convolution-with-derivative-martingale distribution) remains open.
- Extensions to symplectic / orthogonal groups and to $L$-functions of higher rank — joint moments and ratios — are partially settled but not uniform.
- Connections to Liouville CFT (Remy / Fyodorov–Bouchaud formula) and to holomorphic multiplicative chaos suggest unexplored bridges between random-matrix moments and 2D quantum gravity.

## Key terms
log-correlated Gaussian field, Gaussian multiplicative chaos, Fyodorov–Hiary–Keating conjecture, characteristic polynomial, CUE, U(N), Riemann zeta function, Selberg integral, moments of moments, Toeplitz determinant, Fisher–Hartwig singularity, freezing transition, branching random walk, Keating–Snaith, symmetric functions, Schur, ratios conjecture, extreme value theory
