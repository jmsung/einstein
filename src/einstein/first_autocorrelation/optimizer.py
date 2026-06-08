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


def surrogate_vsq(
    v: torch.Tensor, beta: float, *, mask: torch.Tensor | None = None, fft: bool = True
) -> torch.Tensor:
    """Differentiable surrogate of C(f) with f = v**2 (square parameterization).

    Unlike ``exp(v)`` (always positive ⇒ full support), ``v**2`` admits exact
    zeros at ``v=0`` where the gradient also vanishes — so a cell can lock at
    exactly zero. This is the parameterization that can reach a *compact-support*
    basin. With ``mask`` (a 0/1 tensor), ``f = mask * v**2`` is zero outside the
    mask and the gradient there is identically zero, so the support stays compact
    under optimization. Scale-invariant.
    """
    f = v * v
    if mask is not None:
        f = f * mask
    n = f.shape[-1]
    dx = 0.5 / n
    conv = autoconv_fft(f) if fft else autoconv_direct(f)
    integral_sum = f.sum()
    ratios = conv / (integral_sum * integral_sum * dx)
    return smooth_max(ratios, beta)


def window_mask(n: int, width: int) -> np.ndarray:
    """A contiguous, centred 0/1 support window of ``width`` cells in ``n``.

    Support *position* is irrelevant to C (shifting f shifts the autoconvolution
    but preserves its max, ∫f and dx), so a centred window covers every distinct
    compact-support family — the schedule only needs to vary ``width``.
    """
    if not 0 < width <= n:
        raise ValueError(f"width {width} out of range (0, {n}]")
    m = np.zeros(n, dtype=bool)
    lo = (n - width) // 2
    m[lo : lo + width] = True
    return m


def score_vsq_masked(v: np.ndarray, mask: np.ndarray) -> float:
    """Arena-exact C of ``f = mask * v**2`` (independent code path from the surrogate)."""
    f = mask.astype(np.float64) * (v.astype(np.float64) ** 2)
    return float(verify_and_compute(f.tolist()))


def lbfgs_vsq(
    v_init: np.ndarray,
    betas: list[float],
    *,
    mask: np.ndarray | None = None,
    max_iter: int = 2000,
    lr: float = 1.0,
    history_size: int = 200,
) -> tuple[np.ndarray, float]:
    """Run a v**2 smooth-max L-BFGS β-cascade; return ``(f, exact_C)``.

    Optimizes on CPU float64 (sequential L-BFGS — GPU sits idle; see
    compute-router). ``mask`` keeps the support compact throughout. Returns the
    best arena-exact score across the cascade, not the surrogate value.
    """
    v = torch.tensor(v_init.copy(), dtype=torch.float64, requires_grad=True)
    mask_t = None if mask is None else torch.tensor(mask, dtype=torch.float64)
    mask_np = None if mask is None else mask.astype(np.float64)
    best_c = float("inf")
    best_f = None

    for beta in betas:
        opt = torch.optim.LBFGS(
            [v],
            lr=lr,
            max_iter=max_iter,
            tolerance_grad=1e-15,
            tolerance_change=1e-20,
            history_size=history_size,
            line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_vsq(v, beta, mask=mask_t)
            loss.backward()
            return loss

        opt.step(closure)
        f_np = (v.detach().cpu().numpy() ** 2).astype(np.float64)
        if mask_np is not None:
            f_np = f_np * mask_np
        c = float(verify_and_compute(f_np.tolist()))
        if c < best_c:
            best_c = c
            best_f = f_np.copy()

    return best_f, best_c


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
