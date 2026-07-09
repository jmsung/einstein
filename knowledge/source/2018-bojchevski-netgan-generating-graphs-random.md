---
type: source
kind: paper
title: "NetGAN: Generating Graphs via Random Walks"
authors: Aleksandar Bojchevski, Oleksandr Shchur, Daniel Zügner, Stephan Günnemann
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.00816
source_local: ../raw/2018-bojchevski-netgan-generating-graphs-random.pdf
topic: general-knowledge
cites:
---

# NetGAN: Generating Graphs via Random Walks

**Authors:** Aleksandar Bojchevski, Oleksandr Shchur, Daniel Zügner, Stephan Günnemann  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.00816

## One-line
A GAN that learns to generate realistic graphs by modeling the distribution of biased random walks over a single input network, rather than the adjacency matrix directly.

## Key claim
An implicit generative model trained only on random walks reproduces global graph statistics (degree distribution, assortativity, triangle count, clustering, community structure) of real citation networks better than prescribed baselines (configuration model, DC-SBM, ERGM, BTER, VGAE), while simultaneously achieving competitive/SOTA link prediction (e.g. AUC 96.30 / AP 96.89 on CITESEER, AUC 95.51 on POLBLOGS) — without being trained for that task.

## Method
Generator $G$ is an LSTM whose latent code $z \sim \mathcal{N}(0,I_d)$ initializes $(C_0,h_0)$; at each step it emits logits $p_t$ (via down/up projection $W_{\text{down}}\in\mathbb{R}^{N\times H}$, $W_{\text{up}}\in\mathbb{R}^{H\times N}$) and samples the next node $v_t \sim \text{Cat}(\sigma(p_t))$ using the Straight-Through Gumbel estimator $v_t^* = \sigma((p_t+g)/\tau)$ to backprop through the categorical. Discriminator is another LSTM scoring random walks; training uses Wasserstein GAN with gradient penalty (Gulrajani et al. 2017), random walks of length $T=16$ sampled by node2vec-style 2nd-order biased walks. Adjacency matrix is assembled from a symmetrized transition-count matrix $S$ by sampling edges with $p_{ij} \propto s_{ij}$ until target edge count is reached; two early-stopping criteria (VAL: validation link-prediction; EO: target edge-overlap) let the user dial generalization vs replication.

## Result
On CORA-ML (2,810 nodes, 7,981 edges) NetGAN-EO at 52% edge overlap matches input max-degree 233 vs 240, assortativity $-0.066$ vs $-0.075$, triangle count 1,588, power-law exponent 1.793 vs 1.860, characteristic path length 5.20 vs 5.61 — best average rank across 8 statistics among 6 baselines. Link prediction with 100M sampled walks gives AUC/AP up to 96.30/96.89 (CITESEER) and 95.51/94.83 (POLBLOGS). On a DC-SBM synthetic with $N=300$ and 3 communities, NetGAN recovers ground-truth edge probabilities with Spearman rank correlation 0.998 at EO=0.42, indicating it learns the generative process rather than memorizing edges.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are continuous-geometry and combinatorial-extremal (sphere packing, kissing numbers, autocorrelation, Sidon sets) — graph-generation GANs are off-topic for the optimizer stack. Tangential interest: random-walk-as-distribution and Gumbel-Straight-Through could conceivably inform sampling/exploration in discrete combinatorial problems, but no current arena problem calls for either.

## Open questions / connections
- Does the random-walk distribution view generalize to other discrete combinatorial structures (Sidon sets, contact graphs of sphere packings)?
- Gumbel-Straight-Through gradient flow through arg-max sampling — applicable to discrete-geometry basin sampling where current optimizers rely on continuous relaxations?
- Edge-overlap (EO) early-stopping as a generalization-vs-memorization knob — analogue for solution-space exploration in continuous optimizers?
- Extends prescribed models (configuration model, DC-SBM, ERGM, BTER) and edge-level deep methods (node2vec, VGAE, GraphGAN).

## Key terms
NetGAN, graph generation, random walks, Wasserstein GAN, gradient penalty, LSTM, Gumbel-Softmax, Straight-Through estimator, node2vec biased walks, link prediction, stochastic blockmodel, configuration model, implicit generative model, edge overlap
