---
type: source
kind: paper
title: Interpretable bilinear attention network with domain adaptation improves drug–target prediction
authors: Peizhen Bai, Filip Miljkovi'c, Bino John, Haiping Lu
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2208.02194
source_local: ../raw/2022-bai-interpretable-bilinear-attention-network.pdf
topic: general-knowledge
cites:
---

# Interpretable bilinear attention network with domain adaptation improves drug–target prediction

**Authors:** Peizhen Bai, Filip Miljkovi'c, Bino John, Haiping Lu  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2208.02194

## One-line
A deep learning framework (DrugBAN) that predicts drug–target interactions using a bilinear attention network over molecular graphs and protein sequences, with conditional adversarial domain adaptation for cross-distribution generalization.

## Key claim
DrugBAN achieves state-of-the-art AUROC on three DTI benchmarks (BindingDB 0.960, BioSNAP 0.903, Human in-domain) and, with CDAN, improves cross-domain AUROC by 2.9–7.4% over MolTrans on clustering-based splits; bilinear attention maps provide substructure-level interpretability validated against three PDB co-crystal structures (6QL2, 5W8L, 4N6H).

## Method
GCN encodes 2D drug molecular graphs; 1D-CNN encodes protein sequences (23 amino-acid tokens). A low-rank bilinear attention module computes a pairwise interaction matrix $I = \mathrm{softmax}((H_d^\top U)(V^\top H_p))$ between drug-atom and protein-subsequence representations, then bilinear pooling yields a joint vector decoded by an FC sigmoid classifier. For cross-domain transfer, Conditional Adversarial Domain Adaptation (CDAN) embeds the joint representation and softmax logits via outer-product multilinear map into a discriminator trained adversarially against the feature extractor.

## Result
On in-domain random splits, DrugBAN beats SVM/RF/DeepConv-DTI/GraphDTA/MolTrans across AUROC, AUPRC, accuracy. Under clustering-based cross-domain splits (single-linkage on ECFP4 Jaccard + PSC cosine, threshold 0.5), DrugBAN+CDAN reaches 0.604 AUROC on BindingDB and 0.684 on BioSNAP, beating vanilla DrugBAN by ~4.6% AUROC and 16.9% AUPRC on BioSNAP. Ablations show bilinear attention > one-side attention > linear concatenation, and CDAN > DANN. Top-20% attention-weighted atoms correctly highlight sulfonamide / hydroxyl / biphenyl binding groups corroborated by X-ray structures.

## Why it matters here
General background; no direct arena tie. The bilinear low-rank pooling trick ($H_d^\top U \odot V^\top H_p$ → sum-pool) is a parameter-efficient way to model pairwise local interactions and could be a reference architecture if a future arena problem requires substructure-level matching, but the math problems in this repo (sphere packing, autocorrelation, kissing numbers) are not DTI-shaped.

## Open questions / connections
- Bilinear pooling as a low-rank pairwise-interaction primitive — relation to tensor decomposition methods used elsewhere.
- Cross-domain generalization via adversarial alignment — analogous to distribution-shift problems but not invoked in Einstein Arena scoring.
- Interpretability via attention weights — weaker on 1D protein sequences than on 2D drug graphs, hinting that representation geometry constrains interpretability.

## Key terms
drug-target interaction, bilinear attention network, conditional domain adaptation, CDAN, graph convolutional network, low-rank bilinear pooling, ECFP4 fingerprint, pseudo amino acid composition, adversarial domain adaptation, molecular graph encoding, DrugBAN, cross-domain generalization
