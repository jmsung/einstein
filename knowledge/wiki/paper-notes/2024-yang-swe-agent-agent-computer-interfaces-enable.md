---
type: note
kind: paper-relevance
about: 2024-yang-swe-agent-agent-computer-interfaces-enable
canonical: ../../domains/ai-agents/source/2024-yang-swe-agent-agent-computer-interfaces-enable.md
---

# Relevance note — SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

Canonical distillation: [`2024-yang-swe-agent-agent-computer-interfaces-enable.md`](../../domains/ai-agents/source/2024-yang-swe-agent-agent-computer-interfaces-enable.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The transferable lesson for the autonomous-loop agent on Einstein Arena is interface design: small, compact, well-documented action sets with informative-but-concise feedback and guardrails (linter-style rejection of bad edits, suppressed verbose tool output, collapsed history) outperform raw shell access — directly relevant to how the agent's wiki-ingest, council-dispatch, and optimizer-launch commands are exposed.

## Open questions / connections
- Can ACI design itself be automated (meta-optimization of agent tools) rather than crafted from manual trajectory inspection?
- Do the four principles (simple actions, compact actions, informative-concise feedback, guardrails) generalize to non-programming domains like math-optimizer dispatch or wiki navigation?
- Extends ReAct (Yao et al.) and InterCode (Yang et al. 2024) by adding interface-layer rather than prompting-layer interventions; complements SWE-bench (Jimenez et al. 2024) as the evaluation harness.
