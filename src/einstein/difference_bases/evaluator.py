"""Exact replica of the arena verifier for Problem ID 19 (Difference Bases).

Per the arena problem page:

    score = |B|² / v

where:
    B is the deduplicated, sorted set of non-negative integers (0 mandatory),
    v is the largest integer such that every integer in {1, ..., v} appears
      as a positive difference b_i - b_j (b_i > b_j) for some b_i, b_j in B.

Lower scores are better. Constraint: |B| ≤ 2000.
"""

from __future__ import annotations

from typing import Iterable


def _normalize(elements: Iterable[int]) -> list[int]:
    """Deduplicate, sort, and ensure 0 is included."""
    s = set(int(x) for x in elements)
    s.add(0)
    return sorted(s)


def coverage(elements: Iterable[int]) -> int:
    """Largest v such that {1, ..., v} are all positive differences in B.

    O(k²) construction of difference set, then linear walk.
    """
    B = _normalize(elements)
    diffs: set[int] = set()
    k = len(B)
    for i in range(k):
        bi = B[i]
        for j in range(i):
            diffs.add(bi - B[j])
    v = 0
    while (v + 1) in diffs:
        v += 1
    return v


def score_set(elements: Iterable[int]) -> tuple[float, int, int]:
    """Compute (score, k, v) for a candidate set.

    score = k² / v.
    Returns (score, k, v).
    """
    B = _normalize(elements)
    k = len(B)
    v = coverage(B)
    if v == 0:
        return float("inf"), k, 0
    return k * k / v, k, v


def evaluate(data: dict) -> float:
    """Score a solution dict {"set": [...]}."""
    return score_set(data["set"])[0]


def verify_and_compute(elements: Iterable[int]) -> float:
    """Bit-for-bit arena scorer: returns score float."""
    return score_set(elements)[0]
