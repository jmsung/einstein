---
type: source
kind: paper
title: Are we done with ImageNet?
authors: Lucas Beyer, Olivier J. H'enaff, Alexander Kolesnikov, Xiaohua Zhai, Aäron van den Oord
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.07159
source_local: ../raw/2020-beyer-done-imagenet.pdf
topic: general-knowledge
cites:
---

# Are we done with ImageNet?

**Authors:** Lucas Beyer, Olivier J. H'enaff, Alexander Kolesnikov, Xiaohua Zhai, Aäron van den Oord  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.07159

## One-line
Reassesses the ImageNet validation benchmark by collecting model-assisted multi-label human annotations ("ReaL"), revealing that recent classifier gains partly reflect overfitting to label idiosyncrasies rather than genuine generalization.

## Key claim
Top modern models (BiT-L, NoisyStudent, ensembles up to 91.20% ReaL accuracy) now exceed the original ILSVRC-2012 labels (90.02% ReaL) at predicting human preferences; the regression slope of ReaL vs. original accuracy drops from 0.86 (early models) to 0.51 (recent models, $p<0.001$).

## Method
Generate label proposals by pooling top-1 predictions plus high-logit/probability candidates from 19 diverse models, then prune to a 6-model subset achieving 97.1% recall at 28.3% precision. 5 raters per image answer yes/no/maybe on up to 8 candidate labels via a simultaneous-presentation UI; Dawid–Skene EM aggregates ratings into binary labels, with the ImageNet label as a virtual 6th rater for animal classes. The resulting ReaL metric counts top-1 prediction as correct if it lies in the multi-label set.

## Result
46,837 of 50,000 validation images get 57,553 ReaL labels (≈29% have multiple labels). Co-occurring-class analysis shows top models exceed an "unbiased oracle" that picks any valid label uniformly (e.g., desktop computer: 71.1% vs. 29.9% oracle), evidencing label-bias exploitation. Training fixes — sigmoid (non-exclusive) loss + BiT-L-cleaned training set (≈90% retained) over 900 epochs — yield ResNet-50 76.0→78.5% (ImageNet) and 82.5→84.1% (ReaL), reversing the long-schedule overfit.

## Why it matters here
General background; no direct arena tie. Tangentially relevant as a methodological case study in **benchmark-label drift and verifier-vs-evaluator mismatch** — parallels the einstein project's triple-verify rule and P9/P14/P17 verifier-tolerance findings, where local-evaluator divergence from the arena verifier mimics ImageNet's labeling-pipeline overfitting.

## Open questions / connections
- Extends Recht et al. 2019 (replication study) and Engstrom et al. 2020 (statistical-bias correction) by attacking labels rather than image-collection bias.
- How to evaluate fine-grained classes where non-expert raters mark "undecidable" — expert annotation needed for further progress on that axis.
- Whether sigmoid-loss + cleaned-label gains transfer to downstream tasks (detection, segmentation, transfer learning) or are ImageNet-internal.

## Key terms
ImageNet, ILSVRC-2012, ReaL labels, label noise, multi-label annotation, Dawid–Skene, crowdsourcing, benchmark overfitting, sigmoid cross-entropy, label cleaning, BiT-L, NoisyStudent, evaluation-metric drift
