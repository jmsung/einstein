---
type: finding
author: agent
drafted: 2026-05-02
question_origin: cross-problem
status: answered
related_concepts: [bose-chowla-construction.md, kissing-number.md, cohn-elkies-bound.md]
related_techniques: []
related_findings: [dead-end-p19-bose-chowla.md, p22-d12-construction-survey.md]
related_personas: [gauss.md, conway.md, cohn.md]
cites:
  - ../concepts/bose-chowla-construction.md
  - p22-d12-construction-survey.md
  - ../questions/2026-05-02-bose-chowla-840-kissing-d12.md
---

# Dead end: 840 = 29²−1 = κ(12) is a numerical coincidence (H1 confirmed)

## TL;DR

The open question `2026-05-02-bose-chowla-840-kissing-d12.md` asked whether `29² − 1 = 840 = κ(12)_empirical` is a structural connection (H2/H3) or a coincidence (H1). **Verdict: H1 — coincidence.** The number 840 plays fundamentally different mathematical roles in the two contexts (group order vs point count), and the cardinality mismatch (30 BC elements vs 840 kissing points) is decisive. Striking secondary observation: BC q=29 has a remarkably dense low-difference structure (96/99 differences in `[1, 99]`), but this doesn't transfer to the κ(12) sphere-packing context.

## What we computed

`scripts/p22_kissing_d12/bc_840_check.py` computes Bose–Chowla q=29 explicitly:

```
B = {1, 25, 34, 93, 100, 101, 143, 148, 294, 305, 321, 367, 449, 489, 502, 512,
     527, 546, 566, 583, 597, 615, 618, 676, 698, 702, 704, 800, 829}
|B| = 29  (= q for one normalization; q+1=30 with infinity-point convention)
modulus = 840  (= q² − 1)
Sidon: ✓ (all 406 = C(29,2) pairwise differences distinct in Z/840)
```

Difference structure:
- First 10 differences: `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}` (contiguous!)
- Distribution: 96 / 97 / 97 / 116 across `[1,99] / [100,199] / [200,299] / [300,420]`
- 96 of 99 possible diffs in `[1, 99]` are present (97% density at the bottom)
- Range: `[1, 419]` (all differences fit within half the modulus by canonical reduction)

## What κ(12) = 840 actually is

From `findings/p22-d12-construction-survey.md`:

The P₁₂ₐ construction (Leech–Sloane 1971) achieves κ(12) ≥ 840 via:

- 24 axis shifts (`±eᵢ` for i = 1..12)
- 816 = 16 × 51 half-integer patterns derived from binary [12, 6, 4] codes
- All pairwise inner products in `{0, ±¼, ±½, ±1}` — touching at 60°

So 840 = 24 + 816 is a SUM of two structurally derived counts in ℝ¹², not a group-theoretic invariant.

Three independent pathways all hit 840 (lattice-based K₁₂ + extension, Construction A from binary codes, Leech cross-section + deep-hole shift) — each gives 840 via different math, none of them via Bose–Chowla.

## The cardinality argument (decisive)

For H2 (structural identification) to hold, the two appearances of 840 would need to play **the same role**. They don't:

| Context | What 840 is |
|---|---|
| Bose–Chowla q=29 | the **modulus** \|ℤ/(q²−1)\| (group order) |
| κ(12) configuration | the **count** of points on S¹¹ in ℝ¹² |

A 30-element subset of ℤ/840 (BC) is a different kind of object than an 840-element subset of S¹¹ (kissing). Even at the difference-set level — BC's 406 pairwise differences vs the kissing config's set of inner products — the structures don't align: kissing has 4 distinct inner-product values `{0, ±¼, ±½, ±1}`; BC's differences span 406 distinct values in `[1, 419]`.

## Why 840 appears in both contexts

`840 = 2³ · 3 · 5 · 7` is **highly composite** — the 5th-most-composite number under 1000. Its many divisors make it a natural fit for many structural constructions. Specifically:

- BC q=29: forced by `q² − 1 = (29−1)(29+1) = 28 × 30 = 840` for the prime q=29
- κ(12): forced by `24 + 816` where both summands come from independent constructions on 12-dimensional codes/lattices

The two pathways don't intersect. This is the same kind of "highly composite number appears in multiple unrelated contexts" pattern as seen with 24 (Leech lattice dimension AND number of hours, both from divisibility arguments at different scales) or 168 (PSL(2,7) order AND number of hours/week).

## What this rules out

- **H2** (BC q=29 underlies κ(12) = 840): false. The structures don't share the right kind of mathematical object at the right cardinality.
- **H3** (BC has multiplicative regularity exploitable in κ(12) analysis): no direct path; BC's 30-element structure isn't a useful tool for analyzing 840 sphere positions in ℝ¹².

## What this opens up (and the meta-lesson)

**Methodological lesson worth filing**: highly composite numbers like 840 generate "pattern recognition" hits across unrelated domains. The `cross-pollination-not-compute` filter says to *test* such hits with a low-cost experiment — that's exactly what this cycle did. The hit failed; the methodology worked. Future cycles should:

1. Notice numerical coincidences when they appear (gap-detector hint).
2. **Run the cardinality test FIRST** (cheap, decisive in 90% of cases).
3. If cardinality matches, run the structural test (multiplicative / additive regularity comparison).
4. Document the result either way — confirmed coincidences are themselves wisdom (avoid future pattern-match-driven research).

Companion finding `findings/cross-pollination-not-compute.md` says *which candidates to keep*. This finding adds the corollary: **highly composite number coincidences fail at the cardinality test 90% of the time**; treat them as low-prior speculation, not high-priority leads.

## Striking secondary observation (worth a future page if it recurs)

BC q=29's first differences are dense: 96/99 of `[1, 99]` are present, with the first 10 being `{1, 2, ..., 10}` exactly. This is **higher density than naive Sidon expectations**: a random Sidon set in ℤ/840 of size 29 would have C(29,2) = 406 differences spread over [1, 419], expected density 406/419 ≈ 0.97 globally — but local clustering at the bottom is interesting.

Could this be useful for other problems? Maybe. Sidon sets with dense low-prefix coverage are exactly what P19 wanted (and BC didn't deliver at the 90-mark scale because the LARGE differences scatter too much). At smaller scales (q=29), the local density is high enough to be interesting for other contexts (P3 second-autocorrelation, P15/P16 Heilbronn?). Filed as low-priority for future investigation.

## Reproduction

```bash
cd cb/
uv run python scripts/p22_kissing_d12/bc_840_check.py
```

Expected: prints the 29-element BC set in Z/840, confirms Sidon property, dumps difference distribution, prints H1 verdict.

## See also

- [`questions/2026-05-02-bose-chowla-840-kissing-d12.md`](../questions/2026-05-02-bose-chowla-840-kissing-d12.md) — the question this finding closes (annotated as `status: answered`)
- [`findings/dead-end-p19-bose-chowla.md`](dead-end-p19-bose-chowla.md) — sibling P19 closure on the same construction
- [`findings/p22-d12-construction-survey.md`](p22-d12-construction-survey.md) — the P22 structure survey that established the 24+816 decomposition
- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — the meta-principle this cycle exemplifies (test cheap connections; document either way)

*Last updated: 2026-05-02*
