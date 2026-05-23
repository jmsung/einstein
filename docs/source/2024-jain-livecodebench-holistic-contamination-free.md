---
type: source
kind: paper
title: LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code
authors: Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2403.07974
source_local: ../raw/2024-jain-livecodebench-holistic-contamination-free.pdf
topic: general-knowledge
cites:
---

# LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

**Authors:** Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2403.07974

## One-line
A live-updating, contamination-resistant benchmark of 511 competition-programming problems (LeetCode/AtCoder/CodeForces, May 2023–May 2024) evaluating LLMs across four code scenarios — generation, self-repair, code execution, and test-output prediction.

## Key claim
Time-segmented evaluation exposes contamination invisible to static benchmarks: DeepSeek-Coder, GPT-4-O, and Codestral show sharp Pass@1 drops on LeetCode problems released after their respective cutoff dates (Aug 2023, Oct/Nov 2023, Jan 2024), while a separate cluster of fine-tuned open models score well on HumanEval but fail to transfer to LiveCodeBench — diagnosing HumanEval overfitting.

## Method
Scrape weekly contests across three platforms, tag each problem with its release date $D$, and filter evaluation windows so only problems with $D >$ model-cutoff are scored — making contamination falsifiable rather than guessed. Tests are collected from platform graders where available; otherwise GPT-4-Turbo synthesizes *input generators* (not raw inputs) via one-shot prompts, with separate random and adversarial variants validated against known-correct human solutions. Holistic evaluation uses four scenarios with Pass@1 (n=10, temperature 0.2, top-p 0.95) over Easy/Medium/Hard splits derived from platform difficulty ratings.

## Result
GPT-4-O leads code generation at 41.9% overall (88.3% Easy, 33.2% Medium, 4.2% Hard); Claude-3-Opus surpasses GPT-4 on test-output prediction (58.7% vs 52.9%); CoT gives a massive boost to code execution (GPT-4-O: 39.1% → 91.0%). The open/closed gap widens on non-generation tasks; only L3-Ins-70B, Mixtral-8x22B, and DS-Ins-33B (>30B instruction-tuned) close the gap to closed-API models. 511 problems / ~17 tests each / 52 models evaluated.

## Why it matters here
General background; no direct arena tie. The contamination-via-release-date methodology and triple-channel evaluation (generate / execute / predict-output) are structurally analogous to the einstein wiki's triple-verify discipline and to the cycle-log honesty checks — evidence that benchmark integrity requires the same anti-cherry-picking gates the einstein agent already enforces.

## Open questions / connections
- How to extend the contamination test to math-optimization benchmarks where problem text is shorter and rephrasing easier than competition code?
- Generator-based test synthesis (random + adversarial input generators validated on known-correct programs) — a transferable pattern for hardening the einstein verifier suite.
- HumanEval-overfitting cluster suggests SFT on benchmark-shaped problems creates capability illusions; relevant when reading any "X-tuned model beats Y" claim.

## Key terms
LiveCodeBench, contamination, HumanEval overfitting, Pass@1, code generation, self-repair, code execution, test output prediction, time-segmented evaluation, CRUXEval, input generator synthesis, competition programming
