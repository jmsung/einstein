---
type: note
kind: paper-relevance
about: 2024-chan-mle-bench-evaluating-machine-learning
canonical: ../../domains/ai-agents/source/2024-chan-mle-bench-evaluating-machine-learning.md
---

# Relevance note — MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering

Canonical distillation: [`2024-chan-mle-bench-evaluating-machine-learning.md`](../../domains/ai-agents/source/2024-chan-mle-bench-evaluating-machine-learning.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — MLE-bench is an ML-engineering agent benchmark, not a math-optimization one. Closest relevance is methodological: it is a sibling to the autonomous-loop infrastructure being built in `cb-feat-autonomous-loop/` and offers a concrete template for scaffold comparison (AIDE tree search vs ReAct-style MLAB vs OpenHands), pass@k scaling curves, contamination probes (token familiarity, description obfuscation), and the *cherry-picking-forbidden* discipline already encoded in this repo's `cycle-discipline.md`.

## Open questions / connections
- Does an AIDE-style tree search over candidate optimizer configurations transfer from Kaggle ML pipelines to Einstein Arena math-optimization runs (basin hops, Remez exchanges, LP relaxations)?
- Why does extra compute (2× GPU, 100 h) yield only marginal gains — is the ceiling scaffold quality (failure to iterate / debug) rather than raw compute, mirroring the project's "hammer the optimizer harder ≠ progress" anti-pattern?
- The Dolos + log-inspection rule-breaking detector is a direct analogue to a needed audit tool for the autonomous-loop council dispatch: how to verify that persona subagents actually consult the wiki rather than re-derive from training?
- The token-familiarity test (Carlini-style) is a cheap contamination probe — could be applied to detect whether the LLM-distill step has memorized arxiv math sources verbatim.
