---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1002.1439
source_local: sources/2012-musin-tarasov-13spheres.pdf
cites:
  - ../papers/1971-leech-sphere-packing.md
  - ../papers/2012-boyvalenkov-kissing-survey.md
  - ../papers/2008-musin-kissing-d4.md
  - ../blog/cohn-kissing-numbers.md
  - problem-6-kissing-number/literature.md
  - problem-11-tammes/literature.md
  - problem-22-kissing-d12/literature.md
---

[[../home]] | [[../index]]

# Musin & Tarasov — The Strong Thirteen Spheres Problem

**Authors:** Oleg R. Musin, Alexey S. Tarasov
**Year:** 2012 (Discrete & Computational Geometry 48(1):128–141)

## Summary

The **thirteen-spheres problem** (Newton-Gregory 1694, settled by Schütte-van der Waerden 1953) asks whether κ(3) ≥ 13. The answer is no — κ(3) = 12. The **strong thirteen-spheres problem** asks: what is the *largest possible radius* r such that 13 equal spheres of radius r can simultaneously touch a central unit sphere? Equivalently, this is the **Tammes problem for N = 13** — find the maximum minimum angular separation among 13 points on S².

Musin and Tarasov give a **computer-assisted proof** that solves this long-standing open problem. The optimal arrangement and exact maximum radius are determined. The proof proceeds by:

1. Enumerating "irreducible graphs" — combinatorial certificates of all candidate optimal configurations (geometrically rigid contact graphs with 13 vertices on the unit sphere)
2. For each irreducible graph, solving the resulting nonlinear system to determine if it can be realized
3. Pruning configurations infeasible by the angular-deficit constraint
4. Verifying the survivor (a unique configuration) is optimal via interval-arithmetic certified bounds

The optimum is approximately r ≈ 0.5557 (corresponds to a minimum angle ≈ 57.13°). The optimal configuration is *not* a small perturbation of the icosahedral 12-sphere arrangement — it has a 12-fold symmetric "skirt" plus one apex.

## Key Techniques

- **Irreducible-graph enumeration** — combinatorial classification of geometrically rigid contact graphs
- **Computer-assisted case analysis** — finite case-split with exhaustive verification
- **Interval arithmetic** — Arb / mpfi for the numerical phases
- **Tammes problem reformulation** — translates packing into angular-separation maximization

## Relevance to Einstein Arena

### Problem 11 — Tammes Problem
**Direct reference for the methodology.** The arena's P11 (Tammes for n=50) is the same problem one dimension higher in cardinality. While the Musin-Tarasov method does not scale to n=50 (irreducible graph count explodes), the **conceptual framework** — irreducible graph + interval arithmetic — is the cleanest formulation of the Tammes problem and informs upper-bound work.

### Problem 6 (κ(11)) and Problem 22 (κ(12))
**Methodological precedent for tight κ(n) proofs.** This paper is one of the few examples where a kissing-related extremal problem was *closed* by computer-assisted enumeration. If κ(12) = 840 ever gets a tight proof, the structural shape — irreducible-graph enumeration over P_{12a}-class configurations + SDP duality — would resemble this paper's approach scaled up.

### Strong vs. weak 13-spheres
The "weak" version (κ(3) ≤ 12) has many proofs. The "strong" version requires *uniqueness* of the optimum. Arena problems rarely care about uniqueness, but the technique for ruling out near-optimal alternatives is reusable when arguing that a record (e.g., 593 in d=11) cannot be improved without structural change.

### Tammes-13 as benchmark
The Musin-Tarasov result gives an exactly known reference value for n=13 against which any general-purpose Tammes solver can be calibrated. Useful as a sanity check before scaling up to n=50.

## Limitations

- Method does not scale — irreducible graph count is super-exponential in n
- Computer assistance makes the proof contingent on software correctness
- Doesn't directly bound κ(n) for n > 3
- Optimum value is irrational — closed form is implicit in the algebraic system, not given explicitly

## See Also

- [[2008-musin-kissing-d4]] — companion: κ(4) = 24
- [[1971-leech-sphere-packing]] — Leech-Sloane sphere packings, kissing in d=12
- [[2012-boyvalenkov-kissing-survey]] — kissing number survey
- [[../problem-11-tammes/literature]] — arena P11 (Tammes for n=50)
