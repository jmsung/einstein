---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2411.00566
source_local: sources/2024-charton-patternboost.pdf
cites:
  - ../papers/2021-wagner-constructions-nn.md
  - ../papers/2023-romera-paredes-funsearch.md
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2025-georgiev-math-exploration.md
  - ../papers/2025-ellenberg-generative-math.md
  - findings/strategic-approach.md
  - strategy.md
---

[[../home]] | [[../index]]

# Charton, Ellenberg, Wagner & Williamson — PatternBoost: Constructions in Mathematics with a Little Help from AI

**Authors:** François Charton, Jordan S. Ellenberg, Adam Zsolt Wagner, Geordie Williamson
**Year:** 2024 (arXiv:2411.00566)

## Summary

PatternBoost is a two-phase iterative algorithm for finding extremal-combinatorics constructions:

1. **Local phase**: a classical search algorithm (often a greedy heuristic) generates many candidate constructions and keeps the top-k by score.
2. **Global phase**: a transformer is trained on the top constructions, then samples from the trained transformer become seeds for the next local phase.

The transformer learns *patterns* implicit across the top constructions and re-injects them as inductive bias. Iterating local↔global produces a population that is both diverse (from local search) and structurally aligned with what works (from the transformer's learned distribution).

Headline results: PatternBoost finds best-known solutions to several long-standing problems and **constructs a counterexample to a conjecture that had been open for 30 years**. Performance varies by problem — some problems show large gains, others modest.

PatternBoost sits between Wagner-2021 (pure RL on a single problem) and FunSearch (LLM mutates Python heuristics) on the spectrum of "ML help for extremal combinatorics." It is the most accessible of the three for academic groups: a transformer is much smaller than a frontier LLM and can be trained on commodity GPUs.

## Key Techniques

- **Transformer as global mutator** — train a small transformer on top constructions, sample new candidates
- **Local-global alternation** — greedy/MCTS for local exploitation, transformer for global generalization
- **Tokenization of constructions** — map combinatorial objects (graphs, point sets) to token sequences
- **Iterative refinement** — each iteration's top-k seeds the next iteration; quality monotonically improves on average
- **Domain-light** — minimal hand-crafting of priors; works across multiple combinatorial domains

## Relevance to Einstein Arena

### Methodology family
PatternBoost is one of the four canonical "AI-assisted construction" methods alongside Wagner-2021 (pure RL), FunSearch (LLM-mutated programs), and AlphaEvolve (ensemble LLM + verifier). The arena's extremal-combinatorics problems (P1, P3, P14–P19, P22) all admit PatternBoost-style attacks: produce a tokenization, hand-craft a local search, train a transformer on top configurations, iterate.

### Open-source / commodity-compute
Unlike AlphaEvolve, PatternBoost is reproducible on academic infrastructure. This makes it the most realistic methodology to deploy *ourselves* on an arena problem, especially for problems where current SOTA has not been heavily attacked by AlphaEvolve already.

### Wagner co-author lineage
Wagner is a co-author of PatternBoost, AlphaEvolve, and Wagner-2021. The lineage of these three papers (RL → PatternBoost → AlphaEvolve) is a single research thread and the author sees these as complementary tools, not competitors. Reading them in order gives the cleanest picture of the field.

### Counterexample-finding
The "30-year-old conjecture refuted" headline is a methodological caveat — extremal combinatorics conjectures with no known structural obstruction are vulnerable to ML search. Several arena problems (especially the un-conquered ones) may be in this regime.

## Limitations

- Tokenization is problem-specific — needs hand-crafting per domain
- Transformer architecture and hyperparameters require tuning
- Performance is uneven across problems (the paper is honest about this)
- No theoretical guarantee — convergence is empirical
- Local search must be reasonably strong on its own; PatternBoost amplifies, doesn't replace, classical methods

## See Also

- [[2021-wagner-constructions-nn]] — Wagner's original RL-only paper
- [[2023-romera-paredes-funsearch]] — LLM-mutated programs
- [[2025-novikov-alphaevolve]] — full DeepMind successor
- [[2025-ellenberg-generative-math]] — open-source FunSearch (Ellenberg co-author)
- [[2025-georgiev-math-exploration]] — 67-problem benchmark
