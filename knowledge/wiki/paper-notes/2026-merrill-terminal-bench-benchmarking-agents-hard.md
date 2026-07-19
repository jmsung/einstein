---
type: note
kind: paper-relevance
about: 2026-merrill-terminal-bench-benchmarking-agents-hard
canonical: ../../domains/ai-agents/source/2026-merrill-terminal-bench-benchmarking-agents-hard.md
---

# Relevance note — Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces

Canonical distillation: [`2026-merrill-terminal-bench-benchmarking-agents-hard.md`](../../domains/ai-agents/source/2026-merrill-terminal-bench-benchmarking-agents-hard.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card:

## Why it matters here
General background; no direct arena tie. Indirectly relevant as infrastructure context for the autonomous-loop agent — Terminal-Bench's Terminus 2 scaffold, Harbor harness, and failure-mode taxonomy (execution / coherence / verification; premature termination, weak verification) parallel the einstein agent's own cycle-discipline and triple-verify rules, and the empirical finding that *model choice >> scaffold choice* is a useful prior for compute-router decisions.

## Open questions / connections
- Saturation risk: authors predict Terminal-Bench 2.0 may be solved within a year — what task properties resist saturation (e.g., creative/adversarial reasoning gaps seen in human-medium / model-hard cells)?
- The MAST-derived taxonomy (Pan et al. 2025) collapses several subcategories as "irrelevant to our setup"; would a math/optimization-domain agent surface different failure modes (e.g., evaluator drift, precision loss)?
- No correlation between turns/tokens and success contradicts a common "more thinking = better" prior — suggests scaffold improvements should target failure-mode-specific fixes, not raw budget.
