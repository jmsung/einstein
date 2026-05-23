---
type: source
kind: paper
title: Online Learning with Predictable Sequences
authors: A. Rakhlin, Karthik Sridharan
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1208.3728
source_local: ../raw/2012-rakhlin-online-learning-predictable-sequences.pdf
topic: general-knowledge
cites:
---

# Online Learning with Predictable Sequences

**Authors:** A. Rakhlin, Karthik Sridharan  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1208.3728

## One-line
Online linear optimization algorithms that exploit a known "predictable process" $M_t$ to get regret scaling with $\sum_t \|x_t - M_t\|_*^2$ instead of $\sqrt{T}$, while retaining worst-case guarantees.

## Key claim
For any predictable sequence $M_t$ (arbitrary function of the past), modified FTRL / Mirror Descent algorithms achieve regret $O(\sqrt{\sum_{t=1}^T \|x_t - M_t\|_*^2})$ — tight when $M_t$ predicts $x_t$ well, only $2\times$ worse than standard bounds when it doesn't. Path-length and variance bounds drop out as special cases ($M_t = x_{t-1}$ or $M_t = \frac{1}{t-1}\sum_{s<t} x_s$).

## Method
**Optimistic FTRL**: at step $t+1$, minimize $\eta\langle f, \sum_{s\le t} x_s + M_{t+1}\rangle + R(f)$ with self-concordant barrier $R$ — i.e., "guess the next move" and bake it into the leader. **Optimistic Mirror Descent**: two-projection update, first against observed $x_t$, then against predicted $M_{t+1}$, using a 1-strongly convex regularizer. Extensions cover bandit feedback (SCRiBLe variants) and concurrent model selection across a finite class $\Pi$ of predictable processes via a secondary experts/bandit game on loss $\|x_t - M_t^\pi\|_*^2$.

## Result
Lemma 2 (Optimistic MD): $\sum_t\langle f_t - f^*, x_t\rangle \le \eta^{-1} R_{\max}^2 + \frac{\eta}{2}\sum_t \|x_t - M_t\|_*^2$. Lemma 1 (Optimistic FTRL with self-concordant barrier): same form with $R(f^*) \le \vartheta \log T$ constant. With model selection (Lemma 5): regret $\le \eta^{-1} R_{\max}^2 + 3.2\eta(\inf_{\pi\in\Pi}\sum_t \|x_t - M_t^\pi\|_*^2 + \log|\Pi|)$ — competitive with the best predictor in $\Pi$ in hindsight. Doubling trick removes need to know $\sum\sigma_t^2$ in advance.

## Why it matters here
General background; no direct arena tie. The "predictable process + adversarial noise" decomposition is a useful framing for any online/iterative optimizer where prior structure (trend, autoregressive guess, phase) can be exploited — relevant philosophically to compute scheduling and adaptive optimizer-selection, but not to the specific math/combinatorial extremal problems on Einstein Arena.

## Open questions / connections
- Which full-information statistics $M_t'$ admit good bandit-feedback estimators $M_t$ (beyond reservoir-sampled means of Hazan-Kale)?
- Extension of variation-style bounds to Follow-the-Perturbed-Leader algorithms is novel here — limits of the random-playout technique?
- Connection to time-series / stock prediction: can autoregressive or phase-based $M_t$ models be learned online with provable regret?

## Key terms
online learning, predictable sequences, regret minimization, optimistic mirror descent, optimistic FTRL, self-concordant barrier, SCRiBLe, multi-armed bandit, variance bounds, path-length bounds, Rakhlin, Sridharan, Hazan-Kale, model selection, Bregman divergence
