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


def arena_c(f: np.ndarray) -> float:
    """Arena-exact C(f) from a numpy array (positive-peak autoconvolution ratio)."""
    n = len(f)
    dx = 0.5 / n
    conv = np.convolve(f, f, mode="full") * dx
    return float(abs(conv.max()) / (f.sum() * dx) ** 2)


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
    return smooth_max(conv, beta) / (integral**2)


def exact_score(f: torch.Tensor) -> float:
    """Compute the arena-exact C from a torch tensor."""
    return float(verify_and_compute(f.detach().cpu().numpy().tolist()))


# --------------------------------------------------------------------------- #
# Signed-parameterisation search (Goal 1).
#
# Goal 0 recon (findings/p4-fragmentation-not-fraction-shared-envelope) showed
# the leader's edge over our basin is high-frequency *sign fragmentation* riding
# on a *shared* low-frequency envelope, not a different Fourier basin. These
# helpers support both the cold both-sign Fourier ansatz (the literal Goal 1
# brief) and the higher-EV perturbative-on-envelope mode.
# --------------------------------------------------------------------------- #


def both_sign_fourier_init(
    n: int, n_modes: int, neg_bias: float, rng: np.random.Generator
) -> np.ndarray:
    """Cold both-sign Fourier ansatz on [-1/4, 1/4].

    A smooth signed function built from random-amplitude cosine modes plus a
    positive DC term so ``∫f > 0``. ``neg_bias ∈ [0, 1)`` lowers the DC term to
    push more of f negative (higher ⇒ more negative content). NOT warm-started
    from any existing solution.
    """
    t = np.linspace(0.0, np.pi, n)
    amps = rng.normal(scale=1.0, size=n_modes) / (1.0 + np.arange(1, n_modes + 1))
    f = np.zeros(n, dtype=np.float64)
    for k, a in enumerate(amps, start=1):
        f += a * np.cos(k * t)
    f = f / (np.abs(f).max() + 1e-300)
    # DC offset controls negative fraction: less DC ⇒ more cells go negative.
    dc = (1.0 - neg_bias) * 0.5 + 1e-3
    return f + dc


def lowpass_envelope(v: np.ndarray, keep: int) -> np.ndarray:
    """Low-pass a reference solution to its first ``keep`` rFFT modes.

    Extracts the shared equioscillation envelope (Goal 0 finding) so a fresh
    high-frequency signed perturbation can be optimised on top of it.
    """
    F = np.fft.rfft(v)
    F[keep:] = 0.0
    return np.fft.irfft(F, n=len(v))


def soft_neg_fraction(f: torch.Tensor, sharpness: float) -> torch.Tensor:
    """Differentiable approximation of the fraction of cells with f < 0.

    ``mean(sigmoid(-sharpness · f_normalised))`` → the true negative fraction as
    ``sharpness → ∞``. Normalised by the scale of f so it is scale-robust.
    """
    scale = f.detach().abs().mean() + 1e-30
    return torch.sigmoid(-sharpness * f / scale).mean()


def surrogate_with_neg(
    f: torch.Tensor,
    beta: float,
    *,
    fft: bool,
    neg_target: float = 0.0,
    neg_weight: float = 0.0,
    neg_sharpness: float = 50.0,
) -> torch.Tensor:
    """Smooth-max surrogate plus an optional negative-content nudge.

    Adds ``neg_weight · relu(neg_target − soft_neg_fraction)²`` — a one-sided
    penalty that pushes the negative fraction up toward ``neg_target`` without
    penalising overshoot. Set ``neg_weight=0`` (default) to recover the plain
    surrogate. Anneal ``neg_weight → 0`` across the β-cascade so the final
    stages optimise the true arena objective.
    """
    base = surrogate(f, beta, fft=fft)
    if neg_weight <= 0.0 or neg_target <= 0.0:
        return base
    frac = soft_neg_fraction(f, neg_sharpness)
    deficit = torch.relu(torch.as_tensor(neg_target, dtype=f.dtype) - frac)
    return base + neg_weight * deficit**2


