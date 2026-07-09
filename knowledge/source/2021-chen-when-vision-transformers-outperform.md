---
type: source
kind: paper
title: When Vision Transformers Outperform ResNets without Pretraining or Strong Data Augmentations
authors: Xiangning Chen, Cho-Jui Hsieh, Boqing Gong
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2106.01548
source_local: ../raw/2021-chen-when-vision-transformers-outperform.pdf
topic: general-knowledge
cites:
---

# When Vision Transformers Outperform ResNets without Pretraining or Strong Data Augmentations

**Authors:** Xiangning Chen, Cho-Jui Hsieh, Boqing Gong  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2106.01548

## One-line
Applying a sharpness-aware optimizer (SAM) to Vision Transformers and MLP-Mixers smooths their extremely sharp converged loss landscapes, letting them match or beat ResNets on ImageNet without large-scale pretraining or strong data augmentations.

## Key claim
On ImageNet with only Inception-style preprocessing, SAM lifts ViT-B/16 from 74.6% → 79.9% and Mixer-B/16 from 66.4% → 77.4% top-1 (vs. +0.8% for ResNet-152), with even larger relative gains on robustness benchmarks (ImageNet-C: +9.9% for ViT-B/16, +15.0% for Mixer-B/16).

## Method
Diagnose convergence quality via loss-landscape visualization (filter normalization, Li et al. 2018), dominant Hessian eigenvalue $\lambda_{\max}$ via power iteration, average flatness $L^N_{\text{train}}=\mathbb{E}_{\epsilon\sim\mathcal{N}}[L_{\text{train}}(w+\epsilon)]$, and NTK condition number $\kappa=\lambda_1/\lambda_m$. Then optimize with SAM (Foret et al. 2021): the minimax $\min_w \max_{\|\epsilon\|_2\le\rho} L_{\text{train}}(w+\epsilon)$, solved with the first-order approximation $\hat\epsilon(w)=\rho\nabla_w L/\|\nabla_w L\|_2$ followed by a gradient step at $w+\hat\epsilon$. Tune $\rho$ per architecture (larger for sharper models: $\rho\approx0.2$ for ViT-B/16, $\rho\approx0.6$ for Mixer-B/16, vs. $\rho\approx0.02$–$0.05$ for ResNets).

## Result
Pre-SAM Hessians: $\lambda_{\max}=$ 179.8 (ResNet-152), 738.8 (ViT-B/16), 1644.4 (Mixer-B/16); SAM collapses ViT/Mixer values to 20.9 / 22.5. NTK $\kappa$ diverges for ViT/Mixer (14468) but is stable for ResNets (2801.6). Sub-diagonal Hessian analysis shows shallower layers (especially the patch-embedding layer) carry the largest curvature, consistent with the recursion $H_k=(a_{k-1}a_{k-1}^T)\otimes\mathcal{H}_k$ with $\mathcal{H}_k=B_k W_{k+1}^T \mathcal{H}_{k+1} W_{k+1} B_k+D_k$. SAM increases weight norms (so weight decay alone is insufficient regularization) and drives sparser GELU activations in early layers; ViTs are intrinsically very sparse. SAM also rescues SGD-trained ViTs (71.5% → 79.1%), and gains compound across adversarial, supervised-contrastive, and transfer-learning settings.

## Why it matters here
General background; no direct arena tie. Tangential relevance: the loss-landscape / Hessian-curvature / flatness-vs-generalization framing is the same toolset used to diagnose basin rigidity in continuous arena optimizers, and the minimax $\min_w\max_{\|\epsilon\|\le\rho}$ formulation is structurally identical to robust-optimization patches one might apply to verifier-tolerance traps (P14, P17).

## Open questions / connections
- Could a SAM-style $\rho$-ball minimax be repurposed to find arena solutions robust to verifier tolerance drift (analogous to P14's tolerance-band exploitation)?
- The Hessian-recursion decomposition (Botev et al. 2017) gives a principled per-layer curvature diagnostic — is there an analog for per-coordinate/per-block curvature on geometric-packing parameterizations?
- Sharp-minimum / flat-minimum dichotomy as a generalization signal connects to basin-hopping accept/reject heuristics: does landscape sharpness predict which local optima are "real" vs. tolerance artifacts?

## Key terms
sharpness-aware minimization, SAM, vision transformer, ViT, MLP-Mixer, loss landscape, Hessian eigenvalue, neural tangent kernel, NTK condition number, flatness, generalization, minimax optimization, filter normalization, weight decay
