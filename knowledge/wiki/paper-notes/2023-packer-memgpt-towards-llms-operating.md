---
type: note
kind: paper-relevance
about: 2023-packer-memgpt-towards-llms-operating
canonical: ../../domains/ai-agents/source/2023-packer-memgpt-towards-llms-operating.md
---

# Relevance note — MemGPT: Towards LLMs as Operating Systems

Canonical distillation: [`2023-packer-memgpt-towards-llms-operating.md`](../../domains/ai-agents/source/2023-packer-memgpt-towards-llms-operating.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The paging/heartbeat/function-chaining pattern is relevant to the autonomous-loop agent infrastructure (context management across long cycles, wiki retrieval, multi-hop lookups across `knowledge/wiki/` + `knowledge/source/`) rather than to any specific Einstein Arena math problem.

## Open questions / connections
- Can OS-style swap policies be learned (vs prompt-engineered) for better eviction/recall decisions?
- How does memory-pressure-driven self-summarization compare against external RAG with a learned retriever for long-horizon coherence?
- Extends FLARE (Jiang et al. 2023) and ReAct (Yao et al. 2022) by giving the agent write-access to its own working memory, not just read-access to external corpora.
