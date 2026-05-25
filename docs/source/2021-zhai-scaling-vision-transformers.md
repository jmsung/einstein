---
type: source
kind: paper
title: Scaling Vision Transformers
authors: Xiaohua Zhai, Alexander Kolesnikov, N. Houlsby, Lucas Beyer
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.04560
source_local: ../raw/2021-zhai-scaling-vision-transformers.pdf
topic: general-knowledge
cites:
---

# Scaling Vision Transformers

**Authors:** Xiaohua Zhai, Alexander Kolesnikov, N. Houlsby, Lucas Beyer  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.04560

## One-line
Empirically characterizes how Vision Transformer (ViT) error rate scales with model size, dataset size, and compute, and trains a 2B-parameter ViT-G/14 that reaches 90.45% top-1 on ImageNet.

## Key claim
Representation-quality error follows a double-saturating power law $E = a(C+d)^{-b} + c$ in compute $C$, with fits like $E = 0.09 + 0.26(C+0.01)^{-0.35}$ (ImageNet finetune) and $E = 0.12 + 0.63(C+0.52)^{-0.32}$ (10-shot), holding across two orders of magnitude of compute; ViT-G/14 sets new SOTA at 90.45% ImageNet top-1 and 84.86% 10-shot.

## Method
Train ViT models from 5M to 2B parameters on datasets from 1M to 3B images (ImageNet-21k and proprietary JFT-3B), varying compute from <1 to >10,000 TPUv3 core-days. Architecture/training refinements: decoupled weight decay for the prediction head (strong head WD improves few-shot transfer at cost of upstream accuracy), removal of the [class] token in favor of MAP/GAP pooling (saves padding-induced memory), memory-efficient Adafactor with half-precision first momentum, and a reciprocal-square-root LR schedule with warmup + cooldown enabling multiple training-duration evaluations from a single run.

## Result
Three scaling regularities: (i) compute-performance Pareto frontier is a saturating power law with both a high-compute floor $c$ (irreducible error) and a low-compute shift $d$; (ii) representation quality is bottlenecked separately by model size and by dataset size — small models (Ti/16, B/32) gain nothing from data past ~30M images, while L/16 and G/14 keep improving from 1B → 3B; (iii) large models are markedly more sample-efficient (Ti/16 needs ~100× more images than L/16 to reach the same 10-shot error). ViT-G/14 achieves 90.45% ImageNet, 83.33% ImageNet-V2, 90.81% ReaL, 70.53% ObjectNet, 78.29% VTAB.

## Why it matters here
General background; no direct arena tie. Methodology is transfer learning for vision, not math optimization; the only conceptual hook to Einstein Arena work is the **double-saturating power-law form** $E = a(C+d)^{-b} + c$ as a template for fitting compute-vs-score curves, which could in principle apply to characterizing optimizer convergence on a fixed Arena problem.

## Open questions / connections
- Does the double-saturating power law $E = a(C+d)^{-b} + c$ fit Einstein Arena optimizer trajectories (compute vs. score-gap-to-SOTA) the way it fits ViT? Would let us forecast diminishing returns and pre-audit Modal spend.
- Extends Kaplan et al.'s NLP scaling laws [22] to supervised vision pretraining; the "irreducible entropy" $c$ in $E = aC^{-b} + c$ also appears in generative-model scaling [19].
- Sample-efficiency of large models depends on having $>1$B images — no analog exists for the Arena's fixed-problem regime; possibly irrelevant.

## Key terms
Vision Transformer, ViT, scaling laws, power law, double saturation, irreducible error, compute-optimal training, few-shot transfer, JFT-3B, Adafactor, weight decay decoupling, attention pooling
