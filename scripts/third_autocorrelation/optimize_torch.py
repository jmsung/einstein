"""Refine a third-autocorrelation candidate via L-BFGS on a smooth surrogate.

Direct-convolution backend. For larger ``--n``, use ``optimize_fft.py``.

Usage:
    uv run python scripts/third_autocorrelation/optimize_torch.py \\
        --warmstart PATH --n N --beta BETAS --iters ITERS --out OUTPUT
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.third_autocorrelation.optimizer import (
    exact_score,
    load_warmstart,
    surrogate,
    upsample,
)


def optimize(n: int, warmstart: Path, betas, iters: int, lr: float, seed: int):
    rng = np.random.default_rng(seed)
    torch.manual_seed(seed)

    v0 = load_warmstart(warmstart)
    if len(v0) != n:
        v0 = upsample(v0, n)
        v0 = v0 + rng.normal(scale=1e-6 * np.std(v0), size=v0.shape)

    f = torch.tensor(v0, dtype=torch.float64, requires_grad=True)
    print(f"Warmstart: {warmstart}  n={n}")
    best_c = exact_score(f)
    best_v = f.detach().cpu().numpy().copy()
    print(f"Initial C = {best_c:.13f}")

    for beta in betas:
        opt = torch.optim.LBFGS(
            [f], lr=lr, max_iter=iters, tolerance_grad=1e-14,
            tolerance_change=1e-16, history_size=100,
            line_search_fn="strong_wolfe",
        )

        def closure():
            opt.zero_grad()
            loss = surrogate(f, beta, fft=False)
            loss.backward()
            return loss

        t0 = time.time()
        opt.step(closure)
        c_exact = exact_score(f)
        print(f"  beta={beta:.0e}  C={c_exact:.13f}  ({time.time()-t0:.1f}s)",
              flush=True)
        if c_exact < best_c:
            best_c = c_exact
            best_v = f.detach().cpu().numpy().copy()

    return best_v, best_c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n", type=int, required=True, help="Discretization size")
    p.add_argument("--warmstart", type=Path, required=True,
                   help="JSON solution file with 'values' field")
    p.add_argument("--beta", type=str, required=True,
                   help="Comma-separated beta cascade values")
    p.add_argument("--iters", type=int, default=1000)
    p.add_argument("--lr", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    betas = [float(b) for b in args.beta.split(",")]
    best_v, best_c = optimize(args.n, args.warmstart, betas,
                              args.iters, args.lr, args.seed)

    print(f"\nFinal C = {best_c:.13f}  (n={args.n})")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump({"values": best_v.tolist(), "score": best_c, "n": args.n},
                      fh)
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
