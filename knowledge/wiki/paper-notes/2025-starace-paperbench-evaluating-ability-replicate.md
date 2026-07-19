---
type: note
kind: paper-relevance
about: 2025-starace-paperbench-evaluating-ability-replicate
canonical: ../../domains/ai-agents/source/2025-starace-paperbench-evaluating-ability-replicate.md
---

# Relevance note — PaperBench: Evaluating AI's Ability to Replicate AI Research

Canonical distillation: [`2025-starace-paperbench-evaluating-ability-replicate.md`](../../domains/ai-agents/source/2025-starace-paperbench-evaluating-ability-replicate.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — PaperBench measures ML-research-replication agents, not math-optimization agents. Indirectly relevant to einstein's autonomous-loop design: it documents the long-horizon failure mode (agents terminate early, can't sustain multi-step plans, code-without-execution gap) and shows scaffolding choice (BasicAgent vs IterativeAgent) shifts scores by $>10$ pts and is model-specific — a cautionary data point for the einstein loop's own scaffolding.

## Open questions / connections
- Does an "iterative, no-early-stop, prompt-to-continue" scaffold help or hurt math-optimization agents the way it helps o1 but hurts Claude here? Worth testing on einstein's loop.
- The Code Development → Execution → Result Match drop-off (e.g. Claude $35.4\% \to 1.8\% \to 0.7\%$) mirrors einstein's "score-claim without triple-verify" failure mode — points to a structural agent weakness, not paper-specific.
- Extends MLE-Bench / SWE-bench / RE-Bench (already in wiki source/) by targeting from-scratch *paper* replication rather than ML-engineering tasks or bug fixes; same family of long-horizon-agent evals.
