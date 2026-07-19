---
type: note
kind: paper-relevance
about: 2024-liu-toward-team-ai-made-scientists
canonical: ../../domains/ai-agents/source/2024-liu-toward-team-ai-made-scientists.md
---

# Relevance note — Toward a Team of AI-made Scientists for Scientific Discovery from Gene Expression Data

Canonical distillation: [`2024-liu-toward-team-ai-made-scientists.md`](../../domains/ai-agents/source/2024-liu-toward-team-ai-made-scientists.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is a genomics multi-agent paper, not a math-optimization paper. The relevant transferable signal for the Einstein Arena agent is architectural: bounded write-run-audit review loops yield $\sim 1.4\times$ F1 lift after one round and diminishing returns after two, paralleling the council-dispatch + code-review structure in this repo.

## Open questions / connections
- Does a bounded $k$-round review budget similarly cap returns in math-optimizer code (e.g., $k=1$ catches most drift)?
- The "preprocessing is the bottleneck" finding suggests parsing/normalizing problem inputs may outweigh solver quality — analogous to specialize-before-optimize in math-solving-protocol step 7.
- Extends MetaGPT-style role decomposition; orthogonal to AI Scientist (Lu et al. 2024) which targets end-to-end paper writing rather than one analytical pipeline.
