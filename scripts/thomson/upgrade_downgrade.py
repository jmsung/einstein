"""Upgrade/Downgrade algorithm for Thomson problem n=282.

Based on arXiv:2506.08398:
- Upgrade: Take optimal n=281, insert best 282nd point, optimize
- Downgrade: Take optimal n=283, remove best point, optimize

Uses Wales Cambridge database for neighboring configurations.
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
from scipy.optimize import minimize as scipy_minimize
from scipy.spatial import SphericalVoronoi

RESULTS_DIR = Path("results/problem-10-thomson")
SOTA_ENERGY = 37147.29441846226
N = 282


# ---------------------------------------------------------------------------
# Core energy / gradient routines
# ---------------------------------------------------------------------------

def normalize(pts: np.ndarray) -> np.ndarray:
    """Project points onto unit sphere."""
    norms = np.linalg.norm(pts, axis=1, keepdims=True)
    return pts / norms


def coulomb_energy(pts: np.ndarray) -> float:
    """Compute Coulomb energy (vectorized)."""
    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)
    n = len(pts)
    idx_i, idx_j = np.triu_indices(n, k=1)
    dists = np.sqrt(dist_sq[idx_i, idx_j])
    dists = np.maximum(dists, 1e-12)
    return float(np.sum(1.0 / dists))


def coulomb_gradient(pts: np.ndarray) -> np.ndarray:
    """Gradient of Coulomb energy: dE/dp_i = -sum_{j!=i} (p_i-p_j)/||p_i-p_j||^3."""
    diff = pts[:, None, :] - pts[None, :, :]  # (n, n, 3)
    dist_sq = np.sum(diff ** 2, axis=-1, keepdims=True)  # (n, n, 1)
    dist_sq = np.maximum(dist_sq, 1e-24)
    dist = np.sqrt(dist_sq)
    inv_dist3 = 1.0 / (dist_sq * dist)
    np.fill_diagonal(inv_dist3[:, :, 0], 0)
    grad = -np.sum(diff * inv_dist3, axis=1)  # (n, 3)
    return grad


# ---------------------------------------------------------------------------
# L-BFGS optimizer (spherical coordinates)
# ---------------------------------------------------------------------------

def cart_to_sph(pts: np.ndarray) -> np.ndarray:
    x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
    theta = np.arccos(np.clip(z, -1, 1))
    phi = np.arctan2(y, x)
    return np.column_stack([theta, phi])


def sph_to_cart(sph: np.ndarray) -> np.ndarray:
    theta, phi = sph[:, 0], sph[:, 1]
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.column_stack([x, y, z])


def lbfgs_optimize(pts: np.ndarray, maxiter: int = 10000,
                   verbose: bool = True) -> tuple[np.ndarray, float]:
    """L-BFGS optimization with spherical coordinates."""

    def energy_and_grad(params):
        sph = params.reshape(-1, 2)
        cart = sph_to_cart(sph)
        energy = coulomb_energy(cart)

        grad_cart = coulomb_gradient(cart)

        theta, phi = sph[:, 0], sph[:, 1]
        st, ct = np.sin(theta), np.cos(theta)
        sp, cp = np.sin(phi), np.cos(phi)

        dx_dt = ct * cp
        dy_dt = ct * sp
        dz_dt = -st
        dx_dp = -st * sp
        dy_dp = st * cp

        grad_theta = (grad_cart[:, 0] * dx_dt + grad_cart[:, 1] * dy_dt
                      + grad_cart[:, 2] * dz_dt)
        grad_phi = grad_cart[:, 0] * dx_dp + grad_cart[:, 1] * dy_dp

        grad_sph = np.column_stack([grad_theta, grad_phi]).ravel()
        return energy, grad_sph

    sph0 = cart_to_sph(pts)
    x0 = sph0.ravel()

    best = {"energy": coulomb_energy(pts), "count": 0}

    def callback(xk):
        best["count"] += 1
        if best["count"] % 500 == 0 and verbose:
            sph = xk.reshape(-1, 2)
            cart = sph_to_cart(sph)
            e = coulomb_energy(cart)
            if e < best["energy"]:
                best["energy"] = e
            print(f"    L-BFGS iter {best['count']}: E = {best['energy']:.11f}")

    result = scipy_minimize(
        energy_and_grad, x0, method='L-BFGS-B', jac=True,
        options={'maxiter': maxiter, 'ftol': 1e-16, 'gtol': 1e-14},
        callback=callback,
    )

    final_pts = sph_to_cart(result.x.reshape(-1, 2))
    final_energy = coulomb_energy(final_pts)

    if verbose:
        print(f"    L-BFGS done: E = {final_energy:.11f} "
              f"(converged={result.success}, iters={result.nit})")

    return final_pts, final_energy


# ---------------------------------------------------------------------------
# Download Wales configurations
# ---------------------------------------------------------------------------

def download_wales_xyz(n: int) -> np.ndarray:
    """Download n-point Thomson configuration from Wales Cambridge database."""
    url = f"https://www-wales.ch.cam.ac.uk/~wales/CCD/Thomson/xyz/{n}.xyz"
    print(f"  Downloading {url} ...")

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ERROR downloading: {e}")
        raise

    lines = text.strip().split("\n")
    count = int(lines[0].strip())
    assert count == n, f"Expected {n} points, header says {count}"

    pts = []
    for line in lines[1:]:
        parts = line.strip().split()
        if len(parts) >= 4:
            # Format: "LA x y z"
            x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
            pts.append([x, y, z])
        elif len(parts) == 3:
            # Format: "x y z"
            x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
            pts.append([x, y, z])

    pts = np.array(pts, dtype=np.float64)
    assert len(pts) == n, f"Parsed {len(pts)} points, expected {n}"
    pts = normalize(pts)
    print(f"  Loaded {n} points, energy = {coulomb_energy(pts):.11f}")
    return pts


# ---------------------------------------------------------------------------
# UPGRADE: n-1 -> n (insert a point)
# ---------------------------------------------------------------------------

def find_voronoi_vertices(pts: np.ndarray) -> np.ndarray:
    """Compute Voronoi vertices on the unit sphere."""
    center = np.array([0.0, 0.0, 0.0])
    sv = SphericalVoronoi(pts, radius=1.0, center=center)
    sv.sort_vertices_of_regions()
    vertices = sv.vertices
    # Normalize vertices to unit sphere
    norms = np.linalg.norm(vertices, axis=1, keepdims=True)
    vertices = vertices / norms
    return vertices


def upgrade(pts_small: np.ndarray, target_n: int,
            verbose: bool = True) -> tuple[np.ndarray, float]:
    """Upgrade: insert best point into n-1 configuration, optimize to n.

    Strategy:
    1. Compute Voronoi vertices of the n-1 config
    2. Try inserting at each vertex, pick the one with lowest energy
    3. L-BFGS optimize the full n-point configuration
    """
    n_small = len(pts_small)
    assert target_n == n_small + 1

    print(f"\n  Computing Voronoi vertices for {n_small}-point configuration...")
    vertices = find_voronoi_vertices(pts_small)
    n_vertices = len(vertices)
    print(f"  Found {n_vertices} Voronoi vertices")

    # Also try antipodal points and midpoints of nearby pairs as candidates
    # But Voronoi vertices are the primary candidates
    print(f"  Testing {n_vertices} insertion candidates...")

    best_energy = np.inf
    best_candidate = None
    energies = []

    for i, v in enumerate(vertices):
        # Insert candidate point
        pts_trial = np.vstack([pts_small, v.reshape(1, 3)])
        e = coulomb_energy(pts_trial)
        energies.append(e)

        if e < best_energy:
            best_energy = e
            best_candidate = v.copy()
            best_idx = i

        if verbose and (i + 1) % 100 == 0:
            print(f"    Tested {i+1}/{n_vertices}, best so far: {best_energy:.11f}")

    print(f"  Best insertion at vertex {best_idx}: E = {best_energy:.11f}")
    print(f"  Energy range: [{min(energies):.6f}, {max(energies):.6f}]")

    # Build the n-point configuration
    pts_new = np.vstack([pts_small, best_candidate.reshape(1, 3)])
    assert len(pts_new) == target_n

    # Also try the top-k candidates and optimize each
    sorted_indices = np.argsort(energies)
    top_k = min(5, n_vertices)
    print(f"\n  Optimizing top-{top_k} insertion candidates with L-BFGS...")

    overall_best_energy = np.inf
    overall_best_pts = None

    for rank, idx in enumerate(sorted_indices[:top_k]):
        v = vertices[idx]
        pts_trial = np.vstack([pts_small, v.reshape(1, 3)])
        e_before = energies[idx]

        print(f"\n  --- Candidate {rank+1} (vertex {idx}): "
              f"pre-opt E = {e_before:.11f} ---")

        pts_opt, e_opt = lbfgs_optimize(pts_trial, maxiter=10000, verbose=verbose)

        print(f"  Post-optimization: E = {e_opt:.11f}")

        if e_opt < overall_best_energy:
            overall_best_energy = e_opt
            overall_best_pts = pts_opt.copy()
            print(f"  >>> New best from upgrade: {overall_best_energy:.11f}")

    return overall_best_pts, overall_best_energy


# ---------------------------------------------------------------------------
# DOWNGRADE: n+1 -> n (remove a point)
# ---------------------------------------------------------------------------

def compute_point_contributions(pts: np.ndarray) -> np.ndarray:
    """Compute per-point energy contribution (sum of 1/r to all other points)."""
    n = len(pts)
    contributions = np.zeros(n)

    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)
    dists = np.sqrt(dist_sq)
    np.fill_diagonal(dists, 1e30)
    dists = np.maximum(dists, 1e-12)
    inv_dists = 1.0 / dists

    # contribution[i] = sum_{j!=i} 1/dist(i,j)
    contributions = np.sum(inv_dists, axis=1)
    return contributions


def energy_without_point(pts: np.ndarray, total_energy: float,
                         idx: int) -> float:
    """Compute energy of configuration with point idx removed. O(n)."""
    # Remove all pairwise interactions involving point idx
    diffs = pts - pts[idx]
    dists = np.sqrt(np.sum(diffs ** 2, axis=1))
    dists[idx] = 1e30
    dists = np.maximum(dists, 1e-12)
    contribution = np.sum(1.0 / dists)
    return total_energy - contribution


def downgrade(pts_large: np.ndarray, target_n: int,
              verbose: bool = True) -> tuple[np.ndarray, float]:
    """Downgrade: remove best point from n+1 configuration, optimize to n.

    Strategy:
    1. For each point, compute energy if removed
    2. Remove point giving lowest remaining energy
    3. L-BFGS optimize the remaining n-point configuration
    """
    n_large = len(pts_large)
    assert target_n == n_large - 1

    total_energy = coulomb_energy(pts_large)
    print(f"\n  Full {n_large}-point energy: {total_energy:.11f}")

    # Compute energy for each possible removal
    print(f"  Testing {n_large} point removals...")
    removal_energies = np.zeros(n_large)
    for i in range(n_large):
        removal_energies[i] = energy_without_point(pts_large, total_energy, i)

    best_removal = np.argmin(removal_energies)
    best_removal_energy = removal_energies[best_removal]
    worst_removal = np.argmax(removal_energies)

    print(f"  Best removal: point {best_removal}, "
          f"E_remaining = {best_removal_energy:.11f}")
    print(f"  Worst removal: point {worst_removal}, "
          f"E_remaining = {removal_energies[worst_removal]:.11f}")

    # Try top-k removals
    sorted_indices = np.argsort(removal_energies)
    top_k = min(5, n_large)
    print(f"\n  Optimizing top-{top_k} removal candidates with L-BFGS...")

    overall_best_energy = np.inf
    overall_best_pts = None

    for rank, idx in enumerate(sorted_indices[:top_k]):
        # Remove point idx
        pts_reduced = np.delete(pts_large, idx, axis=0)
        assert len(pts_reduced) == target_n
        e_before = removal_energies[idx]

        print(f"\n  --- Candidate {rank+1} (remove point {idx}): "
              f"pre-opt E = {e_before:.11f} ---")

        pts_opt, e_opt = lbfgs_optimize(pts_reduced, maxiter=10000,
                                        verbose=verbose)

        print(f"  Post-optimization: E = {e_opt:.11f}")

        if e_opt < overall_best_energy:
            overall_best_energy = e_opt
            overall_best_pts = pts_opt.copy()
            print(f"  >>> New best from downgrade: {overall_best_energy:.11f}")

    return overall_best_pts, overall_best_energy


# ---------------------------------------------------------------------------
# Save solution
# ---------------------------------------------------------------------------

def save_solution(pts: np.ndarray, score: float, tag: str):
    """Save solution to results directory."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": pts.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag}: {score:.11f} -> {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t_start = time.time()
    print("=" * 70)
    print("Thomson n=282: Upgrade/Downgrade Algorithm")
    print(f"SOTA energy: {SOTA_ENERGY:.11f}")
    print("=" * 70)

    # ------------------------------------------------------------------
    # Step 1: Download neighboring configurations
    # ------------------------------------------------------------------
    print("\n[1] Downloading Wales configurations...")
    pts_281 = download_wales_xyz(281)
    pts_283 = download_wales_xyz(283)

    # ------------------------------------------------------------------
    # Step 2: UPGRADE from n=281
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[2] UPGRADE: 281 -> 282")
    print("=" * 70)

    pts_up, e_up = upgrade(pts_281, target_n=282, verbose=True)
    print(f"\n  UPGRADE result: E = {e_up:.11f}")
    print(f"  vs SOTA:          {SOTA_ENERGY:.11f}")
    print(f"  Gap:              {e_up - SOTA_ENERGY:.6e}")

    if e_up <= SOTA_ENERGY:
        print("  >>> BEATS OR MATCHES SOTA! <<<")
        save_solution(pts_up, e_up, "upgrade_282")

    # ------------------------------------------------------------------
    # Step 3: DOWNGRADE from n=283
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[3] DOWNGRADE: 283 -> 282")
    print("=" * 70)

    pts_down, e_down = downgrade(pts_283, target_n=282, verbose=True)
    print(f"\n  DOWNGRADE result: E = {e_down:.11f}")
    print(f"  vs SOTA:            {SOTA_ENERGY:.11f}")
    print(f"  Gap:                {e_down - SOTA_ENERGY:.6e}")

    if e_down <= SOTA_ENERGY:
        print("  >>> BEATS OR MATCHES SOTA! <<<")
        save_solution(pts_down, e_down, "downgrade_282")

    # ------------------------------------------------------------------
    # Step 4: Take best candidate and do deep polishing
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("[4] DEEP POLISHING of best candidate")
    print("=" * 70)

    if e_up < e_down:
        best_pts, best_energy = pts_up.copy(), e_up
        best_source = "upgrade"
    else:
        best_pts, best_energy = pts_down.copy(), e_down
        best_source = "downgrade"

    print(f"  Best source: {best_source}, E = {best_energy:.11f}")

    # Multiple rounds of L-BFGS with re-parameterization
    for round_i in range(3):
        print(f"\n  Polish round {round_i + 1}...")
        pts_pol, e_pol = lbfgs_optimize(best_pts.copy(), maxiter=20000,
                                        verbose=False)
        if e_pol < best_energy:
            improvement = best_energy - e_pol
            best_energy = e_pol
            best_pts = pts_pol.copy()
            print(f"    Improved by {improvement:.2e} -> E = {best_energy:.11f}")
        else:
            print(f"    No improvement (E = {e_pol:.11f})")
            break

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    elapsed = time.time() - t_start
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Upgrade energy:    {e_up:.11f}")
    print(f"  Downgrade energy:  {e_down:.11f}")
    print(f"  Best polished:     {best_energy:.11f} (from {best_source})")
    print(f"  SOTA energy:       {SOTA_ENERGY:.11f}")
    print(f"  Gap to SOTA:       {best_energy - SOTA_ENERGY:.6e}")
    print(f"  Elapsed time:      {elapsed:.1f}s")

    if best_energy <= SOTA_ENERGY:
        print("\n  >>> BEATS OR MATCHES SOTA! Saving... <<<")
        save_solution(best_pts, best_energy, "upgrade_downgrade_best")
    else:
        print(f"\n  Did not beat SOTA. Gap = {best_energy - SOTA_ENERGY:.6e}")
        # Save anyway for reference
        save_solution(best_pts, best_energy, "upgrade_downgrade_best")

    print("=" * 70)
    return best_pts, best_energy


if __name__ == "__main__":
    main()
