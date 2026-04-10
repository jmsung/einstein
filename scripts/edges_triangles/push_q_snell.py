"""P13 push: KKT-stationarity ratio at scallop cusps.

KKT stationarity at each scallop cusp x_k = 1-1/k gives:
    h_{k-} * (3 - t*'(x_k^-)) = h_{k+} * (3 - t*'(x_k^+))

This script tests a range of h+/h- ratios at cusp-adjacent gaps, polishes
each with bounded L-BFGS, and keeps the best. The smooth E-L prediction
h_- = h_+ is tested as a control.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def apply_snell_at_cusps(multi_xs: np.ndarray, ratio: float = 2.0) -> np.ndarray:
    """Adjust gaps around each cusp so h+/h- = ratio, keeping total length.

    For each cusp x_k = 1-1/k (k=3..19):
    - Find index of snapped cusp point (nearest point)
    - Current left gap g_L = x_cusp - x_{i-1}, right gap g_R = x_{i+1} - x_cusp
    - Total g_L + g_R is preserved
    - New g_L = (g_L + g_R) / (1 + ratio)
    - New g_R = ratio * new g_L
    - Move x_{i-1} and x_{i+1} accordingly? NO — keep x_{i-1} and x_{i+1} fixed,
      move the cusp point itself? Actually, the cusp point is at x_k (fixed).
      We need to move x_{i-1} or x_{i+1} to adjust h_{k-} and h_{k+}.

    Alternative: move x_{i-1} (just outside scallop k-1) to achieve the ratio.
    New x_{i-1} = x_cusp - g_L_new.
    """
    xs = multi_xs.copy()
    for k in range(3, 20):
        x_k = 1.0 - 1.0 / k
        idx_snap = int(np.argmin(np.abs(xs - x_k)))
        if abs(xs[idx_snap] - x_k) > 1e-6:
            continue  # no cusp point found
        if idx_snap == 0 or idx_snap == len(xs) - 1:
            continue

        x_cusp = xs[idx_snap]
        x_left = xs[idx_snap - 1]
        x_right = xs[idx_snap + 1]
        g_L = x_cusp - x_left
        g_R = x_right - x_cusp
        total = g_L + g_R

        # New ratio: g_R = ratio * g_L, g_L + g_R = total
        # g_L * (1 + ratio) = total → g_L = total / (1 + ratio)
        new_g_L = total / (1 + ratio)
        new_g_R = ratio * new_g_L

        # Move neighbors to achieve these gaps (keeping cusp fixed)
        xs[idx_snap - 1] = x_cusp - new_g_L
        xs[idx_snap + 1] = x_cusp + new_g_R

    # Resort (should be mostly unchanged)
    return np.sort(xs)


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best_multi = multi_xs.copy()
    best_score = init_score

    # Test different ratios
    for ratio in [2.0, 1.5, 1.25, 1.0, 0.75, 0.5, 3.0, 4.0]:
        adjusted = apply_snell_at_cusps(multi_xs, ratio)
        raw_sc = true_score(bi_xs, adjusted)
        try:
            pol, _ = lbfgs_polish_bounded(adjusted, bi_xs, max_rounds=80)
            sc = true_score(bi_xs, pol)
        except Exception:
            print(f"  ratio={ratio:.2f}: raw={raw_sc:.14f}  polish failed")
            continue
        marker = " NEW BEST" if sc > best_score + 1e-13 else ""
        print(f"  ratio={ratio:.2f}: raw={raw_sc:.14f}  polished={sc:.14f}{marker}")
        if sc > best_score + 1e-13:
            best_multi = pol.copy()
            best_score = sc

    # Iterate: apply ratio 2.0, polish, repeat
    print("\n=== Iterative Snell + polish (ratio=2.0) ===")
    cur = multi_xs.copy()
    for it in range(5):
        cur = apply_snell_at_cusps(cur, 2.0)
        pol, _ = lbfgs_polish_bounded(cur, bi_xs, max_rounds=80)
        sc = true_score(bi_xs, pol)
        print(f"  iter {it}: {sc:.14f}")
        cur = pol
        if sc > best_score + 1e-13:
            best_multi = pol.copy()
            best_score = sc

    print(f"\nFinal: {best_score:.14f}")
    print(f"Gain : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-q-final")
        print("\n** IMPROVED")


if __name__ == "__main__":
    main()
