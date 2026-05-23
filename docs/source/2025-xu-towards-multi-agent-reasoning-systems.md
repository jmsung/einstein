---
type: source
kind: paper
title: Towards Multi-Agent Reasoning Systems for Collaborative Expertise Delegation: An Exploratory Design Study
authors: Baixuan Xu, Chunyang Li, Weiqi Wang, Wei Fan, Tianshi ZHENG, Haochen Shi, Tao Fan, Yangqiu Song, Qiang Yang
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.07313
source_local: ../raw/2025-xu-towards-multi-agent-reasoning-systems.pdf
topic: general-knowledge
cites:
---

# Towards Multi-Agent Reasoning Systems for Collaborative Expertise Delegation: An Exploratory Design Study

**Authors:** Baixuan Xu, Chunyang Li, Weiqi Wang, Wei Fan, Tianshi ZHENG, Haochen Shi, Tao Fan, Yangqiu Song, Qiang Yang  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.07313

## One-line
Empirically studies how three design axes — expertise-domain alignment, collaboration paradigm, and system scale — affect collective reasoning in multi-agent LLM systems on MMLU-Pro.

## Key claim
On MMLU-Pro (Math, Business, Health, Law) with DeepSeek-R1-Distill-Qwen-7B agents: (1) expertise alignment helps most for contextual-reasoning domains (Health/Law: +6.75% relative when aligned vs. second-best misaligned) but is marginal or hurts for math-style domains; (2) diversity-driven fine-grained-expertise collaboration beats structured solver/critic/coordinator workflow by ~1.25% relative on average across all groups, with lower pairwise Sentence-BERT cosine similarity confirming higher semantic diversity; (3) scaling agents from 3→6→10 monotonically improves accuracy under both paradigms, with no observed saturation in the tested range, but communication cost grows superlinearly.

## Method
Fixes a sequential pipeline communication protocol (each agent $A_i$ sees the full rationale of $A_{i-1}$ and only the final answers of $A_1,\dots,A_{i-2}$) to avoid context explosion. Agents are instantiated by GPT-4o-generated personas $A_i \leftarrow (EG, FR, R, ID)$ — expert group, formal role, responsibility, index. Three sweeps: (a) 4×4 domain×expert-group accuracy matrix; (b) diversity-driven (sub-domain specialists) vs. structured workflow (solver/critic/coordinator) at $n=3$; (c) scale ablation at $n\in\{3,6,10\}$. Expertise–task relevance is quantified by prompting DeepSeek-V3 on 100 sampled instances per domain to name 2–3 relevant expertise domains and aggregating into a heatmap.

## Result
Aligned-diagonal accuracies (Math 78.0, Business 65.4, Health 30.4, Law 20.8) win in 3/4 domains; Business is the exception where Math experts (65.4) tie/beat Business experts (64.3). Diversity-driven gains are largest in Business/Health (+1.75% avg relative). Scaling to 10 agents improves both paradigms across all four domains, but pairwise message volume scales quadratically — the paper explicitly calls for more efficient communication protocols. Sentence-BERT cosine similarity is consistently lower (more diverse) for diversity-driven than for structured workflows.

## Why it matters here
General background; no direct arena tie. Relevant only as scaffolding for the council-dispatch rule — it supports the design choice that personas should be fine-grained sub-domain specialists writing diverse perspectives rather than a fixed solver/critic/coordinator pipeline, and that aligning persona expertise to the problem category (sphere_packing → Viazovska, autocorrelation → Hilbert, etc.) is empirically justified for "contextual" tasks. Says nothing useful about pure mathematical deduction, which is the einstein regime — the paper itself notes expertise alignment gives only marginal gains on math.

## Open questions / connections
- Does the diversity > workflow result hold for hard math (e.g., olympiad / research-level proof search), or only mid-difficulty MMLU-Pro math where the 7B base model already saturates?
- What is the right communication topology beyond sequential — sparse graphs, hierarchical aggregation, sparse Mixture-of-Agents — for cost-bounded scaling past $n=10$?
- The "Knowledge Recall vs Perspective Synthesis" dichotomy is asserted but never causally separated; ablations isolating each mechanism would test whether persona prompts do more than activate a stylistic register.

## Key terms
multi-agent LLM systems, collaborative expertise specialization, persona prompting, council dispatch, diversity-driven collaboration, structured workflow, MMLU-Pro, response diversity, Sentence-BERT cosine similarity, DeepSeek-R1-Distill, sequential communication protocol, scaling laws agents
