---
type: note
kind: paper-relevance
about: 2024-xiao-cellagent-llm-driven-multi-agent-framework
canonical: ../../domains/ai-agents/source/2024-xiao-cellagent-llm-driven-multi-agent-framework.md
---

# Relevance note — CellAgent: An LLM-driven Multi-Agent Framework for Automated Single-cell Data Analysis

Canonical distillation: [`2024-xiao-cellagent-llm-driven-multi-agent-framework.md`](../../domains/ai-agents/source/2024-xiao-cellagent-llm-driven-multi-agent-framework.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background on multi-agent LLM orchestration: Planner/Executor/Evaluator separation, hierarchical decision-making, code-sandbox isolation, and self-iterative optimization via MLLM-judged visualizations — directly relevant to designing einstein's own autonomous-loop agent (council dispatch → execute → evaluate → re-plan). No direct arena/math tie; the domain is scRNA-seq, but the architecture patterns inform agent-system design.

## Open questions / connections
- How to extend self-evaluation beyond GPT-4V image judgment to richer optimization targets when users have specific preferences — gestures toward configurable evaluator prompts.
- How to let users register new tools at runtime so the agent aligns with shifting requirements — an open AI-for-science research direction.
- Comparison to MetaGPT-style software-engineering multi-agent frameworks: what biological-domain priors actually buy vs generic agent scaffolding (ablation not reported).
