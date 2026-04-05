"""Smooth gradient optimization: softplus-smoothed overlap loss + PyTorch L-BFGS.

Replaces hinge loss with softplus approximation to enable gradient flow.
Anneal beta (smoothing sharpness) to converge toward true hinge loss.

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/optimize_smooth_gradient.py
"""

import json
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
            print(f"Loaded {path.name}")
            return vecs / norms
    raise FileNotFoundError("No solution found")


def overlap_loss_exact_np(unit_vecs):
    """Exact hinge loss (numpy, for verification)."""
    centers = 2.0 * unit_vecs
    diff = centers[:, None, :] - centers[None, :, :]
    dists = np.sqrt(np.sum(diff**2, axis=-1))
    n = len(unit_vecs)
    i, j = np.triu_indices(n, k=1)
    return float(np.sum(np.maximum(0.0, 2.0 - dists[i, j])))


def smooth_overlap_loss(unit_vecs, beta=500.0):
    """Softplus-smoothed overlap loss for gradient computation.

    softplus(x) = log(1 + exp(x))
    smooth_hinge(2-d) = softplus(beta*(2-d)) / beta
    As beta → ∞, this converges to max(0, 2-d).
    """
    gram = unit_vecs @ unit_vecs.T
    n = unit_vecs.shape[0]
    idx_i, idx_j = torch.triu_indices(n, n, offset=1)
    cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
    # Distance: d = 2*sqrt(2*(1-cos))
    dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=1e-30))
    # Smooth hinge: softplus(beta * (2 - d)) / beta
    arg = beta * (2.0 - dists)
    # Use logsigmoid trick for numerical stability: softplus(x) = x + softplus(-x)
    penalties = torch.nn.functional.softplus(arg) / beta
    return penalties.sum()


def hinge_loss_torch(unit_vecs):
    """Exact hinge loss in PyTorch (for comparison)."""
    gram = unit_vecs @ unit_vecs.T
    n = unit_vecs.shape[0]
    idx_i, idx_j = torch.triu_indices(n, n, offset=1)
    cos_vals = gram[idx_i, idx_j].clamp(-1.0, 1.0)
    dists = 2.0 * torch.sqrt(2.0 * torch.clamp(1.0 - cos_vals, min=1e-30))
    penalties = torch.clamp(2.0 - dists, min=0.0)
    return penalties.sum()


def project_to_sphere(vecs):
    """Project vectors to unit sphere (retraction)."""
    return vecs / vecs.norm(dim=1, keepdim=True)


def run_lbfgs_stage(vecs_np, beta, n_steps, lr=1e-4):
    """Run L-BFGS optimization at a given beta smoothing level."""
    vecs = torch.tensor(vecs_np, dtype=torch.float64, requires_grad=True)
    optimizer = torch.optim.LBFGS(
        [vecs], lr=lr, max_iter=20, line_search_fn="strong_wolfe",
        history_size=50, tolerance_grad=1e-20, tolerance_change=1e-20,
    )

    best_hinge = float("inf")
    best_vecs = vecs_np.copy()
    t0 = time.time()

    for step in range(n_steps):
        def closure():
            optimizer.zero_grad()
            unit = project_to_sphere(vecs)
            loss = smooth_overlap_loss(unit, beta=beta)
            loss.backward()
            return loss

        smooth_loss = optimizer.step(closure)

        # Project to sphere after step
        with torch.no_grad():
            vecs.data = project_to_sphere(vecs.data)

        if (step + 1) % 10 == 0:
            with torch.no_grad():
                unit = project_to_sphere(vecs)
                hinge = hinge_loss_torch(unit).item()
                smooth = smooth_overlap_loss(unit, beta=beta).item()

            if hinge < best_hinge:
                best_hinge = hinge
                best_vecs = vecs.detach().numpy().copy()
                norms = np.linalg.norm(best_vecs, axis=1, keepdims=True)
                best_vecs = best_vecs / norms

            elapsed = time.time() - t0
            print(
                f"  [beta={beta:.0f}] step {step+1:>4d} | "
                f"smooth={smooth:.12f} | hinge={hinge:.15f} | "
                f"best={best_hinge:.15f} | {elapsed:.0f}s"
            )

    return best_vecs, best_hinge


