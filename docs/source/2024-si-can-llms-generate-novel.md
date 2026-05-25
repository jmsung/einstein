---
type: source
kind: paper
title: Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers
authors: Chenglei Si, Diyi Yang, Tatsunori Hashimoto
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2409.04109
source_local: ../raw/2024-si-can-llms-generate-novel.pdf
topic: general-knowledge
cites:
---

# Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers

**Authors:** Chenglei Si, Diyi Yang, Tatsunori Hashimoto  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2409.04109

## One-line
A controlled head-to-head study comparing LLM-generated NLP research ideas against those of 100+ expert researchers via blind review.

## Key claim
LLM-generated research ideas are judged statistically significantly more novel than expert-written ideas ($p < 0.05$, two-tailed Welch's t-test with Bonferroni correction), though slightly weaker on feasibility; AI ideas $\mu=5.64 \pm 1.76$ vs human $\mu=4.84 \pm 1.79$ on novelty.

## Method
Recruited 49 expert idea-writers and 79 reviewers (104 total NLP researchers across 32 institutions); collected 298 blind reviews across three conditions (Human, AI, AI+Human-Rerank) on 7 fixed topics with style-normalized writeups. The LLM agent uses RAG (Semantic Scholar API + Claude-3.5-Sonnet), over-generates 4000 seed ideas per topic, deduplicates via Sentence-Transformer cosine similarity ($\tau=0.8$), and ranks via Swiss-tournament pairwise comparison (LLM ranker achieves 71.4% accuracy predicting ICLR accept/reject).

## Result
Across three statistical tests (per-review, per-idea, per-reviewer), AI conditions beat humans on novelty significantly; excitement and overall trend higher but underpowered. Only ~5% of 4000 seed ideas survive deduplication — LLMs lack diversity at scale. LLM self-evaluation is unreliable (Claude ranker disagrees with human reranker on 32/49 picks). Execution-agent pilot: ~50% of generated code runs, only 5/30 (safety) and 1/30 (factuality) actually outperform baselines under manual audit.

## Why it matters here
General background; no direct arena tie. Relevant as methodological prior for the einstein self-improvement loop — specifically, this paper validates that LLM ideation *can* produce novel candidates but warns that (a) LLM rankers are weak, (b) diversity collapses with scale, (c) LLM-as-judge and LLM-as-executor are unreliable without human verification — all of which mirror the repo's triple-verify and human-gated promotion stances.

## Open questions / connections
- Does novelty-judged-by-experts predict actual research outcome? (Authors propose a follow-up execution study.)
- How to fix LLM-ranker miscalibration so reranking doesn't need a human in the loop?
- Why does over-generation collapse to ~5% unique ideas — is this a sampling-temperature artifact or a deeper mode-collapse?
- Connects to council-dispatch (personas-as-question-generators) and failure-is-a-finding (execution agent's silent baseline-gaming as a dead-end-finding template).

## Key terms
LLM ideation, research agents, novelty evaluation, blind review, retrieval-augmented generation, RAG, Swiss tournament ranking, pairwise comparison, inference-time scaling, LLM-as-judge, idea diversity, Claude-3.5-Sonnet, Welch's t-test, Bonferroni correction
