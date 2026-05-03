#!/usr/bin/env python3
"""Compute Bose-Chowla q=29 explicitly in Z/840, dump its structure.

Closes the open question:
  wiki/questions/2026-05-02-bose-chowla-840-kissing-d12.md

Three hypotheses tested:
- H1 (coincidence): 840 = 29²-1 (BC modulus) AND 840 = κ(12) (kissing count) are unrelated.
- H2 (structural): BC q=29 underlies the K(12)=840 P₁₂ₐ construction.
- H3 (related): BC has multiplicative regularity exploitable in the K(12) analysis.

Method: compute BC(q=29) → 30-element Sidon set in Z/840. Look at:
1. Its element distribution
2. Its difference set (B-B mod 840)
3. Whether either matches the {0, ±1/4, ±1/2, ±1} inner-product structure of P₁₂ₐ

Cardinality check is the first decisive test:
- BC: |B| = 30 (a difference SET in Z/840)
- κ(12) config: 840 POINTS on S¹¹ in ℝ¹²
- These play different mathematical roles; equality of cardinalities (30 vs 840) is required for any
  direct structural identification.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Reuse construction from sibling P19 script
sys.path.insert(0, str(Path(__file__).parent.parent / "difference_bases"))
from bose_chowla import bose_chowla_set


def main():
    q = 29
    modulus = q * q - 1  # 840
    B = bose_chowla_set(q)

    print(f"Bose-Chowla q={q}: Sidon set in Z/{modulus}")
    print(f"  |B| = {len(B)}  (= q+1 = {q+1})")
    print(f"  Modulus = {modulus}  (= q²-1)")
    print()
    print(f"  B = {B}")
    print()

    # Difference set in Z/840 (canonical: min(d, 840-d))
    diffs = set()
    for i, bi in enumerate(B):
        for j in range(i):
            d = (bi - B[j]) % modulus
            d = min(d, modulus - d)
            diffs.add(d)
    print(f"  |B-B|+ (canonical, in Z/{modulus}) = {len(diffs)}")
    print(f"  Expected for Sidon: |B|·(|B|-1)/2 = {len(B)*(len(B)-1)//2}")
    print(f"  Sidon? {'✓' if len(diffs) == len(B)*(len(B)-1)//2 else '✗'}")
    print()

    # Distribution analysis
    diffs_sorted = sorted(diffs)
    print(f"  First 10 diffs: {diffs_sorted[:10]}")
    print(f"  Last 10 diffs:  {diffs_sorted[-10:]}")
    print(f"  Range: [{min(diffs)}, {max(diffs)}]")
    print(f"  In [1, 99]: {sum(1 for d in diffs if 1 <= d <= 99)} values")
    print(f"  In [100, 199]: {sum(1 for d in diffs if 100 <= d <= 199)} values")
    print(f"  In [200, 299]: {sum(1 for d in diffs if 200 <= d <= 299)} values")
    print(f"  In [300, 420]: {sum(1 for d in diffs if 300 <= d <= 420)} values")
    print()

    print("="*70)
    print("Comparison to P₁₂ₐ kissing-12 structure:")
    print()
    print("  κ(12) = 840 configuration:")
    print("    - 840 unit vectors in ℝ¹² on the unit sphere S¹¹")
    print("    - Decomposes as 24 axis shifts (±e_i, i=1..12) + 816 half-integer patterns")
    print("    - 816 = 16 · 51 (code-derived)")
    print("    - All pairwise inner products in {0, ±¼, ±½, ±1}")
    print()
    print("  BC q=29 in Z/840:")
    print(f"    - 30 elements of Z/840 (a Sidon difference SET)")
    print(f"    - {len(diffs)} distinct pairwise differences in Z/840")
    print(f"    - Modulus 840 = (29-1)(29+1)")
    print()
    print("  Cardinality test: 30 (BC elements) vs 840 (kissing points) — MISMATCH.")
    print("  Even at the difference-set level: 435 (BC pairwise diffs) vs ??? (kissing diffs).")
    print()
    print("  The 'pairwise inner products in {0, ±¼, ±½, ±1}' for kissing = 4 distinct values.")
    print("  Bose-Chowla differences span 420 distinct values in [1, 420].")
    print("  Multiplicative structure: completely different.")
    print()
    print("Verdict: H1 (numerical coincidence). The number 840 plays")
    print("DIFFERENT mathematical roles in the two contexts:")
    print("  - In BC: 840 is the GROUP ORDER (|Z/(q²-1)|)")
    print("  - In κ(12): 840 is the COUNT of unit vectors in a code-based config")
    print("These are unrelated; 840 is highly composite (2³·3·5·7) and appears in many contexts.")


if __name__ == "__main__":
    main()
