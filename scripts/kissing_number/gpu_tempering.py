"""GPU-accelerated parallel tempering for Kissing Number.

Pure PyTorch implementation — runs on any CUDA device (local, cloud, etc.).
Provider-agnostic: use with Modal, RunPod, Lambda, or local GPU.

Usage:
    # Local GPU:
    python scripts/kissing_number/gpu_tempering.py

    # Cloud GPU (set GPU_PROVIDER env var for your platform):
    GPU_PROVIDER=modal python scripts/kissing_number/gpu_tempering.py
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
    raise FileNotFoundError("No solution found in results dir")


def overlap_loss_batch(vecs_batch, device):
    """Full O(n²) overlap loss for a batch of configurations.
    vecs_batch: (B, N, D) tensor
    Returns: (B,) tensor
    """
    gram = torch.bmm(vecs_batch, vecs_batch.transpose(1, 2))
    idx_i, idx_j = torch.triu_indices(N, N, offset=1, device=device)
    cos_vals = gram[:, idx_i, idx_j].clamp(-1.0, 1.0)
    dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
    penalties = torch.clamp(2.0 - dists, min=0.0)
    return penalties.sum(dim=1)


def incremental_loss_vectorized(vecs_batch, indices, old_losses, old_vecs, device):
    """Vectorized batch incremental loss — no Python loop over B.
    vecs_batch: (B, N, D), indices: (B,), old_losses: (B,), old_vecs: (B, D)
    Returns: (B,) new losses
    """
    B = vecs_batch.shape[0]
    batch_idx = torch.arange(B, device=device)

    new_vecs = vecs_batch[batch_idx, indices]

    old_dots = torch.bmm(old_vecs.unsqueeze(1), vecs_batch.transpose(1, 2)).squeeze(1)
    new_dots = torch.bmm(new_vecs.unsqueeze(1), vecs_batch.transpose(1, 2)).squeeze(1)

    old_dots[batch_idx, indices] = -1.0
    new_dots[batch_idx, indices] = -1.0

    old_cos = old_dots.clamp(-1.0, 1.0)
    old_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - old_cos, min=0.0))
    old_p = torch.clamp(2.0 - old_d, min=0.0).sum(dim=1)

    new_cos = new_dots.clamp(-1.0, 1.0)
    new_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - new_cos, min=0.0))
    new_p = torch.clamp(2.0 - new_d, min=0.0).sum(dim=1)

    return old_losses - old_p + new_p


def compute_probs(vecs, device):
    """Contribution-weighted sampling probabilities."""
    gram = vecs @ vecs.T
    idx_i, idx_j = torch.triu_indices(N, N, offset=1, device=device)
    cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
    dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=0.0))
    pens = torch.clamp(2.0 - dists, min=0.0)
    c = torch.zeros(N, device=device, dtype=torch.float64)
    c.scatter_add_(0, idx_i, pens)
    c.scatter_add_(0, idx_j, pens)
    total = c.sum()
    return c / total if total > 0 else torch.ones(N, device=device, dtype=torch.float64) / N


def run_parallel_tempering(
    sota_np,
    n_replicas=64,
    n_iters=50_000_000,
    scale=1e-6,
    timeout_sec=7000,
):
    """Core parallel tempering algorithm. Runs on any CUDA device."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float64

    if device == "cpu":
        print("WARNING: No CUDA device — running on CPU (slow)")

    print(f"Device: {device}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    t0 = time.time()

    sota = torch.tensor(sota_np, device=device, dtype=dtype)
    sota_loss = overlap_loss_batch(sota.unsqueeze(0), device)[0].item()
    print(f"SOTA loss: {sota_loss:.15f}")

    temps = torch.tensor(np.geomspace(1e-12, 1e-4, n_replicas), device=device, dtype=dtype)
    print(f"Replicas: {n_replicas}, Temps: [{temps[0]:.1e}, ..., {temps[-1]:.1e}]")

    replicas = sota.unsqueeze(0).expand(n_replicas, -1, -1).clone()
    losses = overlap_loss_batch(replicas, device)

    best_loss = losses.min().item()
    best_vecs = replicas[losses.argmin()].clone()

    probs = compute_probs(replicas[0], device)

    swap_interval = 500
    recompute_every = 50_000
    accepts = torch.zeros(n_replicas, device=device, dtype=torch.long)
    swaps_attempted = 0
    swaps_accepted = 0

    print(f"Starting {n_iters:,} iterations...")

    for it in range(n_iters):
        if it > 0 and it % recompute_every == 0:
            probs = compute_probs(replicas[0], device)

        vec_indices = torch.multinomial(probs, n_replicas, replacement=True)
        batch_idx = torch.arange(n_replicas, device=device)
        old_vecs = replicas[batch_idx, vec_indices].clone()

        noise = torch.randn(n_replicas, D, device=device, dtype=dtype) * scale
        replicas[batch_idx, vec_indices] += noise
        new_norms = replicas[batch_idx, vec_indices].norm(dim=1, keepdim=True).clamp(min=1e-30)
        replicas[batch_idx, vec_indices] /= new_norms

        new_losses = incremental_loss_vectorized(replicas, vec_indices, losses, old_vecs, device)

        delta_E = new_losses - losses
        rand_vals = torch.rand(n_replicas, device=device, dtype=dtype)
        accept_prob = torch.exp((-delta_E / temps).clamp(max=0))
        accept_mask = (delta_E < 0) | (rand_vals < accept_prob)

        losses = torch.where(accept_mask, new_losses, losses)
        accepts += accept_mask.long()

        reject_mask = ~accept_mask
        if reject_mask.any():
            reject_idx = batch_idx[reject_mask]
            replicas[reject_idx, vec_indices[reject_mask]] = old_vecs[reject_mask]

        min_loss = losses.min().item()
        if min_loss < best_loss:
            best_loss = min_loss
            best_vecs = replicas[losses.argmin()].clone()

        if (it + 1) % swap_interval == 0:
            for r in range(n_replicas - 1):
                swaps_attempted += 1
                delta = (losses[r] - losses[r + 1]) * (1.0 / temps[r] - 1.0 / temps[r + 1])
                if torch.rand(1, device=device).item() < min(1.0, torch.exp(delta.clamp(max=50)).item()):
                    replicas[[r, r + 1]] = replicas[[r + 1, r]]
                    losses[[r, r + 1]] = losses[[r + 1, r]]
                    swaps_accepted += 1

        if (it + 1) % 1_000_000 == 0:
            elapsed = time.time() - t0
            exact = overlap_loss_batch(best_vecs.unsqueeze(0), device)[0].item()
            swap_rate = swaps_accepted / max(1, swaps_attempted) * 100
            speed = (it + 1) / elapsed

            print(f"\n  iter {it + 1:>10,d} | {elapsed:.0f}s | {speed:.0f} it/s")
            print(f"  BEST: {exact:.15f} (delta={sota_loss - exact:.2e})")
            print(f"  Swap rate: {swap_rate:.1f}%")
            for r in [0, n_replicas // 4, n_replicas // 2, 3 * n_replicas // 4, n_replicas - 1]:
                rate = accepts[r].item() / (it + 1) * 100
                print(f"    T={temps[r]:.1e}: loss={losses[r]:.10f}, accept={rate:.2f}%")

            accepts.zero_()
            swaps_attempted = 0
            swaps_accepted = 0

        if time.time() - t0 > timeout_sec:
            print(f"\nTimeout at iter {it + 1}")
            break

    final = overlap_loss_batch(best_vecs.unsqueeze(0), device)[0].item()
    elapsed = time.time() - t0

    print(f"\n{'=' * 70}")
    print(f"FINAL: {final:.15f}")
    print(f"SOTA:  {sota_loss:.15f}")
    print(f"Delta: {sota_loss - final:.2e}")
    print(f"Time:  {elapsed:.0f}s | {(it + 1) / elapsed:.0f} it/s")
    print(f"{'=' * 70}")

    return {
        "best_score": final,
        "sota_score": sota_loss,
        "delta": sota_loss - final,
        "best_vectors": best_vecs.cpu().numpy(),
        "elapsed_seconds": elapsed,
        "n_iters": it + 1,
    }


def save_result(result, tag="gpu_tempering"):
    """Save optimization result."""
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
    n_iters = int(os.environ.get("N_ITERS", "50000000"))
    timeout = int(os.environ.get("TIMEOUT", "7000"))

    result = run_parallel_tempering(
        vecs,
        n_replicas=n_replicas,
        n_iters=n_iters,
        scale=1e-6,
        timeout_sec=timeout,
    )
    save_result(result)
