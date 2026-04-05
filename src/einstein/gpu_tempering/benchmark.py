"""Benchmark GPU approaches to decide which to use.

Runs each approach for a fixed time, measures perturbations/sec and GPU
utilization. Use this BEFORE committing to a long GPU run.

Usage:
    # Local GPU:
    python -m einstein.gpu_tempering.benchmark --solution results/problem-6-kissing-number/solution_best.json

    # Or import and call:
    from einstein.gpu_tempering.benchmark import run_benchmark
    result = run_benchmark(vectors, n_vectors=594, dim=11, loss_type="hinge")

Decision criteria:
    - If Level 2 (torch.compile) is >2x faster than Level 1 → use Level 2
    - If Level 2 GPU util < 50% → consider Level 3 (Triton)
    - If Level 2 GPU util > 70% → Level 3 not worth the effort
    - If CPU is within 3x of GPU → stay on CPU (no cloud cost)
"""

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch


def _get_gpu_util():
    """Get GPU utilization % (returns -1 if not available)."""
    try:
        import subprocess
        r = subprocess.run(
            ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=5,
        )
        return int(r.stdout.strip())
    except Exception:
        return -1


def _run_vanilla_pytorch(vecs_t, temps, n_replicas, scale, duration_sec, device):
    """Level 1: vanilla PyTorch ops in Python loop."""
    from einstein.gpu_tempering.losses import HingeOverlapLoss
    from einstein.gpu_tempering.manifolds import SphereManifold

    N, D = vecs_t.shape
    R = n_replicas
    loss_fn = HingeOverlapLoss()
    manifold = SphereManifold(dim=D)

    replicas = vecs_t.unsqueeze(0).expand(R, -1, -1).clone()
    losses = torch.stack([loss_fn.full_loss(replicas[r]) for r in range(R)])
    probs = loss_fn.contributions(replicas[0])
    probs = probs / probs.sum()
    batch_idx = torch.arange(R, device=device)

    perts = 0
    t0 = time.time()

    while time.time() - t0 < duration_sec:
        ki = torch.multinomial(probs, R, replacement=True)
        old_vecs = manifold.perturb_batch(replicas, ki, scale)
        deltas = loss_fn.batch_incremental_delta(replicas, ki, old_vecs)

        accept_prob = torch.exp((-deltas / temps).clamp(max=0))
        accept_mask = (deltas < 0) | (torch.rand(R, device=device, dtype=torch.float64) < accept_prob)
        losses += torch.where(accept_mask, deltas, torch.zeros_like(deltas))

        reject_mask = ~accept_mask
        if reject_mask.any():
            replicas[batch_idx[reject_mask], ki[reject_mask]] = old_vecs[reject_mask]

        perts += R

    elapsed = time.time() - t0
    return perts, elapsed, _get_gpu_util()


def _run_compiled_pytorch(vecs_t, temps, n_replicas, scale, duration_sec, device):
    """Level 2: torch.compile on the inner step."""
    from einstein.gpu_tempering.losses import HingeOverlapLoss
    from einstein.gpu_tempering.manifolds import SphereManifold

    N, D = vecs_t.shape
    R = n_replicas
    loss_fn = HingeOverlapLoss()
    manifold = SphereManifold(dim=D)

    replicas = vecs_t.unsqueeze(0).expand(R, -1, -1).clone()
    losses = torch.stack([loss_fn.full_loss(replicas[r]) for r in range(R)])
    probs = loss_fn.contributions(replicas[0])
    probs = probs / probs.sum()
    batch_idx = torch.arange(R, device=device)

    @torch.compile(mode="reduce-overhead")
    def step(replicas, losses, probs, temps):
        ki = torch.multinomial(probs.expand(R, -1), 1, replacement=True).squeeze(1)
        old_vecs = replicas[batch_idx, ki].clone()

        noise = torch.randn(R, D, device=device, dtype=torch.float64) * scale
        replicas[batch_idx, ki] += noise
        replicas[batch_idx, ki] /= replicas[batch_idx, ki].norm(dim=1, keepdim=True).clamp(min=1e-30)

        new_vecs = replicas[batch_idx, ki]
        od = torch.bmm(old_vecs.unsqueeze(1), replicas.transpose(1, 2)).squeeze(1)
        nd = torch.bmm(new_vecs.unsqueeze(1), replicas.transpose(1, 2)).squeeze(1)
        od[batch_idx, ki] = -1.0
        nd[batch_idx, ki] = -1.0

        op = torch.clamp(2.0 - 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - od.clamp(-1, 1), min=0.0)), min=0.0).sum(1)
        np_ = torch.clamp(2.0 - 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - nd.clamp(-1, 1), min=0.0)), min=0.0).sum(1)
        deltas = np_ - op

        accept_prob = torch.exp((-deltas / temps).clamp(max=0))
        accept_mask = (deltas < 0) | (torch.rand(R, device=device, dtype=torch.float64) < accept_prob)
        losses = losses + torch.where(accept_mask, deltas, torch.zeros_like(deltas))

        reject_mask = ~accept_mask
        if reject_mask.any():
            replicas[batch_idx[reject_mask], ki[reject_mask]] = old_vecs[reject_mask]

        return replicas, losses

    # Warmup (torch.compile needs a few runs to compile)
    print("    Compiling (warmup)...", end=" ", flush=True)
    for _ in range(10):
        replicas, losses = step(replicas, losses, probs, temps)
    torch.cuda.synchronize() if device == "cuda" else None
    print("done")

    perts = 0
    t0 = time.time()

    while time.time() - t0 < duration_sec:
        replicas, losses = step(replicas, losses, probs, temps)
        perts += R

    elapsed = time.time() - t0
    return perts, elapsed, _get_gpu_util()


