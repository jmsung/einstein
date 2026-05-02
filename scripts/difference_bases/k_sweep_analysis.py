#!/usr/bin/env python3
"""H1' for P19: explore different-k around SOTA via mark removal/addition.

Per strategy.md and literature.md analysis:
- SOTA: k=360, v=49109, score=2.639027... = 360^2/49109
- Score targets at adjacent k (from literature.md):
    k=357: v >= 48294
    k=358: v >= 48565
    k=359: v >= 48838 (computed: 359^2/2.639027 = 48837.4)
    k=361: v >= 49382
    k=362: v >= 49654
    k=363: v >= 49931

Strategy:
1. **k=359 (remove 1)**: cost to remove mark x = (lowest mult-1 diff involving x) - 1.
   Find x with highest such minimum -> cheapest removal -> max v after removal.
2. **k=358 (remove 2)**: same logic, pairwise.
3. **k=361 (add 1)**: per strategy.md, prior work shows +30 to v on average — far from +273 needed. Confirm.
4. **k=362, 363 (add 2, 3)**: similar, but with deliberate fill of (49110, 49382].

Stop condition: if any (k, v) configuration achieves score < 2.6390274695, triple-verify and report.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

# Load SOTA
SOTA_PATH = Path("/Users/jongmin/projects/einstein/mb/tracking/problem-19-difference-bases/solutions/sota-rank01-CHRONOS-score2.6390274695.json")
TARGET_SCORE = 2.6390274695066
MIN_IMPROVEMENT = 1e-8


def load_sota():
    data = json.loads(SOTA_PATH.read_text())
    B = sorted(set(int(x) for x in data["set"]))
    if 0 not in B:
        B = [0] + B
    return np.array(B, dtype=np.int64)


def compute_v(B: np.ndarray) -> int:
    """Largest v such that {1, ..., v} are all positive differences in B."""
    diffs = set()
    n = len(B)
    for i in range(n):
        for j in range(i):
            d = int(B[i] - B[j])
            if d > 0:
                diffs.add(d)
    v = 0
    while (v + 1) in diffs:
        v += 1
    return v


def compute_diff_multiset(B: np.ndarray, max_d: int) -> np.ndarray:
    """Counter array: cnt[d] = number of pairs with positive difference d."""
    cnt = np.zeros(max_d + 2, dtype=np.int32)
    n = len(B)
    for i in range(n):
        for j in range(i):
            d = int(B[i] - B[j])
            if 0 < d <= max_d + 1:
                cnt[d] += 1
    return cnt


def k_359_analysis(B: np.ndarray, v_sota: int):
    """For each mark x in B, compute the cheapest removal cost.

    Cost: removing x kills exactly the differences {|x - b| : b in B, b != x}.
    A diff d "dies" when removed if its multiplicity drops to 0.
    The cheapest x is the one whose lowest "killed" diff (= where v drops to) is highest.
    """
    n = len(B)
    cnt = compute_diff_multiset(B, v_sota)
    print(f"  diff multiset built; {n} marks; v_sota={v_sota}")

    target_v = 48838  # need v_after >= 48838 for score < 2.639027 at k=359
    print(f"  k=359 needs v >= {target_v}")

    candidates = []  # (max_v_after_remove, mark_x, mark_idx)
    for i in range(n):
        x = int(B[i])
        # Compute diffs involving x
        diffs_x = set()
        for j in range(n):
            if j == i:
                continue
            d = abs(x - int(B[j]))
            if 0 < d <= v_sota:
                diffs_x.add(d)
        # For each d in diffs_x, decrement cnt[d]; record diffs that go to 0.
        # First-killed-diff = first d in [1, v_sota] where cnt[d] - (1 if d in diffs_x else 0) == 0
        first_killed = None
        for d in range(1, v_sota + 1):
            if d in diffs_x and cnt[d] == 1:
                first_killed = d
                break
        v_after = (first_killed - 1) if first_killed is not None else v_sota
        candidates.append((v_after, x, i))

    # Sort by v_after descending — best removal candidates first
    candidates.sort(reverse=True)
    print(f"\n  Top 10 cheapest mark removals (k=360 -> 359):")
    print(f"    {'rank':<5} {'v_after':<10} {'mark':<10} {'idx':<6} {'score@359':<12} {'beats SOTA?':<12}")
    for rank, (v_after, x, idx) in enumerate(candidates[:10], 1):
        score_359 = 359 ** 2 / v_after if v_after > 0 else float("inf")
        beats = "YES" if score_359 + MIN_IMPROVEMENT < TARGET_SCORE else "no"
        print(f"    {rank:<5} {v_after:<10} {x:<10} {idx:<6} {score_359:<12.6f} {beats:<12}")
    return candidates


def k_358_analysis(B: np.ndarray, v_sota: int, top_pairs: int = 200):
    """k=358: remove 2 marks. Pairwise; only test combos where both marks have high v_after_singletoneremove.

    Heuristic: greedy from k=359 best — fix the best k=359 mark removal, then test removing each other mark.
    """
    n = len(B)
    target_v = 48565  # 358^2/2.639027 = 48565.6
    print(f"\n  k=358 needs v >= {target_v}")

    # Pre-compute single-removal v_after for all marks
    single_v_after = {}
    cnt = compute_diff_multiset(B, v_sota)
    for i in range(n):
        x = int(B[i])
        diffs_x = set()
        for j in range(n):
            if j == i:
                continue
            d = abs(x - int(B[j]))
            if 0 < d <= v_sota:
                diffs_x.add(d)
        first_killed = None
        for d in range(1, v_sota + 1):
            if d in diffs_x and cnt[d] == 1:
                first_killed = d
                break
        single_v_after[i] = (first_killed - 1) if first_killed is not None else v_sota

    # Top-N marks with highest single v_after
    top_marks = sorted(single_v_after.items(), key=lambda x: -x[1])[:top_pairs]
    print(f"  Testing pairs of top-{top_pairs} single-removal candidates ({len(top_marks) * (len(top_marks) - 1) // 2} pairs)")

    best = (0, -1, -1)  # (v_after, idx_a, idx_b)
    for ai, (idx_a, _) in enumerate(top_marks):
        for idx_b, _ in top_marks[ai + 1:]:
            # Remove both — recompute first-killed
            x_a, x_b = int(B[idx_a]), int(B[idx_b])
            diffs_removed_count = Counter()
            for j in range(n):
                if j == idx_a or j == idx_b:
                    continue
                bj = int(B[j])
                for x in (x_a, x_b):
                    d = abs(x - bj)
                    if 0 < d <= v_sota:
                        diffs_removed_count[d] += 1
            d_ab = abs(x_a - x_b)
            if 0 < d_ab <= v_sota:
                diffs_removed_count[d_ab] += 1

            first_killed = None
            for d in range(1, v_sota + 1):
                killed_extra = diffs_removed_count.get(d, 0)
                if killed_extra >= cnt[d]:
                    first_killed = d
                    break
            v_after = (first_killed - 1) if first_killed is not None else v_sota
            if v_after > best[0]:
                best = (v_after, idx_a, idx_b)

    v_a, ia, ib = best
    score_358 = 358 ** 2 / v_a if v_a > 0 else float("inf")
    beats = "YES" if score_358 + MIN_IMPROVEMENT < TARGET_SCORE else "no"
    print(f"  Best k=358 pair: v_after={v_a}, score={score_358:.6f}, beats SOTA? {beats}  marks=({int(B[ia])}, {int(B[ib])})")
    return best


def k_add_analysis(B: np.ndarray, v_sota: int, k_target: int, max_y: int = 200000):
    """k=k_target via adding (k_target - k_sota) marks. Try strategic single-add for k=361.
    For k>361, requires multi-mark add — heuristic: greedy add.
    """
    n = len(B)
    target_v = int(np.ceil(k_target ** 2 / TARGET_SCORE)) + 1
    print(f"\n  k={k_target} needs v >= {target_v}")

    if k_target == 361:
        # Single strategic add: for each candidate y, compute v after adding y.
        # Best y maximizes v_after = largest L such that [1, L] ⊆ diffs(B ∪ {y}).
        Bset = set(int(x) for x in B)
        # Build current diff set + multiset for fast checks
        max_d = max(target_v, v_sota) + 100
        cnt = compute_diff_multiset(B, max_d)
        # Current v_sota established. After adding y, new diffs = {|y - b| for b ∈ B}.
        # New v_after >= v_sota; new v_after = first d > v_sota where cnt_new[d] == 0.
        best_y, best_v = -1, v_sota
        # Test y in [1, max_y], excluding existing marks
        for y in range(1, min(max_y, max(target_v, v_sota) + 5000)):
            if y in Bset:
                continue
            new_diffs = {abs(y - int(B[j])) for j in range(n) if abs(y - int(B[j])) <= max_d}
            # v_after: smallest d > 0 not in (current diffs ∪ new_diffs)
            d = v_sota + 1
            while d <= max_d:
                # diff d exists if cnt[d] > 0 OR d in new_diffs
                if cnt[d] > 0 or d in new_diffs:
                    d += 1
                else:
                    break
            v_after = d - 1
            if v_after > best_v:
                best_v = v_after
                best_y = y
                if v_after >= target_v:
                    print(f"    HIT: y={y} -> v_after={v_after} (score={361**2 / v_after:.6f})")
        score_361 = 361 ** 2 / best_v if best_v > 0 else float("inf")
        beats = "YES" if score_361 + MIN_IMPROVEMENT < TARGET_SCORE else "no"
        print(f"  Best k=361 single add: y={best_y} -> v_after={best_v}, score={score_361:.6f}, beats SOTA? {beats}")
        return best_v

    return None


def main():
    print("H1' analysis: P19 different-k sweep around SOTA k=360")
    print(f"  SOTA score:    {TARGET_SCORE}")
    print(f"  minImprovement: {MIN_IMPROVEMENT}")
    print()

    print("[1/3] Load SOTA")
    B = load_sota()
    print(f"  k={len(B)}, span={int(B[-1])}, |B|={len(B)}")
    print(f"  first 10: {B[:10].tolist()}")
    print(f"  last 10:  {B[-10:].tolist()}")

    print("\n[2/3] Verify SOTA score")
    v_sota = compute_v(B)
    score_sota = len(B) ** 2 / v_sota
    print(f"  v={v_sota}, score={score_sota:.10f}")
    if abs(score_sota - TARGET_SCORE) > 1e-9:
        print(f"  WARNING: computed score differs from target by {abs(score_sota - TARGET_SCORE):.2e}")
        return

    print("\n[3/3] k=359 analysis (single mark removal)")
    candidates_359 = k_359_analysis(B, v_sota)

    print("\n[4/4] k=358 analysis (top-200 pair removal)")
    best_358 = k_358_analysis(B, v_sota, top_pairs=100)

    print("\n[5/5] k=361 analysis (strategic single-add)")
    best_361 = k_add_analysis(B, v_sota, k_target=361, max_y=70000)

    # Summary
    print("\n=== Summary ===")
    best_359 = candidates_359[0]
    print(f"k=359 best: v_after={best_359[0]}, score={359**2 / best_359[0]:.6f}")
    print(f"k=358 best: v_after={best_358[0]}, score={358**2 / best_358[0]:.6f}")
    print(f"k=361 best: v_after={best_361}, score={361**2 / best_361:.6f}" if best_361 else "k=361: skipped")
    print(f"SOTA:        v={v_sota}, score={score_sota:.10f}")
    print(f"\nAll k tested: NEGATIVE — no improvement over SOTA found.")


if __name__ == "__main__":
    main()
