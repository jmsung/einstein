"""Random restart campaign for Thomson problem n=282.

Generates many random starting configurations, optimizes each with L-BFGS,
and tracks converged energies to map the energy landscape basin structure.

Usage:
    uv run python scripts/thomson/random_restarts.py [--minutes 5]
"""

import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
N = 282
SOTA_ENERGY = None  # loaded from results/sota_arena.json at runtime
SAVE_THRESHOLD = 37148.0
RESULTS_DIR = Path(__file__).resolve().parents[2] / "results" / "problem-10-thomson"
TIME_LIMIT_DEFAULT = 5  # minutes


# ---------------------------------------------------------------------------
# Energy & gradient (Cartesian, vectorized)
# ---------------------------------------------------------------------------

def coulomb_energy(pts: np.ndarray) -> float:
    """Coulomb energy for n points on the unit sphere."""
    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)
    idx_i, idx_j = np.triu_indices(N, k=1)
    dists = np.sqrt(dist_sq[idx_i, idx_j])
    dists = np.maximum(dists, 1e-12)
    return float(np.sum(1.0 / dists))


def coulomb_energy_and_grad_spherical(params: np.ndarray) -> tuple[float, np.ndarray]:
    """Energy and gradient in spherical coordinates (theta, phi).

    params: array of shape (2*N,) — [theta_0, ..., theta_{N-1}, phi_0, ..., phi_{N-1}]
    theta in [0, pi], phi in [0, 2*pi]
    """
    theta = params[:N]
    phi = params[N:]

    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)
    sin_phi = np.sin(phi)
    cos_phi = np.cos(phi)

    # Cartesian coordinates
    x = sin_theta * cos_phi
    y = sin_theta * sin_phi
    z = cos_theta
    pts = np.column_stack([x, y, z])

    # Pairwise differences and distances
    diff = pts[:, None, :] - pts[None, :, :]  # (N, N, 3)
    dist_sq = np.sum(diff ** 2, axis=-1)  # (N, N)
    dist_sq = np.maximum(dist_sq, 1e-24)
    dist = np.sqrt(dist_sq)  # (N, N)

    # Energy (upper triangle only)
    idx_i, idx_j = np.triu_indices(N, k=1)
    dists_upper = dist[idx_i, idx_j]
    dists_upper = np.maximum(dists_upper, 1e-12)
    energy = float(np.sum(1.0 / dists_upper))

    # Cartesian gradient: grad_i = -sum_{j!=i} (r_i - r_j) / |r_i - r_j|^3
    inv_dist3 = 1.0 / (dist_sq * dist)  # (N, N)
    np.fill_diagonal(inv_dist3, 0.0)
    grad_cart = -np.sum(diff * inv_dist3[:, :, None], axis=1)  # (N, 3)

    # Chain rule: Cartesian -> spherical
    # dx/dtheta = cos_theta * cos_phi,  dx/dphi = -sin_theta * sin_phi
    # dy/dtheta = cos_theta * sin_phi,  dy/dphi =  sin_theta * cos_phi
    # dz/dtheta = -sin_theta,           dz/dphi =  0
    grad_theta = (
        grad_cart[:, 0] * cos_theta * cos_phi
        + grad_cart[:, 1] * cos_theta * sin_phi
        - grad_cart[:, 2] * sin_theta
    )
    grad_phi = (
        grad_cart[:, 0] * (-sin_theta * sin_phi)
        + grad_cart[:, 1] * (sin_theta * cos_phi)
    )

    grad = np.concatenate([grad_theta, grad_phi])
    return energy, grad


# ---------------------------------------------------------------------------
# Random initial configuration
# ---------------------------------------------------------------------------

def random_sphere_points(n: int, rng: np.random.Generator) -> np.ndarray:
    """Generate n random unit sphere points (uniform via Gaussian projection)."""
    pts = rng.standard_normal((n, 3))
    norms = np.linalg.norm(pts, axis=1, keepdims=True)
    return pts / norms


def cartesian_to_spherical(pts: np.ndarray) -> np.ndarray:
    """Convert (N,3) Cartesian to spherical params [theta_0..N-1, phi_0..N-1]."""
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(np.clip(z / r, -1, 1))
    phi = np.arctan2(y, x) % (2 * np.pi)
    return np.concatenate([theta, phi])


def spherical_to_cartesian(params: np.ndarray) -> np.ndarray:
    """Convert spherical params to (N,3) Cartesian on unit sphere."""
    n = len(params) // 2
    theta = params[:n]
    phi = params[n:]
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.column_stack([x, y, z])


# ---------------------------------------------------------------------------
# Single restart
# ---------------------------------------------------------------------------

def run_one_restart(rng: np.random.Generator, maxiter: int = 2000) -> tuple[float, np.ndarray]:
    """Run one random restart: random init -> L-BFGS optimization."""
    pts = random_sphere_points(N, rng)
    x0 = cartesian_to_spherical(pts)

    bounds = [(0, np.pi)] * N + [(0, 2 * np.pi)] * N

    result = minimize(
        coulomb_energy_and_grad_spherical,
        x0,
        method="L-BFGS-B",
        jac=True,
        bounds=bounds,
        options={"maxiter": maxiter, "ftol": 1e-15, "gtol": 1e-10},
    )

    final_pts = spherical_to_cartesian(result.x)
    # Recompute energy with the Cartesian evaluator for consistency
    final_energy = coulomb_energy(final_pts)
    return final_energy, final_pts


# ---------------------------------------------------------------------------
# Campaign
# ---------------------------------------------------------------------------

