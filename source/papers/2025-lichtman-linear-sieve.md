---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2109.02851
source_local: sources/2025-lichtman-linear-sieve.pdf
cites:
  - problem-7-prime-number-theorem/strategy.md
  - problem-7-prime-number-theorem/literature.md
  - findings/prime-number-theorem-lp.md
---

[[../home]] | [[../index]]

# Lichtman — A Modification of the Linear Sieve, and the Count of Twin Primes

**Author:** Jared Duker Lichtman
**Year:** 2025 (published in Algebra & Number Theory Vol. 19; arXiv v1 2021, v2 2024)
**arXiv:** 2109.02851
**Categories:** math.NT (11N35, 11N36, 11N05)

## Summary

Lichtman introduces a modification of the linear sieve whose weights satisfy strong factorization properties, enabling equidistribution of primes up to size x in arithmetic progressions to moduli up to x^(10/17). This surpasses the level of distribution x^(4/7) from Bombieri-Friedlander-Iwaniec (1986) and x^(7/12) from Maynard's recent extension.

As an application, the paper gives a new upper bound on the count of twin primes, achieving a 2.94% refinement from Wu's 2004 record — the largest percentage improvement since Bombieri-Friedlander-Iwaniec (1986). The method also simplifies Wu's 2004 argument.

## Key Techniques

- **Modified linear sieve weights**: Weights with strong factorization properties that avoid previous barriers to equidistribution
- **Level of distribution improvement**: x^(10/17) > x^(7/12) > x^(4/7) — each step enables tighter sieve bounds
- **Well-factorable weights**: The construction produces weights compatible with Buchstab identity and switching principles
- **Twin prime counting application**: The improved sieve directly yields better upper bounds on pi_2(x)

## Relevance to Einstein Project

### Problem 7 (Prime Number Theorem) — Indirect

The arena's P7 is a finite-N LP over sieve-like weights, not an asymptotic sieve theory problem. However, this paper is relevant because:

1. **Optimal sieve weight design** is the shared underlying problem — P7's LP is the finite, numerical version of what this paper studies asymptotically
2. **The score's limiting value**: as N -> infinity in the arena LP, the optimal score likely converges to 1.0 (the PNT). This paper's techniques operate in the asymptotic regime
3. **Factorization structure**: the "strong factorization properties" of Lichtman's weights could inspire structured LP solutions (rather than black-box LP solvers) for P7

### General Methodology

Demonstrates that sieve weight optimization remains an active research frontier with practical improvements still achievable — the same spirit as the arena's numerical approach.

## Limitations

- Asymptotic results — does not give explicit numerical bounds useful for finite-N LP
- The arena's problem formulation (maximize -sum f(k)log(k)/k with floor constraints) is not directly addressed
- No computational implementation or code provided

*Last updated: 2026-04-21*
