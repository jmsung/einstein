"""Tests for the warm self-pruning kernel ported from P2 (signed variant).

P4's f may be negative, so the kernel parameterizes f = mask * w with w
unconstrained-sign (NOT P2's mask * v**2). Pruning zeroes the smallest-|w|
active cells; the masked re-opt may re-fragment signs inside the surviving
support.
"""

from __future__ import annotations

import numpy as np

from einstein.third_autocorrelation.evaluator import verify_and_compute
from einstein.third_autocorrelation.optimizer import (
    lbfgs_masked,
    neg_run_count,
    prune_energy,
    prune_smallest,
    prune_split,
    self_pruning_search,
    softmax_cell_weights,
    surrogate_masked,
)


def _warm_seed(n: int, rng: np.random.Generator) -> np.ndarray:
    """Small signed near-smooth seed with positive integral (CI stand-in)."""
    t = np.linspace(0.0, np.pi, n)
    f = 1.0 + 0.5 * np.cos(2 * t) - 0.3 * np.cos(5 * t) + 0.01 * rng.normal(size=n)
    assert f.sum() > 0
    return f


class TestNegRunCount:
    def test_hand_case(self):
        assert neg_run_count(np.array([1.0, -1.0, -1.0, 2.0, -3.0, 4.0])) == 2

    def test_all_positive(self):
        assert neg_run_count(np.ones(5)) == 0

    def test_single_run_at_edge(self):
        assert neg_run_count(np.array([-1.0, -2.0, 3.0])) == 1


class TestPruneSmallest:
    def test_keeps_largest_abs_active(self):
        w = np.array([5.0, -0.1, 3.0, 0.2, -4.0])
        mask = np.ones(5, dtype=bool)
        new = prune_smallest(w, mask, 3)
        assert new.tolist() == [True, False, True, False, True]

    def test_noop_when_target_geq_support(self):
        w = np.array([1.0, -2.0, 3.0])
        mask = np.array([True, False, True])
        new = prune_smallest(w, mask, 2)
        assert new.tolist() == mask.tolist()

    def test_never_resurrects_pruned_cells(self):
        w = np.array([0.1, 100.0, 0.2, 0.3])
        mask = np.array([True, False, True, True])  # cell 1 already pruned
        new = prune_smallest(w, mask, 2)
        assert not new[1]
        assert new.sum() == 2


class TestCouncilPruneRules:
    def test_softmax_weights_sum_and_peak(self):
        rng = np.random.default_rng(7)
        f = _warm_seed(128, rng)
        p = softmax_cell_weights(f, beta_sel=1e4)
        assert p.shape == (128,)
        assert np.all(p >= 0)
        assert p.sum() <= 1.0 + 1e-12  # cell positions are a subset of conv positions

    def test_energy_prune_diverges_from_abs_when_weights_spread(self):
        # With a spread softmax (the equioscillation regime the rule targets),
        # curvature coupling must reorder the selection away from smallest-|w|.
        # (At collapsed softmax — smooth f, high beta_sel — p≈0 everywhere and
        # the rule degrades to smallest-|w| by the eps tiebreak, by design.)
        rng = np.random.default_rng(8)
        f = _warm_seed(128, rng)
        mask = np.ones(128, dtype=bool)
        new = prune_energy(f, mask, 100, beta_sel=50.0)
        assert new.sum() == 100
        assert not np.array_equal(new, prune_smallest(f, mask, 100))

    def test_energy_prune_noop_and_no_resurrection(self):
        rng = np.random.default_rng(9)
        f = _warm_seed(64, rng)
        mask = np.ones(64, dtype=bool)
        mask[:5] = False
        new = prune_energy(f, mask, 64)
        assert new.tolist() == mask.tolist()
        new2 = prune_energy(f, mask, 50)
        assert not new2[:5].any()
        assert new2.sum() == 50

    def test_split_prunes_only_long_run_interiors_middomain(self):
        n = 200
        w = np.ones(n)
        w[100:104] = -1.0  # short run (≤ median) — not a candidate
        mask = np.ones(n, dtype=bool)
        new = prune_split(w, mask, n - 10, margin=5, lo_frac=0.2, hi_frac=0.7)
        died = np.flatnonzero(mask & ~new)
        assert len(died) == 10
        assert np.all(died >= 40) and np.all(died < 140)  # mid-domain only
        assert not set(died) & set(range(100, 104))  # short run untouched

    def test_split_falls_back_when_pool_small(self):
        n = 64
        rng = np.random.default_rng(10)
        w = _warm_seed(n, rng)
        mask = np.ones(n, dtype=bool)
        # mid-domain pool of a 64-cell array with margin 5 is tiny; ask for a
        # huge cut so the pool can't cover it → must fall back, still valid.
        new = prune_split(w, mask, 20, margin=5)
        assert new.sum() == 20


