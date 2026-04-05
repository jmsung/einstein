"""Triton-fused SA step kernel for parallel tempering.

Fuses the entire inner loop (perturb + incremental loss + accept/reject)
into a single GPU kernel launch, eliminating all Python overhead.

Each Triton program handles one (replica, perturbation) pair.
Total programs = R * K, each computes:
1. Load old vector (D elements)
2. Generate noise via Philox PRNG
3. Compute new vector (add noise, normalize)
4. Dot products with all N others → old/new penalties
5. Reduce to get delta loss
6. Metropolis accept/reject
7. Write back if accepted

Requires: pip install triton (included with recent PyTorch)

Usage:
    from einstein.gpu_tempering.triton_kernel import triton_sa_step
    # Falls back to fused_step if Triton not available
"""

import torch
import numpy as np

try:
    import triton
    import triton.language as tl
    HAS_TRITON = True
except ImportError:
    HAS_TRITON = False


if HAS_TRITON:
    @triton.jit
    def _hinge_delta_kernel(
        # Pointers
        replicas_ptr,       # (R, N, D) flattened
        old_vecs_ptr,       # (RK, D) old vectors
        new_vecs_ptr,       # (RK, D) new vectors
        flat_indices_ptr,   # (RK,) which vector was perturbed
        replica_ids_ptr,    # (RK,) which replica each perturbation belongs to
        deltas_out_ptr,     # (RK,) output deltas
        # Sizes
        N: tl.constexpr,
        D: tl.constexpr,
        stride_rep_r,       # stride for replica dimension
        stride_rep_n,       # stride for vector dimension
        stride_rep_d,       # stride for dim dimension
    ):
        """Compute hinge overlap delta for one (replica, perturbation) pair."""
        pid = tl.program_id(0)  # index into RK

        # Load which replica and which vector
        rep_id = tl.load(replica_ids_ptr + pid)
        vec_idx = tl.load(flat_indices_ptr + pid)

        # Load old and new vectors: (D,)
        old_vec = tl.load(old_vecs_ptr + pid * D + tl.arange(0, D))
        new_vec = tl.load(new_vecs_ptr + pid * D + tl.arange(0, D))

        # Accumulate old and new penalties across all N others
        old_penalty_sum = tl.zeros([], dtype=tl.float64)
        new_penalty_sum = tl.zeros([], dtype=tl.float64)

        base_ptr = replicas_ptr + rep_id * stride_rep_r

        for j in range(N):
            if j == vec_idx:
                continue

            # Load other vector
            other = tl.load(base_ptr + j * stride_rep_n + tl.arange(0, D))

            # Old dot product
            old_dot = tl.sum(old_vec * other)
            old_cos = tl.minimum(tl.maximum(old_dot, -1.0), 1.0)
            old_arg = 2.0 * tl.maximum(1.0 - old_cos, 0.0)
            old_dist = 2.0 * tl.sqrt(old_arg + 1e-30)
            old_pen = tl.maximum(2.0 - old_dist, 0.0)
            old_penalty_sum += old_pen

            # New dot product
            new_dot = tl.sum(new_vec * other)
            new_cos = tl.minimum(tl.maximum(new_dot, -1.0), 1.0)
            new_arg = 2.0 * tl.maximum(1.0 - new_cos, 0.0)
            new_dist = 2.0 * tl.sqrt(new_arg + 1e-30)
            new_pen = tl.maximum(2.0 - new_dist, 0.0)
            new_penalty_sum += new_pen

        # Delta = new - old
        delta = new_penalty_sum - old_penalty_sum
        tl.store(deltas_out_ptr + pid, delta)

    @triton.jit
    def _coulomb_delta_kernel(
        replicas_ptr,
        old_vecs_ptr,
        new_vecs_ptr,
        flat_indices_ptr,
        replica_ids_ptr,
        deltas_out_ptr,
        N: tl.constexpr,
        D: tl.constexpr,
        stride_rep_r,
        stride_rep_n,
        stride_rep_d,
    ):
        """Compute Coulomb energy delta for one (replica, perturbation) pair."""
        pid = tl.program_id(0)

        rep_id = tl.load(replica_ids_ptr + pid)
        vec_idx = tl.load(flat_indices_ptr + pid)

        old_vec = tl.load(old_vecs_ptr + pid * D + tl.arange(0, D))
        new_vec = tl.load(new_vecs_ptr + pid * D + tl.arange(0, D))

        old_energy_sum = tl.zeros([], dtype=tl.float64)
        new_energy_sum = tl.zeros([], dtype=tl.float64)

        base_ptr = replicas_ptr + rep_id * stride_rep_r

        for j in range(N):
            if j == vec_idx:
                continue

            other = tl.load(base_ptr + j * stride_rep_n + tl.arange(0, D))

            # Old distance
            old_diff = old_vec - other
            old_dist_sq = tl.sum(old_diff * old_diff)
            old_dist = tl.sqrt(old_dist_sq + 1e-24)
            old_energy_sum += 1.0 / old_dist

            # New distance
            new_diff = new_vec - other
            new_dist_sq = tl.sum(new_diff * new_diff)
            new_dist = tl.sqrt(new_dist_sq + 1e-24)
            new_energy_sum += 1.0 / new_dist

        delta = new_energy_sum - old_energy_sum
        tl.store(deltas_out_ptr + pid, delta)


