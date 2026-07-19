---
type: note
kind: paper-relevance
about: 2025-xu-robustflow-towards-robust-agentic
canonical: ../../domains/ai-agents/source/2025-xu-robustflow-towards-robust-agentic.md
---

# Relevance note — RobustFlow: Towards Robust Agentic Workflow Generation

Canonical distillation: [`2025-xu-robustflow-towards-robust-agentic.md`](../../domains/ai-agents/source/2025-xu-robustflow-towards-robust-agentic.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The math-solving protocol's council-dispatch and self-improvement loop are themselves agentic workflows — robustness-under-paraphrase is the failure mode that produces drift when the same problem statement gets re-framed across sessions. The ScPO recipe (canonicalize → vote-weight → DPO) is a plausible training-time fix for council-output consistency, and the node-chain + reachability F1 metrics are reusable for measuring whether the protocol produces stable trajectories on identical Einstein problems.

## Open questions / connections
- Does ScPO scale to *task-level* (long-horizon) workflows where a single canonical DAG may not exist, or only to query-level synthesis?
- Robustness here is measured against synonymous queries, not against *adversarial restatements that change difficulty cues* — would the same training regime hold under shifted persona/context priors (the analog of council-dispatch reframing)?
- Extends ScoreFlow (DPO on execution score alone) by adding the self-consistency vote term; ablation of $\lambda_q$ would clarify how much of the gain is voting vs. instruction-augmented SFT.
