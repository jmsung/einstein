---
type: source
kind: paper
title: m1: Unleash the Potential of Test-Time Scaling for Medical Reasoning with Large Language Models
authors: Xiaoke Huang, Juncheng Wu, Hui Liu, Xianfeng Tang, Yuyin Zhou
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2504.00869
source_local: ../raw/2025-huang-unleash-potential-test-time-scaling.pdf
topic: general-knowledge
cites:
---

# m1: Unleash the Potential of Test-Time Scaling for Medical Reasoning with Large Language Models

**Authors:** Xiaoke Huang, Juncheng Wu, Hui Liu, Xianfeng Tang, Yuyin Zhou  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2504.00869

## One-line
Shows that test-time scaling (longer chain-of-thought budgets) improves medical QA but saturates around 4K tokens because the bottleneck is missing domain knowledge, not reasoning depth.

## Key claim
A lightweight SFT recipe (1K–23K curated medical QA traces from DeepSeek-R1) plus a token-budget inference control lets a 7B model reach 60.32% average accuracy across 10 medical benchmarks — beating HuatuoGPT-o1-7B (RL on 40K) and matching UltraMedical-8B (hundreds of thousands of instructions); the 32B-1K variant rivals 70B-class medical LLMs. Performance peaks near a ~4K-token "thinking budget" and degrades beyond it; "Wait"-token budget forcing fails to improve and sometimes corrupts correct answers.

## Method
Three-stage data curation: (1) difficulty-filter 196K → 37K by dropping items either Qwen2.5-7B or 32B-Instruct solves; (2) generate CoT traces with DeepSeek-R1 and keep only correct ones (23K, "m23K"); (3) MeSH-stratified diversity sampling to a balanced 1K subset ("m1K"). SFT Qwen2.5-7B/32B-Instruct (5 epochs, lr 1e-4, batch 16, format `<|im_start|>think ... answer`). Inference: cap and pad CoT to a target token budget; optionally inject "Wait." at the end-of-think token to force re-thinking (s1-style budget forcing).

## Result
m1-7B-23K averages 60.32% across MedMCQA, MedQA-USMLE, PubMedQA, MMLU-Pro (Med), GPQA (Med), Lancet, MedBullets Op4/Op5, MedXpertQA, NEJM — a new SOTA in the ≤10B class. m1-32B-1K averages 68.24%, comparable to HuatuoGPT-o1-70B (70.01%). Accuracy rises monotonically with thinking budget up to ~4K tokens then plateaus or declines; budget forcing yields flat-to-negative deltas. Ablations: difficulty filtering > random by 0.27% (1K) / 0.65% (23K); adding MeSH-domain + dataset balance adds another ~1.5% at 1K scale.

## Why it matters here
General background; no direct arena tie. The agent-relevant lesson is the failure mode of test-time scaling: extra reasoning tokens cannot patch missing factual grounding and can flip correct answers to wrong via "overthinking" — analogous to the einstein wiki's wiki-first-lookup and triple-verify rules, where a council persona without the right grounding produces plausible-but-wrong markdown. Reinforces the principle that knowledge curation (data quality + model capacity) compounds where pure inference-time scaling saturates.

## Open questions / connections
- Extends s1 (Muennighoff 2025) to a knowledge-bound rather than reasoning-bound domain — what is the analogous saturation regime for math/optimizer agents?
- Does budget forcing also degrade in math-heavy domains when the base model holds wrong "facts" (e.g., misremembered LP bounds, miscited Cohn–Elkies thresholds)?
- The ~4K-token optimum is empirical — is there a predictor of optimal CoT length from question difficulty / entropy?

## Key terms
test-time scaling, chain-of-thought, budget forcing, supervised fine-tuning, DeepSeek-R1 distillation, s1 method, medical QA, MeSH stratified sampling, difficulty filtering, overthinking, Qwen2.5, knowledge grounding
