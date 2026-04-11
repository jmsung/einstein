"""High-precision KKT solver for Circles in Rectangle (n=21).

The strict-disjoint SLSQP optimum has exactly 64 active constraints for
64 variables (0 DOF). This means the configuration is uniquely determined
by the active set. We solve the constraint equations in mpmath (50+ digits)
then round to float64 — the result may be above capybara's score if SLSQP
lost precision in the float64 constraint satisfaction.

Usage:
    uv run python scripts/circles_rectangle/kkt_solve.py
"""

from __future__ import annotations

import json
from pathlib import Path

import mpmath
import numpy as np

mpmath.mp.dps = 80  # 80 decimal digits

RESULTS_DIR = Path("results/problem-17-circles-rectangle")
CAPYBARA_SCORE = 2.3658323759185156


def solve_kkt():
    """Solve the fully-determined constraint system in high precision."""
    with open(RESULTS_DIR / "kkt_config.json") as f:
        config = json.load(f)

    n = config["n"]
    active_pairs = [tuple(p) for p in config["active_pairs"]]
    active_walls = [(w[0], w[1]) for w in config["active_walls"]]
    x0_np = np.array(config["x0"])
    w_init = config["width_init"]

    # Variables: cx_0, cy_0, r_0, cx_1, cy_1, r_1, ..., cx_20, cy_20, r_20, w
    # Total: 64 variables
    n_vars = 3 * n + 1

    # Convert initial guess to mpmath
    x0 = [mpmath.mpf(str(x0_np[i // 3, i % 3])) if i < 3 * n
           else mpmath.mpf(str(w_init))
           for i in range(n_vars)]

    def get_circle(x, i):
        """Return (cx, cy, r) for circle i."""
        return x[3*i], x[3*i+1], x[3*i+2]

    def equations(x):
        """64 constraint equations that must equal zero at the solution."""
        eqs = []
        w = x[3 * n]
        h = mpmath.mpf(2) - w

        # Pair constraints: ||c_i - c_j|| - (r_i + r_j) = 0
        for i, j in active_pairs:
            cx_i, cy_i, r_i = get_circle(x, i)
            cx_j, cy_j, r_j = get_circle(x, j)
            dx = cx_i - cx_j
            dy = cy_i - cy_j
            # Use squared form to avoid sqrt: d^2 - (r_i+r_j)^2 = 0
            eqs.append(dx*dx + dy*dy - (r_i + r_j)**2)

        # Wall constraints
        for idx, wall_type in active_walls:
            cx, cy, r = get_circle(x, idx)
            if wall_type == 'L':    # cx - r = 0
                eqs.append(cx - r)
            elif wall_type == 'R':  # w - cx - r = 0
                eqs.append(w - cx - r)
            elif wall_type == 'B':  # cy - r = 0
                eqs.append(cy - r)
            elif wall_type == 'T':  # h - cy - r = 0
                eqs.append(h - cy - r)

        return eqs

    print(f"Solving {len(active_pairs)} pair + {len(active_walls)} wall = {n_vars} equations")
    print(f"Precision: {mpmath.mp.dps} decimal digits")
    print(f"Initial score (SLSQP float64): {sum(float(x0[3*i+2]) for i in range(n)):.18f}")
    print()

    # Newton iteration
    from mpmath import matrix, lu_solve, norm

    x = matrix(x0)
    max_iter = 100

    for iteration in range(max_iter):
        # Evaluate equations
        x_list = [x[i] for i in range(n_vars)]
        F = equations(x_list)
        F_mat = matrix(F)
        residual = float(norm(F_mat, 2))

        # Score
        score_mp = sum(x_list[3*i+2] for i in range(n))

        if iteration % 5 == 0 or residual < 1e-60:
            print(f"  iter {iteration:3d}: residual={residual:.4e}  score={mpmath.nstr(score_mp, 25)}")

        if residual < mpmath.mpf(10)**(-70):
            print(f"\n  Converged at iter {iteration}!")
            break

        # Compute Jacobian numerically
        eps = mpmath.mpf(10)**(-60)
        J = mpmath.matrix(n_vars, n_vars)
        for j in range(n_vars):
            x_plus = [x[i] for i in range(n_vars)]
            x_plus[j] += eps
            F_plus = equations(x_plus)
            for i in range(n_vars):
                J[i, j] = (F_plus[i] - F[i]) / eps

        # Newton step: J * dx = -F
        try:
            dx = lu_solve(J, -F_mat)
            # Damped step
            alpha = mpmath.mpf(1)
            for _ in range(10):
                x_trial = matrix([x[i] + alpha * dx[i] for i in range(n_vars)])
                F_trial = equations([x_trial[i] for i in range(n_vars)])
                if float(norm(matrix(F_trial), 2)) < residual:
                    break
                alpha /= 2
            x = x_trial
        except Exception as e:
            print(f"  LU solve failed at iter {iteration}: {e}")
            break

    # Extract solution
    x_final = [x[i] for i in range(n_vars)]
    w_final = x_final[3*n]
    h_final = mpmath.mpf(2) - w_final

    # Compute score in high precision
    score_hp = sum(x_final[3*i+2] for i in range(n))
    print(f"\nHigh-precision score: {mpmath.nstr(score_hp, 40)}")
    print(f"Width:               {mpmath.nstr(w_final, 40)}")
    print(f"Height:              {mpmath.nstr(h_final, 40)}")

    # Round to float64
    circles_f64 = np.zeros((n, 3))
    for i in range(n):
        circles_f64[i, 0] = float(x_final[3*i])
        circles_f64[i, 1] = float(x_final[3*i+1])
        circles_f64[i, 2] = float(x_final[3*i+2])

    score_f64 = float(np.sum(circles_f64[:, 2]))
    w_f64 = float(w_final)

    print(f"\nFloat64 score:       {score_f64:.18f}")
    print(f"Float64 width:       {w_f64:.18f}")
    print(f"Capybara score:      {CAPYBARA_SCORE:.18f}")
    print(f"Δ vs capybara:       {score_f64 - CAPYBARA_SCORE:+.4e}")

    # Verify strict disjointness in float64
    worst_gap = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            d = np.sqrt((circles_f64[i,0]-circles_f64[j,0])**2 +
                       (circles_f64[i,1]-circles_f64[j,1])**2)
            gap = d - circles_f64[i,2] - circles_f64[j,2]
            worst_gap = min(worst_gap, gap)

    h_f64 = 2.0 - w_f64
    perim = 2 * (w_f64 + h_f64)
    print(f"\nFloat64 worst gap:   {worst_gap:.4e}  ({'DISJOINT' if worst_gap >= 0 else 'OVERLAP'})")
    print(f"Float64 perimeter:   {perim:.18f}")

    if score_f64 > CAPYBARA_SCORE and worst_gap >= 0:
        print("\n*** STRICTLY DISJOINT SOLUTION BEATS CAPYBARA! ***")
        sol = {"circles": circles_f64.tolist()}
        out = RESULTS_DIR / "solution-kkt-strict.json"
        with open(out, "w") as f:
            json.dump(sol, f, indent=2)
        print(f"Saved to {out}")
    elif score_f64 > CAPYBARA_SCORE:
        print(f"\n*** Score beats capybara but has overlap {worst_gap:.4e} ***")
        # Try rounding radii DOWN by 1 ULP to eliminate overlap
        circles_safe = circles_f64.copy()
        circles_safe[:, 2] = np.nextafter(circles_safe[:, 2], 0)  # round down by 1 ULP
        score_safe = float(np.sum(circles_safe[:, 2]))
        worst_safe = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                d = np.sqrt((circles_safe[i,0]-circles_safe[j,0])**2 +
                           (circles_safe[i,1]-circles_safe[j,1])**2)
                gap = d - circles_safe[i,2] - circles_safe[j,2]
                worst_safe = min(worst_safe, gap)
        print(f"After 1-ULP radius shrink: score={score_safe:.18f}  gap={worst_safe:.4e}")
        if score_safe > CAPYBARA_SCORE and worst_safe >= 0:
            print("*** SAFE SOLUTION BEATS CAPYBARA! ***")
            sol = {"circles": circles_safe.tolist()}
            out = RESULTS_DIR / "solution-kkt-safe.json"
            with open(out, "w") as f:
                json.dump(sol, f, indent=2)
            print(f"Saved to {out}")
    else:
        print(f"\nStrict-disjoint score {score_f64:.18f} is below capybara.")
        print("The basin floor in exact arithmetic is below capybara's float64-noise score.")


if __name__ == "__main__":
    solve_kkt()
