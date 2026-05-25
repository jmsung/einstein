---
type: source
kind: paper
title: "CoCa: Contrastive Captioners are Image-Text Foundation Models"
authors: Jiahui Yu, Zirui Wang, Vijay Vasudevan, Legg Yeung, Mojtaba Seyedhosseini, Yonghui Wu
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2205.01917
source_local: ../raw/2022-yu-coca-contrastive-captioners-image-text.pdf
topic: general-knowledge
cites:
---

# CoCa: Contrastive Captioners are Image-Text Foundation Models

**Authors:** Jiahui Yu, Zirui Wang, Vijay Vasudevan, Legg Yeung, Mojtaba Seyedhosseini, Yonghui Wu  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2205.01917

## One-line
A unified image-text foundation model trained jointly with contrastive and captioning losses via a decoupled encoder-decoder, subsuming CLIP-style dual-encoder, classification-style single-encoder, and generative encoder-decoder paradigms.

## Key claim
A single pretrained CoCa checkpoint achieves SOTA on visual recognition, crossmodal retrieval, captioning, and multimodal understanding: 86.3% zero-shot ImageNet top-1, 90.6% frozen-encoder, 91.0% finetuned; 88.0/88.5/81.1% on Kinetics-400/600/700; 47.4% on Moments-in-Time; 82.3% VQA; 120.6 CIDEr on NoCaps.

## Method
Encoder-decoder transformer where the text decoder is split into $n_\text{uni}$ unimodal layers (no cross-attention, produce text-only embeddings via a learnable [CLS] token) and $n_\text{multi}$ multimodal layers (cross-attend to image encoder). Two task-specific attentional poolers ($n_\text{query}=1$ for contrastive, $n_\text{query}=256$ for generative) extract pooled image features. Joint loss $\mathcal{L}_\text{CoCa} = \lambda_\text{Con}\mathcal{L}_\text{Con} + \lambda_\text{Cap}\mathcal{L}_\text{Cap}$ with $\lambda_\text{Cap}=2, \lambda_\text{Con}=1$, trained from scratch in one stage on JFT-3B label-prompts + ALIGN alt-text pairs, 2.1B params, 500k steps, batch 65,536 on 2,048 TPUv4.

## Result
Outperforms CLIP, ALIGN, Florence, LiT, BASIC, SimVLM across all benchmark categories with one checkpoint. Ablations show captioning loss subsumes cross-entropy classification ($\mathcal{L}_\text{Cls}$ is a special case of $\mathcal{L}_\text{Cap}$ over the label-name vocabulary); joint loss matches captioning-only training cost while adding retrieval capability; symmetric decoder split ($n_\text{uni}=n_\text{multi}$) is optimal; single learnable [CLS] token beats multi-token aggregation for unimodal text embedding.

## Why it matters here
General background; no direct arena tie. Vision-language foundation modeling is outside the Einstein Arena math optimization scope (sphere packing, autocorrelation, kissing numbers, etc.).

## Open questions / connections
- Whether the "one loss subsumes another as a special case" framing (captioning ⊇ classification when vocabulary = label set) generalizes to other dual-objective settings.
- Decoupled-decoder design as a template for multi-objective training sharing one forward pass — relevant only if the agent ever combines heterogeneous learned objectives.
- Robustness gains on corrupted inputs from joint contrastive+generative training; not exercised in this repo's numerical-optimization pipeline.

## Key terms
contrastive learning, image-text pretraining, foundation model, encoder-decoder transformer, captioning loss, CLIP, ALIGN, attentional pooling, unimodal decoder, multimodal decoder, vision transformer, zero-shot transfer