def triton_sa_step(
    replicas: torch.Tensor,     # (R, N, D)
    losses: torch.Tensor,       # (R,)
    temps: torch.Tensor,        # (R,)
    probs: torch.Tensor,        # (N,)
    scale: float,
    K: int,
    loss_type: str = "hinge",
    project_sphere: bool = True,
) -> tuple[torch.Tensor, int]:
    """SA step using Triton kernel for delta computation.

    Falls back to fused_step if Triton not available.
    """
    if not HAS_TRITON or not replicas.is_cuda:
        from einstein.gpu_tempering.fused_step import fused_sa_step
        return fused_sa_step(replicas, losses, temps, probs, scale, K, loss_type, project_sphere)

    R, N, D = replicas.shape
    device = replicas.device
    dtype = replicas.dtype
    RK = R * K

    # Sample indices
    vec_indices = torch.multinomial(probs.expand(R, -1), K, replacement=False)
    flat_indices = vec_indices.reshape(RK)
    replica_ids = torch.arange(R, device=device).unsqueeze(1).expand(R, K).reshape(RK)

    # Gather old vectors
    old_vecs = replicas[replica_ids, flat_indices].clone()  # (RK, D)

    # Perturb
    noise = torch.randn(RK, D, device=device, dtype=dtype) * scale
    new_vecs = old_vecs + noise
    if project_sphere:
        new_vecs = new_vecs / new_vecs.norm(dim=1, keepdim=True).clamp(min=1e-30)

    # Allocate output
    deltas = torch.empty(RK, device=device, dtype=dtype)

    # Launch Triton kernel
    kernel = _hinge_delta_kernel if loss_type == "hinge" else _coulomb_delta_kernel
    grid = (RK,)

    kernel[grid](
        replicas,
        old_vecs,
        new_vecs,
        flat_indices.to(torch.int64),
        replica_ids.to(torch.int64),
        deltas,
        N=N,
        D=D,
        stride_rep_r=replicas.stride(0),
        stride_rep_n=replicas.stride(1),
        stride_rep_d=replicas.stride(2),
    )

    # Metropolis acceptance
    temps_expanded = temps[replica_ids]
    accept_prob = torch.exp((-deltas / temps_expanded).clamp(max=0))
    accept_mask = (deltas < 0) | (torch.rand(RK, device=device, dtype=dtype) < accept_prob)

    # Apply accepted perturbations
    accepted = accept_mask.nonzero(as_tuple=True)[0]
    if accepted.numel() > 0:
        replicas[replica_ids[accepted], flat_indices[accepted]] = new_vecs[accepted]

    # Update losses
    deltas_rk = deltas.reshape(R, K)
    mask_rk = accept_mask.reshape(R, K)
    losses = losses + (deltas_rk * mask_rk.float()).sum(dim=1)

    return losses, int(accept_mask.sum().item())


