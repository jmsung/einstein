<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents, ai-reasoning]
title: "CAMEL: Communicative Agents for \"Mind\" Exploration of Large Language Model Society"
authors: [G. Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem]
year: 2023
source_url: https://arxiv.org/abs/2303.17760
drive_file_id: 1qq8plNr5joX4nwYVJiT56sX0mevccD2j
text_source: paperclip
ingested_by: agent
---

# CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society

**Authors:** G. Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.17760

## One-line
A role-playing framework where two LLM agents (an "AI user" task-planner and an "AI assistant" executor) autonomously cooperate through inception prompting to complete tasks from a single human idea, with minimal human supervision.

## Key claim
Carefully engineered symmetric system prompts — assigning roles, forbidding role-flipping, enforcing a fixed `Instruction:`/`Input:`/`Solution:` schema, and using a `<CAMEL_TASK_DONE>` termination token — yield stable autonomous multi-turn cooperation; solutions from CAMEL outperform single-shot `gpt-3.5-turbo` outputs in both GPT-4 and human evaluations, and fine-tuning LLaMA on progressively larger CAMEL-generated datasets shows knowledge emergence on HumanEval / HumanEval+.

## Method
Two `gpt-3.5-turbo` instances are seeded with a preliminary idea and a pair of roles (e.g. Python Programmer × Stock Trader); a task-specifier agent expands the idea into a concrete task. The user agent $U$ emits instructions $I_{t+1} = U(M_t)$ and the assistant $A$ produces solutions $S_{t+1} = A(M_t, I_{t+1})$, with message history $M_{t+1} \leftarrow M_t \cup (I_{t+1}, S_{t+1})$. Stability hinges on "inception prompts" — three templated prompts ($P_T, P_A, P_U$) covering task specification, role assignment, communication protocol, refusal clauses, formatting, and termination. An optional critic-in-the-loop enables tree-search-style decisions.

## Result
The framework produces four large datasets (AI Society, Code, Math, Science) plus a Misalignment set, used both to study cooperative behavior and as fine-tuning data; CAMEL-tuned LLaMA shows monotonic gains on HumanEval/HumanEval+ as dataset size grows. The paper catalogs failure modes that pure prompting must defeat — role-flipping, instruction repetition, flake replies ("I will do something"), and infinite politeness loops — and shows the specific prompt clauses that suppress each.

## Key terms
role-playing agents, inception prompting, multi-agent cooperation, communicative agents, AI alignment, instruction-following, task specifier, role flipping, critic-in-the-loop, LLM society, autonomous cooperation, conversational dataset generation
