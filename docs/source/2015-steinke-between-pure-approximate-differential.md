---
type: source
kind: paper
title: Between Pure and Approximate Differential Privacy
authors: T. Steinke, Jonathan Ullman
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1501.06095
source_local: ../raw/2015-steinke-between-pure-approximate-differential.pdf
topic: general-knowledge
cites:
---

# Between Pure and Approximate Differential Privacy

**Authors:** T. Steinke, Jonathan Ullman  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1501.06095

## One-line
Establishes a tight $\sqrt{d \log(1/\delta)}/\alpha\varepsilon$ sample-complexity lower bound for $(\varepsilon,\delta)$-differentially private release of one-way marginals, smoothly interpolating between pure ($\delta=0$) and approximate DP.

## Key claim
For $2^{-\Omega(n)} \le \delta \le 1/n^{1+\Omega(1)}$, any $(\varepsilon,\delta)$-DP mechanism $M:\{\pm 1\}^{n\times d}\to[\pm 1]^d$ with $\mathbb{E}\|M(D)-\bar D\|_1 \le \alpha d$ requires $n \ge \Omega(\sqrt{d\log(1/\delta)}/\alpha\varepsilon)$, matching the Laplace mechanism up to constants and giving the first *multiplicative* $\log(1/\delta)$ factor in DP lower bounds.

## Method
Reduction from fingerprinting codes (Boneh–Shaw / Tardos, average-case variant) to DP attacks, generalizing Bun–Ullman–Vadhan (STOC'14) via **group differential privacy**: amplify a single-row $(\varepsilon,\delta)$-DP mechanism to a $k$-row $(k\varepsilon, e^{k\varepsilon}\delta)$-DP mechanism by row replication, then choose $k\approx \log(1/\delta)/\varepsilon$ so the tracer attack still applies. Upper bounds use the exponential mechanism with $L_\infty$-norm score (pure DP) and Gaussian noise + sparse-vector "fix-up" of bad coordinates (approximate DP).

## Result
Lower bound: $n = \Omega(\sqrt{d\log(1/\delta)}/\alpha\varepsilon)$, tight against Laplace. New pure-DP mechanism: density $\propto \exp(-\eta\|y\|_\infty)$ achieves $L_\infty$ error $\alpha$ with $n\ge 4d/\varepsilon\alpha$ — saves a $\log d$ factor over Laplace. New approximate-DP mechanism: Gaussian noise + sparse vector achieves $L_\infty$ error with $n = O(\sqrt{d\log(1/\delta)\log\log d}/\varepsilon\alpha)$ — saves $\log d / \log\log d$ over Gaussian.

## Why it matters here
General background; no direct arena tie. The closest abstract resonance is the *gamma-distribution tail / exponential-mechanism with $L_\infty$ score* construction — a tool for adding multivariate noise with sharper worst-case (not average-case) tails than i.i.d. Laplace/Gaussian, conceivably relevant if any Einstein problem ever needs an $L_\infty$-controlled perturbation.

## Open questions / connections
- Can fingerprinting-code / tracing-attack frameworks lower-bound other vector-output problems beyond one-way marginals?
- Does the multiplicative $\log(1/\delta)$ phenomenon extend to higher-order (k-way) marginals or arbitrary statistical queries?
- The exponential-mechanism-with-$L_\infty$-norm trick (gamma radius × uniform cube) — does it generalize to other norm-shaped privacy/perturbation problems?

## Key terms
differential privacy, fingerprinting codes, group privacy, one-way marginals, sample complexity lower bound, exponential mechanism, sparse vector technique, Gaussian mechanism, Laplace mechanism, Tardos codes, Bun-Ullman-Vadhan, tracing attack
