"""P13 push: multi-start with push_k chain on each.

Tries push_k (snap + BH chain) from several starting points:
1. Current best (our solution.json)
2. Top-5 warm-starts (polished first)

Keeps the best across all.
"""

import json
import shutil
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402
from push_j_boundary_snap import snap_to_boundaries  # noqa: E402
from push_k_chain import bh_local  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")
WARM = RESULTS / "warm-starts"


def chain_one(multi_xs, bi_xs, max_iters=3, label=""):
    best = multi_xs.copy()
    best_score = true_score(bi_xs, best)
    print(f"  [{label}] start: {best_score:.14f}")

    for it in range(max_iters):
        # Snap + polish
        snapped = snap_to_boundaries(best, range(3, 20))
        pol, _ = lbfgs_polish_bounded(snapped, bi_xs, max_rounds=80)
        sc = true_score(bi_xs, pol)
        if sc > best_score + 1e-13:
            best = pol.copy()
            best_score = sc
        # BH
        bhm, bhs = bh_local(best, bi_xs, n_seeds=10, max_time=120)
        if bhs > best_score + 1e-13:
            best = bhm.copy()
            best_score = bhs
        print(f"  [{label}] iter {it}: {best_score:.14f}")

    return best, best_score


def main():
    current_bi, current_multi = load_xs_from_solution(RESULTS / "solution.json")
    current_score = true_score(current_bi, current_multi)
    print(f"Current best: {current_score:.14f}")

    # 1. Chain on current best
    print("\n=== Chain on current best ===")
    m_cur, s_cur = chain_one(current_multi, current_bi, max_iters=3, label="current")

    global_best = m_cur.copy()
    global_bi = current_bi.copy()
    global_score = s_cur
    print(f"  → {s_cur:.14f}")

    # 2. Chain on each warm-start (after initial polish)
    for wf in sorted(WARM.glob("*.json")):
        print(f"\n=== Chain on {wf.stem} ===")
        try:
            bi_ws, multi_ws = load_xs_from_solution(wf)
        except Exception as e:
            print(f"  Load failed: {e}")
            continue
        ws_init = true_score(bi_ws, multi_ws)
        print(f"  Raw: {ws_init:.14f}")

        # Polish first
        pol, _ = lbfgs_polish_bounded(multi_ws, bi_ws, max_rounds=80)
        pol_score = true_score(bi_ws, pol)
        print(f"  Polished: {pol_score:.14f}")

        # Chain
        m_ws, s_ws = chain_one(pol, bi_ws, max_iters=3, label=wf.stem[:20])
        if s_ws > global_score + 1e-13:
            global_best = m_ws.copy()
            global_bi = bi_ws.copy()
            global_score = s_ws
            print(f"  *** NEW GLOBAL BEST ***")

    print(f"\n===== DONE =====")
    print(f"Current: {current_score:.14f}")
    print(f"Final  : {global_score:.14f}")
    print(f"Gain   : {global_score - current_score:+.3e}")

    if global_score > current_score + 1e-12:
        save_solution(global_bi, global_best, "push-l-final")
        print("\n** IMPROVED — saved as solution-push-l-final.json")


if __name__ == "__main__":
    main()
