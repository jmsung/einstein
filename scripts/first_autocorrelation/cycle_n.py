"""Cycle through different n values, using fractional upsample/downsample as
basin-breaking noise. Run smooth cascade at each n, keep global best.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.first_autocorrelation.optimizer import (
    exact_score_f,
    surrogate_v,
    to_v,
    upsample,
)


def cascade(v_np, betas, iters):
    v = torch.tensor(v_np.copy(), dtype=torch.float64, requires_grad=True)
    for beta in betas:
        opt = torch.optim.LBFGS(
            [v], lr=1.0, max_iter=iters, tolerance_grad=1e-14,
            tolerance_change=1e-18, history_size=100,
            line_search_fn="strong_wolfe",
        )
        def closure():
            opt.zero_grad()
            loss = surrogate_v(v, beta, fft=True)
            loss.backward()
            return loss
        opt.step(closure)
    f = np.exp(v.detach().cpu().numpy()).astype(np.float64)
    return f, exact_score_f(f)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--warmstart", type=Path, required=True)
    p.add_argument("--n-cycle", type=str, required=True,
                   help="Comma-separated n values to cycle through")
    p.add_argument("--cycles", type=int, default=5)
    p.add_argument("--iters", type=int, default=1200)
    p.add_argument("--beta", type=str, default="1e8,1e9,1e10,1e11,1e12")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()

    with open(args.warmstart) as fh:
        data = json.load(fh)
    f_current = np.array(data["values"], dtype=np.float64)
    c_current = exact_score_f(f_current)
    print(f"Initial: n={len(f_current)} C={c_current:.18f}")

    ns = [int(x) for x in args.n_cycle.split(",")]
    betas = [float(b) for b in args.beta.split(",")]
    best_f = f_current.copy()
    best_c = c_current
    best_n = len(f_current)

    t0 = time.time()
    for cyc in range(args.cycles):
        for n_target in ns:
            # upsample/downsample current f
            if len(f_current) != n_target:
                f_resized = upsample(f_current, n_target)
            else:
                f_resized = f_current.copy()
            v0 = to_v(f_resized, floor=1e-25)
            f_new, c_new = cascade(v0, betas, args.iters)
            tag = ""
            if c_new < best_c:
                delta = best_c - c_new
                best_c = c_new
                best_f = f_new.copy()
                best_n = n_target
                tag = f"  * NEW BEST  Δ={delta:.3e}"
            # Always advance current to the new cascaded result so the next
            # n value starts from the latest basin.
            f_current = f_new
            print(f"  cycle={cyc} n={n_target:>6}  C={c_new:.18f}{tag}",
                  flush=True)

    print(f"\nBest C = {best_c:.18f}  at n={best_n}  ({time.time()-t0:.1f}s)")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as fh:
        json.dump({"values": best_f.tolist(), "score": best_c, "n": best_n}, fh)
    print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
