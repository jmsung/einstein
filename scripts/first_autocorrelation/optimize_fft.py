"""L-BFGS cascade over a smooth surrogate of the autocorrelation objective.

Uses an FFT-based autoconvolution (``O(n log n)`` per step) and a log-space
parameterization of the scalar field for non-negativity.

Usage:
    uv run python scripts/first_autocorrelation/optimize_fft.py \\
        --warmstart PATH --n N --beta BETAS --iters ITERS --out OUTPUT
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.optimizer import (
    exact_score_v,
    load_warmstart,
    surrogate_v,
    to_v,
    upsample,
)


def optimize(n: int, warmstart: Path, betas, iters: int, lr: float, seed: int,
             noise: float, floor: float):
    rng = np.random.default_rng(seed)
    torch.manual_seed(seed)

    v0 = load_warmstart(warmstart)
    if len(v0) != n:
        v0 = upsample(v0, n)

    v_param_np = to_v(v0, floor=floor)
    if noise > 0:
        v_param_np = v_param_np + rng.normal(
            scale=noise, size=v_param_np.shape
        )

    v = torch.tensor(v_param_np, dtype=torch.float64, requires_grad=True)
    print(f"Warmstart: {warmstart}  n={n}  noise={noise}  floor={floor}")
    best_c = exact_score_v(v)
    best_v = v.detach().cpu().numpy().copy()
    print(f"Initial C = {best_c:.16f}")

    for beta in betas:
        opt = torch.optim.LBFGS(
            [v], lr=lr, max_iter=iters, tolerance_grad=1e-14,
            tolerance_change=1e-18, history_size=100,
            line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate_v(v, beta, fft=True)
            loss.backward()
            return loss

        t0 = time.time()
        opt.step(closure)
        c_exact = exact_score_v(v)
        print(f"  beta={beta:.0e}  C={c_exact:.16f}  "
              f"delta_best={best_c - c_exact:+.3e}  ({time.time()-t0:.1f}s)",
              flush=True)
        if c_exact < best_c:
            best_c = c_exact
            best_v = v.detach().cpu().numpy().copy()

    best_f = np.exp(best_v).astype(np.float64)
    return best_f, best_c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n", type=int, required=True, help="Discretization size")
    p.add_argument("--warmstart", type=Path, required=True,
                   help="JSON solution file with 'values' field")
    p.add_argument("--beta", type=str, required=True,
                   help="Comma-separated beta cascade values")
    p.add_argument("--iters", type=int, default=1500)
    p.add_argument("--lr", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--noise", type=float, default=1e-3,
                   help="Gaussian noise scale added to log(f) initial (0 off)")
    p.add_argument("--floor", type=float, default=1e-30,
                   help="Floor on f before taking log (zero cells → log(floor))")
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    betas = [float(b) for b in args.beta.split(",")]
    best_f, best_c = optimize(args.n, args.warmstart, betas,
                              args.iters, args.lr, args.seed, args.noise,
                              args.floor)

    print(f"\nFinal C = {best_c:.16f}  (n={args.n})")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({"values": best_f.tolist(), "score": best_c, "n": args.n},
                      fh)
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
