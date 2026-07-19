---
type: note
kind: paper-relevance
about: 2026-sherwood-alphazero-coding-agents
canonical: ../../domains/ai-agents/source/2026-sherwood-alphazero-coding-agents.md
---

# Relevance note — Frontier Coding Agents Implement an AlphaZero Self-Play Pipeline for Connect Four

Canonical distillation: [`2026-sherwood-alphazero-coding-agents.md`](../../domains/ai-agents/source/2026-sherwood-alphazero-coding-agents.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — the paper is about AI-building-AI capability forecasting and sandbagging detection, not math optimization. Mild methodological relevance: Bradley–Terry MLE for ranking under noisy paired comparisons could inform any future agent-vs-agent or solver-anchored evaluation of arena submissions.

## Open questions / connections
- Can the proof-of-concept scale to larger state spaces (Mancala, Checkers, Othello, Chess, Shogi, Go) to give a more discriminating ceiling-free signal?
- Is GPT-5.4's low time-budget usage actually strategic sandbagging vs. evaluation-coded prompt sensitivity? Resolution likely requires thinking-block / interpretability access.
- Connects to METR time-horizon trend, Epoch Capabilities Index, PaperBench/MLAgentBench/RE-Bench, and the sandbagging literature (Van Der Weij, Tice, Hofstätter, Meinke).
