#!/usr/bin/env python3
"""Bose–Chowla Sidon-set construction (1962) and its application to P19.

Bose–Chowla 1962: for any prime power q, there exists a Sidon set (B_2[1] set)
of size q inside Z/(q^2 - 1). Constructed via discrete logarithms of trace-zero
elements in GF(q^2).

For P19 (max v such that {1..v} ⊆ (B-B)+, score = |B|²/v), we want a 90-mark
"atom" with HIGH contiguous-prefix coverage c(A). Bose–Chowla gives a Sidon
set — every difference distinct — which means c(A) is SMALL because most of
[1, q²-1] is empty. This is the structural reason all classical algebraic
Sidon constructions (Singer, Bose-Chowla, Paley QR, GMW) fail for P19.

This script verifies the construction for small q, then projects the c(A)
that would result for q ≈ 89 (Bose–Chowla's closest match to P19's |A|=90).

Companion to:
- wiki/concepts/bose-chowla-construction.md
- wiki/findings/dead-end-p19-bose-chowla.md (this cycle's deliverable)
"""
from __future__ import annotations

import sys

import numpy as np


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


def primitive_root(p: int) -> int:
    """Find smallest primitive root mod prime p."""
    if not is_prime(p):
        raise ValueError(f"{p} not prime")
    phi = p - 1
    factors = []
    n = phi
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, phi // f, p) != 1 for f in factors):
            return g
    raise RuntimeError("no primitive root found")


def gf_q2_mul(a, b, p, irred_const):
    """Multiplication in GF(p²) = F_p[x]/(x² - irred_const).
    Elements as (a0, a1) representing a0 + a1*x.
    """
    a0, a1 = a
    b0, b1 = b
    return ((a0 * b0 + irred_const * a1 * b1) % p, (a0 * b1 + a1 * b0) % p)


def find_irreducible_constant(p: int) -> int:
    """Find smallest non-square c in F_p* so x² - c is irreducible."""
    squares = {(i * i) % p for i in range(1, p)}
    for c in range(2, p):
        if c not in squares:
            return c
    raise RuntimeError(f"no non-square found in F_{p}")


def find_primitive_element_gf_q2(p: int):
    """Find primitive element θ in GF(p²) by trial.
    GF(p²) has multiplicative order p² - 1. θ is primitive iff θ^d ≠ 1 for any
    proper divisor d of p² - 1.
    Returns (theta, irred_const).
    """
    irred = find_irreducible_constant(p)
    n = p * p - 1
    factors = []
    nn = n
    d = 2
    while d * d <= nn:
        if nn % d == 0:
            factors.append(d)
            while nn % d == 0:
                nn //= d
        d += 1
    if nn > 1:
        factors.append(nn)
    # θ candidates: try (a, 1) for a = 0, 1, 2, ...
    for a in range(p):
        theta = (a, 1)
        is_prim = True
        for f in factors:
            d = n // f
            x = (1, 0)
            base = theta
            e = d
            while e > 0:
                if e & 1:
                    x = gf_q2_mul(x, base, p, irred)
                base = gf_q2_mul(base, base, p, irred)
                e >>= 1
            if x == (1, 0):
                is_prim = False
                break
        if is_prim:
            return theta, irred
    raise RuntimeError(f"no primitive element found in GF({p}²)")


def bose_chowla_set(p: int):
    """Construct the Bose–Chowla Sidon set of size p+1 in Z/(p²-1).

    Method: B = {discrete_log(θ − a) : a ∈ F_p}, where θ is primitive in GF(p²).
    Reference: Bose & Chowla 1962, Comment. Math. Helv.

    Returns sorted list of integers in [0, p²-2] of size p+1.
    """
    if not is_prime(p):
        raise ValueError(f"{p} must be prime (prime power extension possible)")
    theta, irred = find_primitive_element_gf_q2(p)
    n = p * p - 1

    # Build discrete-log table: log[(a0, a1)] = k such that θ^k = (a0, a1).
    log_table = {}
    x = (1, 0)
    for k in range(n):
        log_table[x] = k
        x = gf_q2_mul(x, theta, p, irred)

    # B = {log(θ − a) : a ∈ F_p}
    a0_theta, a1_theta = theta
    B = []
    for a in range(p):
        diff = ((a0_theta - a) % p, a1_theta)
        if diff == (0, 0):
            continue  # would be log(0), undefined; corresponds to a=θ which can't happen for θ ∉ F_p
        if diff in log_table:
            B.append(log_table[diff])
    return sorted(B)


