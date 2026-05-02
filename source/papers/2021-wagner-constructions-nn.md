---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2104.14516
source_local: sources/2021-wagner-constructions-nn.pdf
cites:
  - ../papers/2024-charton-patternboost.md
  - ../papers/2023-romera-paredes-funsearch.md
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2022-fawzi-alphatensor.md
  - ../papers/2025-georgiev-math-exploration.md
  - findings/strategic-approach.md
  - strategy.md
---

[[../home]] | [[../index]]

# Wagner — Constructions in Combinatorics via Neural Networks

**Authors:** Adam Zsolt Wagner
**Year:** 2021 (arXiv:2104.14516)

## Summary

The seminal "RL for extremal combinatorics" paper. Wagner uses the **deep cross-entropy method** (a simple policy-gradient RL algorithm) to find explicit constructions and counterexamples in graph theory and extremal combinatorics, with **zero domain knowledge** baked into the agent. The agent generates candidate objects (e.g., graphs, matrices) sequentially as token streams, receives a fitness score, and updates its policy.

Headline results: refutations of conjectures by Brualdi-Cao on permanents of pattern-avoiding matrices, and counterexamples to several open conjectures about adjacency/distance eigenvalues of graphs. None of the refuted conjectures are individually famous, but the *generality* of the result — RL works on combinatorial-construction problems out of the box — is what mattered.

This paper is the founding document of the entire AI-for-extremal-combinatorics research thread. PatternBoost (2024), AlphaEvolve (2025), and Georgiev et al. (2025) all explicitly cite it as the launching point.

## Key Techniques

- **Deep cross-entropy method** — sampling-based policy improvement: keep top-q% of trajectories, train policy to imitate them
- **Token-stream construction** — combinatorial object emitted as a sequence (graph adjacency upper triangle, matrix entries, etc.)
- **Sparse reward** — agent gets a single score at the end of the trajectory; no shaping
- **Domain-agnostic** — same algorithm applied to ~10 different conjecture-refutation tasks with minimal modification
- **Pure RL, no LLM** — pre-LLM era; demonstrates that simple RL is enough for moderate-sized problems

## Relevance to Einstein Arena

### Foundational methodology
This is the RL-only baseline that PatternBoost (transformer-augmented), FunSearch (LLM-augmented), and AlphaEvolve (ensemble + verifier) all extend. Reading Wagner-2021 first explains why so many of the later papers' headline results are "we tried Wagner-style RL but with [LLM/transformer/ensemble] and got further."

### Direct portability to arena problems
Many arena problems map onto Wagner's setup almost without modification: P14 circle packing, P15/P16 Heilbronn, P17 hexagon packing, P19 difference bases. The cross-entropy method is implementable in 100 lines of PyTorch and runs on a single GPU.

### Reality check on RL-only ceilings
Most of the conjectures Wagner refuted are small (n ≤ 20) and structurally weak (no obvious obstruction). When SOTA on arena problems is already past the "obvious construction" stage, pure RL plateaus quickly. This paper is the right baseline to *compare against* — not the right method to *use* — on arena problems where AlphaEvolve / Ganzhinov / structured constructions already exist.

### Cross-entropy vs. funsearch tradeoffs
Wagner's CEM is much more sample-efficient than FunSearch on small problems but cannot make algorithmic leaps (no concept of "code"). For arena problems with bounded structure and exact verifiers (P14, P19), CEM may be the right tool.

## Limitations

- Single-agent, no curriculum, no transfer between problems
- No structural inductive bias — every problem starts from scratch
- Token-stream representation is wasteful for symmetric problems (no equivariance)
- Reward sparsity makes long-horizon tasks (large n) slow to learn
- The refuted conjectures are minor; this paper's importance is methodological, not result-driven

## See Also

- [[2024-charton-patternboost]] — direct successor, transformer-augmented
- [[2023-romera-paredes-funsearch]] — LLM-augmented programmatic search
- [[2025-novikov-alphaevolve]] — full ensemble pipeline
- [[2022-fawzi-alphatensor]] — RL on a structured tensor-decomposition game
- [[2025-georgiev-math-exploration]] — 67-problem benchmark
