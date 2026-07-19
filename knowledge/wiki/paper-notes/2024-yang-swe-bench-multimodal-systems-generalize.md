---
type: note
kind: paper-relevance
about: 2024-yang-swe-bench-multimodal-systems-generalize
canonical: ../../domains/ai-agents/source/2024-yang-swe-bench-multimodal-systems-generalize.md
---

# Relevance note — SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?

Canonical distillation: [`2024-yang-swe-bench-multimodal-systems-generalize.md`](../../domains/ai-agents/source/2024-yang-swe-bench-multimodal-systems-generalize.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is a software-engineering agent benchmark, not a math-optimization result. Tangentially relevant to the autonomous-loop design (current branch `feat/autonomous-loop`): documents how language-agnostic, tool-light agent scaffolds (SWE-agent) generalize better than rigid localize-then-repair pipelines (Agentless, Moatless) that hard-code per-language parsers.

## Open questions / connections
- Extends SWE-bench (Jimenez et al. 2024a) along language and modality axes; complements MLE-bench, HumanEval, RepoBench for agent eval.
- Open: how to build agents that generalize across languages without per-language tool re-engineering — implicates ACI design over AST-graph design.
- Open: scope extensions to more languages (C++, Rust), more modalities (audio), and more JS domain libraries.
