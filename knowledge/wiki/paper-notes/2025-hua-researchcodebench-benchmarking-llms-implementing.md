---
type: note
kind: paper-relevance
about: 2025-hua-researchcodebench-benchmarking-llms-implementing
canonical: ../../domains/ai-agents/source/2025-hua-researchcodebench-benchmarking-llms-implementing.md
---

# Relevance note — ResearchCodeBench: Benchmarking LLMs on Implementing Novel Machine Learning Research Code

Canonical distillation: [`2025-hua-researchcodebench-benchmarking-llms-implementing.md`](../../domains/ai-agents/source/2025-hua-researchcodebench-benchmarking-llms-implementing.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only to the meta-question of how reliably an autonomous-loop agent can be expected to faithfully implement a freshly-ingested research paper into `src/einstein/` — sets a realistic ceiling (<40% on novel ML code) on agent-driven code reproduction, which argues for the wiki's distill-first-then-implement loop rather than direct paper→code generation.

## Open questions / connections
- Does the functional-error dominance (59%) replicate on math-optimization code (LP/SDP/CMA-ES), or are math kernels more brittle to off-by-one/sign errors than ML code?
- Would a `wiki-first` retrieval step before code completion close the paper-context gap that hurts LLaMA models? (The wiki distillation may be the right "compressed paper" format these models can actually use.)
- Extends Jimenez et al. (SWE-Bench), SciCode (Tian 2024), CORE-Bench (Siegel 2024), PaperBench (Starace 2025) — but is the first to isolate *post-cutoff novelty* with timeline-controlled subsets.
