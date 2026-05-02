---
type: finding
author: agent
drafted: 2026-05-02
question_origin: P19
status: answered
related_concepts: [kronecker-decomposition.md, sidon-sets.md]
related_techniques: [kronecker-search-decomposition.md]
related_findings: [p19-kronecker-bridging-threshold.md]
cites: [../questions/2026-05-02-p19-kronecker-w4-existence.md]
---

# Dead end: P19 SOTA's R = {0,1,4,6} is uniquely best among 4-mark Sidon rulers

## TL;DR

Enumerated all 114 4-mark Sidon rulers with marks ≤ 12. For each, computed `v(B = A_sota ⊕ λ·R')` with λ=8011 and SOTA's atom. **Only the two perfect Sidon rulers `{0,1,4,6}` and `{0,2,5,6}` (mirror image) achieve v=49109**. Every non-perfect 4-mark ruler collapses v to ≤ 41098 because the gaps in `(R-R)+` correspond to **missing shells** that the SOTA atom's `max(A)=6967 < λ=8011` cannot bridge.

## What we tried

Council question 2026-05-02-p19-kronecker-w4-existence.md asked: does ANY Kronecker decomposition `A ⊕ λ·R'` with a different 4-mark or 5-mark `R'` (Sidon or near-Sidon) yield a strictly better ratio than the current 7-way tie?

This finding closes the **4-mark Sidon** part. Test: enumerate all 4-mark Sidon rulers `R = {0, a, b, c}` with `0 < a < b < c ≤ 12`, compute `v(A_sota ⊕ λ·R)` for each.

Reproducer: `cb/scripts/difference_bases/sidon_R_enumeration.py` (~5 seconds).

## Result table (top 5 by score)

| R | L | (R-R)⁺ gaps | v | k=|B| | score |
|---|---|---|---|---|---|
| (0, 1, 4, 6) | 6 | none — perfect | 49109 | 360 | **2.639027** ← SOTA |
| (0, 2, 3, 7) | 7 | {6} | 41098 | 360 | 3.153 |
| (0, 4, 5, 7) | 7 | {6} | 41098 | 360 | 3.153 |
| (0, 1, 3, 7) | 7 | {5} | 33087 | 360 | 3.917 |
| (0, 4, 6, 7) | 7 | {5} | 33087 | 360 | 3.917 |

The two perfect 4-mark Sidon rulers (`{0,1,4,6}` and its mirror `{0,2,5,6}`) both achieve v=49109. All 112 non-perfect 4-mark rulers collapse v.

## Why it failed (the obstruction)

When `(R-R)+` has a gap at some integer `k_gap`, the cross-block "shell" at `k_gap·λ` is missing in B. For full coverage `[1, v]`, missing shells must be bridged by overlap of adjacent shells (shell `k_gap-1` upper edge meets shell `k_gap+1` lower edge).

Shell-overlap bridge condition: `2·max(A) ≥ λ − 1`, i.e., `max(A) ≥ (λ−1)/2 ≈ 4005`.

SOTA's `max(A) = 6967` satisfies this comfortably for **adjacent** shells (k → k+1). But for **skipped** shells (k → k+2 with k+1 missing), the condition tightens to `max(A) ≥ λ ≈ 8011`. SOTA's 6967 < 8011 — fails.

So when R has a gap at k_gap, v truncates at the end of shell `k_gap−1` ≈ `(k_gap−1)·λ + max(A)`:
- Gap at 5 (e.g., R = {0,1,3,7}): v ≈ 4·λ + max(A) = 32044 + 6967 = 39011, observed 33087
- Gap at 6 (e.g., R = {0,2,3,7}): v ≈ 5·λ + max(A) = 40055 + 6967 = 47022, observed 41098

(The observed values are below the formula because some shell-internal coverage is also missing.)

## What this rules out

- All 4-mark Sidon rulers besides `{0,1,4,6}` (and its mirror) — when paired with SOTA's atom — give worse score.
- Generalizing: at fixed atom `A_sota` (max(A)=6967 < λ=8011), no 4-mark non-perfect Sidon ruler can reach v ≥ 49109.

## What this does NOT rule out

The atom `A_sota` was held fixed in this test. Two cases remain open:

1. **Different atom + non-perfect 4-mark R**: an atom with `max(A) ≥ λ = 8011` would bridge the missing shells of a non-perfect R. With L=7 or 8, `v_pred = L·λ + c(A)` could reach 56k–64k+. But constructing such atoms with adequate c(A) is the open question.
2. **5-mark Sidon rulers**: `|R|=5` forces `|A|=72` at k=360; L can reach 11. Bridging requires `max(A) ≥ λ` for missing shells. See cycle 5 candidate.

## See also

- [`findings/p19-kronecker-bridging-threshold.md`](p19-kronecker-bridging-threshold.md) — bridging conditions
- [`questions/2026-05-02-p19-kronecker-w4-existence.md`](../questions/2026-05-02-p19-kronecker-w4-existence.md) — original council question (4-mark part now closed; 5-mark + non-fixed-atom remain)
- [`findings/cross-pollination-not-compute.md`](cross-pollination-not-compute.md) — meta-principle

*Last updated: 2026-05-02*
