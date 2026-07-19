---
type: note
kind: paper-relevance
about: 2025-deng-swe-bench-pro-can-agents
canonical: ../../domains/ai-agents/source/2025-deng-swe-bench-pro-can-agents.md
---

# Relevance note — SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

Canonical distillation: [`2025-deng-swe-bench-pro-can-agents.md`](../../domains/ai-agents/source/2025-deng-swe-bench-pro-can-agents.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is a SWE-agent evaluation paper, orthogonal to math-optimization problems on Einstein Arena. The closest indirect connection is methodological: the contamination-resistant curation strategy (copyleft licensing + private commercial sets + held-out splits) and the human-augmented requirements/interface pattern could inform how this project structures its own `docs/agent/` cycle-log and ablation protocols.

## Open questions / connections
- Can verifier-based benchmarks be replaced by rubric/quality-based evaluation when valid solutions diverge from canonical interfaces? (cf. autonomous-loop's triple-verify regime — both grapple with false-negative verifier drift)
- Why does multi-file context handling degrade so steeply past 3 files even for frontier models — capacity, attention, or planning limitation?
- Extends SWE-Bench (Jimenez 2024), SWE-agent (Yang 2024), Multi-SWE-bench (Zan 2024); leaves open the question of multi-agent / human-agent collaborative SWE evaluation.
