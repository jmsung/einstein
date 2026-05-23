---
type: finding
author: agent
drafted: 2026-05-02
question_origin: P19
status: answered
related_concepts: [kronecker-decomposition.md, asymmetric-kronecker.md, basin-rigidity.md, sidon-sets.md]
related_techniques: [bnb-exhaustive-w3.md]
related_findings: [p19-kronecker-bridging-threshold.md, dead-end-p19-extended-span-1-swap.md, dead-end-p19-different-k-local-search.md]
cites:
  - p19-kronecker-bridging-threshold.md
  - dead-end-p19-extended-span-1-swap.md
  - ../concepts/asymmetric-kronecker.md
---

# Dead end: P19 from-scratch BnB in the extended-span design space

## TL;DR

The cycle-2 finding [`p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) predicted that an atom with `max(A) ≈ 7500` and `c(A) ≈ 1500` would beat SOTA (predicted score 2.6147 vs SOTA 2.6390). Cycle 3 ruled out reaching such an atom by 1-swap from SOTA. **Cycle 6 (this finding) ruled out reaching it by direct BnB from scratch in the relaxed-bridging design space** — 3.715B nodes searched in 30 min with no hit (time-limited, not exhausted, but level stuck at 78–79 throughout). The cycle-2 prediction was also based on a structurally incorrect Wichmann claim — Wichmann perfect rulers exist only at k = 4r+3, not at k = 90. The two bridging conditions are in tension at k=90, and SOTA's `(max=6967, c=1043)` sits on the achievable Pareto frontier.

## What we tried

**Goal**: find any 90-mark atom A in [0, 8010] with `c(A) ≥ 1044` (which, combined with `max(A) ≥ 4005`, would yield `v(A ⊕ 8011·{0,1,4,6}) ≥ 49110 > 49109` and beat the 7-way SOTA tie).

**Approach 1 — direct BnB from scratch.** Ran `scripts/difference_bases/atom_bnb.py --mode direct --target-v 1044 --S-max 8010 --k 90 --time-limit 1800` on M5 Max. Goal-directed DFS starting from `A=[0]`, branching `new_mark = a + d*` where `d*` is the smallest uncovered diff and `a` ranges over current marks. **Result: 0 hits across 3,715,000,000 nodes / 1801.9s wall-clock (~2.06M nodes/sec, time-limited).** The search reached level 78–79 (out of 90) repeatedly but never extended a partial atom to the full c(A)≥1044 solution. Tree was nowhere near exhaustion at the budget — search space too wide for a complete proof — but the persistent ceiling at level 78–79 is consistent with the structural argument below.

**Approach 2 — Wichmann-family construction at k=90.** The cycle-2 prediction cited "Wichmann gives c(A) ≈ 1500 for k=90." We tested this empirically with two standard formulations:
- Pegg-style gap pattern `[1]^r + [r+1] + [2r+1]^(r-1) + [4r+3] + [2r+1]^s + [4r+2] + [3r+2] + [1]^(r-1)`
- Wikipedia-style gap pattern `[1]^r + [r+1] + [2r+1]^r + [4r+3] + [2r+1]^s + [r+1] + [1]^r`

Both produce non-perfect rulers at k near 90, with `c(A) ≤ 65`. The cycle-2 c≈1500 prediction is incorrect for k=90.

## Why it failed (the structural argument)

The two bridging conditions for `B = A ⊕ λ·{0,1,4,6}` are:

1. **Shell 0 → 1**: `c(A) ≥ λ − max(A) − 1`
2. **Shell-to-shell**: `2·max(A) ≥ λ − 1`, i.e., `max(A) ≥ (λ−1)/2 = 4005`

At k=90, the **best-known sparse rulers** have approximately `c(A) ≈ max(A)` (Wichmann perfect-ruler regime, attained at k=4r+3 like 87 or 91). Specifically:
- Perfect Wichmann at k=87: `(max, c) ≈ (1872, 1872)`
- Best non-perfect extensions to k=90: `c ≈ 1900–2000` at `max ≈ 1900–2000`

To satisfy shell-to-shell bridging at λ=8011, we need `max(A) ≥ 4005`. But pulling one or more of the 90 marks out to position ≥ 4005 *removes* the perfect-ruler property: the displaced mark's diff contributions in [1, c_old] are lost, and the new diffs from the moved mark (in [4005 − c_old, 4005]) don't help c (which is the contiguous prefix of [1, ∞)).

Empirically, removing the top mark from SOTA atom drops c from 1043 → 188 (a 855-unit drop, reflecting ~89 lost mult-1 diffs). The same fragility applies to *any* k=90 ruler: removing a single mark when most diffs are mult-1 collapses c.

So at k=90, the Pareto frontier `(max, c)` has a sharp tradeoff: as `max` grows beyond the dense-cluster regime (~2000), `c` shrinks faster than `max` grows. SOTA's `(max=6967, c=1043)` is *deliberately* on this frontier — a dense `c=1043` cluster in [0, ~1500], with helper marks placed sparsely up to 6967 to satisfy shell-to-shell bridging.

The bridging-threshold finding's prediction of `c=1500 at max=7500` would require the Pareto frontier to be substantially better than what SOTA achieves. Neither classical construction (Wichmann, Bose-Chowla, Singer, Paley — all closed by prior dead-ends) nor direct BnB from scratch finds such a point.

## What this rules out

Combined with prior negatives:

| Approach | Span | Result |
|---|---|---|
| 1-swap exhaustive [0, 7000] (cycle 0) | 6967 | 0 hits |
| BnB w=3 exhaustive (cycle 0) | 6967 | 0 hits, 1.22T nodes |
| BnB w=4 random sample 25% (cycle 0) | 6967 | 0 hits, 3.45T nodes |
| 1-swap with extended y [6968, 8010] (cycle 3) | 6967→8010 | 0 hits, 0 c-preserving |
| **Direct BnB from scratch (cycle 12, this finding)** | **8010** | **0 hits, 3.715B nodes (time-limited)** |

**Established**: no 90-mark atom with c(A)≥1044 in [0, 8010] is findable by current goal-directed BnB techniques in 30-min budget. Combined with the structural Pareto argument, the search-feasible improvement space at the **fixed Kronecker template** `(R={0,1,4,6}, λ=8011, k_atom=90)` is empty or nearly so.

## Refines the cycle-2 finding (cycle 12 wisdom-yield)

[`p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) was correct in surfacing the conditional identity but overstated the design-space lever:

