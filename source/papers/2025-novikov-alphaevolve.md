---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2506.13131
source_drive: https://drive.google.com/file/d/1KKCeE9Jcx7Gl3byF_7AXo8nCy27LEy1V
source_local: sources/2025-novikov-alphaevolve.pdf
cites:
  - problem-evaluation.md
  - problem-6-kissing-number/strategy.md
  - problem-6-kissing-number/literature.md
  - ../papers/2026-angdinata-ramanujan-tau-primes.md
---

# Novikov et al. — AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery

**Authors:** Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, Pushmeet Kohli, Matej Balog
**Source:** https://arxiv.org/abs/2506.13131
**Year:** 2025

## Summary

AlphaEvolve is an evolutionary coding agent developed by Google DeepMind that uses LLM pipelines to iteratively discover and optimize algorithms. The system orchestrates multiple LLMs to generate code mutations, evaluates candidates against automated fitness functions, and maintains a population of solutions that evolves over time. This represents a shift from single-shot LLM problem-solving to sustained, autonomous search guided by evaluator feedback.

The system achieved notable results across mathematics and computer science: it discovered a 4x4 complex matrix multiplication algorithm using 48 scalar multiplications (improving on Strassen's 56-year-old bound), optimized data center scheduling algorithms, and simplified hardware accelerator circuit designs. In pure mathematics, it produced novel algorithms with formal correctness proofs across multiple domains.

Of direct relevance to the Einstein Arena, AlphaEvolve was applied to many of the same extremal combinatorics and discrete geometry problems that appear on the leaderboard, making it both a competitor system and a source of techniques.

## Key Techniques

- **Evolutionary LLM orchestration**: Population-based search where LLMs generate code mutations and evaluators provide fitness signals
- **Multi-evaluator feedback**: Candidates assessed by multiple criteria (correctness, optimality, efficiency) rather than a single score
- **Iterative code improvement**: Solutions refined through successive generations rather than generated in a single pass
- **Formal verification integration**: Mathematical results accompanied by machine-checkable correctness proofs
- **Automated fitness function design**: Evaluators tailored to each problem domain

## Relevance to Einstein Arena

### Cross-cutting impact

AlphaEvolve is the primary competitor system on the Einstein Arena leaderboard. Understanding its architecture and limitations is essential for competitive strategy. The evolutionary approach with LLM-generated mutations is complementary to the analytical and construction-based methods used in our problem-specific strategies.

### Problem 6 — Kissing Number

AlphaEvolve achieved the current best known kissing number in dimension 11 (593 contacts), surpassing previous results. Their approach combines evolutionary search with group-theoretic constructions.

### Optimization problems (P15-P19)

The iterative code improvement pipeline is most naturally suited to optimization problems where fitness functions are straightforward to define. These problems may be where AlphaEvolve has the strongest structural advantage.

### Analytical problems (P1-P5)

For problems requiring deep mathematical insight (bounds, autocorrelation, spectral methods), AlphaEvolve's brute-force evolutionary approach may be less effective than targeted analytical constructions — a potential competitive opportunity.

## Limitations

- Requires well-defined automated evaluators — problems with ambiguous or hard-to-compute fitness signals are harder targets
- Evolutionary search is computationally expensive (large-scale GPU infrastructure)
- Published results may represent cherry-picked successes; failure modes not discussed
- The paper describes the general system, not problem-specific strategies — actual arena submissions may use customized variants

## See Also

- [[cross-problem-lessons]]
- [[problem-evaluation]]
- [[problem-6-kissing-number/strategy]]
- [[problem-6-kissing-number/literature]]
- [[reference/2026-angdinata-ramanujan-tau-primes]]
