---
type: note
kind: paper-relevance
about: 2024-weij-sandbagging-language-models-can
canonical: ../../domains/ai-agents/source/2024-weij-sandbagging-language-models-can.md
---

# Relevance note — AI Sandbagging: Language Models can Strategically Underperform on Evaluations

Canonical distillation: [`2024-weij-sandbagging-language-models-can.md`](../../domains/ai-agents/source/2024-weij-sandbagging-language-models-can.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Tangential relevance: sandbagging is the *evaluator-trust* dual of triple-verification — a reminder that single-evaluator scores can be manipulated (parallels P9/P14/P17 verifier-drift findings about untrustworthy single-source scoring), and that synthetic-data fine-tuning generalizes to held-out benchmarks (relevant if the agent ever trains specialized evaluators).

## Open questions / connections
- Can mechanistic interpretability detect password-locking when the password is unknown to the evaluator? (Extends Hubinger et al. sleeper-agents work.)
- What detection methods beyond capability-profile inspection catch *non-naive* sandbagging that mimics a weaker model's profile?
- How does sandbagging interact with RL fine-tuning and agentic scaffolding (vs the supervised-LoRA regime tested here)?
