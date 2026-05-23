---
type: source
kind: paper
title: Efficient Non-Parametric Optimizer Search for Diverse Tasks
authors: Ruochen Wang, Yuanhao Xiong, Minhao Cheng, Cho-Jui Hsieh
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2209.13575
source_local: ../raw/2022-wang-efficient-non-parametric-optimizer-search.pdf
topic: general-knowledge
cites:
---

# Efficient Non-Parametric Optimizer Search for Diverse Tasks

**Authors:** Ruochen Wang, Yuanhao Xiong, Minhao Cheng, Cho-Jui Hsieh  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2209.13575

## One-line
Automates the discovery of gradient-based optimizer update rules by formulating the symbolic expression space as a super-tree and traversing it with Monte Carlo tree search, finding strong optimizers in only 128 evaluations.

## Key claim
A simple Monte Carlo tree-search adaptation over a tight tree-structured space of symbolic update rules, augmented with rejection sampling (descent test, score thresholding) and equivalent-form detection (constraint pruning + hash-based equivalence), discovers optimizers that beat hand-designed (SGD/Adam/RMSprop) and prior automated (NOS-RL) baselines across six task families using ~1% of NOS-RL's >10k-evaluation budget (e.g., 77.02% vs 76.21% top NOS-RL on CIFAR-10 ConvNet).

## Method
Optimizer update rules $\phi(\nabla_\theta L)$ are viewed as math expressions with an innate tree structure (nodes = unary/binary operators, leaves = inputs like $g, m_1, m_2$, decays, constants); all expressions of length $\le N$ are arranged into a "tight" super-tree where each path encodes one optimizer (Proposition 1). Search uses MCT: at each level, child nodes are scored by Monte-Carlo unrolling to leaves, and the best child is expanded; sample efficiency is boosted by (i) a train-free descent test rejecting $\phi$ that fail $\mathbb{E}_{u\sim\mathcal{N}(0,1)}\cos(\phi(\nabla L),\nabla L) > \lambda_d$ on random Gaussian "gradients", (ii) score thresholding to stabilize MC estimates, (iii) on-the-fly constraint pruning of mathematically redundant branches (e.g., $\mathrm{sign}\circ\mathrm{sign}$, $\log\circ\exp$), and (iv) probing-vector hashing for fast equivalence checks against the evaluated pool.

## Result
With 4 MCT levels × 32 MC samples = 128 total evaluations and super-tree depth 10, discovered optimizers beat baselines on: MNISTNET digit classification (lowest cumulative train loss + best transfer to ReLU/2Layer/Big variants, where the LSTM-based L2LGD2 overfits its search task); CIFAR-10 ConvNet (77.02% ± 0.19 vs PowSign-cd 76.21%, AddSign-cd 76.07%, Adam 73.42%); adversarial attack on robust models, where log-based forms like $\log(|\mathrm{cd} + \mathrm{sign}(g)|)$ rival the heavily hand-tuned APGD; GAT node classification (sign-based forms dominate; "products2" $= \mathrm{ld}\cdot(\mathrm{sign}(m_1) - \mathrm{RMSprop})$ transfers across 5 graph datasets); and BERT fine-tuning on GLUE subsets (cola2, rte optimizers consistently outperform AdamW). Search wall-clock: ~0.92h on RTX 2080ti (MNIST) vs L2LGD2's 2.62h; ~7h for CIFAR-10 ConvNet.

## Why it matters here
General background; no direct arena tie. The math-optimization problems in Einstein Arena are solved by classical optimizers (L-BFGS, basin-hopping, CMA-ES, mpmath polish), not by learned-update-rule deep-learning optimizers — but the meta-idea of (i) representing a search space as a tight expression super-tree and (ii) using MCT + rejection-sampling + hashing for equivalent-form pruning could inspire symbolic search over *parameterizations* or *coordinate transforms* for specific arena problems, and the descent-test trick (cheap train-free validity filter) is a transferable design pattern.

## Open questions / connections
- Could the super-tree + MCT framework be adapted to symbolic-regression-style search over *parameterizations* of arena configurations (analogue: search the symbolic form of a coordinate change that linearizes a basin)?
- Authors note that precomputed momentum terms ($m_1, m_2, m_3$, Adam, RMSprop) are hard-coded inputs — searching for novel internal-state update rules is left as future work; relates to deep symbolic regression literature [Petersen et al. 2021, AI Feynman / Udrescu-Tegmark 2020].
- The descent-test idea ($\cos$ with $\nabla L > \lambda_d$) is a general "cheap necessary condition" filter — analogous filters (e.g., monotonicity / KKT-residual sanity checks) could screen optimizer-config proposals in arena work before full evaluation.

## Key terms
optimizer search, non-parametric optimizer, symbolic regression, Monte Carlo tree search, MCTS, expression tree, super-tree, rejection sampling, equivalent-form hashing, descent test, AutoML, NOS-RL, AutoML-Zero, L2LGD2, APGD adversarial attack, BERT fine-tuning, GAT node classification
