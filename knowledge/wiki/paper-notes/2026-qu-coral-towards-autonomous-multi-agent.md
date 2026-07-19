---
type: note
kind: paper-relevance
about: 2026-qu-coral-towards-autonomous-multi-agent
canonical: ../../domains/ai-agents/source/2026-qu-coral-towards-autonomous-multi-agent.md
---

# Relevance note — CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery

Canonical distillation: [`2026-qu-coral-towards-autonomous-multi-agent.md`](../../domains/ai-agents/source/2026-qu-coral-towards-autonomous-multi-agent.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Directly relevant to the einstein autonomous-loop / self-improvement architecture: CORAL's shared-memory + heartbeat design is essentially a working implementation of this repo's wiki-first + cycle-discipline + failure-is-a-finding loop, with empirical evidence that (a) periodic forced reflection prevents micro-optimization plateaus, (b) externalized notes/skills produce 10× more reuse on hard problems, and (c) horizontal multi-agent parallelism with no role specialization outperforms single-agent runs on stress tests like the Erdős minimum overlap problem (P-relevant) and circle packing (P11-adjacent). Validates the council-dispatch + wiki-as-memory bet.

## Open questions / connections
- Heartbeat schedule (every-1 reflect, every-10 consolidate, every-5-plateau pivot) is hand-tuned — can the agent learn its own heartbeat? Maps onto the gap-detector cadence question in `cycle-discipline.md`.
- Knowledge artifacts/attempt ratio (0.05 vs 0.55) as a diagnostic for whether a task is "in-distribution for the wiki" — could be a metric for the einstein cycle-log.
- Extends AlphaEvolve / FunSearch / ShinkaEvolve by removing the fixed MAP-Elites / island selection rule; connects to EvoX's meta-evolved search and to AdaEvolve's adaptive strategies. Leaves open whether evaluator-hacking risks scale with agent autonomy.
