---
type: note
kind: paper-relevance
about: 2024-hu-nova-iterative-planning-search
canonical: ../../domains/ai-agents/source/2024-hu-nova-iterative-planning-search.md
---

# Relevance note — Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas

Canonical distillation: [`2024-hu-nova-iterative-planning-search.md`](../../domains/ai-agents/source/2024-hu-nova-iterative-planning-search.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The "plan-which-knowledge-to-retrieve before retrieving" pattern is structurally similar to the einstein agent's wiki-first + council-dispatch + self-improvement loop, and the Swiss-tournament pairwise ranking is a candidate template for ranking competing optimizer ideas when no analytical ground truth exists.

## Open questions / connections
- No reward model on the planning step — authors flag this as a limitation; analogous to council dispatch lacking an explicit utility for "which question to ask next".
- Iteration plateau at $T{=}3$: why does novelty saturate? Maps to the einstein loop's "same gap re-learned next cycle" failure mode.
- Pairwise Swiss-tournament ranking (5 rounds × Claude-3.5-Sonnet) reported as more reliable than direct scoring — potentially reusable for ranking dead-end findings or candidate techniques in `docs/agent/skill-library.md`.
