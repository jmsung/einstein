"""Shrink–regrow probe: refill pruned cells and re-opt at full support.

The pruning campaign bought sign fragmentation (823 → 2021 negative runs) by
removing support, but the P4 leader holds 4705 runs at FULL support — the
shrink trajectory cannot converge to the leader's structure. This probe uses
pruning as a *fragmentation generator* only: take the fragmented pruned best,
refill its zero cells with tiny random-sign noise, and run the strong cascade
at full support. The re-opt starts in the fragmented sign-topology basin (not
the smooth seed's), with the support dimension restored.

Usage:
    uv run python scripts/third_autocorrelation/regrow_reopt.py \\
        --start results/problem-4-third-autocorrelation/selfprune-FINAL-1.452437615039.json \\
        --noise-scale 1e-6 --seeds 0 1 2
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import (
    lbfgs_masked,
    load_warmstart,
    neg_run_count,
)

RESULTS = Path("results/problem-4-third-autocorrelation")
ARENA_1 = 1.4523043331832
DEFAULT_BETAS = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13]


def regrow(f: np.ndarray, noise_scale: float, rng: np.random.Generator) -> np.ndarray:
    """Refill zero cells with tiny random-sign noise; keep active cells as-is."""
    out = f.copy()
    dead = out == 0.0
    scale = noise_scale * np.median(np.abs(out[~dead]))
    out[dead] = rng.normal(scale=scale, size=int(dead.sum()))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--start", required=True, help="pruned (compact-support) solution JSON")
    ap.add_argument("--noise-scale", type=float, default=1e-6)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0])
    ap.add_argument("--max-iter", type=int, default=2000)
    ap.add_argument("--betas", type=float, nargs="*", default=DEFAULT_BETAS)
    args = ap.parse_args()

    f0 = load_warmstart(args.start)
    n = len(f0)
    dead = int((f0 == 0.0).sum())
    print(
        f"start: {args.start}  n={n}  support={n - dead}  dead={dead}  neg_runs={neg_run_count(f0)}"
    )

    full_mask = np.ones(n, dtype=bool)
    best_c, best_f = float("inf"), None
    for seed in args.seeds:
        rng = np.random.default_rng(seed)
        f_init = regrow(f0, args.noise_scale, rng)
        f_opt, c = lbfgs_masked(f_init, list(args.betas), mask=full_mask, max_iter=args.max_iter)
        print(
            f"  seed={seed}  C={c:.13f}  neg_runs={neg_run_count(f_opt)}  "
            f"support={int(np.count_nonzero(f_opt))}",
            flush=True,
        )
        if c < best_c:
            best_c, best_f = c, f_opt.copy()

    print(f"\nbest C = {best_c:.16f}  (vs arena #1 {ARENA_1:.13f}, delta {ARENA_1 - best_c:+.3e})")
    RESULTS.mkdir(parents=True, exist_ok=True)
    out = RESULTS / f"regrow-{best_c:.12f}.json"
    with open(out, "w") as fh:
        json.dump(
            {
                "values": best_f.tolist(),
                "score": best_c,
                "n": n,
                "neg_runs": neg_run_count(best_f),
                "tag": "regrow",
            },
            fh,
        )
    print(f"saved {out}")


if __name__ == "__main__":
    main()
