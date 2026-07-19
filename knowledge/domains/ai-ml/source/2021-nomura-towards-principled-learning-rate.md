---
type: source
kind: paper
title: Towards a Principled Learning Rate Adaptation for Natural Evolution Strategies
authors: M. Nomura, I. Ono
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2112.10680
source_local: ../raw/2021-nomura-towards-principled-learning-rate.pdf
topic: general-knowledge
cites:
---

# Towards a Principled Learning Rate Adaptation for Natural Evolution Strategies

**Authors:** M. Nomura, I. Ono  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2112.10680

## One-line
Proposes adapting the xNES learning rate online based on how accurately the natural gradient is being estimated, measured via the KL-divergence movement along an evolution path in covariance-parameter space.

## Key claim
A learning rate scaled by the length $l_\theta$ of an evolution path (compared to its expected value $\gamma_\theta$ under a random-function null) yields xNES that is both faster than the default-conservative setting on easy problems and more robust than aggressive fixed rates on hard/multimodal problems, without prior tuning.

## Method
xNES on a multivariate normal $\mathcal{N}(m,\sigma^2 BB^\top)$ is augmented with an evolution path $p_\Sigma$ accumulating Fisher-normalized covariance movements $I_{\Sigma}^{1/2}\delta\Sigma$. The squared path length (a movement in KL divergence) is compared to its random-function expectation $\gamma_\theta$, and learning rates $\eta_\sigma,\eta_B$ are multiplicatively updated as $\eta \leftarrow \eta\cdot\exp(\beta(l_\theta/\alpha - \gamma_\theta))$, clipped to $[\eta_{\min}=\text{xNES default},\,\eta_{\max}=1]$. A second-order Taylor approximation gives a closed-form expression for $E[\|I_\Sigma^{1/2}\delta\Sigma\|^2]\approx (1+\eta_\sigma^2/(4d\mu_w))\,\eta_B^2(d^2{+}d{-}2)/\mu_w + \eta_\sigma^2$ used as the normalizer each iteration.

## Result
On 10-d benchmarks (Sphere, Ellipsoid, Rastrigin, Bohachevsky), the adaptive scheme: (i) raises $\eta$ above default when $\lambda$ is large enough for the natural-gradient estimate to be reliable, (ii) keeps $\eta$ near default when $\lambda$ is small (e.g. $\lambda=10$ on Sphere), and (iii) matches the best fixed-$\eta$ setting (typically $8\times$ default) on Rastrigin while strictly dominating in success rate at small populations where fixed-$8\times$ diverges. Hyperparameters $\alpha_\sigma=\alpha_B=1.3$, $\beta=0.2$ were chosen empirically.

## Why it matters here
General background for any arena problem solved by black-box continuous optimization (basin-hopping, CMA-ES rank-$\mu$, parallel tempering on smooth landscapes) — provides a principled, parameter-free trigger for when to crank the step size vs. stay conservative, complementing the existing compute-router and basin-hopping techniques. Most directly relevant to problems whose surrogate is smooth-multimodal (P11 kissing/contact graph, P15/P16 equioscillation polishing, P17 strict-tol traps) where fixed aggressive rates risk overshoot.

## Open questions / connections
- Does the KL-movement / evolution-path diagnostic transfer to CMA-ES rank-$\mu$ as used in this repo, or only xNES? (Authors cite PSA-CMA-ES [Nishida-Akimoto 2016/2018] which adapts $\lambda$, not $\eta$ — orthogonal axis.)
- Hyperparameters $\alpha,\beta$ are set empirically; principled selection (or schedule) is open.
- No comparison to DX-NES variants or to the maximum-likelihood adaptation of Loshchilov et al. 2014 — relative merits unclear.
- Extension to constrained / implicitly-constrained problems (relevant to several arena problems with equality constraints) untested.

## Key terms
natural evolution strategies, xNES, CMA-ES, learning rate adaptation, natural gradient, Fisher information, KL divergence, evolution path, covariance matrix adaptation, step-size control, black-box optimization, multimodal benchmarks, Nomura, Akimoto, fitness shaping