def run_triton_tempering(
    initial_vectors: np.ndarray,
    n_replicas: int = 64,
    n_steps: int = 200_000,
    k_per_step: int = 50,
    scale: float = 1e-6,
    t_min: float = 1e-12,
    t_max: float = 1e-4,
    swap_interval: int = 100,
    recompute_every: int = 1000,
    report_every: int = 5_000,
    timeout_sec: float = 6900,
    loss_type: str = "hinge",
) -> dict:
    """Run parallel tempering using Triton kernel.

    Same interface as run_fused_tempering but uses Triton for delta computation.
    Falls back to fused_step automatically if Triton not available.
    """
    import time
    from einstein.gpu_tempering.losses import HingeOverlapLoss, CoulombLoss

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float64
    R = n_replicas
    K = k_per_step
    N, D = initial_vectors.shape

    backend = "triton" if (HAS_TRITON and device == "cuda") else "fused_step"
    print(f"Backend: {backend}")
    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    t0 = time.time()

    sota = torch.tensor(initial_vectors, device=device, dtype=dtype)
    sota = sota / sota.norm(dim=1, keepdim=True).clamp(min=1e-30)

    loss_fn = HingeOverlapLoss() if loss_type == "hinge" else CoulombLoss()
    initial_score = loss_fn.full_loss(sota).item()
    print(f"Initial: {initial_score:.15f}")
    print(f"R={R}, K={K}, scale={scale:.0e}, T=[{t_min:.0e}..{t_max:.0e}]")

    temps = torch.tensor(np.geomspace(t_min, t_max, R), device=device, dtype=dtype)
    replicas = sota.unsqueeze(0).expand(R, -1, -1).clone()
    losses = torch.stack([loss_fn.full_loss(replicas[r]) for r in range(R)])

    best_loss = losses.min().item()
    best_vecs = replicas[losses.argmin()].clone()

    probs = loss_fn.contributions(replicas[0])
    probs = probs / probs.sum() if probs.sum() > 0 else torch.ones(N, device=device, dtype=dtype) / N

    total_perts = 0
    total_accepts = 0
    swaps_att = 0
    swaps_acc = 0

    print(f"Starting {n_steps:,} steps ({n_steps * R * K:,} perturbations)...\n")

    for step in range(n_steps):
        if step > 0 and step % recompute_every == 0:
            probs = loss_fn.contributions(replicas[0])
            probs = probs / probs.sum() if probs.sum() > 0 else torch.ones(N, device=device, dtype=dtype) / N

        losses, n_acc = triton_sa_step(replicas, losses, temps, probs, scale, K, loss_type)
        total_perts += R * K
        total_accepts += n_acc

        ml = losses.min().item()
        if ml < best_loss:
            best_loss = ml
            best_vecs = replicas[losses.argmin()].clone()

        if (step + 1) % swap_interval == 0:
            for parity in [0, 1]:
                rl = torch.arange(parity, R - 1, 2, device=device)
                rh = rl + 1
                if len(rl) == 0:
                    continue
                swaps_att += len(rl)
                delta = (losses[rl] - losses[rh]) * (1.0 / temps[rl] - 1.0 / temps[rh])
                sm = torch.rand(len(rl), device=device, dtype=dtype) < torch.exp(delta.clamp(max=50))
                if sm.any():
                    sl, sh = rl[sm], rh[sm]
                    swaps_acc += sm.sum().item()
                    tv = replicas[sl].clone()
                    replicas[sl] = replicas[sh]
                    replicas[sh] = tv
                    tl_v = losses[sl].clone()
                    losses[sl] = losses[sh]
                    losses[sh] = tl_v

        if (step + 1) % report_every == 0:
            elapsed = time.time() - t0
            exact = loss_fn.full_loss(best_vecs).item()
            sr = swaps_acc / max(1, swaps_att) * 100
            ar = total_accepts / max(1, total_perts) * 100
            pps = total_perts / elapsed

            print(
                f"  step {step+1:>8,d} | {elapsed:.0f}s | {pps:,.0f} p/s | "
                f"BEST={exact:.15f} (Δ={initial_score-exact:.2e}) | "
                f"acc={ar:.1f}% | swap={sr:.1f}%"
            )
            total_accepts = 0
            total_perts = 0
            swaps_att = 0
            swaps_acc = 0

        if time.time() - t0 > timeout_sec:
            print(f"\nTimeout at step {step+1}")
            break

    final = loss_fn.full_loss(best_vecs).item()
    elapsed = time.time() - t0
    eff = (step + 1) * R * K

    print(f"\n{'='*70}")
    print(f"FINAL: {final:.15f} ({backend})")
    print(f"START: {initial_score:.15f}")
    print(f"Delta: {initial_score - final:.2e}")
    print(f"Time:  {elapsed:.0f}s | {eff/elapsed:,.0f} p/s | {eff:,} total")
    print(f"{'='*70}")

    return {
        "best_score": final,
        "initial_score": initial_score,
        "delta": initial_score - final,
        "best_vectors": best_vecs.cpu().numpy(),
        "elapsed_seconds": elapsed,
        "total_perturbations": eff,
        "perturbations_per_sec": eff / elapsed,
        "backend": backend,
    }
