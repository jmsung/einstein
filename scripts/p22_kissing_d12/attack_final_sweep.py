"""Final 50M GPU sweep — confirm 2.0 floor with mixed structured seeding.

Phase 1 (GPU, 50M positions, MPS): mix of seed strategies
- Pure random unit vectors (baseline)
- Spherical Fibonacci-like quasi-uniform points (proxy for 5-design)
- Antipodal-pair midpoints (cross gamma=-1 with gamma=+0.5 link)
- M_{12}-orbit-perturbed CHRONOS axes (e_i + small noise)

Phase 2 (CPU float64): refine top-2000 with exact-hinge Riemannian GD.

If all 50M samples still give best basin > 2.0, the empirical case is closed.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, "src")

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"


def load_core() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    v = np.array(data["vectors"], dtype=np.float64)
    seen = {}
    keep = []
    for i, row in enumerate(v):
        key = tuple(row.tolist())
        if key not in seen:
            seen[key] = i
            keep.append(i)
    return v[keep] / np.linalg.norm(v[keep], axis=1, keepdims=True)


def batch_score(core_t: torch.Tensor, V_t: torch.Tensor) -> torch.Tensor:
    gamma = V_t @ core_t.t()
    g = gamma.clamp(-1.0, 1.0)
    dist = 2.0 * torch.sqrt(2.0 * (1.0 - g))
    return (2.0 - dist).clamp(min=0.0).sum(dim=1)


def fibonacci_sphere_d12(n: int, device: str, dtype) -> torch.Tensor:
    """Generate quasi-uniform points on S^11 via golden-ratio sequencing in R^12.

    For high-dim, we use a generalization: orthogonal sequencing of frequencies.
    """
    phi = torch.tensor((1.0 + 5**0.5) / 2.0, device=device, dtype=dtype)
    idx = torch.arange(n, device=device, dtype=dtype)
    # 12 different "frequencies" via prime-spaced phi powers
    freqs = torch.tensor([phi ** (k + 1) for k in range(12)], device=device, dtype=dtype)
    angles = (idx[:, None] * freqs[None, :]) % (2 * torch.pi)
    coords = torch.cat([torch.cos(angles[:, :6]), torch.sin(angles[:, :6])], dim=1)
    coords = coords / coords.norm(dim=1, keepdim=True)
    return coords


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-samples", type=int, default=50_000_000)
    ap.add_argument("--batch", type=int, default=500_000)
    ap.add_argument("--top-k", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=20260425)
    args = ap.parse_args()

    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32
    print(f"Device: {device}", flush=True)

    core_np = load_core()
    core_t = torch.tensor(core_np, dtype=dtype, device=device)
    print(f"Core: {core_t.shape}", flush=True)

    gen = torch.Generator(device=device).manual_seed(args.seed)
    top_scores = torch.full((args.top_k,), float("inf"), device=device, dtype=dtype)
    top_vecs = torch.zeros((args.top_k, 12), device=device, dtype=dtype)

    total = args.n_samples
    n_batches = (total + args.batch - 1) // args.batch
    t0 = time.time()
    print(f"Phase 1: {total:,} samples in {n_batches} batches ({args.batch:,}/batch)", flush=True)

    for b in range(n_batches):
        B = min(args.batch, total - b * args.batch)
        # Mix: 70% random, 20% perturbed core (small scale), 10% mid-pair
        n_rand = int(0.7 * B)
        n_pert = int(0.2 * B)
        n_mid = B - n_rand - n_pert

        # 1. Random unit vectors
        x_rand = torch.randn(n_rand, 12, device=device, dtype=dtype, generator=gen)
        x_rand = x_rand / x_rand.norm(dim=1, keepdim=True)

        # 2. Perturbed core vectors (pick random core index, add Gaussian noise)
        idx_pert = torch.randint(0, 840, (n_pert,), device=device, generator=gen)
        scales = 10 ** (torch.rand(n_pert, device=device, generator=gen, dtype=dtype) * 3 - 4)  # 1e-4 to 0.1
        x_pert = core_t[idx_pert] + scales[:, None] * torch.randn(n_pert, 12, device=device, dtype=dtype, generator=gen)
        x_pert = x_pert / x_pert.norm(dim=1, keepdim=True)

        # 3. Pair midpoints (random pairs of core vectors)
        i_idx = torch.randint(0, 840, (n_mid,), device=device, generator=gen)
        j_idx = torch.randint(0, 840, (n_mid,), device=device, generator=gen)
        x_mid = core_t[i_idx] + core_t[j_idx]
        norms = x_mid.norm(dim=1, keepdim=True)
        # Avoid degeneracies (i==j or antipodal)
        mask = norms.squeeze(-1) > 1e-3
        x_mid_ok = x_mid[mask] / norms[mask]
        # Pad with random if any rejected
        n_pad = n_mid - x_mid_ok.shape[0]
        if n_pad > 0:
            x_pad = torch.randn(n_pad, 12, device=device, dtype=dtype, generator=gen)
            x_pad = x_pad / x_pad.norm(dim=1, keepdim=True)
            x_mid_ok = torch.cat([x_mid_ok, x_pad])

        x_batch = torch.cat([x_rand, x_pert, x_mid_ok])

        scores = batch_score(core_t, x_batch)
        combined_s = torch.cat([top_scores, scores])
        combined_v = torch.cat([top_vecs, x_batch])
        idx = torch.topk(combined_s, args.top_k, largest=False).indices
        top_scores = combined_s[idx]
        top_vecs = combined_v[idx]

        if b % 5 == 0 or b == n_batches - 1:
            elapsed = time.time() - t0
            best = top_scores.min().item()
            rate = (b + 1) * args.batch / elapsed / 1e6
            print(f"  batch {b+1:3d}/{n_batches}  best={best:.6f}  rate={rate:.2f}M/s  ({elapsed:.1f}s)", flush=True)

    elapsed_p1 = time.time() - t0
    print(f"\nPhase 1 done in {elapsed_p1:.1f}s.  GPU best = {top_scores.min().item():.6f}", flush=True)

    # Phase 2: refine top-K on CPU with exact RGD
    top_scores_cpu = top_scores.cpu().numpy().astype(np.float64)
    top_vecs_cpu = top_vecs.cpu().numpy().astype(np.float64)
    order = np.argsort(top_scores_cpu)
    print(f"\nPhase 2: refine top-{args.top_k} on CPU...", flush=True)

    def refine_one(v0, steps=2000, lr=5e-4):
        v = v0 / np.linalg.norm(v0)
        best_v = v.copy()
        gamma = core_np @ v
        mask = gamma > 0.5
        if not np.any(mask):
            return v, 0.0
        g = np.clip(gamma[mask], -1.0, 1.0)
        dist = 2.0 * np.sqrt(2.0 * (1.0 - g))
        best_s = float(np.maximum(0.0, 2.0 - dist).sum())
        vel = np.zeros_like(v)
        cur_lr = lr
        for t in range(steps):
            gamma = core_np @ v
            mask = gamma > 0.5 + 1e-15
            if not np.any(mask):
                return v, 0.0
            g = np.clip(gamma[mask], -1.0, 1.0 - 1e-15)
            dh_dg = np.sqrt(2.0) / np.sqrt(1.0 - g)
            grad_amb = (dh_dg[:, None] * core_np[mask]).sum(axis=0)
            grad = grad_amb - (grad_amb @ v) * v
            vel = 0.9 * vel + grad
            v = v - cur_lr * vel
            v /= np.linalg.norm(v)
            cur_lr *= 0.9995
            gamma = core_np @ v
            mask = gamma > 0.5
            if not np.any(mask):
                best_s = 0.0
                best_v = v.copy()
                break
            g = np.clip(gamma[mask], -1.0, 1.0)
            dist = 2.0 * np.sqrt(2.0 * (1.0 - g))
            s = float(np.maximum(0.0, 2.0 - dist).sum())
            if s < best_s:
                best_s = s
                best_v = v.copy()
        return best_v, best_s

    t1 = time.time()
    best_overall = 2.0
    best_v = None
    refined_scores = []
    for k, i in enumerate(order):
        v_opt, s_opt = refine_one(top_vecs_cpu[i])
        refined_scores.append(s_opt)
        if s_opt < best_overall - 1e-13:
            best_overall = s_opt
            best_v = v_opt
            print(f"  refine[{k:4d}]  init={top_scores_cpu[i]:.6f}  refined={s_opt:.15f}  *** NEW BEST ***", flush=True)
        if k < 5 or k % 200 == 0:
            print(f"  refine[{k:4d}]  init={top_scores_cpu[i]:.6f}  refined={s_opt:.9f}", flush=True)

    elapsed_p2 = time.time() - t1
    print(f"\nPhase 2 done in {elapsed_p2:.1f}s", flush=True)

    refined_scores = np.array(refined_scores)
    print(f"\n=== Refined basin distribution ({args.top_k} starts) ===")
    print(f"  min:  {refined_scores.min():.10f}")
    print(f"  10%:  {np.percentile(refined_scores, 10):.10f}")
    print(f"  50%:  {np.percentile(refined_scores, 50):.10f}")
    print(f"  90%:  {np.percentile(refined_scores, 90):.10f}")
    below_2 = (refined_scores < 2.0 - 1e-12).sum()
    print(f"  basins below 2.0: {below_2}/{len(refined_scores)}")
    print(f"\nFinal best: {best_overall!r}")

    out = RESULTS_DIR / "attack_final_sweep_50M.json"
    json.dump(
        {
            "n_samples": args.n_samples,
            "best_score": best_overall,
            "best_v": best_v.tolist() if best_v is not None else None,
            "refined_min": float(refined_scores.min()),
            "elapsed_total_sec": time.time() - t0,
        },
        open(out, "w"),
    )
    print(f"Saved → {out}")


if __name__ == "__main__":
    main()
