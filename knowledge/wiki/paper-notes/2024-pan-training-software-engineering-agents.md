---
type: note
kind: paper-relevance
about: 2024-pan-training-software-engineering-agents
canonical: ../../domains/ai-agents/source/2024-pan-training-software-engineering-agents.md
---

# Relevance note — Training Software Engineering Agents and Verifiers with SWE-Gym

Canonical distillation: [`2024-pan-training-software-engineering-agents.md`](../../domains/ai-agents/source/2024-pan-training-software-engineering-agents.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
General background; no direct arena tie. The relevant transferable ideas for the einstein autonomous-loop agent are (a) outcome-supervised verifier reranking of $k$ rollouts as a concrete inference-time scaling lever for the council/optimizer loop, and (b) per-instance trajectory capping as a remedy for long-tail success bias when distilling rollouts back into the wiki.

## Open questions / connections
- On-policy RL (PPO) for self-improvement beyond rejection sampling — currently regressive at 32B; matches our council/skill-library "promotion" tension.
- Process-reward (PRM) vs outcome-reward (ORM) verification — only ORM tested; PRM at trajectory-step granularity is open.
- Environment synthesis (auto-generated tasks/tests) as the next bottleneck — analogous to wiki gap-detection → question filing.
- Long-tail repeated-sampling distribution (Brown et al. "Large Language Monkeys") as a model for compute-budget allocation across the 23 arena problems.
