---
type: note
kind: paper-relevance
about: 2023-yang-large-language-models-automated
canonical: ../../domains/ai-agents/source/2023-yang-large-language-models-automated.md
---

# Relevance note — Large Language Models for Automated Open-domain Scientific Hypotheses Discovery

Canonical distillation: [`2023-yang-large-language-models-automated.md`](../../domains/ai-agents/source/2023-yang-large-language-models-automated.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The interesting transferable pattern is the **multi-aspect iterative critic loop** (clarity / reality / novelty + past/future-feedback) as a template for the einstein self-improvement loop — analogous to council-dispatch + gap-detect + failure-finding, but with the critic explicitly separated per-axis and looped. Reinforces that LLM hypothesis-generation needs explicit novelty-vs-validity tension management, mirroring the wiki's reality-check vs cross-pollination filter.

## Open questions / connections
- Does the present/past/future-feedback decomposition transfer to math hypothesis generation (conjecture-style claims about bounds, structure), or is it specific to soft-science narrative hypotheses?
- The "less-related inspirations → more novel" past-feedback heuristic — is there a math analogue (e.g., dispatching personas from distant problem categories to seed P-X)?
- Extends prior self-refine work (Madaan et al., 2023) by adding non-instant feedback channels; future work flags transfer to natural-science domains.
