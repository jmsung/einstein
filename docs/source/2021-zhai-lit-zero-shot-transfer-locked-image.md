---
type: source
kind: paper
title: "LiT: Zero-Shot Transfer with Locked-image text Tuning"
authors: Xiaohua Zhai, Xiao Wang, Basil Mustafa, A. Steiner, Daniel Keysers, Alexander Kolesnikov, Lucas Beyer
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2111.07991
source_local: ../raw/2021-zhai-lit-zero-shot-transfer-locked-image.pdf
topic: general-knowledge
cites:
---

# LiT: Zero-Shot Transfer with Locked-image text Tuning

**Authors:** Xiaohua Zhai, Xiao Wang, Basil Mustafa, A. Steiner, Daniel Keysers, Alexander Kolesnikov, Lucas Beyer  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2111.07991

## One-line
Contrastively align a *frozen* pre-trained image encoder with a trainable text encoder on noisy image-text pairs to get a strong zero-shot classifier without retraining the vision backbone.

## Key claim
Locking the image tower (initialized from a strong pre-trained model) while training only the text tower with contrastive loss beats both from-scratch CLIP/ALIGN-style training and fine-tuning the image tower; with ViT-g/14 on a 4B-pair private dataset, LiT reaches $85.2\%$ zero-shot ImageNet top-1 (vs. CLIP $76.2\%$, ALIGN $76.4\%$) and $82.5\%$ on ObjectNet ($+10.2\%$ over CLIP).

## Method
Two-tower contrastive learning with a global (cross-device) InfoNCE-style loss, but with three init/lock variants — $Lu$ (locked pre-trained image + unlocked random text), $Uu$ (unlocked pre-trained image), $uu$ (both random, the CLIP/ALIGN baseline) — plus linear projection heads to a shared embedding dimension. The recommended recipe is $Lu$: freeze a strongly pre-trained image encoder (supervised JFT/ImageNet-21k, or self-supervised DINO/MoCo-v3) and only train the text encoder to "read out" its representation.

## Result
On YFCC100m-CLIP $+$ CC12M with public ViT-L/16, LiT achieves $75.7\%$ zero-shot ImageNet ($+30.9\%$ over prior public-data SOTA OpenCLIP $34.8\%$). Data efficiency: $81.7\%$ ImageNet 0-shot after only $300\mathrm{M}$ image-text pairs, vs CLIP needing $12.8\mathrm{B}$ pairs to reach $76.2\%$ (~40× less data). Ablations show locking helps even at $4\mathrm{B}$-pair scale, that locking *worsens* in-distribution contrastive loss but *improves* OOD loss (COCO captions) — the locked encoder preserves general representation quality that fine-tuning destroys.

## Why it matters here
General background; no direct arena tie. This is a CLIP-family vision-language paper — none of the Einstein Arena problems (sphere packing, autocorrelation, kissing numbers, sieve theory, extremal graphs) involve image-text alignment or contrastive learning over visual data. The "freeze a strong prior, train only the alignment layer" idea has no clear analogue in this repo's optimizer stack.

## Open questions / connections
- Partial-freeze schedules (e.g. lock early, unlock late, separate learning rates) — authors flag this as open; no setup strictly beat $Lu$.
- Structured VTAB tasks (counting, depth, angle estimation) remain near random-guess despite prompt engineering — open how to make contrastive vision-language models *count*.
- Multilingual generalization via SentencePiece byte-fallback tokenization works without explicit multilingual pre-training — surprising and underexplored.

## Key terms
contrastive learning, CLIP, ALIGN, zero-shot transfer, Vision Transformer, ViT-g/14, locked-image tuning, image-text alignment, InfoNCE, two-tower model, DINO, MoCo-v3, transfer learning, representation locking
