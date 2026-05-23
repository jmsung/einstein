---
type: source
kind: paper
title: Non-Euclidean Differentially Private Stochastic Convex Optimization
authors: Raef Bassily, Crist'obal Guzm'an, Anupama Nandi
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.01278
source_local: ../raw/2021-bassily-non-euclidean-differentially-private-stochastic.pdf
topic: general-knowledge
cites:
---

# Non-Euclidean Differentially Private Stochastic Convex Optimization

**Authors:** Raef Bassily, Cristóbal Guzmán, Anupama Nandi  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.01278

## One-line
Gives the first linear-time differentially private stochastic convex optimization (DP-SCO) algorithms achieving (nearly) optimal excess risk for smooth losses in $\ell_p$ geometries with $1 \le p \le 2$, plus matching lower bounds.

## Key claim
For smooth convex losses with $(\varepsilon,\delta)$-DP on $n$ i.i.d. samples in $\mathbb{R}^d$ with the $\ell_p$ geometry: a linear-time algorithm achieves excess population risk $\tilde O\!\left(\sqrt{\kappa/n} + \kappa\sqrt{d}/(\varepsilon n)\right)$ for $1<p\le 2$ (where $\kappa = \min\{1/(p-1),\,2\ln d\}$), and $\tilde O(\log d/\sqrt n + \log d \cdot \sqrt d/(\varepsilon n))$ for $p=1$, both with high probability and matched up to log factors by new lower bounds (e.g. $\Omega((p-1)\sqrt{d}/(\varepsilon n))$ for $1<p<2$).

## Method
A noisy variance-reduced Stochastic Frank-Wolfe (SFW) using a SPIDER-style recursive gradient estimator over a binary-tree batch schedule, with privacy injected through a new **Generalized Gaussian mechanism** — density $\propto \exp(-\|z-\mu\|_+^2/(2\sigma^2))$ tied to the $\kappa$-regular smooth norm $\|\cdot\|_+$ on the dual space. Vector-valued martingale concentration in $\kappa$-regular spaces (Juditsky–Nemirovski) controls bias/variance of the noisy estimator; for $p=1$ the polyhedral linear-optimization oracle is privatized via report-noisy-max. Lower bounds use fingerprinting-code arguments combined with uniform convexity of $\ell_p$ (Ball–Carlen–Lieb).

## Result
Optimal-up-to-logs rates are attained in **linear time** in $n$ (vs prior $O(\min\{n^{3/2}, n^2/\sqrt d\})$ for $1<p<2$), with high-probability rather than only in-expectation guarantees. For $2<p\le\infty$ in the low-dimensional regime $d\lesssim n$, existing Euclidean phased-SGD already achieves the optimal $L_0 M(d^{1/2-1/p}/\sqrt n + d^{1-1/p}\sqrt{\log(1/\delta)}/(\varepsilon n))$ rate; in particular $p=\infty$ inherits near-optimality. A sharp phase transition is identified at $p=1$: for $1+\Omega(1) < p < 2$ the rate matches the Euclidean case (a $\sqrt d$ dependence is unavoidable).

## Why it matters here
General background; no direct arena tie. The conceptual content — $\kappa$-regular normed spaces, uniform convexity/smoothness of $\ell_p$ via Ball–Carlen–Lieb, and dual-norm sensitivity — is adjacent to functional-inequality machinery (uncertainty, autocorrelation) but the privacy mechanism and SFW algorithmics are unrelated to Einstein Arena optimization problems.

## Open questions / connections
- Closing the polylog gap between upper and lower bounds for $p=1$ and the high-dimensional regime $d \gg n$ at $p>2$.
- Extending the Generalized Gaussian mechanism to non-smooth losses in general $\kappa$-regular spaces (current sharp result needs smoothness).
- Concurrent/independent work by Asi–Feldman–Koren–Talwar achieves similar rates for $1<p<2$ via iterative localization + mirror descent but in super-linear time — is there a unifying linear-time framework?
- Relationship to Juditsky–Nemirovski martingale concentration in 2-smooth normed spaces as a general tool beyond DP.

## Key terms
differential privacy, stochastic convex optimization, DP-SCO, Frank-Wolfe, SPIDER variance reduction, $\ell_p$ geometry, $\kappa$-regular normed space, uniform convexity, uniform smoothness, Generalized Gaussian mechanism, Ball-Carlen-Lieb, fingerprinting codes, mirror descent, Juditsky-Nemirovski
