---
type: note
kind: paper-relevance
about: 2025-xiang-self-supervised-prompt-optimization
canonical: ../../domains/ai-agents/source/2025-xiang-self-supervised-prompt-optimization.md
---

# Relevance note — Self-Supervised Prompt Optimization

Canonical distillation: [`2025-xiang-self-supervised-prompt-optimization.md`](../../domains/ai-agents/source/2025-xiang-self-supervised-prompt-optimization.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card:

## Why it matters here
General background; no direct arena tie. Relevant as a candidate inner-loop for the autonomous-loop agent's own *prompt refinement* (e.g., council-persona prompts, optimizer config-gen prompts) — particularly when ground-truth scores are slow/expensive (long Modal jobs) and a cheap pairwise "did this prompt produce better reasoning?" judgment suffices. Complements GEPA/TextGrad/DSPy-style optimizers in the wiki.

## Open questions / connections
- Does pairwise OvO degrade on tasks where the LLM judge lacks domain competence (e.g., evaluating mpmath polish quality, equioscillation diagnostics)?
- 3-sample evaluation: when does sample-size variance dominate the optimization signal? No formal variance analysis given.
- Extends TextGrad (Yuksekgonul 2024) and PromptBreeder (Fernando 2024) by removing ground-truth dependency; relates to GEPA (Agrawal 2025) reflective prompt evolution and DSPy (Khattab 2023) declarative pipelines.
- Could the OvO signal be combined with arena-verifier ground-truth in a hybrid (cheap pairwise pre-filter → expensive verified scoring on survivors)?
