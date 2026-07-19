---
type: note
kind: paper-relevance
about: 2024-wijk-re-bench-evaluating-frontier-capabilities
canonical: ../../domains/ai-agents/source/2024-wijk-re-bench-evaluating-frontier-capabilities.md
---

# Relevance note — RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts

Canonical distillation: [`2024-wijk-re-bench-evaluating-frontier-capabilities.md`](../../domains/ai-agents/source/2024-wijk-re-bench-evaluating-frontier-capabilities.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The methodology is relevant as a template for the einstein agent's own evaluation — score-normalization against a reference solution, score@$k$ vs wall-clock, and explicit "agents are fast/cheap but plateau while humans climb" framing inform how cycle-log.md should track agent-vs-human comparisons over compute budgets.

## Open questions / connections
- Why do agents' returns to time saturate while humans' don't? Suggests scaffolding/long-horizon planning is the binding constraint, not raw token cost.
- Best-of-$k$ allocation differs by agent (Claude favors many short runs, o1-preview favors fewer longer runs, humans favor longest single runs) — analogous question for einstein optimizer multistarts vs deeper polish.
- Score normalization that caps near reference may hide a heavy right tail; relevant to triple-verify when one of three numbers is an "above-ceiling" outlier.
