<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
authors: [Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan]
year: 2024
doi: 10.48550/arXiv.2310.06770
source_url: https://doi.org/10.48550/arXiv.2310.06770
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

## TL;DR
SWE-bench is a benchmark of 2,294 real GitHub issue→pull-request tasks across 12 popular Python repos, where a model must edit a full codebase to resolve an issue and pass the repo's unit tests; even the best 2023-era model (Claude 2) resolved only 1.96% of issues, exposing a large gap between LLM coding ability and real software engineering.

## Key findings
- **Benchmark scale and construction.** 2,294 task instances distilled from ~90,000 PRs across 12 widely-used Python repos (django, sympy, scikit-learn, matplotlib, sphinx, etc.) via a 3-stage pipeline: scrape merged PRs → keep those that resolve an issue *and* edit test files → execution-filter to those with ≥1 fail-to-pass test and clean install (Fig. 2, Table 10).
- **Tasks are large and cross-file.** Codebases average 3,010 non-test files / 438K lines; issue text averages 195 words; the gold patch edits on average **1.7 files, 3.0 functions, 32.8 lines** (Table 1). 40% of instances have ≥2 fail-to-pass tests; a median of 51 additional pass-to-pass tests guard against regressions.
- **Near-total failure of frontier models (BM25 retrieval, Table 5).** Claude 2 resolves **1.96%**, GPT-4-turbo 1.31%, ChatGPT-3.5 0.17%, Claude 3 Opus 3.79%. On the easier 300-instance **SWE-bench Lite**, rates rise only modestly (Claude 2 3.0%, Claude 3 Opus 4.33%).
- **Retrieval matters enormously.** With "oracle" retrieval (handing the model exactly the files the gold patch edits), Claude 2 jumps to 4.8% (Table 18). An "oracle-collapsed" setting (only edited lines ±15) pushes Claude 3 Opus to 9.39%, Claude 2 to 5.93% (Table 6).
- **Difficulty correlates with context length, not date.** Performance drops sharply as total input tokens grow (Fig. 5) — models fail to localize the lines needing edits among a "sea of context," corroborating lost-in-the-middle effects. Performance is roughly flat before/after 2023 (Table 7), arguing against memorization/data-leakage.
- **Models under-edit.** Successfully-applied model patches are <half the length of gold patches (e.g. Claude 2 19.6 vs 44.1 lines, Table 8) and rarely touch >1 file; outcome analysis (Table 23) shows most non-resolved patches are "No-Op" or "Regression" — they pass zero fail-to-pass tests.
- **Open model.** SWE-Llama 7b/13b — CodeLlama fine-tuned via LoRA on 19,000 issue-PR pairs from 37 disjoint repos — is competitive with Claude 2 in some settings and handles >100K-token contexts, but is sensitive to context-distribution shift (poor with BM25 since trained on oracle context).

## Methods (brief)
Execution-based evaluation: a model emits a unix patch; the harness checks out the base commit, installs the repo in a version-specific conda env, applies the test patch, applies the prediction, and runs the test script — an instance is "resolved" only if all fail-to-pass *and* pass-to-pass tests pass. Retrieval baselines use BM25 (dense retrieval ill-suited to long code+NL queries). SWE-Llama trained with LoRA (r=16) on attention sublayers, Flash Attention + DeepSpeed Ulysses for long-context.

## Limitations
Python-only and 2023-era models — absolute resolve rates (≤4%) are now far surpassed by agentic scaffolds, so the *numbers* are dated even if the benchmark design endures. Execution-based pass/fail does not capture code quality, efficiency, or readability (qualitative analyses show models write primitive, stylistically inconsistent code); image-bearing issues (e.g. 32% of matplotlib) are unsolvable without vision.

## Citations of interest
- Chen et al. 2021 (HumanEval) — the prior code-generation standard SWE-bench contrasts against (self-contained, few-line problems).
- Rozière et al. 2023 (Code Llama) — base model fine-tuned into SWE-Llama; only family handling the required long contexts at the time.
- Hu et al. 2022 (LoRA) — parameter-efficient fine-tuning used to train SWE-Llama.
- Liu et al. 2023b ("Lost in the Middle") — explains why model performance degrades with longer retrieved context.
- Robertson et al. 2009 (BM25) — the sparse retriever used to select in-context files.
- Yao et al. 2022 (WebShop) / Liu et al. 2023d (AgentBench) — related interactive-agent benchmarks motivating the realistic, multi-step framing.
