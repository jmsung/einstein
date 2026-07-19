---
type: source
kind: paper
title: "MOMENTS OF RANDOM MULTIPLICATIVE FUNCTIONS, I: LOW MOMENTS, BETTER THAN SQUAREROOT CANCELLATION, AND CRITICAL MULTIPLICATIVE CHAOS"
authors: Adam J. Harper
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.06654
source_local: ../raw/2017-harper-moments-random-multiplicative-functions.pdf
topic: general-knowledge
cites:
---

# MOMENTS OF RANDOM MULTIPLICATIVE FUNCTIONS, I: LOW MOMENTS, BETTER THAN SQUAREROOT CANCELLATION, AND CRITICAL MULTIPLICATIVE CHAOS

**Authors:** Adam J. Harper  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.06654

## One-line
Determines the exact order of magnitude of low moments $\mathbb{E}|\sum_{n\le x} f(n)|^{2q}$ for $0 \le q \le 1$ of random multiplicative functions, proving Helson's conjecture that the first moment is strictly smaller than $\sqrt{x}$.

## Key claim
For Steinhaus (and analogously Rademacher) random multiplicative $f$, uniformly in $0 \le q \le 1$ and large $x$:
$$\mathbb{E}\Big|\sum_{n\le x} f(n)\Big|^{2q} \asymp \left(\frac{x}{1+(1-q)\sqrt{\log\log x}}\right)^{q}.$$
At $q=1/2$ this gives $\mathbb{E}|\sum_{n\le x} f(n)| \asymp \sqrt{x}/(\log\log x)^{1/4}$ — *better than squareroot cancellation*, confirming Helson and refuting the Harper–Nikeghbali–Radziwiłł and Heap–Lindqvist counter-conjectures.

## Method
Two-stage reduction: (1) use multiplicativity (split $n=p\cdot m$ for primes $p\in(\sqrt x,x]$), Khintchine / Hölder, and Parseval to relate $\mathbb{E}|\sum f(n)|^{2q}$ to $x^q\,\mathbb{E}\big(\tfrac{1}{\log x}\int_{-1/2}^{1/2}|F(1/2+it)|^2\,dt\big)^q$ where $F$ is the random Euler product. (2) Identify this integral as (a truncation of) a *critical Gaussian multiplicative chaos* with logarithmic covariance across $\log\log x$ "scales"; gain over the trivial Hölder bound by inserting an indicator $1_G$ that all subproducts obey simultaneous barrier bounds $\log|F(1/2+it)| \le \log\log x + K/(1-q)$, controlled by Girsanov-type estimates and a Gaussian-random-walk barrier argument (Probability Results 1 & 2, proved via iterated-log conditioning).

## Result
Sharp two-sided bounds match for all $0\le q\le 1$ in both Steinhaus and Rademacher models, with the extra $\tfrac{1}{(\log\log x)^{1/4}}$ factor at $q=1/2$ being the precise correction to $\sqrt{x}$ cancellation. Consequences: (i) negative answer to the embedding problem for Dirichlet polynomials for all $0<2q<2$; (ii) the normalized sum $\sum f(n)/\sqrt{\mathbb{E}|\sum f|^2}$ cannot have a Gaussian limit (variance grows slower than $x$); (iii) tail-probability and large-deviation consequences via Paley–Zygmund.

## Why it matters here
General background; no direct arena tie. The closest relevance is methodological: the **barrier / multi-scale-decomposition technique** (treating $\log|F|$ as a logarithmically-correlated Gaussian field with $\log\log x$ scales, then applying simultaneous-barrier indicators with Girsanov rescaling) is a transferable tool for any extremal problem whose objective decomposes hierarchically across log-scales — potentially relevant if an arena problem ever reduces to extremes of a log-correlated process (zeta-like, branching-random-walk-like).

## Open questions / connections
- Companion paper II handles $q>1$ moments — yields the full moment curve.
- Almost-sure law-of-iterated-logarithm gap remains: upper bound $\sqrt{x}(\log\log x)^{2+\epsilon}$ (Lau–Tenenbaum–Wu) vs lower bound $\sqrt{x}/(\log\log x)^{5/2+\epsilon}$ (Harper 2013) — comparable to Gonek's $O(\sqrt{x}(\log\log\log x)^{5/4})$ conjecture for $\sum\mu(n)$.
- Tail probability $P(|\sum f(n)|\ge \lambda\sqrt{x})$ still only known via Chebyshev $\ll 1/\lambda^2$ for moderate $\lambda$ — no Gaussian-decay bound proved.
- Extends Duplantier–Rhodes–Sheffield–Vargas critical-chaos renormalization to a number-theoretic Euler-product setting; ties to Saksman–Webb chaos models of $\zeta$.

## Key terms
random multiplicative function, Steinhaus, Rademacher, Helson conjecture, critical multiplicative chaos, Gaussian multiplicative chaos, log-correlated field, Euler product, Dirichlet polynomial, barrier method, Girsanov theorem, branching random walk, Riemann zeta moments, squareroot cancellation, Möbius function