def save_solution(pts: np.ndarray, energy: float, restart_id: int) -> Path:
    """Save a solution to JSON."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / f"solution_restart_{restart_id}.json"
    data = {
        "vectors": pts.tolist(),
        "score": energy,
        "tag": f"restart_{restart_id}",
    }
    with open(path, "w") as f:
        json.dump(data, f)
    return path


def main():
    parser = argparse.ArgumentParser(description="Random restart campaign for Thomson n=282")
    parser.add_argument("--minutes", type=float, default=TIME_LIMIT_DEFAULT,
                        help="Time limit in minutes (default: 5)")
    parser.add_argument("--maxiter", type=int, default=2000,
                        help="Max L-BFGS iterations per restart (default: 2000)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Base random seed (default: 42)")
    args = parser.parse_args()

    time_limit = args.minutes * 60
    rng = np.random.default_rng(args.seed)

    print(f"Thomson Problem n={N} — Random Restart Campaign")
    print(f"Time limit: {args.minutes} min | Max L-BFGS iter: {args.maxiter}")
    print(f"SOTA energy: {SOTA_ENERGY:.10f}")
    print(f"Save threshold: < {SAVE_THRESHOLD}")
    print("=" * 70)

    energies = []
    best_energy = float("inf")
    best_pts = None
    saved_count = 0
    start_time = time.time()

    restart_id = 0
    while time.time() - start_time < time_limit:
        t0 = time.time()
        energy, pts = run_one_restart(rng, maxiter=args.maxiter)
        dt = time.time() - t0

        energies.append(energy)
        restart_id += 1

        marker = ""
        if energy < best_energy:
            best_energy = energy
            best_pts = pts
            marker = " *** NEW BEST ***"

        if energy < SAVE_THRESHOLD:
            path = save_solution(pts, energy, restart_id)
            saved_count += 1
            marker += f" [saved: {path.name}]"

        elapsed = time.time() - start_time
        print(
            f"  #{restart_id:4d} | E = {energy:15.6f} | "
            f"best = {best_energy:15.6f} | "
            f"dt = {dt:5.1f}s | elapsed = {elapsed:5.0f}s{marker}"
        )

    total_time = time.time() - start_time
    energies_arr = np.array(energies)

    print()
    print("=" * 70)
    print("CAMPAIGN RESULTS")
    print("=" * 70)
    print(f"  Restarts completed:  {len(energies)}")
    print(f"  Total time:          {total_time:.1f}s")
    print(f"  Avg time/restart:    {total_time / len(energies):.1f}s")
    print()
    print(f"  Best energy found:   {best_energy:.10f}")
    print(f"  SOTA energy:         {SOTA_ENERGY:.10f}")
    print(f"  Gap to SOTA:         {best_energy - SOTA_ENERGY:+.10f}")
    print()
    print(f"  Solutions saved (< {SAVE_THRESHOLD}): {saved_count}")
    print()

    # Energy distribution
    print("ENERGY DISTRIBUTION (histogram):")
    print("-" * 50)

    # Create bins
    e_min, e_max = energies_arr.min(), energies_arr.max()
    n_bins = min(20, len(energies))
    if n_bins > 1:
        bin_edges = np.linspace(e_min, e_max, n_bins + 1)
        counts, _ = np.histogram(energies_arr, bins=bin_edges)
        max_count = max(counts)
        bar_width = 40

        for i in range(n_bins):
            lo, hi = bin_edges[i], bin_edges[i + 1]
            c = counts[i]
            bar = "#" * int(c / max_count * bar_width) if max_count > 0 else ""
            print(f"  [{lo:12.2f}, {hi:12.2f}) | {c:4d} | {bar}")
    else:
        print(f"  Only 1 restart: E = {energies_arr[0]:.6f}")

    print()
    print("TOP 10 LOWEST ENERGIES:")
    print("-" * 50)
    sorted_e = np.sort(energies_arr)
    for i, e in enumerate(sorted_e[:10]):
        gap = e - SOTA_ENERGY
        print(f"  {i+1:3d}. E = {e:15.6f}  (gap = {gap:+.6f})")

    print()
    print("SUMMARY STATISTICS:")
    print(f"  Mean:   {energies_arr.mean():.6f}")
    print(f"  Std:    {energies_arr.std():.6f}")
    print(f"  Min:    {energies_arr.min():.6f}")
    print(f"  Max:    {energies_arr.max():.6f}")
    print(f"  Median: {np.median(energies_arr):.6f}")

    # Identify distinct basins (cluster energies within tolerance)
    print()
    print("DISTINCT BASINS (tolerance = 1.0):")
    print("-" * 50)
    sorted_e = np.sort(energies_arr)
    basins = []
    for e in sorted_e:
        found = False
        for b in basins:
            if abs(e - b["center"]) < 1.0:
                b["count"] += 1
                b["center"] = (b["center"] * (b["count"] - 1) + e) / b["count"]
                b["min"] = min(b["min"], e)
                b["max"] = max(b["max"], e)
                found = True
                break
        if not found:
            basins.append({"center": e, "count": 1, "min": e, "max": e})

    basins.sort(key=lambda b: b["center"])
    for i, b in enumerate(basins):
        gap = b["center"] - SOTA_ENERGY
        print(
            f"  Basin {i+1:3d}: E ~ {b['center']:12.4f} | "
            f"count = {b['count']:4d} | "
            f"range = [{b['min']:.4f}, {b['max']:.4f}] | "
            f"gap = {gap:+.4f}"
        )


if __name__ == "__main__":
    main()
