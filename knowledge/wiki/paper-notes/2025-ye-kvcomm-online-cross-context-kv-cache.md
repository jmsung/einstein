---
type: note
kind: paper-relevance
about: 2025-ye-kvcomm-online-cross-context-kv-cache
canonical: ../../domains/ai-agents/source/2025-ye-kvcomm-online-cross-context-kv-cache.md
---

# Relevance note — KVCOMM: Online Cross-context KV-cache Communication for Efficient LLM-based Multi-agent Systems

Canonical distillation: [`2025-ye-kvcomm-online-cross-context-kv-cache.md`](../../domains/ai-agents/source/2025-ye-kvcomm-online-cross-context-kv-cache.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is LLM-systems infrastructure (multi-agent inference latency), not math optimization. It is only loosely relevant to einstein's council-dispatch pattern: if the agent ever runs many parallel mathematician personas sharing long problem-statement prefixes, KV-cache reuse across personas would attack the same redundancy KVCOMM targets.

## Open questions / connections
- Does anchor-pool retrieval generalize to long math-reasoning chains where shared context is symbolic (formulae) rather than natural language?
- How does the offset-variance characterization interact with reasoning models (e.g., Qwen-QwQ, o1-style) whose KV-caches encode latent chain-of-thought?
- Extends DroidSpeak [27], CacheBlend [58], KVLink [56], PromptCache [10]; relies on RoPE [37] rotation properties for key-cache portability.
