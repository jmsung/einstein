---
type: source
kind: paper
title: Denoising Diffusion Probabilistic Models
authors: Jonathan Ho, Ajay Jain, P. Abbeel
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.11239
source_local: ../raw/2020-ho-denoising-diffusion-probabilistic-models.pdf
topic: general-knowledge
cites:
---

# Denoising Diffusion Probabilistic Models

**Authors:** Jonathan Ho, Ajay Jain, P. Abbeel  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.11239

## One-line
Trains a generative model that learns to reverse a fixed Gaussian noising process, producing high-quality images via a denoising objective equivalent to score matching at multiple noise scales.

## Key claim
A specific $\epsilon$-prediction parameterization of the reverse-process mean, trained on the simplified unweighted MSE loss $L_\text{simple} = \mathbb{E}_{t,x_0,\epsilon}\|\epsilon - \epsilon_\theta(\sqrt{\bar\alpha_t}x_0 + \sqrt{1-\bar\alpha_t}\epsilon, t)\|^2$, yields FID 3.17 and Inception 9.46 on unconditional CIFAR10 (SOTA at the time among unconditional models).

## Method
Fix a forward Markov chain $q(x_t|x_{t-1}) = \mathcal{N}(\sqrt{1-\beta_t}x_{t-1}, \beta_t I)$ with linear $\beta_t$ schedule from $10^{-4}$ to $0.02$, $T=1000$. Learn reverse transitions $p_\theta(x_{t-1}|x_t) = \mathcal{N}(\mu_\theta(x_t,t), \sigma_t^2 I)$ via the variational bound, but reparameterize so the network predicts the noise $\epsilon$ rather than the mean $\tilde\mu_t$ or $x_0$. Drop the per-$t$ weight $\beta_t^2/(2\sigma_t^2\alpha_t(1-\bar\alpha_t))$ from the loss — this down-weights small-$t$ terms (easy denoising) and emphasizes large-$t$ terms, improving samples at the cost of likelihood.

## Result
Establishes a formal equivalence: variational training of the reverse Markov chain with $\epsilon$-parameterization = denoising score matching across noise levels + annealed Langevin sampling. CIFAR10 FID 3.17 (vs StyleGAN2+ADA 2.67; better than BigGAN's 14.73 unconditional best of class). LSUN 256² FID: Bedroom 4.90, Church 7.89, Cat 19.75. Models have weak NLL (~3.70 bits/dim) but excellent lossy-compression behavior — >50% of codelength describes imperceptible detail.

## Why it matters here
General background; no direct arena tie. None of the 23 arena problems (sphere packing, autocorrelation, kissing, sieves, extremal graphs) involve generative modeling or image synthesis. Possible loose conceptual analogies (annealed Langevin ↔ parallel tempering; multi-scale noise schedule ↔ continuation methods) but the wiki already has stronger, more direct sources for those techniques.

## Open questions / connections
- Extends Sohl-Dickstein et al. 2015 (nonequilibrium thermodynamics formulation) and Song-Ermon NCSN — fuses the variational and score-matching views.
- Leaves open: better likelihoods (later addressed by improved-DDPM / continuous-time / Karras schedules), faster sampling than $T=1000$ NFEs, learned variances.
- Conceptual-compression and progressive-decoding view connects to autoregressive models with generalized bit orderings.

## Key terms
diffusion probabilistic model, DDPM, denoising score matching, annealed Langevin dynamics, variational bound, reverse Markov chain, epsilon-prediction parameterization, Gaussian noise schedule, U-Net, generative modeling, Sohl-Dickstein, Song-Ermon
