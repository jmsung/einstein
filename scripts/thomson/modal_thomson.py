"""GPU-accelerated Thomson problem optimizer on Modal.

Runs massive parallel basin-hopping with PyTorch on A100.
Searches for undiscovered low-energy basins for n=282.
"""

import json
import modal

app = modal.App("thomson-n282")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=3600,  # 60 min
    memory=32768,
)
def massive_basin_hopping(sota_vectors: list[list[float]], n_parallel: int = 256,
                           n_hops: int = 2000) -> dict:
    """Run massive parallel basin-hopping on GPU."""
    import torch
    import numpy as np
    import time

    device = 'cuda'
    dtype = torch.float64
    N = 282
    t0 = time.time()

    # ---- Energy computation on GPU ----
    def coulomb_energy_batch(pts_batch):
        """Compute Coulomb energy for a batch of configurations.
        pts_batch: (B, N, 3) tensor on GPU
        Returns: (B,) tensor of energies
        """
        B = pts_batch.shape[0]
        # Normalize to unit sphere
        norms = torch.norm(pts_batch, dim=2, keepdim=True).clamp(min=1e-12)
        pts = pts_batch / norms

        # Pairwise distances: (B, N, N)
        diff = pts.unsqueeze(2) - pts.unsqueeze(1)  # (B, N, N, 3)
        dist_sq = (diff * diff).sum(dim=3)  # (B, N, N)

        # Upper triangular mask
        mask = torch.triu(torch.ones(N, N, device=device, dtype=torch.bool), diagonal=1)
        mask = mask.unsqueeze(0).expand(B, -1, -1)

        dists = torch.sqrt(dist_sq[mask].reshape(B, -1)).clamp(min=1e-12)
        energies = (1.0 / dists).sum(dim=1)
        return energies

    def coulomb_energy_single(pts):
        """Single configuration energy."""
        return coulomb_energy_batch(pts.unsqueeze(0))[0]

    def coulomb_gradient(pts):
        """Gradient for single config via autograd."""
        pts_var = pts.clone().requires_grad_(True)
        e = coulomb_energy_single(pts_var)
        e.backward()
        return pts_var.grad.clone()

    def normalize_sphere(pts):
        """Project to unit sphere."""
        return pts / torch.norm(pts, dim=-1, keepdim=True).clamp(min=1e-12)

    def random_sphere_points(n, batch=1):
        """Generate random points on unit sphere."""
        pts = torch.randn(batch, n, 3, device=device, dtype=dtype)
        return normalize_sphere(pts)

    # ---- L-BFGS local optimization on GPU ----
    def lbfgs_optimize_gpu(pts, max_iter=2000):
        """L-BFGS optimization with spherical projection."""
        best_pts = pts.clone()
        best_energy = coulomb_energy_single(pts).item()

        # Spherical coordinates
        x, y, z = pts[:, 0], pts[:, 1], pts[:, 2]
        theta = torch.arccos(z.clamp(-1, 1))
        phi = torch.atan2(y, x)
        params = torch.stack([theta, phi], dim=1).requires_grad_(True)

        def sph_to_cart(p):
            t, f = p[:, 0], p[:, 1]
            return torch.stack([
                torch.sin(t) * torch.cos(f),
                torch.sin(t) * torch.sin(f),
                torch.cos(t)
            ], dim=1)

        optimizer = torch.optim.LBFGS([params], lr=1.0, max_iter=20,
                                        history_size=50, line_search_fn='strong_wolfe')

        for i in range(max_iter // 20):
            def closure():
                optimizer.zero_grad()
                cart = sph_to_cart(params)
                e = coulomb_energy_single(cart)
                e.backward()
                return e

            optimizer.step(closure)
            with torch.no_grad():
                cart = sph_to_cart(params)
                e = coulomb_energy_single(cart).item()
                if e < best_energy:
                    best_energy = e
                    best_pts = cart.clone()

        return best_pts, best_energy

    # ---- Riemannian gradient descent (fast, on GPU) ----
    def riemannian_gd_gpu(pts, lr=1e-6, steps=5000):
        """Fast Riemannian GD on GPU with adaptive step size."""
        best_pts = pts.clone()
        best_energy = coulomb_energy_single(pts).item()

        for step in range(steps):
            pts_var = pts.clone().requires_grad_(True)
            e = coulomb_energy_single(pts_var)
            e.backward()
            grad = pts_var.grad

            # Project to tangent plane
            dots = (grad * pts).sum(dim=1, keepdim=True)
            grad_tan = grad - dots * pts

            # Step
            with torch.no_grad():
                pts = pts - lr * grad_tan
                pts = normalize_sphere(pts)

                if step % 100 == 0:
                    e_val = coulomb_energy_single(pts).item()
                    if e_val < best_energy:
                        best_energy = e_val
                        best_pts = pts.clone()

        return best_pts, best_energy

    # ---- Main campaign ----
    results = {
        "method": "gpu_massive_basin_hopping",
        "n_parallel": n_parallel,
        "n_hops": n_hops,
        "energies": [],
        "best_energy": float('inf'),
        "best_vectors": None,
        "n_completed": 0,
    }

    # Load SOTA
    sota = torch.tensor(sota_vectors, device=device, dtype=dtype)
    sota = normalize_sphere(sota)
    sota_energy = coulomb_energy_single(sota).item()
    print(f"SOTA energy (GPU): {sota_energy:.15f}")
    results["sota_energy_gpu"] = sota_energy

    # Phase 1: Riemannian GD polish from SOTA (high precision)
    print("\n=== Phase 1: GPU Riemannian GD polish ===")
    for lr in [1e-7, 1e-8, 1e-9, 1e-10]:
        pts_gd, e_gd = riemannian_gd_gpu(sota.clone(), lr=lr, steps=10000)
        print(f"  GD lr={lr:.0e}: E = {e_gd:.15f}")
        if e_gd < results["best_energy"]:
            results["best_energy"] = e_gd
            results["best_vectors"] = pts_gd.cpu().numpy().tolist()

    # Phase 2: L-BFGS polish from SOTA
    print("\n=== Phase 2: GPU L-BFGS polish ===")
    pts_lb, e_lb = lbfgs_optimize_gpu(sota.clone(), max_iter=5000)
    print(f"  L-BFGS: E = {e_lb:.15f}")
    if e_lb < results["best_energy"]:
        results["best_energy"] = e_lb
        results["best_vectors"] = pts_lb.cpu().numpy().tolist()

    # Phase 3: Massive random restart campaign
    print(f"\n=== Phase 3: Random restarts ({n_parallel} parallel) ===")
    batch_energies = []
    n_batches = max(1, n_hops // n_parallel)

    for batch in range(n_batches):
        if time.time() - t0 > 2400:  # 40 min limit
            print(f"  Time limit reached at batch {batch}")
            break

        # Generate random starting points
        starts = random_sphere_points(N, n_parallel)

        # Evaluate batch
        init_energies = coulomb_energy_batch(starts)

        # Optimize top candidates
        sorted_idx = torch.argsort(init_energies)
        n_optimize = min(16, n_parallel)

        for rank in range(n_optimize):
            idx = sorted_idx[rank].item()
            pts_opt, e_opt = lbfgs_optimize_gpu(starts[idx], max_iter=2000)
            batch_energies.append(e_opt)

            if e_opt < results["best_energy"]:
                results["best_energy"] = e_opt
                results["best_vectors"] = pts_opt.cpu().numpy().tolist()
                print(f"  Batch {batch}, rank {rank}: NEW BEST E = {e_opt:.15f}")

            results["n_completed"] += 1

        if batch % 10 == 0:
            elapsed = time.time() - t0
            print(f"  Batch {batch}/{n_batches}: {results['n_completed']} completed, "
                  f"best = {results['best_energy']:.10f}, "
                  f"time = {elapsed:.0f}s")

    # Phase 4: Basin-hopping from SOTA
    print(f"\n=== Phase 4: Basin-hopping from SOTA ({n_hops} hops) ===")
    current = sota.clone()
    current_energy = sota_energy
    bh_best = sota_energy
    bh_best_pts = sota.clone()

    for hop in range(n_hops):
        if time.time() - t0 > 3300:  # 55 min limit
            print(f"  Time limit reached at hop {hop}")
            break

        trial = current.clone()

        # Perturb: move 1-30 points
        n_move = torch.randint(1, 31, (1,)).item()
        indices = torch.randperm(N, device=device)[:n_move]

        for idx in indices:
            noise = torch.randn(3, device=device, dtype=dtype) * 0.3
            noise -= torch.dot(noise, trial[idx]) * trial[idx]
            trial[idx] += noise
            trial[idx] = trial[idx] / torch.norm(trial[idx])

        # Local minimize
        trial, trial_energy = lbfgs_optimize_gpu(trial, max_iter=1000)

        # Metropolis
        delta = trial_energy - current_energy
        temp = 0.01
        if delta < 0 or torch.rand(1).item() < np.exp(-delta / temp):
            current = trial
            current_energy = trial_energy

            if trial_energy < bh_best:
                bh_best = trial_energy
                bh_best_pts = trial.clone()
                print(f"  Hop {hop}: NEW BEST E = {bh_best:.15f}")

        if hop % 100 == 0:
            elapsed = time.time() - t0
            print(f"  Hop {hop}/{n_hops}: best = {bh_best:.10f}, "
                  f"current = {current_energy:.10f}, time = {elapsed:.0f}s")

    if bh_best < results["best_energy"]:
        results["best_energy"] = bh_best
        results["best_vectors"] = bh_best_pts.cpu().numpy().tolist()

    # Phase 5: Simulated annealing with very slow cooling
    print(f"\n=== Phase 5: Simulated annealing ===")
    sa_pts = sota.clone()
    sa_energy = sota_energy
    sa_best = sota_energy
    sa_best_pts = sota.clone()
    T_max, T_min = 1.0, 1e-6
    sa_steps = 5000

    for step in range(sa_steps):
        if time.time() - t0 > 3500:
            break

        T = T_max * (T_min / T_max) ** (step / sa_steps)

        trial = sa_pts.clone()
        n_move = max(1, int(N * T / T_max))
        n_move = min(n_move, N)
        indices = torch.randperm(N, device=device)[:n_move]

        scale = max(0.01, T)
        for idx in indices:
            noise = torch.randn(3, device=device, dtype=dtype) * scale
            noise -= torch.dot(noise, trial[idx]) * trial[idx]
            trial[idx] += noise
            trial[idx] /= torch.norm(trial[idx])

        trial_energy = coulomb_energy_single(trial).item()

        delta = trial_energy - sa_energy
        if delta < 0 or torch.rand(1).item() < np.exp(-delta / T):
            sa_pts = trial
            sa_energy = trial_energy

            if sa_energy < sa_best:
                sa_best = sa_energy
                sa_best_pts = sa_pts.clone()

        if step % 500 == 0:
            print(f"  SA step {step}: T={T:.6f}, E={sa_energy:.10f}, best={sa_best:.10f}")

    # Polish SA result
    if sa_best < results["best_energy"] + 10:
        sa_best_pts, sa_best = lbfgs_optimize_gpu(sa_best_pts, max_iter=3000)
        if sa_best < results["best_energy"]:
            results["best_energy"] = sa_best
            results["best_vectors"] = sa_best_pts.cpu().numpy().tolist()

    # Summary
    elapsed = time.time() - t0
    results["elapsed_seconds"] = elapsed
    results["energies"] = sorted(batch_energies)[:20]  # Top 20 energies found
    print(f"\n{'='*60}")
    print(f"FINAL BEST: {results['best_energy']:.15f}")
    print(f"SOTA:       {sota_energy:.15f}")
    print(f"Gap:        {results['best_energy'] - sota_energy:.2e}")
    print(f"Elapsed:    {elapsed:.0f}s")
    print(f"Restarts:   {results['n_completed']}")
    print(f"{'='*60}")

    return results


@app.local_entrypoint()
def main():
    import json
    from pathlib import Path

    results_dir = Path("results/problem-10-thomson")

    # Load SOTA
    with open(results_dir / "sota_arena.json") as f:
        sota = json.load(f)

    print("Launching GPU optimization on Modal A100...")
    result = massive_basin_hopping.remote(
        sota_vectors=sota["vectors"],
        n_parallel=256,
        n_hops=2000,
    )

    print(f"\nBest energy: {result['best_energy']:.15f}")
    print(f"SOTA energy: {result['sota_energy_gpu']:.15f}")
    print(f"Gap: {result['best_energy'] - result['sota_energy_gpu']:.2e}")
    print(f"Elapsed: {result['elapsed_seconds']:.0f}s")
    print(f"Restarts: {result['n_completed']}")

    # Save result
    if result["best_vectors"]:
        out_path = results_dir / "solution_gpu.json"
        with open(out_path, "w") as f:
            json.dump({
                "vectors": result["best_vectors"],
                "score": result["best_energy"],
                "tag": "gpu_modal",
            }, f)
        print(f"\nSaved to {out_path}")

    # Save full results
    results_path = results_dir / "gpu_results.json"
    result_save = {k: v for k, v in result.items() if k != "best_vectors"}
    with open(results_path, "w") as f:
        json.dump(result_save, f, indent=2)
    print(f"Results saved to {results_path}")
