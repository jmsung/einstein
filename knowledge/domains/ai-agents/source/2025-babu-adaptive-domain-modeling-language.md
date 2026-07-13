<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: Adaptive Domain Modeling with Language Models: A Multi-Agent Approach to Task Planning
authors: [Harisankar Babu, Philipp Schillinger, Tamim Asfour]
year: 2025
source_url: https://arxiv.org/abs/2506.19592
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Adaptive Domain Modeling with Language Models: A Multi-Agent Approach to Task Planning

**Authors:** Harisankar Babu, Philipp Schillinger, Tamim Asfour  ·  **Year:** 2025  ·  **Source:** https://arxiv.org/abs/2506.19592

## One-line
TAPAS is a multi-LLM-agent framework that dynamically generates and adapts symbolic planning domains (types, fluents, actions) from natural-language task descriptions, bridging LLM flexibility with classical planner rigor.

## Key claim
A modular three-agent system (Domain / Initial-State / Goal-State generators) with structured tool-call feedback can autonomously extend PDDL-style domains to novel attributes (color, size, battery) without manual redefinition, achieving 88.42% average solve rate across seven LLM+P benchmark domains using GPT-4o.

## Method
Three specialized LLM agents collaboratively build a Unified Planning (UP) problem in Python: downstream agents detect missing fluents/objects and invoke structured tools (`missing_or_incorrect_fluent`, `action_modification`, `missing_objects`) to request upstream modifications. Each agent uses a self-reflection loop with an LLM critic scoring $\sigma \in [0,1]$ against threshold $\tau$, plus short-term context memory and a cosine-similarity-retrieved procedural memory $\text{score}(q,s_i)=e_q\cdot e_{s_i}/\|e_q\|\|e_{s_i}\|$. Execution uses a RAG-assisted solver-debugger, NL plan abstraction, and a ReAct-style Action Executor + Validator pair.

## Result
On seven LLM+P domains (20 problems each, GPT-4o, temp=0.0): Barman 97%, Blocksworld 100%, Floortile 57%, Grippers 100%, Storage 90%, Termes 95%, Tyreworld 80%. Adaptability tests: color-goal blocksworld 100%, size-goal (modifies stack precondition to $(<\text{size}(b_1)\,\text{size}(b_2))$) 90%, battery-grippers 100%, battery-floortile 70%. Claude 3.7 Sonnet matched GPT-4o; smaller models (GPT-4o-mini, Mistral Large, Cohere Command-R) degraded sharply. Temperature 0.1 slightly beat 0.0 (92.42% avg); 0.3 hurt (83.57%).

## Key terms
LLM task planning, PDDL, Unified Planning framework, multi-agent LLM, ReAct, tool calling, domain modeling, neuro-symbolic planning, self-reflection critic, procedural memory, RAG debugger, VirtualHome, LLM+P benchmark, adaptive domain extension
