---
type: source
kind: paper
title: Prediction with Corrupted Expert Advice
authors: Idan Amir, Idan Attias, Tomer Koren, Roi Livni, Y. Mansour
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.10286
source_local: ../raw/2020-amir-prediction-corrupted-expert-advice.pdf
topic: general-knowledge
cites:
---

# Prediction with Corrupted Expert Advice

**Authors:** Idan Amir, Idan Attias, Tomer Koren, Roi Livni, Y. Mansour  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.10286

## One-line
Shows that adaptive Multiplicative Weights with decreasing step sizes $\eta_t=\sqrt{\log(N)/t}$ achieves constant regret in stochastic expert prediction even when an adversary corrupts feedback up to total budget $C$.

## Key claim
In the adversarially-corrupted stochastic experts setting with $N$ experts, gap $\Delta$ between best and second-best mean losses, and corruption budget $C = \sum_t \|\tilde\ell_t - \ell_t\|_\infty$, adaptive MW attains expected pseudo-regret $\Theta(\log(N)/\Delta + C)$ — independent of horizon $T$, without knowing $\Delta$ or $C$.

## Method
FTRL with negative-entropy regularization and decreasing step size $\eta_t = \sqrt{\log(N)/t}$. Analysis uses a second-order regret bound for time-varying regularization (Theorem 10), then exploits a **self-bounding property**: the second-moment sum and the entropy-stability sum are each bounded by the pseudo-regret itself (up to exponentially-decaying terms summing to a constant), yielding a closed inequality $\mathbb{E}[R_T] \le \text{const} + \tfrac{15}{16}\mathbb{E}[R_T]$.

## Result
Theorem 5: adaptive MW (FTRL variant, Eq. 4) achieves $O(\log(N)/\Delta + C)$ expected pseudo-regret simultaneously in pure-stochastic, adversarially-corrupted, and fully-adversarial regimes. Theorem 9: the **OMD** variant (Eq. 5) with the same step-size schedule is strictly worse — suffers $\Omega(C/\Delta)$ regret (or exponential-in-$\sqrt{C}$) on a 2-expert instance, despite OMD and FTRL being equivalent under fixed step size. Lower bound $\Omega(\log(N)/\Delta + C)$ matches up to constants.

## Why it matters here
General background; no direct arena tie. Methodological interest only: the **self-bounding / instantaneous-regret-bounds-the-stability-term** trick is a general online-learning device that could inform adaptive weighting of multistart seeds or persona-vote aggregation in council-dispatch, but no concept currently in the einstein wiki cites it.

## Open questions / connections
- Tightening the OMD upper bound for pure stochastic (currently $O(\Delta^{-1}\log N\,\log^2(\Delta^{-1}\log N))$) — log-log gap with FTRL unresolved.
- Extends Wei–Luo (2018) and Zimmert–Seldin (2019) self-bounding analyses from bandits to full-information; analogue of Orabona–Pál (2018) FTRL-vs-OMD separation in the corrupted regime.
- Whether the FTRL/OMD gap persists for non-entropy regularizers (e.g. Tsallis, log-barrier) under corruption.

## Key terms
Multiplicative Weights, Follow the Regularized Leader, Online Mirror Descent, prediction with expert advice, adversarial corruption, stochastic bandits, pseudo-regret, self-bounding regret, adaptive step size, negative entropy regularization, Bregman divergence, Hedge algorithm
