"""Icosadeltahedral seed generator for Thomson problem n=282.

Generates 282 points on S^2 via the Caspar-Klug construction:
  282 = 10*(4^2 + 4*2 + 2^2) + 2 = 10*28 + 2
  => Class III geodesic polyhedron {3,5+}_{4,2} with T-number 28.

Construction:
  1. Start with the 12 vertices of a regular icosahedron.
  2. For each triangular face, place a rotated triangular lattice defined
     by (h,k) = (4,2) and collect all lattice points inside the face.
  3. Project all points onto the unit sphere.
  4. Deduplicate shared edge/vertex points.

By Pick's theorem, each face has 18 lattice points:
  12 interior + 3 edge-interior + 3 corners = 18.
Total: 20*12 + 30*1 + 12 = 282.
"""

import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize as scipy_minimize

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = PROJECT_ROOT / "results" / "problem-10-thomson"

N = 282
H, K = 4, 2
T = H * H + H * K + K * K  # 28


# ---------------------------------------------------------------------------
# Icosahedron
# ---------------------------------------------------------------------------

def icosahedron_vertices() -> np.ndarray:
    """12 vertices of a regular icosahedron on the unit sphere."""
    phi = (1 + np.sqrt(5)) / 2
    verts = []
    for s1 in [1, -1]:
        for s2 in [1, -1]:
            verts.append([0, s1, s2 * phi])
            verts.append([s1, s2 * phi, 0])
            verts.append([s2 * phi, 0, s1])
    verts = np.array(verts, dtype=np.float64)
    return verts / np.linalg.norm(verts, axis=1, keepdims=True)


def icosahedron_faces(verts: np.ndarray) -> list[tuple[int, int, int]]:
    """20 triangular faces as vertex index triples."""
    n = len(verts)
    dists = np.sqrt(np.sum((verts[:, None] - verts[None, :]) ** 2, axis=-1))
    edge_len = np.min(dists[dists > 0.1])
    adj = dists < edge_len * 1.05
    np.fill_diagonal(adj, False)

    faces = []
    for i in range(n):
        for j in range(i + 1, n):
            if not adj[i, j]:
                continue
            for k in range(j + 1, n):
                if adj[i, k] and adj[j, k]:
                    faces.append((i, j, k))
    assert len(faces) == 20, f"Expected 20 faces, got {len(faces)}"
    return faces


# ---------------------------------------------------------------------------
# (h,k) lattice points in a triangle
# ---------------------------------------------------------------------------

def lattice_points_in_triangle(h: int, k: int) -> list[tuple[float, float]]:
    """Find all triangular lattice points inside the super-cell triangle.

    The super-cell triangle has vertices at:
      A = (0, 0)
      B = h*a1 + k*a2  (= L1)
      C = -k*a1 + (h+k)*a2  (= L2)

    where a1 = (1, 0), a2 = (0.5, sqrt(3)/2) are the triangular
    lattice basis vectors.

    Returns list of (s, t) where the 3D point is:
      p = (1 - s - t) * v0 + s * v1 + t * v2

    (s, t) are barycentric coordinates within the icosahedron face.
    """
    a1 = np.array([1.0, 0.0])
    a2 = np.array([0.5, np.sqrt(3) / 2])

    L1 = h * a1 + k * a2
    L2 = -k * a1 + (h + k) * a2

    # Solve p = s*L1 + t*L2 for each lattice point p = i*a1 + j*a2
    M = np.array([[L1[0], L2[0]], [L1[1], L2[1]]])
    M_inv = np.linalg.inv(M)

    tol = 1e-10
    result = []

    for i in range(-k - 2, h + k + 3):
        for j in range(-2, h + k + 3):
            p = i * a1 + j * a2
            st = M_inv @ p
            s, t = float(st[0]), float(st[1])
            if s >= -tol and t >= -tol and s + t <= 1 + tol:
                s = np.clip(s, 0.0, 1.0)
                t = np.clip(t, 0.0, 1.0)
                if s + t > 1.0:
                    scale = 1.0 / (s + t)
                    s *= scale
                    t *= scale
                result.append((s, t))

    return result


# ---------------------------------------------------------------------------
# Full geodesic polyhedron
# ---------------------------------------------------------------------------

