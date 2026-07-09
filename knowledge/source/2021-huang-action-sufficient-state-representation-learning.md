---
type: source
kind: paper
title: Action-Sufficient State Representation Learning for Control with Structural Constraints
authors: Biwei Huang, Chaochao Lu, Liu Leqi, José Miguel Hernández-Lobato, C. Glymour, B. Scholkopf, Kun Zhang
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2110.05721
source_local: ../raw/2021-huang-action-sufficient-state-representation-learning.pdf
topic: general-knowledge
cites:
---

# Action-Sufficient State Representation Learning for Control with Structural Constraints

**Authors:** Biwei Huang, Chaochao Lu, Liu Leqi, José Miguel Hernández-Lobato, C. Glymour, B. Scholkopf, Kun Zhang  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2110.05721

## One-line
Learns a minimal-sufficient subset of latent state dimensions (ASRs) for RL by encoding causal-graph structure among observations, states, actions, and rewards in a structured sequential VAE.

## Key claim
Under Markov + faithfulness on the generative environment model, the *Action-Sufficient state Representations* $\mathbf{s}^{\mathrm{ASR}}_t \subseteq \mathbf{s}_t$ — exactly those state dimensions with a directed path to a future reward — are a minimal sufficient statistic for the optimal policy, characterized by $s_{i,t} \in \mathbf{s}^{\mathrm{ASR}}_t \iff s_{i,t} \not\perp\!\!\!\perp R_{t+1} \mid a_{t-1:t}, \mathbf{s}^{\mathrm{ASR}}_{t-1}$ (Proposition 1).

## Method
Generative POMDP model with binary structural matrices $D^{s\to o}, D^{s\to r}, D^{a\to r}, D^{s\to s}, D^{a\to s}$ encoding which variables influence which. A Structured Sequential VAE (SS-VAE) — LSTM encoder + Mixture Density Network, decoder with deconv reconstruction + reward predictor, MoG transition dynamics — jointly learns the structure and the latents, regularized by (i) conditional MI maximizing $I(\tilde{s}^{\mathrm{ASR}}; R_{t+1} \mid \cdot)$ and minimizing $I(\tilde{s}^C; R_{t+1} \mid \cdot)$, (ii) information-bottleneck KL term, (iii) $L_1$ sparsity on all structural matrices. Identifiability proved up to orthogonal rotation in the linear-Gaussian case (Proposition 2) via second-order statistics.

## Result
Theoretical: in linear-Gaussian case, $\bar{D}^{s\to o}\bar{D}^{s\to o\top}$, $D^{a\to r}$, $\bar{D}^{s\to o}D_s^k D^{a\to s}$ ($k\ge 0$) and noise covariances $\Sigma_e, \Sigma_\epsilon$ are identifiable from second-order statistics. Empirical: on CarRacing and VizDoom (take-cover), ASR-based DDPG/DQN beats world-model (Ha & Schmidhuber 2018), PlaNet, Dreamer, DRQN, and full-latent baselines in both sample efficiency and asymptotic return; learned $D^{s\to r}, D^{a\to s}$ are visibly sparse.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are deterministic math-optimization (sphere packing, autocorrelation, kissing numbers), not partially-observable RL — there is no observation model, reward MDP, or latent-state graph to recover.

## Open questions / connections
- Extends causal-state-representation work (Zhang et al. 2019a) and bisimulation methods (Zhang et al. 2021) by making the latent graph explicit and sparsity-regularized.
- Identifiability is shown only for linear-Gaussian; the nonlinear case is heuristic — no guarantee SS-VAE recovers the true ASR set.
- Hyperparameters $\lambda_{1\ldots 8}$ are hand-tuned; no principled selection.

## Key terms
action-sufficient state representation, ASR, POMDP, causal graph, structural constraints, sequential VAE, minimal sufficient statistic, information bottleneck, mixture density network, identifiability, d-separation, faithfulness, world model, Dreamer, reinforcement learning
