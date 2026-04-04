"""Thomson Problem (n=282) optimizer.

Minimize Coulomb energy E = sum_{i<j} 1/||p_i - p_j||
for 282 points on the unit sphere S^2.

Strategies:
1. Riemannian gradient descent (gradient on tangent plane, project back)
2. L-BFGS with spherical projection
3. Basin-hopping (random perturbation + local minimization)
4. Multi-scale micro-perturbation
5. Targeted perturbation (contribution-weighted sampling)
"""

import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize as scipy_minimize

RESULTS_DIR = Path("results/problem-10-thomson")
N = 282


def load_sota(tag: str = "arena") -> tuple[np.ndarray, float]:
    """Load a SOTA solution."""
    path = RESULTS_DIR / f"sota_{tag}.json"
    with open(path) as f:
        data = json.load(f)
    pts = np.array(data["vectors"], dtype=np.float64)
    norms = np.linalg.norm(pts, axis=1, keepdims=True)
    pts = pts / norms
    energy = coulomb_energy(pts)
    return pts, energy


def save_solution(pts: np.ndarray, score: float, tag: str = "best"):
    """Save a solution."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": pts.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag}: {score:.15f} -> {path}")


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
    """Compute gradient of Coulomb energy w.r.t. point positions.

    dE/dp_i = -sum_{j!=i} (p_i - p_j) / ||p_i - p_j||^3
    """
    diff = pts[:, None, :] - pts[None, :, :]  # (n, n, 3)
    dist_sq = np.sum(diff ** 2, axis=-1, keepdims=True)  # (n, n, 1)
    dist_sq = np.maximum(dist_sq, 1e-24)
    dist = np.sqrt(dist_sq)  # (n, n, 1)
    # grad_i = -sum_{j!=i} (p_i - p_j) / dist^3
    inv_dist3 = 1.0 / (dist_sq * dist)  # (n, n, 1)
    np.fill_diagonal(inv_dist3[:, :, 0], 0)
    grad = -np.sum(diff * inv_dist3, axis=1)  # (n, 3)
    return grad


def project_tangent(grad: np.ndarray, pts: np.ndarray) -> np.ndarray:
    """Project gradient onto tangent plane of sphere at each point."""
    # Remove radial component: grad_tan = grad - (grad . p) * p
    dots = np.sum(grad * pts, axis=1, keepdims=True)
    return grad - dots * pts


def riemannian_gd(pts: np.ndarray, lr: float = 1e-7, n_steps: int = 1000,
                  verbose: bool = True) -> tuple[np.ndarray, float]:
    """Riemannian gradient descent on the sphere manifold."""
    best_pts = pts.copy()
    best_energy = coulomb_energy(pts)

    for step in range(n_steps):
        grad = coulomb_gradient(pts)
        grad_tan = project_tangent(grad, pts)

        # Descent step
        pts = pts - lr * grad_tan
        pts = normalize(pts)

        energy = coulomb_energy(pts)
        if energy < best_energy:
            best_energy = energy
            best_pts = pts.copy()
            if verbose and step % 100 == 0:
                print(f"  GD step {step}: E = {best_energy:.15f}")

    return best_pts, best_energy


def lbfgs_optimize(pts: np.ndarray, maxiter: int = 5000,
                   verbose: bool = True) -> tuple[np.ndarray, float]:
    """L-BFGS optimization with spherical projection.

    Uses spherical coordinates (theta, phi) internally.
    """
    def cart_to_sph(pts):
        """Convert Cartesian to spherical (theta, phi)."""
        x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        theta = np.arccos(np.clip(z, -1, 1))
        phi = np.arctan2(y, x)
        return np.column_stack([theta, phi])

    def sph_to_cart(sph):
        """Convert spherical to Cartesian."""
        theta, phi = sph[:, 0], sph[:, 1]
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        return np.column_stack([x, y, z])

    def energy_and_grad(params):
        sph = params.reshape(-1, 2)
        cart = sph_to_cart(sph)
        energy = coulomb_energy(cart)

        # Gradient in Cartesian
        grad_cart = coulomb_gradient(cart)

        # Chain rule: convert to spherical gradient
        theta, phi = sph[:, 0], sph[:, 1]
        st, ct = np.sin(theta), np.cos(theta)
        sp, cp = np.sin(phi), np.cos(phi)

        # d(x,y,z)/d(theta) and d(x,y,z)/d(phi)
        dx_dt = ct * cp
        dy_dt = ct * sp
        dz_dt = -st
        dx_dp = -st * sp
        dy_dp = st * cp
        dz_dp = np.zeros_like(st)

        grad_theta = grad_cart[:, 0] * dx_dt + grad_cart[:, 1] * dy_dt + grad_cart[:, 2] * dz_dt
        grad_phi = grad_cart[:, 0] * dx_dp + grad_cart[:, 1] * dy_dp + grad_cart[:, 2] * dz_dp

        grad_sph = np.column_stack([grad_theta, grad_phi]).ravel()
        return energy, grad_sph

    sph0 = cart_to_sph(pts)
    x0 = sph0.ravel()

    best_energy = coulomb_energy(pts)
    callback_data = {"best": best_energy, "count": 0}

    def callback(xk):
        callback_data["count"] += 1
        if callback_data["count"] % 100 == 0 and verbose:
            sph = xk.reshape(-1, 2)
            cart = sph_to_cart(sph)
            e = coulomb_energy(cart)
            if e < callback_data["best"]:
                callback_data["best"] = e
            print(f"  L-BFGS iter {callback_data['count']}: E = {callback_data['best']:.15f}")

    result = scipy_minimize(
        energy_and_grad, x0, method='L-BFGS-B', jac=True,
        options={'maxiter': maxiter, 'ftol': 1e-16, 'gtol': 1e-14},
        callback=callback,
    )

    final_pts = sph_to_cart(result.x.reshape(-1, 2))
    final_energy = coulomb_energy(final_pts)

    if verbose:
        print(f"  L-BFGS done: E = {final_energy:.15f} (converged={result.success})")

    return final_pts, final_energy


def incremental_energy_change(pts: np.ndarray, idx: int,
                               new_pt: np.ndarray,
                               total_energy: float) -> float:
    """Compute energy change when replacing pts[idx] with new_pt. O(n)."""
    old_pt = pts[idx]

    # Remove old contributions
    diffs_old = pts - old_pt  # (n, 3)
    dists_old = np.sqrt(np.sum(diffs_old ** 2, axis=1))
    dists_old[idx] = 1e30  # skip self
    dists_old = np.maximum(dists_old, 1e-12)
    old_contrib = np.sum(1.0 / dists_old)

    # Add new contributions
    diffs_new = pts - new_pt
    dists_new = np.sqrt(np.sum(diffs_new ** 2, axis=1))
    dists_new[idx] = 1e30
    dists_new = np.maximum(dists_new, 1e-12)
    new_contrib = np.sum(1.0 / dists_new)

    return total_energy - old_contrib + new_contrib


def micro_perturbation(pts: np.ndarray, energy: float, scale: float,
                       n_trials: int = 100000, rng=None,
                       verbose: bool = True) -> tuple[np.ndarray, float]:
    """Random single-point micro-perturbation with greedy acceptance."""
    if rng is None:
        rng = np.random.default_rng()

    n = len(pts)
    best_pts = pts.copy()
    best_energy = energy
    improvements = 0

    for trial in range(n_trials):
        idx = rng.integers(0, n)
        old_pt = pts[idx].copy()

        # Random tangent perturbation
        noise = rng.standard_normal(3) * scale
        # Project to tangent plane
        noise -= np.dot(noise, old_pt) * old_pt
        new_pt = old_pt + noise
        new_pt = new_pt / np.linalg.norm(new_pt)

        new_energy = incremental_energy_change(pts, idx, new_pt, best_energy)

        if new_energy < best_energy:
            pts[idx] = new_pt
            best_energy = new_energy
            best_pts = pts.copy()
            improvements += 1

            if verbose and improvements % 10 == 0:
                print(f"  Perturbation scale={scale:.0e}: {improvements} improvements, E = {best_energy:.15f}")

    if verbose:
        print(f"  Scale {scale:.0e}: {improvements}/{n_trials} improvements, final E = {best_energy:.15f}")

    return best_pts, best_energy


def targeted_perturbation(pts: np.ndarray, energy: float, scale: float,
                          n_trials: int = 50000, rng=None,
                          verbose: bool = True) -> tuple[np.ndarray, float]:
    """Perturbation with contribution-weighted point sampling."""
    if rng is None:
        rng = np.random.default_rng()

    n = len(pts)
    best_pts = pts.copy()
    best_energy = energy
    improvements = 0

    # Compute per-point contributions
    contributions = np.zeros(n)
    for i in range(n):
        diffs = pts - pts[i]
        dists = np.sqrt(np.sum(diffs ** 2, axis=1))
        dists[i] = 1e30
        dists = np.maximum(dists, 1e-12)
        contributions[i] = np.sum(1.0 / dists)

    # Weight by contribution (higher contribution = more likely to be perturbed)
    probs = contributions / contributions.sum()

    for trial in range(n_trials):
        idx = rng.choice(n, p=probs)
        old_pt = pts[idx].copy()

        noise = rng.standard_normal(3) * scale
        noise -= np.dot(noise, old_pt) * old_pt
        new_pt = old_pt + noise
        new_pt = new_pt / np.linalg.norm(new_pt)

        new_energy = incremental_energy_change(pts, idx, new_pt, best_energy)

        if new_energy < best_energy:
            pts[idx] = new_pt
            best_energy = new_energy
            best_pts = pts.copy()
            improvements += 1

            # Recompute contributions periodically
            if improvements % 50 == 0:
                for i in range(n):
                    diffs = pts - pts[i]
                    dists = np.sqrt(np.sum(diffs ** 2, axis=1))
                    dists[i] = 1e30
                    dists = np.maximum(dists, 1e-12)
                    contributions[i] = np.sum(1.0 / dists)
                probs = contributions / contributions.sum()

    if verbose:
        print(f"  Targeted {scale:.0e}: {improvements}/{n_trials} improvements, E = {best_energy:.15f}")

    return best_pts, best_energy


def basin_hopping(pts: np.ndarray, energy: float, n_hops: int = 500,
                  perturb_scale: float = 0.3, temperature: float = 0.1,
                  rng=None, verbose: bool = True) -> tuple[np.ndarray, float]:
    """Basin-hopping: random perturbation + local minimization."""
    if rng is None:
        rng = np.random.default_rng()

    best_pts = pts.copy()
    best_energy = energy
    current_pts = pts.copy()
    current_energy = energy

    for hop in range(n_hops):
        # Random perturbation: move a subset of points
        n_move = max(1, rng.integers(1, min(20, N)))
        trial_pts = current_pts.copy()
        indices = rng.choice(N, size=n_move, replace=False)

        for idx in indices:
            noise = rng.standard_normal(3) * perturb_scale
            noise -= np.dot(noise, trial_pts[idx]) * trial_pts[idx]
            trial_pts[idx] += noise
            trial_pts[idx] /= np.linalg.norm(trial_pts[idx])

        # Local minimization
        trial_pts, trial_energy = lbfgs_optimize(trial_pts, maxiter=500, verbose=False)

        # Metropolis acceptance
        delta = trial_energy - current_energy
        if delta < 0 or rng.random() < np.exp(-delta / temperature):
            current_pts = trial_pts
            current_energy = trial_energy

            if trial_energy < best_energy:
                best_energy = trial_energy
                best_pts = trial_pts.copy()
                if verbose:
                    print(f"  Basin hop {hop}: NEW BEST E = {best_energy:.15f}")

        if verbose and hop % 50 == 0:
            print(f"  Basin hop {hop}/{n_hops}: best E = {best_energy:.15f}, current E = {current_energy:.15f}")

    return best_pts, best_energy


def fibonacci_sphere(n: int) -> np.ndarray:
    """Generate n points on sphere using Fibonacci spiral."""
    pts = np.zeros((n, 3))
    golden_ratio = (1 + np.sqrt(5)) / 2
    for i in range(n):
        theta = np.arccos(1 - 2 * (i + 0.5) / n)
        phi = 2 * np.pi * i / golden_ratio
        pts[i] = [np.sin(theta) * np.cos(phi),
                  np.sin(theta) * np.sin(phi),
                  np.cos(theta)]
    return pts


def multi_point_swap(pts: np.ndarray, energy: float, n_trials: int = 10000,
                     rng=None, verbose: bool = True) -> tuple[np.ndarray, float]:
    """Try swapping pairs of points with perturbation."""
    if rng is None:
        rng = np.random.default_rng()

    n = len(pts)
    best_pts = pts.copy()
    best_energy = energy
    improvements = 0

    for trial in range(n_trials):
        # Pick 2-4 points and apply correlated rotation
        n_pts = rng.integers(2, 5)
        indices = rng.choice(n, size=n_pts, replace=False)

        trial_pts = pts.copy()
        # Random rotation axis and small angle
        axis = rng.standard_normal(3)
        axis /= np.linalg.norm(axis)
        angle = rng.normal(0, 0.01)

        # Rodrigues rotation
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)
        for idx in indices:
            p = trial_pts[idx]
            rotated = (p * cos_a +
                       np.cross(axis, p) * sin_a +
                       axis * np.dot(axis, p) * (1 - cos_a))
            trial_pts[idx] = rotated / np.linalg.norm(rotated)

        new_energy = coulomb_energy(trial_pts)
        if new_energy < best_energy:
            pts = trial_pts
            best_energy = new_energy
            best_pts = pts.copy()
            improvements += 1

    if verbose:
        print(f"  Multi-point swap: {improvements}/{n_trials} improvements, E = {best_energy:.15f}")

    return best_pts, best_energy


def run_optimization():
    """Main optimization pipeline."""
    print("=" * 70)
    print("Thomson Problem (n=282) Optimizer")
    print("=" * 70)

    # Load SOTA
    print("\n[1] Loading SOTA solutions...")
    pts_arena, e_arena = load_sota("arena")
    print(f"  Arena SOTA: {e_arena:.15f}")

    pts_wales, e_wales = load_sota("wales")
    print(f"  Wales SOTA: {e_wales:.15f}")

    # Use whichever is better
    if e_wales < e_arena:
        pts, energy = pts_wales.copy(), e_wales
        print("  Using Wales coordinates (lower energy)")
    else:
        pts, energy = pts_arena.copy(), e_arena
        print("  Using Arena coordinates (lower energy)")

    best_pts, best_energy = pts.copy(), energy
    target = e_arena - 1e-5
    print(f"\n  Current:  {best_energy:.15f}")
    print(f"  Target:   {target:.15f}")
    print(f"  Gap:      {best_energy - target:.2e}")

    # Phase 1: Polish with L-BFGS
    print("\n[2] Phase 1: L-BFGS polish...")
    pts_lbfgs, e_lbfgs = lbfgs_optimize(pts.copy(), maxiter=10000)
    if e_lbfgs < best_energy:
        best_energy = e_lbfgs
        best_pts = pts_lbfgs
        print(f"  L-BFGS improved: {best_energy:.15f}")
        save_solution(best_pts, best_energy, "lbfgs")
    else:
        print(f"  L-BFGS no improvement: {e_lbfgs:.15f}")

    # Phase 2: Riemannian GD with multiple learning rates
    print("\n[3] Phase 2: Riemannian gradient descent...")
    for lr in [1e-8, 1e-9, 1e-10]:
        pts_gd, e_gd = riemannian_gd(best_pts.copy(), lr=lr, n_steps=2000, verbose=False)
        if e_gd < best_energy:
            best_energy = e_gd
            best_pts = pts_gd
            print(f"  GD lr={lr:.0e} improved: {best_energy:.15f}")
            save_solution(best_pts, best_energy, "gd")
        else:
            print(f"  GD lr={lr:.0e} no improvement: {e_gd:.15f}")

    # Phase 3: Multi-scale micro-perturbation
    print("\n[4] Phase 3: Multi-scale micro-perturbation...")
    rng = np.random.default_rng(42)
    for scale in [1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10]:
        pts_mp, e_mp = micro_perturbation(best_pts.copy(), best_energy,
                                           scale=scale, n_trials=200000,
                                           rng=rng, verbose=False)
        if e_mp < best_energy:
            best_energy = e_mp
            best_pts = pts_mp
            print(f"  Scale {scale:.0e} improved: {best_energy:.15f}")
            save_solution(best_pts, best_energy, f"micro_{scale:.0e}")
        else:
            print(f"  Scale {scale:.0e} no improvement")

    # Phase 4: Targeted perturbation
    print("\n[5] Phase 4: Targeted perturbation...")
    for scale in [1e-5, 1e-6, 1e-7, 1e-8]:
        pts_tp, e_tp = targeted_perturbation(best_pts.copy(), best_energy,
                                              scale=scale, n_trials=100000,
                                              rng=rng, verbose=False)
        if e_tp < best_energy:
            best_energy = e_tp
            best_pts = pts_tp
            print(f"  Targeted {scale:.0e} improved: {best_energy:.15f}")
            save_solution(best_pts, best_energy, f"targeted_{scale:.0e}")
        else:
            print(f"  Targeted {scale:.0e} no improvement")

    # Phase 5: Multi-point correlated moves
    print("\n[6] Phase 5: Multi-point correlated moves...")
    pts_mp, e_mp = multi_point_swap(best_pts.copy(), best_energy,
                                     n_trials=50000, rng=rng)
    if e_mp < best_energy:
        best_energy = e_mp
        best_pts = pts_mp
        save_solution(best_pts, best_energy, "multipoint")

    # Phase 6: Basin-hopping (try to find new basin)
    print("\n[7] Phase 6: Basin-hopping from SOTA...")
    for perturb in [0.1, 0.3, 0.5]:
        pts_bh, e_bh = basin_hopping(best_pts.copy(), best_energy,
                                      n_hops=100, perturb_scale=perturb,
                                      temperature=0.01, rng=rng, verbose=False)
        if e_bh < best_energy:
            best_energy = e_bh
            best_pts = pts_bh
            print(f"  BH perturb={perturb}: NEW BEST {best_energy:.15f}")
            save_solution(best_pts, best_energy, "basin_hop")
        else:
            print(f"  BH perturb={perturb}: no improvement (best found: {e_bh:.15f})")

    # Phase 7: Basin-hopping from Fibonacci seed
    print("\n[8] Phase 7: Basin-hopping from Fibonacci seed...")
    fib_pts = fibonacci_sphere(N)
    fib_energy = coulomb_energy(fib_pts)
    print(f"  Fibonacci initial: {fib_energy:.15f}")
    fib_pts, fib_energy = lbfgs_optimize(fib_pts, maxiter=5000, verbose=False)
    print(f"  Fibonacci + L-BFGS: {fib_energy:.15f}")
    if fib_energy < best_energy:
        best_energy = fib_energy
        best_pts = fib_pts
        save_solution(best_pts, best_energy, "fibonacci")

    # Final L-BFGS polish
    print("\n[9] Final L-BFGS polish...")
    pts_final, e_final = lbfgs_optimize(best_pts.copy(), maxiter=20000)
    if e_final < best_energy:
        best_energy = e_final
        best_pts = pts_final
        save_solution(best_pts, best_energy, "final")

    # Summary
    print("\n" + "=" * 70)
    print(f"FINAL RESULT: {best_energy:.15f}")
    print(f"Arena SOTA:   {e_arena:.15f}")
    print(f"Improvement:  {e_arena - best_energy:.2e}")
    print(f"Target:       {target:.15f}")
    if best_energy < target:
        print(">>> BELOW TARGET! Ready for submission <<<")
    else:
        print(f"Still {best_energy - target:.2e} above target")
    print("=" * 70)

    save_solution(best_pts, best_energy, "best")
    return best_pts, best_energy


if __name__ == "__main__":
    run_optimization()
