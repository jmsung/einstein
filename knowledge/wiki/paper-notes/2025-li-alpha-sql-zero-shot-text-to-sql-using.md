---
type: note
kind: paper-relevance
about: 2025-li-alpha-sql-zero-shot-text-to-sql-using
canonical: ../../domains/ai-agents/source/2025-li-alpha-sql-zero-shot-text-to-sql-using.md
---

# Relevance note — Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search

Canonical distillation: [`2025-li-alpha-sql-zero-shot-text-to-sql-using.md`](../../domains/ai-agents/source/2025-li-alpha-sql-zero-shot-text-to-sql-using.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie — Text-to-SQL is out of scope for sphere packing / autocorrelation / extremal problems. **Relevant only as a methodology reference**: MCTS + LLM-as-action-model + self-consistency reward is a candidate template for the autonomous-loop agent itself (e.g., council dispatch + action-space exploration on math problems), complementing rStar and AFlow already in the wiki.

## Open questions / connections
- Can the self-consistency reward generalize to math optimization where "execution equivalence" is harder to define (numerical equality with tolerance? triple-verify agreement?).
- Action-space design for math problems: what is the Text-to-SQL action set's analog for sphere packing / kissing configurations (e.g., "select parameterization", "polish basin", "verify")?
- Extends rStar (Qi et al. 2024) MCTS-with-self-consistency and CHASE-SQL multi-path decomposition; relates to AFlow (Zhang et al. 2025) for automated workflow generation already in agent literature.
