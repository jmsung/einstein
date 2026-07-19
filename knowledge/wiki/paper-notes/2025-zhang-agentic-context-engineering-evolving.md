---
type: note
kind: paper-relevance
about: 2025-zhang-agentic-context-engineering-evolving
canonical: ../../domains/ai-agents/source/2025-zhang-agentic-context-engineering.md
---

# Relevance note — Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

Canonical distillation: [`2025-zhang-agentic-context-engineering.md`](../../domains/ai-agents/source/2025-zhang-agentic-context-engineering.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Directly informs the autonomous-loop agent architecture being built on this branch (`feat/autonomous-loop`): the wiki *is* the playbook, and ACE's grow-and-refine + incremental delta pattern is a principled alternative to monolithic `/wiki-learn` rewrites — preserving the detailed dead-end findings and triple-verify lore that brevity-biased rewrites would erase. Suggests adding bullet-level metadata (helpful/harmful counters) to wiki findings to enable Reflector-style attribution across cycles.

## Open questions / connections
- Can the Generator/Reflector/Curator split replace the current single-pass `/wiki-learn` flow without losing the human-attribution honesty layer (`author: agent|human|hybrid`)?
- ACE works without GT labels via execution feedback — analog for arena math: triple-verify disagreement as the Reflector signal instead of arena submission outcome.
- Bullet-level helpful/harmful counters resemble the cite-count promotion threshold (3+ cites → concept) in `wiki-attribution.md`; could be unified into one provenance system.
- Extends GEPA (Agrawal 2025) and Dynamic Cheatsheet (Suzgun 2025); compare against TextGrad (Yuksekgonul 2025) and Reflexion (Shinn 2023) for the council-dispatch loop.
