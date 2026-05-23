---
type: source
kind: paper
title: CritiQ: Mining Data Quality Criteria from Human Preferences
authors: Honglin Guo, Kai Lv, Qipeng Guo, Tianyi Liang, Zhiheng Xi, Demin Song, Qiuyinzhe Zhang, Yu Sun, Kai Chen, Xipeng Qiu, Tao Gui
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.19279
source_local: ../raw/2025-guo-critiq-mining-data-quality.pdf
topic: general-knowledge
cites:
---

# CritiQ: Mining Data Quality Criteria from Human Preferences

**Authors:** Honglin Guo, Kai Lv, Qipeng Guo, Tianyi Liang, Zhiheng Xi, Demin Song, Qiuyinzhe Zhang, Yu Sun, Kai Chen, Xipeng Qiu, Tao Gui  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.19279

## One-line
An LLM-agent workflow that mines verbal data-quality criteria from only ~30 human pairwise annotations, then trains a lightweight Bradley-Terry scorer for large-scale corpus filtering.

## Key claim
With ~30 human-annotated pairs, CritiQ Flow + CritiQ Scorer reaches 90.04% average agreement with human quality judgments across code/math/logic (vs. 75.96% vanilla, 75.50% TextGrad), and continual pretraining of Llama-3.2-3B on CritiQ-selected subsets beats uniform sampling and QuRating-Edu on HumanEval/MBPP, GSM8k/SAT-Math/MATH, and ARC-C/LogiQA.

## Method
A manager agent (GPT-4o) and multiple worker agents (Qwen2.5-72B-Instruct) iteratively evolve a set of verbal quality criteria: workers do pairwise judgments under each criterion; the manager keeps high-accuracy criteria, reflects on mid-accuracy criteria using wrong cases to refine descriptions, and replaces low-accuracy ones. Initial criteria are retrieved from a 342-entry knowledge base auto-extracted from prior dataset papers. Final criteria annotate 25k pairs used to train a Bradley-Terry Scorer ($\mathcal{L} = -\log \sigma(s_\theta(d_\text{high}) - s_\theta(d_\text{low}))$) on Qwen2.5-1.5B, then Gumbel top-$k$ sampling with $p_i \propto \exp(s_i/\tau)$ selects the high-quality subset.

## Result
Test-set accuracies: CritiQ Scorer 89.89/90.00/90.22 (code/math/logic) vs. vanilla 82.02/72.86/72.99 and best single QuRating criterion (Educational Value) 85.39/68.57/84.33. Ablations confirm both the knowledge base (+3.5 avg) and reflective evolution (+3.9 avg) contribute. Continual pretraining on 10B/3B/10B-token CritiQ subsets yields HumanEval 39.02 vs 28.66 raw, GSM8k 32.22 vs 27.60, LogiQA 30.41 vs 27.34. Refusal rates of criteria drop and accuracy distribution shifts upward across iterations; several criteria reach 100% accuracy on applicable subsets.

## Why it matters here
General background; no direct arena tie. The agent-loop pattern — manager/worker split, reflection on wrong cases, accuracy-gated criterion updates, knowledge-base-seeded initialization from ~30 human anchors — is structurally relevant to the einstein self-improvement loop (gap→search→ingest→distill→page) and to council-dispatch, where personas could similarly evolve via reflection on per-question accuracy rather than be hand-curated.

## Open questions / connections
- Does the accuracy-gated update rule (only accept $c'_i$ if $\text{acc}'_i \geq \text{acc}_i$) transfer to multi-step math-reasoning critique, where "accuracy on 30 pairs" has no clean analogue?
- The knowledge base is built by Jaccard-dedup of paper-extracted criteria (threshold 0.3) — would this same pipeline produce a usable persona/heuristic base from mathematician biographies for einstein's council?
- Extends TextGrad (Yuksekgonul 2024) and Reflexion-style (Shinn 2023) reflection by adding explicit per-criterion accuracy bookkeeping; relates to QuRating (Wettig 2024) which used hand-defined criteria.

## Key terms
data quality, pairwise preference, Bradley-Terry model, LLM agent workflow, manager-worker, reflection, criteria evolution, knowledge base, TextGrad, QuRating, continual pretraining, Gumbel top-k sampling
