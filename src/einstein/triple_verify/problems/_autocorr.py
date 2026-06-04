"""Shared autocorrelation triple-verify for P2 (first) and P4 (third).

Three distinct code paths for the score ``max(f★f)·dx / (Σf·dx)²``:

  fast  — the arena evaluator (``np.convolve``)
  exact — ``scipy.signal.fftconvolve`` (FFT-based linear convolution)
  cross — power-spectrum route: ``irfft(rfft(f)²)`` (autoconvolution via the
          Fourier domain — a structurally different formulation)

P2 enforces non-negativity and uses ``max``; P4 allows negatives and uses
``abs(max)`` (only the positive peak counts).
"""

from __future__ import annotations

import numpy as np
from scipy.signal import fftconvolve


def _f(seed: dict) -> np.ndarray:
    return np.asarray(seed["values"], dtype=np.float64)


def _peak(conv: np.ndarray, *, take_abs: bool) -> float:
    m = np.max(conv)
    return float(abs(m) if take_abs else m)


def make_fast(arena_evaluate):
    def fast(seed: dict) -> float:
        return float(arena_evaluate(seed))

    return fast


def make_exact(*, require_nonneg: bool, take_abs: bool):
    def exact(seed: dict) -> float:
        f = _f(seed)
        if require_nonneg and np.any(f < 0):
            raise ValueError("negative values not allowed")
        s = float(np.sum(f))
        if s == 0:
            raise ValueError("zero integral")
        n = len(f)
        dx = 0.5 / n
        conv = fftconvolve(f, f, mode="full") * dx
        return _peak(conv, take_abs=take_abs) / (s * dx) ** 2

    return exact


def make_cross(*, take_abs: bool):
    def cross(seed: dict) -> float:
        f = _f(seed)
        s = float(np.sum(f))
        if s == 0:
            raise ValueError("zero integral")
        n = len(f)
        dx = 0.5 / n
        m = 2 * n - 1
        F = np.fft.rfft(f, n=2 * n)
        conv = np.fft.irfft(F * F, n=2 * n)[:m] * dx
        return _peak(conv, take_abs=take_abs) / (s * dx) ** 2

    return cross
