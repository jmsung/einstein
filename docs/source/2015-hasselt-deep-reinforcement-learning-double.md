---
type: source
kind: paper
title: Deep Reinforcement Learning with Double Q-Learning
authors: H. V. Hasselt, A. Guez, David Silver
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1509.06461
source_local: ../raw/2015-hasselt-deep-reinforcement-learning-double.pdf
topic: general-knowledge
cites:
---

# Deep Reinforcement Learning with Double Q-Learning

**Authors:** H. V. Hasselt, A. Guez, David Silver  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1509.06461

## One-line
Shows that DQN systematically overestimates action values on Atari, and that a minimal modification — using the online network to select but the target network to evaluate the max — fixes it.

## Key claim
The max operator in Q-learning's target $Y_t^Q = R_{t+1} + \gamma \max_a Q(S_{t+1},a;\theta_t)$ couples action selection with action evaluation, producing an upward bias whenever value estimates have any error; decoupling them (Double DQN) reduces bias and lifts normalized median Atari score from 93.5% to 114.7% (no-op) and 47.5% to 116.7% (tuned, human starts).

## Method
Replace the DQN target with $Y_t^{\text{DoubleDQN}} = R_{t+1} + \gamma Q(S_{t+1}, \arg\max_a Q(S_{t+1},a;\theta_t); \theta_t^-)$ — online weights $\theta_t$ pick the greedy action, target-network weights $\theta_t^-$ evaluate it. Reuses DQN's existing target network as the "second estimator," adding zero parameters or networks. Trained identically to DQN (RMSProp, $\gamma{=}0.99$, $\alpha{=}2.5\!\times\!10^{-4}$, 200M frames).

## Result
**Theorem 1 (lower bound on overestimation):** if $m$ actions have true value $V_*(s)$ and unbiased estimate errors with mean-square $C$, then $\max_a Q_t(s,a) \ge V_*(s) + \sqrt{C/(m-1)}$, and this bound is tight; the Double Q-learning estimator's analogous lower bound is $0$. **Theorem 2:** for iid uniform errors on $[-1,1]$, $\mathbb{E}[\max_a Q_t(s,a) - V_*(s)] = (m-1)/(m+1)$. Empirically, DQN's value estimates diverge dramatically from true returns on Asterix, Wizard of Wor, etc., with score collapse coinciding with the divergence; Double DQN stays stable and reaches new SOTA on Atari.

## Why it matters here
General background; no direct arena tie. The paper is about RL value-function bias, not the math-optimization problems this wiki tracks (sphere packing, autocorrelation, kissing numbers, etc.). The decouple-selection-from-evaluation pattern has a faint analogy to triple-verify (use a different estimator to check the one you used to select), but the connection is too loose to inform Einstein Arena problem solving directly.

## Open questions / connections
- Does the selection/evaluation decoupling principle generalize to other estimator-selection coupled procedures (e.g., basin-hopping where the same evaluator both picks the best basin and scores it)?
- The $\sqrt{C/(m-1)}$ lower bound on max-bias under unbiased noise is a clean inequality — possible faint relevance to optimizer overestimation bias when many candidate basins are scored by the same noisy evaluator.
- Extends Thrun-Schwartz (1993) noise-induced overestimation analysis and van Hasselt (2010) tabular Double Q-learning to function-approximation setting.

## Key terms
Q-learning, Double Q-learning, DQN, Double DQN, action-value overestimation, max-estimator bias, target network, experience replay, Atari 2600, deep reinforcement learning, Jensen's inequality, selection-evaluation decoupling
