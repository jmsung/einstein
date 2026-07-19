---
type: note
kind: paper-relevance
about: 2025-dong-agentic-reinforced-policy-optimization
canonical: ../../domains/ai-agents/source/2025-dong-agentic-reinforced-policy-optimization.md
---

# Relevance note — Agentic Reinforced Policy Optimization

Canonical distillation: [`2025-dong-agentic-reinforced-policy-optimization.md`](../../domains/ai-agents/source/2025-dong-agentic-reinforced-policy-optimization.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card:

## Why it matters here
General background; no direct arena tie. Relevant only if the einstein agent itself moves to RL-trained tool use — the entropy-spike-after-tool-call observation and macro-action policy gradient could inform how to budget exploration when the agent branches between optimizer calls, mpmath polishes, and wiki queries.

## Open questions / connections
- Does the entropy spike after tool calls reproduce for math-heavy tools (HiGHS LP solves, mpmath polish, basin-hopping returns) the way it does for web search?
- Can the macro-action GPG framing be adapted to reward-shaping over compute-routing decisions (local CPU vs MPS vs Modal) rather than just tool selection?
- Extends GRPO/DAPO/REINFORCE++ trajectory-level RL; leaves open whether entropy-based branching helps when tool feedback is deterministic (Python) vs informative-textual (search) — paper itself notes search introduces more uncertainty (Ob.3).
