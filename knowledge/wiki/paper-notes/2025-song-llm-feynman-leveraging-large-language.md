---
type: note
kind: paper-relevance
about: 2025-song-llm-feynman-leveraging-large-language
canonical: ../../domains/ai-agents/source/2025-song-llm-feynman-leveraging-large-language.md
---

# Relevance note — LLM-Feynman: Leveraging Large Language Models for Universal Scientific Formula and Theory Discovery

Canonical distillation: [`2025-song-llm-feynman-leveraging-large-language.md`](../../domains/ai-agents/source/2025-song-llm-feynman-leveraging-large-language.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The relevant transferable idea for the Einstein Arena loop is the multi-objective Pareto scoring (error + complexity + LLM-judged interpretability) plus MCTS-guided explanation refinement — a template for how an LLM council could propose, score, and iterate candidate ansätze for closed-form bounds in problems like P15/P16 equioscillation, Cohn–Elkies magic functions, or autocorrelation kernels.

## Open questions / connections
- Can the loss-function self-evaluation $S$ be replaced or augmented by a *verifier*-grounded signal (analogous to triple-verify) to avoid LLM sycophancy on interpretability?
- LLM-from-scratch feature engineering underperforms Automatminer+MI — suggests human-curated descriptor libraries remain essential; analogue for arena: persona-curated parameterization libraries beat free-form LLM ansatz generation.
- Token-length bottleneck limits to ~$10^4$ samples; hierarchical / RLHF extensions proposed but unimplemented.
