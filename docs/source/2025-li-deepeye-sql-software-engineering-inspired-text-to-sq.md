---
type: source
kind: paper
title: DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework
authors: Boyan Li, Chong Chen, Zhujun Xue, Yinan Mei, Yuyu Luo
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2510.17586
source_local: ../raw/2025-li-deepeye-sql-software-engineering-inspired-text-to-sq.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. The SDLC-orchestration paradigm (N-version programming for diversity, deterministic checker tool-chain over self-reflection, confidence-gated quality selection) is relevant as agent-architecture inspiration for the einstein autonomous loop — particularly the "checker tool-chain replaces probabilistic self-judgment" principle, which mirrors the repo's triple-verify axiom.

## Open questions / connections
- Can N-version programming with diverse reasoning paradigms (vs same-prompt sampling) improve persona-council dispatch coverage on math problems?
- The deterministic-checker-replaces-self-reflection principle generalizes; what's the analog for math optimizer outputs beyond the existing triple-verify rule?
- Confidence-aware selection via execution-clustering + pairwise LLM adjudication — applicable to picking among multiple optimizer candidates that produce near-tied scores?

## Key terms
Text-to-SQL, SDLC orchestration, N-version programming, schema linking, semantic value retrieval, HNSW vector index, deterministic verification, checker tool-chain, confidence-aware selection, self-consistency, MoE LLM, BIRD benchmark, Spider benchmark
