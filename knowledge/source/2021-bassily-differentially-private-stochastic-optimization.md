---
type: source
kind: paper
title: "Differentially Private Stochastic Optimization: New Results in Convex and Non-Convex Settings"
authors: Raef Bassily, Crist'obal Guzm'an, Michael Menart
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2107.05585
source_local: ../raw/2021-bassily-differentially-private-stochastic-optimization.pdf
topic: general-knowledge
cites:
---

# Differentially Private Stochastic Optimization: New Results in Convex and Non-Convex Settings

**Authors:** Raef Bassily, Crist'obal Guzm'an, Michael Menart  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2107.05585

## One-line
Faster and more accurate differentially private stochastic optimization algorithms for convex generalized linear losses and (smooth / non-smooth weakly convex) non-convex losses, in both $\ell_2$ and non-Euclidean $\ell_p$ ($1 \le p \le 2$) geometries.

## Key claim
For non-smooth convex GLLs in $\ell_1$, an $(\varepsilon,\delta)$-DP algorithm achieves excess population risk $\tilde O(\sqrt{\log d / (n\varepsilon)})$ — nearly dimension-independent — circumventing the polynomial-$d$ lower bound of [AFKT21] for general non-smooth convex losses; for $\ell_2$ GLLs it achieves optimal excess risk in near-linear $O(n \log n)$ time. New non-convex rates: smooth $\ell_1$ at $\tilde O((\log^2 d/(n\varepsilon))^{1/3})$ in linear time, smooth $\ell_2$ at $\tilde O(n^{-1/3} + (d/(n\varepsilon)^2)^{1/5})$, and non-smooth weakly convex $\ell_2$ at $\tilde O(n^{-1/4} + (d/(n\varepsilon)^2)^{1/6})$.

## Method
Three core techniques: (1) **Moreau envelope smoothing applied to the 1-D link function $\ell^{(y)}$** of a GLL rather than to $f$ itself — reduces the proximal subproblem to a 1-D convex problem solved by bisection in $O(\log(L_0^2 R^2/\alpha^2))$ time, sidestepping the $n^3$ per-iteration cost of [BFTT19]. (2) **Variance-reduced stochastic Frank–Wolfe** (recursive gradient estimator from [HKMS20, ZSM+20]) with careful round-scheduling and noise tuning for the non-convex smooth case. (3) **Proximally-guided stochastic subgradient** [DG19] where each strongly-convex proximal subproblem is solved by an optimal DP-SCO method [AFKT21], extended to $\ell_p$ via the strong convexity of $\tfrac12\|\cdot\|_p^2$ with parameter $\kappa = 1/(p-1)$ (or $\log d$).

## Result
Convex GLL: $\ell_2$ rate $\tilde O(1/\sqrt n + \sqrt d/(n\varepsilon))$ in nearly linear time (Thm. 6); $\ell_1$ rate $\tilde O(\sqrt{\log d/(n\varepsilon)})$ (Thm. 9). Non-convex smooth: $\ell_1$ stationarity gap $\tilde O((\log^2 d/(n\varepsilon))^{1/3})$ in linear time (Thm. 11); $1<p\le 2$ rate involves $\kappa = \min\{1/(p-1), \log d\}$ (Thm. 13). Non-convex non-smooth weakly convex ($\ell_p$, $1\le p\le 2$): proximal-near-stationarity $\tilde O(\kappa^{5/4}/n^{1/4} + \kappa^{4/3}(d/(n\varepsilon)^2 \tilde\kappa)^{1/6})$ in $\tilde O(\min\{n^{3/2}, n^2\varepsilon/\sqrt d\})$ time (Thm. 20). $\ell_2$ matches the best non-private rate $O(1/n^{1/4})$ when $d = O(\sqrt n)$ and $\varepsilon = \Theta(1)$.

## Why it matters here
General background; no direct arena tie — this is a privacy-aware ML optimization paper, not a math-wisdom artifact for sphere packing / autocorrelation / extremal problems. The Moreau-envelope-via-1-D-bisection trick is the only piece that might tangentially echo smoothing techniques used in equioscillation / Remez polishing, but the connection is weak.

## Open questions / connections
- Can the $\ell_1$ GLL algorithm be made linear-time? Current noisy Frank–Wolfe step is superlinear, and one-pass variants [AFKT21, BGN21] inflate the smoothness-dependent risk too much.
- Are the $\ell_1$ non-convex smooth rates $\tilde O((\log^2 d/(n\varepsilon))^{1/3})$ tight for linear-time algorithms? Authors conjecture yes, citing the $\Omega(1/n^{1/3})$ lower bound of [ACD+19] for $\ell_2$ via stochastic gradient oracles.
- Extends [DG19] proximally-guided subgradient method to DP and to non-Euclidean $\ell_p$; first DP treatment of weakly convex non-smooth SO.

## Key terms
differential privacy, stochastic convex optimization, generalized linear losses, Moreau envelope, proximal operator, Frank-Wolfe, weakly convex, stationarity gap, $\ell_p$ geometry, variance reduction, Bassily, Guzm\'an, non-Euclidean optimization
