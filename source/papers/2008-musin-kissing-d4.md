---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/math/0309430
source_local: sources/2008-musin-kissing-d4.pdf
cites:
  - ../papers/1971-leech-sphere-packing.md
  - ../papers/2012-boyvalenkov-kissing-survey.md
  - ../papers/2024-delaat-kissing-sdp.md
  - ../blog/cohn-kissing-numbers.md
  - ../papers/2012-musin-tarasov-13spheres.md
  - problem-6-kissing-number/literature.md
  - problem-22-kissing-d12/literature.md
---

[[../home]] | [[../index]]

# Musin — The Kissing Number in Four Dimensions

**Authors:** Oleg R. Musin
**Year:** 2008 (Annals of Mathematics 168(1):1–32)

## Summary

Proves κ(4) = 24, settling a conjecture open since the 19th century. The proof is a **modification of Delsarte's linear programming method**: Musin constructs an auxiliary polynomial f on [-1, 1/2] satisfying the Delsarte feasibility conditions f(t) ≤ 0 and f̂_k ≥ 0, but with a *strengthened* normalization that makes the LP value exactly 24 in d=4 (the standard Delsarte bound gives 25.5582…, off by one).

The strengthening exploits an observation that the Delsarte LP is not tight for d=4 because the underlying spherical-code symmetry permits an additional inequality (the "Musin polynomial constraint"). The proof reduces to certifying the auxiliary polynomial via interval arithmetic.

This is one of only **six dimensions** where κ(n) is known exactly (1, 2, 3, 4, 8, 24). All others — including d=11, 12 (the arena's kissing problems) — remain open.

## Key Techniques

- **Modified Delsarte LP** — auxiliary polynomial with stronger constraints than standard Delsarte
- **Interval arithmetic verification** — certifying the polynomial coefficients to rule out floating-point error
- **Spherical-cap argument** — the geometric content beyond Delsarte's algebraic LP
- **Symmetry exploitation** — d=4 has the F_4 root system (24 vectors) which the LP must "see" as the optimum

## Relevance to Einstein Arena

### Problem 6 (kissing) and Problem 22 (kissing d=12)
This is the **methodological template** for any future "κ(d) is exactly K" proof in unsolved dimensions. If κ(11) is ever shown to equal some specific number (e.g., 593), the proof will likely follow a Musin-style strengthened-LP route. The Delsarte LP in d=12 already gives an upper bound of 1355 (de Laat-Leijenhorst 2024 SDP); a Musin-style strengthening might close it toward 840.

### The "modified Delsarte" toolkit
Musin's strengthening is one of several techniques (Cohn-Elkies LP, Bachoc-Vallentin SDP, Leijenhorst-de Laat clustered SDP) that improve over basic Delsarte. Reading them as a family explains why d=8 and d=24 are *easier* than other dimensions (the modular-form bonus closes them) while d=11, 12 remain stubborn.

### Verifier-first lesson
The Annals proof was contested for years over numerical certification. The eventual acceptance turned on **Arb / interval-arithmetic verification**. This mirrors arena-side discipline on P9 / P12 floats: claims of optimality require certified arithmetic, not floating-point experiments.

## Limitations

- Method is highly dimension-specific — d=4 admits an LP gap that d=11, 12 do not
- Auxiliary polynomial design is mostly hand-crafted; no general algorithm
- Doesn't extend obviously to d > 4 (Musin & coauthors have not closed d=5–7 in 15+ years of subsequent work)
- Interval-arithmetic certificates are huge and reproducibility-sensitive

## See Also

- [[1971-leech-sphere-packing]] — Leech-Sloane sphere packings
- [[2012-boyvalenkov-kissing-survey]] — survey of kissing numbers
- [[2024-delaat-kissing-sdp]] — modern SDP upper bounds
- [[2012-musin-tarasov-13spheres]] — companion paper on κ(3)=12, strong 13-spheres problem
- [[resource-cohn-kissing-numbers]] — Cohn's MIT table
