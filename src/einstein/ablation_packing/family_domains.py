"""Non-geometric ablation families — sphere (Tammes) and 1D-sequence (autocorrelation).

These live in their own representations (n×3 unit vectors; a 1D non-negative sequence),
NOT the 2D-points-in-[0,1]^2 mold the runner originally hardcoded. Importing this module
self-registers them via `families.register`, so `get_family("tammes_sphere")` /
`get_family("autocorrelation_seq")` resolve. They provide the cross-DOMAIN endpoints the
v3 transfer design needs: near = Heilbronn (2D) → Tammes (sphere); far = Heilbronn →
autocorrelation (1D sequence) — pre-reg §0b.

All `score` functions return higher-is-better (the runner/DV assume maximize), so the
autocorrelation peak ratio (naturally minimized) is negated.
"""

from __future__ import annotations

import numpy as np

from .evaluator import TripleVerify
from .families import Family, register

# ---------------------------------------------------------------------------
# Tammes — n points on the unit sphere S^2 ⊂ R^3, maximize min pairwise distance
# ---------------------------------------------------------------------------

_TAMMES_DIM = 3


def _unit(vectors: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms < 1e-12] = 1e-12
    return vectors / norms


def tammes_cold_init(n: int, seed: int) -> np.ndarray:
    """Deterministic random start: n Gaussian points projected to the unit sphere."""
    rng = np.random.RandomState(seed)
    return _unit(rng.standard_normal((n, _TAMMES_DIM)))


def tammes_score(vectors: np.ndarray) -> float:
    """Min pairwise Euclidean distance of the normalized vectors (higher = better).

    Returns -inf for a degenerate config (< 2 points), so a bad parse scores at the
    cold baseline rather than raising.
    """
    v = np.asarray(vectors, dtype=np.float64)
    if v.ndim != 2 or v.shape[0] < 2 or v.shape[1] != _TAMMES_DIM:
        return float("-inf")
    u = _unit(v)
    diffs = u[:, None, :] - u[None, :, :]
    dist_sq = np.sum(diffs**2, axis=2)
    iu = np.triu_indices(u.shape[0], k=1)
    return float(np.sqrt(np.min(dist_sq[iu])))


def tammes_triple_verify(vectors: np.ndarray, *, tol: float = 1e-9) -> TripleVerify:
    """Three independent computations of the min pairwise distance (A1)."""
    v = np.asarray(vectors, dtype=np.float64)
    n = v.shape[0] if v.ndim == 2 else 0
    feasible = v.ndim == 2 and n >= 2 and v.shape[1] == _TAMMES_DIM
    feasible = feasible and bool(np.all(np.linalg.norm(v, axis=1) > 1e-12))
    if not feasible:
        return TripleVerify(0.0, 0.0, 0.0, False, False, "degenerate or wrong-shape vectors")
    u = _unit(v)
    iu = np.triu_indices(n, k=1)
    # fast: Gram matrix → cos → distance
    gram = np.clip(u @ u.T, -1.0, 1.0)
    fast = float(np.sqrt(np.min(2.0 * (1.0 - gram[iu]))))
    # exact: direct pairwise difference norms (different code path)
    diffs = u[:, None, :] - u[None, :, :]
    exact = float(np.sqrt(np.min(np.sum(diffs**2, axis=2)[iu])))
    # cross: scipy C-path pairwise distances
    from scipy.spatial.distance import pdist

    cross = float(np.min(pdist(u)))
    passed = abs(fast - exact) < tol and abs(fast - cross) < tol
    return TripleVerify(fast, exact, cross, passed, True, "ok" if passed else "3-way mismatch")


def _tammes_parse(raw: object, n: int) -> np.ndarray | None:
    if not isinstance(raw, list) or len(raw) != n:
        return None
    try:
        arr = np.asarray(raw, dtype=np.float64)
    except (ValueError, TypeError):
        return None
    return arr if arr.shape == (n, _TAMMES_DIM) else None


def _tammes_space(n: int) -> str:
    return (
        f"{n} points on the unit sphere S^2 in R^3 (each point is a 3D vector "
        f"[x, y, z]; vectors are normalized to unit length when scored)"
    )


