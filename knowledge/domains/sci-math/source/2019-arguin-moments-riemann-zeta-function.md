---
type: source
kind: paper
title: Moments of the Riemann zeta function on short intervals of the critical line
authors: L. Arguin, Frédéric Ouimet, Maksym Radziwill
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1901.04061
source_local: ../raw/2019-arguin-moments-riemann-zeta-function.pdf
topic: general-knowledge
cites:
---

# Moments of the Riemann zeta function on short intervals of the critical line

**Authors:** L. Arguin, Frédéric Ouimet, Maksym Radziwill  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1901.04061

## One-line
Proves the Fyodorov–Keating conjecture (extended): for typical $t \in [T,2T]$, the $\beta$-th moment $\int_{-\log^\theta T}^{\log^\theta T} |\zeta(\tfrac12 + it + ih)|^\beta\, dh$ equals $(\log T)^{f_\theta(\beta) + o(1)}$ with an explicit freezing exponent $f_\theta(\beta)$, and the local maximum equals $(\log T)^{m(\theta)+o(1)}$.

## Key claim
For $\theta > -1$ and $\beta > 0$, with $\tau$ uniform on $[T,2T]$, the integral $\int_{|h|\le \log^\theta T} |\zeta(\tfrac12+i\tau+ih)|^\beta dh = (\log T)^{f_\theta(\beta)+o(1)}$ in probability, where:
- $\theta \le 0$: $m(\theta) = 1+\theta$; $f_\theta(\beta) = \tfrac{\beta^2}{4}(1+\theta) + \theta$ for $\beta \le 2$, else $\beta m(\theta) - 1$.
- $\theta > 0$: $m(\theta) = \sqrt{1+\theta}$; $f_\theta(\beta) = \tfrac{\beta^2}{4} + \theta$ for $\beta \le 2\sqrt{1+\theta}$, else $\beta m(\theta) - 1$.

A freezing phase transition occurs at critical $\beta_c(\theta)$; the exponent form differs between mesoscopic ($-1<\theta<0$) and macroscopic ($\theta>0$) intervals, reflecting an approximate tree-of-correlations structure. Also $\max_{|h|\le\log^\theta T} |\zeta(\tfrac12+i\tau+ih)| = (\log T)^{m(\theta)+o(1)}$. Unconditional except upper bounds need RH when $\theta > 3$.

## Method
Upper bound: moment estimates on $\zeta$ (Soundararajan / Heap–Radziwiłł–Soundararajan) combined with a discretization showing $\zeta$ varies on scale $(\log T)^{-1}$, so a continuous max/moment over $\log^\theta T$ reduces to $(\log T)^{1+\theta}$ discrete samples; for $\theta<0$ they mollify $\zeta \cdot e^{-P_{|\theta|}}$ to kill the small-primes contribution. Lower bound: off-axis reduction via Gabriel's subharmonic inequality + an explicit entire Φ approximating a thin-rectangle indicator; mollification by $M(s)=\sum \mu(n)/n^s$ on smooth primes; Kistler's multiscale second-moment method on the log-correlated Dirichlet polynomial $\mathrm{Re}\, P_{1-\delta}(\sigma_0+i\tau+ih)$, using the covariance $\tfrac12 \log|h-h'|^{-1} + O(1)$ (a branching-random-walk / Galton–Watson-tree analog with branching degree $e$).

## Result
Establishes the moment and maximum asymptotics for all interval widths $\log^\theta T$, $\theta>-1$, with the explicit two-regime $f_\theta(\beta)$ and $m(\theta)$ above. The freezing transition persists for any fixed-power interval (since $\beta_c(\theta)\to\infty$ as $\theta\to\infty$). Conjecture 1.3 (subleading $r(\theta)\log\log\log T$ term with discontinuity at $\theta=0$: $r(0)=3/4$, $r(\theta)=1/(4\sqrt{1+\theta})$ for $\theta>0$) refines the picture; for $\theta<0$ they predict an extra Gaussian fluctuation $\sqrt{|\theta|/2}\,\sqrt{\log\log T}\cdot Z$ from the small-primes Dirichlet polynomial.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems is about $\zeta$ moments. The transferable techniques are (a) the multiscale second-moment method on log-correlated Gaussian-like processes, (b) the REM-vs-branching-random-walk heuristic for predicting maxima from variance + correlation tree, and (c) Gabriel's subharmonic-integral inequality + entire approximation of indicators — all are general tools for extremal/probabilistic analysis.

## Open questions / connections
- Subleading $r(\theta)\log\log\log T$ correction (Conjecture 1.3) and the predicted $\theta=0$ discontinuity, including the $\theta\sim(\log\log T)^{-\alpha}$ interpolation $r=(1+2\alpha)/4$ from Arguin–Dubach–Hartung (2021).
- Extension beyond $\theta=3$ unconditionally (currently RH-dependent because moment bound $\mathbb{E}|\zeta(\tfrac12+i\tau)|^\beta \ll (\log T)^{\beta^2/4+\varepsilon}$ is only known for $\beta\le 4$ unconditionally).
- Whether the freezing analogue / Gaussian-multiplicative-chaos identification (Fyodorov–Bouchaud, Remy) carries over from CUE characteristic polynomials to $\zeta$ on mesoscopic intervals.

## Key terms
Riemann zeta moments, Fyodorov–Keating conjecture, freezing phase transition, log-correlated process, branching random walk, REM, random energy model, Selberg central limit theorem, mollifier method, Gabriel subharmonic inequality, multiscale second moment method, Gaussian multiplicative chaos, CUE characteristic polynomial, Dirichlet polynomial, critical exponent
