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
# Warm self-pruning support-shrinking search (js/feat/p4-warm-pruning-transfer).
#
# P2's record operator (findings/p2-warm-self-pruning-beats-record) ported to
# the signed P4 objective. Two load-bearing differences from the P2 kernel:
#   1. f = mask * w with w UNCONSTRAINED-SIGN (not mask * v**2) — the masked
#      re-opt may re-fragment signs inside the surviving support, which is the
#      move-class argument against the discrete-sign-topology obstruction
#      (findings/p4-basin-is-discrete-sign-topology).
#   2. No leader support target — the P4 leader is full-support, so the
#      schedule floor is a free hyperparameter.
# --------------------------------------------------------------------------- #


def neg_run_count(f: np.ndarray) -> int:
    """Number of contiguous runs of f < 0 — the sign-fragmentation diagnostic.

    The leader's edge over our basin is fragmentation (4705 runs vs our 823) on
    a shared envelope (findings/p4-fragmentation-not-fraction-shared-envelope).
    """
    neg = np.asarray(f) < 0.0
    if not neg.any():
        return 0
    return int(neg[0]) + int(np.count_nonzero(~neg[:-1] & neg[1:]))


def prune_smallest(w: np.ndarray, mask: np.ndarray, target_support: int) -> np.ndarray:
    """Return a new 0/1 mask keeping the ``target_support`` largest-|w| *active* cells.

    Data-driven, monotone support shrink: only cells currently active in ``mask``
    are candidates (pruned cells are never resurrected), and the smallest-|w|
    active cells are zeroed — the optimizer chooses *which* cells die, not a
    pre-imposed window. No-op when ``target_support`` ≥ current support.
    """
    active = np.flatnonzero(mask)
    if target_support >= active.size:
        return mask.copy()
    keep = active[np.argsort(np.abs(w[active]))][-target_support:]
    new_mask = np.zeros_like(mask, dtype=bool)
    new_mask[keep] = True
    return new_mask


def softmax_cell_weights(f: np.ndarray, beta_sel: float = 1e7) -> np.ndarray:
    """Per-cell active-set weights p_{2i} from the smooth-max softmax.

    The LSE multiplier measure p_t = softmax(β·ratios) over conv positions is
    the curvature coupling of the equioscillation (∂²(f★f)(t)/∂w_i² = 2 at
    t = 2i). Cell i's weight is p at its self-convolution position 2i.
    Moderate β_sel spreads p over the near-active set (graded energy); the
    optimization β (1e13) would collapse it to a few spikes.
    """
    n = len(f)
    dx = 0.5 / n
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    conv = np.fft.irfft(F * F, n=m_pad)[:m]
    ratios = conv / (f.sum() * f.sum() * dx)
    z = beta_sel * (ratios - ratios.max())
    p = np.exp(z)
    p /= p.sum()
    return p[2 * np.arange(n)]


def prune_energy(
    w: np.ndarray,
    mask: np.ndarray,
    target_support: int,
    *,
    beta_sel: float = 1e7,
    eps: float = 1e-12,
) -> np.ndarray:
    """Energy-norm prune (Hilbert, council 2026-06-10): smallest e_i = w_i²·p_{2i}.

    Smallest-|w| pruning measures cells in the Euclidean norm, but the basin
    geometry is governed by the Lagrangian curvature: killing a small-|w| cell
    under an active peak (large p_{2i}) pins the equioscillation and U-turns,
    while a moderate-|w| cell with negligible coupling (p_{2i}≈0) is free mass
    whose death re-fragments the sign field. ``eps·w²`` tiebreaks the p≈0 sea.
    """
    active = np.flatnonzero(mask)
    if target_support >= active.size:
        return mask.copy()
    p_cell = softmax_cell_weights(w * mask, beta_sel)
    e = w[active] ** 2 * (p_cell[active] + eps)
    keep = active[np.argsort(e)][-target_support:]
    new_mask = np.zeros_like(mask, dtype=bool)
    new_mask[keep] = True
    return new_mask


