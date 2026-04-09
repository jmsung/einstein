"""Apollonian pocket swap for Circle Packing in Square (P14, n=26).

Conway's deterministic technique:
1. Find every triangular pocket in AE's contact graph (3 mutually-tangent circles).
2. For each pocket, compute the inner Soddy circle radius via Descartes' theorem:
       k_4 = k_1 + k_2 + k_3 + 2*sqrt(k_1*k_2 + k_2*k_3 + k_3*k_1)
   where k_i = 1/r_i (curvature). The Soddy circle is in the gap between the 3.
3. If r_Soddy > r_min (smallest circle in AE), this pocket is a swap candidate:
   delete smallest circle from AE, insert a circle near the Soddy center.
4. Re-polish with SLSQP. The new contact graph differs → potentially a NEW basin
   with sum strictly above AE.
"""

from __future__ import annotations

import argparse
import json
import math
import multiprocessing as mp
import time
from pathlib import Path

import networkx as nx
import numpy as np


def find_triangular_pockets(circles: np.ndarray, contacts: list[tuple[int, int]]):
    """Build planar graph + identify triangular faces."""
    n = len(circles)
    G = nx.Graph()
    for i in range(n):
        G.add_node(i)
    for i, j in contacts:
        G.add_edge(i, j)

    is_planar, embedding = nx.check_planarity(G)
    if not is_planar:
        return []

    visited = set()
    faces = []
    for v in embedding.nodes:
        for u in embedding.neighbors_cw_order(v):
            if (v, u) not in visited:
                face = embedding.traverse_face(v, u)
                for k in range(len(face)):
                    visited.add((face[k], face[(k + 1) % len(face)]))
                faces.append(face)

    triangles = [f for f in faces if len(f) == 3]
    return triangles


def soddy_inner_circle(c1, c2, c3):
    """Compute inner Soddy circle (smaller, in the gap) of 3 mutually tangent circles.

    Returns (cx, cy, r) of the inscribed Soddy circle, or None if invalid.
    Uses Descartes' theorem + complex coordinate formulation for the center.
    """
    k1, k2, k3 = 1.0 / c1[2], 1.0 / c2[2], 1.0 / c3[2]
    disc = k1 * k2 + k2 * k3 + k3 * k1
    if disc < 0:
        return None
    sqrt_disc = math.sqrt(disc)
    # Inner Soddy = + sign (smaller circle in the gap)
    k4 = k1 + k2 + k3 + 2 * sqrt_disc
    if k4 <= 0:
        return None
    r4 = 1.0 / k4

    # Center via complex Descartes (Larmor):
    # z_4 * k_4 = z_1*k_1 + z_2*k_2 + z_3*k_3 + 2*sqrt(k_1*k_2*z_1*z_2 + k_2*k_3*z_2*z_3 + k_3*k_1*z_3*z_1)
    z1 = complex(c1[0], c1[1])
    z2 = complex(c2[0], c2[1])
    z3 = complex(c3[0], c3[1])
    inner = k1 * k2 * z1 * z2 + k2 * k3 * z2 * z3 + k3 * k1 * z3 * z1
    z4 = (z1 * k1 + z2 * k2 + z3 * k3 + 2 * np.sqrt(inner)) / k4

    return (float(z4.real), float(z4.imag), r4)


def verify_inscribed(cx, cy, r, all_circles, n_skip=None):
    """Check if a candidate Soddy circle is feasible (in square, not overlapping)."""
    if r <= 0:
        return False
    # Inside square
    if cx - r < -1e-12 or cx + r > 1 + 1e-12:
        return False
    if cy - r < -1e-12 or cy + r > 1 + 1e-12:
        return False
    # Not overlapping with any existing circle (except optionally one being removed)
    for k, c in enumerate(all_circles):
        if n_skip is not None and k == n_skip:
            continue
        d = math.hypot(cx - c[0], cy - c[1])
        if d + 1e-9 < r + c[2]:
            return False
    return True


