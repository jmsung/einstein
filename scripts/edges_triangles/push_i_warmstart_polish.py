"""P13 push: Re-polish all top-5 competitor solutions with bounded L-BFGS.

Previous warm-start polish used GS-based BH. Now we use bounded L-BFGS which
extracts more from each basin. Polish each competitor separately, then combine
via multi-seed BH from the best.
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
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, perturb_log_gaps, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")
WARM_DIR = RESULTS / "warm-starts"


def main():
    warm_files = sorted(WARM_DIR.glob("*.json"))
    print(f"Found {len(warm_files)} warm-starts")

    # Best from current work
    current_best = true_score(*load_xs_from_solution(RESULTS / "solution.json"))
    print(f"Current best: {current_best:.14f}")

    best_multi = None
    best_bi = None
    best_score = current_best

    for wf in warm_files:
        print(f"\n=== Polishing {wf.stem} ===")
        try:
            bi_xs, multi_xs = load_xs_from_solution(wf)
        except Exception as e:
            print(f"  Load failed: {e}")
            continue
        init = true_score(bi_xs, multi_xs)
        print(f"  Raw: {init:.14f}  ({len(bi_xs)} bipartite, {len(multi_xs)} multi)")

        # Deep polish
        polished, _ = lbfgs_polish_bounded(multi_xs, bi_xs, max_rounds=100)
        ps = true_score(bi_xs, polished)
        print(f"  Polished: {ps:.14f}  delta={ps-init:+.3e}")

        # BH from polished
        rng = np.random.default_rng(int(wf.stem.split("id")[-1][:3]) + 1)
        wbest = polished.copy()
        wscore = ps
        for seed in range(20):
            r2 = np.random.default_rng(seed * 37 + int(wf.stem.split("id")[-1][:3]))
            for noise in [0.3, 0.2, 0.12, 0.08, 0.05, 0.03, 0.015]:
                pert = perturb_log_gaps(wbest, 0.5, 0.95, noise, r2)
                try:
                    pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=30)
                    sc = true_score(bi_xs, pol)
                    if sc > wscore + 1e-13:
                        wscore = sc
                        wbest = pol.copy()
                except Exception:
                    pass
        print(f"  After BH: {wscore:.14f}  delta={wscore-ps:+.3e}")

        if wscore > best_score + 1e-13:
            best_multi = wbest.copy()
            best_bi = bi_xs.copy()
            best_score = wscore
            print(f"  *** NEW OVERALL BEST ***")

    print(f"\nFinal best: {best_score:.14f}")
    print(f"Gain vs current: {best_score - current_best:+.3e}")

    if best_multi is not None and best_score > current_best + 1e-12:
        save_solution(best_bi, best_multi, "push-i-final")
        print("** IMPROVED — saved as solution-push-i-final.json")


if __name__ == "__main__":
    main()
