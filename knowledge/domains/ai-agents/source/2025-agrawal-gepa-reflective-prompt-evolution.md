---
type: source
kind: paper
title: GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
authors: Lakshya A. Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, A. Dimakis, Ion Stoica, Dan Klein, Matei A. Zaharia, O. Khattab
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2507.19457
source_local: ../raw/2025-agrawal-gepa-reflective-prompt-evolution.pdf
topic: general-knowledge
cites:
---

# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

**Authors:** Lakshya A. Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, Herumb Shandilya, Michael J Ryan, Meng Jiang, Christopher Potts, Koushik Sen, A. Dimakis, Ion Stoica, Dan Klein, Matei A. Zaharia, O. Khattab  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2507.19457

## One-line
GEPA is a sample-efficient prompt optimizer that evolves LLM-module prompts by reflecting on natural-language execution traces and selecting candidates from a Pareto frontier, outperforming RL (GRPO) and prior prompt optimizers (MIPROv2) with far fewer rollouts.

## Key claim
Across six tasks (HotpotQA, IFBench, Hover, PUPA, AIME-2025, LiveBench-Math) with Qwen3-8B, GEPA beats GRPO by up to $+20\%$ (avg $+6\%$) while using up to $35\times$ fewer rollouts, and beats MIPROv2 by $>10\%$ aggregate (e.g. $+12\%$ on AIME-2025). On GPT-4.1-Mini it achieves $+9\%$ aggregate over baseline and shows cross-model generalization (Qwen-optimized prompts transfer to GPT-4.1-Mini).

## Method
Treats a compound AI system as $\Phi=(M,C,X,Y)$ with per-module prompts $\pi_i$, fixed weights $\theta_i$. Inner loop: (i) **Pareto-based candidate selection** — keep candidates that lead on at least one training instance, prune dominated ones, sample weighted by per-task wins (illumination strategy, after Mouret & Clune); (ii) **reflective prompt mutation** — run candidate on a minibatch, feed (prompt, trace, score, feedback text from a feedback function $\mu_f$) to a reflection LM, which proposes a revised instruction for one module (round-robin); (iii) accept if minibatch score improves, then re-score on validation $D_{\text{pareto}}$. Optional **system-aware merge (crossover)** combines complementary module updates from two ancestors.

## Result
Qwen3-8B aggregate: Baseline 45.23, GRPO 48.91 (24 000 rollouts), MIPROv2 47.84, GEPA 54.85 (1.8k–7k rollouts), GEPA+Merge 52.40. GPT-4.1-Mini aggregate: Baseline 53.03, MIPROv2 58.67, TextGrad 59.14, GEPA higher (with Qwen-optimized GEPA prompts already $\approx +9\%$ over baseline). Total reflection-LM calls are modest (17–92 per benchmark, Table 4). Also serves as inference-time search for code/kernel generation: NPUEval rises $4.25\% \to 26.85\%$ with the same GPT-4o agent.

## Why it matters here
General background; no direct Einstein-Arena math tie, but methodologically central to this repo's autonomous-loop agent: GEPA is the academic instance of the "reflect on traces, write back lessons, keep a diverse frontier" pattern that the wiki+council architecture targets. Directly informs the **self-improvement-loop**, **council-dispatch**, **failure-is-a-finding**, and **wiki-attribution** rules — Pareto-frontier candidate selection is a concrete answer to the "don't collapse to the global-best prompt/finding" problem, and the $\mu_f$ feedback-function abstraction maps onto the triple-verify evaluator returning natural-language diagnostics, not just scalars.

## Open questions / connections
- Extends MIPROv2 (Opsahl-Ong et al. 2024) and DSPy (Khattab et al. 2024); contrasts with GRPO (Shao et al. 2024) and TextGrad (Yuksekgonul et al. 2024).
- Can the Pareto-front illumination be ported to **finding/concept selection** in the wiki (keep findings that lead on at least one problem, prune strictly dominated ones)?
- Cross-model prompt transfer (Qwen→GPT-4.1-Mini) suggests prompts encode task-level wisdom rather than model-specific tricks — relevant to whether wiki-distilled "lessons" generalize across solver models.
- Inference-time search variant (NPUEval, KernelBench) hints at using GEPA-style reflection as a per-problem optimizer wrapper, not just an offline trainer.

## Key terms
GEPA, reflective prompt evolution, Pareto frontier candidate selection, MAP-Elites illumination, MIPROv2, GRPO, TextGrad, DSPy, compound AI system, reflection LM, feedback function, sample-efficient optimization, prompt mutation, system-aware merge, credit assignment
