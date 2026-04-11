"""Torch-based differentiable optimization for Heilbronn Convex P16.

Uses automatic differentiation for exact gradients and multiple loss
formulations to explore the landscape:
1. Log-sum-exp soft-min (varying beta)
2. Entropy-regularized min
3. p-norm approximation to min
4. Multi-restart Adam + L-BFGS with thousands of random starts

Runs on CPU (float64 needed for precision).

Usage:
    uv run python scripts/heilbronn_convex/torch_attack.py --time 1800 --seed 123
"""

from __future__ import annotations

import argparse
import itertools
import json
import time
from pathlib import Path

import numpy as np
import torch
from scipy.spatial import ConvexHull

from einstein.heilbronn_convex import arena_score, fast_score, active_triples, hull_vertex_indices
from einstein.heilbronn_convex.optimizer import polish_slsqp

RESULTS_DIR = Path("results/problem-16-heilbronn-convex")

ARENA_BEST = 0.02783558051755368259
SUBMIT_THRESHOLD = 0.02783558045993943589 + 1e-9

# Precompute triple indices
TRIPLES = torch.tensor(
    list(itertools.combinations(range(14), 3)), dtype=torch.long
)


def triangle_areas_torch(pts):
    """Compute all 364 triangle areas using torch (differentiable)."""
    i = TRIPLES[:, 0]
    j = TRIPLES[:, 1]
    k = TRIPLES[:, 2]
    p1 = pts[i]
    p2 = pts[j]
    p3 = pts[k]
    cross = (
        p1[:, 0] * (p2[:, 1] - p3[:, 1])
        + p2[:, 0] * (p3[:, 1] - p1[:, 1])
        + p3[:, 0] * (p1[:, 1] - p2[:, 1])
    )
    return torch.abs(cross) * 0.5


def hull_area_torch(pts):
    """Compute convex hull area (not differentiable, used as constant)."""
    pts_np = pts.detach().numpy()
    try:
        return ConvexHull(pts_np).volume
    except Exception:
        return 1e-12


def loss_lse(pts, beta=1e5):
    """Log-sum-exp soft-min loss (negated)."""
    areas = triangle_areas_torch(pts)
    ha = hull_area_torch(pts)
    if ha < 1e-12:
        return torch.tensor(1e10, dtype=torch.float64)
    normed = areas / ha
    mn = normed.min()
    # Smooth min approximation: mn - log(sum(exp(-beta*(a-mn))))/beta
    soft_min = mn - torch.log(torch.sum(torch.exp(-beta * (normed - mn)))) / beta
    return -soft_min  # minimize


def loss_pnorm(pts, p=-50.0):
    """p-norm approximation to min (p < 0 gives min-like behavior)."""
    areas = triangle_areas_torch(pts)
    ha = hull_area_torch(pts)
    if ha < 1e-12:
        return torch.tensor(1e10, dtype=torch.float64)
    normed = areas / ha
    # Generalized mean with p < 0 → min
    pnorm = torch.pow(torch.mean(torch.pow(normed, p)), 1.0 / p)
    return -pnorm


def loss_entropy(pts, tau=1e-5):
    """Entropy-regularized min: softmin + entropy bonus."""
    areas = triangle_areas_torch(pts)
    ha = hull_area_torch(pts)
    if ha < 1e-12:
        return torch.tensor(1e10, dtype=torch.float64)
    normed = areas / ha
    # Softmin weights
    weights = torch.softmax(-normed / tau, dim=0)
    soft_min = (weights * normed).sum()
    entropy = -(weights * torch.log(weights + 1e-30)).sum()
    return -(soft_min + tau * 0.01 * entropy)


