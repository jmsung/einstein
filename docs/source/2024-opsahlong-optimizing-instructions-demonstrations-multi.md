---
type: source
kind: paper
title: Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs
authors: Krista Opsahl-Ong, Michael J Ryan, Josh Purtell, David Broman, Christopher Potts, Matei Zaharia, O. Khattab
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2406.11695
source_local: ../raw/2024-opsahlong-optimizing-instructions-demonstrations-multi.pdf
topic: general-knowledge
cites:
---

# Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs

**Authors:** Krista Opsahl-Ong, Michael J Ryan, Josh Purtell, David Broman, Christopher Potts, Matei Zaharia, O. Khattab  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2406.11695

## One-line
Introduces MIPRO, an optimizer that jointly tunes free-form instructions and few-shot demonstrations across all modules of a multi-stage LM program using grounded proposal + Bayesian surrogate credit assignment, without access to module-level labels or gradients.

## Key claim
On a 7-task benchmark with Llama3-8B, MIPRO outperforms baseline optimizers (Bootstrap Random Search, Module-Level OPRO, OPRO+RS) on 5 of 7 LM-program tasks, by up to $13\%$ accuracy; jointly optimizing instructions + bootstrapped demos generally beats either alone, while demos-only suffices on most tasks and instructions matter most for tasks with conditional rules.

## Method
Formalizes prompt optimization for an LM program $\Phi$ with $m$ modules as finding a variable-to-string assignment $V \to S$ maximizing $\frac{1}{|D|}\sum \mu(\Phi_{V \to S}(x), x')$ given only inputs, a metric, and final labels. Tackles two sub-problems: (1) *proposal* — bootstrap few-shot demos by rejection-sampling traces with $\mu(\Phi(x),x') \geq \lambda$, plus *grounding* a proposer LM with dataset summary, program control flow, prior instructions+scores; (2) *credit assignment* — explored greedy (per-stage), history-based (OPRO-style: feed instruction/score history back to proposer LM), and Bayesian surrogate (Tree-Structured Parzen Estimator from Optuna over discrete instruction/demo choices, evaluated on stochastic mini-batches). MIPRO combines bootstrapped-demo + grounded-instruction proposal with TPE surrogate for credit assignment; variants include 0-Shot MIPRO (instructions only), Bayesian Bootstrap (demos only), and MIPRO++ (meta-optimize proposer hyperparameters).

## Result
Across ScoNe, HotPotQA, HoVer, HotPotQA-conditional, Iris-typo, Heart Disease, MIPRO is top or co-top on 5/7. Five practitioner lessons: (i) optimizing bootstrapped demos is often the single biggest lever; (ii) instruction optimization dominates on tasks with explicit conditional rules (e.g. HotPotQA-conditional jumped 13.8 → 26.6); (iii) joint instruction+demo optimization gives best overall; (iv) Bayesian surrogate beats LM-only history-based credit assignment when $m>1$ because OPRO's equal-attribution assumption breaks; (v) overfit-to-meta-prompt instructions surprisingly sometimes win, hypothesized to act as implicit few-shot examples.

## Why it matters here
General background; no direct arena tie — this is an LM-program prompt-optimization framework (DSPy/MIPRO), not a math-optimization result. Indirectly relevant only as a possible scaffold for *meta*-optimization of the autonomous-loop agent's own multi-stage prompts (council dispatch, distill, gap-detect), where bootstrapped demos + grounded instructions could replace hand-tuned prompts.

## Open questions / connections
- Can MIPRO-style surrogate credit assignment be applied to optimizing the agent's wiki-first / council-dispatch / failure-finding prompt chain itself, with arena score as $\mu$?
- Extends OPRO (Yang 2023) and APE (Zhou 2023) to multi-stage programs; complements DSPy's BootstrapFewshotWithRandomSearch (Khattab 2024).
- Failure mode: proposers overfit instructions to demos shown in meta-prompt — open whether explicit credit assignment would suppress or whether overfit instructions are functionally demos in disguise.

## Key terms
MIPRO, DSPy, prompt optimization, LM program, multi-stage pipeline, OPRO, APE, bootstrapped demonstrations, Bayesian surrogate, Tree-structured Parzen Estimator, credit assignment, instruction proposal, Khattab, Opsahl-Ong
