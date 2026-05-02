#!/usr/bin/env python3
"""Cycle 4 — non-perfect 4-mark Sidon rulers as alternative R for P19 Kronecker.

Cycle 1-3 exhausted single-mark methods on SOTA's atom (perfect Sidon
R = {0,1,4,6}, L=6). Per the cross-pollination filter, the next direction
is changing R — the question council H1 asked but we deferred.

Hypothesis: a non-perfect 4-mark Sidon ruler R' with L > 6 gives larger
v = L·λ + c(A) IF the missing shells (gaps in R'-R'+) are bridged by
shell-overlap (requires max(A) ≥ λ).

Concrete test: enumerate 4-mark Sidon rulers R = {0, a, b, c} with
0 < a < b < c ≤ S_max (some bound), keep only Sidon ones, compute v
for B = A ⊕ λ·R using a candidate A. Look for any (R, A, λ) tuple with
v > 49109 = SOTA.

Strategy: use SOTA's atom A_sota for fairness initially. If that doesn't
work, try simple atom constructions (Wichmann-style) with stretched span.
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
LAM = 8011  # SOTA's lambda


def load_atom():
    data = json.loads(SOTA_PATH.read_text())
    Bset = set(int(x) for x in data["set"])
    if 0 not in Bset:
        Bset.add(0)
    A = sorted(b for b in Bset if b < LAM)
    return np.array(A, dtype=np.int64)


def is_sidon(R):
    """A set is Sidon iff all pairwise positive differences are distinct."""
    R = sorted(R)
    diffs = []
    for i in range(len(R)):
        for j in range(i):
            diffs.append(R[i] - R[j])
    return len(set(diffs)) == len(diffs)


def enumerate_sidon_rulers_4mark(c_max=12):
    """Enumerate 4-mark Sidon rulers with all marks in [0, c_max]."""
    rulers = []
    for a in range(1, c_max + 1):
        for b in range(a + 1, c_max + 1):
            for c in range(b + 1, c_max + 1):
                R = (0, a, b, c)
                if is_sidon(R):
                    rulers.append(R)
    return rulers


def compute_v(B):
    """Brute v: largest integer with {1..v} ⊆ (B-B)+."""
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
    return v, len(diffs)


def kronecker_v(A, R, lam):
    """v(B) where B = A ⊕ lam*R."""
    B = []
    for a in A:
        for r in R:
            B.append(int(a) + lam * r)
    B = sorted(set(B))
    v, _ = compute_v(np.array(B))
    return v, len(B)


def main():
    print("Cycle 4 — non-perfect 4-mark Sidon ruler enumeration for P19")
    print()
    A_sota = load_atom()
    print(f"  |A_sota|={len(A_sota)}, max(A)={int(A_sota[-1])}, λ={LAM}")
    sota_target = 49109
    print(f"  SOTA score 2.6390274695 = 360²/{sota_target}")
    print()

    print("[1/3] Enumerate 4-mark Sidon rulers up to c=12")
    rulers = enumerate_sidon_rulers_4mark(c_max=12)
    print(f"  Found {len(rulers)} 4-mark Sidon rulers")
    # Annotate each with L and gap structure
    perfect_rulers = []
    nonperfect = []
    for R in rulers:
        diffs = sorted({R[i] - R[j] for i in range(len(R)) for j in range(i)})
        L = max(diffs)
        is_perfect = diffs == list(range(1, L + 1))  # covers [1..L] contiguously
        gaps = [d for d in range(1, L + 1) if d not in diffs]
        info = {"R": R, "L": L, "diffs": diffs, "gaps": gaps, "is_perfect": is_perfect}
        if is_perfect:
            perfect_rulers.append(info)
        else:
            nonperfect.append(info)
    print(f"    Perfect: {len(perfect_rulers)} (L=6 only — {{0,1,4,6}} and {{0,2,5,6}})")
    print(f"    Non-perfect: {len(nonperfect)} (L=7..12)")
    print()
    print("  Sample non-perfect rulers (R, L, gaps):")
    nonperfect.sort(key=lambda x: x["L"])
    for info in nonperfect[:10]:
        print(f"    R={info['R']}, L={info['L']}, diffs={info['diffs']}, gaps={info['gaps']}")
    print()

    print("[2/3] For each ruler, compute v(B = A_sota ⊕ λ·R)")
    print(f"  {'R':<22}{'L':<5}{'gaps':<14}{'v(B)':<10}{'k=|B|':<8}{'score':<14}{'beats SOTA?':<14}")
    results = []
    for info in [{"R": (0, 1, 4, 6), "L": 6, "gaps": [], "is_perfect": True}] + nonperfect:
        R = info["R"]
        L = info["L"]
        v, k = kronecker_v(A_sota, R, LAM)
        score = k ** 2 / v if v > 0 else float("inf")
        beats = "YES" if score < 2.6390274695 - 1e-9 else "no"
        results.append({"R": R, "L": L, "gaps": info["gaps"], "v": v, "k": k, "score": score, "beats": beats})
        if v > 30000 or info["L"] == 6 or beats == "YES":
            print(f"  {str(R):<22}{L:<5}{str(info['gaps']):<14}{v:<10}{k:<8}{score:<14.6f}{beats:<14}")

    print()
    print("[3/3] Top 5 by score (lowest = best)")
    results.sort(key=lambda r: r["score"])
    for r in results[:5]:
        print(f"  R={r['R']}, L={r['L']}, gaps={r['gaps']}, v={r['v']}, k={r['k']}, score={r['score']:.6f}")

    print()
    best = results[0]
    if best["beats"] == "YES":
        print(f"  ★ HIT: R={best['R']} gives score {best['score']:.10f} < 2.6390274695")
    else:
        print(f"  No hit. Best non-SOTA: R={best['R']}, score={best['score']:.6f}")
        print(f"  Implication: SOTA's R={{0,1,4,6}} is locally optimal among 4-mark Sidon rulers")
        print(f"               when paired with atom A_sota.")
        print(f"  Note: this test FIXES the atom. Different (R', A') joint optimization is open.")


if __name__ == "__main__":
    main()
