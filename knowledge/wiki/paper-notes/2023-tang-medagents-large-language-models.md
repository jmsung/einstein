---
type: note
kind: paper-relevance
about: 2023-tang-medagents-large-language-models
canonical: ../../domains/ai-agents/source/2023-tang-medagents-large-language-models.md
---

# Relevance note — MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning

Canonical distillation: [`2023-tang-medagents-large-language-models.md`](../../domains/ai-agents/source/2023-tang-medagents-large-language-models.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The mechanism — role-play "council of experts" each writing analyses, iterative voting toward a consensus report — is the exact structural template the einstein repo's `council-dispatch.md` rule implements with mathematician personas (Gauss, Tao, Cohn, ...). Concretely supports: each persona writes a *question*, synthesizer compiles, iterative refinement, unanimous-report gate. Useful as a citation for why the council should produce *analyses/questions* not direct answers (cf. hallucination from naive CoT) and for the $m=5, n=2, t=5$ parameter choices.

## Open questions / connections
- Does the unanimous-vote stopping rule scale when experts are *adversarial* (council of mathematicians disagreeing on approach) vs collaborative (medical specialists converging)? The paper assumes convergence; math problems may benefit from preserving dissent.
- Role-play replaces RAG here because medical facts live in pretraining; for math arena problems where the wiki *is* the retrieval target, role-play + RAG (qmd query) seems strictly better than either alone.
- No comparison to debate frameworks (Liang et al. 2023, Du et al. 2023) that preserve disagreement — relevant to council-dispatch design choice between "consensus" vs "spread of stances".
