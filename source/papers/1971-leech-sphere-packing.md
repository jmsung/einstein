---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://doi.org/10.4153/CJM-1971-081-3
source_local: sources/1971-leech-sphere-packing.pdf
cites:
  - problem-6-kissing-number/strategy.md
  - problem-6-kissing-number/literature.md
  - problem-22-kissing-d12/strategy.md
  - problem-22-kissing-d12/literature.md
  - findings/p22-d12-construction-survey.md
---

[[../home]] | [[../index]]

# Leech & Sloane — Sphere Packings and Error-Correcting Codes

**Authors:** John Leech, Neil J. A. Sloane
**Year:** 1971
**Venue:** Canadian Journal of Mathematics, Vol. 23, pp. 718–745

## Summary

Leech and Sloane use error-correcting codes for systematic constructions of sphere packings in n-dimensional Euclidean spaces. The paper derives many of the best sphere packings known at the time and constructs new packings in dimensions 9–15, 36, 40, 48, 60, and 2^m for m ≥ 6. These constructions increase the previously known kissing numbers in several dimensions.

For dimension 12, the paper establishes a lower bound of K(12) = 840 via the P₁₂ₐ construction based on the Coxeter-Todd lattice K₁₂. This remained the best known lower bound for over 50 years.

## Key Techniques

- Error-correcting code constructions for sphere packings
- Lattice-based kissing number lower bounds
- Systematic enumeration of contact vectors

## Relevance to Einstein Arena

Foundational for **Problem 6 (Kissing Number)**, particularly the D12 variant. The K(12) = 840 bound from this paper is the starting point for arena optimization. Understanding the lattice structure (Coxeter-Todd K₁₂) is essential for warm-starting optimizers and for recognizing when a solution has lattice-like symmetry.

Also foundational for the broader sphere packing literature relevant to D11 and D16 problems.

## Limitations

- 1971 constructions — some bounds have since been improved
- Does not provide computational optimization techniques (purely algebraic)
