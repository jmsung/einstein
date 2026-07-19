---
type: note
kind: paper-relevance
about: 2024-qu-crispr-gpt-agentic-automation-gene-editing
canonical: ../../domains/ai-agents/source/2024-qu-crispr-gpt-agentic-automation-gene-editing.md
---

# Relevance note — CRISPR-GPT for agentic automation of gene-editing experiments

Canonical distillation: [`2024-qu-crispr-gpt-agentic-automation-gene-editing.md`](../../domains/ai-agents/source/2024-qu-crispr-gpt-agentic-automation-gene-editing.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. **Methodologically relevant** to the einstein autonomous-loop agent: same pattern of *LLM-planner + state-machine task executor + wrapped tool calls + human-override* that this repo is building for math problem-solving — particularly the "wrap APIs behind LLM-friendly textual interfaces" lesson and the static-dependency-DAG vs dynamic-planning tradeoff (CRISPR-GPT deliberately forbids LLM from adding/deleting tasks at runtime for robustness).

## Open questions / connections
- Static task DAG vs dynamic planner: paper flags dynamic task addition as future work — same tradeoff facing einstein's [[council-dispatch]] and math-solving-protocol state machines.
- "I don't know" → human handoff for raw sequence requests — analog to the agent's wiki-first refusal + triple-verify when asked for numerical claims it can't ground.
- Extends ChemCrow (chemistry) and Coscientist (Pd-catalyzed coupling) into the bio domain; the cross-domain pattern (wrapped-tool LLM agent + wet-lab loop) is the transferable artifact, not the CRISPR specifics.
