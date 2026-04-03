"""Optimizer for Problem 6: Kissing Number (d=11, n=594).

Warm-starts from SOTA and applies multiple optimization strategies:
1. Riemannian gradient descent on sphere manifold
2. Micro-perturbation with greedy acceptance
3. L-BFGS polish on overlapping pairs

Usage:
    uv run python scripts/kissing_number/optimize.py
"""

import json
import time
from pathlib import Path

import numpy as np

RESULTS_DIR = Path("results/problem-6-kissing-number")
N = 594
D = 11


def load_sota() -> np.ndarray:
    """Load best available solution."""
    path = RESULTS_DIR / "sota_vectors.json"
    with open(path) as f:
        data = json.load(f)
    vecs = np.array(data["vectors"], dtype=np.float64)
    # Normalize to unit sphere
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    return vecs / norms


def overlap_loss(unit_vecs: np.ndarray) -> float:
    """Total overlap penalty. Matches arena verifier."""
    centers = 2.0 * unit_vecs
    diff = centers[:, None, :] - centers[None, :, :]
    dists = np.sqrt(np.sum(diff**2, axis=-1))
    n = len(unit_vecs)
    idx_i, idx_j = np.triu_indices(n, k=1)
    penalties = np.maximum(0.0, 2.0 - dists[idx_i, idx_j])
    return float(np.sum(penalties))


