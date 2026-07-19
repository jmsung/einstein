---
type: note
kind: paper-relevance
about: 2025-chai-scimaster-towards-general-purpose-scientific
canonical: ../../domains/ai-agents/source/2025-chai-scimaster-towards-general-purpose-scientific.md
---

# Relevance note — SciMaster: Towards General-Purpose Scientific AI Agents, Part I. X-Master as Foundation: Can We Lead on Humanity's Last Exam?

Canonical distillation: [`2025-chai-scimaster-towards-general-purpose-scientific.md`](../../domains/ai-agents/source/2025-chai-scimaster-towards-general-purpose-scientific.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The relevance is *agent architecture*, not math: the scattered-and-stacked (5 Solvers → Critics → Rewriters → Selector) pattern, code-as-interaction-language, and Initial Reasoning Guidance are templates the autonomous-loop agent could borrow for council dispatch and gap-detect synthesis — particularly the empirical finding that rewriter-synthesis-over-N-solutions is where most of the gain lives (5.6-pt jump vs 3.9 for critic).

## Open questions / connections
- Does the scattered-and-stacked workflow improve quantitative math optimization (continuous score), not just multiple-choice/short-answer accuracy? HLE judges with o3-mini; arena problems are exact numerical.
- The Critic→Rewriter rewrite gain (5.6 pts) dominates the Critic's own gain (3.9 pts) — what's the analog for a numerical optimizer council? Maybe "rewrite five strategy.md drafts after seeing all five" rather than per-persona critique.
- Initial Reasoning Guidance (first-person self-statements injected post-`<think>`) is a cheap alternative to finetuning for agent behavior — could be useful for persona dispatch where personas currently re-derive their stance each call.
- Open question: does code-as-interaction generalize to long-running compute jobs (Modal) rather than sub-second tool calls? Paper only shows sub-second `web_search`/`web_parse`.
