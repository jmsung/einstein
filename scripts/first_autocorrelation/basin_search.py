"""Basin search: many diverse seeds at n=90k to find deeper basins.

The v3 breakthrough (our previous rank #1) found one basin at 1.502861628.
OrganonAgent found a slightly deeper basin at 1.502861427. There may be
even deeper basins accessible with different initialization and optimization.

Strategy: 30k→90k block-repeat, then v^2 L-BFGS with many diverse seeds,
varied noise scales, beta schedules, and history sizes.

Also try: direct scipy L-BFGS-B on the exact max objective with subgradient.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import torch
from scipy.optimize import minimize as scipy_minimize

from einstein.first_autocorrelation.evaluator import verify_and_compute

RESULTS = Path("results/problem-2-first-autocorrelation")
RESULTS.mkdir(parents=True, exist_ok=True)


def exact_score(f: np.ndarray) -> float:
    return float(verify_and_compute(f.astype(np.float64).tolist()))


def autoconv_fft_torch(f: torch.Tensor) -> torch.Tensor:
    n = f.shape[-1]
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = torch.fft.rfft(f, n=m_pad)
    return torch.fft.irfft(F * F, n=m_pad)[:m]


def smooth_max(x: torch.Tensor, beta: float) -> torch.Tensor:
    return (1.0 / beta) * torch.logsumexp(beta * x, dim=-1)


def surrogate_vsq(v: torch.Tensor, beta: float) -> torch.Tensor:
    f = v * v
    n = f.shape[-1]
    dx = 0.5 / n
    conv = autoconv_fft_torch(f)
    s = f.sum()
    ratios = conv / (s * s * dx)
    return smooth_max(ratios, beta)


def lbfgs_vsq(v_init: np.ndarray, betas: list[float],
              max_iter: int = 2000, lr: float = 1.0,
              history_size: int = 200) -> tuple[np.ndarray, float]:
    """Run v^2 L-BFGS cascade, return (f, score)."""
    v = torch.tensor(v_init.copy(), dtype=torch.float64, requires_grad=True)
    best_c = float("inf")
    best_f = None

    for beta in betas:
        opt = torch.optim.LBFGS(
            [v], lr=lr, max_iter=max_iter,
            tolerance_grad=1e-15, tolerance_change=1e-20,
            history_size=history_size, line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_vsq(v, beta)
            loss.backward()
            return loss

        opt.step(closure)
        f_np = (v.detach().cpu().numpy() ** 2).astype(np.float64)
        c = exact_score(f_np)
        if c < best_c:
            best_c = c
            best_f = f_np.copy()

    return best_f, best_c


def compute_subgradient(f: np.ndarray) -> tuple[np.ndarray, float]:
    """Compute subgradient of C at the argmax of autoconvolution."""
    n = len(f)
    dx = 0.5 / n
    s = f.sum()
    integral_sq = (s * dx) ** 2

    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    conv = np.fft.irfft(F * F, n=m_pad)[:m] * dx

    C = np.max(conv) / integral_sq
    t_star = np.argmax(conv)

    # Gradient: d/df_i [conv(t*)] / integral_sq - conv(t*) * d/df_i [integral_sq] / integral_sq^2
    # = 2 * f[t*-i] * dx / integral_sq - 2 * C * dx / (s * dx)
    grad = np.zeros(n, dtype=np.float64)
    lo = max(0, t_star - (n - 1))
    hi = min(n - 1, t_star)
    for i in range(lo, hi + 1):
        j = t_star - i
        if 0 <= j < n:
            grad[i] = 2.0 * f[j] * dx / integral_sq
    grad -= 2.0 * C * dx / (s * dx)

    return grad, C


def scipy_lbfgsb(f_init: np.ndarray, maxiter: int = 5000) -> tuple[np.ndarray, float]:
    """Direct scipy L-BFGS-B on the max objective with subgradient."""
    n = len(f_init)
    best_c = exact_score(f_init)
    best_f = f_init.copy()

    def objective_and_grad(f_flat):
        f = np.maximum(f_flat, 0.0)
        grad, C = compute_subgradient(f)
        return C, grad

    bounds = [(0.0, None)] * n
    result = scipy_minimize(
        objective_and_grad, f_init.copy(), method='L-BFGS-B',
        jac=True, bounds=bounds,
        options={'maxiter': maxiter, 'maxfun': maxiter * 2, 'ftol': 1e-20,
                 'gtol': 1e-15, 'maxcor': 100},
    )

    f_opt = np.maximum(result.x, 0.0)
    c_opt = exact_score(f_opt)
    if c_opt < best_c:
        return f_opt, c_opt
    return best_f, best_c


def gradient_polish(f_init: np.ndarray, max_iters: int = 10000,
                    lr0: float = 1e-6) -> tuple[np.ndarray, float]:
    """Extended gradient descent with adaptive step size."""
    f = f_init.astype(np.float64).copy()
    n = len(f)
    best_c = exact_score(f)
    best_f = f.copy()
    lr = lr0
    no_improve = 0
    total_improved = 0

    for it in range(max_iters):
        grad, C_approx = compute_subgradient(f)

        # Direction
        active = (f > 1e-30) | (grad < 0)
        d = np.where(active, -grad, 0.0)
        gnorm = np.linalg.norm(d)
        if gnorm < 1e-30:
            break
        d = d / gnorm

        # Armijo line search
        accepted = False
        for _ in range(50):
            f_try = np.maximum(f + lr * d, 0.0)
            if f_try.sum() <= 0:
                lr *= 0.5
                continue
            c_try = exact_score(f_try)
            if c_try < best_c:
                f = f_try
                delta = best_c - c_try
                best_c = c_try
                best_f = f.copy()
                lr = min(lr * 1.3, lr0 * 100)
                accepted = True
                no_improve = 0
                total_improved += 1
                break
            lr *= 0.5

        if not accepted:
            no_improve += 1
            lr = lr0
            if no_improve >= 20:
                break

    return best_f, best_c


def save_sol(f: np.ndarray, c: float, tag: str):
    path = RESULTS / f"basin-{tag}-{c:.10f}.json"
    with open(path, "w") as fh:
        json.dump({"values": f.tolist(), "score": c, "n": len(f), "tag": tag}, fh)
    return path


def main():
    t_start = time.time()

    # Load warmstarts
    with open(RESULTS / "sol-01-OrganonAgent-1798.json") as f:
        org = json.load(f)
    f_org = np.array(org["values"], dtype=np.float64)
    c_org = exact_score(f_org)

    sol30k = RESULTS / "sol-03-Together-AI-44.json"
    with open(sol30k) as f:
        d30k = json.load(f)
    f_30k = np.array(d30k["values"], dtype=np.float64)

    target = c_org - 1e-7
    print(f"OrganonAgent #1: {c_org:.18f}")
    print(f"Target: < {target:.18f}")
    print(f"30k base: C={exact_score(f_30k):.18f}")

    global_best_c = c_org
    global_best_f = f_org.copy()

    def update(f, c, tag):
        nonlocal global_best_c, global_best_f
        if c < global_best_c:
            delta = global_best_c - c
            global_best_c = c
            global_best_f = f.copy()
            save_sol(f, c, tag)
            print(f"  >>> GLOBAL BEST: {c:.18f} (delta={delta:.3e}) <<<")
            return True
        return False

    # ── Strategy A: Massive seed search at n=90k ─────────────────────────
    print(f"\n{'='*60}")
    print("Strategy A: Diverse seed search at n=90k from 30k base")
    print(f"{'='*60}")

    f_90k = np.repeat(f_30k, 3)
    c_90k = exact_score(f_90k)
    print(f"Block-repeat 30k→90k: C={c_90k:.18f}")

    # Define diverse configurations
    configs = [
        # (noise_scale, betas, history_size, max_iter, label)
        (0.0,   [1e6]*3 + [1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13],      300, 3000, "ultra-low-beta"),
        (1e-5,  [1e6]*3 + [1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13],      300, 3000, "tiny-noise"),
        (3e-5,  [1e6]*3 + [1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13],      300, 3000, "small-noise"),
        (1e-4,  [1e6]*3 + [1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13],      300, 3000, "med-noise"),
        (3e-4,  [5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 1e9, 1e10, 1e11, 1e12], 250, 2500, "large-noise"),
        (1e-3,  [5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 1e9, 1e10, 1e11, 1e12], 250, 2500, "xlarge-noise"),
        (0.0,   [1e5, 5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 1e9, 1e10, 1e11], 200, 2000, "very-low-beta"),
        (5e-5,  [1e5, 5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 1e9, 1e10, 1e11], 300, 3000, "very-low-beta-noisy"),
        (0.0,   [1e6]*5 + [1e7]*3 + [1e8, 1e9, 1e10, 1e11, 1e12],      300, 3000, "ext-low-beta"),
        (2e-5,  [1e6]*5 + [1e7]*3 + [1e8, 1e9, 1e10, 1e11, 1e12],      300, 3000, "ext-low-noisy"),
        (0.0,   [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14],    400, 4000, "high-hist"),
        (1e-5,  [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14],    400, 4000, "high-hist-noisy"),
    ]

    for ci, (noise, betas, hist, iters, label) in enumerate(configs):
        elapsed = time.time() - t_start
        if elapsed > 9000:  # 2.5h time limit for this strategy
            break

        seed = ci * 7  # spread seeds
        rng = np.random.default_rng(seed)
        v0 = np.sqrt(np.maximum(f_90k, 0.0))
        if noise > 0:
            v0 = v0 + rng.normal(scale=noise, size=v0.shape)

        print(f"\n  Config {ci}/{len(configs)}: {label} (noise={noise:.1e}, "
              f"hist={hist}, iters={iters})", flush=True)
        t0 = time.time()
        f_new, c_new = lbfgs_vsq(v0, betas, max_iter=iters, history_size=hist)
        dt = time.time() - t0
        print(f"  => C={c_new:.18f} ({dt:.0f}s)", flush=True)
        update(f_new, c_new, f"A-{label}")

    # ── Strategy B: scipy L-BFGS-B on exact objective ────────────────────
    elapsed = time.time() - t_start
    if elapsed < 10800:
        print(f"\n{'='*60}")
        print("Strategy B: scipy L-BFGS-B on exact objective")
        print(f"{'='*60}")

        # Try on OrganonAgent
        print("  From OrganonAgent:", flush=True)
        t0 = time.time()
        f_b1, c_b1 = scipy_lbfgsb(f_org, maxiter=10000)
        dt = time.time() - t0
        print(f"  => C={c_b1:.18f} ({dt:.0f}s)", flush=True)
        update(f_b1, c_b1, "B-scipy-org")

        # Try on best from strategy A
        if global_best_c < c_org:
            print("  From Strategy A best:", flush=True)
            t0 = time.time()
            f_b2, c_b2 = scipy_lbfgsb(global_best_f, maxiter=10000)
            dt = time.time() - t0
            print(f"  => C={c_b2:.18f} ({dt:.0f}s)", flush=True)
            update(f_b2, c_b2, "B-scipy-best")

    # ── Strategy C: Extended gradient polish ──────────────────────────────
    elapsed = time.time() - t_start
    if elapsed < 10800:
        print(f"\n{'='*60}")
        print("Strategy C: Extended gradient polish")
        print(f"{'='*60}")

        # Polish the global best
        print(f"  From current best (C={global_best_c:.18f}):", flush=True)
        t0 = time.time()
        f_c, c_c = gradient_polish(global_best_f, max_iters=10000, lr0=1e-6)
        dt = time.time() - t0
        print(f"  => C={c_c:.18f} ({dt:.0f}s)", flush=True)
        update(f_c, c_c, "C-polish")

    # ── Summary ──────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    print(f"\n{'='*60}")
    print("BASIN SEARCH COMPLETE")
    print(f"{'='*60}")
    print(f"OrganonAgent #1: {c_org:.18f}")
    print(f"Our best:        {global_best_c:.18f}")
    delta = c_org - global_best_c
    print(f"Delta:           {delta:+.6e}")
    print(f"Beats #1:        {'YES' if global_best_c < target else 'NO'}")
    print(f"Total time:      {elapsed/60:.1f} min")

    save_sol(global_best_f, global_best_c, "basin-final")


if __name__ == "__main__":
    main()
