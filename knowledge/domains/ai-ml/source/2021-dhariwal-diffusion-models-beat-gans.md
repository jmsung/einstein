---
type: source
kind: paper
title: Diffusion Models Beat GANs on Image Synthesis
authors: Prafulla Dhariwal, Alex Nichol
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2105.05233
source_local: ../raw/2021-dhariwal-diffusion-models-beat-gans.pdf
topic: general-knowledge
cites:
---

# Diffusion Models Beat GANs on Image Synthesis

**Authors:** Prafulla Dhariwal, Alex Nichol  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2105.05233

## One-line
A UNet-architecture ablation plus a classifier-gradient guidance scheme makes diffusion models surpass GANs on ImageNet image synthesis while preserving distribution coverage.

## Key claim
Class-conditional diffusion with classifier guidance achieves FID 2.97 on ImageNet 128×128, 4.59 on 256×256, and 7.72 on 512×512 (improved to 3.94 and 3.85 respectively when combined with upsampling), beating BigGAN-deep with as few as 25 forward passes per sample.

## Method
Refined UNet (multi-resolution attention at 32/16/8, BigGAN up/downsampling residual blocks, 64 channels per attention head, adaptive group normalization $\mathrm{AdaGN}(h,y)=y_s\,\mathrm{GroupNorm}(h)+y_b$ injecting timestep/class embeddings). Classifier guidance: train $p_\phi(y|x_t,t)$ on noised images, then shift the reverse-process mean by $s\Sigma\nabla_{x_t}\log p_\phi(y|x_t)$ (Algorithm 1) or modify the noise prediction $\hat\epsilon = \epsilon_\theta - \sqrt{1-\bar\alpha_t}\,\nabla_{x_t}\log p_\phi$ for DDIM (Algorithm 2). The gradient scale $s>1$ samples from a sharpened $\propto p(y|x)^s$, trading recall for precision.

## Result
On ImageNet 256×256, classifier guidance raises a conditional model from FID 10.94 → 4.59 (precision 0.69→0.82, recall 0.63→0.52). Guidance scale sweep (Figure 4) shows monotone precision/IS gain vs recall loss; classifier guidance Pareto-dominates BigGAN's truncation trick on FID-vs-IS. Compute: matches BigGAN-deep with comparable V100-day budgets and beats it at 1/8–1/3 of full training iterations.

## Why it matters here
General background; no direct arena tie. The classifier-guidance trick is a clean example of $\log p \propto \log p_0 + s\log p_y$ tempering — a generic recipe for sharpening a base distribution by an auxiliary score, conceptually adjacent to importance-tempered sampling / parallel tempering used in arena optimizers, but not directly applicable to the deterministic math-optimization problems here.

## Open questions / connections
- Score-function tempering as a general fidelity/diversity knob — analogous to temperature in parallel tempering / annealing schedules.
- Trade-off curves (Figure 5) as a methodology template for ablating any diversity-vs-quality knob.
- Whether classifier-free guidance (later work) supersedes the explicit-classifier approach; not addressed here.

## Key terms
diffusion models, DDPM, DDIM, classifier guidance, score matching, UNet, adaptive group normalization, FID, Inception Score, precision-recall trade-off, variational lower bound, Langevin dynamics, BigGAN, ImageNet, generative modeling