# ---------------------------------------------------------------------------
# Autocorrelation — a 1D non-negative sequence, minimize the peak autoconvolution
# ratio (negated here so the family maximizes, like all others)
# ---------------------------------------------------------------------------


def _autoconv_peak_ratio(values: np.ndarray) -> float:
    """max(f*f) / (∫f)^2 on [0, 0.5] via the arena's discrete rule. Lower is better."""
    f = np.asarray(values, dtype=np.float64)
    n_points = len(f)
    dx = 0.5 / n_points
    autoconv = np.convolve(f, f, mode="full") * dx
    integral_sq = (np.sum(f) * dx) ** 2
    return float(np.max(autoconv) / integral_sq)


def autocorr_cold_init(n: int, seed: int) -> np.ndarray:
    """Deterministic random start: a length-n strictly-positive sequence."""
    rng = np.random.RandomState(seed)
    return rng.uniform(0.1, 1.0, size=n)


def autocorr_score(values: np.ndarray) -> float:
    """Negated peak autoconvolution ratio (higher = better). -inf if infeasible."""
    f = np.asarray(values, dtype=np.float64)
    if f.ndim != 1 or len(f) < 1 or np.any(f < 0) or np.sum(f) <= 0:
        return float("-inf")
    return -_autoconv_peak_ratio(f)


def autocorr_triple_verify(values: np.ndarray, *, tol: float = 1e-9) -> TripleVerify:
    """Three independent computations of the (negated) peak ratio (A1)."""
    f = np.asarray(values, dtype=np.float64)
    feasible = f.ndim == 1 and len(f) >= 1 and bool(np.all(f >= 0)) and float(np.sum(f)) > 0
    if not feasible:
        return TripleVerify(0.0, 0.0, 0.0, False, False, "negative or empty sequence")
    dx = 0.5 / len(f)
    integral_sq = (float(np.sum(f)) * dx) ** 2
    # fast: numpy full convolution
    fast = -float(np.max(np.convolve(f, f, mode="full") * dx) / integral_sq)
    # exact: explicit autoconvolution sum (different code path)
    m = len(f)
    peak = 0.0
    for k in range(2 * m - 1):
        lo = max(0, k - m + 1)
        hi = min(k, m - 1)
        s = sum(f[i] * f[k - i] for i in range(lo, hi + 1))
        peak = max(peak, s * dx)
    exact = -float(peak / integral_sq)
    # cross: FFT-based convolution (structurally different)
    size = 2 * m - 1
    fft = np.fft.rfft(f, n=size)
    conv = np.fft.irfft(fft * fft, n=size) * dx
    cross = -float(np.max(conv) / integral_sq)
    passed = abs(fast - exact) < tol and abs(fast - cross) < tol
    return TripleVerify(fast, exact, cross, passed, True, "ok" if passed else "3-way mismatch")


def _autocorr_parse(raw: object, n: int) -> np.ndarray | None:
    if not isinstance(raw, list) or len(raw) != n:
        return None
    try:
        arr = np.asarray(raw, dtype=np.float64)
    except (ValueError, TypeError):
        return None
    return arr if arr.shape == (n,) else None


def _autocorr_space(n: int) -> str:
    return (
        f"a length-{n} non-negative sequence f = [f_0, ..., f_{{{n - 1}}}] (a discretized "
        f"function on [0, 0.5]); the objective rewards a LOWER peak autoconvolution ratio"
    )


def _seq_format(init: np.ndarray) -> list:
    return [float(x) for x in init]


def _vec_format(init: np.ndarray) -> list:
    return [[float(x) for x in row] for row in init]


register(
    Family(
        name="tammes_sphere",
        score=tammes_score,
        triple_verify=tammes_triple_verify,
        cold_init=tammes_cold_init,
        answer_key="vectors",
        config_space=_tammes_space,
        parse=_tammes_parse,
        format_init=_vec_format,
    )
)

register(
    Family(
        name="autocorrelation_seq",
        score=autocorr_score,
        triple_verify=autocorr_triple_verify,
        cold_init=autocorr_cold_init,
        answer_key="values",
        config_space=_autocorr_space,
        parse=_autocorr_parse,
        format_init=_seq_format,
    )
)
