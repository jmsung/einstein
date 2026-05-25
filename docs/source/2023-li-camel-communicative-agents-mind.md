---
type: source
kind: paper
title: "CAMEL: Communicative Agents for \"Mind\" Exploration of Large Language Model Society"
authors: G. Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, Bernard Ghanem
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2303.17760
source_local: ../raw/2023-li-camel-communicative-agents-mind.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie — CAMEL is multi-agent NLP infrastructure, not math. Loosely relevant to the council-dispatch rule (multiple personas as instruction-following agents writing questions), and to autonomous-loop design (termination tokens, refusal-on-incapability, fixed schema) — its catalog of cooperative-prompting failure modes maps directly onto risks the einstein autonomous loop must engineer around.

## Open questions / connections
- Does inception-prompting stability degrade under longer horizons (the paper's tasks are short; arena-style multi-cycle compute campaigns are not tested)?
- Critic-in-the-loop is mentioned but not quantitatively benchmarked — what is the marginal value of a critic agent for math-style verification problems?
- Extends Self-Instruct [Wang 2022] and Unnatural-Instruction [Honovich 2022] to *conversational* instruction generation; could analogous role-play generate triple-verify-style cross-checking dialogues?

## Key terms
role-playing agents, inception prompting, multi-agent cooperation, communicative agents, AI alignment, instruction-following, task specifier, role flipping, critic-in-the-loop, LLM society, autonomous cooperation, conversational dataset generation
