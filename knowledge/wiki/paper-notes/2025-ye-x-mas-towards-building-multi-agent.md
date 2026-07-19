---
type: note
kind: paper-relevance
about: 2025-ye-x-mas-towards-building-multi-agent
canonical: ../../domains/ai-agents/source/2025-ye-x-mas-towards-building-multi-agent.md
---

# Relevance note — X-MAS: Towards Building Multi-Agent Systems with Heterogeneous LLMs

Canonical distillation: [`2025-ye-x-mas-towards-building-multi-agent.md`](../../domains/ai-agents/source/2025-ye-x-mas-towards-building-multi-agent.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — but directly relevant to **council-dispatch** and **self-improvement-loop** design: a math-solving agentic council should heterogeneously assign roles (e.g., chatbot for planner/role-assigner, reasoner for solver/critic/aggregator) rather than running one model everywhere. The function decomposition (QA / revise / aggregation / planning / evaluation) maps cleanly onto the einstein protocol's persona/synthesis/verify stages.

## Open questions / connections
- Automated (vs manual) per-role LLM selection — current X-MAS-Design is human-picked; can a router LLM learn this from problem features?
- Does the chatbot-planner + reasoner-solver pattern transfer to *math research* tasks (e.g., sphere packing, autocorrelation) where ground truth is a continuous score, not a multiple-choice answer?
- Extends MoA [Wang 2025], ReConcile [Chen 2024], MASRouter [Yue 2025], LLM-Blender [Jiang 2023] — those involve all candidates or learn routing for one framework; X-MAS provides framework-agnostic empirical selection.
- Open: scalability to >27 LLMs, cost-aware selection (some 7B specialists beat 72B generalists → cheaper MAS possible).