def random_init_torch(rng, mode="10p4"):
    """Generate random initial configuration as torch tensor."""
    if mode == "10p4":
        angles = np.sort(rng.uniform(0, 2 * np.pi, 10))
        radii = rng.uniform(0.8, 1.2, 10)
        hull = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
        interior = rng.uniform(-0.5, 0.5, (4, 2))
        pts = np.vstack([hull, interior])
    elif mode == "disk":
        u = rng.uniform(size=(14, 2))
        r = np.sqrt(u[:, 0])
        theta = u[:, 1] * 2 * np.pi
        pts = np.column_stack([r * np.cos(theta), r * np.sin(theta)])
    elif mode == "square":
        pts = rng.uniform(-1, 1, (14, 2))
    elif mode == "perturb_ref":
        ref_data = json.loads(
            (RESULTS_DIR / "reference_solution.json").read_text()
        )
        pts = np.array(ref_data["points"], dtype=np.float64)
        scale = rng.choice([1e-3, 5e-3, 1e-2, 5e-2, 0.1, 0.3])
        pts = pts + rng.normal(0, scale, pts.shape)
    else:
        pts = rng.uniform(-1, 1, (14, 2))

    return torch.tensor(pts, dtype=torch.float64, requires_grad=True)


def optimize_adam(pts_init, loss_fn, lr=1e-4, n_steps=2000, **loss_kwargs):
    """Run Adam optimizer on the given loss function."""
    pts = pts_init.clone().detach().requires_grad_(True)
    optimizer = torch.optim.Adam([pts], lr=lr)

    best_pts = pts.detach().clone()
    best_loss = float("inf")

    for step in range(n_steps):
        optimizer.zero_grad()
        loss = loss_fn(pts, **loss_kwargs)
        if not torch.isfinite(loss):
            break
        loss.backward()
        optimizer.step()

        if loss.item() < best_loss:
            best_loss = loss.item()
            best_pts = pts.detach().clone()

    return best_pts.numpy()


