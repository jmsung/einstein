---
type: source
kind: paper
title: X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs
authors: Rui Ye, Xiangrui Liu, Qimin Wu, Xianghe Pang, Zhenfei Yin, Lei Bai, Siheng Chen
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2505.16997
source_local: ../raw/2025-ye-x-mas-towards-building-multi-agent.pdf
topic: general-knowledge
cites:
---

# X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs

**Authors:** Rui Ye, Xiangrui Liu, Qimin Wu, Xianghe Pang, Zhenfei Yin, Lei Bai, Siheng Chen  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2505.16997

## One-line
Benchmarks 27 LLMs across 5 multi-agent-system (MAS) functions × 5 domains and shows that assigning *different* LLMs to different agent roles (heterogeneous MAS) beats single-model MAS without any structural change.

## Key claim
Replacing the uniform LLM driver of an existing MAS (AgentVerse, LLM-Debate, DyLAN, X-MAS-Proto) with per-role optimal LLMs picked from X-MAS-Bench yields consistent gains: up to $+8.4\%$ on MATH in chatbot-only mode, and in mixed chatbot+reasoner mode AgentVerse jumps $20\% \to 50\%$ and DyLAN $40\% \to 63\%$ on AIME2024 (a $\sim 47\%$ absolute boost). No single LLM is best across all 25 function-domain cells.

## Method
X-MAS-Bench decomposes agent behavior into 5 standardized functions — **question-answering, revise, aggregation, planning, evaluation** — each tested under fixed prompts so only the examined LLM varies; ~1.7M evaluations across 27 LLMs × 21 datasets identify per-cell top performers. X-MAS-Design then keeps the original MAS topology and prompts but substitutes the top-performing LLM (from the bench) into each (role, domain) slot; selection takes <1 minute per MAS and could be automated by a small LLM.

## Result
Heterogeneous MAS beats every homogeneous baseline on average across 4 MAS methods and 5 domains (e.g., DyLAN 65.9 vs best-homogeneous 62.7). Findings: (1) smaller specialized models (e.g., Qwen2.5-7B in revise-coding 79.2 > Qwen2.5-72B 77.3) sometimes win; (2) a single LLM's performance varies wildly across function/domain cells; (3) increasing the candidate-LLM pool gives monotone gains; (4) reasoner-only MAS often *underperforms* chatbot-only, but chatbot+reasoner heterogeneous mixes win big — planner=chatbot, solver/critic/evaluator=reasoner is a recurring pattern.

## Why it matters here
General background; no direct arena tie — but directly relevant to **council-dispatch** and **self-improvement-loop** design: a math-solving agentic council should heterogeneously assign roles (e.g., chatbot for planner/role-assigner, reasoner for solver/critic/aggregator) rather than running one model everywhere. The function decomposition (QA / revise / aggregation / planning / evaluation) maps cleanly onto the einstein protocol's persona/synthesis/verify stages.

## Open questions / connections
- Automated (vs manual) per-role LLM selection — current X-MAS-Design is human-picked; can a router LLM learn this from problem features?
- Does the chatbot-planner + reasoner-solver pattern transfer to *math research* tasks (e.g., sphere packing, autocorrelation) where ground truth is a continuous score, not a multiple-choice answer?
- Extends MoA [Wang 2025], ReConcile [Chen 2024], MASRouter [Yue 2025], LLM-Blender [Jiang 2023] — those involve all candidates or learn routing for one framework; X-MAS provides framework-agnostic empirical selection.
- Open: scalability to >27 LLMs, cost-aware selection (some 7B specialists beat 72B generalists → cheaper MAS possible).

## Key terms
multi-agent system, heterogeneous LLMs, X-MAS-Bench, X-MAS-Design, agent role assignment, LLM-Debate, AgentVerse, DyLAN, MetaGPT, mixture-of-agents, planner-solver-evaluator-reviser-aggregator, chatbot vs reasoner, DeepSeek-R1, QwQ-32B, AIME2024, MATH benchmark, collective intelligence, council dispatch
