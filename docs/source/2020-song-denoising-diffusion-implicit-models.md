---
type: source
kind: paper
title: Denoising Diffusion Implicit Models
authors: Jiaming Song, Chenlin Meng, Stefano Ermon
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.02502
source_local: ../raw/2020-song-denoising-diffusion-implicit-models.pdf
topic: general-knowledge
cites:
---

# Denoising Diffusion Implicit Models

**Authors:** Jiaming Song, Chenlin Meng, Stefano Ermon  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.02502

## One-line
Generalizes denoising diffusion models (DDPMs) to a family of non-Markovian forward processes whose deterministic limit (DDIM) yields an implicit generative model usable for 10–50× faster sampling without retraining.

## Key claim
The DDPM training objective $L_\gamma$ depends only on the marginals $q(x_t|x_0)$, so a whole family of non-Markovian inference processes indexed by $\sigma \in \mathbb{R}^T_{\ge 0}$ share the same surrogate loss; the deterministic $\sigma = 0$ choice (DDIM) produces samples in 20–100 steps matching the FID of 1000-step DDPM (CIFAR10 FID 4.16 at 100 steps vs 4.04 at 1000; CelebA FID 6.53 at 100 vs 3.51 at 1000).

## Method
Replace the Markov forward chain with $q_\sigma(x_{t-1}|x_t,x_0) = \mathcal{N}(\sqrt{\alpha_{t-1}}x_0 + \sqrt{1-\alpha_{t-1}-\sigma_t^2}\cdot \tfrac{x_t-\sqrt{\alpha_t}x_0}{\sqrt{1-\alpha_t}}, \sigma_t^2 I)$, designed via Bayes' rule (Lemma 1) so the marginals $q_\sigma(x_t|x_0) = \mathcal{N}(\sqrt{\alpha_t}x_0,(1-\alpha_t)I)$ match DDPM exactly. Theorem 1 shows $J_\sigma = L_\gamma + C$, so a pretrained DDPM noise-predictor $\epsilon_\theta^{(t)}$ is reusable as-is. Sampling on any sub-sequence $\tau \subset [1,T]$ uses the update $x_{t-1} = \sqrt{\alpha_{t-1}}\,\hat{x}_0 + \sqrt{1-\alpha_{t-1}-\sigma_t^2}\,\epsilon_\theta + \sigma_t \epsilon$; in the $\sigma=0$ limit this is the Euler discretization of the ODE $d\bar{x} = \epsilon_\theta(\bar{x}/\sqrt{\sigma^2+1})\,d\sigma$, equivalent (Prop. 1) to Song et al.'s variance-exploding probability-flow ODE.

## Result
On CIFAR10 ($32\times 32$), DDIM ($\eta=0$) reaches FID 4.67 in 50 steps and 4.16 in 100 vs DDPM's 8.01 / 5.78; on CelebA ($64\times64$), 9.17 / 6.53 vs 18.48 / 13.93. The deterministic map $x_T \mapsto x_0$ gives near-perfect reconstruction (per-dim MSE $\le 10^{-4}$ at $S\ge 100$ on CIFAR10), enables semantically meaningful spherical-linear interpolation in latent space, and exhibits "consistency": fixing $x_T$ produces samples with the same high-level features across trajectory lengths.

## Why it matters here
General background; no direct arena tie. The relevant mathematical content for this project is the marginal-preserving reparameterization trick (any joint with matching marginals shares the variational objective up to a known reweighting) — a clean instance of "different processes, same target distribution" which mirrors how distinct optimizer dynamics on the same energy landscape can reach the same basin at different cost. The ODE reinterpretation (deterministic flow as Euler integration over $d\sigma$ rather than $dt$) is a worked example of choosing the right integration variable for a one-parameter family — analogous to parameterization-selection issues that appear in continuous-relaxation approaches to combinatorial problems.

## Open questions / connections
- Multistep ODE integrators (Adams–Bashforth) for fewer-step sampling — does higher-order integration further reduce discretization error?
- Non-Gaussian forward processes (Gaussian is the only stable distribution with finite variance) — Appendix A sketches a multinomial categorical version; what other combinatorial structures admit such forward kernels?
- Extends Sohl-Dickstein 2015 / Ho 2020 / Song-Ermon 2019 (NCSN); concurrent with Song et al. 2020 (score SDE) which DDIM is shown equivalent to in the VE limit.

## Key terms
denoising diffusion, DDIM, DDPM, non-Markovian forward process, variational lower bound, score matching, neural ODE, probability flow ODE, variance-exploding SDE, implicit generative model, Euler integration, spherical linear interpolation, marginal-preserving reparameterization, Song, Ermon
