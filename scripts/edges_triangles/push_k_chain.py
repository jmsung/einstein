"""P13 push: iterative snap + BH chain until convergence.

Cycle: snap-to-boundary → BH-polish → snap → BH → ... until no more gains.
Also tries multi-point snapping (snap 2 points per boundary).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, perturb_log_gaps, save_solution, true_score  # noqa: E402
from push_h_aggressive import (  # noqa: E402
    perturb_adjacent_pair_swap_or_replace,
    perturb_block_shuffle,
    perturb_point_move,
)
from push_j_boundary_snap import insert_boundary_points, snap_to_boundaries  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def snap_and_polish(multi_xs, bi_xs, k_range):
    snapped = snap_to_boundaries(multi_xs, k_range)
    pol, _ = lbfgs_polish_bounded(snapped, bi_xs, max_rounds=80)
    return pol, true_score(bi_xs, pol)


def bh_local(multi_xs, bi_xs, n_seeds=20, max_time=120) -> tuple[np.ndarray, float]:
    """Fast BH with mixed strategies."""
    best = multi_xs.copy()
    best_score = true_score(bi_xs, best)
    t0 = time.time()
    for seed in range(n_seeds):
        if time.time() - t0 > max_time:
            break
        rng = np.random.default_rng(seed * 73 + 29)
        # Mix of perturbation strategies
        for strategy in [
            ("bs", {"w": 3}), ("bs", {"w": 5}), ("bs", {"w": 10}), ("bs", {"w": 20}),
            ("ps", {"n": 1}), ("ps", {"n": 5}), ("pm", {"n": 1}),
            ("lg", {"noise": 0.08}), ("lg", {"noise": 0.03}),
        ]:
            if strategy[0] == "bs":
                pert = perturb_block_shuffle(best, strategy[1]["w"], rng)
            elif strategy[0] == "ps":
                pert = perturb_adjacent_pair_swap_or_replace(best, strategy[1]["n"], rng)
            elif strategy[0] == "pm":
                pert = perturb_point_move(best, strategy[1]["n"], rng)
            elif strategy[0] == "lg":
                pert = perturb_log_gaps(best, 0.5, 0.95, strategy[1]["noise"], rng)
            try:
                pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=30)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-14:
                    best = pol.copy()
                    best_score = sc
            except Exception:
                pass
    return best, best_score


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best_multi = multi_xs.copy()
    best_score = init_score

    MAX_ITERS = 8
    for it in range(MAX_ITERS):
        print(f"\n=== Chain iter {it} (best so far {best_score:.14f}) ===")

        # Phase A: fresh snap (all boundaries)
        s_multi, s_score = snap_and_polish(best_multi, bi_xs, range(3, 20))
        gain_a = s_score - best_score
        print(f"  snap all   : {s_score:.14f} (delta={gain_a:+.3e})")
        if s_score > best_score + 1e-13:
            best_multi = s_multi.copy()
            best_score = s_score

        # Phase B: BH from current best
        bh_multi, bh_score = bh_local(best_multi, bi_xs, n_seeds=15, max_time=180)
        gain_b = bh_score - best_score
        print(f"  bh         : {bh_score:.14f} (delta={gain_b:+.3e})")
        if bh_score > best_score + 1e-13:
            best_multi = bh_multi.copy()
            best_score = bh_score

        # Phase C: try partial snap + bh
        for k_set in [range(3, 10), range(10, 20)]:
            ks_multi, ks_score = snap_and_polish(best_multi, bi_xs, k_set)
            ksm, kss = bh_local(ks_multi, bi_xs, n_seeds=8, max_time=90)
            gain = kss - best_score
            print(f"  snap {list(k_set)[0]}-{list(k_set)[-1]} + bh: {kss:.14f} (delta={gain:+.3e})")
            if kss > best_score + 1e-13:
                best_multi = ksm.copy()
                best_score = kss

        # Converged?
        if gain_a + gain_b < 1e-11:
            print(f"\nConverged at iter {it}")
            break

    print(f"\n===== DONE =====")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-12:
        save_solution(bi_xs, best_multi, "push-k-final")
        print("\n** IMPROVED — saved")


if __name__ == "__main__":
    main()
