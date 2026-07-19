---
type: note
kind: paper-relevance
about: 2023-hong-metagpt-meta-programming-multi-agent
canonical: ../../domains/ai-agents/source/2023-hong-metagpt-meta-programming-multi-agent.md
---

# Relevance note — MetaGPT: Meta Programming for Multi-Agent Collaborative Framework

Canonical distillation: [`2023-hong-metagpt-meta-programming-multi-agent.md`](../../domains/ai-agents/source/2023-hong-metagpt-meta-programming-multi-agent.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as design reference for the einstein agent's own infrastructure — the *council dispatch* pattern (specialized personas writing structured outputs), structured message handoffs, and the executable-feedback / self-correction loop echo what `.claude/rules/council-dispatch.md` and `self-improvement-loop.md` already prescribe; the SOP-driven structured-output discipline is the same intuition behind mandatory wiki frontmatter + cycle-log discipline.

## Open questions / connections
- Does SOP-style structured handoff between mathematician personas (PRD-analog → architecture-analog → execution) outperform the current free-form "each persona writes 2–3 questions" council dispatch? Worth testing on one arena problem.
- The recursive constraint-prompt rewriting in Appendix A is a concrete implementation of "agent rewrites its own rules from cycle feedback" — could inspire a `/agent-reflect` step that proposes edits to `knowledge/wiki/personas/*.md` from cycle-log outcomes.
- Extends NLSOM (Zhuge 2023) and ChatDev (Qian 2023); leaves open whether SOPs help for *research / proof* tasks (vs the well-scoped software-dev SOP that already exists in industry).
