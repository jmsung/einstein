"""Numba-accelerated kernels for Difference Bases optimization.

Provides fast incremental ``cnt[]`` updates and ``coverage`` recomputation.
"""

from __future__ import annotations

import numpy as np
from numba import njit


@njit(cache=True)
def build_cnt(B: np.ndarray, U: int) -> np.ndarray:
    """Build difference-multiset count array of length U+1."""
    cnt = np.zeros(U + 1, dtype=np.int32)
    k = B.shape[0]
    for i in range(k):
        bi = B[i]
        for j in range(i):
            d = bi - B[j]
            if 0 < d <= U:
                cnt[d] += 1
    return cnt


@njit(cache=True)
def find_first_zero(cnt: np.ndarray) -> int:
    """Smallest d ≥ 1 with cnt[d] == 0; or len(cnt)-1 if all > 0."""
    for d in range(1, cnt.shape[0]):
        if cnt[d] == 0:
            return d
    return cnt.shape[0] - 1


@njit(cache=True)
def try_swap_v(cnt: np.ndarray, B: np.ndarray, x_idx: int, y: int, U: int) -> int:
    """Return new v after swapping B[x_idx] → y. Restores cnt before returning."""
    k = B.shape[0]
    x = B[x_idx]
    # remove diffs |x - b| for b != x
    for j in range(k):
        if j == x_idx:
            continue
        d = x - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] -= 1
    # add diffs |y - b| for b != x
    for j in range(k):
        if j == x_idx:
            continue
        d = y - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] += 1
    new_v = 0
    for d in range(1, U + 1):
        if cnt[d] == 0:
            new_v = d - 1
            break
    else:
        new_v = U
    # revert
    for j in range(k):
        if j == x_idx:
            continue
        d = y - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] -= 1
        d = x - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] += 1
    return new_v


@njit(cache=True)
def try_add_v(cnt: np.ndarray, B: np.ndarray, y: int, U: int) -> int:
    """Return new v after adding y. Restores cnt."""
    k = B.shape[0]
    for j in range(k):
        d = y - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] += 1
    new_v = 0
    for d in range(1, U + 1):
        if cnt[d] == 0:
            new_v = d - 1
            break
    else:
        new_v = U
    for j in range(k):
        d = y - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] -= 1
    return new_v


@njit(cache=True)
def commit_swap(cnt: np.ndarray, B: np.ndarray, x_idx: int, y: int, U: int) -> int:
    """Commit swap B[x_idx] := y. Returns new v. Resorts B in place."""
    k = B.shape[0]
    x = B[x_idx]
    for j in range(k):
        if j == x_idx:
            continue
        d = x - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] -= 1
        d = y - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] += 1
    B[x_idx] = y
    # re-sort B
    B[:] = np.sort(B)
    return find_first_zero(cnt) - 1 if find_first_zero(cnt) > 0 else 0


@njit(cache=True)
def commit_add(cnt: np.ndarray, B: np.ndarray, y: int, U: int) -> tuple:
    """Commit add y. Returns (new_B, new_v)."""
    k = B.shape[0]
    for j in range(k):
        d = y - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] += 1
    new_B = np.empty(k + 1, dtype=B.dtype)
    new_B[:k] = B
    new_B[k] = y
    new_B = np.sort(new_B)
    fz = find_first_zero(cnt)
    return new_B, fz - 1 if fz > 0 else 0


@njit(cache=True)
def commit_remove(cnt: np.ndarray, B: np.ndarray, x_idx: int, U: int) -> tuple:
    """Commit remove B[x_idx]. Returns (new_B, new_v)."""
    k = B.shape[0]
    x = B[x_idx]
    for j in range(k):
        if j == x_idx:
            continue
        d = x - B[j]
        if d < 0:
            d = -d
        if 0 < d <= U:
            cnt[d] -= 1
    new_B = np.empty(k - 1, dtype=B.dtype)
    pos = 0
    for j in range(k):
        if j != x_idx:
            new_B[pos] = B[j]
            pos += 1
    fz = find_first_zero(cnt)
    return new_B, fz - 1 if fz > 0 else 0


@njit(cache=True, parallel=False)
def best_add(cnt: np.ndarray, B: np.ndarray, U: int, y_max: int) -> tuple:
    """Find best y in [0, y_max] (not in B) maximizing v after adding y.

    Returns (best_y, best_v). best_y == -1 if none.
    """
    Bset = np.zeros(y_max + 2, dtype=np.int8)
    for j in range(B.shape[0]):
        if 0 <= B[j] <= y_max:
            Bset[B[j]] = 1
    best_y = -1
    best_v = -1
    for y in range(y_max + 1):
        if Bset[y]:
            continue
        new_v = try_add_v(cnt, B, y, U)
        if new_v > best_v:
            best_v = new_v
            best_y = y
    return best_y, best_v


@njit(cache=True)
def best_swap_for_target(
    cnt: np.ndarray,
    B: np.ndarray,
    U: int,
    target_d: int,
    cands: np.ndarray,
) -> tuple:
    """For each x in B, for each y in cands, compute new v after swap.

    Returns (best_x_idx, best_y, best_v). Returns (-1,-1,-1) if no improvement.
    """
    cur_v = find_first_zero(cnt) - 1
    best_v = cur_v
    best_x = -1
    best_y = -1
    k = B.shape[0]
    for xi in range(k):
        for ci in range(cands.shape[0]):
            y = cands[ci]
            # quick skip: y in B?
            in_B = False
            for j in range(k):
                if B[j] == y:
                    in_B = True
                    break
            if in_B:
                continue
            new_v = try_swap_v(cnt, B, xi, y, U)
            if new_v > best_v:
                best_v = new_v
                best_x = xi
                best_y = y
    return best_x, best_y, best_v
