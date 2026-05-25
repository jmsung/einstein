---
type: source
kind: paper
title: "Freezing transitions and extreme values: random matrix theory, and disordered landscapes"
authors: Y. Fyodorov, J. Keating
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1211.6063
source_local: ../raw/2012-fyodorov-freezing-transitions-extreme-values.pdf
topic: general-knowledge
cites:
---

# Freezing transitions and extreme values: random matrix theory, and disordered landscapes

**Authors:** Y. Fyodorov, J. Keating  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1211.6063

## One-line
Conjectures that the freezing transition of 1/f-noise disordered energy landscapes governs the extreme-value statistics of CUE characteristic polynomials and, conjecturally, of $\zeta(1/2+it)$ over short critical-line intervals.

## Key claim
For a CUE characteristic polynomial $p_N(\theta)$ on an interval of $N_L$ eigenvalues, $-2\max_{\theta\in[0,L)}\log|p_N(\theta)| \sim -2\log N_L + c\log\log N_L + x$ with universal constant $c = 3/2$ (not $1/2$ as for short-range correlated variables) and a non-Gumbel limiting distribution $p(x)$; backward tail $p(x)\sim -xe^x$ as $x\to-\infty$. The same form is conjectured for $\zeta(1/2+it)$ with $N_L \to \frac{L}{2\pi}\log\frac{T}{2\pi}$.

## Method
Identify $Z_N(\beta;L) = \frac{N}{2\pi}\int_0^L |p_N(\theta)|^{2\beta}d\theta$ as the partition function of a particle in a log-correlated random potential $V_N(\theta)=-2\log|p_N(\theta)|$; the two-point correlation $\langle V(\theta_1)V(\theta_2)\rangle \approx -2\log|\theta_1-\theta_2|$ matches the 1/f-noise / 2D-GFF universality class. Moments computed via Fisher-Hartwig / Selberg / Dyson-Morris integrals; replica/freezing scenario from statistical mechanics of logarithmic REM imported to read off the extreme-value distribution. Freezing at $\beta_c=1$: mean free energy $-\mathbb{E}\{F(\beta)\} = \beta+\beta^{-1}$ for $\beta\le 1$, $=2$ for $\beta>1$.

## Result
Full-circle ($L=2\pi$): density of the maximum is $p(x) = 2e^x K_0(2 e^{x/2})$ (Bessel-K form, also expressible as sum of two independent Gumbels). High-points measure $\mu_N(x;L)$ — fraction of length where $|p_N|>N_L^x$ — has typical scale $\mu_e(x) \sim N^{-x^2}$ with multifractal exponent $\tau_q = \tfrac{1}{4}q(q-1)$, and density $P(\xi) = \frac{1}{x^2}\xi^{-1-1/x^2}e^{-\xi^{-1/x^2}}$ for $0<x<1$. Mesoscopic case ($1\ll N_L\ll N$): $x = u\sqrt{-2\ln L} + y$ with $u$ standard Gaussian and $y$ given by a contour integral involving the Barnes double-$\Gamma$ function. For $\zeta(1/2+it)$ the arithmetic factor $a(x)=\prod_p(1-1/p)^{x^2}\sum_m\binom{x+m-1}{m}^2 p^{-m}$ multiplies the measure scale but, since $a(1)=1$, does not appear at leading order in the maximum.

## Why it matters here
General background on log-correlated Gaussian extreme-value statistics, Fisher-Hartwig asymptotics, and Selberg-integral machinery — relevant to problems involving extremal/autocorrelation behavior of random-like functions (e.g. Fejér / Chebyshev / autocorrelation-inequality problems) and as a worked example of how multifractal exponents arise from log-correlated potentials. No direct arena tie; informs concepts of log-correlated maxima, freezing, and multifractal sojourn-length distributions.

## Open questions / connections
- Rigorous justification of the freezing-replica predictions for CUE; sharpness of the $c=3/2$ universal constant.
- Role of arithmetic (Euler product $a(x)$) in subleading corrections to the $\zeta$ extreme-value distribution and at finite $T$.
- Quantitative numerical verification of $P(\xi)$ for multifractal sojourn lengths — remains elusive even for the circular-logarithmic model.
- Connection to 2D Gaussian Free Field maxima (Bramson-Ding-Zeitouni) and Liouville quantum gravity (Barnes double-$\Gamma$, Gaussian multiplicative chaos).

## Key terms
freezing transition, log-correlated Gaussian field, CUE characteristic polynomial, Riemann zeta extreme values, Fisher-Hartwig asymptotics, Selberg integral, Barnes G-function, multifractality, 1/f noise, Gumbel vs non-Gumbel maxima, Fyodorov-Bouchaud, partition-function method
