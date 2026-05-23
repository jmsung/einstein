---
type: source
kind: paper
title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"
authors: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, M. Minderer, G. Heigold, S. Gelly, Jakob Uszkoreit, N. Houlsby
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.11929
source_local: ../raw/2020-dosovitskiy-image-worth-16x16-words.pdf
topic: general-knowledge
cites:
---

# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale

**Authors:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, M. Minderer, G. Heigold, S. Gelly, Jakob Uszkoreit, N. Houlsby  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.11929

## One-line
Introduces the Vision Transformer (ViT): apply a standard NLP Transformer directly to sequences of flattened image patches and match/beat CNNs on image classification when pre-trained at sufficient scale.

## Key claim
A pure Transformer, with no convolutional inductive bias beyond patchification, achieves SOTA image classification when pre-trained on large datasets (ImageNet-21k, JFT-300M): 88.55% on ImageNet, 90.72% on ImageNet-ReaL, 94.55% on CIFAR-100, 77.63% on VTAB-19, while using $2$–$4\times$ less pre-training compute than comparable ResNets (BiT).

## Method
Split image $x \in \mathbb{R}^{H \times W \times C}$ into $N = HW/P^2$ patches of size $P \times P$, flatten and linearly project to $D$-dim patch embeddings, prepend a learnable `[class]` token, add learnable 1D position embeddings, then feed to a standard Transformer encoder ($L$ alternating layers of multi-head self-attention + MLP with GELU, pre-LayerNorm and residual). Fine-tuning at higher resolution keeps patch size fixed (longer sequences) and 2D-interpolates the pre-trained position embeddings. Hybrid variants substitute CNN feature maps as the patch source.

## Result
ViT-H/14 (JFT-300M pre-trained) reaches 88.55% ImageNet top-1 at 2.5k TPUv3-core-days vs BiT-L's 87.54% at 9.9k and Noisy Student EfficientNet-L2 at 12.3k. Scaling laws (Figs. 3–5): on small datasets (ImageNet-1k) ViT underperforms ResNets due to missing inductive bias, but crosses over around 14M–100M images and continues to improve where ResNets plateau. Inspection: position embeddings auto-learn 2D row/column topology; some attention heads attend globally even at the lowest layers, with "attention distance" increasing with depth — analogous to CNN receptive fields, but globally accessible from layer 1.

## Why it matters here
General background; no direct arena tie. Relevant only as methodology: the "minimal inductive bias + scale" lesson and the patch-tokenization trick are the conceptual ancestors of transformer-based scientific/structured-data models, but neither sphere packing, autocorrelation, nor the Arena's optimization problems are directly addressed.

## Open questions / connections
- Does the scale-trumps-inductive-bias pattern extend to structured math objects (lattice configurations, autocorrelation sequences) where symmetry priors are strong and data is scarce?
- Self-supervised ViT (masked patch prediction) yields a 2% gain over scratch but trails supervised pre-training by 4% — gap to contrastive / generative pre-training left open.
- Axial attention variants (Axial-ViT) improve accuracy at higher compute cost; efficient TPU-optimized axial implementations remain unbuilt.

## Key terms
Vision Transformer, ViT, self-attention, multi-head attention, patch embedding, position embedding, transfer learning, inductive bias, ImageNet, JFT-300M, BiT ResNet, pre-training scaling, attention distance
