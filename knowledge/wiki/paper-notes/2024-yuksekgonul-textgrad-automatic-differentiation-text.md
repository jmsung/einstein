---
type: note
kind: paper-relevance
about: 2024-yuksekgonul-textgrad-automatic-differentiation-text
canonical: ../../domains/ai-agents/source/2024-yuksekgonul-textgrad-automatic-differentiation-text.md
---

# Relevance note — TextGrad: Automatic \"Differentiation\" via Text

Canonical distillation: [`2024-yuksekgonul-textgrad-automatic-differentiation-text.md`](../../domains/ai-agents/source/2024-yuksekgonul-textgrad-automatic-differentiation-text.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — the Einstein Arena workflow is numerical optimization with verified scoring (triple-verify), not blackbox text-feedback loops. However TextGrad is a plausible mental model for the agent's *own* self-improvement loop (council dispatch → gap → finding → concept): textual "gradients" on wiki pages and strategy.md, with cycle-log as the optimization trace. Relevant if any sub-step (prompt for council personas, refinement of strategy.md drafts) is ever framed as iterative LLM-feedback optimization.

## Open questions / connections
- Does TGD converge or oscillate on long horizons? The paper reports ≤10 iterations; no convergence analysis or step-size theory beyond the gradient-descent analogy.
- How does it compare against DSPy-style compiled prompts on the same prompt-optimization benchmarks under matched compute? GSM8k split is borrowed from DSPy but no head-to-head.
- Extends Pryzant et al. ("Automatic Prompt Optimization with 'Gradient Descent'", 2023) by generalizing beyond prompts to arbitrary variables and arbitrary forward functions.
- Open: can textual gradients be combined with numerical gradients in hybrid systems (e.g., LLM proposes a molecule, autodiff polishes geometry)?
- For agent self-improvement: could `docs/agent/cycle-log.md` rows be treated as ∂L/∂(strategy) signals to refine `mb/<problem>/strategy.md` via TGD?
