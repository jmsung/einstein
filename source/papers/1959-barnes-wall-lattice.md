---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://doi.org/10.1017/S1446788700025064
cites:
  - problem-6-kissing-number/strategy.md
  - problem-6-kissing-number/literature.md
  - ../papers/1971-leech-sphere-packing.md
---

[[../home]] | [[../index]]

# Barnes & Wall — Some Extreme Forms Defined in Terms of Abelian Groups

**Authors:** E. S. Barnes, G. E. Wall
**Year:** 1959
**Venue:** Journal of the Australian Mathematical Society, Vol. 1, pp. 47–63

## Summary

Barnes and Wall introduce a family of lattices in 2^(m+1) dimensions constructed using Abelian group theory. The Barnes-Wall lattices BW_{2^m} include well-known lattices as special cases: the integer lattice (m=0), D₄ (m=1), E₈ (m=2), and Λ₁₆ (m=3). These lattices are among the densest known in their respective dimensions.

For dimension 16, the Barnes-Wall lattice Λ₁₆ establishes a kissing number lower bound of K(16) = 4320, which has stood as the best known construction for over 60 years.

## Key Techniques

- Abelian group constructions for lattice families
- Extreme form theory (lattices that are local maxima of the packing density function)
- Systematic construction across power-of-2 dimensions

## Relevance to Einstein Arena

Foundational for **Problem 6 (Kissing Number D16)**. The BW₁₆ lattice with K(16) = 4320 is the baseline construction. Understanding the group-theoretic structure is essential for:
- Warm-starting optimizers from lattice configurations
- Recognizing symmetry in discovered solutions
- Exploring whether non-lattice packings can exceed 4320

## Limitations

- 1959 construction — lattice-only approach
- Does not explore non-lattice packings that might achieve higher kissing numbers
- The gap to the upper bound (7320) suggests room for improvement
