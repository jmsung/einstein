"""P13 push: scipy L-BFGS-B with PyTorch autograd gradient.

Per research recommendation: scipy's L-BFGS-B has a more robust More-Thuente
line search than torch.optim.LBFGS for piecewise-smooth objectives. This may
extract additional gains where torch.optim.LBFGS stalled.

Uses bounded sigmoid parameterization (each x_i inside its scallop).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import assign_scallops, load_xs_from_solution, turan_y_torch  # noqa: E402
from push_g_bounded import (  # noqa: E402
    inverse_sigmoid_param,
    perturb_log_gaps,
    save_solution,
    scallop_bounds,
    score_torch_bounded,
    true_score,
)

RESULTS = Path("results/problem-13-edges-triangles")
torch.set_default_dtype(torch.float64)


def make_value_and_grad(bi_xs_np: np.ndarray, lo_np: np.ndarray, hi_np: np.ndarray, k_np: np.ndarray):
    """Build a scipy-compatible (f, g) function using torch autograd."""
    bi_t = torch.tensor(bi_xs_np, dtype=torch.float64)
    lo_t = torch.tensor(lo_np, dtype=torch.float64)
    hi_t = torch.tensor(hi_np, dtype=torch.float64)
    k_t = torch.tensor(k_np, dtype=torch.int64)

    def fg(raw_np: np.ndarray):
        raw = torch.tensor(raw_np, dtype=torch.float64, requires_grad=True)
        s = score_torch_bounded(raw, bi_t, lo_t, hi_t, k_t)
        loss = -s  # minimize
        loss.backward()
        return loss.item(), raw.grad.numpy()

    return fg


def scipy_polish(multi_xs: np.ndarray, bi_xs: np.ndarray, maxiter: int = 2000) -> tuple[np.ndarray, float]:
    """Polish using scipy L-BFGS-B with autograd gradient."""
    k_np = assign_scallops(multi_xs)
    lo_np, hi_np = scallop_bounds(k_np)
    multi_clamped = np.clip(multi_xs, lo_np, hi_np)
    raw0 = inverse_sigmoid_param(multi_clamped, lo_np, hi_np)

    fg = make_value_and_grad(bi_xs, lo_np, hi_np, k_np)

    result = minimize(
        fg,
        raw0,
        jac=True,
        method="L-BFGS-B",
        options={
            "maxcor": 20,
            "ftol": 1e-18,
            "gtol": 1e-14,
            "maxls": 40,
            "maxiter": maxiter,
        },
    )

    # Reconstruct xs from best raw
    raw_best = result.x
    sigmoid = 1.0 / (1.0 + np.exp(-raw_best))
    new_xs = lo_np + (hi_np - lo_np) * sigmoid
    new_xs = np.sort(new_xs)
    return new_xs, -result.fun


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best_multi = multi_xs.copy()
    best_score = init_score

    # Phase 1: scipy polish from current
    print("\n=== scipy L-BFGS-B polish ===")
    try:
        pol, _ = scipy_polish(multi_xs, bi_xs, maxiter=3000)
        sc = true_score(bi_xs, pol)
        print(f"  scipy polish: {sc:.14f}  delta={sc-init_score:+.3e}")
        if sc > best_score + 1e-14:
            best_multi = pol.copy()
            best_score = sc
    except Exception as e:
        print(f"  scipy polish failed: {e}")

    # Phase 2: BH with scipy polish as local minimizer
    print(f"\n=== BH + scipy L-BFGS-B ===")
    t0 = time.time()
    n_improvements = 0
    for seed in range(20):
        if time.time() - t0 > 400:
            break
        rng = np.random.default_rng(seed * 41 + 11)
        for noise in [0.3, 0.15, 0.08, 0.05, 0.03, 0.015, 0.01, 0.005]:
            pert = perturb_log_gaps(best_multi, 0.5, 0.95, noise, rng)
            try:
                pol, _ = scipy_polish(pert, bi_xs, maxiter=500)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-14:
                    best_multi = pol.copy()
                    best_score = sc
                    n_improvements += 1
                    print(f"  seed={seed:2d} noise={noise:.3f}: {sc:.14f} (+{sc-init_score:.3e})")
            except Exception:
                pass

    print(f"\nDone. {n_improvements} improvements.")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-m-final")
        print("\n** IMPROVED — saved")


if __name__ == "__main__":
    main()
