---
type: source
kind: paper
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
authors: Songlin Yang, Jan Kautz, Ali Hatamizadeh
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2412.06464
source_local: ../raw/2024-yang-gated-delta-networks-improving.pdf
topic: general-knowledge
cites:
---

# Gated Delta Networks: Improving Mamba2 with Delta Rule

**Authors:** Songlin Yang, Jan Kautz, Ali Hatamizadeh  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2412.06464

## One-line
Combines a scalar decay gate with the delta update rule inside linear-attention RNNs, yielding a hardware-efficient sequence model that outperforms Mamba2 and DeltaNet on language and retrieval benchmarks.

## Key claim
The gated delta rule $S_t = S_{t-1}\bigl(\alpha_t(I - \beta_t k_t k_t^\top)\bigr) + \beta_t v_t k_t^\top$ unifies adaptive forgetting ($\alpha_t \to 0$ clears memory) with targeted key–value replacement ($\alpha_t \to 1$ reduces to pure delta rule), and admits a chunkwise-parallel matmul-heavy training algorithm via an extended WY representation.

## Method
Hidden state $S \in \mathbb{R}^{d_v \times d_k}$ is updated as a generalized Householder $(I - \beta_t k_t k_t^\top)$ scaled by data-dependent decay $\alpha_t \in (0,1)$. Training parallelism is achieved by extending the WY/UT-transform decomposition of DeltaNet (Yang et al. 2024b) with cumulative decay products $\gamma_j = \prod_{i \le j} \alpha_i$, giving $U_{[t]} = (I + \mathrm{strictLower}(\mathrm{diag}(\beta_{[t]})(\Gamma_{[t]} \odot K_{[t]}K_{[t]}^\top)))^{-1}\mathrm{diag}(\beta_{[t]})V_{[t]}$. Architecture stacks Gated-DeltaNet blocks (q/k with L2-norm + SiLU + short conv, $\alpha,\beta$ linear) with SwiGLU MLPs; hybrid H1/H2 variants interleave with sliding-window attention and Mamba2.

## Result
At 1.3B params / 100B FineWeb-Edu tokens, Gated DeltaNet beats Mamba2 and DeltaNet on perplexity (Wiki 16.42 vs 16.56, LAMBADA 12.17 vs 12.56), commonsense reasoning average (55.32 vs 54.89/52.14), and synthetic retrieval (S-NIAH-2 at 8K: 29.6 vs Mamba2's 17.0 and DeltaNet's 14.4). Online-learning framework view: gated delta rule = test-time SGD on $\tfrac12\|S_t k_t - v_t\|^2$ with adaptive learning rate $\beta_t$ and weight decay $\alpha_t$. Hybrid Mamba2 + Gated DeltaNet + SWA gives the best ablation result.

## Why it matters here
General background; no direct arena tie. Relevant only as deep-learning architecture context (test-time SGD framing, weight-decay-as-gating) — not connected to sphere packing, autocorrelation, kissing numbers, or any of the 23 Einstein Arena problems.

## Open questions / connections
- Extends DeltaNet (Schlag et al. 2021, Yang et al. 2024b) and Mamba2/SSD (Dao & Gu 2024) by composing their state-update structures.
- Connection to Longhorn (Liu et al. 2024) and Titans (Behrouz et al. 2024): all frame recurrent updates as closed-form online-learning solutions with regularization.
- Open: whether matrix-valued $\alpha_t$ (cf. GLA, Yang et al. 2024a) combined with delta rule preserves chunkwise efficiency; state-tracking expressivity with $\beta_t \in (0,2)$ negative-eigenvalue regime (Grazzi 2024, Siems 2025).

## Key terms
gated delta rule, DeltaNet, Mamba2, linear attention, state space duality, WY representation, Householder transformation, chunkwise parallel training, fast weight programming, test-time SGD, online learning, sliding window attention, hybrid RNN-transformer
