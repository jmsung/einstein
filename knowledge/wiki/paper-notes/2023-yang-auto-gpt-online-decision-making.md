---
type: note
kind: paper-relevance
about: 2023-yang-auto-gpt-online-decision-making
canonical: ../../domains/ai-agents/source/2023-yang-auto-gpt-online-decision-making.md
---

# Relevance note — Auto-GPT for Online Decision Making: Benchmarks and Additional Opinions

Canonical distillation: [`2023-yang-auto-gpt-online-decision-making.md`](../../domains/ai-agents/source/2023-yang-auto-gpt-online-decision-making.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant to agent-architecture design rather than math: the "additional opinions" idea (cheap expert sampling top-$k$ candidates, LLM as final judge) is the closest published analog to this repo's [council-dispatch](.claude/rules/council-dispatch.md) (multiple personas write questions, LLM synthesizes) and could inform how to wire IL/heuristic suggesters into the autonomous loop being built on this branch.

## Open questions / connections
- Does the additional-opinions boost survive when the "experts" are weak symbolic heuristics (e.g., rule-based optimizer hints) rather than trained IL models? Relevant for council-style multi-persona dispatch.
- Why does GPT-3.5 collapse on repetitive/bad opinions while GPT-4 filters them — is robustness to adversarial expert noise a capability threshold or a prompting artifact?
- Extends Reflexion [Shinn 2023] and ReAct [Yao 2022]; sits alongside HuggingGPT / TaskMatrix.ai for tool-augmented agents but uniquely studies *advisory* (not delegated) expert integration.