def run_adam_stage(vecs_np, beta, n_steps, lr=1e-6):
    """Run Riemannian Adam at a given beta smoothing level."""
    vecs = torch.tensor(vecs_np, dtype=torch.float64, requires_grad=True)
    optimizer = torch.optim.Adam([vecs], lr=lr)

    best_hinge = float("inf")
    best_vecs = vecs_np.copy()
    t0 = time.time()

    for step in range(n_steps):
        optimizer.zero_grad()
        unit = project_to_sphere(vecs)
        loss = smooth_overlap_loss(unit, beta=beta)
        loss.backward()

        # Project gradient to tangent space of sphere
        with torch.no_grad():
            dots = (vecs.grad * vecs).sum(dim=1, keepdim=True)
            vecs.grad -= dots * vecs

        optimizer.step()

        # Retract to sphere
        with torch.no_grad():
            vecs.data = project_to_sphere(vecs.data)

        if (step + 1) % 100 == 0:
            with torch.no_grad():
                unit = project_to_sphere(vecs)
                hinge = hinge_loss_torch(unit).item()
                smooth = smooth_overlap_loss(unit, beta=beta).item()

            if hinge < best_hinge:
                best_hinge = hinge
                best_vecs = vecs.detach().numpy().copy()
                norms = np.linalg.norm(best_vecs, axis=1, keepdims=True)
                best_vecs = best_vecs / norms

            if (step + 1) % 500 == 0:
                elapsed = time.time() - t0
                print(
                    f"  [Adam beta={beta:.0f}] step {step+1:>5d} | "
                    f"smooth={smooth:.12f} | hinge={hinge:.15f} | "
                    f"best={best_hinge:.15f} | {elapsed:.0f}s"
                )

    return best_vecs, best_hinge


def save_solution(vecs, score, tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag} (score={score:.15f})")


def main():
    print("=" * 70)
    print("SMOOTH GRADIENT: Softplus-smoothed loss + PyTorch optimization")
    print("=" * 70)

    vecs_np = load_best()
    initial = overlap_loss_exact_np(vecs_np)
    print(f"Start (exact hinge): {initial:.15f}")
    best_vecs, best_score = vecs_np.copy(), initial

    # Phase 1: Adam with low beta (broad gradient signal)
    print("\n=== Phase 1: Adam, beta=100 (broad smoothing) ===")
    v, s = run_adam_stage(best_vecs, beta=100, n_steps=5000, lr=1e-6)
    exact = overlap_loss_exact_np(v)
    print(f"  Exact hinge: {exact:.15f} (delta={initial - exact:.2e})")
    if exact < best_score:
        best_score = exact
        best_vecs = v.copy()
        save_solution(best_vecs, best_score, "smooth_best")

    # Phase 2: Adam with medium beta
    print("\n=== Phase 2: Adam, beta=500 ===")
    v, s = run_adam_stage(best_vecs, beta=500, n_steps=5000, lr=1e-7)
    exact = overlap_loss_exact_np(v)
    print(f"  Exact hinge: {exact:.15f} (delta={initial - exact:.2e})")
    if exact < best_score:
        best_score = exact
        best_vecs = v.copy()
        save_solution(best_vecs, best_score, "smooth_best")

    # Phase 3: L-BFGS with high beta (close to true hinge)
    print("\n=== Phase 3: L-BFGS, beta=1000 ===")
    v, s = run_lbfgs_stage(best_vecs, beta=1000, n_steps=200, lr=1e-5)
    exact = overlap_loss_exact_np(v)
    print(f"  Exact hinge: {exact:.15f} (delta={initial - exact:.2e})")
    if exact < best_score:
        best_score = exact
        best_vecs = v.copy()
        save_solution(best_vecs, best_score, "smooth_best")

    # Phase 4: L-BFGS with very high beta
    print("\n=== Phase 4: L-BFGS, beta=5000 ===")
    v, s = run_lbfgs_stage(best_vecs, beta=5000, n_steps=200, lr=1e-6)
    exact = overlap_loss_exact_np(v)
    print(f"  Exact hinge: {exact:.15f} (delta={initial - exact:.2e})")
    if exact < best_score:
        best_score = exact
        best_vecs = v.copy()
        save_solution(best_vecs, best_score, "smooth_best")

    # Phase 5: Final polish with micro-perturbation at 1e-12
    print("\n=== Phase 5: Micro-perturbation polish ===")
    from scripts.kissing_number.optimize_harden import run_perturbation
    v, l, n = run_perturbation(best_vecs.copy(), 1e-12, 5_000_000, 7777)
    exact = overlap_loss_exact_np(v)
    print(f"  After polish: {exact:.15f}")
    if exact < best_score:
        best_score = exact
        best_vecs = v.copy()

    final = overlap_loss_exact_np(best_vecs)
    print(f"\n{'='*70}")
    print(f"Final:   {final:.15f}")
    print(f"Start:   {initial:.15f}")
    print(f"Delta:   {initial - final:.2e}")
    print(f"{'='*70}")

    if final < initial:
        save_solution(best_vecs, final, "best")
        print("Improved! Saved as solution_best.json")
    else:
        print("No improvement from smooth gradient approach.")


if __name__ == "__main__":
    main()
