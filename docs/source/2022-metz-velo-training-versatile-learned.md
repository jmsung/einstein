---
type: source
kind: paper
title: "VeLO: Training Versatile Learned Optimizers by Scaling Up"
authors: Luke Metz, James Harrison, C. Freeman, Amil Merchant, Lucas Beyer, James Bradbury, Naman Agrawal, Ben Poole, Igor Mordatch, Adam Roberts, Jascha Narain Sohl-Dickstein
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2211.09760
source_local: ../raw/2022-metz-velo-training-versatile-learned.pdf
topic: general-knowledge
cites:
---

# VeLO: Training Versatile Learned Optimizers by Scaling Up

**Authors:** Luke Metz, James Harrison, C. Freeman, Amil Merchant, Lucas Beyer, James Bradbury, Naman Agrawal, Ben Poole, Igor Mordatch, Adam Roberts, Jascha Narain Sohl-Dickstein  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2211.09760

## One-line
A neural-network optimizer meta-trained at massive scale (~4000 TPU-months) that replaces hand-designed update rules like Adam, requires zero hyperparameter tuning, and beats learning-rate-tuned baselines on a broad benchmark of deep learning tasks.

## Key claim
VeLO outperforms learning-rate-tuned Adam on 100% of 83 VeLOdrome benchmark tasks, achieves >4× speedup on ~50% of tasks and >16× speedup on >14%, and beats a 1000-trial NAdamW hyperparameter search on >85% of tasks with a single untuned run.

## Method
Hierarchical hypernetwork: a per-tensor LSTM (512 hidden units) consumes aggregated tensor-level features (Adam-style moment EMAs, parameter mean/variance, training-completion fraction, loss) and *generates the weights* of a tiny per-parameter MLP (2 hidden layers, 4 hidden units) that emits the scalar update for each parameter; tensor LSTMs coordinate via a max-pooled global context signal. Meta-trained on a parametric distribution of thousands of tasks (MLPs, ConvNets, ResNets, Transformers, ViTs, RNNs, VAEs, etc.) with task-augmentations and rejection sampling by runtime. Meta-gradients estimated by Evolution Strategies on *full-length* unrolls targeting final training loss, with per-task unit-norm gradient normalization, an increasing curriculum, and 1–4K asynchronous TPU workers over ~4 weeks.

## Result
VeLO is hyperparameter-free (only input is total step count), trains faster than LR-tuned Adam on all 83 VeLOdrome tasks, matches or beats Adam-with-cosine-schedule on 5/6 MLCommons workloads (ImageNet ViT/ResNet50, WMT17 Transformer, LibriSpeech DeepSpeech/Conformer; weaker only on OGBG graph NN), and adapts its update schedule to the declared horizon. Limitations: unreliable past 200K steps, ~2× Adam's memory, longer JAX compile times, weaker on out-of-distribution regimes (graph NNs, RL).

## Why it matters here
General background; no direct arena tie — VeLO targets deep-learning training and the arena's optimizers are hand-designed numerical methods (L-BFGS, SLSQP, basin-hopping, CMA-ES, parallel tempering, mpmath polish) on small low-dim landscapes, not gradient descent on neural nets. Tangential relevance: confirms that meta-learned, problem-conditioned update rules can replace fixed-form optimizers when there is a *distribution* of tasks to amortize over — a possible long-horizon framing for a learned meta-optimizer over the 23 arena problems, but currently out of scope.

## Open questions / connections
- Can a similar meta-learning approach work on a small, fixed distribution of math-optimization landscapes (e.g. 23 arena problems × seeds) where each "task" is a basin-hopping run rather than NN training?
- Extends Andrychowicz et al. 2016 (L2L by gradient descent), Wichrowska et al. 2017 (hierarchical learned opt), Metz et al. 2020a/2022 (per-parameter MLP opt); leaves open extended-horizon generalization, second-order feature integration (KFac/Shampoo), and tunable test-time objectives (validation loss, unbounded horizons).
- The ES-on-full-unrolls + unit-norm cross-task gradient averaging recipe may transfer to other meta-optimization settings; gradient staleness from heterogeneous task runtimes (~4 orders of magnitude) is flagged as a novel, under-studied issue.

## Key terms
learned optimizer, meta-learning, hypernetwork, LSTM optimizer, Evolution Strategies, ES meta-gradient, hyperparameter-free optimization, Adam, NAdamW, Shampoo, per-parameter MLP, full-length unrolls, VeLOdrome, MLCommons, neural network training