def _run_segments(sign: np.ndarray) -> list[tuple[int, int]]:
    """Contiguous same-sign segments of a sign array as (start, end) half-open."""
    edges = np.flatnonzero(sign[:-1] != sign[1:]) + 1
    bounds = np.concatenate(([0], edges, [len(sign)]))
    return [(int(bounds[i]), int(bounds[i + 1])) for i in range(len(bounds) - 1)]


def prune_split(
    w: np.ndarray,
    mask: np.ndarray,
    target_support: int,
    *,
    beta_sel: float = 1e7,
    lo_frac: float = 0.2,
    hi_frac: float = 0.7,
    margin: int = 5,
) -> np.ndarray:
    """Run-splitting prune (Tao + Hilbert, council 2026-06-10).

    Candidates = interior cells (≥``margin`` from run boundaries) of same-sign
    runs longer than the median run length, inside the mid-domain
    [lo_frac·n, hi_frac·n) where the leader's extra negative runs sit. Among
    candidates, prune the smallest energy e_i = w_i²·(p_{2i}+eps) — splitting
    long runs instead of re-carving existing boundaries. Falls back to global
    energy pruning when the candidate pool is too small.
    """
    active = np.flatnonzero(mask)
    if target_support >= active.size:
        return mask.copy()
    k = active.size - target_support

    n = len(w)
    f = w * mask
    sign = np.sign(f)
    segs = _run_segments(sign)
    lengths = np.array([b - a for a, b in segs])
    med = np.median(lengths)
    lo, hi = int(lo_frac * n), int(hi_frac * n)

    cand = np.zeros(n, dtype=bool)
    for a, b in segs:
        if b - a > med and a + margin < b - margin:
            cand[a + margin : b - margin] = True
    cand[:lo] = False
    cand[hi:] = False
    cand &= mask

    pool = np.flatnonzero(cand)
    if pool.size < k:
        return prune_energy(w, mask, target_support, beta_sel=beta_sel)

    p_cell = softmax_cell_weights(f, beta_sel)
    e = w[pool] ** 2 * (p_cell[pool] + 1e-12)
    die = pool[np.argsort(e)][:k]
    new_mask = mask.copy()
    new_mask[die] = False
    return new_mask


PRUNE_RULES = {
    "abs": lambda w, mask, t: prune_smallest(w, mask, t),
    "energy": lambda w, mask, t: prune_energy(w, mask, t),
    "split": lambda w, mask, t: prune_split(w, mask, t),
}


def surrogate_masked(
    w: torch.Tensor, beta: float, *, mask: torch.Tensor, fft: bool = True
) -> torch.Tensor:
    """Differentiable surrogate of C(f) with f = mask · w (signed w).

    Ratio-first LSE (the P2 record kernel's formulation): the pointwise ratio is
    unit-scale ≈ 1.45, so the LSE gap ≈ log(N)/beta tracks the true max to
    <1e-9 already at beta=1e10. Scale-invariant in w.
    """
    f = w * mask
    n = f.shape[-1]
    dx = 0.5 / n
    conv = autoconv_fft(f) if fft else autoconv_direct(f)  # unscaled f★f
    integral_sum = f.sum()
    ratios = conv / (integral_sum * integral_sum * dx)
    return smooth_max(ratios, beta)