def icosadeltahedral_points(h: int, k: int) -> np.ndarray:
    """Generate the vertices of a {3,5+}_{h,k} geodesic polyhedron.

    The key challenge: shared edge/vertex points from adjacent faces
    must produce the same 3D coordinates after spherical projection.

    Strategy: for each face, compute 3D points via linear interpolation
    in the embedding space (not on the sphere), THEN project to sphere.
    This guarantees that shared vertices (at corners and edge midpoints)
    produce identical coordinates regardless of which face generates them.
    """
    T_num = h * h + h * k + k * k
    expected_n = 10 * T_num + 2

    verts = icosahedron_vertices()
    faces = icosahedron_faces(verts)

    # Get barycentric coordinates for the subdivision
    bary_list = lattice_points_in_triangle(h, k)
    print(f"    Lattice points per face: {len(bary_list)}")

    # Classify each barycentric point
    tol = 1e-10
    n_corner = sum(1 for s, t in bary_list
                   if min(s, t, 1-s-t) < tol and max(s, t, 1-s-t) > 1-tol)
    n_edge = sum(1 for s, t in bary_list
                 if min(s, t, 1-s-t) < tol and max(s, t, 1-s-t) < 1-tol)
    n_interior = len(bary_list) - n_corner - n_edge
    print(f"    Corners: {n_corner}, Edge: {n_edge}, Interior: {n_interior}")

    # Generate all 3D points and deduplicate
    all_points = {}
    decimals = 10

    for face in faces:
        fv0 = verts[face[0]]
        fv1 = verts[face[1]]
        fv2 = verts[face[2]]

        for s, t in bary_list:
            u = 1.0 - s - t
            pt = u * fv0 + s * fv1 + t * fv2
            norm = np.linalg.norm(pt)
            if norm < 1e-15:
                continue
            pt = pt / norm
            key = tuple(np.round(pt, decimals))
            all_points[key] = pt

    pts = np.array(list(all_points.values()), dtype=np.float64)
    print(f"    Generated {len(pts)} unique points (expected {expected_n})")

    if len(pts) != expected_n:
        # Debug: try different dedup precisions
        print(f"    Trying different dedup precisions...")
        for dec in range(12, 4, -1):
            test_points = {}
            for face in faces:
                fv0 = verts[face[0]]
                fv1 = verts[face[1]]
                fv2 = verts[face[2]]
                for s, t in bary_list:
                    u = 1.0 - s - t
                    pt = u * fv0 + s * fv1 + t * fv2
                    norm = np.linalg.norm(pt)
                    if norm < 1e-15:
                        continue
                    pt = pt / norm
                    key = tuple(np.round(pt, dec))
                    test_points[key] = pt
            n = len(test_points)
            print(f"      decimals={dec}: {n} points")
            if n == expected_n:
                pts = np.array(list(test_points.values()), dtype=np.float64)
                break

    return pts


# ---------------------------------------------------------------------------
# L-BFGS optimizer
# ---------------------------------------------------------------------------

def coulomb_energy(pts: np.ndarray) -> float:
    """Fast Coulomb energy."""
    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)
    n = len(pts)
    idx_i, idx_j = np.triu_indices(n, k=1)
    dists = np.sqrt(dist_sq[idx_i, idx_j])
    dists = np.maximum(dists, 1e-12)
    return float(np.sum(1.0 / dists))


def coulomb_gradient(pts: np.ndarray) -> np.ndarray:
    """Gradient of Coulomb energy."""
    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1, keepdims=True)
    dist_sq = np.maximum(dist_sq, 1e-24)
    dist = np.sqrt(dist_sq)
    inv_dist3 = 1.0 / (dist_sq * dist)
    np.fill_diagonal(inv_dist3[:, :, 0], 0)
    return -np.sum(diff * inv_dist3, axis=1)


