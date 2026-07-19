---
type: note
kind: paper-relevance
about: 2024-yao-multi-objective-evolution-heuristic-using
canonical: ../../domains/ai-agents/source/2024-yao-multi-objective-evolution-heuristic-using.md
---

# Relevance note — Multi-objective Evolution of Heuristic Using Large Language Model

Canonical distillation: [`2024-yao-multi-objective-evolution-heuristic-using.md`](../../domains/ai-agents/source/2024-yao-multi-objective-evolution-heuristic-using.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background — no direct arena tie. Potentially relevant as scaffolding for the autonomous-loop self-improvement layer: the dominance-dissimilarity / AST-diversity trick is a concrete antidote to LLM-driven evolutionary search collapsing onto one code template, which is the same failure mode the einstein agent risks when re-running optimizers across cycles. Does **not** advance any of the 23 arena math problems directly.

## Open questions / connections
- Extends FunSearch (Romera-Paredes 2024) and EoH (Liu 2024) — both already on the einstein agent's radar as code-search baselines.
- Scaling beyond ~3 objectives is flagged as unsolved; relevant if the cycle-runner ever weights gap + runtime + code-complexity + readability jointly.
- AST-similarity as diversity proxy is cheap but syntactic; semantically equivalent code with different ASTs would be falsely "diverse" — open question whether behavioral/output dissimilarity is a better signal for math-optimizer heuristics.
- No connection to LP duality, Cohn–Elkies, equioscillation, or any concept currently in the einstein wiki.
