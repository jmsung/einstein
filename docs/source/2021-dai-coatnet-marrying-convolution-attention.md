---
type: source
kind: paper
title: "CoAtNet: Marrying Convolution and Attention for All Data Sizes"
authors: Zihang Dai, Hanxiao Liu, Quoc V. Le, Mingxing Tan
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.04803
source_local: ../raw/2021-dai-coatnet-marrying-convolution-attention.pdf
topic: general-knowledge
cites:
---

# CoAtNet: Marrying Convolution and Attention for All Data Sizes

**Authors:** Zihang Dai, Hanxiao Liu, Quoc V. Le, Mingxing Tan  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.04803

## One-line
A hybrid image-classification architecture that fuses depthwise convolution and self-attention into one block via relative attention, then stacks Conv-Conv-Transformer-Transformer stages to win across all data scales.

## Key claim
CoAtNet attains 86.0% ImageNet top-1 with ImageNet-1K only, 88.56% with ImageNet-21K pre-training (matching ViT-Huge trained on 23× more JFT-300M data), and a new SOTA of 90.88% with JFT-3B at 1.5× less compute than ViT-G/14.

## Method
Combine depthwise convolution kernel $w_{i-j}$ and softmax attention into a single pre-normalization relative-attention layer: $A_{i,j} \propto \exp(x_i^\top x_j + w_{i-j})$, giving translation-equivariance + input-adaptive weighting + global receptive field at minimal extra cost. Vertically stack five stages S0–S4 with 2× spatial downsampling each; ablation across {C-C-C-C, C-C-C-T, C-C-T-T, C-T-T-T, ViT_rel} identifies **C-C-T-T** as the best trade-off — convolution stages handle low-level local patterns, Transformer stages capture global capacity. MBConv blocks (inverted bottleneck, SE) used for convolution; both block types share pre-activation residual structure.

## Result
On ImageNet-1K only, CoAtNet-3 hits 84.5%@224, 86.0%@512, matching NFNet-F5. With 21K pretrain, CoAtNet-4 reaches 88.56%@512 — equal to ViT-H/14 (JFT-300M) using 23× less data and 2.2× fewer steps. With JFT-3B, CoAtNet-7 reaches 90.88% at 2586B FLOPs (vs ViT-G/14: 90.45% at 5160B). Ablations show relative attention boosts generalization (not just capacity); C-C-T-T transfers better than C-T-T-T despite equal pretrain loss.

## Why it matters here
General background; no direct arena tie — this is computer-vision architecture work, not math optimization. Marginal relevance: the inductive-bias-vs-capacity framing parallels the agent's tension between hand-coded math priors (wiki concepts, axioms) and large-search optimization, and the "stack specialized blocks in the right order" insight is a generic ML design heuristic.

## Open questions / connections
- Does C-C-T-T-style staged inductive-bias-first design extend to dense prediction (detection, segmentation)?
- Why does relative attention help generalization more than capacity? Connection to translation-equivariance theory.
- Trade-off between local vs global attention on TPU vs GPU — the local-attention rejection here is hardware-specific.

## Key terms
CoAtNet, relative attention, depthwise convolution, MBConv, inverted bottleneck, Vision Transformer, inductive bias, translation equivariance, multi-stage architecture, ImageNet, JFT-300M, self-attention
