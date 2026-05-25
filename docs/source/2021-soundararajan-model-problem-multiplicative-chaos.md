---
type: source
kind: paper
title: A model problem for multiplicative chaos in number theory
authors: Kannan Soundararajan, Asif Zaman
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2108.07264v1
source_local: ../raw/2021-soundararajan-model-problem-multiplicative-chaos.pdf
topic: general-knowledge
cites: 
---

# A model problem for multiplicative chaos in number theory

**Authors:** Kannan Soundararajan, Asif Zaman  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2108.07264v1

## One-line
A simplified Gaussian model of random multiplicative functions exhibiting "better than square-root cancellation," presented as a pedagogical entry point to Harper's multiplicative chaos breakthrough.

## Key claim
For $A(N)$ defined by $\exp\left(\sum_{k\geq 1} \frac{X(k)}{\sqrt{k}} z^k\right) = \sum_{n\geq 0} A(n) z^n$ with $X(k)$ i.i.d. standard complex Gaussians: $\mathbb{E}[|A(N)|^2] = 1$ but $\mathbb{E}[|A(N)|] \asymp (\log N)^{-1/4}$, so the first moment tends to $0$. More generally, $\mathbb{E}[|A(N)|^{2q}] \asymp \bigl((1-q)\sqrt{\log N} + 1\bigr)^{-q}$ uniformly in $0 \leq q \leq 1$.

## Method
Generating-function representation $A(N) = \sum_{|\lambda|=N} a(\lambda)$ over integer partitions, with Cauchy-contour extraction reducing first-moment bounds to averages of $|F_K(re^{i\theta})|^{2q}$ over the unit circle. Upper bound: dyadic decomposition by largest part $\lambda_1$ plus Hölder. Lower bound: a "ballot problem" / barrier argument on Gaussian random walks (Harper's Probability Result 1) controlling $\sum_k \mathrm{Re}(X(k) r^k e^{ik\theta}/\sqrt{k})$, combined with a bivariate-Gaussian decorrelation trick that splits weakly correlated walks at $\theta_1, \theta_2$ into nearly independent ones.

## Result
Both upper and lower bounds matching Harper's $(\log N)^{-1/4}$-style cancellation, made fully self-contained except for one ballot-problem lemma. The model is exactly the $q \to \infty$ limit of Steinhaus random multiplicative functions on $\mathbb{F}_q[t]$, with $N \leftrightarrow \log x$ matching variance $\asymp x$ and first moment $\asymp \sqrt{x}/(\log\log x)^{1/4}$ in the integer case.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: the ballot-problem / barrier-event technique for controlling extrema of log-correlated Gaussian fields is a transferable tool, and the Fyodorov–Hiary–Keating circle is related to extremal-value / autocorrelation thinking that may inform problems involving log-correlation or random-matrix heuristics.

## Open questions / connections
- Law-of-the-iterated-logarithm analogue: almost surely $|A(N)| \geq (\log N)^{1/4-\varepsilon}$ for arbitrarily large $N$ (Harper proved the multiplicative-function version; transfer to $A(N)$ open).
- Extension to high moments $q > 1$ (Harper II [20]) and to the Rademacher class.
- Connections to Fyodorov–Hiary–Keating maximum of $|\zeta(1/2 + it)|$ on unit intervals and the related second-moment estimate $\frac{1}{T}\int_0^T \bigl(\frac{1}{\log T}\int |\zeta|^2 dh\bigr)^{1/2} \asymp (\log\log T)^{-1/4}$.
- Multiplication-table problem (Ford) and permutation-product analogues as further log-correlated examples.

## Key terms
random multiplicative functions, multiplicative chaos, Helson conjecture, Harper, Fyodorov-Hiary-Keating, Riemann zeta function, critical line, log-correlated field, ballot problem, Gaussian random walk, barrier method, Steinhaus, function field, bivariate Gaussian, low moments, square-root cancellation, partition generating function
