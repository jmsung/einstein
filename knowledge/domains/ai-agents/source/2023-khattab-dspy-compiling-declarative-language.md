<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines
authors: [O. Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts]
year: 2023
source_url: https://arxiv.org/abs/2310.03714
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines

**Authors:** O. Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2310.03714

## One-line
A programming model that replaces hand-crafted LM prompt strings with declarative, parameterized modules and a compiler ("teleprompter") that auto-bootstraps few-shot demonstrations or finetunes to optimize an arbitrary LM pipeline against a metric.

## Key claim
Compiled DSPy programs from a few lines of code outperform expert-written prompt chains: GPT-3.5 vanilla programs rise from 33%→82% (GSM8K) and 32%→46% (HotPotQA); llama2-13b-chat rises 9%→47% and 22%→41%; small open LMs (T5-770M, llama2-13b) compiled via DSPy match proprietary GPT-3.5 chains.

## Method
Three abstractions: (1) **signatures** — natural-language typed I/O declarations (e.g. `question -> answer`) replacing string prompts; (2) **modules** — parameterized layers like `Predict`, `ChainOfThought`, `ReAct`, `ProgramOfThought`, composed via PyTorch-style define-by-run forward methods; (3) **teleprompters** — compilers (`BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`/`Optuna`, `BootstrapFinetune`) that simulate a teacher program with high temperature, trace multi-stage executions, filter by metric, and use successful traces as bootstrapped few-shot demos or finetuning data.

## Result
On GSM8K (math word problems) and HotPotQA (multi-hop QA), compiled DSPy programs beat both vanilla few-shot prompting (by ~25%/65% for GPT-3.5/llama2) and expert-crafted prompt chains (by 5–46% / 16–40%). Compilation takes minutes; label-efficient (often only final-output labels, intermediate labels bootstrapped). Higher-order optimizations (ensembling, majority voting) further compose modular gains.

## Key terms
DSPy, teleprompter, BootstrapFewShot, declarative modules, signature, Predict, ChainOfThought, ReAct, prompt compilation, demonstration bootstrapping, self-improving pipeline, multi-stage LM pipeline, foundation model programming, in-context learning, retrieval-augmented generation
