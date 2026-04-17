"""Higher-n optimizer: block-repeat OrganonAgent 90k → 180k/270k and optimize.

Key insight: block-repeat preserves score exactly, but the extra DOF allow
the optimizer to break symmetry and find deeper minima. This is exactly
what worked going from 30k→90k (improvement of 1.23e-6).

Uses v^2 parameterization with aggressive low-beta L-BFGS exploration.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.evaluator import verify_and_compute

RESULTS = Path("results/problem-2-first-autocorrelation")
RESULTS.mkdir(parents=True, exist_ok=True)


def exact_score(f: np.ndarray) -> float:
    return float(verify_and_compute(f.astype(np.float64).tolist()))


def autoconv_fft(f: torch.Tensor) -> torch.Tensor:
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
    conv = autoconv_fft(f)
    s = f.sum()
    ratios = conv / (s * s * dx)
    return smooth_max(ratios, beta)


def surrogate_exp(v: torch.Tensor, beta: float) -> torch.Tensor:
    f = torch.exp(v)
    n = f.shape[-1]
    dx = 0.5 / n
    conv = autoconv_fft(f)
    s = f.sum()
    ratios = conv / (s * s * dx)
    return smooth_max(ratios, beta)


def lbfgs_run(v_init: np.ndarray, betas: list[float], param_type: str = "vsq",
              max_iter: int = 2000, lr: float = 1.0,
              history_size: int = 200) -> tuple[np.ndarray, float]:
    """Run L-BFGS cascade. param_type: 'vsq' for f=v^2, 'exp' for f=exp(v)."""
    v = torch.tensor(v_init.copy(), dtype=torch.float64, requires_grad=True)
    best_c = float("inf")
    best_f = None

    surr_fn = surrogate_vsq if param_type == "vsq" else surrogate_exp

    for beta in betas:
        opt = torch.optim.LBFGS(
            [v], lr=lr, max_iter=max_iter,
            tolerance_grad=1e-15, tolerance_change=1e-20,
            history_size=history_size, line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surr_fn(v, beta)
            loss.backward()
            return loss

        t0 = time.time()
        opt.step(closure)
        dt = time.time() - t0

        if param_type == "vsq":
            f_np = (v.detach().cpu().numpy() ** 2).astype(np.float64)
        else:
            f_np = np.exp(v.detach().cpu().numpy()).astype(np.float64)

        c = exact_score(f_np)
        tag = " ***" if c < best_c else ""
        if c < best_c:
            best_c = c
            best_f = f_np.copy()
        print(f"    beta={beta:.0e} C={c:.18f} ({dt:.1f}s){tag}", flush=True)

    return best_f, best_c


def save_solution(f: np.ndarray, score: float, path: Path, tag: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as fh:
        json.dump({"values": f.tolist(), "score": score, "n": len(f), "tag": tag}, fh)
    print(f"  Saved: {path}")


def main():
    t_start = time.time()

    # Load OrganonAgent solution
    with open(RESULTS / "sol-01-OrganonAgent-1798.json") as f:
        org = json.load(f)
    f_org = np.array(org["values"], dtype=np.float64)
    c_org = exact_score(f_org)
    n_org = len(f_org)
    target = c_org - 1e-7
    print(f"OrganonAgent: n={n_org}, C={c_org:.18f}")
    print(f"Target: < {target:.18f}")

    # Also load n=30k for alternative warmstarts
    sol30k = RESULTS / "sol-03-Together_AI-44.json"
    if sol30k.exists():
        with open(sol30k) as f:
            d30k = json.load(f)
        f_30k = np.array(d30k["values"], dtype=np.float64)
    else:
        f_30k = None

    global_best_c = c_org
    global_best_f = f_org.copy()

    def update_best(f, c, label):
        nonlocal global_best_c, global_best_f
        if c < global_best_c:
            delta = global_best_c - c
            global_best_c = c
            global_best_f = f.copy()
            save_solution(f, c, RESULTS / f"best-{label}-{c:.10f}.json", tag=label)
            print(f"\n  >>>>>> NEW GLOBAL BEST: {c:.18f} (delta={delta:.3e}) <<<<<<")
            return True
        return False

    # ── Strategy 1: Block-repeat 90k→180k, then v^2 L-BFGS ──────────────
    for mult, n_target in [(2, 180000), (3, 270000)]:
        elapsed = time.time() - t_start
        if elapsed > 10800:  # 3h limit
            break

        print(f"\n{'='*60}")
        print(f"Strategy: block-repeat {n_org} → {n_target} (×{mult}), then v^2 L-BFGS")
        print(f"{'='*60}")

        f_up = np.repeat(f_org, mult)
        c_up = exact_score(f_up)
        print(f"Block-repeated: C={c_up:.18f}")

        for seed in range(6):
            elapsed = time.time() - t_start
            if elapsed > 10800:
                break

            rng = np.random.default_rng(seed)
            v0 = np.sqrt(np.maximum(f_up, 0.0))

            # Different noise levels
            noise_scales = [0.0, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3]
            noise = noise_scales[seed]
            if noise > 0:
                v0 = v0 + rng.normal(scale=noise, size=v0.shape)

            # Beta schedules: emphasize low-beta exploration
            if seed < 2:
                betas = [1e6, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]
                hist, iters = 300, 3000
            elif seed < 4:
                betas = [5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 1e9, 1e10, 1e11, 1e12]
                hist, iters = 250, 2500
            else:
                betas = [1e5, 5e5, 1e6, 5e6, 1e7, 1e8, 1e9, 1e10, 1e11]
                hist, iters = 200, 2000

            print(f"\n  Seed {seed}: n={n_target}, noise={noise:.1e}, "
                  f"hist={hist}, iters={iters}", flush=True)

            t0 = time.time()
            f_new, c_new = lbfgs_run(v0, betas, param_type="vsq",
                                      max_iter=iters, history_size=hist)
            dt = time.time() - t0
            print(f"  => C={c_new:.18f} ({dt:.0f}s)", flush=True)
            update_best(f_new, c_new, f"n{n_target}-vsq-s{seed}")

    # ── Strategy 2: 30k→180k (6x) to explore different basin ─────────────
    if f_30k is not None:
        elapsed = time.time() - t_start
        if elapsed < 10800:
            print(f"\n{'='*60}")
            print(f"Strategy: 30k→180k (×6), then v^2 L-BFGS")
            print(f"{'='*60}")

            f_up = np.repeat(f_30k, 6)
            c_up = exact_score(f_up)
            print(f"Block-repeated 30k→180k: C={c_up:.18f}")

            for seed in range(3):
                elapsed = time.time() - t_start
                if elapsed > 10800:
                    break
                rng = np.random.default_rng(50 + seed)
                v0 = np.sqrt(np.maximum(f_up, 0.0))
                if seed > 0:
                    v0 = v0 + rng.normal(scale=1e-4, size=v0.shape)

                betas = [1e6, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]
                print(f"\n  Seed {seed}: n=180000 from 30k base", flush=True)
                t0 = time.time()
                f_new, c_new = lbfgs_run(v0, betas, param_type="vsq",
                                          max_iter=3000, history_size=300)
                dt = time.time() - t0
                print(f"  => C={c_new:.18f} ({dt:.0f}s)", flush=True)
                update_best(f_new, c_new, f"n180k-from30k-s{seed}")

    # ── Strategy 3: exp(v) at 180k from OrganonAgent ─────────────────────
    elapsed = time.time() - t_start
    if elapsed < 10800:
        print(f"\n{'='*60}")
        print(f"Strategy: exp(v) L-BFGS at n=180k from OrganonAgent")
        print(f"{'='*60}")

        f_up = np.repeat(f_org, 2)
        for seed in range(3):
            elapsed = time.time() - t_start
            if elapsed > 10800:
                break
            rng = np.random.default_rng(70 + seed)
            v0 = np.log(np.maximum(f_up, 1e-30))
            if seed > 0:
                v0 = v0 + rng.normal(scale=1e-3, size=v0.shape)

            betas = [1e6, 1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]
            print(f"\n  Seed {seed}: exp(v) at n=180000", flush=True)
            t0 = time.time()
            f_new, c_new = lbfgs_run(v0, betas, param_type="exp",
                                      max_iter=2000, history_size=200)
            dt = time.time() - t0
            print(f"  => C={c_new:.18f} ({dt:.0f}s)", flush=True)
            update_best(f_new, c_new, f"n180k-exp-s{seed}")

    # ── Summary ──────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"HIGHER-N OPTIMIZATION COMPLETE")
    print(f"{'='*60}")
    print(f"OrganonAgent #1: {c_org:.18f}")
    print(f"Our best:        {global_best_c:.18f}")
    print(f"Delta:           {c_org - global_best_c:+.6e}")
    beat = global_best_c < target
    print(f"BEATS #1:        {'YES' if beat else 'NO'}")
    print(f"Total time:      {elapsed/60:.1f} min")

    save_solution(global_best_f, global_best_c,
                 RESULTS / "higher-n-best.json", tag="higher-n-final")


if __name__ == "__main__":
    main()
