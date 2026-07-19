---
type: note
kind: paper-relevance
about: 2025-lin-eco-llm-driven-efficient-code
canonical: ../../domains/ai-agents/source/2025-lin-eco-llm-driven-efficient-code.md
---

# Relevance note — ECO: An LLM-Driven Efficient Code Optimizer for Warehouse Scale Computers

Canonical distillation: [`2025-lin-eco-llm-driven-efficient-code.md`](../../domains/ai-agents/source/2025-lin-eco-llm-driven-efficient-code.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Of mild methodological interest: the wiki-first / mine-historical-commits-into-anti-patterns approach is structurally parallel to the einstein self-improvement loop (mine past sessions → distill anti-patterns → embed-search for new instances → LLM apply → verify), and the ReAct-beats-CoT-for-targeted-edits finding could inform council-dispatch prompting choices.

## Open questions / connections
- Could a "performance anti-pattern" mining loop be adapted to mine "optimizer anti-patterns" from `knowledge/wiki/findings/dead-end-*.md` and auto-suggest them as failure-mode checks on new branches?
- Vector-similarity-on-code-diffs outperforming whole-function queries — does qmd's embedding choice for `einstein-wiki-source` use diff-shaped or whole-doc embeddings, and would diff-shaped help?
- Extends Garg et al. (DeepDev-Perf 2022), Shypula et al. (PIE/ICLR 2024), Chen et al. (learning to improve code efficiency 2022) — the open frontier is multi-file edits and proactive (in-IDE) suggestion.
