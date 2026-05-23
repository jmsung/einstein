---
type: source
kind: paper
title: Learning Transferable Visual Models From Natural Language Supervision
authors: Alec Radford, Jong Wook Kim, Chris Hallacy, A. Ramesh, Gabriel Goh, S. Agarwal, G. Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, I. Sutskever
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2103.00020
source_local: ../raw/2021-radford-learning-transferable-visual-models.pdf
topic: general-knowledge
cites:
---

# Learning Transferable Visual Models From Natural Language Supervision

**Authors:** Alec Radford, Jong Wook Kim, Chris Hallacy, A. Ramesh, Gabriel Goh, S. Agarwal, G. Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, I. Sutskever  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2103.00020

## One-line
CLIP jointly trains an image encoder and a text encoder by contrastive matching of 400M (image, caption) web pairs, yielding a single model that zero-shot transfers to dozens of vision tasks via natural-language class descriptions.

## Key claim
A simple contrastive objective — "predict which caption in a batch goes with which image" — scales efficiently and produces zero-shot classifiers competitive with fully supervised baselines: zero-shot CLIP matches the original ResNet-50's ImageNet accuracy without using any of its 1.28M training labels, and the best ViT-L/14@336px reaches 76.2% zero-shot ImageNet top-1.

## Method
Train an image encoder (ResNet variants or ViT-B/16, B/32, L/14) and a text Transformer (63M params, BPE, 76-token cap) from scratch with a symmetric InfoNCE / N-pair contrastive loss over an $N\times N$ batch of cosine similarities $I_e\cdot T_e^\top/\tau$, with $\tau$ a learned log-parameterized scalar clipped at 100. Batch size 32,768; Adam with decoupled weight decay; cosine LR; mixed precision + gradient checkpointing + sharded similarity computation; only augmentation is random square crop. Zero-shot inference embeds prompt-templated class names ("a photo of a {class}") with the text encoder and picks the argmax cosine to the image embedding.

## Result
On a 27-dataset benchmark, zero-shot CLIP is competitive with linear-probe ResNet-50 on most tasks; transfer accuracy is a smooth, predictable function of compute across ~2 orders of magnitude (RN50 → RN50x64; ViT-B/32 → ViT-L/14@336px). The contrastive objective is ~4× more sample-efficient than a bag-of-words predictive baseline and ~12× more than a Transformer language-model caption objective (Fig. 2). Zero-shot CLIP is markedly more robust to distribution shift than equally-accurate supervised ImageNet models (ImageNet-R, ObjectNet, ImageNet-Sketch, ImageNet-Vid, YouTube-BB all improved over prior SOTA). OCR, geolocalization (IM2GPS), and action recognition (UCF-101, Kinetics-700, RareAct +10 pts) emerge as side-effects of natural-language supervision.

## Why it matters here
General background; no direct arena tie — CLIP is a vision-language pretraining paper, not a math-optimization result. Possible tangential relevance: the demonstrated reliability of *contrastive symmetric InfoNCE over large batches* and of *learned-temperature softmax with clipped logits* are general patterns the agent could reuse if any future embedding-based retrieval over the wiki itself (e.g., qmd, gap-detector) is built or tuned.

## Open questions / connections
- How well does language-conditioned zero-shot transfer hold for *structured* domains (math, code, formal proofs) where natural-language class names are less natural? Not addressed.
- The learned-temperature clip (≤100) was needed for training stability — is the optimal $\tau$ schedule scale-dependent? Left to future work.
- Extends Zhang et al. 2020 (ConVIRT) and Joulin et al. 2016; leaves open whether a generative caption objective ever catches up to contrastive given enough compute.

## Key terms
CLIP, contrastive language-image pretraining, InfoNCE, N-pair loss, symmetric cross-entropy, cosine similarity, learned temperature, zero-shot transfer, Vision Transformer, ResNet, prompt engineering, distribution shift robustness
