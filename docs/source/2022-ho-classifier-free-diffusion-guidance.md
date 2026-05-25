---
type: source
kind: paper
title: Classifier-Free Diffusion Guidance
authors: Jonathan Ho
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2207.12598
source_local: ../raw/2022-ho-classifier-free-diffusion-guidance.pdf
topic: general-knowledge
cites:
---

# Classifier-Free Diffusion Guidance

**Authors:** Jonathan Ho  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2207.12598

## One-line
A method to trade off sample fidelity vs diversity in conditional diffusion models by jointly training conditional and unconditional score networks and combining their score estimates at sampling time — no auxiliary classifier required.

## Key claim
The score combination $\tilde{\epsilon}_\theta(z_\lambda, c) = (1+w)\epsilon_\theta(z_\lambda, c) - w\epsilon_\theta(z_\lambda)$ achieves the same FID/IS tradeoff as classifier guidance while eliminating the auxiliary classifier. On 128×128 ImageNet, $w=0.3$ beats classifier-guided ADM-G on FID (2.43 vs 2.97); $w=4.0$ beats BigGAN-deep on both FID and IS.

## Method
Joint training: with probability $p_\text{uncond}$ (best at 0.1–0.2), replace the class label $c$ with a null token $\emptyset$ so a single network learns both $\epsilon_\theta(z_\lambda, c)$ and $\epsilon_\theta(z_\lambda) = \epsilon_\theta(z_\lambda, \emptyset)$. At sampling, replace the score with the linear combination above; this is motivated by an *implicit classifier* $p^i(c|z_\lambda) \propto p(z_\lambda|c)/p(z_\lambda)$ whose gradient would be $\epsilon^*(z_\lambda,c) - \epsilon^*(z_\lambda)$, but since $\epsilon_\theta$ is an unconstrained NN, the combined field is generally non-conservative — not the gradient of any actual classifier.

## Result
Sweeping $w \in [0, 4]$ traces a clean FID/IS Pareto frontier: small $w$ minimizes FID, large $w$ maximizes IS. On 64×64 ImageNet, $w=0.1$ gives FID 1.55; on 128×128, $w=0.3$ gives FID 2.43 (state of the art at publication). $p_\text{uncond}=0.5$ consistently underperforms 0.1/0.2 — only a small fraction of capacity needs to be spent on the unconditional task. Sampling cost is 2× per step (two NN passes).

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are discrete math/optimization (sphere packing, autocorrelation, kissing numbers), not image synthesis — diffusion guidance does not inform any current optimizer or wiki concept. Possible distant analogy: tempering / annealing schedules trading exploration vs exploitation, but the connection is weak.

## Open questions / connections
- Can the "negative score term" idea (subtracting unconditional likelihood) be applied outside generative modeling — e.g., in importance-weighted Monte Carlo or rare-event sampling?
- Sampling-speed mitigation via late-injection of conditioning is left for future work.
- Extends Dhariwal & Nichol (2021) classifier guidance; relates to BigGAN truncation (Brock et al. 2019) and Glow low-temperature sampling (Kingma & Dhariwal 2018).

## Key terms
classifier-free guidance, diffusion model, score matching, denoising score matching, conditional generation, FID, Inception score, truncation tradeoff, implicit classifier, Bayes' rule classifier, unconditional score, ImageNet generation
