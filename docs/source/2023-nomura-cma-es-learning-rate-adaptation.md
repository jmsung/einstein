---
type: source
kind: paper
title: CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?
authors: Masahiro Nomura, Youhei Akimoto, Isao Ono
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2304.03473v3
source_local: ../raw/2023-nomura-cma-es-learning-rate-adaptation.pdf
ingested_for_concept: cma-es-with-warmstart.md
cites: 
---

# CMA-ES with Learning Rate Adaptation: Can CMA-ES with Default Population Size Solve Multimodal and Noisy Problems?

**Authors:** Masahiro Nomura, Youhei Akimoto, Isao Ono  ·  **Year:** 2023  ·  **Source:** http://arxiv.org/abs/2304.03473v3

## One-line
Proposes LRA-CMA-ES, a learning-rate adaptation that lets CMA-ES with default population size solve multimodal and noisy problems without hyperparameter tuning.

## Key claim
Adapting the learning rates $\eta_m$ and $\eta_\Sigma$ to maintain a constant signal-to-noise ratio (SNR $= \alpha\eta$) allows CMA-ES with default $\lambda = 4+\lfloor 3\ln d\rfloor$ to succeed on Rastrigin, Bohachevsky, Griewank, and strongly-noisy ($\sigma_n^2 = 10^6$) variants where fixed-$\eta$ CMA-ES fails.

## Method
Update $m$ and $\Sigma$ with adaptive factors $\eta_m, \eta_\Sigma \in (0,1]$; estimate the SNR $= \|\mathbb{E}[\Delta]\|_F^2 / \mathrm{Tr}(F\,\mathrm{Cov}[\Delta])$ via exponential moving averages of $\Delta$ and $\|\Delta\|^2$ in a local Fisher-identity coordinate ($\sqrt{\Sigma^{-1}}$ whitening for $m$, the analogous tensor map for $\Sigma$). Multiplicatively adjust $\eta \leftarrow \eta\exp(\min(\gamma\eta,\beta)\Pi_{[-1,1]}(\mathrm{SNR}/(\alpha\eta) - 1))$, capped at 1, with a $\sigma \leftarrow \sigma\cdot\eta_m^{(t)}/\eta_m^{(t+1)}$ correction from quality-gain analysis.

## Result
With defaults $\alpha=1.4$, $\beta_m=0.1$, $\beta_\Sigma=0.03$, $\gamma=0.1$, LRA-CMA-ES achieves 100% success on Rastrigin up to $d=40$ at default $\lambda$, matches small-$\eta$ tuned CMA-ES on weak noise ($\sigma_n^2=1$), and uniquely keeps improving under strong noise ($\sigma_n^2=10^6$) on Noisy Sphere/Ellipsoid/Rastrigin where all fixed-$\eta$ baselines stall. Failure mode: 40-D Schaffer, where the SNR adaptation under-shrinks $\eta$.

## Why it matters here
Directly relevant to compute-router routing for CMA-ES workloads (P1, P11, P14, P15, P16 polish phases) — it removes the $\lambda$-vs-$\eta$ tuning sweep that currently consumes a council cycle, and offers a worker-count-friendly alternative to PSA-CMA-ES for parallel basin-hopping on local M5 / Modal. Complements existing wiki coverage of parallel tempering and basin rigidity by giving a tuning-free convergence regulator.

## Open questions / connections
- Why does LRA fail on 40-D Schaffer where tuned small-$\eta$ succeeds? — SNR estimator pathology near non-smooth fractal landscapes.
- Should $\beta_m, \beta_\Sigma$ scale as $O(1/d), O(1/d^2)$ with parameter degrees of freedom (authors' own conjecture)?
- Head-to-head vs PSA-CMA-ES [Nishida & Akimoto 2018] on the same noisy multimodal benchmarks — which adapts faster, which uses compute better?

## Key terms
CMA-ES, learning rate adaptation, signal-to-noise ratio, evolution strategy, multimodal optimization, noisy black-box optimization, Fisher information metric, natural gradient, population size adaptation, step-size correction, Rastrigin, quality gain analysis
