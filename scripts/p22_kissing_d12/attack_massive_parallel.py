"""Massive parallel GPU search for the 841st vector position.

Leverages MPS (Metal Performance Shaders) on M5 Max: evaluate millions
of random unit vectors as candidate fillers, each scored against the
CHRONOS 840 core. Keep the best batch. Then refine best candidates on CPU
with exact Riemannian gradient descent in float64.

- Phase 1 (GPU): Sample B batches of M random unit vectors; compute hinge
  loss for each via batched matmul. Keep top-K per batch.
- Phase 2 (CPU, float64): Refine top candidates with exact hinge RGD.

Memory: 1M candidates × 12 dims × 4 bytes (fp32) = 48 MB each side; Gram
rows are 1M × 840 × 4 = 3.4 GB. Fits comfortably in 128 GB.
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

N = 841
D = 12
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


def score_filler_single(core: np.ndarray, v: np.ndarray) -> float:
    v = v / np.linalg.norm(v)
    gamma = core @ v
    g = np.clip(gamma, -1.0, 1.0)
    dist = 2.0 * np.sqrt(2.0 * (1.0 - g))
    return float(np.maximum(0.0, 2.0 - dist).sum())


def batch_score_filler_gpu(core_t: torch.Tensor, V_t: torch.Tensor) -> torch.Tensor:
    """Batched filler scoring on GPU/MPS.

    core_t: (840, 12), V_t: (B, 12) — unit vectors.
    Returns: (B,) scores (hinge sum per filler).
    """
    # Gram: (B, 840)
    gamma = V_t @ core_t.t()
    g = gamma.clamp(-1.0, 1.0)
    dist = 2.0 * torch.sqrt(2.0 * (1.0 - g))
    pen = (2.0 - dist).clamp(min=0.0)
    return pen.sum(dim=1)


def filler_rgd_cpu(core: np.ndarray, v0: np.ndarray, steps: int, lr: float) -> tuple[np.ndarray, float]:
    """Refine in float64 with exact Riemannian GD."""
    v = v0 / np.linalg.norm(v0)
    best_v = v.copy()
    best_s = score_filler_single(core, v)
    vel = np.zeros_like(v)
    cur_lr = lr
    for t in range(steps):
        gamma = core @ v
        mask = gamma > 0.5 + 1e-15
        if not np.any(mask):
            break
        g = np.clip(gamma[mask], -1.0, 1.0 - 1e-15)
        dh_dg = np.sqrt(2.0) / np.sqrt(1.0 - g)
        grad_ambient = (dh_dg[:, None] * core[mask]).sum(axis=0)
        grad = grad_ambient - (grad_ambient @ v) * v
        vel = 0.9 * vel + grad
        v = v - cur_lr * vel
        v /= np.linalg.norm(v)
        cur_lr *= 0.9995
        s = score_filler_single(core, v)
        if s < best_s:
            best_s = s
            best_v = v.copy()
    return best_v, best_s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-samples", type=int, default=10_000_000)
    ap.add_argument("--batch", type=int, default=1_000_000)
    ap.add_argument("--top-k", type=int, default=500)
    ap.add_argument("--refine-steps", type=int, default=3000)
    ap.add_argument("--refine-lr", type=float, default=5e-4)
    ap.add_argument("--seed", type=int, default=20260425)
    args = ap.parse_args()

    device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}", flush=True)
    dtype_gpu = torch.float32  # MPS performance

    core_np = load_core()
    core_t = torch.tensor(core_np, dtype=dtype_gpu, device=device)
    print(f"Core shape: {core_t.shape}", flush=True)

    gen = torch.Generator(device=device).manual_seed(args.seed)
    np_rng = np.random.default_rng(args.seed)

    total = args.n_samples
    top_k = args.top_k
    top_scores = torch.full((top_k,), float("inf"), device=device, dtype=dtype_gpu)
    top_vecs = torch.zeros((top_k, D), device=device, dtype=dtype_gpu)

    n_batches = (total + args.batch - 1) // args.batch
    print(f"Phase 1 (GPU): {total} samples in {n_batches} batches of {args.batch}", flush=True)
    t0 = time.time()

    for b in range(n_batches):
        B = min(args.batch, total - b * args.batch)
        # Sample B random unit vectors
        x = torch.randn(B, D, device=device, dtype=dtype_gpu, generator=gen)
        x = x / x.norm(dim=1, keepdim=True)
        scores = batch_score_filler_gpu(core_t, x)
        # Merge with top-K
        combined_scores = torch.cat([top_scores, scores])
        combined_vecs = torch.cat([top_vecs, x])
        idx = torch.topk(combined_scores, top_k, largest=False).indices
        top_scores = combined_scores[idx]
        top_vecs = combined_vecs[idx]
        if b % 5 == 0 or b == n_batches - 1:
            best_now = top_scores.min().item()
            elapsed = time.time() - t0
            rate = (b + 1) * args.batch / elapsed
            print(f"  batch {b+1}/{n_batches}  best={best_now:.6f}  rate={rate/1e6:.2f}M/s  ({elapsed:.1f}s)", flush=True)

    # Copy top-K to CPU for refinement
    top_scores_cpu = top_scores.cpu().numpy().astype(np.float64)
    top_vecs_cpu = top_vecs.cpu().numpy().astype(np.float64)
    # Sort ascending
    order = np.argsort(top_scores_cpu)
    top_scores_cpu = top_scores_cpu[order]
    top_vecs_cpu = top_vecs_cpu[order]
    print(f"\nPhase 1 done. Top-{top_k} GPU scores range: [{top_scores_cpu[0]:.6f}, {top_scores_cpu[-1]:.6f}]", flush=True)

    # Phase 2: refine with CPU float64 RGD
    print(f"\nPhase 2 (CPU float64): refine top-{top_k} with exact RGD", flush=True)
    t1 = time.time()
    best_overall_s = 2.0
    best_overall_v = None
    best_overall_source = "duplicate"

    refined = []
    for i in range(top_k):
        v0 = top_vecs_cpu[i] / np.linalg.norm(top_vecs_cpu[i])
        v_opt, s_opt = filler_rgd_cpu(core_np, v0, args.refine_steps, args.refine_lr)
        refined.append((s_opt, v_opt))
        if s_opt < best_overall_s:
            best_overall_s = s_opt
            best_overall_v = v_opt
            best_overall_source = f"rank{i}_gpu_score{top_scores_cpu[i]:.6f}"
            print(f"  refine[{i}]  initial={top_scores_cpu[i]:.6f}  refined={s_opt:.15f}  *** NEW BEST ***", flush=True)
        if i < 10 or i % 50 == 0:
            print(f"  refine[{i}]  initial={top_scores_cpu[i]:.6f}  refined={s_opt:.9f}", flush=True)

    elapsed_refine = time.time() - t1
    print(f"\nPhase 2 done in {elapsed_refine:.1f}s", flush=True)

    # Summary
    refined.sort(key=lambda x: x[0])
    print(f"\n=== Top 20 refined scores ===")
    for k, (s, _) in enumerate(refined[:20]):
        print(f"  {k:2d}:  {s:.15f}")

    print(f"\nBest overall refined score: {best_overall_s!r}")
    print(f"Source: {best_overall_source}")
    print(f"Improvement over 2.0: {2.0 - best_overall_s:+.6e}")

    if best_overall_v is not None and best_overall_s < 2.0:
        print(f"\n*** FOUND SUB-2.0 CONFIGURATION ***")
        vectors_out = np.vstack([core_np, best_overall_v[None, :]])
        out = {
            "method": "massive_parallel_gpu_search",
            "gpu_samples": args.n_samples,
            "best_score": best_overall_s,
            "source": best_overall_source,
            "vectors": vectors_out.tolist(),
        }
        json.dump(out, open(RESULTS_DIR / "attack_massive_best.json", "w"))
        print(f"Saved → {RESULTS_DIR / 'attack_massive_best.json'}")
    else:
        # Save what we have anyway for post-analysis
        best_s, best_v = refined[0]
        vectors_out = np.vstack([core_np, best_v[None, :]])
        out = {
            "method": "massive_parallel_gpu_search (no improvement)",
            "best_score": best_s,
            "refined_top20": [(float(s), v.tolist()) for s, v in refined[:20]],
            "vectors": vectors_out.tolist(),
        }
        json.dump(out, open(RESULTS_DIR / "attack_massive_best.json", "w"))


if __name__ == "__main__":
    main()