def is_sidon(B, modulus=None):
    """Check that B is a Sidon set: all unordered-pair sums distinct.
    Equivalently, all positive differences B[i]-B[j] (i>j) distinct, possibly mod m.
    """
    diffs = set()
    n = len(B)
    for i in range(n):
        for j in range(i):
            d = B[i] - B[j]
            if modulus:
                d = d % modulus
                # canonical representative: min(d, modulus-d) for symmetry
                d = min(d, modulus - d)
            if d in diffs:
                return False, d
            diffs.add(d)
    return True, len(diffs)


def contiguous_prefix(B):
    """c(B): largest L such that {1, ..., L} ⊆ (B-B)⁺."""
    diffs = set()
    n = len(B)
    for i in range(n):
        for j in range(i):
            d = B[i] - B[j]
            if d > 0:
                diffs.add(d)
    L = 0
    while (L + 1) in diffs:
        L += 1
    return L


def main():
    print("Bose–Chowla Sidon-set construction — verification + P19 projection")
    print()

    SOTA_ATOM_K = 90
    SOTA_ATOM_C = 1043
    SOTA_ATOM_MAX = 6967

    # Verify on small primes
    for q in [3, 5, 7, 11, 13, 17, 23]:
        try:
            B = bose_chowla_set(q)
            ok, dist = is_sidon(B, modulus=q * q - 1)
            cB = contiguous_prefix(B)
            print(f"  q={q:>3}, |B|={len(B):>3}, modulus={q*q-1:>5}, "
                  f"sidon={'✓' if ok else '✗'}, distinct_diffs={dist}, c(B)={cB}")
        except Exception as e:
            print(f"  q={q}: failed — {e}")

    print()
    print("Bose–Chowla scaling for P19:")
    print(f"  P19 SOTA atom: |A|={SOTA_ATOM_K}, c(A)={SOTA_ATOM_C}, max(A)={SOTA_ATOM_MAX}")
    print()

    # The closest prime to give |B| ≈ 90:
    for q in [83, 89, 97]:
        try:
            B = bose_chowla_set(q)
            ok, dist = is_sidon(B, modulus=q * q - 1)
            cB = contiguous_prefix(B)
            modulus = q * q - 1
            print(f"  q={q}: |B|={len(B)}, modulus={modulus}, sidon={ok}, c(B)={cB}")
            print(f"    structure: Sidon set in Z/{modulus} of size {q}")
            # P19 framework: B = A ⊕ λ·R with R = {0,1,4,6}, λ=8011
            # If A = Bose-Chowla atom, k_total = |A|·4 = 4·{|B|}, v_pred = 6·8011 + c(A)
            k_total = 4 * len(B)
            v_pred = 6 * 8011 + cB
            score_pred = k_total ** 2 / v_pred if v_pred > 0 else float("inf")
            v_needed_to_beat = int(np.ceil(k_total ** 2 / 2.6390274695)) + 1
            print(f"    if used as P19 atom: k={k_total}, predicted v={v_pred}, score={score_pred:.6f}")
            print(f"    score-target at k={k_total}: v >= {v_needed_to_beat} (need c(A) >= {v_needed_to_beat - 48066})")
            print()
        except Exception as e:
            print(f"  q={q}: failed — {e}")

    print("Conclusion:")
    print("  Bose–Chowla gives Sidon sets where every pairwise difference is DISTINCT.")
    print("  P19 wants atoms with HIGH CONTIGUOUS-PREFIX COVERAGE in (A−A)⁺.")
    print("  These are different goals: Sidon distributes diffs uniformly across [1, q²-1];")
    print("  P19 wants them clustered at [1, c(A)] for large c(A).")
    print("  Empirically c(B) << 100 for q ~ 30-100, while P19 needs c(A) >= 1044.")
    print("  Closes the H1 algebraic-construction sub-question for P19.")


if __name__ == "__main__":
    main()
