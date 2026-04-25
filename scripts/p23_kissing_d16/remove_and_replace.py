"""Remove one BW16 vector, optimize 2 fillers jointly.

If we can place 2 fillers s.t. total penalty (filler-vs-core + filler-vs-filler) < 2,
we beat the duplicate floor and achieve rank #1.

By concavity of p(γ) = 2 - 2*sqrt(2(1-γ)), spreading overlap across pairs
typically increases total penalty (not decreases), so this is mostly a
sanity probe — but BW16's specific link structure may admit a basin.
"""

from __future__ import annotations

import argparse
import time

import numpy as np
from scipy.optimize import minimize

from einstein.p23_kissing_d16.baseline import bw16_min_vectors
from einstein.p23_kissing_d16.evaluator import overlap_loss_fast


def smooth_score(params: np.ndarray, core_centers: np.ndarray, beta: float) -> float:
    """Evaluate smoothed hinge for 2 fillers + core. Score only — scipy uses
    finite differences for the gradient."""
    f1_raw = params[:16]
    f2_raw = params[16:]
    n1 = np.linalg.norm(f1_raw)
    n2 = np.linalg.norm(f2_raw)
    f1 = f1_raw / n1
    f2 = f2_raw / n2
    c1 = 2.0 * f1
    c2 = 2.0 * f2

    # f1 vs core
    diff1 = c1[None, :] - core_centers
    dist1 = np.sqrt((diff1 ** 2).sum(axis=1) + 1e-30)
    h1 = 2.0 - dist1
    bh1 = beta * h1
    sp1 = np.where(bh1 > 30, bh1, np.log1p(np.exp(np.minimum(bh1, 30))))
    s1 = float(sp1.sum() / beta)

    # f2 vs core
    diff2 = c2[None, :] - core_centers
    dist2 = np.sqrt((diff2 ** 2).sum(axis=1) + 1e-30)
    h2 = 2.0 - dist2
    bh2 = beta * h2
    sp2 = np.where(bh2 > 30, bh2, np.log1p(np.exp(np.minimum(bh2, 30))))
    s2 = float(sp2.sum() / beta)

    # f1 vs f2
    diff12 = c1 - c2
    d12 = np.sqrt((diff12 ** 2).sum() + 1e-30)
    h12 = 2.0 - d12
    bh12 = beta * h12
    sp12 = max(bh12, np.log1p(np.exp(min(bh12, 30)))) / beta if bh12 > 30 else float(np.log1p(np.exp(bh12)) / beta)

    return float(s1 + s2 + sp12)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--drop", type=int, nargs="+", default=[0, 32, 2272],
                        help="Indices of BW16 vectors to try dropping (one at a time)")
    parser.add_argument("--n-starts", type=int, default=30)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    bw = bw16_min_vectors()
    rng = np.random.default_rng(args.seed)

    overall_best = (np.inf, None)
    t_start = time.time()
    for drop_idx in args.drop:
        core = np.delete(bw, drop_idx, axis=0)  # (4319, 16)
        core_centers = 2.0 * core
        v_dropped = bw[drop_idx]
        print(f"\nDropping BW16 row {drop_idx} (norm={np.linalg.norm(v_dropped):.6f})")

        best_score = np.inf
        best_params = None
        for k in range(args.n_starts):
            # init: f1 near v_dropped, f2 random
            init1 = v_dropped + 0.05 * rng.standard_normal(16)
            init1 /= np.linalg.norm(init1)
            init2 = rng.standard_normal(16)
            init2 /= np.linalg.norm(init2)
            params = np.concatenate([init1, init2])

            for beta in (10, 50, 200, 1000):
                res = minimize(smooth_score, params, args=(core_centers, beta),
                               method="L-BFGS-B", options={"maxiter": 100, "ftol": 1e-15})
                params = res.x

            f1 = params[:16] / np.linalg.norm(params[:16])
            f2 = params[16:] / np.linalg.norm(params[16:])
            full = np.vstack([core, f1[None, :], f2[None, :]])
            s = overlap_loss_fast(full)
            if s < best_score:
                best_score = s
                best_params = (f1.copy(), f2.copy())
                elapsed = time.time() - t_start
                print(f"  start {k}: score = {s:.10f}  (elapsed {elapsed:.0f}s)")

        print(f"  best for drop_idx={drop_idx}: {best_score:.10f}")
        if best_score < overall_best[0]:
            overall_best = (best_score, drop_idx)

    print(f"\n*** Overall best: drop_idx={overall_best[1]}, score={overall_best[0]:.10f} ***")
    if overall_best[0] < 2.0:
        print("*** BEAT THE 2.0 FLOOR — RANK #1 CANDIDATE ***")
    else:
        print("(score >= 2.0 — rank #1 still infeasible)")


if __name__ == "__main__":
    main()
