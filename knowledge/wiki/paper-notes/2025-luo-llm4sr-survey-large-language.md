---
type: note
kind: paper-relevance
about: 2025-luo-llm4sr-survey-large-language
canonical: ../../domains/ai-agents/source/2025-luo-llm4sr-survey-large-language.md
---

# Relevance note — LLM4SR: A Survey on Large Language Models for Scientific Research

Canonical distillation: [`2025-luo-llm4sr-survey-large-language.md`](../../domains/ai-agents/source/2025-luo-llm4sr-survey-large-language.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Direct tie: this is the field-overview frame for the autonomous-loop agent itself — `cycle_runner`, the council-dispatch + gap-detect + wiki-distill loop, the "novelty/validity/clarity" feedback discipline, and FunSearch-style program-search-with-verifier all sit inside this survey's taxonomy. Especially relevant: FunSearch (Romera-Paredes 2024) is the closest published analog to einstein's verifier-grounded math optimization loop, and MOOSE-Chem's "evolutionary unit" + LMI decomposition is a candidate pattern for the council→hypothesis pipeline.

## Open questions / connections
- Validity checking is the bottleneck across the field — every method outside FunSearch/HypoGeniC/LLM-SR/SGA relies on LLM heuristics; einstein's triple-verify discipline is one concrete answer to this gap.
- Evolutionary algorithms (island-based, evolutionary unit) for hypothesis recombination are underexplored in einstein's current loop — possible upgrade path for council synthesis.
- Multi-inspiration composition (MOOSE-Chem's $P(h|b)$ decomposition) suggests a structured way to combine persona-generated questions rather than treating them as a flat list.
- No direct math-arena prior: the survey covers chemistry, social science, ML — no per-problem extremal-combinatorics benchmark exists in this lineage.
