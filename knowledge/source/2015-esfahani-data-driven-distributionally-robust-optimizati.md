---
type: source
kind: paper
title: "Data-driven distributionally robust optimization using the Wasserstein metric: performance guarantees and tractable reformulations"
authors: Peyman Mohajerin Esfahani, D. Kuhn
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1505.05116
source_local: ../raw/2015-esfahani-data-driven-distributionally-robust-optimizati.pdf
topic: general-knowledge
cites:
---

# Data-driven distributionally robust optimization using the Wasserstein metric: performance guarantees and tractable reformulations

**Authors:** Peyman Mohajerin Esfahani, D. Kuhn  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1505.05116

## One-line
Shows that stochastic programs robustified over a Wasserstein ball around the empirical distribution reduce to finite convex (often LP) programs and enjoy finite-sample out-of-sample guarantees.

## Key claim
For loss $\ell(\xi)$ equal to a pointwise max of finitely many concave functions, $\sup_{Q \in B_\varepsilon(\widehat P_N)} \mathbb{E}_Q[\ell(\xi)]$ equals the optimum of an explicit finite-dimensional convex program; with radius $\varepsilon_N(\beta) \sim (\log(c_1/\beta)/(c_2 N))^{1/\max\{m,2\}}$ this optimum is a $1-\beta$ upper confidence bound on the true out-of-sample cost (Thm 3.5).

## Method
Convex-duality reformulation of the inner $\sup$ over the Wasserstein ball $B_\varepsilon(\widehat P_N) = \{Q : d_W(\widehat P_N, Q) \le \varepsilon\}$ using Kantorovich–Rubinstein duality and conjugate functions, yielding a finite program with one block per training sample. Finite-sample guarantee comes from the Fournier–Guillin measure-concentration bound $\mathbb{P}^N(d_W(P,\widehat P_N) \ge \varepsilon) \le c_1 \exp(-c_2 N \varepsilon^{\max\{m,2\}})$ under a light-tail (exponential-moment) assumption. Worst-case distributions are constructed from a companion finite convex program.

## Result
Tractable LP reformulations are obtained when the norm is $\ell_1$ or $\ell_\infty$ and $\ell$ is a max/min of affine functions, a polytope indicator, or the value function of a parametric LP linear in $\xi$. Asymptotic consistency (Thm 3.6): if $\sum_N \beta_N < \infty$ and $\varepsilon_N(\beta_N) \to 0$, the robust optimizer converges a.s. to a solution of the true stochastic program. Empirically the effective radius decays like $N^{-1/2}$, much faster than the worst-case $N^{-1/m}$.

## Why it matters here
General background; no direct arena tie. Relevant only as methodological context for any agent task requiring distributionally robust estimates from small samples (e.g. estimating arena-vs-local verifier drift, or score distributions under noisy evaluators) — Wasserstein-ball reformulations could in principle bound worst-case expected loss from $N$ runs.

## Open questions / connections
- Extends moment-based DRO (Delage–Ye, Wiesemann–Kuhn–Sim) and Kullback–Leibler ambiguity (Jiang–Guan, Hu–Hong) to a Wasserstein ball that actually contains continuous $P$ around discrete $\widehat P_N$.
- Practical $N^{-1/2}$ decay vs theoretical $N^{-1/m}$ — is the dimension dependence avoidable for smooth/convex losses?
- Generalization beyond pointwise-max-of-concave losses (non-convex $\ell$, support constraints, multi-stage) only partially addressed.

## Key terms
Wasserstein metric, distributionally robust optimization, Kantorovich–Rubinstein duality, ambiguity set, empirical distribution, measure concentration, Fournier–Guillin, finite-sample guarantee, sample average approximation, convex reformulation, linear programming, Kullback–Leibler divergence, optimizer's curse, light-tailed distribution, mean-risk portfolio
