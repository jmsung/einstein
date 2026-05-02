---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1609.08000
source_local: sources/2016-haugland-min-overlap.pdf
cites:
  - ../papers/2022-white-erdos-overlap.md
  - ../papers/2025-yuksekgonul-ttt-discover.md
  - ../blog/bloom-erdos-problems.md
  - problem-1-erdos-overlap/literature.md
  - problem-1-erdos-overlap/strategy.md
---

[[../home]] | [[../index]]

# Haugland — The Minimum Overlap Problem Revisited

**Author:** Jan Kristian Haugland
**Year:** 2016
**arXiv:** 1609.08000

## Summary

Two-page short note giving an explicit improved upper bound for Erdős's minimum overlap constant c = lim M(n)/n. Using a 15-step density function f on [0, 2] (down from 21 steps in his earlier work) Haugland improves the bound from **0.382002 → 0.380926**. The function values are given numerically:
```
f = (0, 0.099, 0.643, 0.361, 0.695, 0.592, 0.896, 0.926)
```
on [0, 1] with f(2-x) = f(x) symmetry.

The methodology is the Swinnerton-Dyer continuous relaxation: M(n)/n ≥ inf over step functions f on [0, 2] with values in [0, 1] and ∫f = 1 of max_k ∫f(x)(1 − f(x+k))dx. By improving the step-function ansatz one squeezes the upper bound on c.

This is a key data point in the long sequence of human-discovered upper bounds (Haugland 1996: 0.382, this paper 2016: 0.380926, White 2023: 0.379... via Fourier+SOCP, AlphaEvolve / TTT-Discover 2024-25: further) all converging toward the true c (lower bound √(4-√15) ≈ 0.356 by Moser).

## Key Techniques

- **Swinnerton-Dyer continuous relaxation** — reduce the discrete optimization to a continuous LP over densities
- **Step-function ansatz** — discretize f into N equal subintervals, optimize the height vector
- **Symmetry constraint** — f(2-x) = f(x) halves the search space
- **Hand-tuned numerical optimization** — no machine search; 15 specific values worked out

## Relevance to Einstein Arena

### Problem 1 — Erdős Minimum Overlap

Direct prior art. The arena P1 problem is exactly the Swinnerton-Dyer relaxation: optimize a step function (or equivalent representation) to lower the bound on c. Haugland's 0.380926 sits between the classical 0.382 (Haugland 1996) and the modern White 2023 (0.379...) / AlphaEvolve / TTT-Discover (current SOTA). Useful as a sanity-check reference: any arena submission must beat Haugland's 0.380926 with the matching number of steps to be a real improvement.

### Methodological lesson
The step-function ansatz is a baseline approach — modern methods (Fourier + SOCP per White 2023, RL per TTT-Discover 2025) outperform it but only by careful relaxation of the discretization assumption. This paper is the simplest entry point into the problem.

## Limitations

- 15-step ansatz is not even close to converged — Fourier methods (White) reach much lower bounds
- No structural insight into the extremizer
- Bound has been superseded multiple times since 2016
- Two-page note; sketches the construction without full optimization details

## See Also

- [[2022-white-erdos-overlap]] — White's Fourier + SOCP improvement
- [[2025-yuksekgonul-ttt-discover]] — RL at test time for Erdős overlap
- [[resource-erdos-problems]] — Erdős problems database entry
- [[../problem-1-erdos-overlap/literature]]
- [[../problem-1-erdos-overlap/strategy]]
