<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-ml]
title: ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code
authors: [Tianyu Hua, Harper Hua, Violet Xiang, Benjamin Klieger, Sang T. Truong, Weixin Liang, Fan-Yun Sun, Nick Haber]
year: 2025
source_url: https://arxiv.org/abs/2506.02314
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
LLM code benchmark, research code reproduction, Scaled Pass@1, equivalence tests, unit tests, data contamination, knowledge cutoff, paper-context ablation, fill-in-the-blank code completion, functional error taxonomy, SWE-bench, SciCode, PaperBench, greedy decoding evaluation
