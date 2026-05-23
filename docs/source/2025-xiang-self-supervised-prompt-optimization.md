---
type: source
kind: paper
title: Self-Supervised Prompt Optimization
authors: Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu, Fengwei Teng, Jinhao Tu, Xinbing Liang, Sirui Hong, Chenglin Wu, Yuyu Luo
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2502.06855
source_local: ../raw/2025-xiang-self-supervised-prompt-optimization.pdf
topic: general-knowledge
cites:
---

# Self-Supervised Prompt Optimization

**Authors:** Jinyu Xiang, Jiayi Zhang, Zhaoyang Yu, Fengwei Teng, Jinhao Tu, Xinbing Liang, Sirui Hong, Chenglin Wu, Yuyu Luo  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2502.06855

## One-line
A reference-free prompt optimization framework that uses pairwise LLM output comparisons — no ground truth, no human feedback — to iteratively refine prompts at ~$0.15/dataset.

## Key claim
SPO matches or beats state-of-the-art prompt optimizers (APE, OPRO, PromptAgent, PromptBreeder, TextGrad) on both closed (GPQA, AGIEval-MATH, LIAR, WSC, BBH-Navigate) and open-ended (MT-Bench) tasks while using only **1.1%–5.6% of the cost** ($0.15 vs $2.71–$13.14) and just **3 samples per iteration**.

## Method
Loop of Optimize → Execute → Evaluate, all reference-free: $\phi_{\text{opt}}$ generates a new prompt $P'$ from the current best prompt $P^*$ and its outputs $A^*$; $\phi_{\text{exe}}$ runs $P'$ on 3 sampled questions; $\phi_{\text{eval}}$ uses an LLM-as-judge in pairwise mode (Output-vs-Output, "OvO") with 4 randomized rounds to pick the winner. Replaces ground-truth comparison (OvG) — the standard in OPRO/TextGrad/PromptBreeder — with pairwise output comparison, exploiting (i) prompt quality manifesting in outputs and (ii) LLM judges' task-requirement comprehension.

## Result
Average performance across 5 benchmarks: SPO 66.9, SPO* (GPT-4o opt) 66.3 vs best baseline OPRO 66.6; costs $0.15 / $0.12 vs $2.71–$13.14. On MT-Bench open-ended writing/roleplay/humanities, SPO outperforms all baselines despite having no ground truth available. Only ~8 LLM calls per iteration. Ablation: 4-round randomization of pairwise comparison mitigates (but doesn't eliminate) position/length bias; the optimization trend is robust to residual evaluator noise.

## Why it matters here
General background; no direct arena tie. Relevant as a candidate inner-loop for the autonomous-loop agent's own *prompt refinement* (e.g., council-persona prompts, optimizer config-gen prompts) — particularly when ground-truth scores are slow/expensive (long Modal jobs) and a cheap pairwise "did this prompt produce better reasoning?" judgment suffices. Complements GEPA/TextGrad/DSPy-style optimizers in the wiki.

## Open questions / connections
- Does pairwise OvO degrade on tasks where the LLM judge lacks domain competence (e.g., evaluating mpmath polish quality, equioscillation diagnostics)?
- 3-sample evaluation: when does sample-size variance dominate the optimization signal? No formal variance analysis given.
- Extends TextGrad (Yuksekgonul 2024) and PromptBreeder (Fernando 2024) by removing ground-truth dependency; relates to GEPA (Agrawal 2025) reflective prompt evolution and DSPy (Khattab 2023) declarative pipelines.
- Could the OvO signal be combined with arena-verifier ground-truth in a hybrid (cheap pairwise pre-filter → expensive verified scoring on survivors)?

## Key terms
prompt optimization, self-supervised, LLM-as-a-judge, pairwise comparison, reference-free evaluation, Output-vs-Output, TextGrad, PromptBreeder, OPRO, APE, chain-of-thought, MT-Bench, GPQA, AGIEval, BBH
