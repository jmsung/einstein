<!-- synced from knowledge-base — do not edit here; change upstream and re-pull -->
---
type: source
kind: paper
confidentiality: public
visibility: global
primary: ai-agents
domains: [ai-agents]
title: Building Living Software Systems with Generative & Agentic AI
authors: [Jules White]
year: 2024
source_url: https://arxiv.org/abs/2408.01768
drive_file_id: TODO
text_source: paperclip
ingested_by: agent
---

# Building Living Software Systems with Generative & Agentic AI

**Authors:** Jules White  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2408.01768

## One-line
Opinion paper arguing that generative and agentic AI can replace static, brittle software with "living software systems" that translate human goals directly into API actions.

## Key claim
Software engineering is fundamentally a chain of lossy translations (requirements → code → UI → user mental model), and large language models — built as translators — can collapse this chain by letting users state goals in natural language while an agent dispatches actions over APIs, with prompts/conversations becoming the new intellectual property instead of code.

## Method
Conceptual / position paper, not technical. Two implementation pathways are sketched: (1) using generative AI to accelerate traditional software development (now ~40% of GitHub code per cited estimate), and (2) using agentic AI with system/root prompts plus exposed APIs as tools to dynamically translate goals into action sequences (illustrated with a Thought/Action/Action-Details format for an email client, similar to ReAct-style scaffolding and OpenAI Custom GPTs).

## Result
No theorems or numerical bounds. Establishes a vocabulary — "living software systems," translation-as-core-problem, prompt-as-program, context-as-first-class-input — and argues that prompt engineering is "AI leadership + problem decomposition," not word-choice tweaking. Argues hallucinations are managed by the same fact-checking processes used for human interns (e.g., supplying sources and demanding `[X]` citations in output), not by abolishing the agent.

## Key terms
generative AI, agentic AI, large language models, LLM, prompt engineering, living software systems, translation problem, system prompt, root prompt, Custom GPTs, API tool use, ReAct, Jules White
