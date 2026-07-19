---
type: note
kind: paper-relevance
about: 2023-bran-augmenting-large-language-models
canonical: ../../domains/ai-agents/source/2023-bran-augmenting-large-language-models.md
---

# Relevance note — Augmenting large language models with chemistry tools

Canonical distillation: [`2023-bran-augmenting-large-language-models.md`](../../domains/ai-agents/source/2023-bran-augmenting-large-language-models.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is an LLM-agent / tool-use paper, not a math-optimization paper. The transferable lessons are (a) tool-augmented ReAct loops vs bare-model reasoning, (b) the demonstrated failure of LLM-judge evaluators on fact-critical tasks (relevant to any council-dispatch or auto-grading scheme), and (c) safety/guardrail patterns for autonomous agents.

## Open questions / connections
- LLM-as-judge unreliability when ground truth requires domain expertise — argues for the project's expert/triple-verify discipline over agent self-grading.
- Reproducibility of closed-source LLM agents (5 reruns of the same task diverged in interpretation) — relevant to cycle-discipline replay claims.
- Tool quality bounds agent quality: retrosynthesis ceiling = underlying retro tool's ceiling, mirroring the optimizer/evaluator ceiling in arena work.
