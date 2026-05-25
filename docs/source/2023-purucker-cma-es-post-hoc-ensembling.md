---
type: source
kind: paper
title: "CMA-ES for Post Hoc Ensembling in AutoML: A Great Success and Salvageable Failure"
authors: Lennart Purucker, Joeran Beel
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2307.00286
source_local: ../raw/2023-purucker-cma-es-post-hoc-ensembling.pdf
topic: general-knowledge
cites:
---

# CMA-ES for Post Hoc Ensembling in AutoML: A Great Success and Salvageable Failure

**Authors:** Lennart Purucker, Joeran Beel  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2307.00286

## One-line
Compares CMA-ES against greedy ensemble selection (GES) for post hoc model ensembling in AutoML, finds CMA-ES overfits on ROC AUC but not balanced accuracy, and proposes a GES-inspired weight-normalization fix.

## Key claim
On 71 AutoML-Benchmark classification datasets with AutoGluon base models, CMA-ES statistically significantly beats GES on balanced accuracy but overfits and loses on ROC AUC; a proposed normalization scheme (CMA-ES-ExplicitGES) — softmax + trim weights below $0.5/N_{hyp}$ + round to nearest fraction with denominator $N_{hyp}=50$ + repair so $\sum r_j = N_{hyp}$ — restores parity/superiority on ROC AUC while keeping ensembles sparse (~6.3 vs GES ~5.8 vs unnormalized CMA-ES ~12.9 base models).

## Method
CMA-ES (pycma defaults, $\sigma_0 = 0.2$, $x_0$ = one-hot on the single best model, $m \cdot 50$ function evaluations) searches a weight vector $W = (w_1,\dots,w_m)$ for a $W$-weighted arithmetic mean of base-model probabilities, minimizing a user loss. The salvage construction enforces two GES properties — *pseudo-discreteness* ($W \in \{0, 1/N, \dots, 1\}^m$ with $\sum w_i = 1$) and *sparseness* — as a non-linear normalization applied **before** aggregation (and hence before loss evaluation), rather than as constrained optimization (which caused rejection-sampling failures). Evaluation uses Friedman + Nemenyi post-hoc ($\alpha = 0.05$) with critical-difference plots and a PAR10-style normalized improvement.

## Result
For balanced accuracy CMA-ES dominates (mean rank 1.12 binary / 1.25 multi-class vs GES 2.44 / 2.33); for ROC AUC unnormalized CMA-ES drops from validation rank ~1.0 to test ranks 1.83 (binary) / 2.12 (multi-class), losing to GES. CMA-ES-ExplicitGES recovers ROC AUC performance (rank 1.78 / 1.57 vs GES 2.00 / 1.73) and ties or beats GES across both metrics. Ablation: softmax-only and implicit-GES variants partly close the gap but only the variant satisfying *both* pseudo-discreteness and sparseness is significantly different from raw CMA-ES on multi-class.

## Why it matters here
General background; no direct arena tie. The Einstein Arena problems are continuous math-optimization (sphere packing, autocorrelation, kissing) where CMA-ES is used for weight/parameter search in float64 — not for post hoc model ensembling. The transferable lesson is narrow: **CMA-ES on a smooth objective can overfit a validation surrogate when the search space is unconstrained and dense**, and projecting onto a sparse/quantized manifold *during loss evaluation* (rather than via hard constraints) can act as effective regularization without breaking the CMA-ES update.

## Open questions / connections
- Does the "normalize-before-eval" trick generalize to other gradient-free optimizers (e.g., basin-hopping, differential evolution) when their iterates overfit a validation/proxy surrogate?
- How does this compare to repair-and-inject or penalization constraint-handling for CMA-ES (Hansen 2016; Biedrzycki 2020)?
- Connection to Mallows' Model Averaging (Hansen 2007; Le & Clarke 2022) — does GES inherit MMA's asymptotic guarantees when $L$ is squared error?

## Key terms
CMA-ES, greedy ensemble selection, post hoc ensembling, AutoML, weight normalization, overfitting, ROC AUC, balanced accuracy, sparseness, pseudo-discrete weights, Mallows model averaging, gradient-free optimization
