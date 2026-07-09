---
type: source
kind: paper
title: Constrained Graphic Layout Generation via Latent Optimization
authors: Kotaro Kikuchi, E. Simo-Serra, Mayu Otani, Kota Yamaguchi
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2108.00871
source_local: ../raw/2021-kikuchi-constrained-graphic-layout-generation.pdf
topic: general-knowledge
cites:
---

# Constrained Graphic Layout Generation via Latent Optimization

**Authors:** Kotaro Kikuchi, E. Simo-Serra, Mayu Otani, Kota Yamaguchi  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2108.00871

## One-line
Generates graphic design layouts (UI, document, magazine) that satisfy user-specified alignment/overlap/relational constraints by optimizing the latent code of a pre-trained layout GAN, instead of retraining for each new constraint set.

## Key claim
A single pre-trained unconstrained GAN, combined with augmented-Lagrangian latent-space optimization, beats prior constrained-layout methods (NDN) on three datasets — e.g., on PubLayNet with 10% relational constraints: constraint violation 4.61% vs NDN 17.30%, while matching or improving Max IoU (0.36 vs 0.31) and Alignment.

## Method
LayoutGAN++ — a Transformer-based conditional GAN ($G: (Z, L) \mapsto B$ of bounding boxes) with an auxiliary reconstruction decoder on the discriminator's $h_{\text{const}}'$ embedding for positional-trend awareness. Constrained generation (CLG-LO) freezes $\hat{G}, \hat{D}$ and solves $\min_Z -\hat{D}(\hat{G}(Z,L),L)$ s.t. $c_n(\hat{G}(Z,L))=0$ via augmented Lagrangian $L_A(Z;\lambda,\mu) = f(Z) + \sum \lambda_n h_n(Z) + (\mu/2)\sum h_n(Z)^2$ with multiplier update $\lambda^{k+1}=\lambda^k+\mu^k h(Z^k)$ and $\mu^{k+1}=\alpha\mu^k$ ($\alpha=3$, $k_{\max}=5$). Inner optimizer: CMA-ES (population, gradient-free) outperforms Adam due to many local minima in $L_A$.

## Result
On PubLayNet beautification: CLG-LO+CMA-ES cuts Overlap from 22.80 (base) to 0.02 and Alignment from 0.19 to 0.14, with FID essentially unchanged (20.48 → 22.97). Adversarial-example collapse is prevented by clamping $f'(Z) = \max(f(Z)-f(Z_0), 0)$. Runtime ~1.45–1.96 s per layout with CMA-ES. Performance degrades as constraint count grows (no convergence guarantee on the non-convex neural objective).

## Why it matters here
General background; no direct arena tie. The augmented-Lagrangian + CMA-ES inner loop on a non-convex neural objective is a transferable pattern, and the explicit observation "population-based gradient-free beats Adam when $L_A$ has many local minima" is the kind of compute-router data point that maps onto optimizer choice for arena basin-hopping problems.

## Open questions / connections
- Does piecewise-convex approximation of $L_A$ or smarter $Z_0$ initialization improve convergence under many constraints?
- Can quality-diversity exploration of the latent manifold replace single-point optimization for diverse alternative solutions?
- Extends GAN-latent-editing line (Bau, Zhu, Menon/PULSE) from images to discrete-element layouts; same recipe might apply to other structured-output generators with constraints.

## Key terms
augmented Lagrangian, CMA-ES, latent space optimization, GAN inversion, Transformer GAN, constrained optimization, layout generation, Adam, Fréchet Inception Distance, penalty method, non-convex optimization, gradient-free optimization
