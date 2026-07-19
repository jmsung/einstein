---
type: note
kind: paper-relevance
about: 2023-qian-chatdev-communicative-agents-software
canonical: ../../domains/ai-agents/source/2023-qian-chatdev-communicative-agents-software.md
---

# Relevance note — ChatDev: Communicative Agents for Software Development

Canonical distillation: [`2023-qian-chatdev-communicative-agents-software.md`](../../domains/ai-agents/source/2023-qian-chatdev-communicative-agents-software.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is a multi-agent-LLM software-engineering framework, not a math-optimization result. It is conceptually adjacent to the einstein agent's [council-dispatch](.claude/rules/council-dispatch.md) and [self-improvement-loop](.claude/rules/self-improvement-loop.md): both use role-prompted LLM personas in a chained workflow, and ChatDev's dehallucination ("ask before answering") echoes the [ask-the-question-first](.claude/rules/ask-the-question-first.md) rule.

## Open questions / connections
- Does "role reversal before answering" (dehallucination) transfer to math personas — would Tao/Gauss/Erdős proxies produce sharper questions if forced to request missing context first?
- ChatDev's chain is a strict DAG of subtasks; could the einstein math-solving protocol benefit from a similarly explicit chain (understand → wiki-first → council → research → distill → execute) with enforced solution-passing between phases instead of free-form context?
- Evaluation gap: ChatDev measures Completeness/Executability/Consistency because per-task unit tests don't exist; einstein has triple-verify scores — the comparable question is whether a multi-agent workflow improves *score* over a single-agent run on the same compute budget.
- Token/time overhead is acknowledged as a limitation — relevant when designing the autonomous-loop council-dispatch budget.
