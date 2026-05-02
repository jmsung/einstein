---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/1507.03631
source_local: sources/2012-boyvalenkov-kissing-survey.pdf
cites:
  - ../papers/1971-leech-sphere-packing.md
  - ../papers/2024-delaat-kissing-sdp.md
  - ../papers/2022-ganzhinov-symmetric-lines.md
  - ../blog/cohn-kissing-numbers.md
  - problem-6-kissing-number/literature.md
  - problem-22-kissing-d12/literature.md
  - problem-22-kissing-d12/strategy.md
---

[[../home]] | [[../index]]

# Boyvalenkov, Dodunekov & Musin — A Survey on the Kissing Numbers

**Authors:** Peter Boyvalenkov, Stefan Dodunekov, Oleg R. Musin
**Year:** 2012 (Serdica Math. J. 38(4):507–522). arXiv preprint 1507.03631 posted 2015.

## Summary

Authoritative survey of the kissing-number problem κ(n) = maximum number of non-overlapping unit spheres touching a central unit sphere in ℝⁿ. Frames κ(n) as a special case of the spherical-code maximum A(n, 1/2), and traces the four-decade history of upper and lower bounds in dimensions 1 through 24, with a careful exposition of the linear-programming bound machinery (Delsarte-Goethals-Seidel) and its extensions.

Treated dimensions of direct relevance to the arena:
- κ(2) = 6, κ(3) = 12 (Schütte-van der Waerden), κ(4) = 24 (Musin 2008), κ(8) = 240, κ(24) = 196560 (the only known sharp values besides 1–4 and 8/24).
- κ(8) and κ(24) are tight by the Cohn-Elkies LP bound (later promoted to Viazovska's modular-form proofs in 2016).
- All other dimensions including **n=11 and n=12** remain open: the survey reports κ(12) ≥ 840 (Leech-Sloane 1971, P_{12a} construction) with no tightness proof, and best upper bounds via SDP at the time of writing.

The paper is the standard reference for the *current state of knowledge* table that subsequent improvements (Ganzhinov 2022, AlphaEvolve 2025, de Laat-Leijenhorst 2024) build on.

## Key Techniques

- **Delsarte / linear programming bound** — upper bounds via positive-definite kernels f(t) ≤ 0 for t ∈ [-1, 1/2]
- **Levenshtein bound** — explicit closed-form LP bound, asymptotically optimal in some regimes
- **Spherical code construction A** — lift binary codes to vectors via {±1}/√n coordinates
- **Lattice min-shells** — D_n root system (κ_low = 2n(n-1)), E_8 (κ=240), Λ_24 (κ=196560), Λ_12 / K_12
- **Symmetric configurations** — leveraging group orbits to ensure tightness of LP feasibility

## Relevance to Einstein Arena

### Problem 6 (kissing number) and Problem 22 (kissing d=12)

This is the single best entry-point reference for both arena kissing problems. The d=11 record of 593 (now AlphaEvolve) and the d=12 record of 840 (Leech-Sloane) sit in this table. The survey lays out:

- Why κ(11), κ(12) are stuck — no sharp LP/SDP bound, no known design-tight construction.
- Why κ(8)=240, κ(24)=196560 are special (Cohn-Elkies LP saturates exactly via E_8, Λ_24).
- The **structural gap** between best lower bound (840 in d=12) and best upper bound (1416 at the time, now 1355 via de Laat-Leijenhorst) — confirms the 8-way structural cap claim made by CHRONOS in the P22 attack analysis.

### Cross-cutting LP/SDP framework
The Delsarte machinery in §3 of the survey is the same framework used by de Laat-Leijenhorst 2024 (`../papers/2024-delaat-kissing-sdp.md`) and by Cohn-Gonçalves 2019 (`../papers/2019-cohn-uncertainty-d12.md`). Reading the three together gives the full LP/SDP/modular-form picture.

## Limitations

- Pre-Viazovska — does not cover the 2016 modular-form proofs of κ(8), κ(24)
- Pre-AlphaEvolve / Ganzhinov / de Laat improvements (2022-2025)
- Survey-style: no novel constructions, mostly compilation
- Sparse on numerical tables for d > 24

## See Also

- [[1971-leech-sphere-packing]] — P_{12a} construction giving κ(12) ≥ 840
- [[2024-delaat-kissing-sdp]] — modern SDP upper bounds for κ(11)–κ(23)
- [[2022-ganzhinov-symmetric-lines]] — recent improvements in d=10, 11, 14
- [[resource-cohn-kissing-numbers]] — Cohn's reference table
- [[../problem-6-kissing-number/literature]]
- [[../problem-22-kissing-d12/literature]]
