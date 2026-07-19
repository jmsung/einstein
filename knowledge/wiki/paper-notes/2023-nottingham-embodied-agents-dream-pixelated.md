---
type: note
kind: paper-relevance
about: 2023-nottingham-embodied-agents-dream-pixelated
canonical: ../../domains/ai-agents/source/2023-nottingham-embodied-agents-dream-pixelated.md
---

# Relevance note — Do Embodied Agents Dream of Pixelated Sheep?: Embodied Decision Making using Language Guided World Modelling

Canonical distillation: [`2023-nottingham-embodied-agents-dream-pixelated.md`](../../domains/ai-agents/source/2023-nottingham-embodied-agents-dream-pixelated.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The setup — *hypothesize-then-verify* an LLM-proposed structure, prune the search frontier to the path-to-goal, and treat LLM output as a noisy prior rather than ground truth — is structurally analogous to using LLM-suggested techniques/concepts to guide optimizer exploration on arena problems; potentially informs the council-dispatch and self-improvement loop design rather than any specific math problem.

## Open questions / connections
- Automatic state-abstraction discovery (DECKARD assumes a textual $\phi: O \to X$ is given) — open problem the authors flag.
- Extension to stochastic AWMs (current method assumes deterministic transitions).
- Quantitative threshold: at what LLM error rate does hypothesize-then-verify stop beating tabula-rasa? Figure 6 hints at it but no closed form.
- Connection to Ammanabrolu & Riedl (2021) knowledge-graph world models and to Tam et al. (2022) / Mu et al. (2022) language-as-state-abstraction for exploration.
