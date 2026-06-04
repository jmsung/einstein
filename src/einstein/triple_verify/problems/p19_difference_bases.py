"""P19 — difference bases. Score = |B|² / v (minimize), exact integer arithmetic.

Three structurally distinct algorithms for the coverage v (= largest t with
{1..t} all representable as a positive difference in B):

  fast  — arena score_set (Python-set difference set, O(k²))
  exact — boolean-array difference set, then linear walk (different data path)
  cross — forward membership: for each t, test ∃ b∈B with b+t∈B (no diff set)

The score is an exact rational k²/v computed as float — all three are
bit-identical, so the tolerance is essentially exact.
"""

from __future__ import annotations

from einstein.difference_bases.evaluator import score_set as _arena_score_set

from ..core import Tolerance, register


def _normalize(elements) -> list[int]:
    return sorted(set(int(x) for x in elements) | {0})


def _fast(seed: dict) -> float:
    return float(_arena_score_set(seed["set"])[0])


def _exact(seed: dict) -> float:
    B = _normalize(seed["set"])
    k = len(B)
    maxd = B[-1] if B else 0
    present = bytearray(maxd + 1)
    for i in range(k):
        bi = B[i]
        for j in range(i):
            present[bi - B[j]] = 1
    v = 0
    while v + 1 <= maxd and present[v + 1]:
        v += 1
    return float("inf") if v == 0 else k * k / v


def _cross(seed: dict) -> float:
    B = _normalize(seed["set"])
    k = len(B)
    Bset = set(B)
    v = 0
    while True:
        t = v + 1
        if any((b + t) in Bset for b in B):
            v = t
        else:
            break
    return float("inf") if v == 0 else k * k / v


register(
    19,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=0.0, rel_tol=1e-12),
)
