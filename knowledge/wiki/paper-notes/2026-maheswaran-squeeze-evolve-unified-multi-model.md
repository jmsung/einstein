---
type: note
kind: paper-relevance
about: 2026-maheswaran-squeeze-evolve-unified-multi-model
canonical: ../../domains/ai-agents/source/2026-maheswaran-squeeze-evolve-unified-multi-model.md
---

# Relevance note — Squeeze Evolve: Unified Multi-Model Orchestration for Verifier-Free Evolution

Canonical distillation: [`2026-maheswaran-squeeze-evolve-unified-multi-model.md`](../../domains/ai-agents/source/2026-maheswaran-squeeze-evolve-unified-multi-model.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card:

## Why it matters here
Directly relevant to the einstein agent's circle-packing problem family (P11, P18, etc.) — the paper's evolved program is essentially the *same* LP-decomposition + SA + SLSQP recipe the wiki already uses, so it both validates the technique and offers a verifier-free orchestration layer that could replace single-model `Agent` calls in the autonomous-loop branch. More broadly, the diversity-collapse finding and confidence-as-fitness routing inform any council-dispatch / multi-step recombination pipeline (`council-dispatch.md`, `self-improvement-loop.md`) where the agent currently uses one model uniformly.

## Open questions / connections
- Does cross-model confidence remain a reliable fitness proxy on math-discovery tasks where verifiers *do* exist (cf. triple-verify rule) — i.e., how often does GC disagree with the exact evaluator?
- The accumulate-update rule with fitness-weighted sampling ($\zeta=0.5$) on circle packing — can this replace standard basin-hopping restart schedules on einstein problems P5/P11/P14/P17?
- Extends FunSearch / AlphaEvolve [Romera-Paredes 2024, Novikov 2025] and RSA [Recursive Self-Aggregation, 2025]; leaves open whether the routing scheme survives when $M_1$ and $M_2$ have disjoint failure modes (e.g., open-weight vs proprietary chains-of-thought).
- Spearman correlation between confidence and circle-packing score across loops hovers near 0 (Fig. 18) — when does GC stop being a valid fitness signal for hard discovery problems?
