"""Fused SA step — processes all R×K perturbations in one batched operation.

The key optimization: instead of a Python for-loop over K perturbations,
compute all R×K incremental deltas in a single batched matmul.

At scale ≤ 1e-6, the Jacobi approximation holds: perturbations of different
vectors within the same replica are independent (cross-coupling O(scale²)).
This means we can evaluate all K perturbations against the UNMODIFIED replica
and apply all accepted changes at once.

This eliminates the #1 bottleneck (Python loop overhead) and should give
5-50x throughput improvement depending on K and R.
"""

import torch
import numpy as np


def compute_deltas_hinge(old_dots, new_dots, flat_indices, RK, device):
    """Hinge overlap penalty deltas — kissing number / sphere packing."""
    rk_idx = torch.arange(RK, device=device)
    old_dots[rk_idx, flat_indices] = -1.0
    new_dots[rk_idx, flat_indices] = -1.0

    old_cos = old_dots.clamp(-1.0, 1.0)
    old_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - old_cos, min=0.0))
    old_p = torch.clamp(2.0 - old_d, min=0.0).sum(dim=1)

    new_cos = new_dots.clamp(-1.0, 1.0)
    new_d = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - new_cos, min=0.0))
    new_p = torch.clamp(2.0 - new_d, min=0.0).sum(dim=1)

    return new_p - old_p


def compute_deltas_coulomb(old_dots, new_dots, flat_indices, RK, device):
    """Coulomb energy deltas — Thomson problem."""
    rk_idx = torch.arange(RK, device=device)
    old_dots[rk_idx, flat_indices] = -1.0
    new_dots[rk_idx, flat_indices] = -1.0

    old_d = 2.0 * torch.sqrt(torch.clamp(1.0 - old_dots.clamp(-1, 1), min=1e-24) * 2.0)
    old_d[rk_idx, flat_indices] = 1e12
    old_p = (1.0 / old_d.clamp(min=1e-12)).sum(dim=1)

    new_d = 2.0 * torch.sqrt(torch.clamp(1.0 - new_dots.clamp(-1, 1), min=1e-24) * 2.0)
    new_d[rk_idx, flat_indices] = 1e12
    new_p = (1.0 / new_d.clamp(min=1e-12)).sum(dim=1)

    return new_p - old_p


# Registry of delta functions — add new loss types here
DELTA_FNS = {
    "hinge": compute_deltas_hinge,
    "coulomb": compute_deltas_coulomb,
}


def fused_sa_step(
    replicas: torch.Tensor,      # (R, N, D)
    losses: torch.Tensor,        # (R,)
    temps: torch.Tensor,         # (R,)
    probs: torch.Tensor,         # (N,)
    scale: float,
    K: int,
    loss_type: str = "hinge",
    project_sphere: bool = True,
) -> tuple[torch.Tensor, int]:
    """Process R×K perturbations in one batched operation.

    Args:
        replicas: (R, N, D) tensor of replica configurations
        losses: (R,) current losses per replica
        temps: (R,) temperatures per replica
        probs: (N,) sampling probabilities
        scale: perturbation scale
        K: perturbations per replica per step
        loss_type: "hinge" or "coulomb" (or register custom via DELTA_FNS)
        project_sphere: if True, normalize perturbed vectors to unit sphere

    Returns: (updated_losses, n_accepts)
    Modifies replicas in-place.
    """
    if loss_type not in DELTA_FNS:
        raise ValueError(f"Unknown loss_type: {loss_type}. Available: {list(DELTA_FNS.keys())}")

    R, N, D = replicas.shape
    device = replicas.device
    dtype = replicas.dtype
    RK = R * K

    # 1. Sample K vector indices per replica: (R, K)
    vec_indices = torch.multinomial(probs.expand(R, -1), K, replacement=False)

    # 2. Flatten for batched ops
    flat_indices = vec_indices.reshape(RK)
    replica_ids = torch.arange(R, device=device).unsqueeze(1).expand(R, K).reshape(RK)

    # 3. Gather old vectors: (RK, D)
    old_vecs = replicas[replica_ids, flat_indices].clone()

    # 4. Generate perturbations: (RK, D)
    noise = torch.randn(RK, D, device=device, dtype=dtype) * scale
    new_vecs = old_vecs + noise
    if project_sphere:
        new_vecs = new_vecs / new_vecs.norm(dim=1, keepdim=True).clamp(min=1e-30)

    # 5. Batch dot products against UNMODIFIED replicas (Jacobi approximation)
    parent_replicas = replicas[replica_ids]  # (RK, N, D)
    old_dots = torch.bmm(old_vecs.unsqueeze(1), parent_replicas.transpose(1, 2)).squeeze(1)
    new_dots = torch.bmm(new_vecs.unsqueeze(1), parent_replicas.transpose(1, 2)).squeeze(1)

    # 6. Compute loss deltas via registered function
    deltas = DELTA_FNS[loss_type](old_dots, new_dots, flat_indices, RK, device)

    # 8. Metropolis acceptance per perturbation
    # Temperature for each perturbation: use the replica's temperature
    temps_expanded = temps[replica_ids]  # (RK,)
    accept_prob = torch.exp((-deltas / temps_expanded).clamp(max=0))
    accept_mask = (deltas < 0) | (torch.rand(RK, device=device, dtype=dtype) < accept_prob)

    # 9. Apply accepted perturbations
    # For each accepted (r, k): update replicas[r, idx] = new_vec
    # Handle conflicts: if two perturbations in same replica target same vector,
    # only the last one wins (rare at K<<N, and Jacobi means both are valid)
    accepted_replica_ids = replica_ids[accept_mask]
    accepted_flat_indices = flat_indices[accept_mask]
    accepted_new_vecs = new_vecs[accept_mask]

    if accepted_replica_ids.numel() > 0:
        replicas[accepted_replica_ids, accepted_flat_indices] = accepted_new_vecs

    # 10. Update losses: sum of per-replica accepted deltas
    # Reshape deltas to (R, K), mask to (R, K), sum accepted deltas per replica
    deltas_rk = deltas.reshape(R, K)
    mask_rk = accept_mask.reshape(R, K)
    loss_deltas = (deltas_rk * mask_rk.float()).sum(dim=1)  # (R,)
    losses = losses + loss_deltas

    n_accepts = int(accept_mask.sum().item())

    # Free large intermediate tensors
    del parent_replicas, old_dots, new_dots

    return losses, n_accepts


