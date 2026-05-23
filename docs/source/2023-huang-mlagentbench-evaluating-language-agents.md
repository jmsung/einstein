---
type: source
kind: paper
title: MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation
authors: Qian Huang, Jian Vora, Percy Liang, J. Leskovec
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2310.03302
source_local: ../raw/2023-huang-mlagentbench-evaluating-language-agents.pdf
topic: general-knowledge
cites:
---

# MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation

**Authors:** Qian Huang, Jian Vora, Percy Liang, J. Leskovec  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2310.03302

## One-line
A benchmark of 13 ML experimentation tasks with a ReAct-style LM agent that reads/writes files, executes code, and iterates on model performance against a $10\%$ improvement-over-baseline success criterion.

## Key claim
A Claude v3 Opus agent built on a ReAct-style scaffold (Reflection / Research Plan and Status / Fact Check / Thought / Action) achieves the highest average success rate of $37.5\%$ across the 13 tasks, ranging from $100\%$ on house-price to $0\%$ on BabyLM, Parkinson's-disease, fathomnet, vectorization, and other recent challenges.

## Method
LM-based agent with prompt template that forces structured rationale ($r_t$) before action ($a_t$): reflection, multi-step research plan with status annotations, fact-checking entry (mitigates hallucinated-improvement), then ReAct-style thought + action. Action space mixes primitive file/exec ops (List/Read/Write/Append/Copy/Inspect/Undo/Execute/FinalAnswer) with compound LM-backed actions (Understand File, Edit Script, Edit Script Segment). Memory $m_t = (o_{<t}, r_{<t})$ with a sliding window of the last 3 steps in the prompt; loop until Final Answer or hit max 50 actions / 5 hours.

## Result
Across 8 runs per task, Claude v3 Opus tops 5/13 tasks; GPT-4-turbo and Claude v2.1 tie at $26.0\%$ average success; GPT-4 $19.2\%$; Gemini Pro $3.8\%$; Mixtral $10.4\%$. Failure-mode taxonomy on CIFAR-10 traces: hallucination, bad plan (usually early, unrecoverable), response-format error, submission-format error. Performance often regresses over longer horizons (except Claude v3 Opus). Compound "Edit Script" actions sometimes produce syntactically wrong patches (e.g. `nn.Conv2d(3, 6, 5) + nn.Dropout(0.5)` injected as an expression instead of a new layer) — invisible to the agent until execution.

## Why it matters here
Direct prior art for the einstein autonomous-loop scaffold: the Reflection / Research Plan and Status / Fact Check entries are exactly the structural primitives needed to combat the "hallucinate improvement without executing" failure mode that the triple-verify and cycle-discipline rules guard against. The wall the paper hits — long-horizon planning collapse and unrecoverable early-plan errors — is the same wall the einstein loop must survive across 23 problems × many cycles.

## Open questions / connections
- How to detect and recover from "bad plan in early steps" without human intervention — the dominant failure mode and a direct analog of einstein's council-dispatch / question-first guards.
- Fact-checking entry catches hallucinated execution but not hallucinated *interpretation* of a real execution (e.g. the trace shows the agent calling $52.53\% \to 49.34\%$ an "improvement"); a stronger numeric-grounding check is needed.
- Compound Edit Script action is a known leak point (broken diffs land silently); einstein equivalent would be the optimizer-script edit path — needs a syntax/exec-check gate before counting an edit as applied.
- Token + wall-clock cost grows roughly linearly in actions with no clear saturation — informs the cycle-budget question for autonomous loops.

## Key terms
ReAct agent, LM-based agent, MLAgentBench, research plan and status, fact-check entry, hallucination failure mode, long-horizon planning, autonomous experimentation, Reflexion, AutoGPT, Claude v3 Opus, success rate benchmark
