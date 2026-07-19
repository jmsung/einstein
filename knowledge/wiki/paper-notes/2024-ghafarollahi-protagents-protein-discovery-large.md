---
type: note
kind: paper-relevance
about: 2024-ghafarollahi-protagents-protein-discovery-large
canonical: ../../domains/ai-agents/source/2024-ghafarollahi-protagents-protein-discovery-large.md
---

# Relevance note — ProtAgents: protein discovery via large language model multi-agent collaborations combining physics and machine learning

Canonical distillation: [`2024-ghafarollahi-protagents-protein-discovery-large.md`](../../domains/ai-agents/source/2024-ghafarollahi-protagents-protein-discovery-large.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The paper's relevance is methodological — it is a concrete example of an LLM multi-agent loop (planner / assistant / critic / user_proxy) coordinating physics tools and generative models autonomously, which parallels the einstein agent's council-dispatch + self-improvement-loop architecture for math optimization. The math problems themselves (sphere packing, kissing numbers, autocorrelation) are unrelated to protein design.

## Open questions / connections
- Can a planner/assistant/critic role split improve council-dispatch in the einstein agent vs persona-only dispatch, particularly for tool-execution discipline (the "assistant double-checking parameters" pattern)?
- The paper's RAG retriever returned wrong PDB ids without the agents noticing — what verification analog protects the einstein agent when wiki-first-lookup retrieves a hallucinated finding? Connects to triple-verify and wiki-attribution rules.
- Extends prior MechAgents (Ni & Buehler 2023) and MechGPT (Buehler 2023) multi-agent work; suggests the multi-agent pattern generalizes across physics-heavy domains and is worth comparing to single-agent ReAct loops on the same task set.
