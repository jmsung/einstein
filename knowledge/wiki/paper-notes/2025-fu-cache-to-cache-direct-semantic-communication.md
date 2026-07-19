---
type: note
kind: paper-relevance
about: 2025-fu-cache-to-cache-direct-semantic-communication
canonical: ../../domains/ai-agents/source/2025-fu-cache-to-cache-direct-semantic-communication.md
---

# Relevance note — Cache-to-Cache: Direct Semantic Communication Between Large Language Models

Canonical distillation: [`2025-fu-cache-to-cache-direct-semantic-communication.md`](../../domains/ai-agents/source/2025-fu-cache-to-cache-direct-semantic-communication.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Potentially relevant to the council-dispatch + self-improvement-loop architecture as a future efficiency play — if multiple persona-LLMs are dispatched, KV-cache fusion could replace token-level text handoffs, but current arena work is single-model and the wiki is the durable persistence layer, not in-context cache.

## Open questions / connections
- Does C2C preserve numerical/symbolic precision needed for math problem-solving, or only fuzzy semantic context? (paper benchmarks are multi-choice QA, not math reasoning beyond GSM8K.)
- Failure mode: a weaker Sharer can mislead a stronger Receiver (accounting example) — fusion lacks the "triple-verify" structural correction that text debate offers.
- Scales to $O(N)$ fusers via unified latent space (Sec A.5.2) — extension of intra-model KV-sharing (DroidSpeak, MiniCache) to cross-family cross-size.
