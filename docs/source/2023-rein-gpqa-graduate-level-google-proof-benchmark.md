---
type: source
kind: paper
title: "GPQA: A Graduate-Level Google-Proof Q&A Benchmark"
authors: David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, Samuel R. Bowman
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2311.12022
source_local: ../raw/2023-rein-gpqa-graduate-level-google-proof-benchmark.pdf
topic: general-knowledge
cites:
---

# GPQA: A Graduate-Level Google-Proof Q&A Benchmark

**Authors:** David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, Samuel R. Bowman  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2311.12022

## One-line
Introduces a 448-question multiple-choice benchmark of graduate-level biology/physics/chemistry problems designed to be answerable by domain PhDs but "Google-proof" for skilled non-experts, as a testbed for scalable oversight of LLMs.

## Key claim
The benchmark is simultaneously hard for skilled non-experts (34% accuracy, ~37 min/question with web access) and for frontier LLMs (GPT-4 few-shot CoT: 39%), while domain-expert PhDs reach 65% raw / 74% after discounting clear retrospective mistakes — random chance is 25%.

## Method
Four-stage human pipeline with 61 PhD-level Upwork contractors: (1) expert question writing in subdomain, (2) blind first-expert validation + feedback, (3) writer revision, (4) blind second-expert validation plus three non-expert validators (PhDs in other domains, unrestricted web, ≥15 min, mean 37 min, no LLM assistants). Bonus-heavy incentive structure (~$95/hr) rewards questions both other experts answer correctly and non-experts answer incorrectly. Three released splits: Extended (546), main GPQA (448), Diamond (198, ≥2/2 experts agree & ≤1/3 non-experts correct).

## Result
Expert accuracy 65%/74% (raw/post-hoc-adjusted) vs non-expert 34% on Extended; expertise gap is ~25 pts in biology/physics and ~41 pts in chemistry. Baselines: Llama-2-70B-chat ~30%, GPT-3.5 ~28–32%, GPT-4 few-shot CoT 39%, GPT-4-with-search 39% — all far below expert accuracy. Answer-only classifiers (Llama-2 and CBOW-RoBERTa) fail to beat 25% chance, suggesting no easily exploitable answer-choice artifacts.

## Why it matters here
General background; no direct arena tie. GPQA is an evaluation benchmark for LLM scalable oversight in graduate science Q&A, not a math-optimization or combinatorics paper — it does not inform any of the 23 Einstein Arena problems (sphere packing, autocorrelation, kissing, sieve, extremal graph, etc.) directly.

## Open questions / connections
- How well do reasoning-tuned successor models (post-GPT-4) close the expert–model gap on GPQA, and does that gap predict performance on harder open-ended scientific tasks?
- Can debate / market-making / recursive-reward-modeling oversight protocols let non-expert humans + model assistants outperform the 34% non-expert baseline while staying truthful?
- Extends BIG-Bench / MMLU style multiple-choice evals into a regime explicitly designed to defeat web search — relevant to any future arena-style benchmark of "questions an LLM can't Google its way through".

## Key terms
GPQA, scalable oversight, Google-proof, graduate-level QA, multiple-choice benchmark, expert validation, non-expert validation, RLHF, hallucination, sycophancy, debate (Irving), GPT-4 baseline, chain-of-thought prompting, post-hoc agreement, Diamond subset
