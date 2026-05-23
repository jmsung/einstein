---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2603.29970
source_drive: https://drive.google.com/file/d/1XerPRQRZqpJBFckKNdvi9ohSJ45cXxxy
source_local: sources/2026-angdinata-ramanujan-tau-primes.pdf
cites:
  - ../papers/2025-novikov-alphaevolve.md
  - ../papers/2025-georgiev-math-exploration.md
  - problem-7-prime-number-theorem/literature.md
---

# Angdinata et al. — ABC Implies That Ramanujan's Tau Function Misses Almost All Primes

**Authors:** David Kurniadi Angdinata, Evan Chen, Chris Cummins, Ben Eltschig, Dejan Grubisic, Leopold Haller, Letong Hong, Andranik Kurghinyan, Kenny Lau, Hugh Leather, Seewoo Lee, Simon Mahns, Aram H. Markosyan, Rithikesh Muddana, Ken Ono, Manooshree Patel, Gaurang Pendharkar, Vedant Rathi, Alex Schneidman, Volker Seeker, Shubho Sengupta, Ishan Sinha, Jimmy Xin, Jujian Zhang
**Source:** https://arxiv.org/abs/2603.29970
**Year:** 2026

## Summary

This paper proves that, assuming the abc Conjecture, the number of primes expressible as absolute values of Ramanujan's tau function grows at most as O(X^{13/22}). This establishes that such primes comprise a density-zero subset of all primes — meaning the tau function "misses almost all primes." The result strengthens prior work by Xiong, who established an upper bound of 2/11 density.

The work addresses two classical conjectures: Lehmer's conjecture (tau never vanishes) and a folklore conjecture (infinitely many primes arise as tau values). Despite the upper bound, the authors conjecture S(X) should be infinite with predicted magnitude S(X) ~ C * X^{1/11} / (log X)^2, suggesting finite but nonzero density among primes.

A notable aspect is that the main mathematical engine was formalized and produced automatically in Lean/Mathlib by AxiomProver from a natural-language statement, demonstrating the growing capability of AI-assisted formal theorem proving.

## Key Techniques

- **abc Conjecture application**: Using the abc Conjecture as the primary tool to bound the density of prime values of multiplicative arithmetic functions
- **Galois representation analysis**: Leveraging properties of the l-adic Galois representations attached to Ramanujan's Delta modular form
- **Automated formalization**: Proof formalized in Lean/Mathlib via AxiomProver, an AI system that translates natural-language mathematical statements into machine-checkable proofs
- **Heuristic density prediction**: Probabilistic model predicting S(X) ~ C * X^{1/11} / (log X)^2 based on the Sato-Tate distribution

## Relevance to Einstein Arena

**Number theory connection (P7):** While the arena's Prime Number Theorem problem reduces to LP optimization of Selberg sieve weights rather than analytic number theory, this paper provides background on the deeper structure of prime distribution and multiplicative functions that motivates the problem family.

**AI-assisted formalization:** The use of AxiomProver to automatically formalize proofs in Lean/Mathlib parallels the proof-assistant integration in AlphaEvolve and the Georgiev-Tao benchmark. This trend toward automated formal verification is relevant to validating mathematical constructions discovered by optimization — a potential future direction for arena solutions that claim theoretical bounds.

## Limitations

- Results depend critically on the unproven abc Conjecture — without it, the density bound does not hold
- The heuristic prediction S(X) ~ C * X^{1/11} / (log X)^2 remains unproven
- AxiomProver formalization covers the main theorem but not all auxiliary lemmas
- The paper does not address computational aspects (no algorithms for finding tau-prime values)

## See Also

- [[reference/2025-novikov-alphaevolve]]
- [[reference/2025-georgiev-math-exploration]]
- [[problem-7-prime-number-theorem/literature]]
