<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-foundation-models]
title: Cache-to-Cache: Direct Semantic Communication Between Large Language Models
authors: [Tianyu Fu, Zihan Min, Hanling Zhang, Jichao Yan, Guohao Dai, Wanli Ouyang, Yu Wang]
year: 2025
source_url: https://arxiv.org/abs/2510.03215
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Cache-to-Cache: Direct Semantic Communication Between Large Language Models

**Authors:** Tianyu Fu, Zihan Min, Hanling Zhang, Jichao Yan, Guohao Dai, Wanli Ouyang, Yu Wang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.03215

## One-line
Proposes C2C, a paradigm where two LLMs communicate by directly projecting and fusing their KV-caches via a learned neural fuser, bypassing token-by-token text exchange.

## Key claim
Direct KV-cache fusion between a Sharer and Receiver LLM yields +6.4–14.2% average accuracy over the Receiver alone, beats text-to-text (T2T) collaboration by ~3.1–5.4%, and delivers ~2.5× latency speedup; oracle experiments show enriching KV-cache semantics at fixed sequence length raises accuracy (58.4% → 62.3% on MMLU-Redux).

## Method
A trainable "cache fuser" concatenates the Receiver's per-layer KV-cache with the (token- and layer-aligned) Sharer's KV-cache, projects/fuses them, and reinjects via a residual connection gated per-layer by a Gumbel-sigmoid (annealed differentiable→binary). Token alignment is by decode-then-reencode across tokenizers; layer alignment is "terminal" (last layers paired first, recursing toward shallow). Both LLMs are frozen; only the fuser is trained with next-token-prediction loss (SFT-style) on OpenHermes-2.5 (~500k samples, ~6 GPU-hours to converge).

## Result
On Qwen3-0.6B Receiver across OpenBookQA, MMLU-Redux, ARC-C, C-Eval: C2C lifts accuracy from ~37% baseline to ~48% average across three Sharers (Qwen2.5-0.5B, Llama3.2-1B, Qwen3-4B-Base). T2T takes 1596ms vs C2C's 445ms on MMLU-Redux (Qwen2.5-0.5B Sharer) by replacing 80-token Sharer decode with 90ms parallel fusion. Effective-rank analysis confirms the fused KV-cache has higher information content than the Receiver's own. Extensions: one-Receiver-many-Sharer composition works zero-shot; agentic-flow variant (T-C2C) reaches 78.0% on GSM8K vs 41.2% single-model.

## Key terms
KV-cache fusion, multi-LLM communication, cache-to-cache, semantic transfer, learnable gating, Gumbel-sigmoid, token alignment, layer alignment, effective rank, Sharer-Receiver, mixture-of-agents, prompt caching, LLM collaboration, agentic flow
