---
type: source
kind: paper
title: Sparsity-Preserving Differentially Private Training of Large Embedding Models
authors: Badih Ghazi, Yangsibo Huang, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Amer Sinha, Chiyuan Zhang
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2311.08357
source_local: ../raw/2023-ghazi-sparsity-preserving-differentially-private-traini.pdf
topic: general-knowledge
cites:
---

# Sparsity-Preserving Differentially Private Training of Large Embedding Models

**Authors:** Badih Ghazi, Yangsibo Huang, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Amer Sinha, Chiyuan Zhang  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.08357

## One-line
Two DP-SGD variants (DP-FEST, DP-AdaFEST) that add Gaussian noise only to a selected subset of embedding-table rows, preserving gradient sparsity during private training of large embedding models.

## Key claim
On Criteo pCTR and GLUE (SST-2/QNLI/QQP) at $\varepsilon \in \{1, 3, 8\}$, the methods cut embedding-gradient size by $>10^6\times$ vs vanilla DP-SGD with comparable AUC/accuracy; wall-clock speedups reach $\sim 177\times$ at vocab $10^7$.

## Method
DP-FEST pre-selects top-$k$ buckets per categorical feature (public frequencies, or DP top-$k$ via Gumbel noise [DR21]) and adds Gaussian noise only inside that subset. DP-AdaFEST instead computes, each mini-batch, a clipped per-example "contribution map" $v_i$, releases a noisy aggregated map $V_t$ via a $\sigma_1$ Gaussian mechanism, thresholds at $\tau$, then applies a second $\sigma_2$ Gaussian only on surviving coordinates. Composition gives effective noise $\sigma = (\sigma_1^{-2}+\sigma_2^{-2})^{-1/2}$, accounted via Poisson-subsampled PLD [Goo20].

## Result
Pareto curves (Figs. 3, 4, 8) show DP-AdaFEST dominates DP-FEST and the prior DP-SGD-with-exponential-selection baseline [ZMH21] across all four datasets. A bias–variance lemma (Lemma 3.1) explains the gain: truncating fraction $\gamma$ to $h$ active coords trades bias $\gamma L$ against variance $h\sigma^2$, beating DP-SGD's $D\sigma^2$ whenever $\sqrt{T}(\sqrt{L^2(1+\gamma)^2+h\sigma^2}) + \gamma L < \sqrt{L^2+D\sigma^2}$. Streaming-period ablations on Criteo-1TB show AdaFEST tracks distribution shift where FEST cannot.

## Why it matters here
General background; no direct arena tie. The bias–variance framing for sparse-vs-dense gradient oracles is mildly transferable to coordinate-selection heuristics in high-dim multistart, but the DP machinery (Gaussian mechanism, privacy accounting, top-$k$ selection) is outside the optimization-for-math-problems scope of the einstein wiki.

## Open questions / connections
- Adaptive sparse masking + Gaussian composition — is the $(\sigma_1^{-2}+\sigma_2^{-2})^{-1/2}$ identity reusable as a tool for any two-stage noisy-screening optimizer (screen-then-polish)?
- DP top-$k$ via Gumbel-max [DR21] — related to Gumbel-trick discrete sampling that could appear in extremal-combinatorics search.
- Bias–variance trade-off Lemma 3.1 generalizes Hazan's projected-SGD bound; potentially relevant when truncating coordinates in basin-hopping style methods, but the regime (convex, Lipschitz) is far from arena problems.

## Key terms
differential privacy, DP-SGD, Gaussian mechanism, embedding models, gradient sparsity, Poisson subsampling, privacy loss distribution, top-$k$ selection, Gumbel noise, bias-variance trade-off, LoRA fine-tuning, Criteo pCTR
