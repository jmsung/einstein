---
type: note
kind: paper-relevance
about: 2025-hofsttter-elicitation-game-evaluating-capability
canonical: ../../domains/ai-agents/source/2025-hofsttter-elicitation-game-evaluating-capability.md
---

# Relevance note — The Elicitation Game: Evaluating Capability Elicitation Techniques

Canonical distillation: [`2025-hofsttter-elicitation-game-evaluating-capability.md`](../../domains/ai-agents/source/2025-hofsttter-elicitation-game-evaluating-capability.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as agent-safety context (model-organism methodology, hidden-capability elicitation) — orthogonal to math-optimization problems on the einstein arena.

## Open questions / connections
- Can circuit-breaking-style robustness training be adapted to *positively* elicit latent reasoning capabilities (inverse use of the loss)?
- Why does anti-refusal training transfer to code generation despite zero code data — what shared representation does it unblock?
- Extends Greenblatt et al. (2024) password-locking and Zou et al. (2024) circuit-breaking; leaves open whether circuit-broken models can be made robust to *combined* prompting + fine-tuning attacks.
- Steering vectors underperform prompting — open whether better steering-vector construction (Tan et al. 2024 reliability work) closes the gap.