def neg_weight_schedule(stage: int, n_stages: int, base: float) -> float:
    """Linear anneal of the negative-content nudge to 0 over the β-cascade."""
    if base <= 0.0:
        return 0.0
    return base * max(0.0, 1.0 - stage / max(1, n_stages - 1))


def signed_descent(init_v, betas, iters, lr, neg_target, neg_base):
    """Run the smooth-max L-BFGS β-cascade on a signed init.

    The negative-content nudge weight anneals to 0 across the cascade so the
    final stages optimise the true arena objective. Returns ``(best_v, best_C)``
    where best is the lowest arena-exact C seen across all stages.
    """
    f = torch.tensor(np.asarray(init_v, dtype=np.float64).copy(), requires_grad=True)
    best_c = exact_score(f)
    best_v = f.detach().cpu().numpy().copy()
    for stage, beta in enumerate(betas):
        nw = neg_weight_schedule(stage, len(betas), neg_base)
        opt = torch.optim.LBFGS(
            [f],
            lr=lr,
            max_iter=iters,
            tolerance_grad=1e-14,
            tolerance_change=1e-16,
            history_size=100,
            line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_with_neg(f, beta, fft=True, neg_target=neg_target, neg_weight=nw)
            loss.backward()
            return loss

        opt.step(closure)
        c = exact_score(f)
        if c < best_c:
            best_c = c
            best_v = f.detach().cpu().numpy().copy()
    return best_v, best_c


# --------------------------------------------------------------------------- #
# Kolountzakis–Matolcsi LP fixed-point (Goal 5).
#
# The record-producing method in the signed-autoconvolution literature
# (Matolcsi–Vinuesa 2010, arXiv:0907.1379 §4). f★g is bilinear, so with f fixed
# the peak constraint (f★g)[k] ≤ M is LINEAR in g. We maximise Σg subject to it
# (g=f is always feasible), then line-search a move toward g. This descends the
# minimax the smooth-max gradient stalls on when the active set is broad (P4's
# leader has ~92% of conv positions within 1e-6 of the peak). One-sided ≤ M only
# (variant b: negative excursions of f★g are free) — the signed advantage.
# --------------------------------------------------------------------------- #


def _conv_matrix(f: np.ndarray) -> np.ndarray:
    """Dense (2n-1)×n Toeplitz matrix A with (A g)[k] = (f★g)[k] = Σ_i f[i] g[k-i]."""
    n = len(f)
    A = np.zeros((2 * n - 1, n), dtype=np.float64)
    for j in range(n):
        A[j : j + n, j] = f
    return A


def lp_fixed_point(
    f0: np.ndarray, max_iter: int = 40, n_tsteps: int = 24, tol: float = 1e-12
) -> tuple[np.ndarray, float]:
    """Run the LP fixed-point descent on the arena-exact C. Returns (f_best, C).

    At each step: solve the LP for g, then line-search t∈(0,1] on the exact
    arena C of (1-t)f + t·g, keeping the best. Stops when C stops improving.
    """
    from scipy.optimize import linprog

    f = np.asarray(f0, dtype=np.float64).copy()
    if f.sum() < 0:  # C is sign-invariant; work with ∫f > 0
        f = -f
    best_c = arena_c(f)
    for _ in range(max_iter):
        n = len(f)
        A = _conv_matrix(f)  # (2n-1, n)
        m = float(np.convolve(f, f, mode="full").max())  # current positive peak
        # maximise Σg  ⇔  minimise -Σg, s.t. A g ≤ m·1
        res = linprog(
            c=-np.ones(n),
            A_ub=A,
            b_ub=np.full(2 * n - 1, m),
            bounds=[(None, None)] * n,
            method="highs",
        )
        if not res.success:
            break
        g = res.x
        if g.sum() <= 0:
            break
        # line-search the exact C along f → g
        improved = False
        for t in np.linspace(1.0 / n_tsteps, 1.0, n_tsteps):
            h = (1.0 - t) * f + t * g
            if h.sum() <= 0:
                continue
            c = arena_c(h)
            if c < best_c - tol:
                best_c, best_h = c, h
                improved = True
        if not improved:
            break
        f = best_h
    return f, best_c
