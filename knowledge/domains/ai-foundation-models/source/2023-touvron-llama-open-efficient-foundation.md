---
type: source
kind: paper
title: "LLaMA: Open and Efficient Foundation Language Models"
authors: Hugo Touvron, Thibaut Lavril, Gautier Izacard, X. Martinet, M. Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aur'elien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.13971
source_local: ../raw/2023-touvron-llama-open-efficient-foundation.pdf
topic: general-knowledge
cites:
---

# LLaMA: Open and Efficient Foundation Language Models

**Authors:** Hugo Touvron, Thibaut Lavril, Gautier Izacard, X. Martinet, M. Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aur'elien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.13971

## One-line
Trains a family of 7B–65B-parameter decoder-only transformer language models on 1–1.4T tokens of exclusively public text, matching or beating much larger proprietary LLMs.

## Key claim
LLaMA-13B outperforms GPT-3 (175B) on most benchmarks despite being ~10× smaller, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B — all trained on publicly available data only.

## Method
Standard decoder-only transformer with three architectural tweaks: pre-normalization with RMSNorm (Zhang & Sennrich 2019), SwiGLU activations at dimension $\tfrac{2}{3} \cdot 4d$ (Shazeer 2020), and rotary positional embeddings RoPE (Su et al. 2021). AdamW ($\beta_1{=}0.9, \beta_2{=}0.95$), cosine LR schedule to 10% of peak, weight decay 0.1, grad clip 1.0, batch size 4M tokens; efficient causal attention via xformers (no stored weights / masked scores), manual backward for activation checkpointing, model+sequence parallelism. 65B model runs at ~380 tok/sec/GPU on 2048 A100-80GB (~21 days for 1.4T tokens).

## Result
Concrete benchmark numbers (5-shot MMLU avg): LLaMA-65B 63.4 vs Chinchilla-70B 67.5 vs PaLM-540B 69.3 vs GPT-3 175B 43.9. On GSM8k, LLaMA-65B reaches 50.9 (69.7 with maj1@k), beating Minerva-62B (52.4) without math-specific finetuning. After lightweight instruction tuning, LLaMA-I-65B hits 68.9 MMLU. Training-data mix: 67% CommonCrawl, 15% C4, 4.5% each GitHub/Wikipedia/Books, 2.5% ArXiv, 2% StackExchange.

## Why it matters here
General background; no direct arena tie. Relevant only as infrastructure context — the agent's wiki indexes math papers, not LLM-architecture papers; this distillation exists as scaffolding and should be tagged low-priority for retrieval against math-optimization queries.

## Open questions / connections
- Does scaling tokens-per-parameter beyond Chinchilla-optimal (here ~150 tok/param at 7B) continue to pay off for math-reasoning benchmarks specifically (GSM8k, MATH)?
- LLaMA underperforms on MMLU vs Chinchilla/PaLM — authors attribute to small books/papers fraction (177GB). What is the minimum academic-corpus fraction to close this gap?
- Extends Hoffmann et al. (2022) Chinchilla scaling laws by optimizing for *inference* compute rather than training compute — a different Pareto frontier.

## Key terms
LLaMA, transformer, decoder-only language model, RMSNorm, SwiGLU, rotary positional embeddings, RoPE, Chinchilla scaling laws, AdamW, BPE tokenizer, MMLU, GSM8k, foundation model, instruction finetuning, xformers attention
