"""Optimizer for Hexagon Packing (Problem 17).

Minimize outer hexagon side length for packing 12 unit hexagons.
Uses iterative Nelder-Mead with bounded iterations + hillclimb polish.

Usage:
    uv run python scripts/optimize_hexagon.py --time 300
"""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np
from scipy.optimize import minimize

from einstein.hexagon import evaluate

PENALTY = 1e6


def pack_solution(x: np.ndarray) -> dict:
    hexagons = [[float(x[3*i]), float(x[3*i+1]), float(x[3*i+2])] for i in range(12)]
    return {
        "hexagons": hexagons,
        "outer_side_length": float(x[39]),
        "outer_center": [float(x[36]), float(x[37])],
        "outer_angle_deg": float(x[38]),
    }


def unpack_solution(data: dict) -> np.ndarray:
    x = np.zeros(40)
    for i, h in enumerate(data["hexagons"]):
        x[3*i], x[3*i+1], x[3*i+2] = h[0], h[1], h[2]
    x[36], x[37] = data["outer_center"]
    x[38] = data["outer_angle_deg"]
    x[39] = data["outer_side_length"]
    return x


def objective(x: np.ndarray) -> float:
    return evaluate(pack_solution(x), penalty=PENALTY)


def log(msg: str):
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# Warm-start solutions from arena leaderboard
# ---------------------------------------------------------------------------

WARMSTARTS = {
    "SOTA_GradientExpert": {
        "hexagons": [
            [-4.1889477721133925, 1.8193659318987065, 27.152383860458485],
            [-4.176365298250621, 7.064286739333613, 267.15307297468655],
            [-2.742925127197792, 3.9063064100510863, 27.152295363759663],
            [-6.19452803077041, 4.243911804858563, 87.15309565612368],
            [-2.4736456713958086, 6.430973974132181, 27.15401730858583],
            [-3.8734691291241257, 5.273045963044315, 207.15243890310342],
            [-1.0402159579350443, 3.2730031821868337, 147.15377782773592],
            [-1.3431091093200929, 5.064242326800299, 27.153739808315176],
            [-5.891640010974447, 2.452676281499172, 207.15225576459596],
            [-4.491828745108932, 3.6105962682946204, 327.1524783972399],
            [-2.440041856362029, 2.115076005121041, 147.15240126221158],
            [-5.576170365728103, 5.90635785785185, 207.15301813652604],
        ],
        "outer_center": [-3.702741154677494, 4.263318785977133],
        "outer_angle_deg": 219.59740708327715,
        "outer_side_length": 3.9416523,
    },
    "Feynman_centered": {
        "hexagons": [
            [1.9324264405109448, 1.5728908225387235, -12.507475012489664],
            [-1.42046415542994, -2.460369342617345, -12.439022148445673],
            [-0.5120694126625385, 0.8871136507347932, -12.49227862774481],
            [1.9326360374574183, -1.5733846849024637, -12.438051019655802],
            [-2.3288464215316638, -0.8870221397195174, -12.446323927472804],
            [-0.5122139435036257, -0.8870336798138699, -12.471005605205818],
            [-1.420485932552805, 2.4599684720236734, -12.47920068782392],
            [-2.328716984746752, 0.8868905036528472, -12.467126763323762],
            [2.8406729270743205, -0.000011072703664405381, -12.483650025053635],
            [1.024280674345988, 0.00004272520464065899, -12.491946421076506],
            [0.39598805581771435, 2.460102643909715, -12.483746833557063],
            [0.3963974849066225, -2.4602798349057386, -12.423248443749372],
        ],
        "outer_center": [0, 0],
        "outer_angle_deg": 0,
        "outer_side_length": 3.9419115171115893,
    },
}


# ---------------------------------------------------------------------------
# Optimization routines
# ---------------------------------------------------------------------------

def fit_outer(data: dict, maxiter: int = 50000) -> dict:
    """Optimize only outer params (4 vars) for fixed inner hexagons."""
    inner = []
    for h in data["hexagons"]:
        inner.extend(h)

    def obj(p):
        return objective(np.array(inner + list(p)))

    p0 = [data["outer_center"][0], data["outer_center"][1],
          data["outer_angle_deg"], data["outer_side_length"]]
    res = minimize(obj, p0, method="Nelder-Mead",
                   options={"maxiter": maxiter, "xatol": 1e-15, "fatol": 1e-16})
    data["outer_center"] = [float(res.x[0]), float(res.x[1])]
    data["outer_angle_deg"] = float(res.x[2])
    data["outer_side_length"] = float(res.x[3])
    return data


def iterative_nelder_mead(x0: np.ndarray, deadline: float,
                          chunk_iters: int = 2000) -> np.ndarray:
    """Run Nelder-Mead in bounded chunks until deadline."""
    x = x0.copy()
    best = objective(x0)
    total_iters = 0

    while time.time() < deadline:
        res = minimize(objective, x, method="Nelder-Mead",
                       options={"maxiter": chunk_iters, "xatol": 1e-15,
                                "fatol": 1e-16, "adaptive": True})
        total_iters += res.nit
        if res.fun < best - 1e-14:
            best = res.fun
            x = res.x.copy()
        else:
            # Converged — no more improvement
            break

    log(f"  Nelder-Mead: {total_iters} iters, best={best:.10f}")
    return x


