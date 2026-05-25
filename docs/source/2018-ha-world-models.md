---
type: source
kind: paper
title: World Models
authors: David R Ha, J. Schmidhuber
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.10122
source_local: ../raw/2018-ha-world-models.pdf
topic: general-knowledge
cites:
---

# World Models

**Authors:** David R Ha, J. Schmidhuber  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.10122

## One-line
Train a large generative world model (VAE + MDN-RNN) unsupervised from random rollouts, then evolve a tiny linear controller on its compressed features — even entirely inside the model's "dream" — to solve RL tasks.

## Method
Three-part agent: (V) a Variational Autoencoder compresses each frame to a latent $z \in \mathbb{R}^{32}$ or $\mathbb{R}^{64}$; (M) an LSTM with a Mixture Density Network output models $P(z_{t+1} \mid a_t, z_t, h_t)$ as a 5-component factored Gaussian, with sampling temperature $\tau$; (C) a single linear layer $a_t = W_c [z_t\ h_t] + b_c$ with ~$10^3$ parameters trained by CMA-ES. V and M are trained first via backprop on 10,000 random rollouts; C is then evolved separately, optionally entirely inside the M-generated "dream" with no access to the real environment.

## Result
On CarRacing-v0, the full $[z_t\ h_t]$ controller scores $906 \pm 21$ over 100 trials — first reported solve (>900 threshold) and SOTA over prior DQN/A3C (343–652) and the leaderboard's 838. Ablations: $z_t$-only $632 \pm 251$; $z_t$ + hidden layer $788 \pm 141$ — confirming the RNN's predictive hidden state, not just compressed perception, carries the win. On VizDoom Take Cover, a policy trained *only* inside the dream (at $\tau = 1.15$ to prevent world-model exploits) transfers to the real env at $1092 \pm 556$ time steps vs 750 solve threshold. Cheating-the-model failure mode documented: low-$\tau$ dreams let C find adversarial exploits that "extinguish fireballs magically"; raising $\tau$ acts as regularization.

## Why it matters here
General background; no direct arena tie. Conceptually adjacent to the einstein agent's own architecture — a small controller (linear C, evolved by CMA-ES) layered on a large representation learner is structurally what we do with `mb` strategy notes + wiki features feeding per-problem optimizers; the dream/temperature trick is a cautionary tale about training on imperfect surrogates that may apply if we ever fit a learned surrogate scoring model for any of the 23 problems.

## Open questions / connections
- Could M's hidden state $h_t$ play the role of a "compressed memory" of failed approaches across our self-improvement cycles, analogous to how it carries fireball trajectories?
- The CMA-ES choice (Hansen 2016) is the same algorithm we use for small-parameter optimization — paper validates it at ~$10^3$ parameter scale, consistent with our usage envelope.
- "Iterative training" (§5) where C explores, V/M are retrained, repeat — open analogy to our gap-detect → ingest → distill loop, but no convergence theory given.

## Key terms
world model, VAE, MDN-RNN, mixture density network, LSTM, CMA-ES, evolution strategies, latent space, dream environment, model-based reinforcement learning, temperature sampling, controller-model separation, Schmidhuber, Ha
