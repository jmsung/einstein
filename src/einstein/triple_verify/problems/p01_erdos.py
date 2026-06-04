"""P1 — Erdős minimum overlap. Three-way verify of C = max(corr(h, 1-h))·2/n.

Three structurally distinct code paths for the same score (h normalised so
Σh = n/2, lower C better):

  fast  — ``einstein.erdos.fast.fast_evaluate``  (scipy ``fftconvolve``, the
          optimisation-loop scorer)
  exact — ``einstein.erdos.evaluator.compute_upper_bound``  (``np.correlate``
          O(n²) direct sum — the audited arena replica, a different code path)
  cross — mpmath arbitrary-precision direct correlation (a different *kind* of
          evidence: catches float64 roundoff the two numpy paths share). At
          n=600 the three agree to ~5e-17; cross runs in ~0.3s at dps=40.

There is no tight closed-form analytical value for the minimum-overlap constant
(known only to lie in ≈[0.379, 0.381]), so the third check is high-precision
arithmetic rather than an analytical bound — exactly the fallback the
triple-verify rule prescribes when no analytical bound exists.
"""

from __future__ import annotations

import mpmath as mp

from einstein.erdos.evaluator import compute_upper_bound
from einstein.erdos.fast import fast_evaluate

from ..core import Tolerance, register


def _fast(seed: dict) -> float:
    return float(fast_evaluate(seed["values"]))


def _exact(seed: dict) -> float:
    return float(compute_upper_bound(seed["values"]))


def _cross(seed: dict, dps: int = 40) -> float:
    """Direct correlation max at arbitrary precision (np.correlate semantics)."""
    mp.mp.dps = dps
    h = [mp.mpf(repr(x)) for x in seed["values"]]
    n = len(h)
    target = mp.mpf(n) / 2
    s = mp.fsum(h)
    if s == 0:
        raise ValueError("zero total sum — cannot normalise")
    if s != target:
        factor = target / s
        h = [x * factor for x in h]
    g = [1 - x for x in h]
    best = mp.mpf("-inf")
    for lag in range(-(n - 1), n):
        acc = mp.fsum(h[m] * g[m - lag] for m in range(n) if 0 <= m - lag < n)
        if acc > best:
            best = acc
    return float(best / n * 2)


# n=600 seed: the three routes agree to ~5e-17 (see
# tests/erdos/test_triple_verify.py). Tight band matches the autocorr family.
register(
    1,
    fast=_fast,
    exact=_exact,
    cross=_cross,
    tolerance=Tolerance(abs_tol=1e-12, rel_tol=1e-9),
)
