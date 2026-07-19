---
type: note
kind: paper-relevance
about: 2025-wan-loongflow-directed-evolutionary-search
canonical: ../../domains/ai-agents/source/2025-wan-loongflow-directed-evolutionary-search.md
---

# Relevance note — LoongFlow: Directed Evolutionary Search via a Cognitive Plan-Execute-Summarize Paradigm

Canonical distillation: [`2025-wan-loongflow-directed-evolutionary-search.md`](../../domains/ai-agents/source/2025-wan-loongflow-directed-evolutionary-search.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Directly relevant to the einstein autonomous-loop on `feat/autonomous-loop` — LoongFlow is a current-SOTA reference architecture for the exact category this repo is building (PES = effectively the math-solving protocol's UNDERSTAND→PLAN→EXECUTE→LOOK-BACK→FAILURE-LOG steps, MAP-Elites + Island + Boltzmann = a population-level analogue to the wiki/findings/skill-library memory) and it explicitly competes on shared problems including Autocorrelation II (P15/P16-family), Circle Packing in a Square (P3-family), Hexagon Packing, Uncertainty Inequality (P11-family), and Erdős-minimum-overlap.

## Open questions / connections
- The Autocorrelation II $0.9027$ result was reached without disclosed construction — worth ingesting the GitHub repo (`baidu-baige/LoongFlow`) to extract the actual function/sequence and triple-verify against our P15/P16 evaluators.
- Lineage-based context retrieval over `(plan, summary, parent_id)` chains is an alternative to RAG/qmd vector search for the wiki-first lookup — would the einstein wiki benefit from explicit parent-chain links in `findings/` frontmatter?
- Behavior descriptors are hand-picked (complexity × length); the paper flags "unsupervised diversity metrics for novel domains" as open — directly relevant to choosing $\Phi(\cdot)$ for arena problems whose code is short but whose configurations are high-dim.
- No theoretical guarantees on the entropy-Boltzmann schedule; the $\tau\propto\exp(-\lambda H)$ rule is heuristic and could collapse under noisy reward.
- Baselines compared are OpenEvolve/ShinkaEvolve only; no comparison to FunSearch or AlphaEvolve under matched compute.
