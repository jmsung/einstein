---
type: note
kind: paper-relevance
about: 2026-yun-graph-of-agents-graph-based-framework-multi-agent
canonical: ../../domains/ai-agents/source/2026-yun-graph-of-agents-graph-based-framework-multi-agent.md
---

# Relevance note — Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration

Canonical distillation: [`2026-yun-graph-of-agents-graph-based-framework-multi-agent.md`](../../domains/ai-agents/source/2026-yun-graph-of-agents-graph-based-framework-multi-agent.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Possibly relevant to council-dispatch design (3–5 personas writing questions) — GoA's empirical finding that a *selected, structured* subset of 3 agents beats an undirected pool of 6 supports the einstein council's "pick personas by category, don't dispatch all" heuristic, and the directional refine→feedback message-passing pattern is a candidate refinement for how persona outputs interact.

## Open questions / connections
- Can relevance-weighted directed message passing improve council-dispatch (Source = topic-matched persona like Viazovska for sphere packing; Target = generalist Tao/Polya) vs the current parallel-independent dispatch?
- Does the $k=3$ vs $k=6$ result generalize to math-reasoning specialists (vs the generic LLM specialists tested), or is the gain mostly from filtering out clearly-irrelevant agents (Legal/Finance on anatomy)?
- Extends MoA (Wang et al. 2024), DyLAN (Liu et al. 2024), GPTSwarm (Zhuge et al. 2024) — dynamic relevance-driven topology vs static DAG or symmetric debate.
