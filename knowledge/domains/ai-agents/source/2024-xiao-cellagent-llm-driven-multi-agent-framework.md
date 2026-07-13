<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-multiomics]
title: "CellAgent: An LLM-driven Multi-Agent Framework for Automated Single-cell Data Analysis"
authors: [Yihang Xiao, Jinyi Liu, Yan Zheng, Xiaohan Xie, Jianye Hao, Mingzhi Li, Ruitao Wang, Fei Ni, Yuxiao Li, Jintian Luo, Shaoqing Jiao, Jiajie Peng]
year: 2024
source_url: https://arxiv.org/abs/2407.09811
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
LLM agent, multi-agent framework, Planner-Executor-Evaluator, hierarchical decision-making, self-iterative optimization, GPT-4V multimodal judge, tool retrieval, code sandbox, scRNA-seq, batch correction, cell type annotation, trajectory inference, agent for science, MetaGPT
