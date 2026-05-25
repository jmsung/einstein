---
type: source
kind: paper
title: Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation
authors: Sangmin Bae, Yujin Kim, Reza Bayat, Sungnyun Kim, Jiyoun Ha, Tal Schuster, Adam Fisch, Hrayr Harutyunyan, Ziwei Ji, Aaron C. Courville, SeYoung Yun
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.10524
source_local: ../raw/2025-bae-mixture-of-recursions-learning-dynamic-recursive.pdf
topic: general-knowledge
cites:
---

# Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation

**Authors:** Sangmin Bae, Yujin Kim, Reza Bayat, Sungnyun Kim, Jiyoun Ha, Tal Schuster, Adam Fisch, Hrayr Harutyunyan, Ziwei Ji, Aaron C. Courville, SeYoung Yun  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.10524

## One-line
A Transformer architecture that ties weights across a recursion block and uses lightweight routers to assign each token a per-token recursion depth, unifying parameter sharing with adaptive computation.

## Key claim
At equal training FLOPs ($16.5\times 10^{18}$), MoR with expert-choice routing and $N_r=2$ beats a 315M-parameter vanilla Transformer on validation NLL ($2.7511$ vs $2.7824$) and average few-shot accuracy ($43.1\%$ vs $42.3\%$) while using ~50% fewer unique parameters; recursion-wise KV caching cuts KV memory/IO to $(N_r+1)/2N_r$ and per-layer attention FLOPs to $(k/N_{\text{ctx}})^2$ of the vanilla cost.

## Method
A Recursive Transformer shares one block $\Phi'$ across $N_r$ recursion steps (best variant: "Middle-Cycle" — distinct first/last layers, shared middle). At each step a router computes $g_t^r = \mathcal{G}(\theta_r^\top \mathcal{H}_t^r)$ and either (a) **expert-choice**: top-$k_r$ tokens with $k_r$ scheduled $N_r/N_r,\dots,1/N_r$ continue (hierarchical filtering enforces causality), or (b) **token-choice**: a single up-front $\arg\max_j g_t^j$ commits each token to $i$ recursions. Two KV strategies: recursion-wise caching (only active tokens stored at each depth, restricts attention block-locally) and recursive sharing (cache only at recursion 1, reuse keys/values at all depths).

## Result
- IsoFLOP scaling 135M–1.7B: MoR ($N_r=3$) matches/exceeds vanilla above 360M params despite ~1/3 unique parameters; underperforms only at 135M (capacity bottleneck).
- Fixed-token (20B) regime: MoR $N_r=2$ achieves lower NLL with 25% fewer FLOPs, 19% less training time, 25% less peak memory than vanilla.
- Expert-choice ($42.6\%$) > token-choice ($40.0\%$) at $N_r=3$; auxiliary-loss + sigmoid + linear router gives best load balancing (dead-token ratio 0.1%, sampling accuracy 99.2%).
- KV cache sharing trades small NLL hit ($\Delta\approx 0.02$) for $1/N_r$ memory; continuous depth-wise batching gives further inference throughput gains.

## Why it matters here
General background; no direct arena tie. Relevant only as architectural context for the agent itself (adaptive per-token compute, parameter sharing) — not a math-content paper informing sphere packing, autocorrelation, or any Einstein Arena problem family.

## Open questions / connections
- Can expert-choice causality leakage be eliminated without auxiliary routers — e.g., a non-causal-to-causal distillation step?
- Token-choice load balancing remains poor under heterogeneous experts (different recursion depths); better balancing losses for depth-heterogeneous MoE remain open.
- Relaxation of KV sharing (LoRA, DoRA, adaptation prompts, recursion-output encodings) gave no substantial gains — what structural relaxation would actually help?
- Extends prior recursive Transformers (Bae 2024, Dehghani 2018, Geiping 2025) and MoD (Raposo 2024) by unifying their axes in one pretraining recipe.

## Key terms
Mixture-of-Recursions, Recursive Transformer, parameter sharing, layer tying, adaptive computation, token-level routing, expert-choice routing, token-choice routing, Mixture-of-Depths, KV cache sharing, continuous depth-wise batching, Middle-Cycle, early-exit, load balancing, latent reasoning
