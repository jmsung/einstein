---
type: note
kind: paper-relevance
about: 2023-huang-mlagentbench-evaluating-language-agents
canonical: ../../domains/ai-agents/source/2023-huang-mlagentbench-evaluating-language-agents.md
---

# Relevance note — MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation

Canonical distillation: [`2023-huang-mlagentbench-evaluating-language-agents.md`](../../domains/ai-agents/source/2023-huang-mlagentbench-evaluating-language-agents.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Direct prior art for the einstein autonomous-loop scaffold: the Reflection / Research Plan and Status / Fact Check entries are exactly the structural primitives needed to combat the "hallucinate improvement without executing" failure mode that the triple-verify and cycle-discipline rules guard against. The wall the paper hits — long-horizon planning collapse and unrecoverable early-plan errors — is the same wall the einstein loop must survive across 23 problems × many cycles.

## Open questions / connections
- How to detect and recover from "bad plan in early steps" without human intervention — the dominant failure mode and a direct analog of einstein's council-dispatch / question-first guards.
- Fact-checking entry catches hallucinated execution but not hallucinated *interpretation* of a real execution (e.g. the trace shows the agent calling $52.53\% \to 49.34\%$ an "improvement"); a stronger numeric-grounding check is needed.
- Compound Edit Script action is a known leak point (broken diffs land silently); einstein equivalent would be the optimizer-script edit path — needs a syntax/exec-check gate before counting an edit as applied.
- Token + wall-clock cost grows roughly linearly in actions with no clear saturation — informs the cycle-budget question for autonomous loops.
