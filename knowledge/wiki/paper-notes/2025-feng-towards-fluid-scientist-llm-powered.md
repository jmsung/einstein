---
type: note
kind: paper-relevance
about: 2025-feng-towards-fluid-scientist-llm-powered
canonical: ../../domains/ai-agents/source/2025-feng-towards-fluid-scientist-llm-powered.md
---

# Relevance note — Towards an AI Fluid Scientist: LLM-Powered Scientific Discovery in Experimental Fluid Mechanics

Canonical distillation: [`2025-feng-towards-fluid-scientist-llm-powered.md`](../../domains/ai-agents/source/2025-feng-towards-fluid-scientist-llm-powered.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is fluid-mechanics LLM-agent infrastructure, not a math-optimization paper. The methodological lesson relevant to the Einstein Arena loop is the adaptive-resolution hypothesis-driven campaign (3000 → 122 trials via coarse-to-fine refinement) and the empirical finding that NN surrogates beat mechanistic decompositions on strongly nonlinear response surfaces — a cautionary data point for any "fit a physical formula" step in problems like P14/P17 where evaluator surfaces are nonlinearly coupled.

## Open questions / connections
- Does the adaptive 4-stage coarse-to-fine campaign template generalize as a meta-protocol for arena problems (cf. council-dispatch + gap-detect)?
- When should the agent abandon mechanistic parameterization and switch to a tanh-network surrogate? The paper's pivot trigger ($R^2$ stuck at 0.43 after augmentation) is a candidate heuristic.
- Extends Khalak & Williamson (1999), Assi et al. (2010, 2013); leaves open high-Re ($>10^5$), 3D effects, and phase control.