def hillclimb(x0: np.ndarray, deadline: float) -> np.ndarray:
    """Coordinate-wise hill-climbing with adaptive steps."""
    x = x0.copy()
    best = objective(x)
    n = len(x)
    steps = np.full(n, 1e-6)
    improvements = 0

    while time.time() < deadline:
        improved = False
        for i in range(n):
            if time.time() > deadline:
                break
            for sign in [1.0, -1.0]:
                xt = x.copy()
                xt[i] += sign * steps[i]
                s = objective(xt)
                if s < best - 1e-15:
                    x, best = xt, s
                    steps[i] *= 1.3
                    improved = True
                    improvements += 1
                    break
            else:
                steps[i] *= 0.6
        if not improved and np.max(steps) < 1e-12:
            break

    log(f"  Hillclimb: {improvements} improvements, best={best:.10f}")
    return x


def perturbation_search(x0: np.ndarray, deadline: float,
                         sigma: float = 0.005) -> np.ndarray:
    """Random perturbations + quick Nelder-Mead polish."""
    x_best = x0.copy()
    best = objective(x0)
    trials = 0

    while time.time() < deadline:
        xt = x_best.copy()
        xt[:36] += np.random.randn(36) * sigma
        xt[36:39] += np.random.randn(3) * sigma * 0.1

        res = minimize(objective, xt, method="Nelder-Mead",
                       options={"maxiter": 1000, "xatol": 1e-14, "fatol": 1e-15})
        trials += 1

        if res.fun < best - 1e-12:
            best = res.fun
            x_best = res.x.copy()
            log(f"  Perturbation {trials}: NEW BEST {best:.10f}")

    log(f"  Perturbation: {trials} trials, best={best:.10f}")
    return x_best


def random_basin_search(deadline: float) -> tuple[np.ndarray | None, float]:
    """Quick search from random configurations."""
    best_x, best_score = None, float("inf")
    trials = 0

    while time.time() < deadline:
        rng = np.random.RandomState(trials)
        x = np.zeros(40)
        # Random compact arrangement
        for i in range(12):
            r = rng.uniform(0.5, 3.5)
            theta = rng.uniform(0, 2 * np.pi)
            x[3*i] = r * np.cos(theta)
            x[3*i+1] = r * np.sin(theta)
            x[3*i+2] = rng.uniform(0, 60)
        x[39] = 6.0

        res = minimize(objective, x, method="Nelder-Mead",
                       options={"maxiter": 3000, "xatol": 1e-13, "fatol": 1e-14})
        trials += 1

        if res.fun < best_score:
            best_score = res.fun
            best_x = res.x.copy()
            valid = res.fun < 100
            if valid:
                log(f"  Basin {trials}: {res.fun:.10f}")

    log(f"  Basin search: {trials} trials, best={best_score:.10f}")
    return best_x, best_score


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=int, default=180)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    t0 = time.time()
    budget = args.time

    log("=" * 60)
    log(f"Hexagon Packing Optimizer — budget {budget}s")
    log("=" * 60)

    # Phase 1: Warm-starts with outer fitting
    log("\n--- Phase 1: Warm-starts ---")
    best_data, best_score = None, float("inf")

    for name, data in WARMSTARTS.items():
        d = dict(data, hexagons=[list(h) for h in data["hexagons"]])
        d = fit_outer(d)
        s = evaluate(d, penalty=PENALTY)
        valid = s < 100
        log(f"  {name}: {s:.10f}" + (" OK" if valid else " INVALID"))
        if s < best_score:
            best_score, best_data = s, d

    log(f"  Best: {best_score:.10f}")

    def remaining():
        return budget - (time.time() - t0)

    # Phase 2: Iterative Nelder-Mead on all 40 params
    log("\n--- Phase 2: Nelder-Mead (full) ---")
    if remaining() > 20:
        x = unpack_solution(best_data)
        dl = t0 + budget * 0.30
        x = iterative_nelder_mead(x, dl, chunk_iters=3000)
        s = objective(x)
        if s < best_score:
            best_score, best_data = s, pack_solution(x)

    # Phase 3: Perturbation search near best
    log("\n--- Phase 3: Perturbation search ---")
    if remaining() > 30:
        x = unpack_solution(best_data)
        dl = t0 + budget * 0.55
        x = perturbation_search(x, dl, sigma=0.003)
        s = objective(x)
        if s < best_score:
            best_score, best_data = s, pack_solution(x)

    # Phase 4: Basin search from random starts
    log("\n--- Phase 4: Basin search ---")
    if remaining() > 30:
        dl = t0 + budget * 0.80
        x_b, s_b = random_basin_search(dl)
        if x_b is not None and s_b < best_score:
            best_score, best_data = s_b, pack_solution(x_b)

    # Phase 5: Final hillclimb polish
    log("\n--- Phase 5: Hillclimb ---")
    if remaining() > 5:
        x = unpack_solution(best_data)
        x = hillclimb(x, t0 + budget - 2)
        s = objective(x)
        if s < best_score:
            best_score, best_data = s, pack_solution(x)

    # Report
    log("\n" + "=" * 60)
    final = evaluate(best_data, penalty=PENALTY)
    valid = final < 100
    log(f"Final: {final:.10f} ({'VALID' if valid else 'INVALID'})")
    log(f"Time:  {time.time() - t0:.1f}s")

    sota = 3.9416523
    diff = sota - final
    log(f"\nSOTA:  {sota:.10f}")
    log(f"Ours:  {final:.10f}")
    log(f"Delta: {diff:+.10f} ({'BETTER' if diff > 0 else 'WORSE'})")
    log(f"Beats minImprovement? {'YES' if diff >= 0.0001 else 'NO'}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(best_data, f, indent=2)
        log(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()
