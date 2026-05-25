---
type: source
kind: paper
title: Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function.
authors: Y. Fyodorov, G. Hiary, J. Keating
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1202.4713
source_local: ../raw/2012-fyodorov-freezing-transition-characteristic-polynomials.pdf
topic: general-knowledge
cites:
---

# Freezing transition, characteristic polynomials of random matrices, and the Riemann zeta function.

**Authors:** Y. Fyodorov, G. Hiary, J. Keating  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1202.4713

## One-line
Argues that a spin-glass-style freezing transition governs the extreme-value distribution of CUE characteristic polynomials and, conjecturally, of $|\zeta(1/2+it)|$ over short intervals.

## Key claim
For $U_N \in \mathrm{CUE}(N)$ with characteristic polynomial $p_N(\theta)$, $-2\max_{\theta} \log|p_N(\theta)| \sim a_N + b_N x$ with $a_N = -2\log N + c\log\log N + o(1)$, $c = 3/2$, $b_N \to 1$, and $x$ distributed with density $p(x) = 2e^x K_0(2 e^{x/2})$ — i.e. tail $p(x)\sim |x|e^x$ as $x\to-\infty$. The same law is conjectured for $\max_{t\in[T,T+2\pi]} |\zeta(1/2+it)|$.

## Method
Map $V_N(\theta) = -2\log|p_N(\theta)|$ to a 1D log-correlated random energy landscape and study $Z_N(\beta) = \int e^{-\beta V_N}\, d\theta/(2\pi)$. Compute positive-integer moments $\langle Z_N^k(\beta)\rangle$ via Toeplitz / Selberg-integral asymptotics (Widom + Dyson–Morris), match to the circular-logarithmic ($1/f$-noise) REM partition function of Fyodorov–Bouchaud, and import its freezing-transition results (freezing at $\beta_c=1$) for the extreme-value statistics.

## Result
Establishes (at the moment-asymptotic level) that the maximum of $|p_N(\theta)|$ over $\theta\in[0,2\pi)$ obeys (12)–(13) with the universal log-correlated subleading constant $c=3/2$ (vs. $c=1/2$ for Gumbel/independent maxima). Numerics on $\zeta$ near $T=10^{28}$ (and tables up to $T=10^{22}$) support $c=3/2$ (ratios $\tilde\delta/\delta \approx 1$) over $c=1/2$, support the Bessel-$K_0$ density, and confirm freezing of $-f(\beta) = \beta + 1/\beta$ for $\beta<1$ and $-f(\beta)=2$ for $\beta\ge1$.

## Why it matters here
General background; no direct arena tie — but supplies a template for how logarithmically-correlated Gaussian-like landscapes have universal extreme-value laws ($c=3/2$, Bessel-$K_0$ tail) distinct from Gumbel, potentially relevant if any arena problem reduces to extremizing a log-correlated objective (autocorrelation / uncertainty / functional inequalities).

## Open questions / connections
- Rigorous proof of (12)–(13) for CUE max — moment method only yields $k<\beta^{-2}$, so full distribution from moments is heuristic.
- Lower-order arithmetic corrections (Keating–Snaith / Conrey et al.) to $\zeta$-max distribution not yet incorporated; could shift agreement in Fig. 1.
- Whether the freezing tail $|x|e^x$ persists into the large-deviation regime — would imply Montgomery's $\exp(c_M\sqrt{\log t \log\log t})$ heuristic underestimates true $\zeta$ maxima.
- Connections to 2D GFF, branching random walks, polymers on disordered trees, REM — all share the universal $c=3/2$ class.

## Key terms
freezing transition, log-correlated random energy model, CUE characteristic polynomial, Riemann zeta extreme values, Selberg integral, Toeplitz determinant, Barnes G-function, Fyodorov-Bouchaud, $1/f$ noise, branching random walk, 2D Gaussian free field, Keating-Snaith, Bessel $K_0$ extreme value distribution, Gumbel universality class
