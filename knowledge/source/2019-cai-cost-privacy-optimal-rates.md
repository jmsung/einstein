---
type: source
kind: paper
title: "The Cost of Privacy: Optimal Rates of Convergence for Parameter Estimation with Differential Privacy"
authors: T. Cai, Yichen Wang, Linjun Zhang
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.04495
source_local: ../raw/2019-cai-cost-privacy-optimal-rates.pdf
topic: general-knowledge
cites:
---

# The Cost of Privacy: Optimal Rates of Convergence for Parameter Estimation with Differential Privacy

**Authors:** T. Cai, Yichen Wang, Linjun Zhang  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.04495

## One-line
Establishes minimax-optimal rates (up to log factors) for mean estimation and linear regression under $(\varepsilon,\delta)$-differential privacy, in both low- and high-dimensional regimes.

## Key claim
The minimax squared $\ell_2$ risk of $(\varepsilon,\delta)$-DP estimation has tight lower bounds of order $\frac{d^2\log(1/\delta)}{n^2\varepsilon^2}$ (low-dim mean), $\frac{(s\log d)^2}{n^2\varepsilon^2}$ (sparse mean and high-dim linear regression), and $\frac{d^2}{n^2\varepsilon^2}$ (low-dim regression), each matched by an explicit private algorithm.

## Method
Lower bounds use a refined **tracing adversary** argument: construct an attack $A_\mu(x, M(X)) = \langle x-\mu, M(X)\rangle$ (or a sparse variant restricted to $\mathrm{supp}(\mu)$) and show that a too-accurate private $M$ contradicts the DP guarantee via a Stein-lemma/order-statistic prior on $\mu$. Upper bounds come from Gaussian-mechanism noisy sample mean, noisy projected gradient descent for regression, and a novel **private iterative hard thresholding** (peeling + Laplace top-$k$ selection) for sparse regression. Composition + post-processing of $(\varepsilon/T,\delta/T)$ per-iteration noise gives the overall privacy.

## Result
Theorem 3.1: low-dim mean lower bound $\sigma^2(d/n + d^2\log(1/\delta)/n^2\varepsilon^2)$, matched by truncated Gaussian-noisy mean (Thm 3.2). Theorem 3.3/3.4: sparse mean rate $\sigma^2(s\log d/n + (s\log d)^2/n^2\varepsilon^2)$ — privacy cost depends only **logarithmically** on $d$, unlike $\alpha$-local DP which is linear in $d$. Theorem 4.2: low-dim regression error $\tilde O(d^2\log(1/\delta)/n^2\varepsilon^2)$ for parameter (not excess-risk) estimation; Theorem 4.4: high-dim sparse regression $\tilde O((s\log d)^2\log(1/\delta)/n^2\varepsilon^2)$.

## Why it matters here
General background; no direct arena tie. Possible adjacent relevance: the **peeling / private top-$k$ selection** mechanism is a thresholding technique with the same flavor as sparse-mean estimators (P-class) and iterative hard-thresholding optimizers used in compressed-sensing-style configurations; the tracing-adversary lower-bound machinery is a clean template for proving information-theoretic obstructions, which the agent's failure-finding workflow could borrow stylistically.

## Open questions / connections
- Does the peeling top-$k$ + Laplace-noise selection mechanism transfer to **discrete combinatorial selection** problems (e.g. choosing $k$ active constraints in equioscillation / Sidon-like extremal problems) where exact top-$k$ is intractable?
- Can the tracing-adversary $\mathrm{Tr}\,A = \langle x-\mu, M(X)\rangle$ argument be adapted as a **lower-bound template** for any arena problem where the question is "how close can an estimator get to a target under structural constraints"?
- Extends [21, 28] tracing-attack bounds for Gaussian mean to sparse + regression settings; leaves open the $(\varepsilon, 0)$-pure-DP analogues and whether log factors in the upper bounds are tight.

## Key terms
differential privacy, $(\varepsilon,\delta)$-DP, tracing adversary, minimax risk lower bound, sparse mean estimation, high-dimensional linear regression, iterative hard thresholding, peeling algorithm, Gaussian mechanism, Laplace mechanism, Stein's lemma, sub-Gaussian, composition theorem
