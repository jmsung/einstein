---
type: source
kind: paper
title: DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines
authors: O. Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T. Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, Christopher Potts
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2310.03714
source_local: ../raw/2023-khattab-dspy-compiling-declarative-language.pdf
topic: general-knowledge
cites:
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

## Why it matters here
Direct relevance to the autonomous-loop agent infrastructure on this branch (feat/autonomous-loop): DSPy is the canonical template for "declarative modules + compiler that bootstraps demonstrations from successful traces" — i.e., exactly the self-improvement loop pattern (gap → trace → distill → reuse) the einstein wiki encodes. The council-dispatch + self-improvement-loop architecture mirrors DSPy's teleprompter pattern (teacher program supervises student; only successful traces become demonstrations). No direct math content — general background for agent design, not for arena problem-solving.

## Open questions / connections
- Could a DSPy-style teleprompter compile the math-solving protocol (understand → wiki-first → council → distill) so that successful problem-solve traces auto-bootstrap demonstrations for the next problem?
- Extends to RL- and Bayesian-HPO-based prompt optimization (HyperOpt, Optuna, Hu et al. 2023) — relevant if council dispatch is to be tuned as a hyperparameter search.
- Connects to STaR (Zelikman et al. 2022) rationale self-generation and ReAct (Yao et al. 2022); the failure-is-a-finding rule is the inverse of DSPy's "throw away bad examples" — we keep them with articulated why.

## Key terms
DSPy, teleprompter, BootstrapFewShot, declarative modules, signature, Predict, ChainOfThought, ReAct, prompt compilation, demonstration bootstrapping, self-improving pipeline, multi-stage LM pipeline, foundation model programming, in-context learning, retrieval-augmented generation
