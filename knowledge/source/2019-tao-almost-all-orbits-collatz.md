---
type: source
kind: paper
title: Almost all orbits of the Collatz map attain almost bounded values
authors: T. Tao
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1909.03562
source_local: ../raw/2019-tao-almost-all-orbits-collatz.pdf
topic: general-knowledge
cites:
---

# Almost all orbits of the Collatz map attain almost bounded values

**Authors:** T. Tao  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1909.03562

## One-line
Proves that for any function $f(N)\to\infty$, the Collatz orbit of $N$ dips below $f(N)$ for almost all $N$ (logarithmic density), via 3-adic Fourier analysis of a "Syracuse" random walk.

## Key claim
For any $f:\mathbb{N}+1\to\mathbb{R}$ with $\lim f(N)=+\infty$, $\mathrm{Col}_{\min}(N) < f(N)$ for almost all $N\in\mathbb{N}+1$ in logarithmic density — e.g., $\mathrm{Col}_{\min}(N)<\log\log\log\log N$ a.a. Quantitatively, for any $\delta>0$ there exists $C_\delta=\exp(\delta^{-O(1)})$ with $\mathrm{Col}_{\min}(N)\le C_\delta$ on a set of lower log-density $\ge 1-\delta$. Strictly improves Korec's $N^\theta$ bound for $\theta>\log 3/\log 4\approx 0.7924$.

## Method
Replaces Collatz with the Syracuse map $\mathrm{Syr}(N)=(3N+1)/2^{\nu_2(3N+1)}$ on odd integers; iterates factor as affine maps $\mathrm{Aff}_{\vec a}(N)=3^n 2^{-|\vec a|}N + F_n(\vec a)$ with $\vec a$ behaving like iid $\mathrm{Geom}(2)$. Bootstraps "almost-sure local wellposedness" to "almost-global" à la Bourgain by constructing a family of probability measures $\nu_x$ approximately transported by the first-passage map. Core technical ingredient: superpolynomial decay of the characteristic function of the Syracuse random variable $\mathrm{Syrac}(\mathbb{Z}/3^n\mathbb{Z})$ at high 3-adic frequencies, proved via a 2D renewal process (holding times $\equiv\mathrm{Hold}$ with mean $(4,16)$) interacting with a union of triangles indexed by frequency.

## Result
Theorem 1.3: $\mathrm{Col}_{\min}(N)<f(N)$ for almost all $N$ (log density). Reduction (Prop. 1.11): first-passage locations $\mathrm{Pass}_x(N_{x^\alpha})$ and $\mathrm{Pass}_x(N_{x^{\alpha^2}})$ ($\alpha=1.001$) are total-variation close, $d_{TV}\lesssim \log^{-c}x$, with escape probability $\lesssim x^{-c}$. Fine-scale mixing (Prop. 1.14): $\mathrm{Osc}_{m,n}$ of the Syracuse distribution decays as $m^{-A}$ for any $A>0$.

## Why it matters here
General background; no direct Einstein Arena tie. Methodologically interesting as a template for: (i) bootstrapping local→global probabilistic control via approximately-invariant measure families when no true invariant exists, (ii) 3-adic/$p$-adic Fourier decay arguments, (iii) renewal-process arguments for hitting/passage statistics — patterns potentially transferable to combinatorial-dynamics problems on integer lattices.

## Open questions / connections
- Can log-density be upgraded to natural density? Tao notes this needs fine-scale mixing of the full random affine map, not just the offset.
- Can the $\log^{-c}x$ stabilisation bound be sharpened to $x^{-c}$?
- Can the constants be made explicit enough that, combined with numerical verification, one proves Collatz on a set of positive log density?
- Extends Terras/Everett $\mathrm{Col}_{\min}(N)<N$, Allouche $\theta>0.869$, Korec $\theta>0.7924$, Krasikov–Lagarias $\#\{N\le x:\mathrm{Col}_{\min}=1\}\gg x^{0.84}$.

## Key terms
Collatz conjecture, 3x+1 problem, Syracuse map, logarithmic density, first passage time, 3-adic Fourier analysis, characteristic function decay, renewal process, geometric random variable, Bourgain invariant measure, Korec bound, Tao