def run_fused_tempering(
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
    """Run fused parallel tempering SA.

    Each step processes R×K perturbations in one batched operation.
    """
    import time

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float64
    R = n_replicas
    K = k_per_step

    if device == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")

    N, D = initial_vectors.shape
    t0 = time.time()

    sota = torch.tensor(initial_vectors, device=device, dtype=dtype)
    sota = sota / sota.norm(dim=1, keepdim=True).clamp(min=1e-30)

    # Initial loss
    from einstein.gpu_tempering.losses import HingeOverlapLoss, CoulombLoss
    loss_fn = HingeOverlapLoss() if loss_type == "hinge" else CoulombLoss()
    initial_score = loss_fn.full_loss(sota).item()
    print(f"Initial: {initial_score:.15f}")

    temps = torch.tensor(np.geomspace(t_min, t_max, R), device=device, dtype=dtype)
    print(f"R={R}, K={K}, scale={scale:.0e}, T=[{temps[0]:.1e}..{temps[-1]:.1e}]")
    print(f"Effective perturbations/step: {R * K:,}")

    replicas = sota.unsqueeze(0).expand(R, -1, -1).clone()
    losses = torch.stack([loss_fn.full_loss(replicas[r]) for r in range(R)])

    best_loss = losses.min().item()
    best_vecs = replicas[losses.argmin()].clone()

    # Contribution probs
    probs = loss_fn.contributions(replicas[0])
    probs = probs / probs.sum() if probs.sum() > 0 else torch.ones(N, device=device, dtype=dtype) / N

    total_perts = 0
    total_accepts = 0
    swaps_att = 0
    swaps_acc = 0

    total_eff = n_steps * R * K
    print(f"Starting {n_steps:,} steps ({total_eff:,} total perturbations)...\n")

    for step in range(n_steps):
        if step > 0 and step % recompute_every == 0:
            probs = loss_fn.contributions(replicas[0])
            probs = probs / probs.sum() if probs.sum() > 0 else torch.ones(N, device=device, dtype=dtype) / N

        # ---- THE FUSED STEP: all R×K perturbations in one call ----
        losses, n_acc = fused_sa_step(
            replicas, losses, temps, probs, scale, K, loss_type
        )
        total_perts += R * K
        total_accepts += n_acc

        # Track best
        ml = losses.min().item()
        if ml < best_loss:
            best_loss = ml
            best_vecs = replicas[losses.argmin()].clone()

        # Replica exchange (vectorized)
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
                    tl = losses[sl].clone()
                    losses[sl] = losses[sh]
                    losses[sh] = tl

        # Report
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
    print(f"FINAL: {final:.15f}")
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
    }
