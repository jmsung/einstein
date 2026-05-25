---
type: source
kind: paper
title: DeepEye: A Steerable Self-driving Data Agent System
authors: Boyan Li, Yiran Peng, Yupeng Xie, Sirong Lu, Yizhang Zhu, Xing Mu, Xinyu Liu, Yuyu Luo
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.28889
source_local: ../raw/2026-li-deepeye-steerable-self-driving-data.pdf
topic: general-knowledge
cites: 
---

# DeepEye: A Steerable Self-driving Data Agent System

**Authors:** Boyan Li, Yiran Peng, Yupeng Xie, Sirong Lu, Yizhang Zhu, Xing Mu, Xinyu Liu, Yuyu Luo  ·  **Year:** 2026  ·  **Source:** https://arxiv.org/abs/2603.28889

## One-line
A workflow-centric LLM data-agent system that compiles user intents into validated, optimized DAGs of AgentNodes and ToolNodes for multimodal data analysis.

## Key claim
A database-inspired workflow engine (Compiler / Validator / Optimizer / Executor) plus context-isolated hierarchical reasoning produces more reliable, parallelizable, and transparent data-analysis agents than linear "ChatBI" pipelines — demonstrated on a "Global Sales Performance Analysis" case.

## Method
Formalize every capability as a 5-tuple node $N = \langle D, I, O, C, \Phi \rangle$ split into deterministic ToolNodes ($O = f_{code}(I, C)$) and probabilistic AgentNodes ($O \sim P(\cdot \mid I, C, W_{local}, T_{internal})$) with private context windows. A memory-augmented planner retrieves SOP templates from a vector knowledge base to synthesize a logical DAG; the engine then runs cycle-detection (DFS), schema-consistency checks, Kahn's-algorithm topological layering for parallel execution, and Celery/Redis-backed asynchronous dispatch with feedback-driven re-planning.

## Result
No quantitative benchmarks — this is a SIGMOD demo paper. The reported result is the working system: unified multimodal orchestration across SQL DBs / files / knowledge bases, context isolation that mitigates "context explosion" in single-agent setups, runtime parallelization of independent subtasks (e.g., document search + DB read in the same layer), and human-in-the-loop inspection/editing with static Validator-caught schema mismatches.

## Why it matters here
General background; no direct arena tie. The DAG-with-static-validation + context-isolated sub-agents pattern is loosely analogous to the einstein repo's council-dispatch + self-improvement-loop architecture (planner over isolated persona subagents, gap-detect feedback, SOP-style finding reuse), but DeepEye targets BI workflows rather than math optimization.

## Open questions / connections
- Could the einstein autonomous loop adopt a Validator/Optimizer stage between `/goal` and `/act` to catch malformed plans (missing wiki cites, unrouted compute) before execution?
- Kahn's-algorithm parallel layering could apply to council dispatch and multi-problem optimizer runs — independent personas / problems already run in parallel but without explicit DAG accounting.
- Auto-archiving successful workflows as SOPs mirrors the skill-library promotion mechanism; worth comparing the promotion criteria.

## Key terms
data agents, LLM orchestration, workflow DAG, AgentNode, ToolNode, context isolation, hierarchical reasoning, Kahn's algorithm, topological scheduling, retrieval-augmented planning, multimodal analysis, Text-to-SQL, SIGMOD demo, ChatBI
