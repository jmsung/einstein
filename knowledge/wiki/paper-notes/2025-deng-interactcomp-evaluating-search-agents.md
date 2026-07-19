---
type: note
kind: paper-relevance
about: 2025-deng-interactcomp-evaluating-search-agents
canonical: ../../domains/ai-agents/source/2025-deng-interactcomp-evaluating-search-agents.md
---

# Relevance note — InteractComp: Evaluating Search Agents With Ambiguous Queries

Canonical distillation: [`2025-deng-interactcomp-evaluating-search-agents.md`](../../domains/ai-agents/source/2025-deng-interactcomp-evaluating-search-agents.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — but methodologically relevant to the einstein agent's `ask-the-question-first` and self-improvement-loop rules: it provides empirical evidence that LLM-based agents systematically under-ask even when clarifying would help, supporting a "force interaction at gap-detect" enforcement pattern rather than relying on voluntary questioning.

## Open questions / connections
- Can RLVR on search outcomes (which the authors propose) be re-purposed to train clarification on internal knowledge-base gaps, not just user intent?
- Forced-interaction helps some models and hurts others — what architectural property predicts who benefits, and does this map onto the council-dispatch personas' "question-not-answer" mandate?
- The calibration↔interaction-rate correlation suggests overconfidence is measurable from CE alone; could a calibration probe be a cheaper proxy than full benchmark eval?
