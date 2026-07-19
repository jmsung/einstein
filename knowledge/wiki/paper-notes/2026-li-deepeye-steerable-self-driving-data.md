---
type: note
kind: paper-relevance
about: 2026-li-deepeye-steerable-self-driving-data
canonical: ../../domains/ai-agents/source/2026-li-deepeye-steerable-self-driving-data.md
---

# Relevance note — DeepEye: A Steerable Self-driving Data Agent System

Canonical distillation: [`2026-li-deepeye-steerable-self-driving-data.md`](../../domains/ai-agents/source/2026-li-deepeye-steerable-self-driving-data.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The DAG-with-static-validation + context-isolated sub-agents pattern is loosely analogous to the einstein repo's council-dispatch + self-improvement-loop architecture (planner over isolated persona subagents, gap-detect feedback, SOP-style finding reuse), but DeepEye targets BI workflows rather than math optimization.

## Open questions / connections
- Could the einstein autonomous loop adopt a Validator/Optimizer stage between `/goal` and `/act` to catch malformed plans (missing wiki cites, unrouted compute) before execution?
- Kahn's-algorithm parallel layering could apply to council dispatch and multi-problem optimizer runs — independent personas / problems already run in parallel but without explicit DAG accounting.
- Auto-archiving successful workflows as SOPs mirrors the skill-library promotion mechanism; worth comparing the promotion criteria.