def lbfgs_masked(
    w_init: np.ndarray,
    betas: list[float],
    *,
    mask: np.ndarray,
    max_iter: int = 2000,
    lr: float = 1.0,
    history_size: int = 200,
) -> tuple[np.ndarray, float]:
    """Run a masked signed smooth-max L-BFGS β-cascade; return ``(f, exact_C)``.

    CPU float64 sequential L-BFGS (compute-router: GPU sits idle). ``mask``
    keeps the support compact throughout; cells outside it are exactly zero.
    Returns the best arena-exact score across the cascade with ∫f > 0
    normalization (C is invariant under f → −f).
    """
    w = torch.tensor(w_init.copy(), dtype=torch.float64, requires_grad=True)
    mask_t = torch.tensor(mask, dtype=torch.float64)
    mask_np = mask.astype(np.float64)
    best_c = float("inf")
    best_f: np.ndarray | None = None

    for beta in betas:
        opt = torch.optim.LBFGS(
            [w],
            lr=lr,
            max_iter=max_iter,
            tolerance_grad=1e-15,
            tolerance_change=1e-20,
            history_size=history_size,
            line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_masked(w, beta, mask=mask_t)
            loss.backward()
            return loss

        opt.step(closure)
        f_np = w.detach().cpu().numpy() * mask_np
        if f_np.sum() < 0:
            f_np = -f_np
        c = float(verify_and_compute(f_np.tolist()))
        if c < best_c:
            best_c, best_f = c, f_np.copy()

    assert best_f is not None
    return best_f, best_c


def self_pruning_search(
    f_init: np.ndarray,
    betas: list[float],
    support_schedule: list[int],
    *,
    max_iter: int = 2000,
    history_size: int = 200,
    on_level=None,
    prune_rule: str = "abs",
) -> tuple[np.ndarray, float, list[dict]]:
    """Warm self-pruning support-shrinking schedule on the signed P4 objective.

    Start from a near-converged *full-support* warm seed. At each target support
    level: prune active cells per ``prune_rule`` (see ``PRUNE_RULES`` — "abs" =
    smallest-|w|; "energy"/"split" = council 2026-06-10 active-set-aware rules),
    re-optimize the masked signed surrogate (``lbfgs_masked``) warm-started from
    the current ``w``. Tracks the best arena-exact C across levels, plus the
    per-level sign-fragmentation diagnostic (``neg_run_count``).
    """
    if not support_schedule:
        raise ValueError("support_schedule must be non-empty")
    prune = PRUNE_RULES[prune_rule]
    w = np.asarray(f_init, dtype=np.float64).copy()
    mask = w != 0.0
    best_f: np.ndarray | None = None
    best_c = float("inf")
    trace: list[dict] = []

    for target in support_schedule:
        mask = prune(w, mask, target)
        f_opt, c = lbfgs_masked(w, betas, mask=mask, max_iter=max_iter, history_size=history_size)
        w = f_opt  # warm-start the next level from this level's optimum
        row = {
            "target": target,
            "support": int(np.count_nonzero(f_opt)),
            "score": c,
            "neg_runs": neg_run_count(f_opt),
        }
        trace.append(row)
        if on_level is not None:
            on_level(row)
        if c < best_c:
            best_c, best_f = c, f_opt.copy()

    return best_f, best_c, trace


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


def frozen_sign_descent(s, v_init, betas, iters, lr=0.8):
    """Optimise magnitudes with the sign pattern FROZEN: f = s ⊙ v².

    Council consensus (Tao/Hilbert/Hadamard): continuous descent can't cross
    sign-change barriers, so it's trapped in its starting sign topology. By
    fixing the sign field ``s`` (∈ {−1,+1}^n, an IMPOSED fragmentation pattern)
    and optimising only the nonneg magnitudes ``v²``, the optimiser walks into
    the basin of that sign topology — including high-fragmentation basins that
    free descent never selects. Returns ``(f_best, C_best)``.
    """
    s_t = torch.tensor(np.asarray(s, dtype=np.float64))
    v = torch.tensor(np.abs(np.asarray(v_init, dtype=np.float64)) + 1e-6, requires_grad=True)
    best_c, best_f = float("inf"), None
    for beta in betas:
        opt = torch.optim.LBFGS(
            [v],
            lr=lr,
            max_iter=iters,
            tolerance_grad=1e-14,
            tolerance_change=1e-16,
            history_size=100,
            line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            f = s_t * v**2
            n = f.shape[-1]
            dx = 0.5 / n
            conv = autoconv_fft(f) * dx
            loss = smooth_max(conv, beta) / ((f.sum() * dx) ** 2)
            loss.backward()
            return loss

        opt.step(closure)
        f_np = (s_t * v.detach() ** 2).cpu().numpy()
        if f_np.sum() < 0:
            f_np = -f_np
        c = arena_c(f_np)
        if c < best_c:
            best_c, best_f = c, f_np.copy()
    return best_f, best_c


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
