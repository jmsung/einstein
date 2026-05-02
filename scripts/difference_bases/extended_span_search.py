#!/usr/bin/env python3
"""Cycle 3 — extended-span atom search for P19.

Hypothesis (from p19-kronecker-bridging-threshold.md): the SOTA atom is locked
at max(A)=6967 because prior search FIXED span=6967. With max(A) extended to
[6968, 8000], the bridging threshold relaxes (c(A) ≥ λ − max(A) − 1, where
λ=8011) but to BEAT SOTA we need c(A) ≥ 1044 — same as prior w=3 BnB target.

The genuinely-new direction: swap a SOTA mark x for a new mark y > 6967.
The extra "room" in [6968, 8000] gives 1033 candidate y values that prior
work's 1-swap range [0, 7000] did NOT test.

If any 1-swap (x → y, y ∈ [6968, 8010]) gives c(A_new) ≥ 1044 AND bridging
still holds (max(A_new) ≤ 8010 = λ - c(A) + 1 for c(A)=1043, but with
c(A_new) ≥ 1044 the bridging is automatic for max ≤ λ - 1 = 8010), we have
an improvement candidate.

Cost: ~1033 y × ~90 x = 93k swaps to test. Each c() computation is O(|A|²)
≈ 8000 ops. Total ~750M ops. Should run in ~30s on M5.
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np

SOTA_PATH = Path(
    "/Users/jongmin/projects/einstein/mb/tracking/problem-19-difference-bases/"
    "solutions/sota-rank01-CHRONOS-score2.6390274695.json"
)
LAM = 8011
R = (0, 1, 4, 6)


def load_atom():
    """Recover the 90-mark SOTA atom A from the full SOTA solution."""
    data = json.loads(SOTA_PATH.read_text())
    Bset = set(int(x) for x in data["set"])
    if 0 not in Bset:
        Bset.add(0)
    A = sorted(b for b in Bset if b < LAM)
    return np.array(A, dtype=np.int64)


def c_of(A_set):
    """Longest contiguous prefix of (A − A)+ starting at 1."""
    diffs = set()
    A_list = sorted(A_set)
    n = len(A_list)
    for i in range(n):
        for j in range(i):
            diffs.add(A_list[i] - A_list[j])
    c = 0
    while (c + 1) in diffs:
        c += 1
    return c


def main():
    print("Cycle 3 — extended-span 1-swap search for P19")
    print()
    A_sota = load_atom()
    A_sota_set = set(int(x) for x in A_sota)
    c_sota = c_of(A_sota_set)
    max_sota = max(A_sota_set)
    print(f"  |A_sota| = {len(A_sota)}, max(A) = {max_sota}, c(A) = {c_sota}")
    print(f"  Target: c(A_new) ≥ {c_sota + 1} = 1044  (would break the SOTA basin)")

    # Y range to test: NEW marks in (max_sota, λ-1]
    # max_sota = 6967, λ = 8011, so y ∈ [6968, 8010] = 1043 candidates
    y_min = max_sota + 1
    y_max = LAM - 1
    print(f"  Extended y range: [{y_min}, {y_max}] = {y_max - y_min + 1} candidates")
    print(f"  (prior 1-swap exhaustive tested y ∈ [0, 7000]; this extends by {y_max - 7000} new y values)")
    print()

    n_swaps_tested = 0
    n_safe_to_remove = 0
    best_c = c_sota
    hits = []

    for y in range(y_min, y_max + 1):
        if y in A_sota_set:
            continue
        for x in A_sota_set:
            if x == y:
                continue
            A_new = (A_sota_set - {x}) | {y}
            c_new = c_of(A_new)
            n_swaps_tested += 1
            if c_new == c_sota:
                n_safe_to_remove += 1
            if c_new > best_c:
                best_c = c_new
                hits.append((y, x, c_new))
                print(f"  IMPROVEMENT: y={y}, x={x} → c(A_new)={c_new}")

    print()
    print(f"  Swaps tested:        {n_swaps_tested:,}")
    print(f"  Safe-to-remove (c stays at {c_sota}):  {n_safe_to_remove:,}")
    print(f"  Best c(A_new) found: {best_c}")
    print(f"  Improvements found:  {len(hits)}")
    print()

    if hits:
        print("  ✓ HITS FOUND — at least one 1-swap with extended y improves c(A).")
        print(f"  Best: c(A_new) = {best_c}")
        # Compute v(B_new)
        best_y, best_x, best_c_val = hits[0]
        A_best = sorted((A_sota_set - {best_x}) | {best_y})
        max_A_best = max(A_best)
        # Predicted v with new max(A)
        L = max(r1 - r2 for r1 in R for r2 in R if r1 > r2)
        v_pred = L * LAM + best_c_val
        print(f"\n  Best atom A': max(A')={max_A_best}, c(A')={best_c_val}")
        print(f"  Bridging condition: c(A') ≥ λ − max(A') − 1 = {LAM - max_A_best - 1}")
        if best_c_val >= LAM - max_A_best - 1:
            print(f"  ✓ Bridging holds")
        else:
            print(f"  ✗ Bridging FAILS — formula doesn't apply, v will collapse")
        print(f"  Predicted v(B_new) = L·λ + c(A') = {L}·{LAM} + {best_c_val} = {v_pred}")
        if v_pred > 49109:
            score = 360 ** 2 / v_pred
            print(f"  Predicted score: 360²/{v_pred} = {score:.10f}")
            print(f"  SOTA score:      2.6390274695")
            print(f"  Δ score:         {score - 2.6390274695:+.6e}")
            if score < 2.6390274695:
                print(f"  *** PREDICTED IMPROVEMENT — needs triple-verify ***")
    else:
        print("  ✗ NO HITS — extended-span 1-swap finds no atom with c(A) > 1043.")
        print(f"  This refines the prior negative (1-swap [0, 7000]) to [0, 8010].")
        print(f"  Implication: the SOTA atom basin is rigid even in the extended-span design space.")
        print(f"  Cycle 4 candidate: 2-swap with extended y, OR pivot to a different cross-pollination thread.")


if __name__ == "__main__":
    main()
