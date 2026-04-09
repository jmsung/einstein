"""Shared helpers for the third-autocorrelation optimizer scripts.

Generic differentiable surrogate for the arena verifier in
``einstein.third_autocorrelation.evaluator``. Both the direct-conv and the
FFT-conv entry points consume the same building blocks, so they live here
rather than being duplicated across scripts.
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
    """Resample ``v`` to length ``n_target`` via piecewise-constant indexing."""
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


def autoconv_direct(f: torch.Tensor) -> torch.Tensor:
    """Full autoconvolution via direct conv1d (length 2n-1)."""
    n = f.shape[-1]
    return torch.nn.functional.conv1d(
        f.view(1, 1, -1), f.flip(0).view(1, 1, -1), padding=n - 1
    ).view(-1)


def autoconv_fft(f: torch.Tensor) -> torch.Tensor:
    """Full autoconvolution via real-FFT (length 2n-1)."""
    n = f.shape[-1]
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = torch.fft.rfft(f, n=m_pad)
    return torch.fft.irfft(F * F, n=m_pad)[:m]


def surrogate(f: torch.Tensor, beta: float, *, fft: bool) -> torch.Tensor:
    """Differentiable surrogate of the arena C(f).

    ``smooth_max(f★f · dx) / (∑ f · dx)²``. As ``beta`` grows the surrogate
    converges to the exact arena score.
    """
    n = f.shape[-1]
    dx = 0.5 / n
    conv = (autoconv_fft(f) if fft else autoconv_direct(f)) * dx
    integral = f.sum() * dx
    return smooth_max(conv, beta) / (integral ** 2)


def exact_score(f: torch.Tensor) -> float:
    """Compute the arena-exact C from a torch tensor."""
    return float(verify_and_compute(f.detach().cpu().numpy().tolist()))
