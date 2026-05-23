---
type: source
provenance: papers
author: agent
drafted: 2026-05-02
level: 4
source_type: published_paper
source_url: https://arxiv.org/abs/2411.04916
source_local: sources/2024-cohn-li-kissing.pdf
cites:
  - ../papers/1971-leech-sphere-packing.md
  - ../papers/2012-boyvalenkov-kissing-survey.md
  - ../papers/2024-delaat-kissing-sdp.md
  - ../papers/2022-ganzhinov-symmetric-lines.md
  - ../papers/2025-novikov-alphaevolve.md
  - ../blog/cohn-kissing-numbers.md
  - problem-6-kissing-number/literature.md
  - problem-22-kissing-d12/literature.md
---

[[../home]] | [[../index]]

# Cohn & Li — Improved Kissing Numbers in Seventeen through Twenty-One Dimensions

**Authors:** Henry Cohn, Anqi Li
**Year:** 2024 (arXiv:2411.04916)

## Summary

Improves the lower bounds for κ(n) in dimensions 17–21 by margins ranging from +256 to +2048 over the Leech 1967 records:

| n  | Previous (Leech 1967) | New | Δ |
|----|---|---|---|
| 17 | 5346 | **5730** | +384 |
| 18 | 7398 | **7654** | +256 |
| 19 | 10668 | **11692** | +1024 |
| 20 | 17400 | **19448** | +2048 |
| 21 | 27720 | **29768** | +2048 |

**Method**: unlike Leech's constructions which take cross-sections of Λ_24 (the Leech lattice), Cohn-Li **modify the signs in lattice vectors** to open up additional spherical caps. The new configurations are not lattices — they are codes with controlled-sign multipliers — and so are not subject to the same density-saturation arguments that constrain pure lattice constructions.

The technique is structural and quasi-explicit: the authors describe a finite construction recipe, run it, and verify the resulting kissing configuration. The improvements are not LLM/RL-driven; this is a pure-mathematical paper that nevertheless beats long-standing records.

## Key Techniques

- **Sign-modified lattice vectors** — start with Λ_24 cross-sections, flip subset of coordinates' signs to relieve packing constraints
- **Combinatorial design** — sign patterns chosen via covering-code structure
- **Explicit verification** — final configurations are checked exhaustively (small n)
- **Cross-section escape** — the key insight is that *not all kissing configurations are cross-sections*; this is the source of the gain

## Relevance to Einstein Arena

### Problem 22 — Kissing in d=12 (current branch)
**Direct methodological echo.** P_{12a} (Leech-Sloane 1971) is itself a non-lattice configuration of 840 vectors that is also *not* a Λ_24 cross-section — it predates Λ_24 in fact. The Cohn-Li sign-modification trick is structurally similar to the move from K_12 (lattice, kissing 756) to P_{12a} (non-lattice, kissing 840). The 840→1355 gap on P22 is structurally analogous to the 17668→? open question on κ(20) before this paper. The lesson: **lattice cross-sections are not the ceiling**.

### Problem 6 — Kissing in d=11
**Adjacent dimensions to AlphaEvolve's d=11 record (593, beating Ganzhinov's 592).** Cohn-Li does not touch d=11 specifically, but the sign-modification technique is the natural manual analog of what AlphaEvolve might have rediscovered. Reading both side-by-side suggests the structural moves available in this regime.

### Cross-section saturation as a CHRONOS-relevant claim
CHRONOS's P22 attack analysis claims all 12-d sublattices of Λ_24 cap at 756, i.e., **all lattice cross-sections are below P_{12a}**. Cohn-Li 2024 confirms this is a general phenomenon — sign-modification escapes the cross-section ceiling in higher dimensions. If the same trick can be ported to d=12, it might break the 840 barrier (though the structural cap claim suggests it can't).

## Limitations

- Improvements are modest as a fraction of the gap to upper bounds
- Method is dimension-specific — does not give a clean asymptotic formula
- d=12 specifically not addressed; the special status of d=12 (modular forms, E_6, P_{12a}) means d=17–21 techniques may not transfer
- Manual / structural rather than algorithmic — does not parallelize

## See Also

- [[1971-leech-sphere-packing]] — Leech-Sloane source for the cross-section constructions
- [[2012-boyvalenkov-kissing-survey]] — kissing-number survey
- [[2024-delaat-kissing-sdp]] — current upper bounds
- [[2022-ganzhinov-symmetric-lines]] — comparable lower-bound improvements in d=10,11,14
- [[2025-novikov-alphaevolve]] — d=11 record-holder (593)
- [[resource-cohn-kissing-numbers]] — Cohn's MIT table
