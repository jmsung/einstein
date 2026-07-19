---
type: note
kind: paper-relevance
about: 2024-ghafarollahi-sciagents-automating-scientific-discovery
canonical: ../../domains/ai-agents/source/2024-ghafarollahi-sciagents-automating-scientific-discovery.md
---

# Relevance note — SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning

Canonical distillation: [`2024-ghafarollahi-sciagents-automating-scientific-discovery.md`](../../domains/ai-agents/source/2024-ghafarollahi-sciagents-automating-scientific-discovery.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as architectural inspiration for the autonomous-loop agent — specifically (a) random-walk over a concept graph as a *gap-discovery* mechanism analogous to `wiki_graph.py --file-questions`, and (b) role-specialized council dispatch where each persona writes a *question* rather than an *answer*, which already mirrors the einstein council-dispatch rule.

## Open questions / connections
- Random-path vs shortest-path sampling on the einstein wiki graph: does random sampling surface more fertile cross-problem gaps than the current shortest-path / Type-2 detector?
- No quantitative evaluation of hypothesis quality — only self-rating by the same LLM stack that generated them; circular. How would einstein's triple-verify discipline apply to agent-generated hypotheses?
- The Critic/novelty-check loop terminates without external ground truth; mirrors the local-vs-arena drift risk in einstein. Suggests an arena-verifier analogue is needed before trusting autonomous proposals.
