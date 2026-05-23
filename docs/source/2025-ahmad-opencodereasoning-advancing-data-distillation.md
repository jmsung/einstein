---
type: source
kind: paper
title: OpenCodeReasoning: Advancing Data Distillation for Competitive Coding
authors: Wasi Uddin Ahmad, Sean Narenthiran, Somshubra Majumdar, Aleksander Ficek, Siddhartha Jain, Jocelyn Huang, V. Noroozi, Boris Ginsburg
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2504.01943
source_local: ../raw/2025-ahmad-opencodereasoning-advancing-data-distillation.pdf
topic: general-knowledge
cites:
---

# OpenCodeReasoning: Advancing Data Distillation for Competitive Coding

**Authors:** Wasi Uddin Ahmad, Sean Narenthiran, Somshubra Majumdar, Aleksander Ficek, Siddhartha Jain, Jocelyn Huang, V. Noroozi, Boris Ginsburg  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2504.01943

## One-line
Builds a 736k-sample DeepSeek-R1-distilled SFT dataset for competitive coding and shows SFT-only Qwen2.5 fine-tunes match or beat SFT+RL open models on LiveCodeBench/CodeContests.

## Key claim
SFT alone on a sufficiently large, diverse reasoning-trace dataset (OpenCodeReasoning, 736,712 samples over 28,904 unique competitive-programming questions) yields $61.8\%$ pass@1 on LiveCodeBench and $24.6\%$ on CodeContests at 32B — surpassing R1-Distill-Qwen-32B, OlympicCoder-32B, QwQ-32B and OpenAI O1/O3-Mini(Low/Med), and closing most of the gap to DeepSeek-R1 ($65.6\%$ / $26.2\%$).

## Method
Collect 28,904 deduplicated competitive-coding questions from TACO/APPS/CodeContests/CodeForces; generate multiple R1 reasoning-trace solutions (Python + C++) via nucleus sampling ($T{=}0.6$, top-$p{=}0.95$, forced `<think>` tag, 16k tokens) using SGLang; filter only for `<think>` tag presence, code-block presence, and Tree-Sitter syntactic validity — explicitly NOT for unit-test correctness. SFT Qwen2.5-{7B,14B,32B} base/instruct for 3 epochs (AdamW, lr $5{\times}10^{-5}$, cosine, seqlen 32,768, BF16).

## Result
Scaling from 25k→736k samples shows no plateau; 32B model: LCB $61.8$, CC $24.6$. Surprising ablation: training on R1's *incorrect* solutions ($52.3$ LCB) beats training on its *correct* ones ($47.0$ LCB), because incorrect solutions concentrate on harder questions — instruction diversity/difficulty dominates solution correctness as a quality signal. Adding 356k C++ samples doesn't help Python benchmarks but lifts IOI from 145.5→175.5. OCR-32B uses 20–30% fewer reasoning tokens than QwQ-32B at comparable accuracy. Reasoning-pattern analysis: self-evaluation and subgoal generation are significantly more frequent in correct solutions; entropy of pattern distribution is higher for correct (1.26) than incorrect (1.19) generations.

## Why it matters here
General background; no direct arena tie. The "filter for diversity/difficulty, not for verified correctness" finding is methodologically relevant if the einstein agent ever builds its own distillation corpus from council/persona traces — it argues against discarding failed-attempt reasoning, consistent with the repo's existing `failure-is-a-finding` rule.

## Open questions / connections
- Why does training on incorrect-but-hard reasoning transfer positively? Is the signal the question difficulty distribution, the reasoning structure, or both?
- Optimal multilingual mixing strategy when target benchmarks span languages (Python+C++ here; analogous to mixing optimizer families in math distillation).
- Reasoning-token budget saturates around 16k for hard problems despite 32k allowance — what causes unrecoverable reasoning loops, and does this generalize to math-reasoning distillation?
- Extends BespokeLabs/OpenThoughts/s1 small-SFT line by showing code (unlike math) genuinely needs scale.

## Key terms
reasoning distillation, supervised fine-tuning, DeepSeek-R1, chain-of-thought, LiveCodeBench, CodeContests, synthetic data, instruction diversity, execution filtering, Qwen2.5, reasoning patterns, self-evaluation, subgoal generation, backtracking, competitive programming