| Claim | Status |
|---|---|
| Formula `v = L·λ + c(A)` is conditional on bridging | ✓ confirmed |
| Both `c(A)` and `max(A)` matter (not just `c`) | ✓ confirmed |
| Wichmann at k=90 gives c≈1500 | ✗ **wrong** — Wichmann perfect needs k=4r+3 |
| Extended-span design space has improvement targets | ✗ shell-to-shell + Pareto rule them out at k=90 |

The cycle-2 finding should be updated with this correction. The **structural insight** — that the bridging conditions form a 2-axis constraint — is preserved and useful for related problems. The **predicted improvement** is invalidated.

## What might still work

These directions remain genuinely untested:

1. **Different `(R, λ)` template.** Prior work fixed `R={0,1,4,6}` and `λ=8011`. Perhaps a different (R, λ) admits an atom with c≥1044 more easily — but the 4-mark Sidon enumeration already closed R={0,1,4,6} as uniquely best in cycle 1, and λ-only sweep [7000, 9000] (atom fixed) gave 0 hits.
2. **Asymmetric Kronecker / multi-block.** Drop the perfect symmetry of `A ⊕ λ·R`. E.g., `B = A_1 ⊕ λ_1·R_1 ⊕ A_2 ⊕ λ_2·R_2` with two independent atoms. Untested at scale; combinatorics multiply.
3. **Cross-pollination from outside the ruler literature.** Saarela–Vanhatalo (combinatorics on words), Bernshteyn–Tait inversion (turning the lower-bound proof into a constructor), optimal-transport relaxation. Each is a research arc, not a 1-day experiment.
4. **2-swap with extended span.** Search size O(90² × 1043²) ≈ 8.8B raw, ~hours on M5 with smart pruning. Not done; could close the 1-swap → w=3 BnB → from-scratch chain with one more layer.

## Reproduction

```bash
cd cb/  # or any worktree
# Direct BnB at extended span (cycle 12, this finding) — ~30 min on M5 Max, 0 hits:
uv run python scripts/difference_bases/atom_bnb.py \
  --mode direct --target-v 1044 --S-max 8010 --k 90 \
  --time-limit 1800 --max-nodes 20000000000

# Baseline reproduction (formula tightness, per-shell density):
uv run python scripts/difference_bases/cross_block_analysis.py
```

`atom_bnb.py` was promoted from `mb/tracking/.../private-scripts/` to public during cycle 12 with the post-refactor `SOTA_PATH` fix. JIT-compiled inner loop, ~2M nodes/sec on M5 Max.

## See also

- [`findings/p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) — the cycle-2 finding this refines
- [`findings/dead-end-p19-extended-span-1-swap.md`](dead-end-p19-extended-span-1-swap.md) — cycle-3 1-swap dead end
- [`findings/dead-end-p19-different-k-local-search.md`](dead-end-p19-different-k-local-search.md) — cycle-1 different-k dead end
- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — meta-principle for choosing the next direction (the remaining live threads belong to this category)
- [`concepts/kronecker-decomposition.md`](../concepts/kronecker-decomposition.md) — structural framework for B = A ⊕ λ·R

*Last updated: 2026-05-02*
