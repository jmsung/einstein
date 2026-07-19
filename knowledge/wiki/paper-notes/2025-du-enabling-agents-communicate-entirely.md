---
type: note
kind: paper-relevance
about: 2025-du-enabling-agents-communicate-entirely
canonical: ../../domains/ai-agents/source/2025-du-enabling-agents-communicate-entirely.md
---

# Relevance note — Enabling Agents to Communicate Entirely in Latent Space

Canonical distillation: [`2025-du-enabling-agents-communicate-entirely.md`](../../domains/ai-agents/source/2025-du-enabling-agents-communicate-entirely.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as infrastructure for the autonomous-loop agent if multi-agent council dispatch is ever moved off natural-language transcripts — latent-channel communication could in principle preserve parallel hypotheses (the paper's claimed mechanism for the MATH Level-5 win) that CoT linearization collapses, which matches our council-dispatch rationale of "questions, not single answers."

## Open questions / connections
- Does the "parallel hypotheses preserved in latent space" claim hold under formal information-theoretic measurement, or is it inferred only from Top-k probability gaps?
- Cross-family transfer (Qwen→LLaMA) works without shared tokenizer — what is the minimal representational alignment needed, and does it survive when sender/receiver disagree on task framing?
- Compression to $K=8$ retains task utility but the paper does not test whether the compressed latents encode the *same* reasoning content or a different sufficient statistic — relevant if used to audit agent reasoning.
- Extends Coconut (Hao et al. 2024), activation grafting (Ramesh & Li 2025), and per-token latent deltas (Tang et al. 2025) by being fully language-free and adapter-trained rather than ad-hoc.
