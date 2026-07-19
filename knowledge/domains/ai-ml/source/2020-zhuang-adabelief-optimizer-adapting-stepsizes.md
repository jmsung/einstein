---
type: source
kind: paper
title: "AdaBelief Optimizer: Adapting Stepsizes by the Belief in Observed Gradients"
authors: Juntang Zhuang, Tommy M. Tang, Yifan Ding, S. Tatikonda, N. Dvornek, X. Papademetris, J. Duncan
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.07468
source_local: ../raw/2020-zhuang-adabelief-optimizer-adapting-stepsizes.pdf
topic: general-knowledge
cites:
---

# AdaBelief Optimizer: Adapting Stepsizes by the Belief in Observed Gradients

**Authors:** Juntang Zhuang, Tommy M. Tang, Yifan Ding, S. Tatikonda, N. Dvornek, X. Papademetris, J. Duncan  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.07468

## One-line
A drop-in Adam variant that divides the momentum $m_t$ by the EMA of squared *residuals* $(g_t - m_t)^2$ instead of squared gradients $g_t^2$, scaling step size by how much the observed gradient agrees with its prediction.

## Key claim
Replacing Adam's denominator $\sqrt{v_t}$ (EMA of $g_t^2$) with $\sqrt{s_t}$ (EMA of $(g_t-m_t)^2$) gives Adam-speed early convergence, SGD-level generalization (ResNet18/ImageNet: 70.08 vs SGD 70.23 vs Adam 63.79), and GAN training stability (lowest FID on WGAN/WGAN-GP/SN-GAN on CIFAR-10), with no extra hyperparameters and $O(\sqrt{T})$ convex regret / $O(\log T/\sqrt{T})$ non-convex.

## Method
Modify Adam by tracking $s_t = \beta_2 s_{t-1} + (1-\beta_2)(g_t - m_t)^2 + \epsilon$ (variance-of-gradient-around-its-EMA) and updating $\theta_t \leftarrow \theta_{t-1} - \alpha \hat m_t / (\sqrt{\hat s_t} + \epsilon)$. Bayesian interpretation: Adam approximates the gradient covariance with the *uncentered* second moment $E[g g^\top]$, AdaBelief uses the *centered* covariance $\mathrm{Var}(g)$ — a strictly better posterior estimator when $\|Eg\|^2 \gg \mathrm{Var}(g)$, which fires "large step in low-variance directions, small step in high-variance directions."

## Result
Convex regret bound (Thm 2.1): $\sum_t f_t(\theta_t) - f_t(\theta^*) \le O(\sqrt{T})$ with the same form as Adam/AMSGrad but with $s_T^{1/2}$ replacing $v_T^{1/2}$ — potentially tighter since $E s_t = \mathrm{Var}(g_t) \le E g_t^2 = E v_t$. Non-convex (Thm 2.2): $\min_t E\|\nabla f(\theta_t)\|^2 = O(\log T/\sqrt T)$. Empirically: matches SGD on ImageNet ResNet18, beats Adam on CIFAR VGG/ResNet/DenseNet, lowest LSTM perplexity on Penn TreeBank, lowest FID on WGAN/WGAN-GP/SN-GAN.

## Why it matters here
General background; no direct arena tie. AdaBelief is a first-order ML optimizer aimed at neural-network training, not the LP / SDP / mpmath / basin-hopping / parallel-tempering toolkit used on Einstein Arena problems. Possibly relevant only if the agent ever trains a learned surrogate or neural ansatz — otherwise out of scope for the optimizer router.

## Open questions / connections
- Could the "belief" residual-EMA idea be ported to non-NN optimizers (e.g., CMA-ES step-size adaptation, basin-hopping temperature) as a "trust the gradient when it agrees with its running prediction" heuristic?
- Bayesian framing (centered vs uncentered covariance) connects to natural gradient / Fisher-information methods (Amari, Pascanu) — the appendix proposes a weak-prior schedule but leaves it open.
- Relation to Padam, SWATS, AdaBound (Adam→SGD interpolation): AdaBelief recovers SGD-like generalization without the explicit schedule.

## Key terms
AdaBelief, Adam, adaptive optimizer, exponential moving average, gradient variance, centered second moment, sign descent, convex regret bound, non-convex convergence, generalization gap, GAN training stability, Bayesian gradient posterior
