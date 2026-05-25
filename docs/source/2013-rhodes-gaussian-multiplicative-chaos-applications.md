---
type: source
kind: paper
title: "Gaussian multiplicative chaos and applications: A review"
authors: Rémi Rhodes, Vincent Vargas
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1305.6221
source_local: ../raw/2013-rhodes-gaussian-multiplicative-chaos-applications.pdf
topic: general-knowledge
cites:
---

# Gaussian multiplicative chaos and applications: A review

**Authors:** Rémi Rhodes, Vincent Vargas  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1305.6221

## One-line
A review of Kahane's theory of Gaussian multiplicative chaos (GMC) — random measures formally written as $M_\gamma(A) = \int_A e^{\gamma X(x) - \frac{\gamma^2}{2}\mathbb{E}[X^2(x)]}\sigma(dx)$ for log-correlated Gaussian fields $X$ — covering its construction, multifractal structure, and applications to turbulence, finance, and 2d Liouville quantum gravity.

## Key claim
For a log-correlated Gaussian field with covariance $\mathbb{E}[X(x)X(y)] = \ln_+\frac{T}{\rho(x,y)} + g(x,y)$ on a $d$-dimensional domain with Lebesgue $\sigma$, the regularized measure $M_{\epsilon,\gamma}$ converges (independently of the cutoff procedure) to a non-degenerate random measure iff $\gamma^2 < 2d$; the limiting measure is supported on a set of Hausdorff dimension $d - \gamma^2/2$, with finite positive moments of order $p$ iff $p < 2d/\gamma^2$, and finite negative moments of all orders.

## Method
Builds on Kahane's $\sigma$-positive type kernel framework: decompose $K = \sum_k K_k$ into continuous positive-definite pieces, take partial-sum Gaussian fields $X_n$, and exploit the resulting nonnegative martingale structure of $M_{n,\gamma}(A)$ for a.s. convergence. The core tool is **Kahane's convexity inequality** — for centered Gaussians with $\mathbb{E}[A_iA_j] \le \mathbb{E}[B_iB_j]$, $\mathbb{E}[F(\sum p_i e^{A_i - \mathbb{E}[A_i^2]/2})] \le \mathbb{E}[F(\sum p_i e^{B_i - \mathbb{E}[B_i^2]/2})]$ for convex $F$ — which yields cutoff-independence, moment bounds, and multifractal scaling via Girsanov-shifted comparison estimates against exact-scale-invariant fields and discrete cascades.

## Result
Establishes: (i) uniqueness in law of $M_\gamma$ independent of decomposition; (ii) non-degeneracy iff $\gamma^2 < 2d$ (necessary on $C^1$ manifolds, sufficient when $\sigma \in R^+_\alpha$ with $\gamma^2 < 2\alpha$); (iii) moment phase diagram (positive moments up to $2d/\gamma^2$, all negative moments finite); (iv) multifractal spectrum — for $\alpha = d + (\frac{1}{2} - q)\gamma^2$, $M_\gamma^q$-almost-every $x$ satisfies $\lim_{r \to 0}\ln M_\gamma(B(x,r))/\ln r = d - \gamma^2/2$ in the $q=1$ case; (v) Hausdorff dimension of thick-point sets $K_{\gamma,1}$ equals $d - \gamma^2/2$; (vi) new result: discrete Liouville measures on **isoradial graphs** (including triangular/square lattices) converge to continuous Liouville measure as mesh $\to 0$, subcritical and critical regimes, using Chelkak–Smirnov Green-function asymptotics $G_{\Gamma_n}(x,y) = \ln\frac{1}{|x-y|} + O(\epsilon_n^2/|x-y|^2)$.

## Why it matters here
General background; no direct arena tie. Closest adjacency is to log-correlated fields and multifractal measure theory — potentially informs functional-inequality / autocorrelation problems where extremal log-correlated structures appear, but the wiki currently has no GMC concept page and no arena problem in this family.

## Open questions / connections
- Critical and supercritical regimes ($\gamma^2 \ge 2d$): renormalization via derivative martingale (critical GMC) vs. atomic GMC for $\gamma^2 > 2d$, and the duality picture in Liouville QG.
- Maximum of log-correlated Gaussian fields and discrete GFF — Bramson–Ding–Zeitouni convergence in law, freezing transitions (Fyodorov–Bouchaud REM).
- Lognormal $\star$-scale invariance: characterization of all GMC laws via stochastic scale invariance.
- Extensions: complex-valued GMC, matrix-valued GMC (Chevillard–Rhodes–Vargas), non-Gaussian (log-infinitely-divisible) chaos.
- KPZ relation rigorously established in [Duplantier–Sheffield 2011, Rhodes–Vargas 2011] — geometric quantum-gravity dimension formula in any dimension for log-correlated fields.

## Key terms
Gaussian multiplicative chaos, Kahane convexity inequality, log-correlated Gaussian field, Gaussian Free Field, Liouville quantum gravity, KPZ formula, multifractal analysis, thick points, $\sigma$-positive type kernel, multiplicative cascade, isoradial graph, Kolmogorov–Obukhov turbulence
