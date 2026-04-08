"""Third Autocorrelation (P4) — smooth-max gradient optimizer via PyTorch.

Loss: C = LSE_beta(f★f) / (sum(f)·dx)^2  where LSE is log-sum-exp smoothing.
As beta→∞, LSE→max. Differentiable via autograd. Scale-invariant in f so
we fix ∫f = 1 via a normalized parametrization.

Usage:
    uv run python scripts/third_autocorrelation/optimize_torch.py \
        --n 400 --start sota --beta-cascade 1e3,1e4,1e5,1e6 --iters 2000

    # warm-start from SOTA at larger n
    uv run python scripts/third_autocorrelation/optimize_torch.py \
        --n 1600 --start sota --beta-cascade 1e3,1e4,1e5 --iters 1500
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.third_autocorrelation.evaluator import verify_and_compute

REPO_ROOT = Path(__file__).resolve().parents[2]
MB_SOLUTIONS = Path.home() / "projects/workbench/memory-bank/einstein/docs/problem-4-third-autocorrelation/solutions"


def load_sota_n400() -> np.ndarray:
    with open(MB_SOLUTIONS / "rank01_DarwinAgent8427_n400.json") as fh:
        return np.array(json.load(fh)["values"], dtype=np.float64)


def upsample_block(v: np.ndarray, n_target: int) -> np.ndarray:
    """Upsample via piecewise-constant block-repeat (preserves score)."""
    n_src = len(v)
    if n_target == n_src:
        return v.copy()
    assert n_target % n_src == 0, f"n_target={n_target} must be multiple of {n_src}"
    k = n_target // n_src
    return np.repeat(v, k)


def upsample_refine(v: np.ndarray, n_target: int, rng) -> np.ndarray:
    """Block-repeat + tiny noise to give gradient a non-degenerate start."""
    v_new = upsample_block(v, n_target)
    noise = rng.normal(scale=1e-6 * np.std(v_new), size=v_new.shape)
    return v_new + noise


def smooth_max(x: torch.Tensor, beta: float) -> torch.Tensor:
    """log-sum-exp smoothed max. For beta=1e6, converges to true max."""
    return (1.0 / beta) * torch.logsumexp(beta * x, dim=-1)


def compute_score_torch(f: torch.Tensor, beta: float) -> torch.Tensor:
    """Compute smoothed C = smooth_max(f★f·dx) / (sum(f)·dx)^2."""
    n = f.shape[-1]
    dx = 0.5 / n
    f_2d = f.view(1, 1, -1)
    kernel = f.flip(0).view(1, 1, -1)
    autoconv = torch.nn.functional.conv1d(f_2d, kernel, padding=n - 1).view(-1) * dx
    peak = smooth_max(autoconv, beta)
    integral = f.sum() * dx
    return peak / (integral ** 2)


def exact_score_torch(f: torch.Tensor) -> float:
    """Exact max-based C using same formula as arena verifier."""
    return float(verify_and_compute(f.detach().cpu().numpy().tolist()))


def optimize(n: int, start: str, beta_cascade, iters: int, lr: float,
             seed: int = 0, device: str = "cpu", normalize: bool = True):
    rng = np.random.default_rng(seed)
    torch.manual_seed(seed)

    # Initialize
    if start == "sota":
        v0 = load_sota_n400()
        if n != 400:
            v0 = upsample_refine(v0, n, rng)
    elif start == "random_pos":
        v0 = rng.uniform(0.1, 1.0, size=n)
    elif start == "random_mix":
        v0 = rng.normal(0.5, 0.3, size=n)
    elif start == "edge_heavy":
        # Edge-concentrated: large at endpoints, small middle
        x = np.linspace(-1, 1, n)
        v0 = 1.0 + 10.0 * (x ** 8)
    elif start.endswith(".json"):
        with open(start) as fh:
            d = json.load(fh)
        v0 = np.array(d["values"], dtype=np.float64)
        if len(v0) != n:
            if n % len(v0) == 0:
                v0 = upsample_refine(v0, n, rng)
            else:
                raise ValueError(f"n={n} not a multiple of start file len={len(v0)}")
    else:
        raise ValueError(f"Unknown start: {start}")

    f = torch.tensor(v0, dtype=torch.float64, device=device, requires_grad=True)
    print(f"\nStart: {start}  n={n}")
    print(f"Initial exact C = {exact_score_torch(f):.13f}")

    best_c = exact_score_torch(f)
    best_v = f.detach().cpu().numpy().copy()

    for beta_idx, beta in enumerate(beta_cascade):
        print(f"\n--- beta = {beta:.0e} ---")
        opt = torch.optim.LBFGS(
            [f], lr=lr, max_iter=iters, tolerance_grad=1e-14,
            tolerance_change=1e-16, history_size=100, line_search_fn="strong_wolfe"
        )

        def closure():
            opt.zero_grad()
            c = compute_score_torch(f, beta)
            c.backward()
            return c

        t0 = time.time()
        opt.step(closure)
        dt = time.time() - t0
        c_smooth = float(compute_score_torch(f, beta).detach())
        c_exact = exact_score_torch(f)
        print(f"  smooth={c_smooth:.13f}  exact={c_exact:.13f}  ({dt:.1f}s)")
        if c_exact < best_c:
            best_c = c_exact
            best_v = f.detach().cpu().numpy().copy()
            print(f"  NEW BEST: {best_c:.13f}")

    return best_v, best_c


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--n", type=int, default=400)
    p.add_argument("--start", type=str, default="sota")
    p.add_argument("--beta-cascade", type=str, default="1e3,1e4,1e5,1e6,1e7")
    p.add_argument("--iters", type=int, default=2000)
    p.add_argument("--lr", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--device", type=str, default="cpu")
    p.add_argument("--out", type=str, default=None)
    args = p.parse_args()

    betas = [float(b) for b in args.beta_cascade.split(",")]
    best_v, best_c = optimize(args.n, args.start, betas, args.iters,
                              args.lr, args.seed, args.device)

    print(f"\n=== Final: C = {best_c:.13f}  (n={args.n}) ===")
    print(f"SOTA ref: 1.4540379299619")
    print(f"Delta vs SOTA: {best_c - 1.4540379299619:.6e}")

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({"values": best_v.tolist(), "score": best_c, "n": args.n}, fh)
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
