---
type: note
kind: paper-relevance
about: 2024-hu-automated-design-agentic-systems
canonical: ../../domains/ai-agents/source/2024-hu-automated-design-agentic-systems.md
---

# Relevance note — Automated Design of Agentic Systems

Canonical distillation: [`2024-hu-automated-design-agentic-systems.md`](../../domains/ai-agents/source/2024-hu-automated-design-agentic-systems.md).
einstein-specific synthesis, preserved from the pre-ADR-0009 flat `source/` card during the domain-nested migration:

## Why it matters here
Direct relevance to the einstein autonomous-loop branch: same architectural pattern — meta-agent iterating over an archive of "stepping stones" (here: cycle-log + skill-library + findings) to compose ever-better problem solvers. Validates the design choice that **the archive itself is the compounding mechanism** and that crossover-via-LLM of prior fragments outperforms scratch generation. The "interestingness" prompt + self-reflection-for-novelty pattern is directly portable to the council-dispatch / question-filing layer.

## Open questions / connections
- Evaluation function is naive (val-set accuracy only); the paper flags more sophisticated evaluators (cost, latency, diversity-credit) as future work — same gap as einstein's single-metric cycle-log.
- Initialization paradox: hand-designed seeds help except on math, where empty-init wins via broader exploration. Implication for which einstein problems to warm-start vs cold-start.
- Stepping-stone analysis (ARC §4.1): the final winning agent's components first appeared at iterations 5/11/12 with low immediate fitness — argues against greedy pruning of low-score cycles.
- Extends FunSearch (Romera-Paredes 2024) from numeric programs to full agentic workflows; complements Voyager (skill-library accretion) and Self-Refine (single-agent reflection).
- No theoretical guarantee on coverage of the Turing-complete code space; archive curation is heuristic.
