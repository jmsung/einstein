"""Warm self-pruning support-shrinking primitives (Goal 2b of p2-record-breakthrough).

Goal 1's cold-seed-on-fixed-window search dead-ended: cold seeds land +0.022 above
arena #1 and a pre-imposed contiguous window is strictly worse than full support
(`docs/wiki/findings/dead-end-p2-cold-seed-fixed-window.md`). The open path the
finding leaves is *warm self-pruning*: start from a near-converged full-support
basin, let the optimizer choose which cells to zero (smallest-|v|, not a contiguous
window), re-optimize allowing peak-locking, and shrink support toward ~74489.

These tests pin the two new primitives that path needs: `vsq_from_f` (warm-start the
square parameterization from an f array) and `prune_smallest` (data-driven,
monotone support shrink), plus the `self_pruning_search` orchestration.
"""

from __future__ import annotations

import numpy as np

from einstein.first_autocorrelation.optimizer import (
    prune_smallest,
    self_pruning_search,
    vsq_from_f,
)


def test_vsq_from_f_roundtrip() -> None:
    f = np.array([0.0, 0.25, 1.0, 4.0, 0.0])
    v = vsq_from_f(f)
    assert np.allclose(v * v, f)
    # exact zeros are preserved (v=0 is the gradient fixed point that locks support)
    assert v[0] == 0.0 and v[4] == 0.0


def test_prune_smallest_keeps_largest_active_cells() -> None:
    v = np.array([0.1, 5.0, 0.2, 4.0, 0.3, 3.0])
    mask = np.ones(6, dtype=bool)
    new_mask = prune_smallest(v, mask, target_support=3)
    assert new_mask.sum() == 3
    # the three largest |v| (indices 1, 3, 5) survive; the three smallest are zeroed
    assert np.array_equal(np.flatnonzero(new_mask), np.array([1, 3, 5]))


def test_prune_smallest_only_considers_active_and_is_monotone() -> None:
    v = np.array([9.0, 0.1, 8.0, 0.2, 7.0])
    mask = np.array([False, True, True, True, True])  # cell 0 already pruned
    new_mask = prune_smallest(v, mask, target_support=2)
    # cell 0 has the largest |v| but is inactive — pruning never resurrects it
    assert not new_mask[0]
    assert new_mask.sum() == 2
    # among active cells the two largest |v| (2 and 4) survive
    assert np.array_equal(np.flatnonzero(new_mask), np.array([2, 4]))


def test_prune_smallest_noop_when_target_ge_active_support() -> None:
    v = np.array([1.0, 2.0, 3.0])
    mask = np.array([True, False, True])  # support 2
    out = prune_smallest(v, mask, target_support=5)
    assert np.array_equal(out, mask)


def test_self_pruning_search_shrinks_support_warm() -> None:
    n = 256
    # a warm full-support bump (stands in for a near-converged basin)
    t = np.linspace(0.0, 1.0, n)
    f_init = np.sin(np.pi * t) + 0.05
    schedule = [200, 160, 120]
    best_f, best_c, trace = self_pruning_search(
        f_init, betas=[1e5, 1e6, 1e7], support_schedule=schedule, max_iter=200
    )
    assert len(trace) == len(schedule)
    assert np.isfinite(best_c)
    # support shrinks: each level's support is at most its target (peak-locking may
    # zero more), strictly below full, and never grows back
    supports = [row["support"] for row in trace]
    assert supports[0] <= 200 < n
    assert all(s <= tgt for s, tgt in zip(supports, schedule))
    assert supports == sorted(supports, reverse=True)
    # best_f is compact (some cells exactly zero) — the whole point
    assert np.count_nonzero(best_f == 0.0) > 0
