---
type: source
kind: paper
title: "The Cost of Privacy in Generalized Linear Models: Algorithms and Minimax Lower Bounds"
authors: T. Cai, Yichen Wang, Linjun Zhang
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2011.03900
source_local: ../raw/2020-cai-cost-privacy-generalized-linear.pdf
topic: general-knowledge
cites:
---

# The Cost of Privacy in Generalized Linear Models: Algorithms and Minimax Lower Bounds

**Authors:** T. Cai, Yichen Wang, Linjun Zhang  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2011.03900

## One-line
Constructs differentially private estimators for generalized linear model (GLM) parameters in both low- and high-dimensional sparse regimes, and proves matching minimax lower bounds via a new "score attack" technique.

## Key claim
$(\varepsilon,\delta)$-DP estimation of GLM parameters achieves squared $\ell_2$ risk $\tilde O\!\left(\tfrac{d}{n} + \tfrac{d^2 \log(1/\delta)}{n^2\varepsilon^2}\right)$ in low-d (Thm 1) and $\tilde O\!\left(\tfrac{s^* \log d}{n} + \tfrac{(s^*\log d)^2 \log(1/\delta)}{n^2\varepsilon^2}\right)$ in the $s^*$-sparse high-d regime (Thm 3); matching lower bounds (Thms 5, 6) certify near-optimality up to log factors.

## Method
Two algorithms: (i) noisy projected gradient descent on the GLM negative log-likelihood with Gaussian perturbation per iteration, exploiting *restricted* strong convexity / smoothness (Negahban et al.) since global strong convexity fails for GLMs; (ii) noisy iterative hard thresholding with a Laplace-noise "Peeling" top-$s$ selection operator for the sparse case. Lower bounds use a novel **score attack** $A_\beta((y_i,x_i),M) = \nabla_\beta \log f_\beta(y_i\mid x_i)^\top (M(y,X)-\beta)$ built from Stein's lemma, generalizing the tracing-attack technique beyond Gaussian/Beta-Binomial to arbitrary parametric exponential families.

## Result
Linear convergence in $O(\log n)$ iterations under restricted strong convexity (constant $\alpha$) and restricted smoothness (constant $\gamma$). The score attack satisfies soundness ($\mathbb{E}A = 0$ on independent copy) and completeness ($\sum_i \mathbb{E}A_i = \sum_j \partial_{\beta_j} \mathbb{E}M_j$), yielding lower bounds via a Stein-lemma identity $\mathbb{E}_\pi \sum_j \partial_{\beta_j}\mathbb{E}M_j \gtrsim d$ for Gaussian prior on $\beta$. Sparse case uses top-$s^*$ Gaussian-order-statistic prior giving $\gtrsim s^*\log(d/s^*)$.

## Why it matters here
General background; no direct arena tie. The score-attack framework is a clean recipe for lower-bounding estimation in any exponential family, which could conceivably inform information-theoretic obstructions in arena problems whose verifiers reduce to parametric inference — but none of the 23 problems are currently framed that way.

## Open questions / connections
- Can the score-attack template lower-bound estimation in *non-parametric* or constrained families (sphere packings, autocorrelation functionals)?
- Extension to other M-estimation problems with restricted strong convexity / smoothness is claimed but not worked out.
- Closes the gap left by tracing-attack ad-hoc-ness flagged in Murakonda–Shokri–Theodorakopoulos (2019) and Shokri et al. (2017).

## Key terms
differential privacy, generalized linear models, score attack, Stein's lemma, tracing attack, minimax lower bound, restricted strong convexity, iterative hard thresholding, noisy gradient descent, Peeling mechanism, Gaussian mechanism, sparse high-dimensional estimation
