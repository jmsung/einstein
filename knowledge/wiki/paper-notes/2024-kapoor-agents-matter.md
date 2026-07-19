---
type: note
kind: paper-relevance
about: 2024-kapoor-agents-matter
canonical: ../../domains/ai-agents/source/2024-kapoor-agents-matter.md
---

# Relevance note — AI Agents That Matter

Canonical distillation: [`2024-kapoor-agents-matter.md`](../../domains/ai-agents/source/2024-kapoor-agents-matter.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Directly relevant to the einstein autonomous-loop design: validates the project's local-evaluator-discipline / triple-verify / compute-router stance, and the warning against "complex agent architectures" without baselines mirrors the repo's "hammer the optimizer harder" anti-pattern. Reinforces that wiki-cycle metrics (cycle-log.md, skill-library.md) must include cost-per-cycle, not just accuracy/top-3, to avoid the same trap.

## Open questions / connections
- Do System 2 techniques (planning, reflection, debugging) help on harder programming tasks (SWE-bench) where they don't on HumanEval? Open.
- How to design holdout sets for domain-general benchmarks when the agent's training distribution is opaque (e.g., WebArena).
- Joint optimization here is single-objective Pareto via Optuna with 16 trials — more sophisticated multi-objective methods (NSGA-II, Bayesian) likely improve substantially.
- Connection to Einstein Arena: the local↔arena verifier drift documented in einstein findings (P9, P14, P17) is the agent-benchmark analog of the reproducibility failures documented here.
