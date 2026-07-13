<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs"
authors: [Rui Ye, Xiangrui Liu, Qimin Wu, Xianghe Pang, Zhenfei Yin, Lei Bai, Siheng Chen]
year: 2025
source_url: https://arxiv.org/abs/2505.16997
drive_file_id: 1_kWhKsSk0XFDdUAyusE0SmdbiHrThA5h
text_source: paperclip
ingested_by: agent
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

## Key terms
multi-agent system, heterogeneous LLMs, X-MAS-Bench, X-MAS-Design, agent role assignment, LLM-Debate, AgentVerse, DyLAN, MetaGPT, mixture-of-agents, planner-solver-evaluator-reviser-aggregator, chatbot vs reasoner, DeepSeek-R1, QwQ-32B, AIME2024, MATH benchmark, collective intelligence
