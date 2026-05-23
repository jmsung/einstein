---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2207.08266
source_local: sources/2022-ganzhinov-symmetric-lines.pdf
cites:
  - problem-6-kissing-number/strategy.md
  - problem-6-kissing-number/literature.md
---

[[../home]] | [[../index]]

# Ganzhinov — Highly Symmetric Lines

**Author:** Mikhail Ganzhinov
**Year:** 2022
**arXiv:** 2207.08266
**Categories:** math.FA, math.CO, math.MG

## Summary

Ganzhinov generalizes the theory of highly symmetric frames by incorporating projective stabilizers of frame vectors, enabling a unified construction of highly symmetric line systems and subspace systems. The key insight is that systems of subspaces that are subspace-transitive and determined by stabilizer subgroups of their subspaces yield configurations with few distinct angles — making them strong candidates for optimal packings.

The paper's main concrete results are three new kissing configurations that improve lower bounds on the kissing number in dimensions 10, 11, and 14:

| Dimension | Previous lower bound | New lower bound | Upper bound |
|-----------|---------------------|-----------------|-------------|
| d=10 | 500 | **510** | 553 |
| d=11 | 582 | **592** | 869 |
| d=14 | 1606 | **1932** | 3177 |

The d=11 result is particularly relevant: the construction uses PSU(4,2) acting on U(C^5) to build complex frames Phi_1 (80 vectors) and Phi_2 (270 vectors), then embeds into R^11 via a projection Pi(v) = (v, 0) with a unit vector e_11, yielding a 592-vector spherical code:

Pi(ic*Phi_2) ∪ Pi(Phi_1) ∪ Pi(e^{2pi*i/3}*Phi_1) ∪ (sqrt(3)/2 * Pi(e^{4pi*i/3}*Phi_1) ± e_11/2) ∪ {±e_11}

containing 270 + 80 + 80 + 160 + 2 = 592 vectors with inner products at most 1/2.

## Key Techniques

- **Projective stabilizer analysis:** Use stabilizer subgroups H_V of frame vectors/lines to classify and construct symmetric systems
- **Twisted spherical functions:** Compute Gram matrices via twisted spherical functions associated with finite groups and their double cosets
- **Complex-to-real embedding:** Embed complex d-dimensional frames into R^(2d) or R^(2d+1) spherical codes to produce kissing configurations
- **Phase multiplication:** Multiply frames by phases (e^{2pi*i/k}) and combine via unions to expand configurations while controlling angle sets
- **Group orbit enumeration:** Enumerate orbits of finite groups (PSU(4,2), U(3,3), W(H_4)) to find highly symmetric systems with small angle sets

## Relevance to Einstein Project

### Problem 6: Kissing Number d=11 (Direct)

This paper provides the **foundational construction** for the arena's d=11 kissing number problem. The arena's current best is n=594 (2 vectors beyond this paper's 592), suggesting competitors have extended Ganzhinov's construction — likely by finding additional compatible vectors or using a refined embedding.

Key implications for optimization:
- The 592-vector code has inner products at most 1/2 — the same threshold the arena likely uses
- The construction is **algebraic** (group-theoretic), not numerical — warm-starting from this structure and numerically relaxing could find the 594-vector configuration
- The complex frames Phi_1 and Phi_2 have explicit angle sets: {±1/3, ±i/sqrt(3)} and {±1/2, ±e^{2pi*i/3}/2, ±e^{4pi*i/3}/3, -1} — these constrain the search space
- The Mathieu group M_12 construction (Section 5.6) provides an independent 78-line system in d=11 that could offer alternative seeds

### Problem 6: Kissing Number d=12 and d=16

Table 2 shows d=12 lower bound 840, d=16 lower bound 4320 — matching the arena problems (n=841 for d=12, n=4321 for d=16). The paper does not improve these bounds but the framework could be applied.

### General Methodology

The twisted spherical function technique is a systematic way to enumerate candidate kissing configurations from finite group representations — potentially applicable to any sphere packing problem in the arena.

## Limitations

- Constructions are algebraic — no numerical optimization or polishing applied
- The gap between 592 and the arena's 594 is not addressed (published 2022, before the arena)
- No explicit coordinates provided for the 592-vector code (only the algebraic recipe)
- Upper bound for d=11 is 869, leaving significant room — the construction may be far from optimal

*Last updated: 2026-04-21*
