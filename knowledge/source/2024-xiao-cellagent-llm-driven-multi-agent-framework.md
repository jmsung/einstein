---
type: source
kind: paper
title: "CellAgent: An LLM-driven Multi-Agent Framework for Automated Single-cell Data Analysis"
authors: Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, Shaoqing Jiao, Jiajie Peng
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2407.09811
source_local: ../raw/2024-xiao-cellagent-llm-driven-multi-agent-framework.pdf
topic: general-knowledge
cites:
---

# CellAgent: An LLM-driven Multi-Agent Framework for Automated Single-cell Data Analysis

**Authors:** Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, Shaoqing Jiao, Jiajie Peng  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2407.09811

## One-line
An LLM-driven multi-agent framework (Planner / Executor / Evaluator) automates the end-to-end single-cell RNA-seq analysis pipeline with zero human intervention.

## Key claim
CellAgent attains a 92% task completion rate across 50+ scRNA-seq datasets — roughly double GPT-4 alone — and matches or surpasses specialized tools on batch correction (overall 0.684 vs scVI 0.642), cell type annotation (94% cluster accuracy on PBMC), and trajectory inference (overall 0.496 vs Slingshot 0.473).

## Method
Three GPT-4–driven biological "expert roles" collaborate via hierarchical decision-making: a Planner decomposes the natural-language task into subtasks, Executors (Tool Selector + Code Programmer) retrieve tool documentation and emit code, and an Evaluator (using GPT-4V on UMAP visualizations) scores results and triggers re-generation. Auxiliary components — global/local memory (storing only finalized step code), a tool-retrieval registry with docstrings, and a Jupyter-nbconvert code sandbox — support a self-iterative optimization loop with default 3 trials per step, where the Evaluator either ranks methods (batch correction, trajectory) or aggregates them (cell-type annotation across CellMarker 2.0, ACT, CellTypist, SCSA, ScType, GPT-4).

## Result
Benchmarked on 9 batch-correction datasets, 22 expert-labeled annotation datasets across human PBMC/liver/lung/pancreas and mouse retina, and 9 gold-standard trajectory datasets. CellAgent ranks first on 4/9 batch datasets, achieves 10 "fully match" / 5 "partial" / 1 "mismatch" on 17 PBMC clusters, and leads on cordist, F1branches, wcorfeatures, edgeflip, NMSErf, $R^2_{rf}$, isomorphic, F1milestones, corfeatures for trajectory inference. The MLLM-as-judge (GPT-4V on UMAP plots) is presented as a first-of-its-kind replacement for human evaluation.

## Why it matters here
General background on multi-agent LLM orchestration: Planner/Executor/Evaluator separation, hierarchical decision-making, code-sandbox isolation, and self-iterative optimization via MLLM-judged visualizations — directly relevant to designing einstein's own autonomous-loop agent (council dispatch → execute → evaluate → re-plan). No direct arena/math tie; the domain is scRNA-seq, but the architecture patterns inform agent-system design.

## Open questions / connections
- How to extend self-evaluation beyond GPT-4V image judgment to richer optimization targets when users have specific preferences — gestures toward configurable evaluator prompts.
- How to let users register new tools at runtime so the agent aligns with shifting requirements — an open AI-for-science research direction.
- Comparison to MetaGPT-style software-engineering multi-agent frameworks: what biological-domain priors actually buy vs generic agent scaffolding (ablation not reported).

## Key terms
LLM agent, multi-agent framework, Planner-Executor-Evaluator, hierarchical decision-making, self-iterative optimization, GPT-4V multimodal judge, tool retrieval, code sandbox, scRNA-seq, batch correction, cell type annotation, trajectory inference, agent for science, MetaGPT
