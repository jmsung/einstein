---
type: source
kind: paper
title: Evolving mario levels in the latent space of a deep convolutional generative adversarial network
authors: Vanessa Volz, Jacob Schrum, Jialin Liu, S. Lucas, Adam M. Smith, S. Risi
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1805.00728
source_local: ../raw/2018-volz-evolving-mario-levels-latent.pdf
topic: general-knowledge
cites:
---

# Evolving mario levels in the latent space of a deep convolutional generative adversarial network

**Authors:** Vanessa Volz, Jacob Schrum, Jialin Liu, S. Lucas, Adam M. Smith, S. Risi  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1805.00728

## One-line
Trains a DCGAN on Super Mario Bros levels, then uses CMA-ES to search the GAN's latent space for levels meeting specified fitness criteria (tile distributions, agent playability, jump counts).

## Key claim
Latent Variable Evolution (LVE) — evolving inputs to a trained generator with CMA-ES — can produce playable, controllable Mario levels even when the GAN is trained on a single source level (173 sliding-window samples), optimizing both static tile-distribution targets and agent-based difficulty proxies.

## Method
DCGAN (WGAN training, RMSprop, 5000 iterations) with 32-dim latent vector, trained on 10-channel one-hot tile representations of $28 \times 14$ windows from one VGLC Mario level. CMA-ES (population $\lambda=14$, up to 1000 evaluations) searches latent space using fitness functions: (1) squared deviation from target ground-tile fraction $F_{\text{ground}} = (g-t)^2$; (2) agent-based fitness using Robin Baumgarten's A* agent to measure playability fraction $p$ and jump-action counts, averaged over 10 simulations to handle noise.

## Result
Representation-based: hits target ground-tile fractions accurately across $[0,1]$ except near 20%. Combined ground + enemy fitness produces multi-section levels of increasing difficulty. Agent-based: $F_1$ (maximize jumps) and $F_2$ (minimize jumps subject to playability) both produce playable levels matching their objective; average fitness decreases monotonically with iteration, though noisy individuals persist late. Some artifacts: broken pipe structures from discrete-tile output of continuous-valued GAN.

## Why it matters here
General background; no direct arena tie. The technique (CMA-ES navigating a learned generative latent space toward a fitness target) is methodologically analogous to optimizing configurations via a learned embedding rather than raw coordinates, but the problems are discrete level layouts rather than continuous geometric optimization, and no transferable bound or analytical insight applies to sphere packing, autocorrelation, or kissing problems.

## Open questions / connections
- Latent-space CMA-ES landscape: low-jump and unplayable levels cluster together — does the latent geometry create deceptive basins for noisy fitness?
- Could LSTM/Gumbel-Softmax-style discrete conditioning fix the broken-tile artifact (cited Kusner & Hernández-Lobato 2016)?
- Multi-objective LVE (NSGA-II on latent vectors) as a way to balance competing level-quality criteria — applicable to any indirect-encoding evolutionary search.

## Key terms
GAN, DCGAN, WGAN, latent variable evolution, CMA-ES, procedural content generation, PCGML, Mario, A* agent, fitness landscape, one-hot tile encoding, indirect encoding, genotype-to-phenotype mapping, multi-objective optimization