def overlap_loss_fast(unit_vecs: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
    """Fast overlap loss + overlapping pair indices."""
    gram = unit_vecs @ unit_vecs.T
    n = len(unit_vecs)
    idx_i, idx_j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[idx_i, idx_j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    penalties = np.maximum(0.0, 2.0 - dists)
    total = float(np.sum(penalties))

    # Return indices of overlapping pairs
    overlap_mask = penalties > 0
    return total, idx_i[overlap_mask], idx_j[overlap_mask]


def project_to_sphere(vecs: np.ndarray) -> np.ndarray:
    """Project vectors back to unit sphere."""
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    return vecs / norms


def tangent_project(vecs: np.ndarray, grad: np.ndarray) -> np.ndarray:
    """Project gradient to tangent space of sphere at each point."""
    # grad_tan = grad - <grad, v> * v
    dots = np.sum(grad * vecs, axis=1, keepdims=True)
    return grad - dots * vecs


def compute_gradient(unit_vecs: np.ndarray) -> np.ndarray:
    """Compute gradient of overlap loss w.r.t. unit vectors.

    loss = sum_{i<j} max(0, 2 - 2*sqrt(2*(1 - <v_i, v_j>)))

    d(loss)/d(v_i) = sum_{j: overlap(i,j)} 2*sqrt(2) * v_j / (2*sqrt(2*(1-<vi,vj>)))
                   = sum_{j} 2 * v_j / dist(i,j)  [for overlapping pairs]
    """
    gram = unit_vecs @ unit_vecs.T
    n = len(unit_vecs)

    # Compute distances: dist = 2*sqrt(2*(1-cos))
    cos_matrix = np.clip(gram, -1.0, 1.0)
    arg = 2.0 * np.maximum(0.0, 1.0 - cos_matrix)
    dist_matrix = 2.0 * np.sqrt(arg)

    # Overlap mask: dist < 2 and i != j
    np.fill_diagonal(dist_matrix, np.inf)
    overlap = dist_matrix < 2.0

    # Gradient: for each overlapping pair (i,j), d(2-dist)/d(v_i)
    # dist = 2*sqrt(2*(1 - <vi,vj>))
    # d(dist)/d(vi) = 2 * (-vj) / (2*sqrt(2*(1-<vi,vj>))) * sqrt(2)
    #               = -2*vj / dist
    # d(2-dist)/d(vi) = 2*vj / dist (pushes vi toward vj... wait)

    # Actually: penalty = max(0, 2 - dist)
    # We want to MINIMIZE this. Gradient of penalty w.r.t. v_i:
    # d(penalty)/d(vi) = -d(dist)/d(vi) = 2*sqrt(2) * vj / (2*sqrt(2*(1-cos)))
    # But wait: dist = 2*sqrt(2*(1-cos_ij))
    # d(dist)/d(vi) = 2 * 1/(2*sqrt(2*(1-cos_ij))) * (-2) * d(cos_ij)/d(vi)
    # cos_ij = <vi, vj>, d(cos_ij)/d(vi) = vj
    # d(dist)/d(vi) = -2*vj / sqrt(2*(1-cos_ij)) = -2*sqrt(2)*vj / dist

    # So d(penalty)/d(vi) = -d(dist)/d(vi) = 2*sqrt(2)*vj / dist
    # This means gradient points TOWARD vj. To minimize, we move AGAINST gradient.
    # For steepest descent: vi -= lr * gradient

    # Actually this should push AWAY. Let me reconsider.
    # penalty = 2 - dist. We want to decrease penalty (increase dist).
    # grad of penalty = -grad of dist = 2*sqrt(2) * vj / dist
    # This points toward vj. Steepest descent (vi -= lr * grad) moves AWAY from vj. Good.

    # Wait no: d(dist)/d(vi) = -2*sqrt(2)*vj / dist means dist DECREASES when vi moves toward vj.
    # So d(penalty)/d(vi) = -d(dist)/d(vi) = 2*sqrt(2)*vj / dist. Moving in -grad direction
    # means moving away from vj, which increases dist, which decreases penalty. Correct.

    # Hmm, actually let me be more careful. cos_ij = <vi, vj>.
    # If we increase cos_ij (move vi toward vj), dist decreases.
    # d(cos_ij)/d(vi) = vj.
    # d(dist)/d(cos) = -sqrt(2) / sqrt(2*(1-cos)) = -1/sqrt(1-cos)... let me just use the chain rule.

    # dist = 2*sqrt(2) * sqrt(1-cos) where cos = <vi, vj>
    # d(dist)/d(cos) = 2*sqrt(2) * (-1/(2*sqrt(1-cos))) = -sqrt(2)/sqrt(1-cos)
    # d(dist)/d(vi) = d(dist)/d(cos) * d(cos)/d(vi) = -sqrt(2)*vj/sqrt(1-cos)
    # = -sqrt(2)*vj / (dist / (2*sqrt(2))) = -4*vj/dist

    # So d(penalty)/d(vi) = -d(dist)/d(vi) = 4*vj/dist

    # For a pair (i,j), gradient contribution to vi is 4*vj/dist.
    # This points toward vj. Steepest descent (subtract) pushes away. Correct!

    grad = np.zeros_like(unit_vecs)
    for i in range(n):
        mask_j = overlap[i]
        if not np.any(mask_j):
            continue
        js = np.where(mask_j)[0]
        ds = dist_matrix[i, js]  # distances to overlapping neighbors
        # Contribution: sum_j 4 * v_j / dist_ij
        grad[i] = np.sum(4.0 * unit_vecs[js] / ds[:, None], axis=0)

    return grad


def riemannian_gd(
    vecs: np.ndarray,
    lr: float = 1e-5,
    n_iters: int = 5000,
    decay: float = 0.999,
    verbose: bool = True,
) -> tuple[np.ndarray, float]:
    """Riemannian gradient descent on the product of spheres."""
    best_vecs = vecs.copy()
    best_loss, _, _ = overlap_loss_fast(vecs)
    if verbose:
        print(f"  RGD start: {best_loss:.14f}")

    for it in range(n_iters):
        grad = compute_gradient(vecs)
        grad_tan = tangent_project(vecs, grad)

        # Gradient step + retract to sphere
        vecs = vecs - lr * grad_tan
        vecs = project_to_sphere(vecs)

        if (it + 1) % 100 == 0:
            loss, _, _ = overlap_loss_fast(vecs)
            if loss < best_loss:
                best_loss = loss
                best_vecs = vecs.copy()
                if verbose:
                    print(f"  RGD iter {it+1}: {loss:.14f} (improved)")
            lr *= decay

    return best_vecs, best_loss


def micro_perturbation(
    vecs: np.ndarray,
    scale: float = 1e-8,
    n_iters: int = 500_000,
    seed: int = 42,
    verbose: bool = True,
) -> tuple[np.ndarray, float]:
    """Atomic-scale micro-perturbation with greedy acceptance.

    The proven CHRONOS technique: nudge one random vector by randn*scale,
    renormalize, accept if loss decreases.
    """
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    best_loss, _, _ = overlap_loss_fast(vecs)
    current_loss = best_loss
    improvements = 0

    if verbose:
        print(f"  Micro-perturb start (scale={scale:.0e}): {best_loss:.14f}")

    t0 = time.time()
    for it in range(n_iters):
        idx = rng.integers(N)
        perturbation = rng.standard_normal(D) * scale
        old_vec = vecs[idx].copy()

        vecs[idx] += perturbation
        vecs[idx] /= np.linalg.norm(vecs[idx])

        # Incremental loss: only recompute pairs involving idx
        new_loss = _incremental_loss(vecs, idx, current_loss, old_vec)

        if new_loss < current_loss:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        else:
            vecs[idx] = old_vec

        if verbose and (it + 1) % 50_000 == 0:
            elapsed = time.time() - t0
            rate = improvements / (it + 1) * 100
            print(
                f"  iter {it+1:>7d} | loss {best_loss:.14f} | "
                f"improvements {improvements} ({rate:.2f}%) | {elapsed:.0f}s"
            )

    return best_vecs, best_loss


def _incremental_loss(vecs: np.ndarray, idx: int, old_total: float, old_vec: np.ndarray) -> float:
    """Recompute loss incrementally after changing vecs[idx].

    Only recalculates pairs involving idx (O(n) instead of O(n²)).
    """
    # Remove old contributions
    old_cos = old_vec @ np.delete(vecs, idx, axis=0).T
    # Wait, vecs[idx] is already updated. Need old_vec paired with all others.
    others = np.concatenate([vecs[:idx], vecs[idx+1:]], axis=0)

    old_cos_vals = np.clip(old_vec @ others.T, -1.0, 1.0)
    old_dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - old_cos_vals))
    old_penalties = np.maximum(0.0, 2.0 - old_dists)

    new_cos_vals = np.clip(vecs[idx] @ others.T, -1.0, 1.0)
    new_dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - new_cos_vals))
    new_penalties = np.maximum(0.0, 2.0 - new_dists)

    return old_total - float(np.sum(old_penalties)) + float(np.sum(new_penalties))


