<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, bio-clinical]
title: "Conversational Health Agents: A Personalized LLM-Powered Agent Framework"
authors: [Mahyar Abbasian, Iman Azimi, Amir M. Rahmani, Ramesh C. Jain]
year: 2023
source_url: https://arxiv.org/abs/2310.02374
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
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

## Key terms
conversational health agent, openCHA, LLM agent framework, Tree of Thought, ReAct prompting, task planner, task executor, data pipe, orchestrator, tool calling, multimodal LLM, personalized healthcare
