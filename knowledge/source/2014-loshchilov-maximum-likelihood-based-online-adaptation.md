---
type: source
kind: paper
title: Maximum Likelihood-Based Online Adaptation of Hyper-Parameters in CMA-ES
authors: I. Loshchilov, Marc Schoenauer, M. Sebag, N. Hansen
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.2623
source_local: ../raw/2014-loshchilov-maximum-likelihood-based-online-adaptation.pdf
topic: general-knowledge
cites:
---

# Maximum Likelihood-Based Online Adaptation of Hyper-Parameters in CMA-ES

**Authors:** I. Loshchilov, Marc Schoenauer, M. Sebag, N. Hansen  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.2623

## One-line
Proposes self-CMA-ES: a meta-CMA-ES that online-adapts the covariance-matrix learning rates of an inner CMA-ES by maximizing the likelihood (via rank agreement) of the top-$\mu$ sampled solutions.

## Key claim
The default hyper-parameters $c_1, c_\mu, c_c$ of CMA-ES — which are derived as fixed functions of $n$ and $\lambda$ — are substantially sub-optimal when $\lambda$ is enlarged ($\lambda=100$, ~10× default), and online self-adaptation recovers problem- and phase-dependent optimal values, yielding up to ~1.5× speedup on Sharp Ridge and matching CMA-ES elsewhere on the BBOB noiseless testbed.

## Method
Two interdependent CMA-ES instances: a *primary* CMA-ES optimizing $f(x)$, and an *auxiliary* CMA-ES whose search space is the hyper-parameter vector $\theta = (c_1, c_\mu, c_c) \in [0, 0.9]^3$ (with constraint $c_1 + c_\mu \le 0.9$). The auxiliary objective $h_t(\theta)$ is a rank-based surrogate for log-likelihood: backtrack the primary CMA-ES one step, replay the update with candidate $\theta$, compute Mahalanobis distances $d_i = \sqrt{(x_i - m)^\top C^{-1}(x_i - m)}$ for the actually-observed top individuals, and score by the weighted sum of likelihood-ranks vs $f$-ranks. One auxiliary generation per primary generation (cost: $\lambda_h = 20$× the internal CMA-ES cost, negligible vs $f$ evaluations).

## Result
On BBOB Sphere, Rosenbrock, Rotated Ellipsoid, Sharp Ridge (10D and 20D, $\lambda=100$, 15 runs, IPOP restarts): self-CMA-ES adapts $c_1, c_\mu, c_c$ from uniform $[0, 0.9]$ initialization to values consistently *larger* than the conservative defaults (especially $c_\mu, c_c$), with $c_\mu$ high during early covariance learning and decaying near the optimum. Performance matches CMA-ES on most problems and reaches ~1.5× speedup on Sharp Ridge. No degradation observed; the dynamic adaptation captures problem- and phase-specific structure.

## Why it matters here
Directly informs the **CMA-ES techniques** family used across arena problems (sphere packing, kissing, autocorrelation polish) — the default learning rates are tuned for small $\lambda$ and become conservative under our typical large-population / GPU-parallel-tempering regimes. The retrospective "what hyper-parameters would have generated these top samples" idea is reusable as a generic meta-optimization stance (cf. surrogate-assisted CMA-ES [13–14]).

## Open questions / connections
- Does self-CMA-ES help on multi-modal / noisy / constrained problems where the default $\lambda$-derived schedule is most suspect?
- Can the same retrospective-likelihood scheme adapt $\sigma$-path damping $d_\sigma$, $c_\sigma$, or the recombination weights $w_i$ themselves?
- Connection to natural evolution strategies and Rprop-style stochastic learning-rate adaptation [15]; also to surrogate-assisted saACM-ES [14] which inspired the two-layer scheme.
- For arena polish phases: would a "near-optimum" detector trigger a hand-off from adaptive $c_\mu$ (large, fast learning) to fixed small $c_\mu$ (stable shape)?

## Key terms
CMA-ES, self-CMA-ES, covariance matrix adaptation, online hyper-parameter adaptation, evolution strategies, learning rate $c_1$, learning rate $c_\mu$, cumulation $c_c$, Mahalanobis distance, rank-based likelihood, BBOB benchmark, IPOP restart, meta-optimization, Loshchilov, Hansen
