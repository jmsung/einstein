"""GPU parallel tempering v2 — optimized for throughput.

Key optimizations over v1:
1. Batch K perturbations per replica per step (K=50, 50x more work per Python call)
2. Vectorized replica exchange (no Python for-loop)
3. Fused incremental loss computation
4. Pre-allocated tensors, minimal Python overhead in inner loop

Usage:
    # Direct (local GPU):
    python scripts/kissing_number/gpu_tempering_v2.py
    # Or via cloud GPU runner
"""

import json
import os
import time
from pathlib import Path

import numpy as np
import torch

RESULTS_DIR = Path("results/problem-6-kissing-number")
N = 594
D = 11


def load_best():
    for name in ["solution_best.json", "sota_vectors.json"]:
        path = RESULTS_DIR / name
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            vecs = np.array(data["vectors"], dtype=np.float64)
            norms = np.linalg.norm(vecs, axis=1, keepdims=True)
            return vecs / norms
    raise FileNotFoundError("No solution found")


def run_parallel_tempering_v2(
    sota_np,
    n_replicas=64,
    n_steps=2_000_000,
    k_per_step=50,
    scale=1e-6,
    timeout_sec=6900,
):
    """Optimized parallel tempering with batched perturbations.

    Each step perturbs K vectors per replica simultaneously.
    Effective perturbations per step = n_replicas * k_per_step.
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float64

    if device == "cpu":
        print("WARNING: No CUDA device — running on CPU (slow)")
    else:
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    t0 = time.time()

    # Initialize
    sota = torch.tensor(sota_np, device=device, dtype=dtype)

    # Full loss for verification
    def full_loss(vecs):
        gram = vecs @ vecs.T
        idx_i, idx_j = torch.triu_indices(N, N, offset=1, device=device)
        cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
        dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
        return torch.clamp(2.0 - dists, min=0.0).sum()

    def full_loss_batch(vecs_batch):
        gram = torch.bmm(vecs_batch, vecs_batch.transpose(1, 2))
        idx_i, idx_j = torch.triu_indices(N, N, offset=1, device=device)
        cos_vals = gram[:, idx_i, idx_j].clamp(-1.0, 1.0)
        dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
        return torch.clamp(2.0 - dists, min=0.0).sum(dim=1)

    sota_loss = full_loss(sota).item()
    print(f"SOTA loss: {sota_loss:.15f}")

    # Temperature ladder
    temps = torch.tensor(np.geomspace(1e-12, 1e-4, n_replicas), device=device, dtype=dtype)
    print(f"Replicas: {n_replicas}, K/step: {k_per_step}")
    print(f"Effective perturbations/step: {n_replicas * k_per_step}")
    print(f"Temps: [{temps[0]:.1e}, ..., {temps[-1]:.1e}]")

    # Replicas: (R, N, D)
    replicas = sota.unsqueeze(0).expand(n_replicas, -1, -1).clone()
    losses = full_loss_batch(replicas)

    best_loss = losses.min().item()
    best_vecs = replicas[losses.argmin()].clone()

    # Contribution probs
    def compute_probs(vecs):
        gram = vecs @ vecs.T
        idx_i, idx_j = torch.triu_indices(N, N, offset=1, device=device)
        cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
        dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
        pens = torch.clamp(2.0 - dists, min=0.0)
        c = torch.zeros(N, device=device, dtype=dtype)
        c.scatter_add_(0, idx_i, pens)
        c.scatter_add_(0, idx_j, pens)
        total = c.sum()
        return c / total if total > 0 else torch.ones(N, device=device, dtype=dtype) / N

    probs = compute_probs(replicas[0])

    # Pre-allocate
    R = n_replicas
    K = k_per_step
    batch_idx = torch.arange(R, device=device)

    swap_interval = 100  # steps (each step = K perturbations)
    recompute_every = 1000
    report_every = 10_000

    total_perturbations = 0
    total_accepts = 0
    swaps_attempted = 0
    swaps_accepted = 0

    print(f"Starting {n_steps:,} steps ({n_steps * R * K:,} total perturbations)...")

    for step in range(n_steps):
        if step > 0 and step % recompute_every == 0:
            probs = compute_probs(replicas[0])

        # ---- Batch perturbation: K vectors per replica ----
        # Sample K vector indices per replica (R, K)
        vec_indices = torch.multinomial(probs.expand(R, -1), K, replacement=False)  # (R, K)

        # For each of K perturbations, process independently
        # At scale 1e-6, cross-coupling between K perturbations is O(1e-6) — acceptable
        step_accepts = 0

        for k in range(K):
            k_indices = vec_indices[:, k]  # (R,)

            # Save old vectors: (R, D)
            old_vecs = replicas[batch_idx, k_indices].clone()

            # Perturb
            noise = torch.randn(R, D, device=device, dtype=dtype) * scale
            replicas[batch_idx, k_indices] += noise
            nrm = replicas[batch_idx, k_indices].norm(dim=1, keepdim=True).clamp(min=1e-30)
            replicas[batch_idx, k_indices] /= nrm

            # Vectorized incremental loss
            new_vecs = replicas[batch_idx, k_indices]  # (R, D)
            # Dot products: (R, D) @ (R, N, D).T → need bmm
            old_dots = torch.bmm(old_vecs.unsqueeze(1), replicas.transpose(1, 2)).squeeze(1)  # (R, N)
            new_dots = torch.bmm(new_vecs.unsqueeze(1), replicas.transpose(1, 2)).squeeze(1)  # (R, N)

            # Zero self-interaction
            old_dots[batch_idx, k_indices] = -1.0
            new_dots[batch_idx, k_indices] = -1.0

            old_cos = old_dots.clamp(-1.0, 1.0)
            old_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - old_cos, min=0.0))
            old_p = torch.clamp(2.0 - old_d, min=0.0).sum(dim=1)

            new_cos = new_dots.clamp(-1.0, 1.0)
            new_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - new_cos, min=0.0))
            new_p = torch.clamp(2.0 - new_d, min=0.0).sum(dim=1)

            new_losses = losses - old_p + new_p

            # Metropolis acceptance
            delta_E = new_losses - losses
            accept_prob = torch.exp((-delta_E / temps).clamp(max=0))
            accept_mask = (delta_E < 0) | (torch.rand(R, device=device, dtype=dtype) < accept_prob)

            losses = torch.where(accept_mask, new_losses, losses)
            step_accepts += accept_mask.sum().item()

            # Reject: restore old vectors
            reject_mask = ~accept_mask
            if reject_mask.any():
                replicas[batch_idx[reject_mask], k_indices[reject_mask]] = old_vecs[reject_mask]

        total_perturbations += R * K
        total_accepts += step_accepts

        # Track best
        min_loss = losses.min().item()
        if min_loss < best_loss:
            best_loss = min_loss
            best_vecs = replicas[losses.argmin()].clone()

        # ---- Vectorized replica exchange ----
        if (step + 1) % swap_interval == 0:
            # Attempt swaps between ALL adjacent pairs simultaneously
            # Even pairs: (0,1), (2,3), (4,5), ...
            # Odd pairs: (1,2), (3,4), (5,6), ...
            for parity in [0, 1]:
                r_lo = torch.arange(parity, R - 1, 2, device=device)
                r_hi = r_lo + 1

                if len(r_lo) == 0:
                    continue

                swaps_attempted += len(r_lo)

                delta = (losses[r_lo] - losses[r_hi]) * (1.0 / temps[r_lo] - 1.0 / temps[r_hi])
                swap_prob = torch.exp(delta.clamp(max=50))
                swap_mask = torch.rand(len(r_lo), device=device, dtype=dtype) < swap_prob

                if swap_mask.any():
                    swap_lo = r_lo[swap_mask]
                    swap_hi = r_hi[swap_mask]
                    swaps_accepted += swap_mask.sum().item()

                    # Swap replicas
                    temp_vecs = replicas[swap_lo].clone()
                    replicas[swap_lo] = replicas[swap_hi]
                    replicas[swap_hi] = temp_vecs

                    temp_losses = losses[swap_lo].clone()
                    losses[swap_lo] = losses[swap_hi]
                    losses[swap_hi] = temp_losses

        # Report
        if (step + 1) % report_every == 0:
            elapsed = time.time() - t0
            exact = full_loss(best_vecs).item()
            swap_rate = swaps_accepted / max(1, swaps_attempted) * 100
            accept_rate = total_accepts / max(1, total_perturbations) * 100
            perts_per_sec = total_perturbations / elapsed

            print(
                f"  step {step+1:>8,d} | {elapsed:.0f}s | "
                f"{perts_per_sec:.0f} perts/s | "
                f"BEST={exact:.15f} (Δ={sota_loss - exact:.2e}) | "
                f"accept={accept_rate:.2f}% | swap={swap_rate:.1f}%"
            )

            # Sample temperatures
            for r in [0, R // 4, R // 2, 3 * R // 4, R - 1]:
                print(f"    T={temps[r]:.1e}: loss={losses[r]:.10f}")

            total_accepts = 0
            total_perturbations = 0
            swaps_attempted = 0
            swaps_accepted = 0

        if time.time() - t0 > timeout_sec:
            print(f"\nTimeout at step {step + 1}")
            break

    # Final
    final = full_loss(best_vecs).item()
    elapsed = time.time() - t0
    effective_iters = (step + 1) * R * K

    print(f"\n{'=' * 70}")
    print(f"FINAL: {final:.15f}")
    print(f"SOTA:  {sota_loss:.15f}")
    print(f"Delta: {sota_loss - final:.2e}")
    print(f"Time:  {elapsed:.0f}s | {effective_iters / elapsed:.0f} perts/s")
    print(f"Total perturbations: {effective_iters:,}")
    print(f"{'=' * 70}")

    return {
        "best_score": final,
        "sota_score": sota_loss,
        "delta": sota_loss - final,
        "best_vectors": best_vecs.cpu().numpy(),
        "elapsed_seconds": elapsed,
        "total_perturbations": effective_iters,
    }


def save_result(result, tag="gpu_tempering_v2"):
    out_path = RESULTS_DIR / f"solution_{tag}.json"
    data = {
        "vectors": result["best_vectors"].tolist(),
        "score": result["best_score"],
        "tag": tag,
    }
    with open(out_path, "w") as f:
        json.dump(data, f)
    print(f"Saved to {out_path}")

    if result["delta"] > 0:
        best_path = RESULTS_DIR / "solution_best.json"
        with open(best_path, "w") as f:
            json.dump({"vectors": data["vectors"], "score": result["best_score"], "tag": "best"}, f)
        print(f"Updated {best_path}")


if __name__ == "__main__":
    vecs = load_best()
    n_replicas = int(os.environ.get("N_REPLICAS", "64"))
    n_steps = int(os.environ.get("N_STEPS", "2000000"))
    k_per_step = int(os.environ.get("K_PER_STEP", "50"))
    timeout = int(os.environ.get("TIMEOUT", "6900"))

    result = run_parallel_tempering_v2(
        vecs,
        n_replicas=n_replicas,
        n_steps=n_steps,
        k_per_step=k_per_step,
        scale=1e-6,
        timeout_sec=timeout,
    )
    save_result(result)
