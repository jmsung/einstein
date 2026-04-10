"""P13 push: micro-noise BH chain with diverse perturbations.

Many BH seeds with micro noise levels + bounded L-BFGS polish, plus block
shuffle and adjacent-pair-swap perturbations and periodic boundary snap.
Time-bounded 15 min.
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
)
from push_j_boundary_snap import snap_to_boundaries  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best = multi_xs.copy()
    best_score = init_score
    t0 = time.time()
    LIMIT = 900  # 15 min
    improvements = 0

    # Phase 1: micro-noise BH with block_shuffle + pair_swap
    print("\n=== Phase 1: micro-noise fine BH ===")
    for seed in range(200):
        if time.time() - t0 > LIMIT:
            break
        rng = np.random.default_rng(seed * 97 + 13)

        for noise in [0.008, 0.005, 0.003, 0.002, 0.001]:
            pert = perturb_log_gaps(best, 0.5, 0.95, noise, rng)
            try:
                pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=40)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-15:
                    best = pol.copy()
                    best_score = sc
                    improvements += 1
                    print(f"  s={seed:3d} lg n={noise:.3f}: {sc:.14f} (+{sc-init_score:.3e})")
            except Exception:
                pass

        for w in [3, 5, 10, 20, 50, 100]:
            pert = perturb_block_shuffle(best, w, rng)
            try:
                pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=40)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-15:
                    best = pol.copy()
                    best_score = sc
                    improvements += 1
                    print(f"  s={seed:3d} bs w={w:3d}:  {sc:.14f} (+{sc-init_score:.3e})")
            except Exception:
                pass

        for n in [1, 2, 3, 5, 10, 20]:
            pert = perturb_adjacent_pair_swap_or_replace(best, n, rng)
            try:
                pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=40)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-15:
                    best = pol.copy()
                    best_score = sc
                    improvements += 1
                    print(f"  s={seed:3d} ps n={n:2d}:   {sc:.14f} (+{sc-init_score:.3e})")
            except Exception:
                pass

        # Periodic snap
        if seed % 20 == 19:
            snapped = snap_to_boundaries(best, range(3, 20))
            try:
                pol, _ = lbfgs_polish_bounded(snapped, bi_xs, max_rounds=80)
                sc = true_score(bi_xs, pol)
                if sc > best_score + 1e-15:
                    best = pol.copy()
                    best_score = sc
                    improvements += 1
                    print(f"  s={seed:3d} snap: {sc:.14f} (+{sc-init_score:.3e})")
            except Exception:
                pass

    print(f"\n=== DONE ===")
    print(f"Seeds processed: {seed+1}")
    print(f"Improvements: {improvements}")
    print(f"Elapsed: {time.time()-t0:.0f}s")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-14:
        save_solution(bi_xs, best, "push-p-final")
        print("\n** IMPROVED")


if __name__ == "__main__":
    main()
