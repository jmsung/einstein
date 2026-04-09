"""Shared helpers for the first-autocorrelation optimizer scripts.

Differentiable log-sum-exp surrogate of the autocorrelation objective with
a log-space parameterization of the underlying scalar field for
non-negativity. FFT-based autoconvolution keeps per-step cost ``O(n log n)``.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import torch

from .evaluator import verify_and_compute


def load_warmstart(path: str | Path) -> np.ndarray:
    """Load a JSON solution file and return its values as a float64 array."""
    with open(path) as fh:
        data = json.load(fh)
    return np.array(data["values"], dtype=np.float64)


def upsample(v: np.ndarray, n_target: int) -> np.ndarray:
    """Resample ``v`` to length ``n_target`` via piecewise-constant indexing.

    Block-repeat when ``n_target % n_src == 0`` (exact score preservation for
    the autocorrelation family). Otherwise nearest-neighbour indexing.
    """
    n_src = len(v)
    if n_target == n_src:
        return v.copy()
    if n_target % n_src == 0:
        return np.repeat(v, n_target // n_src)
    out = np.empty(n_target, dtype=np.float64)
    for i in range(n_target):
        out[i] = v[int(i * n_src / n_target)]
    return out


def smooth_max(x: torch.Tensor, beta: float) -> torch.Tensor:
    """log-sum-exp smoothed max. Converges to ``x.max()`` as ``beta`` grows."""
    return (1.0 / beta) * torch.logsumexp(beta * x, dim=-1)


def autoconv_fft(f: torch.Tensor) -> torch.Tensor:
    """Full autoconvolution via real-FFT (length 2n-1)."""
    n = f.shape[-1]
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = torch.fft.rfft(f, n=m_pad)
    return torch.fft.irfft(F * F, n=m_pad)[:m]


def autoconv_direct(f: torch.Tensor) -> torch.Tensor:
    """Full autoconvolution via direct conv1d (length 2n-1). Small n only."""
    n = f.shape[-1]
    return torch.nn.functional.conv1d(
        f.view(1, 1, -1), f.flip(0).view(1, 1, -1), padding=n - 1
    ).view(-1)


def surrogate_v(v: torch.Tensor, beta: float, *, fft: bool = True) -> torch.Tensor:
    """Differentiable surrogate of C(f) with f = exp(v).

    Computes the pointwise ratio first (unit scale ≈ 1.5), then applies LSE.
    This keeps the LSE gap ≈ log(N)/beta on a unit-scale quantity, so the
    surrogate tracks the true max to <1e-9 already at beta=1e10. Scale-invariant.
    """
    f = torch.exp(v)
    n = f.shape[-1]
    dx = 0.5 / n
    conv = autoconv_fft(f) if fft else autoconv_direct(f)  # unscaled f★f
    integral_sum = f.sum()
    ratios = conv / (integral_sum * integral_sum * dx)
    return smooth_max(ratios, beta)


def exact_score_v(v: torch.Tensor) -> float:
    """Compute the arena-exact C from a torch tensor parameter v (f = exp(v))."""
    f_np = np.exp(v.detach().cpu().numpy()).astype(np.float64)
    return float(verify_and_compute(f_np.tolist()))


def exact_score_f(f: np.ndarray) -> float:
    """Compute the arena-exact C from a numpy f array."""
    return float(verify_and_compute(f.astype(np.float64).tolist()))


def to_v(f: np.ndarray, floor: float = 1e-30) -> np.ndarray:
    """Convert an f array (≥ 0) to v = log(max(f, floor)).

    Zeros become ``log(floor)`` (≈ -69 at floor=1e-30). The arena verifier
    allows this as it tolerates any non-negative f.
    """
    return np.log(np.maximum(f, floor))
