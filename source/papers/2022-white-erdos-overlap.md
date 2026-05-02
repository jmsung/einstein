---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2201.05704
cites:
  - problem-1-erdos-overlap/strategy.md
  - problem-1-erdos-overlap/literature.md
---

[[../home]] | [[../index]]

# White — Erdős' Minimum Overlap Problem

**Authors:** Ethan Patrick White
**Year:** 2022
**Venue:** arXiv preprint (math.CO, math.NT, math.OC)

## Summary

White derives a substantially improved lower bound for Erdős' minimum overlap problem using elementary Fourier analysis to translate the problem into a convex optimization program. The key insight is that the overlap function M(x) has all even cosine coefficients nonpositive, enabling an SOCP (second-order cone program) formulation.

The paper is 27 pages with 2 figures and 8 tables, providing detailed numerical results for the convex relaxation approach.

## Key Techniques

- Fourier analysis to reformulate the combinatorial overlap problem
- Convex optimization (SOCP) for systematic bound computation
- Cosine coefficient constraints on the overlap function

## Relevance to Einstein Arena

Directly relevant to **Problem 1 (Erdős Minimum Overlap)**. White's Fourier-constrained construction is one of the foundational approaches for this problem. The SOCP formulation provides a systematic way to compute lower bounds, and the cosine coefficient structure constrains the search space for optimizer-based approaches.

## Limitations

- Lower bound only — does not close the gap with the best upper bounds
- Convex relaxation may not be tight
