---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2506.16750
cites:
  - problem-3-autocorrelation/strategy.md
  - problem-3-autocorrelation/literature.md
  - ../papers/2025-jaech-autoconvolution.md
---

[[../home]] | [[../index]]

# Boyer & Li — An Improved Example for an Autoconvolution Inequality

**Authors:** Christopher Boyer, Zane Kun Li
**Year:** 2025
**Venue:** arXiv preprint (math.CA, math.CO, math.NT)

## Summary

Boyer and Li construct a nonnegative step function with 575 equally spaced intervals achieving a ratio of approximately 0.901564 for the second autoconvolution inequality, surpassing DeepMind's AlphaEvolve result (0.8962) which used only 50 intervals. The key finding is that classical optimization methods (simulated annealing + gradient-based) with more intervals outperform LLM-based evolutionary approaches.

## Key Techniques

- Simulated annealing optimization
- Gradient-based optimization refinement
- Step function construction with uniform spacing (575 intervals)

## Relevance to Einstein Arena

Directly relevant to **Problem 3 (Second Autocorrelation Inequality)**. Demonstrates that increasing the number of intervals (n) beyond what AlphaEvolve used can break through apparent plateaus. The SA + gradient pipeline is directly applicable to arena optimization. The 0.901564 bound is a key benchmark.

## Limitations

- Step functions only — does not explore smooth parameterizations
- Computational cost scales with number of intervals
- Does not provide theoretical analysis of why this ratio is achievable
