---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://doi.org/10.1007/s12532-024-00264-w
cites:
  - problem-6-kissing-number/strategy.md
  - problem-6-kissing-number/literature.md
  - ../papers/1971-leech-sphere-packing.md
---

[[../home]] | [[../index]]

# de Laat & Leijenhorst — Solving Clustered Low-Rank Semidefinite Programs Arising from Polynomial Optimization

**Authors:** David de Laat, Nando (Abe van) Leijenhorst
**Year:** 2024
**Venue:** Mathematical Programming Computation, Vol. 16, No. 3, pp. 503–534

## Summary

de Laat and Leijenhorst develop a primal-dual interior point method specialized for clustered low-rank semidefinite programs that require high-precision numerics. These SDP problems arise from multivariate polynomial optimization through sums-of-squares characterizations. The method is applied to compute three-point bounds for the kissing number problem, yielding improved upper bounds in dimensions 11 through 23.

Key results for Einstein Arena dimensions:
- K(12) upper bound: 1355
- K(16) upper bound: 7320

## Key Techniques

- Primal-dual interior point methods for SDPs
- Clustered low-rank decomposition for scalability
- Sums-of-squares polynomial characterizations
- High-precision numerical computation

## Relevance to Einstein Arena

Directly relevant to **Problem 6 (Kissing Number)** across D11, D12, and D16. The upper bounds establish theoretical ceilings: any arena solution cannot exceed K(12) ≤ 1355 or K(16) ≤ 7320. The gap between lower and upper bounds (e.g., 840 vs 1355 for D12) defines the search space for improvement.

## Limitations

- Upper bounds only — does not provide constructions
- SDP methods are computationally expensive at high dimensions
- Gap between upper and lower bounds remains large in most dimensions
