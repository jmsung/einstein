---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: gap-detector
related_problems: [P22, P19]
related_concepts: [bose-chowla-construction.md, kissing-number.md, modular-forms-magic-function.md]
gap_type: cross-problem-coincidence
similarity: structural
---

# Open: is the κ(12) = 840 cap structurally related to Bose–Chowla in ℤ/840?

## Question

`q = 29` (prime) gives the Bose–Chowla modulus `q² − 1 = 840`, which exactly matches P22's empirical kissing-number cap κ(12) = 840 (Levenshtein 1979 + Coxeter–Todd K₁₂ lattice + de Laat–Leijenhorst 2024 SDP cluster bound).

Is this:

- **(a) Coincidence** — 840 = 2³·3·5·7 has many natural decompositions; mathematicians find spurious relationships in such "highly composite" numbers all the time
- **(b) Structural** — the Coxeter–Todd K₁₂ lattice's 756 minimum vectors plus the kissing-tight extension to 840 reflect an underlying multiplicative structure that Bose–Chowla in `ℤ/(q²−1)` makes explicit
- **(c) Cross-pollination opportunity** — apply Bose–Chowla difference-set machinery to construct or verify the d=12 kissing configuration, possibly producing a new proof of κ(12) = 840 OR a new direction for κ(12) ≥ 841

## Why it matters

If (b) or (c), this is a genuine FLT-style cross-domain bridge: P22 (sphere-packing extremal) connecting to P19's algebraic-construction toolkit (additive combinatorics). Both currently sit in different parts of the wiki with no explicit connection. The gap detector flagged Bose–Chowla as a Type-1 missing concept; while authoring it, this coincidence surfaced.

If (a), the resolution is itself a finding (a "looks structural but isn't" lesson, with citation discipline applied).

Either way: the question is testable. The result is a wiki entry.

## What's been tried

Nothing yet. This is a fresh question surfaced 2026-05-02 by:

- The Bose–Chowla concept-page authoring (`concepts/bose-chowla-construction.md`)
- Coincidence noticed: `29² − 1 = 840 = κ(12)_empirical`
- Closed-form check on the K₁₂ lattice's structure not yet done

## Hypotheses

- **H1 (coincidence)**: `840` arises in K₁₂ from `12·70 = 840` (12 = dimension, 70 = number of certain orbit structures); independent of Bose–Chowla. The coincidence is numerical, not structural.
- **H2 (mod-29 structure)**: K₁₂'s minimum vectors map to a difference set in `ℤ/840` that is exactly Bose–Chowla on `q=29`. This would be a startling new connection.
- **H3 (related but not identical)**: K₁₂'s structure has *some* multiplicative regularity that Bose–Chowla machinery can analyze (e.g., bound the maximum number of mutually-non-overlapping kissing positions via difference-set covering arguments).

## Next step

1. Read source/papers/2024-cohn-li-kissing.md (Cohn–Li 2024) for explicit K₁₂ structure description.
2. Read source/papers/2024-delaat-kissing-sdp.md for SDP cluster decomposition of d=12.
3. Compute the Bose–Chowla Sidon set in `ℤ/840` (q=29) explicitly using the existing reproducer (`scripts/difference_bases/bose_chowla.py`).
4. Compare the difference set to the contact-graph differences of the K₁₂ kissing configuration.
5. If the differences match modulo automorphism: **H2 confirmed** — write a finding bridging P22 and P19.
6. If differences are unrelated: **H1 confirmed** — write a finding ruling out the coincidence.
7. Either way: cycle ends, finding filed.

## References

- [`concepts/bose-chowla-construction.md`](../concepts/bose-chowla-construction.md) — the construction
- [`concepts/kissing-number.md`](../concepts/kissing-number.md), [`concepts/cohn-elkies-bound.md`](../concepts/cohn-elkies-bound.md) — P22 / d=12 kissing context
- [`source/papers/2024-cohn-li-kissing.md`](../../source/papers/2024-cohn-li-kissing.md), [`source/papers/2024-delaat-kissing-sdp.md`](../../source/papers/2024-delaat-kissing-sdp.md) — current d=12 references
- [`personas/gauss.md`](../personas/gauss.md), [`personas/conway.md`](../personas/conway.md) — both reach for this kind of structural connection

*Status: open as of 2026-05-02. To be picked up by next P22 or P19 cycle, or as a standalone investigation.*
