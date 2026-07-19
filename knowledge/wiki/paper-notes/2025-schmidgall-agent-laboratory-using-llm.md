---
type: note
kind: paper-relevance
about: 2025-schmidgall-agent-laboratory-using-llm
canonical: ../../domains/ai-agents/source/2025-schmidgall-agent-laboratory-using-llm.md
---

# Relevance note — Agent Laboratory: Using LLM Agents as Research Assistants

Canonical distillation: [`2025-schmidgall-agent-laboratory-using-llm.md`](../../domains/ai-agents/source/2025-schmidgall-agent-laboratory-using-llm.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as architectural precedent for the autonomous-loop branch — patterns like `mle-solver`'s top-program pool + batch-parallel exploration + LLM-reward scoring map directly onto the einstein cycle_runner's apply pipeline, and `paper-solver`'s scaffold→edit→compile loop mirrors the wiki distill→lint cycle.

## Open questions / connections
- Auto-reviewer optimism gap (6.1 vs 3.8) — is the same drift biasing LLM-as-reward in `mle-solver` (and by analogy, any LLM-graded score in our wiki_lint / distill pipeline)?
- Does top-program-pool + EDIT/REPLACE outperform a single-trajectory CMA-ES-style agent loop? Direct analogue to our parallel apply step.
- Co-pilot vs autonomous trade-off: human gates raise quality but hurt experimental throughput — mirrors our wiki-ingest human-gating decision.
- No reproducibility / variance numbers reported across seeds; agent-lab outputs may be high-variance like our cycle-log entries.