class TestSurrogateMasked:
    def test_high_beta_parity_with_arena(self):
        import torch

        rng = np.random.default_rng(0)
        f = _warm_seed(64, rng)
        mask = np.ones(64, dtype=bool)
        s = surrogate_masked(
            torch.tensor(f, dtype=torch.float64),
            1e9,
            mask=torch.tensor(mask, dtype=torch.float64),
        )
        exact = verify_and_compute(f.tolist())
        assert abs(float(s) - exact) < 1e-6

    def test_masked_cells_do_not_contribute(self):
        import torch

        rng = np.random.default_rng(1)
        f = _warm_seed(64, rng)
        mask = np.ones(64, dtype=bool)
        mask[10:20] = False
        f_masked = f.copy()
        f_masked[10:20] = 0.0
        s = surrogate_masked(
            torch.tensor(f, dtype=torch.float64),
            1e9,
            mask=torch.tensor(mask, dtype=torch.float64),
        )
        exact = verify_and_compute(f_masked.tolist())
        assert abs(float(s) - exact) < 1e-6


class TestLbfgsMasked:
    def test_zero_outside_mask_and_improves(self):
        rng = np.random.default_rng(2)
        f = _warm_seed(96, rng)
        mask = np.ones(96, dtype=bool)
        mask[:4] = False
        c0 = verify_and_compute((f * mask).tolist())
        f_opt, c = lbfgs_masked(f, [1e4, 1e6], mask=mask, max_iter=200)
        assert np.all(f_opt[~mask] == 0.0)
        assert c <= c0 + 1e-12
        assert abs(verify_and_compute(f_opt.tolist()) - c) < 1e-12

    def test_positive_integral_convention(self):
        rng = np.random.default_rng(3)
        f = _warm_seed(64, rng)
        f_opt, _ = lbfgs_masked(f, [1e4], mask=np.ones(64, dtype=bool), max_iter=50)
        assert f_opt.sum() > 0


class TestSelfPruningSearch:
    def test_support_shrinks_per_schedule(self):
        rng = np.random.default_rng(4)
        f = _warm_seed(128, rng)
        schedule = [120, 100, 80]
        best_f, best_c, trace = self_pruning_search(f, [1e4, 1e6], schedule, max_iter=150)
        assert len(trace) == 3
        for row, target in zip(trace, schedule):
            assert row["target"] == target
            assert row["support"] <= target
            assert "neg_runs" in row
        supports = [row["support"] for row in trace]
        assert supports == sorted(supports, reverse=True)
        assert np.isfinite(best_c)
        assert best_c == min(row["score"] for row in trace)
        assert np.count_nonzero(best_f) <= max(supports)
        # best_f scores what the kernel claims (independent arena path)
        assert abs(verify_and_compute(best_f.tolist()) - best_c) < 1e-12

    def test_signs_free_within_mask(self):
        # The signed param must not constrain surviving cells to the seed's signs:
        # an all-positive seed may legally end with negative cells after re-opt.
        # (We assert only legality of output, not that flips occur.)
        rng = np.random.default_rng(5)
        f = np.abs(_warm_seed(96, rng))
        best_f, best_c, _ = self_pruning_search(f, [1e4], [90], max_iter=100)
        assert best_f.sum() > 0
        assert np.isfinite(best_c)
