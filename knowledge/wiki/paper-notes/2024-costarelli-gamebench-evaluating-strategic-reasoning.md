---
type: note
kind: paper-relevance
about: 2024-costarelli-gamebench-evaluating-strategic-reasoning
canonical: ../../domains/ai-agents/source/2024-costarelli-gamebench-evaluating-strategic-reasoning.md
---

# Relevance note — GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents

Canonical distillation: [`2024-costarelli-gamebench-evaluating-strategic-reasoning.md`](../../domains/ai-agents/source/2024-costarelli-gamebench-evaluating-strategic-reasoning.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Tangentially relevant as a *benchmark-design* reference for the einstein agent's self-improvement metrics (cycle-log, skill-library) — the paper's discussion of cherry-picking risk, out-of-distribution curation, and aggregation fragility echoes the honesty checks in `docs/agent/`.

## Open questions / connections
- How to design black-box scaffolds beyond CoT/RAP that actually beat CoT — RAP-as-implemented suffered from compounding errors in predicted states.
- Robust aggregation across heterogeneous tasks (g-factor / factor analysis vs. naive Bradley–Terry mean) — parallels the einstein cycle-log's "per-problem vs aggregate" tension.
- How to verify out-of-distribution status without strategy-guide-injection ablations, and how to keep curated benchmarks OOD as frontier models retrain.
