"""P13 push: scallop mass transfer + bounded polish.

The bounded L-BFGS holds each x_i inside its assigned scallop. This creates a
hard barrier against better allocations — e.g., if the optimum has 198 pts
in k=2 and 101 in k=3 (instead of our 201 and 99), bounded L-BFGS can never
find it because it can't move a point across the k=2↔k=3 boundary.

Strategy: explicitly test every (source, target) scallop transfer. Move 1 point
from source to target, redistribute both scallops uniformly, run bounded polish,
evaluate. Try 1-point, 2-point, 3-point transfers.
"""

import json
import shutil
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import assign_scallops, load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def scallop_range(k: int) -> tuple[float, float]:
    return (1.0 - 1.0 / k, 1.0 - 1.0 / (k + 1))


def redistribute_in_scallop(xs_in_scallop: np.ndarray, k: int, n_target: int) -> np.ndarray:
    """Place n_target points uniformly in scallop k's interior."""
    lo, hi = scallop_range(k)
    eps = 1e-10
    if n_target <= 0:
        return np.array([])
    return np.linspace(lo + eps, hi - eps, n_target + 2)[1:-1]  # interior n_target


def get_scallop_counts(multi_xs: np.ndarray) -> dict:
    """Return {k: count} for each scallop."""
    k_vec = assign_scallops(multi_xs)
    counts = {}
    for k in k_vec:
        counts[int(k)] = counts.get(int(k), 0) + 1
    return counts


def transfer_and_polish(
    multi_xs: np.ndarray, bi_xs: np.ndarray,
    src_k: int, dst_k: int, n_transfer: int,
) -> tuple[np.ndarray, float] | None:
    """Move n_transfer points from scallop src_k to scallop dst_k, polish."""
    counts = get_scallop_counts(multi_xs)
    if counts.get(src_k, 0) <= n_transfer + 1:  # keep at least 2 points in source
        return None
    k_vec = assign_scallops(multi_xs)

    # New allocation
    new_counts = dict(counts)
    new_counts[src_k] -= n_transfer
    new_counts[dst_k] = new_counts.get(dst_k, 0) + n_transfer

    # Reallocate: for each scallop, take CURRENT xs if count unchanged, else redistribute
    new_xs_list = []
    for k in sorted(new_counts):
        if new_counts[k] == counts.get(k, 0):
            # Keep current xs in this scallop
            mask = k_vec == k
            new_xs_list.append(multi_xs[mask])
        else:
            # Redistribute
            new_xs_list.append(redistribute_in_scallop(np.array([]), k, new_counts[k]))
    new_multi = np.sort(np.concatenate(new_xs_list))

    # Polish
    try:
        pol, _ = lbfgs_polish_bounded(new_multi, bi_xs, max_rounds=80)
        return pol, true_score(bi_xs, pol)
    except Exception:
        return None


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    counts = get_scallop_counts(multi_xs)
    print(f"Current scallop counts: {dict(sorted(counts.items()))}")

    best_multi = multi_xs.copy()
    best_score = init_score

    # Try all (src, dst) pairs for 1 point
    scallops = sorted(counts.keys())
    t0 = time.time()
    n_improvements = 0
    n_trials = 0

    for n_transfer in [1, 2, 3]:
        print(f"\n=== Transfer {n_transfer} points ===")
        for src in scallops:
            for dst in scallops:
                if src == dst:
                    continue
                if time.time() - t0 > 600:
                    print("  [time limit]")
                    break
                res = transfer_and_polish(best_multi, bi_xs, src, dst, n_transfer)
                n_trials += 1
                if res is None:
                    continue
                pol, sc = res
                if sc > best_score + 1e-13:
                    print(f"  src={src} dst={dst} n={n_transfer}: {sc:.14f} (+{sc-init_score:.3e}) NEW BEST")
                    best_multi = pol.copy()
                    best_score = sc
                    n_improvements += 1

    print(f"\nTotal trials: {n_trials}, improvements: {n_improvements}")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-n-final")
        print("** IMPROVED")


if __name__ == "__main__":
    main()
