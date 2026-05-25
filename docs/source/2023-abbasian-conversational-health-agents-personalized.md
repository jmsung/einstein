---
type: source
kind: paper
title: "Conversational Health Agents: A Personalized LLM-Powered Agent Framework"
authors: Mahyar Abbasian, Iman Azimi, Amir M. Rahmani, Ramesh C. Jain
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2310.02374
source_local: ../raw/2023-abbasian-conversational-health-agents-personalized.pdf
topic: general-knowledge
cites:
---

# Conversational Health Agents: A Personalized LLM-Powered Agent Framework

**Authors:** Mahyar Abbasian, Iman Azimi, Amir M. Rahmani, Ramesh C. Jain  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2310.02374

## One-line
Proposes openCHA, an open-source LLM-powered agent framework that orchestrates external data sources, knowledge bases, and analysis models to deliver personalized, multimodal healthcare conversations.

## Key claim
A central LLM-driven Orchestrator (Task Planner + Task Executor + Data Pipe + Promptist + Response Generator) can decompose a healthcare query into a sequence of tool calls, execute them against external APIs, and synthesize a personalized response — overcoming the four standing limitations of CHAs (no personalization, no fresh knowledge, no tool integration, no multi-step reasoning).

## Method
Service-based agent architecture in which the Task Planner uses Tree-of-Thought (or ReAct) prompting to generate three candidate task-sequence strategies, weighs pros/cons, and selects one; the Task Executor then translates the chosen plan into `execute_task(name, [inputs])` Python calls, with intermediate results parked in a Data Pipe keyed by UUID. The Response Generator runs a separate "mega-prompt" constrained to use only the Thinker (task-result) context, not the LLM's internal knowledge.

## Result
A working framework (released at github.com/Institute4FutureHealth/CHA) with two demos and four use cases — patient sleep/HRV reporting, stress estimation from PPG, nutrition recommendation, and multilingual diabetes Q&A — showing correct task sequencing for queries like "How to improve my sleep?" (google_search → extract_text) and "Estimate stress for par_5 in Aug 2020" (affect_ppg_get → affect_ppg_analysis → affect_stress_analysis). No quantitative benchmark; the contribution is the architecture itself.

## Why it matters here
General background; no direct arena tie. The architectural pattern (LLM planner + tool executor + typed task registry + intermediate-result data pipe) is relevant as a reference design for the autonomous-loop agent's own orchestration layer, but the paper contributes nothing to sphere packing, autocorrelation, kissing numbers, or any Einstein Arena problem class.

## Open questions / connections
- Tree-of-Thought vs ReAct vs Plan-and-Solve as planning backbones — which planning style produces fewer wasted tool calls on long multi-step math workflows?
- Data-Pipe-by-UUID pattern as a way to handle large intermediate artifacts (e.g., solution JSONs, raw multistart outputs) without blowing the planner's context window.
- Separation of Task Planner LLM from Response Generator LLM (different models, different prompts) as a possible split for "compute-heavy planning" vs "narrative wiki-writing" in the cycle loop.

## Key terms
conversational health agent, openCHA, LLM agent framework, Tree of Thought, ReAct prompting, task planner, task executor, data pipe, orchestrator, tool calling, multimodal LLM, personalized healthcare
