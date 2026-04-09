"""P13 push: E-L optimal density initialization + polish.

From theory, the optimal point density is ρ*(x) ∝ sqrt(f(x)) where
f(x) = t'/2 - t'²/6.

We compute the cumulative distribution of sqrt(f) over [0.5, 0.95], place 490
points at the inverse CDF at uniform quantiles, then polish with bounded L-BFGS.

If our current solution is NOT exactly E-L optimal, this should find a new
starting point that's closer to the theoretical floor.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_densities, compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, perturb_log_gaps, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def t_star(x: float) -> float:
    return compute_densities(turan_row(x))[1]


def t_prime(x: float, eps: float = 1e-6) -> float:
    return (t_star(x + eps) - t_star(x - eps)) / (2 * eps)


def f_density(x: float) -> float:
    tp = t_prime(x)
    return max(0.0, tp / 2.0 - tp * tp / 6.0)


def sqrt_f(x: float) -> float:
    return np.sqrt(f_density(x))


def compute_el_positions(m: int = 490, x_lo: float = 0.5, x_hi: float = 0.95) -> np.ndarray:
    """Compute E-L optimal point positions via inverse-CDF sampling."""
    # Build cumulative F(x) = ∫_{x_lo}^x sqrt(f(s)) ds
    # Sample on a fine grid within each scallop (since kinks exist at x=1-1/k)
    grid = []
    for k in range(2, 20):
        lo_k = max(1 - 1/k, x_lo) + 1e-9
        hi_k = min(1 - 1/(k+1), x_hi) - 1e-9
        if lo_k >= hi_k:
            continue
        grid.extend(np.linspace(lo_k, hi_k, 2000))
    grid = np.sort(np.array(grid))
    values = np.array([sqrt_f(x) for x in grid])

    # Cumulative (trapezoid)
    dx = np.diff(grid)
    avg = 0.5 * (values[:-1] + values[1:])
    cum = np.concatenate([[0], np.cumsum(dx * avg)])
    total = cum[-1]
    print(f"  Total ∫ sqrt(f) dx = {total:.8f}")

    # Inverse CDF at quantiles (m+1)/(m+2), avoiding the boundaries
    quantiles = np.linspace(0.5/m, 1 - 0.5/m, m)
    targets = quantiles * total
    # Interpolate: x such that cum(x) = target
    inv_cdf = interp1d(cum, grid, kind="linear", bounds_error=False, fill_value=(grid[0], grid[-1]))
    positions = inv_cdf(targets)
    return np.sort(positions)


def compute_theoretical_excess(m: int = 490) -> float:
    """Asymptotic E-L excess = (∫ sqrt(f))² / m."""
    total = 0
    for k in range(2, 20):
        lo = 1 - 1/k + 1e-10
        hi = 1 - 1/(k+1) - 1e-10
        integral, _ = quad(sqrt_f, lo, hi, limit=500)
        total += integral
    return total * total / m


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Current best: {init_score:.14f}")

    theoretical_excess = compute_theoretical_excess(490)
    theoretical_floor = -0.71158675291847 - theoretical_excess
    print(f"E-L theoretical excess for m=490: {theoretical_excess:.6e}")
    print(f"E-L theoretical floor:  {theoretical_floor:.14f}")
    print(f"Our excess over Razborov: {init_score - (-0.71158675291847):.6e}")
    print()

    # Compute E-L positions
    print("=== Computing E-L optimal positions ===")
    el_multi = compute_el_positions(m=490, x_lo=0.5, x_hi=0.95)
    print(f"E-L positions: {len(el_multi)} pts in [{el_multi.min():.6f}, {el_multi.max():.6f}]")

    el_raw_score = true_score(bi_xs, el_multi)
    print(f"E-L raw score: {el_raw_score:.14f}  delta={el_raw_score-init_score:+.3e}")

    # Polish
    print("\n=== Bounded L-BFGS polish from E-L positions ===")
    pol, _ = lbfgs_polish_bounded(el_multi, bi_xs, max_rounds=100)
    pol_score = true_score(bi_xs, pol)
    print(f"Polished: {pol_score:.14f}  delta={pol_score-init_score:+.3e}")

    best_multi = pol if pol_score > init_score + 1e-13 else multi_xs.copy()
    best_score = max(init_score, pol_score)

    # BH from this new point
    print(f"\n=== BH from best ({best_score:.14f}) ===")
    t0 = time.time()
    n_improvements = 0
    for seed in range(30):
        if time.time() - t0 > 300:
            break
        rng = np.random.default_rng(seed * 53 + 17)
        for noise in [0.2, 0.1, 0.05, 0.03, 0.015, 0.01]:
            pert = perturb_log_gaps(best_multi, 0.5, 0.95, noise, rng)
            try:
                new_pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=30)
                sc = true_score(bi_xs, new_pol)
                if sc > best_score + 1e-13:
                    best_multi = new_pol.copy()
                    best_score = sc
                    n_improvements += 1
                    print(f"  seed={seed} noise={noise}: {sc:.14f} (+{sc-init_score:.3e})")
            except Exception:
                pass

    print(f"\nFinal: {best_score:.14f}  gain from init={best_score-init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-o-final")
        print("\n** IMPROVED — saved")


if __name__ == "__main__":
    main()
