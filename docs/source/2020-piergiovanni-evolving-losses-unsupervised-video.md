---
type: source
kind: paper
title: Evolving Losses for Unsupervised Video Representation Learning
authors: A. Piergiovanni, A. Angelova, M. Ryoo
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2002.12177
source_local: ../raw/2020-piergiovanni-evolving-losses-unsupervised-video.pdf
topic: general-knowledge
cites:
---

# Evolving Losses for Unsupervised Video Representation Learning

**Authors:** A. Piergiovanni, A. Angelova, M. Ryoo  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2002.12177

## One-line
Uses an evolutionary algorithm (CMA-ES) to automatically search the weights of a multi-task, multi-modal self-supervised loss for video representation learning, with a label-free fitness based on KL-divergence to a Zipf prior over k-means clusters.

## Key claim
A single RGB (2+1)D ResNet-50 trained on 2M unlabeled YouTube clips with the evolved loss reaches HMDB51 = 67.4% and UCF101 = 93.8% (fine-tuned), beating ImageNet pretraining and prior self-supervised methods, and nearly matching fully-supervised Kinetics pretraining (74.3 / 95.1); on Kinetics it matches the supervised baseline using ~50% of the labels (~120k of 225k samples).

## Method
Formulate unsupervised learning as a weighted sum $L = \sum_{m,t} \lambda_{m,t} L_{m,t} + \sum_d \lambda_d L_d$ over per-modality self-supervised losses (reconstruction, future-frame prediction, frame-shuffle/reverse classification, multi-modal contrastive embedding, audio/RGB alignment) plus $L_2$ distillation losses that infuse Flow/Audio/Grayscale into the RGB stream. The weight vector $\lambda \in [0,1]^N$ is searched by CMA-ES (250 rounds, faster than tournament selection at 2000 rounds). Fitness uses no labels: train a small proxy net, run k-means on embeddings, treat softmax distances to centroids as $p(c_i|x)$ with prior $q(c_i) = i^{-s}/H_{k,s}$ (Zipf), and minimize $KL(p\|q)$ — Spearman $\rho = 0.91$ with the weakly-supervised HMDB-accuracy fitness.

## Result
The CMA-ES-evolved loss achieves 67.4% HMDB (k-means 43.4, linear 64.5, fine-tune 67.4), versus 26.4 for a random-weight loss in the same search space and 26.4–32.5 for any single self-supervised task — showing the combinatorial weighting matters more than the task pool. Ablating distillation drops HMDB from 67.4 → 53.7 and UCF101 from 93.8 → 84.2. CMA-ES > Tournament (61.4) > Grid (57.3) > Random (52.4). The evolved weights kill RGB frame-shuffle and up-weight audio alignment + cross-modal distillation.

## Why it matters here
General background; no direct arena tie. The transferable idea is **CMA-ES on a continuous weight vector with a cheap, unsupervised fitness proxy** — relevant when the einstein agent needs to tune a composite objective (e.g., multi-term penalty in basin-hopping, weighted ensemble of evaluators) where the "true" metric is too expensive to evaluate per individual; the Zipf-KL trick illustrates how a distributional prior can stand in for the real objective.

## Open questions / connections
- Could the loss weights instead be learned by gradient descent (differentiable hyperparameter optimization)? Authors flag this as future work.
- Is Zipf-class-size a universal prior, or dataset-specific? AVA/Kinetics happen to be Zipf; the proxy may fail on uniformly-distributed-class corpora.
- Extends AutoML-for-architecture (NAS) and AutoAugment to the **loss-function-weighting** axis — analogous to weighted-sum LP/SDP relaxations where the constraint weights are tuned.

## Key terms
evolutionary search, CMA-ES, loss function evolution, multi-task learning, self-supervised learning, knowledge distillation, Zipf distribution, KL divergence, k-means clustering, AutoML, unsupervised fitness, video representation learning