def _run_cpu_baseline(vecs_np, scale, duration_sec):
    """CPU baseline for comparison."""
    N, D = vecs_np.shape
    rng = np.random.default_rng(42)

    vecs = vecs_np.copy()
    gram = vecs @ vecs.T
    idx_i, idx_j = np.triu_indices(N, k=1)
    cos_vals = np.clip(gram[idx_i, idx_j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    current_loss = float(np.sum(np.maximum(0.0, 2.0 - dists)))

    perts = 0
    t0 = time.time()

    while time.time() - t0 < duration_sec:
        idx = rng.integers(N)
        old_vec = vecs[idx].copy()
        vecs[idx] += rng.standard_normal(D) * scale
        vecs[idx] /= np.linalg.norm(vecs[idx])

        others = np.concatenate([vecs[:idx], vecs[idx + 1:]], axis=0)
        old_cos = np.clip(old_vec @ others.T, -1.0, 1.0)
        old_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - old_cos))
        old_p = np.maximum(0.0, 2.0 - old_d)
        new_cos = np.clip(vecs[idx] @ others.T, -1.0, 1.0)
        new_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - new_cos))
        new_p = np.maximum(0.0, 2.0 - new_d)
        new_loss = current_loss - float(np.sum(old_p)) + float(np.sum(new_p))

        if new_loss < current_loss:
            current_loss = new_loss
        else:
            vecs[idx] = old_vec

        perts += 1

    elapsed = time.time() - t0
    return perts, elapsed


