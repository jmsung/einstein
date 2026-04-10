"""Multistart search for novel Heilbronn Triangles (n=11) basins.

Strategy: try 10+ fundamentally different initial layouts, polish each with
direct SLSQP on the full 165-triple epigraph (no softmin warmup), keep best.

Epigraph:
    max t
    s.t. signed_area_ijk(p) >= t   for all 165 triples (sign fixed from init)
         y_i >= 0
         y_i <= sqrt3 * x_i
         y_i <= sqrt3 * (1 - x_i)
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.heilbronn_triangles import (  # noqa: E402
    EQ_TRI_AREA,
    arena_score,
    all_triangle_areas,
)

N = 11
SQRT3 = math.sqrt(3.0)
TRIPLES = np.array(list(itertools.combinations(range(N), 3)), dtype=np.int64)
NT = TRIPLES.shape[0]  # 165

A_VERT = np.array([0.0, 0.0])
B_VERT = np.array([1.0, 0.0])
C_VERT = np.array([0.5, SQRT3 / 2.0])
CENTROID = (A_VERT + B_VERT + C_VERT) / 3.0


def _signed_cross_all(x):
    p = x.reshape(N, 2)
    i = TRIPLES[:, 0]
    j = TRIPLES[:, 1]
    k = TRIPLES[:, 2]
    return (
        p[i, 0] * (p[j, 1] - p[k, 1])
        + p[j, 0] * (p[k, 1] - p[i, 1])
        + p[k, 0] * (p[i, 1] - p[j, 1])
    )


def project_into_triangle(x, eps=1e-6):
    """Iterative clipping into interior with margin eps."""
    pts = x.reshape(N, 2).copy()
    for _ in range(20):
        pts[:, 1] = np.maximum(pts[:, 1], eps)
        # left edge: y <= sqrt3*x  => push if y > sqrt3*x - eps
        over = pts[:, 1] - SQRT3 * pts[:, 0] + eps
        mask = over > 0
        if mask.any():
            d = over[mask] / 4.0
            pts[mask, 0] += SQRT3 * d
            pts[mask, 1] -= d
        over = pts[:, 1] - SQRT3 * (1.0 - pts[:, 0]) + eps
        mask = over > 0
        if mask.any():
            d = over[mask] / 4.0
            pts[mask, 0] -= SQRT3 * d
            pts[mask, 1] -= d
    return pts.flatten()


def slsqp_polish(x_init, maxiter=500, ftol=1e-15):
    """Direct SLSQP epigraph polish with all 165 triple constraints.

    Returns (polished_points_flat, score).
    """
    x0 = project_into_triangle(x_init, eps=1e-6)
    cross0 = _signed_cross_all(x0)
    signs = np.sign(cross0)
    # Replace any zero signs with +1 (degenerate triangles)
    signs[signs == 0] = 1.0

    def neg_t(z):
        return -z[-1]

    def neg_t_grad(z):
        g = np.zeros_like(z)
        g[-1] = -1.0
        return g

    def tri_con(z):
        x = z[:-1]
        t = z[-1]
        cross = _signed_cross_all(x)
        return signs * cross * 0.5 - t

    def tri_jac(z):
        # ∂(signs*cross_ijk/2 - t)/∂ var
        x = z[:-1]
        pts = x.reshape(N, 2)
        J = np.zeros((NT, 2 * N + 1))
        for row, (i, j, k) in enumerate(TRIPLES):
            sgn = signs[row] * 0.5
            # p_i contributes: x_i: (y_j - y_k), y_i: (x_k - x_j)
            J[row, 2 * i] = sgn * (pts[j, 1] - pts[k, 1])
            J[row, 2 * i + 1] = sgn * (pts[k, 0] - pts[j, 0])
            J[row, 2 * j] = sgn * (pts[k, 1] - pts[i, 1])
            J[row, 2 * j + 1] = sgn * (pts[i, 0] - pts[k, 0])
            J[row, 2 * k] = sgn * (pts[i, 1] - pts[j, 1])
            J[row, 2 * k + 1] = sgn * (pts[j, 0] - pts[i, 0])
            J[row, -1] = -1.0
        return J

    def cont_con(z):
        x = z[:-1]
        p = x.reshape(N, 2)
        y_ok = p[:, 1]  # y >= 0
        left_ok = SQRT3 * p[:, 0] - p[:, 1]  # sqrt3*x - y >= 0
        right_ok = SQRT3 * (1 - p[:, 0]) - p[:, 1]  # sqrt3*(1-x) - y >= 0
        return np.concatenate([y_ok, left_ok, right_ok])

    def cont_jac(z):
        J = np.zeros((3 * N, 2 * N + 1))
        for i in range(N):
            # y_i >= 0
            J[i, 2 * i + 1] = 1.0
            # sqrt3*x_i - y_i >= 0
            J[N + i, 2 * i] = SQRT3
            J[N + i, 2 * i + 1] = -1.0
            # sqrt3*(1-x_i) - y_i >= 0
            J[2 * N + i, 2 * i] = -SQRT3
            J[2 * N + i, 2 * i + 1] = -1.0
        return J

    areas_init = np.abs(_signed_cross_all(x0)) * 0.5
    z0 = np.append(x0, areas_init.min())

    try:
        res = minimize(
            neg_t,
            z0,
            jac=neg_t_grad,
            method="SLSQP",
            constraints=[
                {"type": "ineq", "fun": tri_con, "jac": tri_jac},
                {"type": "ineq", "fun": cont_con, "jac": cont_jac},
            ],
            options={"maxiter": maxiter, "ftol": ftol},
        )
        x = res.x[:-1]
    except Exception:
        x = x0
    # Final project to be safe
    x = project_into_triangle(x, eps=1e-13)
    pts = x.reshape(N, 2)
    s = arena_score(pts)
    return pts, s


# ================== Initialization strategies ==================


def init_random_uniform(seed):
    rng = np.random.default_rng(seed)
    pts = []
    while len(pts) < N:
        x = rng.uniform(0, 1)
        y = rng.uniform(0, SQRT3 / 2)
        if y <= SQRT3 * x and y <= SQRT3 * (1 - x):
            pts.append([x, y])
    return np.array(pts, dtype=np.float64).flatten()


def init_corners_3(seed, jitter=0.0):
    rng = np.random.default_rng(seed)
    pts = [
        [0.01, 0.01 * SQRT3 / 2],
        [0.99, 0.01 * SQRT3 / 2],
        [0.5, SQRT3 / 2 - 0.01],
    ]
    while len(pts) < N:
        x = rng.uniform(0.05, 0.95)
        y = rng.uniform(0.02, SQRT3 / 2 - 0.02)
        if y <= SQRT3 * x - 0.02 and y <= SQRT3 * (1 - x) - 0.02:
            pts.append([x, y])
    pts = np.array(pts)
    if jitter > 0:
        pts += jitter * rng.standard_normal(pts.shape)
    return pts.flatten()


def init_corners_1(seed):
    rng = np.random.default_rng(seed)
    pts = [[0.01, 0.01 * SQRT3 / 2]]  # 1 corner
    while len(pts) < N:
        x = rng.uniform(0.05, 0.95)
        y = rng.uniform(0.02, SQRT3 / 2 - 0.02)
        if y <= SQRT3 * x - 0.02 and y <= SQRT3 * (1 - x) - 0.02:
            pts.append([x, y])
    return np.array(pts).flatten()


def init_corners_2(seed):
    rng = np.random.default_rng(seed)
    pts = [[0.01, 0.01 * SQRT3 / 2], [0.99, 0.01 * SQRT3 / 2]]
    while len(pts) < N:
        x = rng.uniform(0.05, 0.95)
        y = rng.uniform(0.02, SQRT3 / 2 - 0.02)
        if y <= SQRT3 * x - 0.02 and y <= SQRT3 * (1 - x) - 0.02:
            pts.append([x, y])
    return np.array(pts).flatten()


def init_d3_symmetric(seed):
    rng = np.random.default_rng(seed)
    # Centroid + 3 orbits of 3 points = 10, plus 1 extra near centroid
    pts = [list(CENTROID)]
    r1 = 0.15 + rng.uniform(-0.05, 0.05)
    r2 = 0.28 + rng.uniform(-0.05, 0.05)
    r3 = 0.40 + rng.uniform(-0.02, 0.02)
    phase1 = rng.uniform(0, 2 * math.pi / 3)
    phase2 = rng.uniform(0, 2 * math.pi / 3)
    phase3 = rng.uniform(0, 2 * math.pi / 3)
    for (rr, ph) in [(r1, phase1), (r2, phase2), (r3, phase3)]:
        for k in range(3):
            a = ph + k * 2 * math.pi / 3
            pts.append([CENTROID[0] + rr * math.cos(a),
                        CENTROID[1] + rr * math.sin(a)])
    # 1 extra slightly off-center
    pts.append([CENTROID[0] + 0.02 * rng.uniform(-1, 1),
                CENTROID[1] + 0.02 * rng.uniform(-1, 1)])
    return np.array(pts).flatten()


def init_lattice(seed):
    rng = np.random.default_rng(seed)
    candidates = []
    step = 0.18 + rng.uniform(-0.03, 0.03)
    for i in range(15):
        for j in range(15):
            x = 0.08 + i * step + (j % 2) * step / 2
            y = 0.08 + j * step * SQRT3 / 2
            if y <= SQRT3 * x - 0.02 and y <= SQRT3 * (1 - x) - 0.02:
                candidates.append([x, y])
    candidates = np.array(candidates)
    if len(candidates) < N:
        return init_random_uniform(seed)
    idx = rng.choice(len(candidates), N, replace=False)
    pts = candidates[idx] + 0.01 * rng.standard_normal((N, 2))
    return pts.flatten()


def init_2_2_2(seed):
    """CHRONOS-like: 2 on each edge + 5 interior."""
    rng = np.random.default_rng(seed)
    pts = []
    # 2 on bottom
    for t in [0.3, 0.7]:
        pts.append([t + rng.uniform(-0.1, 0.1), 0.02])
    # 2 on left
    for t in [0.3, 0.7]:
        x_e = t * 0.5
        y_e = t * SQRT3 / 2
        pts.append([x_e + 0.02, y_e - 0.035])
    # 2 on right
    for t in [0.3, 0.7]:
        x_e = 1 - t * 0.5
        y_e = t * SQRT3 / 2
        pts.append([x_e - 0.02, y_e - 0.035])
    # 5 interior
    for _ in range(5):
        while True:
            x = rng.uniform(0.15, 0.85)
            y = rng.uniform(0.1, SQRT3 / 2 - 0.1)
            if y <= SQRT3 * x - 0.05 and y <= SQRT3 * (1 - x) - 0.05:
                pts.append([x, y])
                break
    return np.array(pts).flatten()


def init_3_3_3(seed):
    """3 points on each edge + 2 interior."""
    rng = np.random.default_rng(seed)
    pts = []
    for t in [0.2, 0.5, 0.8]:
        pts.append([t + rng.uniform(-0.05, 0.05), 0.02])
    for t in [0.2, 0.5, 0.8]:
        pts.append([t * 0.5 + 0.02, t * SQRT3 / 2 - 0.035])
    for t in [0.2, 0.5, 0.8]:
        pts.append([1 - t * 0.5 - 0.02, t * SQRT3 / 2 - 0.035])
    for _ in range(2):
        while True:
            x = rng.uniform(0.2, 0.8)
            y = rng.uniform(0.1, SQRT3 / 2 - 0.1)
            if y <= SQRT3 * x - 0.05 and y <= SQRT3 * (1 - x) - 0.05:
                pts.append([x, y])
                break
    return np.array(pts).flatten()


def init_perturbed_chronos(seed, sigma=0.05):
    rng = np.random.default_rng(seed)
    chr_path = Path("results/problem-15-heilbronn-triangles/rank01_CHRONOS_0.0365298898800302.json")
    pts = np.array(json.loads(chr_path.read_text())["data"]["points"], dtype=np.float64)
    pts = pts + sigma * rng.standard_normal(pts.shape)
    return pts.flatten()


def init_rotated_chronos(seed):
    """Rotate CHRONOS #1 by a random angle (not D3 multiple), shift inward."""
    rng = np.random.default_rng(seed)
    chr_path = Path("results/problem-15-heilbronn-triangles/rank01_CHRONOS_0.0365298898800302.json")
    pts = np.array(json.loads(chr_path.read_text())["data"]["points"], dtype=np.float64)
    angle = rng.uniform(0, 2 * math.pi)
    cos = math.cos(angle)
    sin = math.sin(angle)
    cx, cy = CENTROID
    rotated = np.zeros_like(pts)
    for i in range(N):
        dx = pts[i, 0] - cx
        dy = pts[i, 1] - cy
        rotated[i, 0] = cx + cos * dx - sin * dy
        rotated[i, 1] = cy + sin * dx + cos * dy
    return rotated.flatten()


