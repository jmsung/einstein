---
type: source
kind: paper
title: "RANK-NOSH: Efficient Predictor-Based Architecture Search via Non-Uniform Successive Halving"
authors: Ruochen Wang, Xiangning Chen, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.08019
source_local: ../raw/2021-wang-rank-nosh-efficient-predictor-based-architecture.pdf
topic: general-knowledge
cites:
---

# RANK-NOSH: Efficient Predictor-Based Architecture Search via Non-Uniform Successive Halving

**Authors:** Ruochen Wang, Xiangning Chen, Minhao Cheng, Xiaocheng Tang, Cho-Jui Hsieh  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.08019

## One-line
A predictor-based neural architecture search method that uses non-uniform successive halving plus pairwise ranking to cut search budget ~5× while matching SOTA.

## Key claim
RANK-NOSH achieves competitive-or-better NAS results on NAS-Bench-101, NAS-Bench-201, and DARTS with ~5× less search budget than prior predictor-based methods (e.g., 990 vs 5000 epochs on DARTS; 292 vs 1200 on NAS-Bench-201 CIFAR-10).

## Method
NOSH maintains a pyramid-shaped candidate pool where level-$i$ holds architectures trained for $e^{(i)}$ epochs; top fraction $r$ moves up each level, but losers are kept (non-uniform). New proposals enter at level-1 and compete to ascend. A Siamese GIN-based ranker is trained with pairwise binary labels $y(\alpha_1,\alpha_2)$ defined by either training-epoch level or validation accuracy within a level, sidestepping regression's need for fully-trained accuracies. Training-free pruning proxies (e.g., weight magnitude at init) act as a free level-0.

## Result
On NAS-Bench-201 CIFAR-10/100/ImageNet16-120, RANK-NOSH reaches 94.26%/73.51%/46.34% test accuracy at 292/5550/5550 epoch budgets vs ~20000 for arch2vec-BO. On DARTS CIFAR-10, 2.53% ± 0.02 avg test error at 990 epochs vs 5000 for BANANAS/arch2vec. Robust across schedules $E$ and move ratios $r \in [0.4, 0.7]$; degrades only at $r=0.3$.

## Why it matters here
General background; no direct arena tie. The pyramid-schedule + pairwise-rank-from-partial-training pattern could conceivably apply to allocating compute across optimizer seeds/configurations in basin-hopping or multistart campaigns, but it is not an arena math technique.

## Open questions / connections
- Could FTBO-style learning-curve prediction replace NOSH's fixed schedule with adaptive pause/resume — same idea for terminating poor optimizer trajectories early?
- Pairwise-ranking-from-partial-training as a model for ranking optimizer configurations without running each to convergence — relevant to multistart triage?
- Train-free proxies (Jacobian covariance, synaptic flow magnitude) — analogue would be "cheap predictors of basin quality from initial geometry" before launching polish.

## Key terms
neural architecture search, successive halving, predictor-based NAS, pairwise ranking, learning to rank, Siamese GIN, hyperparameter optimization, bandit, Hyperband, early stopping, training-free proxies, NAS-Bench-201, DARTS
