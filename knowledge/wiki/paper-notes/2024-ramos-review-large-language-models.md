---
type: note
kind: paper-relevance
about: 2024-ramos-review-large-language-models
canonical: ../../domains/ai-agents/source/2024-ramos-review-large-language-models.md
---

# Relevance note — A review of large language models and autonomous agents in chemistry

Canonical distillation: [`2024-ramos-review-large-language-models.md`](../../domains/ai-agents/source/2024-ramos-review-large-language-models.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Useful only as scaffolding for the meta-question of how the Einstein Arena agent itself is built — agent module decomposition (memory/planning/profiling/perception/tools), context-window limits, RAG patterns (PaperQA, WikiCrow), and the agent-authored-content honesty problem that motivates the wiki-attribution rule. No content on sphere packing, kissing numbers, autocorrelation, or any math-optimization problem class.

## Open questions / connections
- How to align LLM agents on non-differentiable downstream scientific metrics (Bou et al., Hayes et al.) — relevant to wiring an agent against arena scores.
- Hallucination + safeguarding tradeoff for autonomous scientific agents (Tang et al. 2024, Ruan et al. sandbox) — informs cycle-discipline rule design.
- Benchmark scarcity: no standard "did the agent improve" metric across cycles, paralleling the `docs/agent/cycle-log.md` honesty-check problem.
