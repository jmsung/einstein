---
type: note
kind: paper-relevance
about: 2025-xu-towards-multi-agent-reasoning-systems
canonical: ../../domains/ai-agents/source/2025-xu-towards-multi-agent-reasoning-systems.md
---

# Relevance note — Towards Multi-Agent Reasoning Systems for Collaborative Expertise Delegation: An Exploratory Design Study

Canonical distillation: [`2025-xu-towards-multi-agent-reasoning-systems.md`](../../domains/ai-agents/source/2025-xu-towards-multi-agent-reasoning-systems.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as scaffolding for the council-dispatch rule — it supports the design choice that personas should be fine-grained sub-domain specialists writing diverse perspectives rather than a fixed solver/critic/coordinator pipeline, and that aligning persona expertise to the problem category (sphere_packing → Viazovska, autocorrelation → Hilbert, etc.) is empirically justified for "contextual" tasks. Says nothing useful about pure mathematical deduction, which is the einstein regime — the paper itself notes expertise alignment gives only marginal gains on math.

## Open questions / connections
- Does the diversity > workflow result hold for hard math (e.g., olympiad / research-level proof search), or only mid-difficulty MMLU-Pro math where the 7B base model already saturates?
- What is the right communication topology beyond sequential — sparse graphs, hierarchical aggregation, sparse Mixture-of-Agents — for cost-bounded scaling past $n=10$?
- The "Knowledge Recall vs Perspective Synthesis" dichotomy is asserted but never causally separated; ablations isolating each mechanism would test whether persona prompts do more than activate a stylistic register.
