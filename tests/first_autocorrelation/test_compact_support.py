"""Compact-support-targeting search primitives (Goal 1 of p2-record-breakthrough).

The shared `optimizer.exp(v)` parameterization is full-support by construction
(exp is never zero), so it can never reach the leaders' compact-support basin.
These tests pin the v**2 + mask primitives that *can*: f = mask * v**2 admits
exact zeros (v=0 is a gradient fixed point), and a contiguous window mask makes
the support compact by construction.
"""

from __future__ import annotations

import numpy as np
import torch

from einstein.first_autocorrelation.evaluator import verify_and_compute
from einstein.first_autocorrelation.optimizer import (
    lbfgs_vsq,
    score_vsq_masked,
    surrogate_vsq,
    window_mask,
)


def test_window_mask_is_contiguous_and_correct_width() -> None:
    m = window_mask(100, 60)
    assert m.sum() == 60
    on = np.flatnonzero(m)
    # contiguous block
    assert np.array_equal(on, np.arange(on[0], on[0] + 60))
    # centered (±1 for parity)
    assert abs(on[0] - (100 - 60) // 2) <= 1


def test_masked_surrogate_keeps_support_compact() -> None:
    n, w = 200, 120
    m = window_mask(n, w)
    mask_t = torch.tensor(m, dtype=torch.float64)
    v = torch.ones(n, dtype=torch.float64, requires_grad=True)
    loss = surrogate_vsq(v, beta=1e6, mask=mask_t)
    loss.backward()
    # f = mask * v**2 is zero outside the window …
    f = (mask_t * v * v).detach().numpy()
    assert np.all(f[~m] == 0.0)
    # … and the gradient on masked-out cells is exactly zero, so L-BFGS can
    # never resurrect them — compact support is invariant under optimization.
    assert np.all(v.grad.detach().numpy()[~m] == 0.0)


def test_score_vsq_masked_matches_arena_evaluator() -> None:
    n, w = 300, 200
    m = window_mask(n, w)
    rng = np.random.default_rng(0)
    v = rng.uniform(0.5, 1.5, n)
    f = m * v * v
    assert score_vsq_masked(v, m) == verify_and_compute(f.tolist())


def test_lbfgs_vsq_preserves_mask_and_does_not_worsen() -> None:
    n, w = 256, 160
    m = window_mask(n, w)
    rng = np.random.default_rng(1)
    # cold seed: smooth positive bump on the window (NOT from our basin)
    v0 = np.zeros(n)
    idx = np.flatnonzero(m)
    bump = np.sin(np.linspace(0, np.pi, w)) + 0.1
    v0[idx] = np.sqrt(bump)
    c0 = score_vsq_masked(v0, m)
    f_opt, c_opt = lbfgs_vsq(v0, betas=[1e5, 1e6, 1e7], mask=m, max_iter=200)
    assert np.all(f_opt[~m] == 0.0)  # support stayed compact
    assert np.isfinite(c_opt)
    assert c_opt <= c0 + 1e-9  # optimization never worsens the score
