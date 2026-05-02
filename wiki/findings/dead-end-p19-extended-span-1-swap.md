---
type: finding
author: agent
drafted: 2026-05-02
question_origin: P19
status: answered
related_concepts: [kronecker-decomposition.md, basin-rigidity.md]
related_techniques: [warm-start-from-leader.md]
related_findings: [p19-kronecker-bridging-threshold.md, dead-end-p19-different-k-local-search.md]
cites: [p19-kronecker-bridging-threshold.md]
---

# Dead end: extended-span 1-swap on SOTA atom (P19)

## TL;DR

The cycle 2 finding [`p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) opened a new design-space direction: extend `max(A)` beyond SOTA's 6967 (the relaxed-bridging regime allows smaller `c(A)`, but to BEAT SOTA we still need `c(A) ≥ 1044`). Cycle 3 tested this directly: 93,870 1-swaps `(x → y)` with `y ∈ [6968, 8010]` (1010 new y values prior 1-swap [0, 7000] never tested). **Result: 0 of 93,870 swaps even *preserve* c(A) at 1043, let alone improve it.** Every swap strictly drops c(A).

## What we tried

Hypothesis from cycle 2: with `max(A)` extended into `(6967, 8010]`, find a 90-mark atom A' with `c(A') ≥ 1044`. Bridging at this threshold range is automatic for any `c(A) ≥ 1044, max(A) ≤ 8010`.

Test: for each `y ∈ [6968, 8010] \ A_sota` and each `x ∈ A_sota`, compute c(A') for `A' = A_sota \ {x} ∪ {y}`.

- 93,870 swaps tested
- 0 swaps preserved c(A) at 1043
- 0 swaps improved c(A) above 1043

Reproducer: `cb/scripts/difference_bases/extended_span_search.py` (~30 seconds on M5 Max).

## Why it failed

The structural argument: every mark `x ∈ A_sota` is load-bearing for **multiple multiplicity-1 differences in [1, 1043]**. Removing x kills those mult-1 diffs simultaneously. For `c(A') ≥ 1043`, the new mark y must ADD new diffs that fill *every* killed gap exactly.

But a single new mark contributes only |A_sota| − 1 = 89 new positive differences `{|y − a'| : a' ∈ A_sota \ {x}}`. Of these, only the subset landing in [1, 1043] can fill the killed gaps. For y ∈ [6968, 8010], the subset of new diffs landing in [1, 1043] is `{y − a' : a' ∈ [y − 1043, y − 1] ∩ A_sota}` — typically a small handful.

Empirically: the killed-diff pattern from removing x is **never** matched exactly by the gap-filling diffs from any single y. The combinatorics of mult-1 placement under the Kronecker structure are too rigid for 1-swap to repair.

## What this rules out

Combined with prior negatives (1-swap [0, 7000]: 0 hits; w=3 BnB exhaustive at span=6967: 0 hits over 1.22T nodes), the extended-span 1-swap result establishes:

**No 1-swap of A_sota with new mark anywhere in `[1, 8010]` yields c(A') ≥ 1044.**

The SOTA atom basin is **globally rigid for 1-swap perturbations across the full bridging-feasible y range**. The "extended span" relaxation (cycle 2's promised lever) doesn't unlock improvement at 1-swap depth — the rigidity isn't about span; it's about the joint structure of A_sota's diff multiset.

## Refines the cycle 2 finding

Cycle 2 surfaced the bridging-threshold structure and predicted (under the formula) that an extended-span atom with `c(A') ≈ 1500` could yield `v ≈ 49566`. Cycle 3 shows: **constructing such an atom via 1-swap from SOTA is not just hard — it's impossible.** The extended span gives "room" but the diff multiset rigidity doesn't relax with span.

The cycle 2 prediction was: "this opens a new optimization target." Cycle 3 says: "yes, but the target is unreachable from SOTA via 1-swap." The atom would have to be constructed *non-locally* — from scratch, not from SOTA — to live in the relaxed-bridging design space.

This is itself a sharpening of the structural result: the rigidity at SOTA isn't about the FORMULA's local constraints; it's about the diff-multiset being globally tight in a way that single-mark perturbations cannot navigate.

## What might still work

1. **2-swap with extended span.** Two new marks have more flexibility in joint gap-filling. Prior 2-swap was random 20M at fixed span=6967 (0 hits). Extended-span 2-swap is untested. Search size: O(90² × 1043²) ≈ 8.8B raw, but smart pruning (only swaps where both new marks contribute to specific gaps) might bring it down to ~1B — tractable in numba on M5 (~hours).
2. **From-scratch construction in the extended-span design space.** Don't start from SOTA atom. Use Wichmann or Bose-Chowla seeded in `[0, 7500]` and locally search. Different basin entirely.
3. **The other cross-pollination threads** from the literature search — Saarela-Vanhatalo partial words, optimal transport, Bernshteyn-Tait inversion. These don't depend on the SOTA atom at all.

## Reproduction

```bash
cd cb/
uv run python scripts/difference_bases/extended_span_search.py
```

Expected: ~30 seconds; "0 hits, 0 safe-to-remove, best c=1043."

## See also

- [`findings/p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) — the cycle-2 structural finding that proposed this test
- [`findings/dead-end-p19-different-k-local-search.md`](dead-end-p19-different-k-local-search.md) — cycle-1 different-k negative (parallel result)
- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — meta-principle for picking the next cycle direction

*Last updated: 2026-05-02*