def lbfgs_optimize(pts: np.ndarray, maxiter: int = 10000,
                   verbose: bool = True) -> tuple[np.ndarray, float]:
    """L-BFGS optimization using spherical coordinates."""
    def cart_to_sph(pts):
        x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        theta = np.arccos(np.clip(z, -1, 1))
        phi = np.arctan2(y, x)
        return np.column_stack([theta, phi])

    def sph_to_cart(sph):
        theta, phi = sph[:, 0], sph[:, 1]
        return np.column_stack([
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta),
        ])

    def energy_and_grad(params):
        sph = params.reshape(-1, 2)
        cart = sph_to_cart(sph)
        energy = coulomb_energy(cart)
        grad_cart = coulomb_gradient(cart)

        theta, phi = sph[:, 0], sph[:, 1]
        st, ct = np.sin(theta), np.cos(theta)
        sp, cp = np.sin(phi), np.cos(phi)

        grad_theta = (grad_cart[:, 0] * ct * cp +
                      grad_cart[:, 1] * ct * sp +
                      grad_cart[:, 2] * (-st))
        grad_phi = (grad_cart[:, 0] * (-st * sp) +
                    grad_cart[:, 1] * (st * cp))

        return energy, np.column_stack([grad_theta, grad_phi]).ravel()

    sph0 = cart_to_sph(pts)
    x0 = sph0.ravel()
    best = {"e": coulomb_energy(pts), "n": 0}

    def callback(xk):
        best["n"] += 1
        if best["n"] % 500 == 0 and verbose:
            sph = xk.reshape(-1, 2)
            e = coulomb_energy(sph_to_cart(sph))
            if e < best["e"]:
                best["e"] = e
            print(f"    L-BFGS iter {best['n']}: E = {best['e']:.15f}")

    result = scipy_minimize(
        energy_and_grad, x0, method='L-BFGS-B', jac=True,
        options={'maxiter': maxiter, 'ftol': 1e-16, 'gtol': 1e-14},
        callback=callback,
    )

    final_pts = sph_to_cart(result.x.reshape(-1, 2))
    final_energy = coulomb_energy(final_pts)
    if verbose:
        print(f"    L-BFGS done: E = {final_energy:.15f} "
              f"(converged={result.success}, iters={best['n']})")
    return final_pts, final_energy


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Load SOTA from data file
    sota_path = RESULTS_DIR / "sota_arena.json"
    if sota_path.exists():
        with open(sota_path) as f:
            SOTA = json.load(f)["score"]
    else:
        SOTA = float("inf")
    print("=" * 70)
    print("Icosadeltahedral Seed Generator for Thomson Problem n=282")
    print(f"(h,k) = ({H},{K}), T = {T}, n = 10*{T}+2 = {10*T+2}")
    print("=" * 70)

    # Step 1: Generate icosadeltahedral seed
    print("\n[1] Generating icosadeltahedral points...")
    t0 = time.time()
    pts = icosadeltahedral_points(H, K)
    t1 = time.time()
    print(f"    Generation time: {t1 - t0:.2f}s")

    n_pts = len(pts)
    if n_pts != N:
        print(f"\n    FATAL: Got {n_pts} points, expected {N}.")
        print("    Debugging dedup...")

        # Show how many duplicates exist
        verts = icosahedron_vertices()
        faces = icosahedron_faces(verts)
        bary_list = lattice_points_in_triangle(H, K)
        all_raw = []
        for face in faces:
            fv0, fv1, fv2 = verts[face[0]], verts[face[1]], verts[face[2]]
            for s, t in bary_list:
                u = 1.0 - s - t
                pt = u * fv0 + s * fv1 + t * fv2
                pt = pt / np.linalg.norm(pt)
                all_raw.append(pt)
        all_raw = np.array(all_raw)
        print(f"    Total raw points (20 faces * {len(bary_list)}): {len(all_raw)}")

        # Check pairwise distances for near-duplicates
        from scipy.spatial.distance import pdist
        dists = pdist(all_raw)
        close_pairs = np.sum(dists < 1e-6)
        print(f"    Near-duplicate pairs (dist < 1e-6): {close_pairs}")
        close_pairs_8 = np.sum(dists < 1e-8)
        print(f"    Near-duplicate pairs (dist < 1e-8): {close_pairs_8}")
        close_pairs_10 = np.sum(dists < 1e-10)
        print(f"    Near-duplicate pairs (dist < 1e-10): {close_pairs_10}")

        # Find clusters
        from scipy.cluster.hierarchy import fcluster, linkage
        Z = linkage(all_raw, method='single')
        for thr in [1e-6, 1e-8, 1e-10, 1e-12]:
            clusters = fcluster(Z, t=thr, criterion='distance')
            n_clusters = len(set(clusters))
            print(f"    Clusters at threshold {thr:.0e}: {n_clusters}")

        return

    raw_energy = coulomb_energy(pts)
    print(f"\n  Raw icosadeltahedral energy:  E = {raw_energy:.10f}")
    print(f"  SOTA:                        E = {SOTA:.10f}")
    print(f"  Gap to SOTA (raw):           {raw_energy - SOTA:.4f}")

    # Step 2: L-BFGS optimization
    print("\n[2] L-BFGS optimization...")
    t0 = time.time()
    pts_opt, energy_opt = lbfgs_optimize(pts, maxiter=15000, verbose=True)
    t1 = time.time()
    print(f"\n  After L-BFGS energy:         E = {energy_opt:.15f}")
    print(f"  SOTA:                        E = {SOTA:.15f}")
    print(f"  Gap to SOTA (after L-BFGS):  {energy_opt - SOTA:.2e}")
    print(f"  L-BFGS time: {t1 - t0:.1f}s")

    # Step 3: Save result
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "solution_icosa_seed.json"
    data = {
        "vectors": pts_opt.tolist(),
        "score": energy_opt,
        "seed": "icosadeltahedral",
        "h": H, "k": K, "T": T,
    }
    with open(out_path, "w") as f:
        json.dump(data, f)
    print(f"\n  Saved to {out_path}")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print(f"  Raw icosadeltahedral:  {raw_energy:.10f}")
    print(f"  After L-BFGS:         {energy_opt:.15f}")
    print(f"  SOTA:                 {SOTA:.15f}")
    print(f"  Gap:                  {energy_opt - SOTA:.2e}")
    if energy_opt < SOTA:
        print("  >>> BELOW SOTA! New best found! <<<")
    print("=" * 70)

    return pts_opt, energy_opt


if __name__ == "__main__":
    main()
