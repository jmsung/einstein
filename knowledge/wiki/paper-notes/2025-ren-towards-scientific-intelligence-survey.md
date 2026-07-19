---
type: note
kind: paper-relevance
about: 2025-ren-towards-scientific-intelligence-survey
canonical: ../../domains/ai-agents/source/2025-ren-towards-scientific-intelligence-survey.md
---

# Relevance note — Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents

Canonical distillation: [`2025-ren-towards-scientific-intelligence-survey.md`](../../domains/ai-agents/source/2025-ren-towards-scientific-intelligence-survey.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background for the autonomous-loop's own architecture: the four-component decomposition (planner / memory / action / verifier) and the P1–P6 + L1–L2 planner taxonomy give vocabulary for designing the JSAgent cycle (council dispatch ≈ P5 role-interactive, wiki-first lookup ≈ P2 context-augmented, search-based deep-research ≈ P4, schema-driven cycle-discipline ≈ P1). No direct arena/math tie.

## Open questions / connections
- Which planner type best fits *math-wisdom* compounding — does iterative wiki-grounded P2 dominate P4 tree-search for problems where the bottleneck is conceptual gap-detection rather than candidate enumeration?
- The survey's verifier discussion frames "factual accuracy + empirical consistency" — how does this map onto the triple-verify axiom (fast eval + exact reimpl + cross-check)?
- AlphaEvolve (Novikov 2025) appears under P6 programmatic — direct precedent for code-generating agents on hard math/algorithmic problems; worth ingesting separately.
- Cycle-discipline (cycle-log + skill-library) corresponds to "memory" + "verifier" feedback loop the survey identifies as critical for reproducibility.
