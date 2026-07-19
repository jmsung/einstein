---
type: note
kind: paper-relevance
about: 2026-zhang-hyperagents
canonical: ../../domains/ai-agents/source/2026-zhang-hyperagents.md
---

# Relevance note — Hyperagents

Canonical distillation: [`2026-zhang-hyperagents.md`](../../domains/ai-agents/source/2026-zhang-hyperagents.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card:

## Why it matters here
General background; no direct arena tie — but the DGM-H archive-with-metacognitive-modification pattern is directly applicable to the einstein autonomous-loop agent: it argues for an editable meta-mechanism and persistent cross-cycle memory (cf. cycle-log, skill-library) as the substrate for compounding wisdom, rather than a fixed handcrafted self-improvement instruction.

## Open questions / connections
- Parent selection ablation (Appendix E.5) shows learned UCB-style mechanisms still trail a handcrafted `score-child-prop` — when does meta-learning beat hand engineering on selection?
- How to design evaluation signals that resist Goodhart-style gaming as self-modification compounds? Especially relevant for arena scores with verifier drift.
- Extends DGM (Zhang 2025), ADAS (Hu 2025), Gödel Machine (Schmidhuber 2003); connects to AI-Scientist, evolutionary code search, and self-referential meta-learning (Kirsch–Schmidhuber 2022).
- Open: bounds on self-acceleration rate; conditions under which meta-improvement transfer is monotone vs. catastrophic.
