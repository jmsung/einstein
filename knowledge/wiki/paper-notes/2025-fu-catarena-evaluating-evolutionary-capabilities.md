---
type: note
kind: paper-relevance
about: 2025-fu-catarena-evaluating-evolutionary-capabilities
canonical: ../../domains/ai-agents/source/2025-fu-catarena-evaluating-evolutionary-capabilities.md
---

# Relevance note — CATArena: Evaluating Evolutionary Capabilities of Code Agents via Iterative Tournaments

Canonical distillation: [`2025-fu-catarena-evaluating-evolutionary-capabilities.md`](../../domains/ai-agents/source/2025-fu-catarena-evaluating-evolutionary-capabilities.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant as methodology mirror for einstein's own cycle-log / skill-library / self-improvement-loop — this paper independently formalizes what the einstein repo calls "compounding": $S_{evo}$ is structurally the same idea as the cycle-log's cross-cycle improvement metric, and its OLS-slope-over-rounds construction is a candidate template for measuring whether the JSAgent loop actually self-improves on the 23 arena problems vs. just hammering harder each cycle.

## Open questions / connections
- Could $S_{evo}$-style OLS-slope-over-cycles replace ad-hoc "did the wiki grow" honesty checks in `docs/agent/metrics.md`?
- The "complexity barrier" phenomenon (agents stop improving once gap to optimum is large) predicts that hard arena problems (P1 sphere packing, P15/P16 equioscillation) will show flat or negative $S_{evo}$ unless peer-solution analogues (top-3 SOTA downloads) are explicitly seeded — matches the council-dispatch rule's top-3 SOTA seeding.
- Their finding that agents can't combine peer-learning + self-reflection is a direct caution against the einstein protocol's combined wiki-first + council-dispatch step — worth tracking whether cycles that do both actually outperform cycles that do one.
