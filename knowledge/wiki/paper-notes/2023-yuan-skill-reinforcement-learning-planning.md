---
type: note
kind: paper-relevance
about: 2023-yuan-skill-reinforcement-learning-planning
canonical: ../../domains/ai-agents/source/2023-yuan-skill-reinforcement-learning-planning.md
---

# Relevance note — Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks

Canonical distillation: [`2023-yuan-skill-reinforcement-learning-planning.md`](../../domains/ai-agents/source/2023-yuan-skill-reinforcement-learning-planning.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The paper is about hierarchical RL + LLM planning for Minecraft, not math optimization — it shares no concepts with sphere packing, autocorrelation, kissing numbers, sieves, or extremal combinatorics. The only loose analogy is the *self-improvement-loop / council-dispatch / skill-library* architecture in this repo: Plan4MC's skill-graph + DFS planner is a structural cousin to the einstein agent's wiki-graph + gap-detector pipeline, but the techniques don't transfer to numerical optimization.

## Open questions / connections
- Can the "fine-grained basic skills + dependency graph" pattern be ported to a numerical-optimizer agent (techniques as nodes, preconditions as edges)? Speculative — needs a different cost model than item inventories.
- Plan4MC still needs human correction on ~11% of LLM-generated graph nodes — what does an automated verifier for graph correctness look like?
- Relates to Go-Explore (Ecoffet et al.) for exploration bootstrapping and to LLM-as-planner work (SayCan, Voyager, DEPS); does not relate to any cited paper in `knowledge/wiki/`.
