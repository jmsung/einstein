#!/usr/bin/env python3
"""Spec C — cross-block coverage scaling for P19 Kronecker decomposition.

Tests whether `v(A, R, λ) = L·λ + c(A)` is exact (tight) or only a lower bound,
on the SOTA's structure: B = A_sota ⊕ 8011·{0,1,4,6}, |A|=90, c(A)=1043, v=49109.

If the formula is *only a lower bound*, then a different A' with smaller c(A')
but better cross-block density could yield v(A') > L·λ + c(A') — refuting the
prior framing that "atom is the bottleneck and c(A) is the only lever."

Per the cross-pollination-not-compute filter: this is a 1-day diagnostic with
either-way wisdom yield (the formula is tight → confirms framing; loose → new
optimization target).
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import numpy as np

SOTA_PATH = Path(
    "/Users/jongmin/projects/einstein/mb/tracking/problem-19-difference-bases/"
    "solutions/sota-rank01-CHRONOS-score2.6390274695.json"
)


def load_sota():
    data = json.loads(SOTA_PATH.read_text())
    B = sorted(set(int(x) for x in data["set"]))
    if 0 not in B:
        B = [0] + B
    return np.array(B, dtype=np.int64)


def compute_v_set(B):
    """Largest v such that {1, ..., v} ⊆ (B - B)+."""
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
    return v, diffs


def kronecker_decomposition_check(B, R=(0, 1, 4, 6), lam=8011):
    """Verify B = A ⊕ λ·R and return atom A, lam, R."""
    Bset = set(int(x) for x in B)
    # For each b in B, find the (a, r) pair such that b = a + lam*r.
    # The atom A consists of all b's where b mod lam < lam (lowest r=0 block has the smallest values).
    # For SOTA: B has 4 blocks at offsets 0, 8011, 4·8011=32044, 6·8011=48066.
    # The atom A is recovered as {b : b in B, b - 0 < lam} (the r=0 block).
    A = sorted([b for b in Bset if b < lam])
    print(f"  Recovered atom A: |A|={len(A)}, span={A[-1] if A else 0}")
    # Verify B = A ⊕ lam·R
    expected_B = set()
    for a in A:
        for r in R:
            expected_B.add(a + lam * r)
    if expected_B == Bset:
        print(f"  ✓ Kronecker decomposition verified: B = A ⊕ {lam}·{list(R)}")
    else:
        print(f"  ✗ MISMATCH: |B|={len(Bset)}, |expected|={len(expected_B)}")
        print(f"    in B not expected: {sorted(Bset - expected_B)[:5]}")
        print(f"    in expected not B: {sorted(expected_B - Bset)[:5]}")
    return np.array(A, dtype=np.int64), lam, R


def per_shell_coverage(A, R, lam):
    """For each cross-block shell k = r1 - r2 ∈ (R-R), compute the set of differences
    contributed by that shell.

    Shell k = 0: same-block, differences are (A-A)+
    Shell k = +1: differences are (A-A) + lam (mostly positive if lam > max(A))
    Shell k = +k: differences are (A-A) + k·lam
    """
    R = list(R)
    shell_diffs = defaultdict(set)  # shell k -> set of positive differences

    for r1 in R:
        for r2 in R:
            k = r1 - r2  # shell index
            for a1 in A:
                for a2 in A:
                    d = int((a1 + lam * r1) - (a2 + lam * r2))
                    if d > 0:
                        shell_diffs[k].add(d)
    return shell_diffs


def coverage_density_per_shell(shell_diffs, lam, max_A):
    """For each shell k > 0, compute (covered, theoretical_max) = (|filled|, |window|).

    The shell window for k > 0 is [k·lam - max_A, k·lam + max_A] = width 2·max_A + 1.
    """
    rows = []
    for k in sorted(shell_diffs.keys()):
        if k <= 0:
            continue
        diffs_k = shell_diffs[k]
        window_lo = max(1, k * lam - max_A)
        window_hi = k * lam + max_A
        diffs_in_window = sum(1 for d in diffs_k if window_lo <= d <= window_hi)
        window_width = window_hi - window_lo + 1
        rows.append({
            "shell_k": k,
            "window_lo": window_lo,
            "window_hi": window_hi,
            "window_width": window_width,
            "covered_in_window": diffs_in_window,
            "density": diffs_in_window / window_width if window_width > 0 else 0,
            "covered_total": len(diffs_k),
        })
    return rows


def detailed_coverage_breakdown(B, A, R, lam, v_sota):
    """For each integer d in [1, v_sota], identify which shell(s) cover it."""
    R = list(R)
    Aset = set(int(a) for a in A)

    d_shells = defaultdict(set)  # d -> set of shells k that cover d
    for r1 in R:
        for r2 in R:
            k = r1 - r2
            for a1 in A:
                for a2 in A:
                    d = int((a1 + lam * r1) - (a2 + lam * r2))
                    if 0 < d <= v_sota:
                        d_shells[d].add(k)

    # Compute multiplicity per shell
    by_shell_count = defaultdict(int)
    for d, shells in d_shells.items():
        by_shell_count[len(shells)] += 1

    return d_shells, by_shell_count


def test_formula_tightness(A, R, lam, c_A, v_actual):
    """Test the claim v = L·λ + c(A).

    For SOTA: L = max((R-R)+) = 6, λ = 8011, c(A) = 1043.
    Predicted: v = 6·8011 + 1043 = 49109. Actual: 49109. So formula is TIGHT for SOTA.

    But this is just a single point. To test whether formula is generally tight,
    perturb A and recompute v vs. predicted.
    """
    R = list(R)
    R_diffs = set()
    for r1 in R:
        for r2 in R:
            d = r1 - r2
            if d > 0:
                R_diffs.add(d)
    L = max(R_diffs)
    predicted = L * lam + c_A
    print(f"\n  Formula v_pred = L·λ + c(A) = {L}·{lam} + {c_A} = {predicted}")
    print(f"  Actual:                v       = {v_actual}")
    print(f"  Formula {'TIGHT' if v_actual == predicted else 'LOOSE'} for SOTA point.")

    return predicted, L


def perturb_test(A_sota, R, lam, n_perturbations=20):
    """Perturb A by small modifications. For each perturbed A':
    - compute c(A')
    - compute v(A' ⊕ R, lam) directly
    - compare to formula L·λ + c(A')
    - report whether perturbation falsifies the formula (v_actual > v_pred → formula loose)
    """
    R = list(R)
    R_diffs = sorted({r1 - r2 for r1 in R for r2 in R if r1 != r2 and r1 - r2 > 0})
    L = max(R_diffs)

    Aset = set(int(a) for a in A_sota)

    # Compute baseline c(A)
    A_diffs_pos = set()
    for a in A_sota:
        for b in A_sota:
            if a > b:
                A_diffs_pos.add(int(a - b))
    c_A_sota = 0
    while (c_A_sota + 1) in A_diffs_pos:
        c_A_sota += 1

    print(f"\n  Baseline: c(A_sota) = {c_A_sota}")
    print(f"  Will test {n_perturbations} small perturbations (1-swap inside A)")
    print(f"\n  {'#':<4}{'swap':<20}{'c(A)':<8}{'v_actual':<10}{'v_pred':<10}{'gap':<8}{'verdict':<12}")

    rng = np.random.default_rng(seed=42)
    falsified = []
    confirmed = []

    candidates = []
    for _ in range(n_perturbations):
        # Pick a mark to remove and one to add (1-swap)
        idx = int(rng.integers(0, len(A_sota)))
        x_old = int(A_sota[idx])
        # Pick a new mark in [1, max(A)] not already in A
        for _ in range(10):
            x_new = int(rng.integers(1, int(A_sota[-1]) + 1))
            if x_new not in Aset and x_new != x_old:
                break
        else:
            continue
        A_new = sorted((Aset - {x_old}) | {x_new})
        candidates.append((idx, x_old, x_new, A_new))

    for i, (idx, x_old, x_new, A_new) in enumerate(candidates):
        # Compute c(A')
        A_diffs = set()
        for a in A_new:
            for b in A_new:
                if a > b:
                    A_diffs.add(a - b)
        c_A = 0
        while (c_A + 1) in A_diffs:
            c_A += 1

        # Compute v(B') exactly
        B_new = []
        for a in A_new:
            for r in R:
                B_new.append(a + lam * r)
        B_new = sorted(set(B_new))
        v_actual, _ = compute_v_set(B_new)

        v_pred = L * lam + c_A
        gap = v_actual - v_pred
        verdict = "FORMULA LOOSE" if gap > 0 else ("formula tight" if gap == 0 else "formula low?")
        print(f"  {i+1:<4}-{x_old}+{x_new:<14}{c_A:<8}{v_actual:<10}{v_pred:<10}{gap:<8}{verdict:<12}")

        if gap > 0:
            falsified.append((idx, x_old, x_new, c_A, v_actual, v_pred, gap))
        elif gap == 0:
            confirmed.append((idx, x_old, x_new, c_A, v_actual, v_pred))

    return falsified, confirmed


def main():
    print("Spec C — cross-block coverage scaling test for P19")
    print()
    print("[1/5] Load SOTA")
    B = load_sota()
    v_sota, _ = compute_v_set(B)
    print(f"  k={len(B)}, v={v_sota}, score={len(B)**2 / v_sota:.10f}")

    print("\n[2/5] Verify Kronecker decomposition B = A ⊕ 8011·{0,1,4,6}")
    A, lam, R = kronecker_decomposition_check(B)

    print("\n[3/5] Per-shell coverage analysis")
    A_diffs_pos = set()
    for a in A:
        for b in A:
            if a > b:
                A_diffs_pos.add(int(a - b))
    c_A = 0
    while (c_A + 1) in A_diffs_pos:
        c_A += 1
    print(f"  c(A) = {c_A}")
    print(f"  max(A) = {int(A[-1])}")
    print(f"  |A-A pos| = {len(A_diffs_pos)}")

    shell_diffs = per_shell_coverage(A, R, lam)
    rows = coverage_density_per_shell(shell_diffs, lam, int(A[-1]))
    print()
    print("  shell  window range          width   covered  density  covered_total")
    for r in rows:
        print(f"  {r['shell_k']:<6} [{r['window_lo']:>5}, {r['window_hi']:>5}]   "
              f"{r['window_width']:<7} {r['covered_in_window']:<8} "
              f"{r['density']:<8.3f} {r['covered_total']}")

    print("\n[4/5] Test formula tightness on SOTA")
    v_pred, L = test_formula_tightness(A, R, lam, c_A, v_sota)

    print("\n[5/5] Perturbation test (1-swap inside A)")
    falsified, confirmed = perturb_test(A, R, lam, n_perturbations=15)

    print("\n=== Verdict ===")
    print(f"  Formula tight on SOTA:        v = {v_sota}, predicted = {v_pred}, equal: {v_sota == v_pred}")
    print(f"  Perturbation outcomes:        {len(falsified)} formula-loose, {len(confirmed)} formula-tight")
    if falsified:
        print(f"\n  REFUTED — formula is only a lower bound. Best falsifying perturbation:")
        best = max(falsified, key=lambda x: x[6])
        print(f"    swap idx {best[0]}: {best[1]} -> {best[2]}, c(A')={best[3]}, "
              f"v_actual={best[4]}, v_pred={best[5]}, gap={best[6]}")
        print(f"\n  Implication: cross-block contribution can exceed the formula's prediction.")
        print(f"  Direction: search for A' with c(A') ≤ c(A_sota) but better cross-block density.")
    else:
        print(f"\n  CONFIRMED — formula is tight across all tested perturbations of A.")
        print(f"  Implication: c(A) is the true bottleneck. To improve v at fixed (R, λ), must improve c(A).")


if __name__ == "__main__":
    main()
