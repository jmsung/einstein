---
type: source
kind: paper
title: ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code
authors: Tianyu Hua, Harper Hua, Violet Xiang, Benjamin Klieger, Sang T. Truong, Weixin Liang, Fan-Yun Sun, Nick Haber
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2506.02314
source_local: ../raw/2025-hua-researchcodebench-benchmarking-llms-implementing.pdf
topic: general-knowledge
cites:
---

# ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code

**Authors:** Tianyu Hua, Harper Hua, Violet Xiang, Benjamin Klieger, Sang T. Truong, Weixin Liang, Fan-Yun Sun, Nick Haber  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.02314

## One-line
A benchmark of 212 fill-in-the-blank coding challenges from 20 recent ML papers (2024–2025) that measures whether LLMs can translate novel research contributions into executable, test-verified code.

## Key claim
Even the best frontier LLM (Gemini-2.5-Pro-Preview-05-06) solves only 37.3% of tasks by Scaled Pass@1, with O3 (High) at 32.3% and O4-mini (High) at 30.8%; all 32 evaluated models drop noticeably on a contamination-safe 13-paper subset whose first commits postdate model knowledge cutoffs.

## Method
Authors hand-select 20 ML papers whose core contributions are cleanly implementable, then use XML-style `<ResearchCodeBench hint="…">` tags to mark code regions in the official repos at multiple granularities (function-level down to line-level), producing a nested hierarchy of 212 tasks. Each task is prompted with the full paper text + contextual code, and completions are scored by a hybrid of equivalence tests (run reference vs. generated on the same inputs, comparing outputs/gradients) and hand-written unit tests; the primary metric is **Scaled Pass@1**, weighting each snippet by its executable LoC: $\text{ScaledPass} = \sum_{s\in S_{\text{passed}}}\text{LoC}(s) / \sum_{s\in S_{\text{all}}}\text{LoC}(s)$.

## Result
Best closed models (Gemini-2.5-Pro, O3, O4-mini, GPT-4.1, Claude-3.7-Sonnet) cluster at 25–37% Scaled Pass@1; open models lag behind. Error taxonomy across all completions: 58.6% functional (semantic) errors, 9% name, 8% type, 8% syntax, 7% import, 6% attribute, 2% index/key — i.e., most failures are runs-but-wrong, not crashes. Paper-context ablation: stronger reasoning models gain up to ~30% relative from having the paper, while LLaMA-family models actually *degrade* with paper context (context dilution).

## Why it matters here
General background; no direct arena tie. Relevant only to the meta-question of how reliably an autonomous-loop agent can be expected to faithfully implement a freshly-ingested research paper into `src/einstein/` — sets a realistic ceiling (<40% on novel ML code) on agent-driven code reproduction, which argues for the wiki's distill-first-then-implement loop rather than direct paper→code generation.

## Open questions / connections
- Does the functional-error dominance (59%) replicate on math-optimization code (LP/SDP/CMA-ES), or are math kernels more brittle to off-by-one/sign errors than ML code?
- Would a `wiki-first` retrieval step before code completion close the paper-context gap that hurts LLaMA models? (The wiki distillation may be the right "compressed paper" format these models can actually use.)
- Extends Jimenez et al. (SWE-Bench), SciCode (Tian 2024), CORE-Bench (Siegel 2024), PaperBench (Starace 2025) — but is the first to isolate *post-cutoff novelty* with timeline-controlled subsets.

## Key terms
LLM code benchmark, research code reproduction, Scaled Pass@1, equivalence tests, unit tests, data contamination, knowledge cutoff, paper-context ablation, fill-in-the-blank code completion, functional error taxonomy, SWE-bench, SciCode, PaperBench, greedy decoding evaluation
