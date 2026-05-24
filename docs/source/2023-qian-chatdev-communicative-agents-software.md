---
type: source
kind: paper
title: "ChatDev: Communicative Agents for Software Development"
authors: Cheng Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, X. Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2307.07924
source_local: ../raw/2023-qian-chatdev-communicative-agents-software.pdf
topic: general-knowledge
cites:
---

# ChatDev: Communicative Agents for Software Development

**Authors:** Cheng Qian, Wei Liu, Hongzhang Liu, Nuo Chen, Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen, Yusheng Su, X. Cong, Juyuan Xu, Dahai Li, Zhiyuan Liu, Maosong Sun  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2307.07924

## One-line
A multi-agent LLM framework that decomposes software development into role-played design / coding / testing subtasks linked by a "chat chain" and a dehallucination communication protocol.

## Key claim
Structuring LLM agents into a chain of paired instructor–assistant dialogues (CEO/CTO/programmer/reviewer/tester) with a "communicative dehallucination" pattern improves software completeness, executability, and consistency over single-agent (GPT-Engineer) and prior multi-agent (MetaGPT) baselines — reaching Executability $0.88$ vs $0.36$–$0.41$, and overall Quality $0.40$ vs $0.14$–$0.15$ on the 1,200-task SRDD benchmark.

## Method
A chat chain $C = \langle P_1, \dots, P_{|C|}\rangle$ segments development into sequential phases (design → code-write → code-complete → code-review → testing), each further split into subtasks $T^j$. In each subtask two LLM-instantiated roles (instructor $I$, assistant $A$, induced via system-prompt "inception" $\rho(\text{LLM}, P_I)$) hold a multi-turn dialogue with short-term memory $M^t_i = \langle(I^1_i, A^1_i),\dots\rangle$ within a phase and long-term memory passing only the extracted solutions $\tau(M^{|M_j|}_j)$ between phases. "Communicative dehallucination" inverts the usual $\langle I\to A, A\to I\rangle$ pattern into $\langle I\to A, \langle A\to I, I\to A\rangle, A\to I\rangle$ so the assistant proactively asks for missing specifics (e.g., dependency name, class signature) before committing code.

## Result
On SRDD (1,200 prompts, 5 categories × 40 subcategories × 30 each), ChatDev beats GPT-Engineer and MetaGPT on Completeness ($0.56$), Executability ($0.88$), Consistency ($0.80$), and integrated Quality ($0.40$); GPT-4 and human win-rate evaluations agree. Ablations show removing role assignments has the largest negative effect (defaults to command-line-only programs, shallow reviews); removing the testing phase tanks Executability; removing dehallucination uniformly drops all metrics. Communication-content analysis: 57.2% natural-language exchange concentrated in design; code reviews are dominated by "Method Not Implemented" (34.85%) and "Module Not Imported" issues; testing-phase errors are led by `ModuleNotFoundError` (45.76%), `NameError` and `ImportError` (15.25% each), with multi-turn iteration monotonically driving the population toward compile-success.

## Why it matters here
General background; no direct arena tie — this is a multi-agent-LLM software-engineering framework, not a math-optimization result. It is conceptually adjacent to the einstein agent's [council-dispatch](.claude/rules/council-dispatch.md) and [self-improvement-loop](.claude/rules/self-improvement-loop.md): both use role-prompted LLM personas in a chained workflow, and ChatDev's dehallucination ("ask before answering") echoes the [ask-the-question-first](.claude/rules/ask-the-question-first.md) rule.

## Open questions / connections
- Does "role reversal before answering" (dehallucination) transfer to math personas — would Tao/Gauss/Erdős proxies produce sharper questions if forced to request missing context first?
- ChatDev's chain is a strict DAG of subtasks; could the einstein math-solving protocol benefit from a similarly explicit chain (understand → wiki-first → council → research → distill → execute) with enforced solution-passing between phases instead of free-form context?
- Evaluation gap: ChatDev measures Completeness/Executability/Consistency because per-task unit tests don't exist; einstein has triple-verify scores — the comparable question is whether a multi-agent workflow improves *score* over a single-agent run on the same compute budget.
- Token/time overhead is acknowledged as a limitation — relevant when designing the autonomous-loop council-dispatch budget.

## Key terms
LLM agents, multi-agent collaboration, chat chain, communicative dehallucination, inception prompting, role-playing agents, waterfall model, instructor-assistant dialogue, short-term memory, long-term memory, coding hallucination, software development, GPT-Engineer, MetaGPT, SRDD benchmark, ChatDev
