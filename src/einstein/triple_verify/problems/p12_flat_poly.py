"""P12 — flat polynomials. Three-way verify of max|p(z)|/√71 over the unit circle.

Score = max_k |p(z_k)| / √71 for z_k the N=1e6 N-th roots of unity, p the ±1
coefficient polynomial (descending degree), lower better. Three routes:

  fast  — ``compute_score``  (np.poly1d Horner eval on the 1M grid — the arena
          evaluator path)
  exact — np.fft.fft of the coefficients at the same 1M roots of unity (a
          different algorithm reaching the identical point set; agrees ~2e-16)
  cross — mpmath dps=40 evaluation of |p| at the float64 argmax grid point (a
          different *kind*: arbitrary precision pins the peak; agrees ~4e-16)

NOTE — local↔arena grid-sampling drift: the score is a *grid maximum*, not the
continuous sup. A denser/shifted grid (4e6 points) gives ~1.28093205285 and the
arena reports 1.2809320527988 for these same coefficients, while our 1M grid
gives 1.2809320520721 — a ~7e-10 drift documented in
docs/wiki/findings/dead-end-p12-grid-sampling-drift.md. The three checks here
verify the evaluator computes *its defined 1M-grid quantity* correctly; the
drift is a separate (real) caveat any submission claim must reconcile.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np

from einstein.flat_poly.evaluator import NORM, compute_score

from ..core import Tolerance, register

_N = 1_000_000


def _coeffs(seed: dict) -> np.ndarray:
    c = np.asarray(seed["coefficients"], dtype=np.float64)
    if len(c) != 70 or not np.all((c == 1) | (c == -1)):
        raise ValueError("expected 70 coefficients in {+1,-1}")
    return c


def _fast(seed: dict) -> float:
    _coeffs(seed)  # enforce the arena contract before scoring
    return float(compute_score(seed["coefficients"]))


def _exact(seed: dict) -> float:
    """FFT of the ascending-power coeffs at the N-th roots of unity — a
    different algorithm reaching the same grid as np.poly1d."""
    desc = _coeffs(seed)
    asc = desc[::-1]  # a[j] = coeff of z^j
    vals = np.fft.fft(asc, n=_N)  # |FFT|_k = |p(z_k)| on the same point set
    return float(np.max(np.abs(vals)) / NORM)


def _cross(seed: dict, dps: int = 40) -> float:
    """mpmath |p| at the float64 argmax grid point (arbitrary precision)."""
    desc = _coeffs(seed)
    z = np.exp(2j * np.pi * np.arange(_N) / _N)
    k = int(np.argmax(np.abs(np.poly1d(desc)(z))))
    mp.mp.dps = dps
    zk = mp.e ** (2j * mp.pi * mp.mpf(k) / _N)
    deg = len(desc) - 1
    pz = mp.fsum(mp.mpf(int(c)) * zk ** (deg - i) for i, c in enumerate(desc))
    return float(abs(pz) / mp.sqrt(71))


# SOTA seed: fast/fft/mpmath agree to <1e-15 on the 1M-grid max (1.28093205207).
register(
    12,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-10, rel_tol=1e-9),
)
