---
type: note
kind: paper-relevance
about: 2024-zhang-cybench-framework-evaluating-cybersecurity
canonical: ../../domains/ai-agents/source/2024-zhang-cybench-framework-evaluating-cybersecurity.md
---

# Relevance note — Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models

Canonical distillation: [`2024-zhang-cybench-framework-evaluating-cybersecurity.md`](../../domains/ai-agents/source/2024-zhang-cybench-framework-evaluating-cybersecurity.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — this is an agent-evaluation benchmark for cybersecurity CTFs, orthogonal to math-optimization on Einstein Arena. Useful only as a methodological reference for FST-style human-time difficulty calibration and subtask decomposition of compound problems, both of which loosely parallel the per-problem inventory and step-wise math-solving protocol used in this repo.

## Open questions / connections
- Does FST remain a clean difficulty predictor as agents scale, or does it bend (analog: does human solve-time on Arena problems predict agent solve-time)?
- Which "insight" tasks (e.g., Robust CBC length-extension) require multi-hop reasoning that current subtask hints can't unlock — what's the right granularity of decomposition?
- Extends Yang et al. 2023 InterCode-CTF (high-school) and Shao et al. 2024 NYU CTF Bench (university) to professional difficulty; complements Bhatt et al. 2024 CYBERSECEVAL and Tihanyi et al. 2024 cyber-QA.
