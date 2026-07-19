---
type: note
kind: paper-relevance
about: 2025-zheng-thought-communication-multiagent-collaboration
canonical: ../../domains/ai-agents/source/2025-zheng-thought-communication-multiagent-collaboration.md
---

# Relevance note — Thought Communication in Multiagent Collaboration

Canonical distillation: [`2025-zheng-thought-communication-multiagent-collaboration.md`](../../domains/ai-agents/source/2025-zheng-thought-communication-multiagent-collaboration.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Potentially relevant scaffolding if the einstein agent ever runs a true multi-persona council that exchanges latent state rather than markdown — currently council-dispatch is natural-language only, so this is a research-direction signal, not a technique to apply now.

## Open questions / connections
- Could council personas (Gauss, Tao, Cohn, …) exchange recovered latent thoughts instead of natural-language questions, reducing the lossy-language bottleneck flagged in `council-dispatch.md`?
- Extends nonlinear ICA identifiability (Hyvärinen, Khemakhem, Lachapelle, Zheng) to pairwise rather than global recovery — first work to drop auxiliary signals entirely.
- Open: does the Jacobian-spanning assumption hold for transformer hidden states in practice, or only asymptotically?
