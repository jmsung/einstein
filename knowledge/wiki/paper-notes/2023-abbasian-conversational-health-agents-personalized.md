---
type: note
kind: paper-relevance
about: 2023-abbasian-conversational-health-agents-personalized
canonical: ../../domains/ai-agents/source/2023-abbasian-conversational-health-agents-personalized.md
---

# Relevance note — Conversational Health Agents: A Personalized LLM-Powered Agent Framework

Canonical distillation: [`2023-abbasian-conversational-health-agents-personalized.md`](../../domains/ai-agents/source/2023-abbasian-conversational-health-agents-personalized.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The architectural pattern (LLM planner + tool executor + typed task registry + intermediate-result data pipe) is relevant as a reference design for the autonomous-loop agent's own orchestration layer, but the paper contributes nothing to sphere packing, autocorrelation, kissing numbers, or any Einstein Arena problem class.

## Open questions / connections
- Tree-of-Thought vs ReAct vs Plan-and-Solve as planning backbones — which planning style produces fewer wasted tool calls on long multi-step math workflows?
- Data-Pipe-by-UUID pattern as a way to handle large intermediate artifacts (e.g., solution JSONs, raw multistart outputs) without blowing the planner's context window.
- Separation of Task Planner LLM from Response Generator LLM (different models, different prompts) as a possible split for "compute-heavy planning" vs "narrative wiki-writing" in the cycle loop.