def init_reflected_chronos(seed):
    chr_path = Path("results/problem-15-heilbronn-triangles/rank01_CHRONOS_0.0365298898800302.json")
    pts = np.array(json.loads(chr_path.read_text())["data"]["points"], dtype=np.float64)
    pts[:, 0] = 1.0 - pts[:, 0]  # reflection across the vertical axis
    return pts.flatten()


STRATEGIES = {
    "random_uniform": init_random_uniform,
    "corners_1": init_corners_1,
    "corners_2": init_corners_2,
    "corners_3": init_corners_3,
    "2_2_2": init_2_2_2,
    "3_3_3": init_3_3_3,
    "d3_symmetric": init_d3_symmetric,
    "lattice": init_lattice,
    "perturbed_chronos": lambda s: init_perturbed_chronos(s, sigma=0.05),
    "heavy_perturbed_chronos": lambda s: init_perturbed_chronos(s, sigma=0.15),
    "rotated_chronos": init_rotated_chronos,
    "reflected_chronos": init_reflected_chronos,
}


def run_trial(strategy, seed):
    init_fn = STRATEGIES[strategy]
    try:
        x_init = init_fn(seed)
        # Safety: ensure 11 points (22 values)
        if x_init.size != 22:
            return None, -float("inf"), f"init_wrong_size: {x_init.size}"
    except Exception as e:
        return None, -float("inf"), f"init_failed: {e}"
    try:
        pts, s = slsqp_polish(x_init)
    except Exception as e:
        return None, -float("inf"), f"polish_failed: {e}"
    return pts, s, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--time", type=float, default=300.0)
    ap.add_argument("--strategies", default="all")
    ap.add_argument("--seed-start", type=int, default=0)
    ap.add_argument("--save-threshold", type=float, default=0.03652988988003)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    strats = list(STRATEGIES.keys()) if args.strategies == "all" else args.strategies.split(",")

    t0 = time.time()
    best_score = -float("inf")
    best_pts = None
    best_strat = None
    results = {k: {"trials": 0, "best": -float("inf"), "best_pts": None} for k in strats}
    trial = 0
    seed = args.seed_start

    while time.time() - t0 < args.time:
        for strat in strats:
            if time.time() - t0 > args.time:
                break
            pts, s, err = run_trial(strat, seed + trial)
            trial += 1
            if err:
                continue
            results[strat]["trials"] += 1
            if s > results[strat]["best"]:
                results[strat]["best"] = s
                results[strat]["best_pts"] = pts
            marker = ""
            if s > best_score:
                best_score = s
                best_pts = pts
                best_strat = strat
                marker = " ★"
            if not args.quiet:
                print(
                    f"[{time.time() - t0:6.1f}s] t{trial:4d} {strat:22s} "
                    f"s={s:.17g}{marker}",
                    flush=True,
                )
        seed += 1

    print("\n=== Summary ===")
    print(f"Target (CHRONOS #1): 0.036529889880030156")
    print(f"Best found:          {best_score!r}  via {best_strat}")
    print(f"Delta:               {best_score - 0.036529889880030156:+.3e}")
    print("\nPer-strategy bests (sorted):")
    for strat, r in sorted(results.items(), key=lambda kv: -kv[1]["best"]):
        print(f"  {strat:24s}  trials={r['trials']:4d}  best={r['best']:.17g}")

    if best_pts is not None and best_score >= args.save_threshold:
        outdir = Path("results/problem-15-heilbronn-triangles")
        outdir.mkdir(parents=True, exist_ok=True)
        fn = outdir / f"multistart_best_{best_score:.15g}.json"
        fn.write_text(json.dumps({"points": best_pts.tolist()}, indent=2))
        print(f"\nSaved best to {fn}")


if __name__ == "__main__":
    main()