def optimize_lbfgs(pts_init, loss_fn, lr=0.01, n_steps=100, **loss_kwargs):
    """Run L-BFGS optimizer."""
    pts = pts_init.clone().detach().requires_grad_(True)
    optimizer = torch.optim.LBFGS([pts], lr=lr, max_iter=20, line_search_fn="strong_wolfe")

    best_pts = pts.detach().clone()
    best_loss = float("inf")
    step_count = [0]

    def closure():
        optimizer.zero_grad()
        loss = loss_fn(pts, **loss_kwargs)
        if torch.isfinite(loss):
            loss.backward()
        step_count[0] += 1
        return loss

    for _ in range(n_steps):
        try:
            loss = optimizer.step(closure)
            if loss is not None and torch.isfinite(loss) and loss.item() < best_loss:
                best_loss = loss.item()
                best_pts = pts.detach().clone()
        except Exception:
            break

    return best_pts.numpy()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=float, default=1800.0)
    parser.add_argument("--seed", type=int, default=123)
    parser.add_argument("--out", type=str, default="/tmp/heilbronn_torch_attack.json")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    start = time.time()

    print(f"Target: {SUBMIT_THRESHOLD:.20f}")
    print(f"Arena #1: {ARENA_BEST:.20f}")
    print(f"Gap: {SUBMIT_THRESHOLD - ARENA_BEST:.3e}")

    best_score = ARENA_BEST
    best_pts = None
    discovered = {}
    trial_count = 0

    loss_configs = [
        ("lse-1e4", loss_lse, {"beta": 1e4}),
        ("lse-1e5", loss_lse, {"beta": 1e5}),
        ("lse-1e6", loss_lse, {"beta": 1e6}),
        ("pnorm-20", loss_pnorm, {"p": -20.0}),
        ("pnorm-50", loss_pnorm, {"p": -50.0}),
        ("pnorm-100", loss_pnorm, {"p": -100.0}),
        ("entropy-1e4", loss_entropy, {"tau": 1e-4}),
        ("entropy-1e5", loss_entropy, {"tau": 1e-5}),
    ]

    init_modes = ["10p4", "disk", "square", "perturb_ref"]
    optimizers = ["adam", "lbfgs"]

    adam_lrs = [1e-3, 5e-4, 1e-4, 5e-5]

    while time.time() - start < args.time:
        # Random configuration
        loss_name, loss_fn, loss_kwargs = loss_configs[rng.integers(0, len(loss_configs))]
        mode = init_modes[rng.integers(0, len(init_modes))]
        opt_type = optimizers[rng.integers(0, len(optimizers))]

        pts_init = random_init_torch(rng, mode=mode)

        if opt_type == "adam":
            lr = adam_lrs[rng.integers(0, len(adam_lrs))]
            n_steps = rng.integers(1000, 5000)
            pts_opt = optimize_adam(pts_init, loss_fn, lr=lr, n_steps=n_steps, **loss_kwargs)
        else:
            lr = rng.choice([0.005, 0.01, 0.05])
            pts_opt = optimize_lbfgs(pts_init, loss_fn, lr=lr, n_steps=50, **loss_kwargs)

        # Polish with SLSQP
        polished, score = polish_slsqp(pts_opt, max_iter=400)
        trial_count += 1

        if np.isfinite(score) and score > 0.02:
            key = int(round(score * 1e10))
            if key not in discovered or score > discovered[key][0]:
                discovered[key] = (score, polished.copy(), f"{loss_name}-{opt_type}-{mode}")

        if score > best_score:
            best_score = score
            best_pts = polished.copy()
            at = active_triples(best_pts, rel_tol=1e-9)
            hv = hull_vertex_indices(best_pts)
            delta = score - ARENA_BEST
            print(f"\n*** NEW BEST! {score:.20f}  delta={delta:+.3e}  "
                  f"hull={len(hv)}+{14-len(hv)}  active={len(at)}  "
                  f"loss={loss_name} opt={opt_type} init={mode}")
            if score > SUBMIT_THRESHOLD:
                print("*** ABOVE SUBMIT THRESHOLD! ***")
                out = {"points": best_pts.tolist(), "score": score}
                Path("/tmp/heilbronn_torch_candidate.json").write_text(
                    json.dumps(out, indent=2)
                )

        if trial_count % 100 == 0:
            elapsed = time.time() - start
            n_basins = len(discovered)
            print(f"[{trial_count:5d}] {elapsed:.0f}s  basins={n_basins}  "
                  f"best={best_score:.16f}  loss={loss_name}  opt={opt_type}  init={mode}")

    # Summary
    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"TORCH ATTACK SUMMARY after {elapsed:.1f}s, {trial_count} trials")
    print(f"{'='*60}")
    print(f"Best score: {best_score:.20f}")
    print(f"Arena #1:   {ARENA_BEST:.20f}")
    print(f"Threshold:  {SUBMIT_THRESHOLD:.20f}")
    if best_score > SUBMIT_THRESHOLD:
        print("*** SUBMITTABLE! ***")
    else:
        print(f"Gap: {SUBMIT_THRESHOLD - best_score:.3e}")

    sorted_basins = sorted(discovered.values(), key=lambda x: -x[0])[:10]
    print(f"\nTop 10 basins ({len(discovered)} total):")
    for i, (sc, pts, cfg) in enumerate(sorted_basins):
        hv = hull_vertex_indices(pts)
        at = active_triples(pts, rel_tol=1e-9)
        print(f"  #{i+1}: {sc:.16f}  hull={len(hv)}+{14-len(hv)}  active={len(at)}  {cfg}")

    out = {
        "best_score": best_score,
        "best_pts": best_pts.tolist() if best_pts is not None else None,
        "above_threshold": best_score > SUBMIT_THRESHOLD,
        "trials": trial_count,
        "basins": len(discovered),
        "elapsed_s": elapsed,
        "top10": [
            {"score": sc, "points": pts.tolist(), "config": cfg,
             "n_hull": len(hull_vertex_indices(pts)),
             "active": len(active_triples(pts, rel_tol=1e-9))}
            for sc, pts, cfg in sorted_basins
        ],
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"\nSaved to {args.out}")


if __name__ == "__main__":
    main()