def targeted_perturbation(
    vecs: np.ndarray,
    scale: float = 1e-8,
    n_iters: int = 200_000,
    seed: int = 42,
    verbose: bool = True,
) -> tuple[np.ndarray, float]:
    """Micro-perturbation focused on high-contribution vectors."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    best_loss, oi, oj = overlap_loss_fast(vecs)
    current_loss = best_loss
    improvements = 0

    if verbose:
        print(f"  Targeted start (scale={scale:.0e}): {best_loss:.14f}")

    # Find contribution per vector
    def _vector_contributions(v):
        gram = v @ v.T
        n = len(v)
        contributions = np.zeros(n)
        idx_i, idx_j = np.triu_indices(n, k=1)
        cos_vals = np.clip(gram[idx_i, idx_j], -1.0, 1.0)
        dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
        penalties = np.maximum(0.0, 2.0 - dists)
        np.add.at(contributions, idx_i, penalties)
        np.add.at(contributions, idx_j, penalties)
        return contributions

    t0 = time.time()
    for it in range(n_iters):
        # Every 10K iterations, recompute target probabilities
        if it % 10_000 == 0:
            contribs = _vector_contributions(vecs)
            probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N

        idx = rng.choice(N, p=probs)
        perturbation = rng.standard_normal(D) * scale
        old_vec = vecs[idx].copy()

        vecs[idx] += perturbation
        vecs[idx] /= np.linalg.norm(vecs[idx])

        new_loss = _incremental_loss(vecs, idx, current_loss, old_vec)

        if new_loss < current_loss:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        else:
            vecs[idx] = old_vec

        if verbose and (it + 1) % 50_000 == 0:
            elapsed = time.time() - t0
            rate = improvements / (it + 1) * 100
            print(
                f"  iter {it+1:>7d} | loss {best_loss:.14f} | "
                f"improvements {improvements} ({rate:.2f}%) | {elapsed:.0f}s"
            )

    return best_vecs, best_loss


def multi_scale_perturbation(
    vecs: np.ndarray,
    scales: list[float] | None = None,
    iters_per_scale: int = 200_000,
    seed: int = 42,
    verbose: bool = True,
) -> tuple[np.ndarray, float]:
    """Run micro-perturbation at multiple scales, finest first."""
    if scales is None:
        scales = [1e-7, 1e-8, 1e-9, 1e-10]

    best_vecs = vecs.copy()
    best_loss, _, _ = overlap_loss_fast(vecs)

    for scale in scales:
        if verbose:
            print(f"\n--- Scale {scale:.0e} ---")
        vecs, loss = targeted_perturbation(
            best_vecs.copy(), scale=scale, n_iters=iters_per_scale,
            seed=seed, verbose=verbose,
        )
        if loss < best_loss:
            best_loss = loss
            best_vecs = vecs.copy()
        seed += 1

    return best_vecs, best_loss


def save_solution(vecs: np.ndarray, score: float, tag: str = "best"):
    """Save solution to results directory."""
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {
        "vectors": vecs.tolist(),
        "score": score,
        "tag": tag,
    }
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"Saved to {path} (score={score:.14f})")


def main():
    print("=" * 60)
    print("Problem 6: Kissing Number (d=11, n=594)")
    print("=" * 60)

    # Load SOTA
    vecs = load_sota()
    initial_loss, _, _ = overlap_loss_fast(vecs)
    print(f"SOTA score: {initial_loss:.14f}")

    # Verify with exact evaluator
    from einstein.kissing_number.evaluator import overlap_loss as eval_loss
    exact_score = eval_loss(vecs)
    print(f"Exact eval: {exact_score:.14f}")

    # Phase 1: Gradient descent to find gradient basin
    print("\n=== Phase 1: Riemannian Gradient Descent ===")
    vecs_gd, loss_gd = riemannian_gd(vecs.copy(), lr=1e-6, n_iters=2000)
    if loss_gd < initial_loss:
        print(f"GD improved: {initial_loss:.14f} -> {loss_gd:.14f}")
        best_vecs, best_loss = vecs_gd, loss_gd
    else:
        print(f"GD no improvement (basin is flat at this scale)")
        best_vecs, best_loss = vecs.copy(), initial_loss

    # Phase 2: Multi-scale micro-perturbation
    print("\n=== Phase 2: Multi-Scale Micro-Perturbation ===")
    vecs_mp, loss_mp = multi_scale_perturbation(
        best_vecs, iters_per_scale=500_000, verbose=True
    )
    if loss_mp < best_loss:
        print(f"\nImproved: {best_loss:.14f} -> {loss_mp:.14f}")
        best_vecs, best_loss = vecs_mp, loss_mp
    else:
        print(f"\nNo improvement from perturbation")

    # Phase 3: Another round of gradient descent + perturbation
    print("\n=== Phase 3: Polish ===")
    vecs_p, loss_p = riemannian_gd(best_vecs.copy(), lr=1e-7, n_iters=1000)
    if loss_p < best_loss:
        best_vecs, best_loss = vecs_p, loss_p

    vecs_p2, loss_p2 = targeted_perturbation(
        best_vecs.copy(), scale=1e-10, n_iters=500_000, seed=100
    )
    if loss_p2 < best_loss:
        best_vecs, best_loss = vecs_p2, loss_p2

    # Final verification
    final_score = eval_loss(best_vecs)
    print(f"\n{'=' * 60}")
    print(f"Final score (exact): {final_score:.14f}")
    print(f"SOTA score:          {initial_loss:.14f}")
    print(f"Improvement:         {initial_loss - final_score:.2e}")
    print(f"{'=' * 60}")

    if final_score < initial_loss:
        save_solution(best_vecs, final_score, tag="best")
        print("NEW BEST! Solution saved.")
    else:
        print("No improvement over SOTA.")


if __name__ == "__main__":
    main()