def worker(args):
    seed, base_circles, swap_idx, soddy_pos = args
    import numpy as np
    from einstein.circle_packing_square import N_CIRCLES, evaluate
    from einstein.circle_packing_square.polish import polish

    rng = np.random.default_rng(seed)
    base = np.array(base_circles, dtype=np.float64).copy()

    # Replace circle at swap_idx with Soddy candidate
    base[swap_idx] = list(soddy_pos)

    # Tiny jitter to break degeneracy
    base[:, :2] += rng.normal(0, 1e-4, (N_CIRCLES, 2))
    base[:, 0] = np.clip(base[:, 0], base[:, 2], 1.0 - base[:, 2])
    base[:, 1] = np.clip(base[:, 1], base[:, 2], 1.0 - base[:, 2])

    # Polish cascade
    cur = base
    best_score = -1.0
    best_c = None
    for slack in (1e-4, 1e-6, 1e-8, 1e-10):
        try:
            new, _ = polish(cur, method="SLSQP", ftol=1e-16, maxiter=2000, overlap_slack=slack)
            try:
                s = evaluate({"circles": new.tolist()}, tol=1e-9)
                if s > best_score:
                    best_score = s
                    best_c = new.copy()
                cur = new
            except Exception:
                pass
        except Exception:
            break
    if best_c is None:
        return None
    return (seed, swap_idx, best_score, best_c.tolist())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", type=str, default="results-temp/p14_top.json")
    p.add_argument("--workers", type=int, default=None)
    p.add_argument("--n-jitter-per-pocket", type=int, default=8)
    p.add_argument("--output", type=str, default="results-temp/p14_apollonian.json")
    args = p.parse_args()

    workers = args.workers or max(1, mp.cpu_count() - 1)
    print(f"Workers: {workers}")

    with open(args.base) as f:
        data = json.load(f)
    if isinstance(data, list) and data:
        base = np.array(data[0]["data"]["circles"], dtype=np.float64)
    elif isinstance(data, dict) and "circles" in data:
        base = np.array(data["circles"], dtype=np.float64)
    else:
        raise ValueError("Unknown base format")

    print(f"Base sum_r: {base[:,2].sum():.16f}")

    # Identify contacts
    n = len(base)
    contacts = []
    for i in range(n):
        for j in range(i + 1, n):
            d = math.hypot(base[i, 0] - base[j, 0], base[i, 1] - base[j, 1])
            if abs(d - base[i, 2] - base[j, 2]) < 1e-9:
                contacts.append((i, j))
    print(f"Contacts: {len(contacts)}")

    # Find triangular pockets
    triangles = find_triangular_pockets(base, contacts)
    print(f"Triangular faces: {len(triangles)}")

    # For each triangle, compute Soddy
    soddy_candidates = []
    for tri in triangles:
        c1 = base[tri[0]]
        c2 = base[tri[1]]
        c3 = base[tri[2]]
        soddy = soddy_inner_circle(c1, c2, c3)
        if soddy is None:
            continue
        cx, cy, r = soddy
        if verify_inscribed(cx, cy, r, base):
            soddy_candidates.append((tri, cx, cy, r))

    soddy_candidates.sort(key=lambda x: -x[3])
    print(f"Feasible Soddy circles: {len(soddy_candidates)}")
    print()
    print("Top 10 Soddy radii (vs smallest in AE = {:.6f}):".format(min(base[:, 2])))
    smallest_idx = int(np.argmin(base[:, 2]))
    smallest_r = base[smallest_idx, 2]
    for tri, cx, cy, r in soddy_candidates[:10]:
        print(f"  triangle {tri} → Soddy r={r:.6f}, gain={r-smallest_r:+.4e}")

    # Build swap tasks
    rng = np.random.default_rng(0)
    tasks = []
    AE = base[:, 2].sum()

    # For each pocket where Soddy radius > smallest_r, swap candidate
    n_promising = sum(1 for _, _, _, r in soddy_candidates if r > smallest_r)
    print(f"\nPromising pockets (r_Soddy > r_min): {n_promising}")

    for tri, cx, cy, r in soddy_candidates:
        # Even if r <= smallest_r, still try — maybe the polish moves things around
        for jit in range(args.n_jitter_per_pocket):
            tasks.append((10000 + jit, base.tolist(), smallest_idx, (cx, cy, r)))

    # Also try swapping each non-smallest circle (might give a different basin)
    print(f"\nTotal tasks: {len(tasks)}")

    if not tasks:
        print("No tasks to run")
        return

    t0 = time.time()
    best_score = AE
    best_c = base.tolist()
    n_done = 0

    with mp.Pool(workers) as pool:
        for result in pool.imap_unordered(worker, tasks):
            n_done += 1
            if result is None:
                continue
            seed, swap_idx, score, circles = result
            if score > best_score + 1e-13:
                best_score = score
                best_c = circles
                elapsed = time.time() - t0
                marker = " <<< above AE!" if score > AE else ""
                print(f"  seed={seed} swap=c{swap_idx} score={score:.16f} d_AE={score-AE:+.3e} ({elapsed:.1f}s){marker}", flush=True)
            if n_done % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ...{n_done}/{len(tasks)} done, best={best_score:.16f}, {elapsed:.1f}s", flush=True)

    print(f"\nFinal: best={best_score:.16f}  d_AE={best_score-AE:+.3e}")
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump({
            "base_score": AE,
            "best_score": best_score,
            "best_circles": best_c,
        }, f, indent=2)
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
