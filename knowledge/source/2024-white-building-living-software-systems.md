---
type: source
kind: paper
title: Building Living Software Systems with Generative & Agentic AI
authors: Jules White
year: 2024
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2408.01768
source_local: ../raw/2024-white-building-living-software-systems.pdf
topic: general-knowledge
cites:
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

## Why it matters here
General background; no direct arena tie. Loosely relevant to how the autonomous-loop agent itself is architected — framing the council/self-improvement loop as a translation+context system, and reinforcing why prompts/conversations (questions in `knowledge/wiki/questions/`) are the durable artifact rather than transient code. No mathematical content for sphere packing, kissing numbers, autocorrelation, etc.

## Open questions / connections
- How to fact-check agent-authored wiki pages systematically (analogue of the source-citation prompt pattern) — ties to the [[wiki-attribution]] rule.
- What "context" should be passed to per-problem council dispatch beyond strategy.md and SOTA solutions — the paper's argument that context is the missing ingredient.
- Reliability/speed limits ("won't fly a plane") suggest where to draw the line between agentic loops and deterministic optimizer code in this repo.

## Key terms
generative AI, agentic AI, large language models, LLM, prompt engineering, living software systems, translation problem, system prompt, root prompt, Custom GPTs, API tool use, ReAct, Jules White
