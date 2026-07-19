---
type: note
kind: paper-relevance
about: 2026-ning-code-as-agent-harness
canonical: ../../domains/ai-agents/source/2026-ning-code-as-agent-harness.md
---

# Relevance note — Code as Agent Harness

Canonical distillation: [`2026-ning-code-as-agent-harness.md`](../../domains/ai-agents/source/2026-ning-code-as-agent-harness.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Direct tie to this repo's autonomous-loop branch: this paper *names* what the einstein agent's `.claude/rules/`, cycle-log, wiki-first protocol, council dispatch, and `mb/` tracking actually are — an agent harness, with code (rules, scripts, distillations, cycle logs) as its substrate. Useful as a vocabulary anchor for the self-improvement-loop and cycle-discipline rules; the "evolution agent" and "governed harness mutation" sections (§3.5) map onto how this repo lets the agent author wiki pages under attribution. No math content for the 23 arena problems themselves.

## Open questions / connections
- Harness-level evaluation: how to measure self-improvement beyond per-cycle task success — relevant to `docs/agent/cycle-log.md` and `metrics.md`.
- Regression-free harness evolution: when the agent edits its own rules / skills, how to prevent silent capability loss — relevant to any future `/agent-reflect` that mutates `.claude/rules/`.
- Semantic verification under incomplete oracles: matches the project's triple-verify axiom (arena verifier is opaque/expensive) and P9/P14/P17 verifier-drift findings.
- Shared program state across multi-agent runs: relevant if council dispatch ever moves from "each persona writes a question" to "personas share a workspace."
