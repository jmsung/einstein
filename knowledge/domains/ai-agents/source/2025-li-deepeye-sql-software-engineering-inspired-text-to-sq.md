<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework
authors: [Boyan Li, Chong Chen, Zhujun Xue, Yinan Mei, Yuyu Luo]
year: 2025
source_url: https://arxiv.org/abs/2510.17586
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework

**Authors:** Boyan Li, Chong Chen, Zhujun Xue, Yinan Mei, Yuyu Luo  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2510.17586

## One-line
Reframes Text-to-SQL as a Software Development Life Cycle (SDLC) workflow with four verifiable stages — intent grounding, N-version generation, deterministic tool-chain testing, and confidence-aware selection — achieving SOTA without fine-tuning.

## Key claim
Principled orchestration around SDLC stages, not LLM scaling or fine-tuning, drives system-level reliability: $73.5\%$ execution accuracy on BIRD-Dev, $75.07\%$ on BIRD-Test leaderboard, and $89.8\%$ on Spider-Test, using open-source MoE LLMs ($\sim$30B total, $\sim$3B activated parameters).

## Method
Four-stage pipeline: (1) Robust Schema Linking (direct + reversed + value-based) plus Semantic Value Retrieval via HNSW vector index; (2) N-version programming — three independent generators (skeleton-based, ICL-based, divide-and-conquer) producing diverse SQL candidates in parallel; (3) deterministic Syntax-Logic-Quality checker tool-chain (SELECT/JOIN/ORDER-BY/NULL/MaxMin/TIME/Result/Syntax checkers) triggering targeted LLM repair; (4) execution-based clustering with confidence-gated selection using pairwise LLM adjudication beyond simple majority voting.

## Result
DeepEye-SQL outperforms larger or fine-tuned baselines (CHESS, Alpha-SQL with MCTS, OmniSQL-32B with SFT) using $\sim$3B activated parameters. Error analysis on BIRD-Dev: 407 total errors vs 470 (Alpha-SQL) and 505 (OmniSQL-32B); strongest gains in Value-related errors (17 vs 56 and 39). Schema Linking remains hardest category (126 errors); $\sim$30% of failures attributed to ground-truth ambiguity.

## Key terms
Text-to-SQL, SDLC orchestration, N-version programming, schema linking, semantic value retrieval, HNSW vector index, deterministic verification, checker tool-chain, confidence-aware selection, self-consistency, MoE LLM, BIRD benchmark, Spider benchmark
