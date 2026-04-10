"""Fast local-search optimizer for Difference Bases (Problem 19).

Maintains an explicit difference-multiset count vector so that single-element
swaps can be evaluated in O(k) instead of O(k²). Designed for k ≈ 360 sets.

Core data structure: ``DiffMultiset``
- ``cnt[d]``: number of pairs (b_i, b_j) with b_i - b_j = d, for d ≥ 1
- ``v``: largest run length such that cnt[1..v] > 0
- The smallest broken d is tracked via a heap of "zero diffs ≤ horizon"

A swap mutates ``cnt`` for ~2k entries; ``v`` is recomputed by walking from
the previous v upward (closing breaks) or from the new lowest break downward.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np


class DiffMultiset:
    """Difference multiset for a set B ⊆ [0, max_universe]."""

    def __init__(self, B: Iterable[int], max_universe: int) -> None:
        B_sorted = sorted(set(int(x) for x in B))
        if 0 not in B_sorted:
            B_sorted = [0] + B_sorted
        self.B: list[int] = B_sorted
        self.B_set: set[int] = set(B_sorted)
        self.U: int = int(max_universe)  # cnt has size U+1; index 0 unused
        self.cnt: np.ndarray = np.zeros(self.U + 1, dtype=np.int32)
        Bnp = np.asarray(self.B, dtype=np.int64)
        for i, bi in enumerate(self.B):
            if i == 0:
                continue
            d = Bnp[:i] * 0 + bi - Bnp[:i]  # bi - prior elements (all > 0)
            d = d[d <= self.U]
            np.add.at(self.cnt, d, 1)
        self._recompute_v()

    # ---- coverage tracking ----

    def _recompute_v(self) -> None:
        """Walk cnt[1:] for the first zero entry."""
        nz = np.flatnonzero(self.cnt[1:] == 0)
        self.v = int(nz[0]) if nz.size else self.U

    def coverage(self) -> int:
        return self.v

    # ---- mutation ----

    def add(self, y: int) -> None:
        """Add element y (assumed not in B)."""
        if y in self.B_set:
            raise ValueError(f"{y} already in B")
        Bnp = np.asarray(self.B, dtype=np.int64)
        d = np.abs(Bnp - y)
        d = d[d <= self.U]
        np.add.at(self.cnt, d, 1)
        # insert in sorted order
        import bisect
        bisect.insort(self.B, y)
        self.B_set.add(y)
        self._recompute_v()

    def remove(self, x: int) -> None:
        """Remove element x (assumed in B)."""
        if x not in self.B_set:
            raise ValueError(f"{x} not in B")
        Bnp = np.asarray([b for b in self.B if b != x], dtype=np.int64)
        d = np.abs(Bnp - x)
        d = d[d <= self.U]
        np.add.at(self.cnt, d, -1)
        self.B.remove(x)
        self.B_set.remove(x)
        self._recompute_v()

    def swap(self, x: int, y: int) -> None:
        """Swap x out and y in (atomic)."""
        if x not in self.B_set:
            raise ValueError(f"{x} not in B")
        if y in self.B_set:
            raise ValueError(f"{y} already in B")
        others_np = np.asarray([b for b in self.B if b != x], dtype=np.int64)
        d_rem = np.abs(others_np - x)
        d_rem = d_rem[d_rem <= self.U]
        d_add = np.abs(others_np - y)
        d_add = d_add[d_add <= self.U]
        np.add.at(self.cnt, d_rem, -1)
        np.add.at(self.cnt, d_add, 1)
        self.B.remove(x)
        import bisect
        bisect.insort(self.B, y)
        self.B_set.remove(x)
        self.B_set.add(y)
        self._recompute_v()

    # ---- non-mutating tentative swap ----

    def try_swap(self, x: int, y: int) -> int:
        """Return new v after swapping x→y, without committing.

        Mutates ``cnt`` temporarily then reverts.
        """
        others_np = np.asarray([b for b in self.B if b != x], dtype=np.int64)
        d_rem = np.abs(others_np - x)
        d_rem = d_rem[d_rem <= self.U]
        d_add = np.abs(others_np - y)
        d_add = d_add[d_add <= self.U]
        np.add.at(self.cnt, d_rem, -1)
        np.add.at(self.cnt, d_add, 1)
        nz = np.flatnonzero(self.cnt[1:] == 0)
        new_v = int(nz[0]) if nz.size else self.U
        # revert
        np.add.at(self.cnt, d_add, -1)
        np.add.at(self.cnt, d_rem, 1)
        return new_v

    def try_add(self, y: int) -> int:
        """Return new v after adding y, without committing."""
        Bnp = np.asarray(self.B, dtype=np.int64)
        d = np.abs(Bnp - y)
        d = d[d <= self.U]
        np.add.at(self.cnt, d, 1)
        nz = np.flatnonzero(self.cnt[1:] == 0)
        new_v = int(nz[0]) if nz.size else self.U
        np.add.at(self.cnt, d, -1)
        return new_v
