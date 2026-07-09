---
type: source
kind: paper
title: "MolGAN: An implicit generative model for small molecular graphs"
authors: Nicola De Cao, Thomas Kipf
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1805.11973
source_local: ../raw/2018-cao-molgan-implicit-generative-model.pdf
topic: general-knowledge
cites:
---

# MolGAN: An implicit generative model for small molecular graphs

**Authors:** Nicola De Cao, Thomas Kipf  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1805.11973

## One-line
Adapts GANs to generate small molecular graphs directly (as adjacency tensor + node feature matrix), bypassing SMILES strings and likelihood-based graph-matching.

## Key claim
A one-shot graph-generating GAN combined with a DDPG-style RL reward network achieves ~99–100% chemically valid molecules on QM9 and beats SMILES-based ORGAN on druglikeness/synthesizability/solubility at ~5× faster training — at the cost of severe mode collapse (unique ≈ 2%).

## Method
Generator is an MLP from $z \sim \mathcal{N}(0,I)$ to a dense atom-type matrix $X \in \mathbb{R}^{N\times T}$ and bond-type adjacency tensor $A \in \mathbb{R}^{N\times N\times Y}$, discretized via categorical / Gumbel-softmax sampling. Discriminator and reward network are permutation-invariant Relational-GCN encoders followed by a node-aggregation readout (Li et al. 2016). Training combines improved-WGAN with gradient penalty and a DDPG-style differentiable reward $\hat{R}_\psi(G)$ trained against RDKit chemical scores; generator loss is $\lambda L_{\text{WGAN}} + (1-\lambda) L_{\text{RL}}$.

## Result
On QM9 ($N=9$, $T=5$, $Y=4$): validity ≈ 98–100%, novelty ≈ 94% (no-RL setting); with RL toward solubility, validity 99.8% and logP score 0.86–0.89 vs ORGAN's 0.55. Trades off severely against diversity: unique ≈ 2% (vs ORGAN's ~97%, GraphVAE's 24–76%). Training time ~0.6–2 h per objective vs ORGAN's 8–10 h.

## Why it matters here
General background; no direct arena tie. Off-domain (molecular ML, not extremal combinatorics / packing / autocorrelation); however, the permutation-invariant Relational-GCN readout and the "predict the whole discrete object at once + categorical sampling + gradient penalty" recipe are reusable patterns *if* a future arena approach ever frames a problem as graph generation (e.g., extremal-graph problems).

## Open questions / connections
- Mode collapse in GAN+RL: can a diversity-promoting reward or pretraining schedule recover the lost coverage?
- One-shot adjacency generation scales poorly past $N \sim 10$; sequential graph RNNs (GraphRNN, Li et al. 2018b) may extend the regime.
- Extends GAN/WGAN-GP and DDPG to discrete graph-structured outputs; connects to Relational-GCN (Schlichtkrull et al. 2017) and Gumbel-softmax (Jang et al. 2017) for differentiable categorical sampling.

## Key terms
MolGAN, GAN, WGAN-GP, Wasserstein distance, Relational-GCN, graph convolution, Gumbel-softmax, DDPG, deterministic policy gradient, molecular graph generation, QM9, mode collapse, permutation invariance
