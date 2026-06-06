"""Tests for the Goal 1 signed-parameterisation search helpers."""

from __future__ import annotations

import numpy as np
import torch

from einstein.third_autocorrelation.evaluator import verify_and_compute
from einstein.third_autocorrelation.optimizer import (
    both_sign_fourier_init,
    lowpass_envelope,
    soft_neg_fraction,
    surrogate,
    surrogate_with_neg,
)


def test_fourier_init_is_signed_with_positive_integral() -> None:
    """Cold ansatz must have both signs and a strictly positive integral."""
    rng = np.random.default_rng(0)
    f = both_sign_fourier_init(2000, n_modes=30, neg_bias=0.5, rng=rng)
    assert len(f) == 2000
    assert (f < 0).any() and (f > 0).any()
    assert f.sum() > 0  # ∫f > 0 so C is well-defined
    # Arena evaluator accepts it (no zero-integral raise).
    assert verify_and_compute(f.tolist()) > 0


def test_fourier_init_neg_bias_monotone() -> None:
    """Higher neg_bias ⇒ more cells driven negative."""
    rng = np.random.default_rng(1)
    low = both_sign_fourier_init(4000, 40, neg_bias=0.2, rng=np.random.default_rng(1))
    high = both_sign_fourier_init(4000, 40, neg_bias=0.8, rng=np.random.default_rng(1))
    assert (high < 0).mean() > (low < 0).mean()
    del rng


def test_lowpass_envelope_keeps_low_modes() -> None:
    """Low-pass kills high-frequency detail but preserves the integral roughly."""
    rng = np.random.default_rng(2)
    v = rng.normal(0.5, 0.3, 1000)
    env = lowpass_envelope(v, keep=10)
    assert len(env) == 1000
    # High-frequency content removed ⇒ far fewer sign runs than the raw signal.
    runs_raw = int((np.diff((v < 0).astype(int)) != 0).sum())
    runs_env = int((np.diff((env < 0).astype(int)) != 0).sum())
    assert runs_env < runs_raw


def test_soft_neg_fraction_tracks_true_fraction() -> None:
    """Soft fraction approximates the hard negative fraction at high sharpness."""
    rng = np.random.default_rng(3)
    f = torch.tensor(rng.normal(0.1, 1.0, 5000), dtype=torch.float64)
    hard = float((f < 0).double().mean())
    soft = float(soft_neg_fraction(f, sharpness=200.0))
    assert abs(soft - hard) < 0.05


def test_neg_nudge_raises_negative_content() -> None:
    """Optimising the nudged surrogate yields more negative cells than the plain one."""
    rng = np.random.default_rng(4)
    n = 1500
    v0 = both_sign_fourier_init(n, 25, neg_bias=0.3, rng=rng)

    def run(neg_weight: float) -> float:
        f = torch.tensor(v0.copy(), dtype=torch.float64, requires_grad=True)
        opt = torch.optim.LBFGS([f], lr=0.5, max_iter=60, line_search_fn="strong_wolfe")

        def closure():
            opt.zero_grad()
            loss = surrogate_with_neg(f, 1e4, fft=True, neg_target=0.45, neg_weight=neg_weight)
            loss.backward()
            return loss

        opt.step(closure)
        return float((f.detach() < 0).double().mean())

    plain = run(0.0)
    nudged = run(5.0)
    assert nudged > plain


def test_surrogate_with_neg_zero_weight_matches_plain() -> None:
    """neg_weight=0 must exactly recover the plain surrogate."""
    rng = np.random.default_rng(5)
    f = torch.tensor(both_sign_fourier_init(800, 20, 0.4, rng), dtype=torch.float64)
    a = surrogate(f, 1e4, fft=True)
    b = surrogate_with_neg(f, 1e4, fft=True, neg_target=0.5, neg_weight=0.0)
    assert torch.allclose(a, b)
