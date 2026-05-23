---
type: source
kind: paper
title: A data-driven statistical model for predicting the critical temperature of a superconductor
authors: K. Hamidieh
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.10260
source_local: ../raw/2018-hamidieh-data-driven-statistical-model-predicting.pdf
topic: general-knowledge
cites:
---

# A data-driven statistical model for predicting the critical temperature of a superconductor

**Authors:** K. Hamidieh  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.10260

## One-line
Fits an XGBoost regression on 81 chemistry-derived features extracted from 21,263 superconductor formulas to predict the superconducting critical temperature $T_c$ from composition alone.

## Key claim
A tuned XGBoost model achieves out-of-sample RMSE $\approx 9.5$ K and $R^2 \approx 0.92$ on $T_c$ prediction, dominating a multiple-regression benchmark (RMSE $\approx 17.6$ K, $R^2 \approx 0.74$); thermal conductivity, atomic radius, valence, electron affinity, and atomic mass features dominate the gain ranking.

## Method
Each chemical formula $\prod_i e_i^{p_i}$ is turned into 10 summary statistics — mean, weighted mean, geometric mean, weighted geometric, entropy, weighted entropy, range, weighted range, standard deviation, weighted standard deviation — over each of 8 elemental properties, giving $8\times 10 + 1 = 81$ features. The model is gradient-boosted trees (XGBoost, Chen–Guestrin 2016) with $L_2$ leaf-weight penalty $\Omega(f) = \gamma T + \tfrac{1}{2}\lambda \sum_j w_j^2$, tuned over a 198-cell grid (learning rate $\eta$, column subsample, max depth, min child weight) via 25-fold $2/3$–$1/3$ train/test splits. Best config: $\eta=0.02$, depth $16$, min child $1$, colsample $0.5$, $374$ trees.

## Result
Out-of-sample $\text{RMSE}=9.5$ K, $R^2=0.92$ across the full $T_c$ range $[2\times 10^{-4},\,185]$ K. Cuprates (49.5% of data) have mean $T_c = 59.9 \pm 31.2$ K vs. non-cuprates $9.5 \pm 10.7$ K; iron-bearing materials have mean $T_c = 26.9$ K vs. non-iron $35.4$ K. Per-element variability scales with mean $T_c$ (higher-$T_c$ elements show larger SD). PCA was tried and abandoned — features carry an average $|\rho|=0.35$ and no low-dimensional projection captured the variance.

## Why it matters here
General background; no direct arena tie. The relevant transferable lesson for the agent is methodological — the *featurization-by-summary-statistics* template (mean/weighted-mean/entropy/range/std over per-element properties) is a generic recipe for turning a structured object (chemical formula, packing configuration, sequence) into a fixed-width feature vector for tree-based regression.

## Open questions / connections
- No pressure / crystal-structure feature → model fails on high-pressure superconductors (predicts H$_2$S badly; observed $T_c=203$ K under pressure).
- Compositional features alone cannot answer "is this a superconductor at all" — only $T_c$ given that it is one (selection bias from NIMS database).
- Cosine-similarity gating to training set as an out-of-distribution check is a reusable idea for the agent's own predictors.

## Key terms
XGBoost, gradient boosting, critical temperature, superconductor, feature engineering, weighted entropy, cuprate, NIMS database, regularized tree ensemble, Chen-Guestrin, multiple regression benchmark, feature importance gain
