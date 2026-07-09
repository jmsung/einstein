---
type: source
kind: paper
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
authors: Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2310.06770
source_local: ../raw/2023-jimenez-swe-bench-can-language-models.pdf
topic: general-knowledge
cites:
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Authors:** Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2310.06770

## One-line
A benchmark of 2,294 real GitHub issue→PR tasks across 12 Python repos that evaluates whether LMs can edit large codebases to fix bugs / add features, with unit-test-based verification.

## Key claim
State-of-the-art LMs solve only the simplest issues: best model (Claude 2 + BM25 retrieval) resolves **1.96%** of 2,294 tasks; with "oracle" retrieval it reaches **4.8%**, and "oracle-collapsed" (gold-edited lines ±15) reaches **5.93%** (Claude 2) / **9.39%** (Claude 3 Opus). Fine-tuned SWE-Llama 13b is competitive with Claude 2 on oracle retrieval despite being open-weights.

## Method
Three-stage filter pipeline over ~90k PRs from 12 popular Python repos: (I) scrape PRs, (II) keep merged PRs that resolve a linked issue and modify test files, (III) require at least one fail-to-pass test and clean install/run — yielding 2,294 instances. Evaluation: feed issue text + retrieved code (BM25 sparse vs. "oracle" gold files) to model, apply generated unified-diff patch with `patch`, run repo's pytest suite; success = patch applies and all fail-to-pass + pass-to-pass tests pass. SWE-Llama produced by LoRA-finetuning CodeLlama-7B/13B on 19k disjoint issue-PR pairs (10k after ≤30k-token filter), training only attention weights.

## Result
On 2,294 tasks with BM25@13k: Claude 2 1.96%, GPT-4-turbo 1.31%, ChatGPT-3.5 0.17%, SWE-Llama-13b 0.70%, Claude 3 Opus 3.79%. Performance degrades with input length (Claude 2 drops sharply past 50k tokens) and with whole-file vs. patch output (Claude 2: 2.2% vs. 4.8% oracle). Model patches average ~17–30 lines edited vs. gold ~74.5; models edit ~1 file vs. gold ~1.7. No measurable post-2023 cutoff effect (no "cheating" via memorized newer code). 40% of BM25@27k retrievals strictly cover the oracle files; the other ~half miss all of them — localization is a primary bottleneck.

## Why it matters here
General background; no direct arena tie. The Einstein Arena agent is itself a long-context code-editing agent over a 23-problem repo with a wiki, so SWE-bench's findings on **context-length degradation, localization failure, and model preference for shorter/simpler patches than the gold edit** are directly relevant to how the autonomous loop should structure prompts and how strictly to gate "the optimizer change is correct."

## Open questions / connections
- Does the "models distract on long context / fail to localize" finding generalize to math-optimizer code edits, and does retrieval over `docs/wiki/` mitigate it the way BM25 partially mitigates here?
- How to capture the gold-patch quality dimension ("structural improvements that anticipate future issues") that current pass/fail tests miss — relevant for measuring whether wiki-write quality compounds.
- Extends prior code benchmarks (HumanEval, MBPP, APPS) by demanding multi-file, repo-scale, test-verified edits; future work: agentic loops on SWE-bench (which later became SWE-agent / Devin evaluations).

## Key terms
SWE-bench, GitHub issues, pull request, unit-test verification, BM25 retrieval, oracle retrieval, long context, code localization, patch generation, SWE-Llama, CodeLlama, LoRA fine-tuning, fail-to-pass test, benchmark contamination, repository-scale code edit
