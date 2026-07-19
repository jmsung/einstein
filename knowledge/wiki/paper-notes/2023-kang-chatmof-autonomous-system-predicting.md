---
type: note
kind: paper-relevance
about: 2023-kang-chatmof-autonomous-system-predicting
canonical: ../../domains/ai-agents/source/2023-kang-chatmof-autonomous-system-predicting.md
---

# Relevance note — ChatMOF: An Autonomous AI System for Predicting and Generating Metal-Organic Frameworks

Canonical distillation: [`2023-kang-chatmof-autonomous-system-predicting.md`](../../domains/ai-agents/source/2023-kang-chatmof-autonomous-system-predicting.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant as a **reference architecture for autonomous-loop agents** — the agent/toolkit/evaluator decomposition, ReAct/MRKL planning loop, LLM-as-GA-operator pattern, and the small-population-vs-token-budget tradeoff all map onto design choices for the einstein autonomous loop (council dispatch, toolkit selection, generator-style proposal of candidate solutions).

## Open questions / connections
- Can an LLM-driven GA with population $\sim 100$ compete with classical GA at population $\sim 10^5$ on continuous geometric optimization (sphere packing, kissing configurations)? The MOF surface-area result suggests yes for discrete combinatorial encodings but is silent on continuous coordinates.
- The "near-target" failure mode (no parent satisfies the band) is structurally identical to basin-rigidity failures in Einstein Arena — when does an LLM gene-mixer escape vs stay trapped?
- Extends ReAct (Yao et al.) and MRKL into materials science; complements HuggingGPT-style model selection. Open: how to scale beyond fine-tuned model registry to a shared open repository.
