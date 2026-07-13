<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems
authors: [Hancheng Ye, Zhengqing Gao, Mingyuan Ma, Qinsi Wang, Yuzhe Fu, M. Chung, Yueqian Lin, Zhijian Liu, Jianyi Zhang, Danyang Zhuo, Yiran Chen]
year: 2025
source_url: https://arxiv.org/abs/2510.12872
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems

**Authors:** Hancheng Ye, Zhengqing Gao, Mingyuan Ma, Qinsi Wang, Yuzhe Fu, M. Chung, Yueqian Lin, Zhijian Liu, Jianyi Zhang, Danyang Zhuo, Yiran Chen  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.12872

## One-line
A training-free framework that reuses LLM KV-caches across multi-agent pipelines by predicting context-dependent cache offsets from a small online "anchor pool" of previously observed deviations, eliminating most prefill recomputation.

## Key claim
Cross-agent KV-cache reuse can be made prompt-adaptive without retraining by storing observed cache deviations under different prefixes as "anchors" and interpolating offsets at runtime — achieving >70% reuse, up to $7.8\times$ prefill speedup (TTFT $\sim$430ms → $\sim$55ms in a 5-agent / 1K-token / 512-prefix / 512-output setting), with <2.5% accuracy drop on GSM8K (95% reuse over 1,319 samples in a 4-agent system using Llama-3.1-8B-instruct).

## Method
Identifies the **offset-variance problem**: the same shared text produces different KV deviations under different prefixes (Fig. 1a), but two embedding-similar tokens exhibit nearly identical layer-wise offset distributions, with rotated-Key offsets much smaller than unrotated ones (Fig. 1b). KVCOMM maintains an online anchor pool of (token segment, measured KV offset under each prefix) pairs; at inference it performs **Anchor Matching** by token similarity (cosine / $\ell_2$-norm) then **Offset Approximation** via weighted interpolation of nearest anchors' stored deviations, applies the offset to RoPE-aligned Keys and directly to Values, and updates the pool online — unshareable segments become new anchors; least-matched anchors are periodically evicted.

## Result
Across RAG, math reasoning (GSM8K, MMLU), and collaborative coding (HumanEval) tasks with Llama-3.1-8B and Qwen-Coder-2.5-7B, KVCOMM yields $\sim 6.7\times$ average prefill speedup, >70% reuse rate, and near-baseline task accuracy. Ablations (Fig. A.12) show $\ell_2$-norm weighted aggregation achieves $\approx 0.92$ key / $0.95$ value cosine similarity vs ground-truth caches with offset error $<0.001$ at deep layers, dominating nearest-anchor and unaligned-reuse baselines (which fall below 0.8 similarity and accumulate error $>0.004$ in layers >25).

## Key terms
KV-cache reuse, multi-agent LLM systems, prefill acceleration, RoPE positional embedding, offset-variance, anchor pool, prompt-adaptive cache sharing, selective recomputation, KVCOMM, retrieval-augmented generation, Llama-3.1-8B, time-to-first-token
