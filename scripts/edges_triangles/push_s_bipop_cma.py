"""P13 push: BIPOP-CMA-ES with micro-sigma.

Council 7 diagnosis: our prior CMA-ES failed because sigma=0.05 was WAY too
large (feature scale is 1e-4). Use sigma=1e-5 instead with popsize=100,
diagonal CMA for first 100 iters, BIPOP restarts.
"""

import json
import sys
import time
from pathlib import Path

import cma
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_f_cmaes import log_gaps_to_multi, multi_to_log_gaps, objective  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    x_lo, x_hi = 0.5, 0.95
    x0 = multi_to_log_gaps(multi_xs, x_lo, x_hi)

    best_multi = multi_xs.copy()
    best_score = init_score

    # BIPOP: alternate between large and small population
    sigma0 = 1e-5  # micro-scale
    base_popsize = 100
    total_budget = 200_000  # evaluations

    # Use pycma's built-in BIPOP via cma.fmin2
    opts = {
        "popsize": base_popsize,
        "maxfevals": total_budget,
        "tolfun": 1e-18,
        "tolx": 1e-18,
        "CMA_diagonal": 100,  # diagonal first 100 iters
        "verbose": -9,
        "verb_disp": 0,
    }

    t0 = time.time()
    print(f"\n=== BIPOP-CMA-ES (sigma={sigma0}, popsize={base_popsize}, budget={total_budget}) ===")

    try:
        result = cma.fmin2(
            lambda x: objective(x, bi_xs, x_lo, x_hi),
            x0,
            sigma0,
            options=opts,
            restarts=5,
            incpopsize=2,
        )
        es = result[1]
        best_x = result[0]
        best_fit = -objective(best_x, bi_xs, x_lo, x_hi)
        print(f"Done. Total evals: {es.countevals}")
        print(f"Best CMA-ES score: {best_fit:.14f}  delta={best_fit-init_score:+.3e}")

        if best_fit > best_score + 1e-13:
            best_multi = log_gaps_to_multi(best_x, x_lo, x_hi)
            # Polish
            pol, _ = lbfgs_polish_bounded(best_multi, bi_xs, max_rounds=80)
            pol_score = true_score(bi_xs, pol)
            print(f"After polish: {pol_score:.14f}")
            if pol_score > best_score:
                best_multi = pol.copy()
                best_score = pol_score
    except Exception as e:
        print(f"BIPOP-CMA failed: {e}")
        import traceback
        traceback.print_exc()

    print(f"\nFinal: {best_score:.14f}")
    print(f"Gain : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-13:
        save_solution(bi_xs, best_multi, "push-s-final")
        print("\n** IMPROVED")


if __name__ == "__main__":
    main()
