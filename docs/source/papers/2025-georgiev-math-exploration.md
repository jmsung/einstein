---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2511.02864
source_drive: https://drive.google.com/file/d/1pseX1hGB_CKMpwVavZFQxXzhT0nwcnAC
source_local: sources/2025-georgiev-math-exploration.pdf
cites:
  - problem-evaluation.md
  - strategy.md
  - ../papers/2026-angdinata-ramanujan-tau-primes.md
---

# Georgiev, Gómez-Serrano, Tao & Wagner — Mathematical Exploration and Discovery at Scale

**Authors:** Bogdan Georgiev, Javier Gómez-Serrano, Terence Tao, Adam Zsolt Wagner
**Source:** https://arxiv.org/abs/2511.02864
**Year:** 2025

## Summary

This companion paper to AlphaEvolve presents a systematic evaluation of LLM-guided evolutionary search on 67 mathematical problems spanning combinatorics, geometry, number theory, classical analysis, and metric geometry. The system merges LLM generation capabilities with automated testing in an evolutionary framework, iteratively proposing, testing, and refining candidate solutions.

On most of the 67 benchmark problems, AlphaEvolve recovered the best-known solutions autonomously. On several problems it achieved improvements over previously known results. The paper demonstrates that LLM-guided evolutionary search can serve as a complementary tool to human mathematical intuition, discovering constructions that would be difficult to find manually, with reduced computational requirements compared to brute-force search.

A key contribution is the integration with proof-assistant tools (Deep Think, AlphaProof), enabling the system to not only find candidate solutions but also generate formal verification. The paper also shows the system can generalize finite constructions to universal formulas — moving from specific numerical solutions to closed-form expressions.

## Key Techniques

- **Evolutionary search with LLM mutations**: Population-based optimization where LLMs propose code modifications guided by fitness evaluators
- **Finite-to-universal generalization**: Automatically lifting solutions found for specific parameters to closed-form formulas covering all cases
- **Proof-assistant integration**: Coupling with Deep Think and AlphaProof for formal verification of discovered results
- **Multi-domain benchmark**: Systematic evaluation across 67 problems to characterize strengths and failure modes
- **Reduced compute requirements**: Achieving competitive results with less computational budget than pure search methods

## Relevance to Einstein Arena

### Cross-cutting impact

This paper provides the most detailed public description of AlphaEvolve's mathematical problem-solving capabilities. The 67-problem benchmark likely overlaps significantly with Einstein Arena problems, making this essential reading for competitive strategy. Understanding which problem types AlphaEvolve excels at (construction/optimization) vs. struggles with (deep analytical bounds) informs where our agent has competitive advantage.

### Combinatorics and autocorrelation (P1-P4)

The benchmark includes problems in combinatorics and analysis that relate to the autocorrelation and overlap problems on the arena. The evolutionary search approach is particularly effective for finding extremal constructions.

### Geometry problems (P6, P10-P11, P14-P18)

Sphere packing, kissing numbers, point configurations, and related geometric optimization problems are well-represented in the benchmark. These are the problem types where AlphaEvolve's construction-finding capabilities are strongest.

### Generalization capability

The finite-to-universal generalization technique is notable — if the system can automatically lift specific numerical solutions to closed-form formulas, this threatens our analytical advantage on problems where we currently compete via mathematical insight.

### P9 Uncertainty Principle — C_{6,11} bounds (Page 24)

The paper establishes known bounds for the sign uncertainty constant C_{6,11}:
- **Lower bound**: C_{6,11} ≥ 0.2025 (no valid solution can score below this)
- **Upper bounds**: C_{6,11} ≤ 0.353 → 0.32831 → 0.3102 (progressively tighter)
- This directly constrains P9 on the arena — any score below 0.2025 is invalid
- vinid cited this specific page when identifying the arena verifier bug (issue #51)

## Limitations

- The 67-problem benchmark may be cherry-picked to favor domains where evolutionary search works well
- Formal verification is only demonstrated for a subset of results
- The paper describes capabilities but not failure modes in detail — survivorship bias likely present
- Computational costs not fully disclosed — "reduced requirements" is relative to what baseline?

## See Also

- [[cross-problem-lessons]]
- [[problem-evaluation]]
- [[strategy]]
- [[reference/2026-angdinata-ramanujan-tau-primes]]
