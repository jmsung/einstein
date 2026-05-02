---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2602.07292
cites:
  - problem-3-autocorrelation/strategy.md
  - problem-3-autocorrelation/literature.md
  - ../papers/2025-jaech-autoconvolution.md
  - ../papers/2025-boyer-autoconvolution.md
---

[[../home]] | [[../index]]

# Rechnitzer — The First 128 Digits of an Autoconvolution Inequality

**Authors:** Andrew Rechnitzer
**Year:** 2026
**Venue:** arXiv preprint (math.NT, math.CO)

## Summary

Rechnitzer uses rigorous high-precision floating point arithmetic to compute tight bounds on the autoconvolution constant ν₂². This constant represents the infimum of a specific integral optimization problem over unit mass functions. The work substantially improves previous bounds established by White, Green, and Martin & O'Bryant, providing the first 128 verified digits of the constant.

## Key Techniques

- Rigorous high-precision floating point computation (verified arithmetic)
- Numerical optimization with certified error bounds
- Interval arithmetic for rigorous bound verification

## Relevance to Einstein Arena

Directly relevant to **Problem 3 (Second Autocorrelation Inequality)**. Establishes a near-definitive numerical target for the autoconvolution constant. The 128-digit precision result serves as the ultimate benchmark — any arena solution approaching this value is essentially optimal. The rigorous verification methodology is also relevant to our float64 polish pipeline.

## Limitations

- Computational approach — does not provide a closed-form expression
- Extremely high precision may not translate to practical arena advantage (arena uses float64)
