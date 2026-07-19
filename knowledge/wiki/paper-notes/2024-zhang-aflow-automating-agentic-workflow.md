---
type: note
kind: paper-relevance
about: 2024-zhang-aflow-automating-agentic-workflow
canonical: ../../domains/ai-agents/source/2024-zhang-aflow-automating-agentic-workflow.md
---

# Relevance note — AFlow: Automating Agentic Workflow Generation

Canonical distillation: [`2024-zhang-aflow-automating-agentic-workflow.md`](../../domains/ai-agents/source/2024-zhang-aflow-automating-agentic-workflow.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. Relevant only as meta-methodology: the math-solving protocol in this repo is itself a hand-built agentic workflow, and AFlow's "operators + MCTS over code-graphs + tree-structured failure memory" maps directly onto the self-improvement loop (council dispatch, gap-detect, failure-finding). It suggests that the council/operator choice and ordering could in principle be search-optimized rather than hand-fixed.

## Open questions / connections
- Could AFlow-style MCTS be applied over the council-dispatch + technique-library to auto-tune which personas + operators to invoke per problem category?
- AFlow requires a numerical evaluator; on math problems we have triple-verified scores, so the loop closes — but operator search would need a budget model since each rollout is expensive.
- Extends ADAS (Hu et al. 2024) (linear heuristic code-search) and GPTSwarm (Zhuge et al. 2024) (RL over graph workflows) by combining code-expressivity with MCTS; leaves open whether discovered workflows transfer across task families.
