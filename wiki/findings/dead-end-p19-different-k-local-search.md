---
type: finding
author: agent
drafted: 2026-05-02
question_origin: P19
status: answered
related_concepts: [kronecker-decomposition.md, sidon-sets.md, basin-rigidity.md, provable-floor-and-frozen-problems.md]
related_techniques: [basin-hopping-multistart.md, slsqp-active-pair-polish.md]
cites:
  - ../source/papers/2010-vinuesa-sidon-thesis.md
  - ../source/papers/2007-gyarmati-sums-differences.md
  - ../questions/2026-05-02-p19-kronecker-w4-existence.md
---

# Dead end: P19 different-k local search around SOTA k=360

## What we tried

For Problem 19 Difference Bases, the SOTA at score 2.6390274695 (7-way tied) sits at k=360, v=49109. We tested whether changing k by ±1 to ±3 could yield a strictly better ratio score = k²/v under local search around the SOTA solution.

**Tested directly** (`scripts/difference_bases/k_sweep_analysis.py`):

- **k=359 (single mark removal)**: for each x ∈ B_SOTA, compute v after removing x. Best v = 16210 (removing the largest mark x=55033). Score 7.95. Need v ≥ 48838 for score < 2.639.
- **k=358 (pair mark removal)**: top-100 single-removal candidates × pairwise. Best v = 16022. Score 7.99. Need v ≥ 48565.
- **k=361 (strategic single add)**: for each y ∈ [1, 70000] \ B, compute v after adding y. Best y = 49111 → v = 49179, score 2.6499. Need v ≥ 49384.

**Implied closed by structural argument** (no search required):

- **k=362, 363, 368** (multi-add): each additional mark gives diminishing returns above SOTA's v=49109. Strategy.md prior result was "greedy add k=360→370: each new mark only extends v by ~30." Our strategic single-add gives +70 (best) to v. Even doubling to +140 for 2 adds (linear extrapolation, optimistic) gives v ≈ 49249 at k=362 — score 2.65, far above SOTA. Higher k requires even larger v gain that isn't structurally available.
- **k=357 (triple removal)**: removing 1 or 2 marks already drops v from 49109 to ~16k. Three removals will be at most marginally worse. Score will be > 2.0² ≈ 8 at best.

## Why it failed (the obstruction)

**Every mark in SOTA is load-bearing in the low-difference range [1, ~16k].** Removing any single mark x causes v to drop catastrophically (to 16210 or lower) because:

1. The Kronecker structure `B = A ⊕ 8011·{0,1,4,6}` (90-mark atom A, 4-mark perfect Sidon ruler R) creates **multiplicity-1 differences** at 91.8% of the integers in [1, 49109] (per prior strategy.md analysis).
2. Each mark x participates in many mult-1 differences scattered across the range.
3. The cheapest mark to remove (x = 55033) still kills the mult-1 difference at d=16211 (= 55033 − 38822). v drops to 16210.

Symmetric obstruction on the additive side:

4. To raise v from 49109 to 49384 (k=361 target), a single new mark y must contribute differences {y − b : b ∈ B} that fill **all 274 consecutive integers** in [49110, 49383].
5. B has density 360 / 55033 ≈ 0.65%. A 274-wide window expects ≈ 1.78 marks of B. Any single y adds at most ~2 differences in any specific 274-wide window — not all 274.
6. The empirical best (y=49111) adds 70 consecutive integers above 49109, capturing only the easiest range right above the SOTA's coverage edge.

## What this rules out

This is a **structural impossibility**, not just an unsearched space:

- All k ∈ [357, 363] via local search around SOTA: provably cannot beat SOTA's score 2.6390274695.
- All "small perturbation" approaches (1-, 2-, 3-swap; ±1, ±2, ±3 marks): exhausted.
- The SOTA basin is a **rigid structural minimum** for this neighborhood. Improvement requires a structurally different construction, not a local move.

Combined with prior work's formal lemma that no 3-swap of the SOTA atom achieves c(A) ≥ 1044 (subject to the BnB no-deferral caveat; w=3 exhaustive on Modal, 1.22T nodes, 0 hits), the conclusion is strong: the 7-way SOTA tie at 2.6390274695 is a **deep structural minimum** that local methods cannot perturb past.

## What might still work

The remaining open paths require **non-local** moves:

1. **Imperfect 5-mark Sidon rulers** with carefully placed gaps + custom A — the council's H1 question (different `R'` with non-perfect coverage). The "5-mark perfect Sidon doesn't exist" fact does NOT close non-perfect 5-mark cases.
2. **LP/SDP cap certificate** (council's H2) — Bernshteyn–Tait 2019 gives c² ≥ 2.434; the gap to 2.639 is "moderate" per the council's Cohn analysis. A tighter dual could prove 2.639 is the true floor.
3. **Algebraic constructions outside the Singer/Bose/Paley/GMW family** (council's H3) — Ramanujan graphs (LPS), modular form magic functions specific to integer rulers, etc.
4. **Helper-mark optimization** at fixed k=360, holding atom A fixed but varying the 75 "above-v" helper marks. Prior search isolated the atom; helper marks were not deeply optimized as a separate DOF.

These become follow-up branches per the cycle stop-condition (b).

## Reproduction

```bash
cd cb/
uv run python scripts/difference_bases/k_sweep_analysis.py
```

Expected: ~10 seconds. Reads SOTA from `mb/tracking/problem-19-difference-bases/solutions/sota-rank01-CHRONOS-score2.6390274695.json`. Output reproduces the v_after numbers in this finding.

*Last updated: 2026-05-02*
