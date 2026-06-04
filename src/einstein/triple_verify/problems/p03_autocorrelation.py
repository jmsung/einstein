"""P3 — second autocorrelation. Three-way verify of C = ‖f★f‖₂²/(‖f★f‖₁·‖f★f‖∞).

Higher C is better. Three structurally distinct routes:

  fast  — ``evaluate``  (arena replica: ``np.convolve`` autoconvolution + a
          Python-loop Simpson L2 + discrete L1 + L∞)
  exact — ``scipy.signal.fftconvolve`` autoconvolution + a *vectorised* Simpson
          (different convolution algorithm AND no python loop; agrees ~1e-14)
  cross — float64 autoconvolution but mpmath dps=30 aggregation of all three
          norms (a different *kind*: arbitrary precision pins the summation
          roundoff). ~2s at n=100000.

CAUTION — this score is **resolution-dependent**. The seed is the n=100000
board-consistent basin; do NOT swap in the 1.6M raw solution, which scores
0.9627 only at high resolution and does not transfer to the arena
(docs/wiki/findings/dead-end-p3-resolution-inflation.md). All three checks run
at the seed's own resolution, so they verify *that array's* C2 — they do not by
themselves certify cross-resolution / arena agreement.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np
from scipy.signal import fftconvolve

from einstein.autocorrelation.evaluator import evaluate

from ..core import Tolerance, register


def _f(seed: dict) -> np.ndarray:
    f = np.asarray(seed["values"], dtype=np.float64)
    if f.ndim != 1 or len(f) == 0 or np.any(f < -1e-6):
        raise ValueError("expected a non-empty non-negative 1-D function")
    return np.maximum(f, 0.0)


def _fast(seed: dict) -> float:
    _f(seed)  # enforce the arena contract
    return float(evaluate(seed))


def _exact(seed: dict) -> float:
    """fftconvolve autoconvolution + vectorised Simpson (different code path)."""
    f = _f(seed)
    conv = fftconvolve(f, f, mode="full")
    m = len(conv)
    xp = np.linspace(-0.5, 0.5, m + 2)
    dx = np.diff(xp)
    yp = np.concatenate(([0.0], conv, [0.0]))
    y1, y2 = yp[:-1], yp[1:]
    l2 = float(np.sum(dx / 3 * (y1**2 + y1 * y2 + y2**2)))
    l1 = float(np.sum(np.abs(conv)) / (m + 1))
    linf = float(np.max(np.abs(conv)))
    return l2 / (l1 * linf)


def _cross(seed: dict, dps: int = 30) -> float:
    """float64 autoconvolution, mpmath aggregation of the three norms."""
    f = _f(seed)
    conv = np.convolve(f, f, mode="full")
    m = len(conv)
    mp.mp.dps = dps
    xp = [mp.mpf(-0.5) + mp.mpf(i) / (m + 1) for i in range(m + 2)]
    yp = [mp.mpf(0)] + [mp.mpf(float(c)) for c in conv] + [mp.mpf(0)]
    l2 = mp.mpf(0)
    for i in range(m + 1):
        h = xp[i + 1] - xp[i]
        y1, y2 = yp[i], yp[i + 1]
        l2 += h / 3 * (y1 * y1 + y1 * y2 + y2 * y2)
    l1 = mp.fsum(abs(mp.mpf(float(c))) for c in conv) / (m + 1)
    linf = max(abs(mp.mpf(float(c))) for c in conv)
    return float(l2 / (l1 * linf))


# n=100000 seed: the three routes agree to ~2e-14.
register(
    3,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-10, rel_tol=1e-9),
)
