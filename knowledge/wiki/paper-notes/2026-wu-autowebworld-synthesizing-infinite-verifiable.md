---
type: note
kind: paper-relevance
about: 2026-wu-autowebworld-synthesizing-infinite-verifiable
canonical: ../../domains/ai-agents/source/2026-wu-autowebworld-synthesizing-infinite-verifiable.md
---

# Relevance note — AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines

Canonical distillation: [`2026-wu-autowebworld-synthesizing-infinite-verifiable.md`](../../domains/ai-agents/source/2026-wu-autowebworld-synthesizing-infinite-verifiable.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Of marginal relevance: the FSM-precondition-gated BFS verification pattern is a clean instance of "embed the verifier into the environment instead of trusting an external judge" — structurally analogous to triple-verify discipline ([[triple-verify]]) and the local-evaluator vs arena-verifier drift problem, but applied to GUI agents rather than math optimization.

## Open questions / connections
- Can FSM-style explicit-state synthetic environments be built for math-solver agents (states = solution candidates, transitions = optimizer moves) to give cheap step-level verification without per-step arena submission?
- Scaling law in synthetic-data volume vs downstream performance — does an analog hold for math-wisdom self-improvement (cycles × wiki entries vs problem score)?
- Reasoning ("Thinking") cost dominates total budget 61% — same pattern likely applies to council dispatch; suggests caching reasoning traces across persona invocations.
