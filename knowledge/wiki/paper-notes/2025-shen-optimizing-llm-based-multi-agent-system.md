---
type: note
kind: paper-relevance
about: 2025-shen-optimizing-llm-based-multi-agent-system
canonical: ../../domains/ai-agents/source/2025-shen-optimizing-llm-based-multi-agent-system.md
---

# Relevance note — Optimizing LLM-Based Multi-Agent System with Textual Feedback: A Case Study on Software Development

Canonical distillation: [`2025-shen-optimizing-llm-based-multi-agent-system.md`](../../domains/ai-agents/source/2025-shen-optimizing-llm-based-multi-agent-system.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The locator-then-optimizer decomposition is a candidate template for the einstein agent's own self-improvement loop — separating "which step failed" from "how to fix it" mirrors the gap-detect → distill split in the wiki workflow, and the textual-feedback-as-gradient view connects to TextGrad/GEPA-style reflective prompt evolution already in scope.

## Open questions / connections
- Locator accuracy is unmeasured — how often does it blame the wrong agent, and does that error compound across steps?
- Extends TextGrad (Yuksekgonul 2024) by adding a credit-assignment step before optimization; relates to GEPA (Agrawal 2025) and DSPy (Khattab 2024) for prompt search.
- Group optimization risk of overfitting on small training sets (here 5 tasks) is unaddressed; transferability to non-software, open-ended optimization problems (e.g. math wisdom compounding) is untested.
