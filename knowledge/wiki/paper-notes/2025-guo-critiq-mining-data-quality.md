---
type: note
kind: paper-relevance
about: 2025-guo-critiq-mining-data-quality
canonical: ../../domains/ai-agents/source/2025-guo-critiq-mining-data-quality.md
---

# Relevance note — CritiQ: Mining Data Quality Criteria from Human Preferences

Canonical distillation: [`2025-guo-critiq-mining-data-quality.md`](../../domains/ai-agents/source/2025-guo-critiq-mining-data-quality.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The agent-loop pattern — manager/worker split, reflection on wrong cases, accuracy-gated criterion updates, knowledge-base-seeded initialization from ~30 human anchors — is structurally relevant to the einstein self-improvement loop (gap→search→ingest→distill→page) and to council-dispatch, where personas could similarly evolve via reflection on per-question accuracy rather than be hand-curated.

## Open questions / connections
- Does the accuracy-gated update rule (only accept $c'_i$ if $\text{acc}'_i \geq \text{acc}_i$) transfer to multi-step math-reasoning critique, where "accuracy on 30 pairs" has no clean analogue?
- The knowledge base is built by Jaccard-dedup of paper-extracted criteria (threshold 0.3) — would this same pipeline produce a usable persona/heuristic base from mathematician biographies for einstein's council?
- Extends TextGrad (Yuksekgonul 2024) and Reflexion-style (Shinn 2023) reflection by adding explicit per-criterion accuracy bookkeeping; relates to QuRating (Wettig 2024) which used hand-defined criteria.
