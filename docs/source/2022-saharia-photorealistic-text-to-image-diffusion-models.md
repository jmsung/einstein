---
type: source
kind: paper
title: Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
authors: Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L. Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. S. Mahdavi, Raphael Gontijo Lopes, Tim Salimans, Jonathan Ho, David J. Fleet, Mohammad Norouzi
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2205.11487
source_local: ../raw/2022-saharia-photorealistic-text-to-image-diffusion-models.pdf
topic: general-knowledge
cites:
---

# Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding

**Authors:** Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L. Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. S. Mahdavi, Raphael Gontijo Lopes, Tim Salimans, Jonathan Ho, David J. Fleet, Mohammad Norouzi  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2205.11487

## One-line
Imagen is a text-to-image diffusion model that uses a frozen large language model (T5-XXL) as text encoder plus a cascade of conditional diffusion models, achieving state-of-the-art photorealism and image-text alignment.

## Key claim
Scaling the *frozen text-only language model* used as the text encoder improves text-to-image sample fidelity and alignment more than scaling the image diffusion U-Net; Imagen reaches zero-shot FID-30K = 7.27 on COCO, beating GLIDE (12.4), DALL-E 2 (10.4), and even COCO-trained Make-A-Scene (7.55).

## Method
Cascade of three diffusion models — base $64\times64$ (2B params) + two super-resolution stages to $256\times256$ and $1024\times1024$ — all conditioned on a frozen T5-XXL embedding sequence via cross-attention and pooled-vector addition. Classifier-free guidance with a new **dynamic thresholding** trick (clip $\hat{x}_0^t$ to $[-s,s]/s$ where $s$ is a high-percentile absolute pixel value) enables large guidance weights without saturation. Super-resolution stages use noise conditioning augmentation and a memory-efficient "Efficient U-Net" variant (2-3× faster steps/sec).

## Result
- Zero-shot COCO FID-30K = 7.27 (SOTA, no COCO training).
- Human raters rate Imagen on par with reference COCO images for image-text alignment (91.4 vs 91.9).
- On DrawBench (a new 200-prompt 11-category benchmark introduced here), human raters prefer Imagen over DALL-E 2, GLIDE, Latent Diffusion, and VQ-GAN+CLIP on both fidelity and alignment.
- T5-XXL beats CLIP text encoder on DrawBench across all 11 categories despite parity on COCO metrics.

## Why it matters here
General background; no direct arena tie. This is a computer-vision generative-modeling paper with no connection to sphere packing, autocorrelation, kissing numbers, or any Einstein Arena math problem category — it should not have been ingested into this wiki.

## Open questions / connections
- Does the "scaling the conditioner beats scaling the generator" finding generalize beyond text-to-image (e.g., to other conditional generative settings)?
- Dynamic thresholding is a percentile-based renormalization heuristic — is there a principled diffusion-process derivation?
- Efficient U-Net architectural choices (skip scaling, ResBlock ordering) — which are essential vs incidental?

## Key terms
diffusion models, text-to-image generation, T5-XXL, classifier-free guidance, dynamic thresholding, cascaded diffusion, noise conditioning augmentation, U-Net, CLIP, DrawBench, FID, COCO