def run_benchmark(
    vectors: np.ndarray,
    n_replicas: int = 64,
    scale: float = 1e-6,
    duration_sec: float = 30,
) -> dict:
    """Run benchmark comparing all GPU approaches.

    Args:
        vectors: (N, D) initial vectors
        n_replicas: number of SA replicas for GPU methods
        scale: perturbation scale
        duration_sec: how long to run each approach

    Returns:
        dict with results and recommendation
    """
    N, D = vectors.shape
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float64

    print(f"Benchmarking: N={N}, D={D}, R={n_replicas}, scale={scale:.0e}")
    print(f"Device: {device}" + (f" ({torch.cuda.get_device_name(0)})" if device == "cuda" else ""))
    print(f"Duration: {duration_sec}s per approach\n")

    vecs_t = torch.tensor(vectors, device=device, dtype=dtype)
    vecs_t = vecs_t / vecs_t.norm(dim=1, keepdim=True)
    temps = torch.tensor(np.geomspace(1e-12, 1e-4, n_replicas), device=device, dtype=dtype)

    results = {}

    # CPU baseline
    print("  [CPU] Greedy micro-perturbation (1 replica)...")
    cpu_perts, cpu_time = _run_cpu_baseline(vectors, scale, duration_sec)
    cpu_pps = cpu_perts / cpu_time
    results["cpu"] = {"perts": cpu_perts, "time": cpu_time, "pps": cpu_pps, "gpu_util": 0}
    print(f"    {cpu_pps:.0f} perturbations/sec\n")

    if device == "cuda":
        # Level 1: Vanilla PyTorch
        print(f"  [GPU L1] Vanilla PyTorch ({n_replicas} replicas)...")
        l1_perts, l1_time, l1_util = _run_vanilla_pytorch(
            vecs_t, temps, n_replicas, scale, duration_sec, device
        )
        l1_pps = l1_perts / l1_time
        results["gpu_vanilla"] = {"perts": l1_perts, "time": l1_time, "pps": l1_pps, "gpu_util": l1_util}
        print(f"    {l1_pps:.0f} perturbations/sec, GPU util: {l1_util}%\n")

        # Level 2: torch.compile
        print(f"  [GPU L2] torch.compile ({n_replicas} replicas)...")
        try:
            l2_perts, l2_time, l2_util = _run_compiled_pytorch(
                vecs_t, temps, n_replicas, scale, duration_sec, device
            )
            l2_pps = l2_perts / l2_time
            results["gpu_compiled"] = {"perts": l2_perts, "time": l2_time, "pps": l2_pps, "gpu_util": l2_util}
            print(f"    {l2_pps:.0f} perturbations/sec, GPU util: {l2_util}%\n")
        except Exception as e:
            print(f"    FAILED: {e}\n")
            results["gpu_compiled"] = None

    if device == "cuda":
        # Level 2b: Fused step (batched R×K)
        print(f"  [GPU L2b] Fused R×K step (K=5, {n_replicas} replicas)...")
        try:
            from einstein.gpu_tempering.fused_step import fused_sa_step
            from einstein.gpu_tempering.losses import HingeOverlapLoss
            loss_fn = HingeOverlapLoss()

            f_replicas = vecs_t.unsqueeze(0).expand(n_replicas, -1, -1).clone()
            f_losses = torch.stack([loss_fn.full_loss(f_replicas[r]) for r in range(n_replicas)])
            f_probs = loss_fn.contributions(f_replicas[0])
            f_probs = f_probs / f_probs.sum()

            K_bench = 5
            f_perts = 0
            f_t0 = time.time()
            while time.time() - f_t0 < duration_sec:
                f_losses, na = fused_sa_step(f_replicas, f_losses, temps, f_probs, scale, K_bench, "hinge")
                f_perts += n_replicas * K_bench
            f_elapsed = time.time() - f_t0
            f_pps = f_perts / f_elapsed
            f_util = _get_gpu_util()
            results["gpu_fused"] = {"perts": f_perts, "time": f_elapsed, "pps": f_pps, "gpu_util": f_util}
            print(f"    {f_pps:.0f} perturbations/sec, GPU util: {f_util}%\n")
        except Exception as e:
            print(f"    FAILED: {e}\n")
            results["gpu_fused"] = None

        # Level 3: Triton kernel
        print(f"  [GPU L3] Triton kernel (K=5, {n_replicas} replicas)...")
        try:
            from einstein.gpu_tempering.triton_kernel import triton_sa_step, HAS_TRITON
            if not HAS_TRITON:
                print("    SKIPPED: Triton not installed\n")
                results["gpu_triton"] = None
            else:
                t_replicas = vecs_t.unsqueeze(0).expand(n_replicas, -1, -1).clone()
                t_losses = torch.stack([loss_fn.full_loss(t_replicas[r]) for r in range(n_replicas)])
                t_probs = loss_fn.contributions(t_replicas[0])
                t_probs = t_probs / t_probs.sum()

                # Warmup
                for _ in range(3):
                    t_losses, _ = triton_sa_step(t_replicas, t_losses, temps, t_probs, scale, K_bench, "hinge")
                torch.cuda.synchronize()

                t_perts = 0
                t_t0 = time.time()
                while time.time() - t_t0 < duration_sec:
                    t_losses, na = triton_sa_step(t_replicas, t_losses, temps, t_probs, scale, K_bench, "hinge")
                    t_perts += n_replicas * K_bench
                t_elapsed = time.time() - t_t0
                t_pps = t_perts / t_elapsed
                t_util = _get_gpu_util()
                results["gpu_triton"] = {"perts": t_perts, "time": t_elapsed, "pps": t_pps, "gpu_util": t_util}
                print(f"    {t_pps:.0f} perturbations/sec, GPU util: {t_util}%\n")
        except Exception as e:
            print(f"    FAILED: {e}\n")
            results["gpu_triton"] = None

    # Analysis and recommendation
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)

    cpu_pps = results["cpu"]["pps"]
    print(f"  CPU:          {cpu_pps:>10,.0f} perts/sec (baseline)")

    recommendation = "cpu"
    best_pps = cpu_pps

    if "gpu_vanilla" in results:
        g1 = results["gpu_vanilla"]
        speedup = g1["pps"] / cpu_pps
        print(f"  GPU vanilla:  {g1['pps']:>10,.0f} perts/sec ({speedup:.1f}x CPU, {g1['gpu_util']}% util)")
        if g1["pps"] > best_pps * 3:  # need >3x to justify cloud cost
            recommendation = "gpu_vanilla"
            best_pps = g1["pps"]

    if results.get("gpu_compiled"):
        g2 = results["gpu_compiled"]
        speedup = g2["pps"] / cpu_pps
        compile_boost = g2["pps"] / results["gpu_vanilla"]["pps"] if "gpu_vanilla" in results else 0
        print(f"  GPU compiled: {g2['pps']:>10,.0f} perts/sec ({speedup:.1f}x CPU, {g2['gpu_util']}% util, {compile_boost:.1f}x vs vanilla)")
        if g2["pps"] > best_pps:
            recommendation = "gpu_compiled"
            best_pps = g2["pps"]

    if results.get("gpu_fused"):
        gf = results["gpu_fused"]
        speedup = gf["pps"] / cpu_pps
        print(f"  GPU fused:    {gf['pps']:>10,.0f} perts/sec ({speedup:.1f}x CPU, {gf['gpu_util']}% util)")
        if gf["pps"] > best_pps:
            recommendation = "gpu_fused"
            best_pps = gf["pps"]

    if results.get("gpu_triton"):
        gt = results["gpu_triton"]
        speedup = gt["pps"] / cpu_pps
        print(f"  GPU Triton:   {gt['pps']:>10,.0f} perts/sec ({speedup:.1f}x CPU, {gt['gpu_util']}% util)")
        if gt["pps"] > best_pps:
            recommendation = "gpu_triton"
            best_pps = gt["pps"]

    print()

    # Decision logic
    gpu_util = 0
    for key in ["gpu_triton", "gpu_fused", "gpu_compiled", "gpu_vanilla"]:
        if results.get(key):
            gpu_util = results[key]["gpu_util"]
            break

    if recommendation == "cpu":
        verdict = "STAY ON CPU — GPU speedup < 3x, not worth cloud cost"
    elif recommendation == "gpu_triton":
        verdict = f"USE TRITON — best throughput ({best_pps:,.0f} p/s, {gpu_util}% util)"
    elif recommendation == "gpu_fused":
        verdict = f"USE FUSED STEP — good throughput ({best_pps:,.0f} p/s, {gpu_util}% util)"
    elif gpu_util > 70:
        verdict = f"USE {recommendation.upper()} — good utilization ({gpu_util}%)"
    elif gpu_util > 50:
        verdict = f"USE {recommendation.upper()} — moderate utilization ({gpu_util}%), fused step may help"
    else:
        verdict = f"USE {recommendation.upper()} — low utilization ({gpu_util}%), try fused step or Triton"

    print(f"RECOMMENDATION: {verdict}")

    # Quick reference
    print()
    print("QUICK REFERENCE — how to run the recommended approach:")
    if "fused" in recommendation or "triton" in recommendation:
        runner = "run_triton_tempering" if "triton" in recommendation else "run_fused_tempering"
        print(f"  from einstein.gpu_tempering import {runner}")
        print(f"  result = {runner}(vectors, n_replicas=64, n_steps=200000, k_per_step=5)")
    elif "gpu" in recommendation:
        print("  from einstein.gpu_tempering import ParallelTemperingSA, HingeOverlapLoss, SphereManifold")
        print("  sa = ParallelTemperingSA(HingeOverlapLoss(), SphereManifold(D), N)")
        print("  result = sa.run(vectors)")
    else:
        print("  Use CPU micro-perturbation — no GPU benefit for this problem size.")

    results["recommendation"] = recommendation
    results["verdict"] = verdict
    return results


def main():
    parser = argparse.ArgumentParser(description="Benchmark GPU approaches")
    parser.add_argument("--solution", type=str, required=True, help="Path to solution JSON")
    parser.add_argument("--replicas", type=int, default=64)
    parser.add_argument("--scale", type=float, default=1e-6)
    parser.add_argument("--duration", type=float, default=30, help="Seconds per approach")
    args = parser.parse_args()

    with open(args.solution) as f:
        data = json.load(f)
    vecs = np.array(data["vectors"], dtype=np.float64)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    vecs = vecs / norms

    run_benchmark(vecs, n_replicas=args.replicas, scale=args.scale, duration_sec=args.duration)


if __name__ == "__main__":
    main()
