"""P13 push: CMA-ES on log-gap parameterization.

Covariance matrix adaptation evolution strategy — never tried. Designed for
non-convex continuous optimization of 100-1000 dim problems. Starts from the
current best, explores via population-based search, and adapts covariance.

Also does a quick L-BFGS polish after each generation's best.
"""

import json
import os
import shutil
import sys
import time
from pathlib import Path

import cma
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_e_bh_lbfgs import lbfgs_polish, reconstruct_weights, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def log_gaps_to_multi(log_gaps: np.ndarray, x_lo: float, x_hi: float) -> np.ndarray:
    """Map log-gap vector to sorted multipartite x positions."""
    gaps = np.exp(np.clip(log_gaps, -30.0, 10.0))
    gaps = gaps / gaps.sum() * (x_hi - x_lo)
    xs = x_lo + np.cumsum(gaps[:-1])
    xs = np.clip(xs, x_lo + 1e-14, x_hi - 1e-14)
    xs.sort()
    return xs


def multi_to_log_gaps(multi_xs: np.ndarray, x_lo: float, x_hi: float) -> np.ndarray:
    """Invert: sorted xs → log-gap vector."""
    gaps = np.empty(len(multi_xs) + 1)
    gaps[0] = multi_xs[0] - x_lo
    gaps[1:-1] = np.diff(multi_xs)
    gaps[-1] = x_hi - multi_xs[-1]
    gaps = np.maximum(gaps, 1e-15)
    return np.log(gaps)


def objective(log_gaps: np.ndarray, bi_xs: np.ndarray, x_lo: float, x_hi: float) -> float:
    """CMA minimizes, so return -score."""
    multi = log_gaps_to_multi(log_gaps, x_lo, x_hi)
    return -true_score(bi_xs, multi)


def save_solution(bi_xs: np.ndarray, multi_xs: np.ndarray, tag: str) -> Path:
    w = reconstruct_weights(bi_xs, multi_xs)
    score = compute_score(w)
    RESULTS.mkdir(parents=True, exist_ok=True)
    out = RESULTS / f"solution-{tag}.json"
    with open(out, "w") as f:
        json.dump({"weights": w.tolist()}, f)
    print(f"  Saved {out}  score={score:.14f}")
    backup_dir = os.environ.get("EINSTEIN_BACKUP_DIR")
    if backup_dir:
        bd = Path(backup_dir)
        bd.mkdir(parents=True, exist_ok=True)
        shutil.copy2(out, bd / f"solution-push-f-{score:.10f}.json")
    return out


def main():
    sol_path = RESULTS / "solution.json"
    bi_xs, multi_xs = load_xs_from_solution(sol_path)
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f} ({len(multi_xs)} multipartite pts)")

    x_lo, x_hi = 0.5, 0.95

    # Start from current best in log-gap space
    x0 = multi_to_log_gaps(multi_xs, x_lo, x_hi)
    print(f"Log-gap dim: {len(x0)}")
    print(f"Log-gap range: [{x0.min():.3f}, {x0.max():.3f}]")

    # CMA-ES config
    # sigma0: initial step. Small since we're near optimum.
    # popsize: default is 4 + 3*log(N) ≈ 22 for N=491. Bump to 30.
    sigma0 = 0.05  # 5% of log-gap spread
    options = {
        "popsize": 30,
        "maxiter": 200,
        "tolfun": 1e-18,
        "tolx": 1e-16,
        "verbose": -9,  # quiet
        "bounds": [[None] * len(x0), [None] * len(x0)],  # unbounded
    }
    es = cma.CMAEvolutionStrategy(x0, sigma0, options)

    best_score = init_score
    best_multi = multi_xs.copy()
    t0 = time.time()
    gen = 0

    print(f"\n=== CMA-ES (popsize={options['popsize']}, sigma0={sigma0}) ===")
    while not es.stop() and time.time() - t0 < 600:
        gen += 1
        solutions = es.ask()
        fitnesses = [objective(s, bi_xs, x_lo, x_hi) for s in solutions]
        es.tell(solutions, fitnesses)

        # Track best
        best_idx = int(np.argmin(fitnesses))
        gen_best_score = -fitnesses[best_idx]
        if gen_best_score > best_score + 1e-14:
            best_score = gen_best_score
            best_multi = log_gaps_to_multi(solutions[best_idx], x_lo, x_hi)
            print(f"  gen {gen:3d}: {best_score:.14f} (+{best_score-init_score:.2e}) NEW BEST")
            # Polish with L-BFGS
            try:
                pol_multi, pol_torch_score = lbfgs_polish(best_multi, bi_xs, x_lo, x_hi, max_rounds=20)
                pol_true = true_score(bi_xs, pol_multi)
                if pol_true > best_score:
                    best_score = pol_true
                    best_multi = pol_multi
                    print(f"            L-BFGS polish: {pol_true:.14f} (+{pol_true-init_score:.2e})")
            except Exception as e:
                print(f"            L-BFGS polish failed: {e}")
        elif gen % 10 == 0:
            print(f"  gen {gen:3d}: best so far {best_score:.14f}  (sigma={es.sigma:.2e})")

    print(f"\nCMA-ES done. {gen} generations, {time.time()-t0:.0f}s")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.2e}")

    if best_score > init_score:
        save_solution(bi_xs, best_multi, "push-f-final")
        print("\n** IMPROVED — saved as solution-push-f-final.json")


if __name__ == "__main__":
    main()
