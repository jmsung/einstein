"""Extended optimizer: push 1e-10 and 1e-11 scale perturbation much harder.

Usage:
    uv run python scripts/kissing_number/optimize_extended.py
"""

import json
import time
from pathlib import Path

import numpy as np

RESULTS_DIR = Path("results/problem-6-kissing-number")
N = 594
D = 11


def load_best() -> tuple[np.ndarray, float]:
    """Load the best solution we have."""
    for name in ["solution_best.json", "sota_vectors.json"]:
        path = RESULTS_DIR / name
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            vecs = np.array(data["vectors"], dtype=np.float64)
            norms = np.linalg.norm(vecs, axis=1, keepdims=True)
            vecs = vecs / norms
            score = overlap_loss_exact(vecs)
            print(f"Loaded {name}: {score:.14f}")
            return vecs, score
    raise FileNotFoundError("No solution found")


def overlap_loss_exact(unit_vecs: np.ndarray) -> float:
    """Exact overlap loss matching arena verifier."""
    centers = 2.0 * unit_vecs
    diff = centers[:, None, :] - centers[None, :, :]
    dists = np.sqrt(np.sum(diff**2, axis=-1))
    n = len(unit_vecs)
    idx_i, idx_j = np.triu_indices(n, k=1)
    penalties = np.maximum(0.0, 2.0 - dists[idx_i, idx_j])
    return float(np.sum(penalties))


def overlap_loss_fast(unit_vecs: np.ndarray) -> float:
    """Fast loss via dot products."""
    gram = unit_vecs @ unit_vecs.T
    n = len(unit_vecs)
    idx_i, idx_j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[idx_i, idx_j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    penalties = np.maximum(0.0, 2.0 - dists)
    return float(np.sum(penalties))


def incremental_loss(vecs, idx, old_total, old_vec):
    """O(n) incremental loss update."""
    others = np.concatenate([vecs[:idx], vecs[idx+1:]], axis=0)
    old_cos = np.clip(old_vec @ others.T, -1.0, 1.0)
    old_dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - old_cos))
    old_pen = np.maximum(0.0, 2.0 - old_dists)
    new_cos = np.clip(vecs[idx] @ others.T, -1.0, 1.0)
    new_dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - new_cos))
    new_pen = np.maximum(0.0, 2.0 - new_dists)
    return old_total - float(np.sum(old_pen)) + float(np.sum(new_pen))


def vector_contributions(vecs):
    """Per-vector overlap contribution for targeted sampling."""
    gram = vecs @ vecs.T
    n = len(vecs)
    idx_i, idx_j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[idx_i, idx_j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    penalties = np.maximum(0.0, 2.0 - dists)
    contribs = np.zeros(n)
    np.add.at(contribs, idx_i, penalties)
    np.add.at(contribs, idx_j, penalties)
    return contribs


def targeted_perturb(vecs, scale, n_iters, seed=42, recompute_every=20_000):
    """Targeted micro-perturbation at a given scale."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
    t0 = time.time()

    # Initial target probabilities
    contribs = vector_contributions(vecs)
    probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N

    for it in range(n_iters):
        if it > 0 and it % recompute_every == 0:
            contribs = vector_contributions(vecs)
            probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N

        idx = rng.choice(N, p=probs)
        old_vec = vecs[idx].copy()
        vecs[idx] += rng.standard_normal(D) * scale
        vecs[idx] /= np.linalg.norm(vecs[idx])

        new_loss = incremental_loss(vecs, idx, current_loss, old_vec)
        if new_loss < current_loss:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        else:
            vecs[idx] = old_vec

        if (it + 1) % 100_000 == 0:
            elapsed = time.time() - t0
            rate = improvements / (it + 1) * 100
            # Periodically sync with exact evaluator
            exact = overlap_loss_exact(best_vecs) if (it + 1) % 500_000 == 0 else best_loss
            print(
                f"  [{scale:.0e}] iter {it+1:>8d} | fast {best_loss:.14f} | "
                f"impr {improvements} ({rate:.3f}%) | {elapsed:.0f}s"
                + (f" | exact {exact:.14f}" if (it + 1) % 500_000 == 0 else "")
            )

    return best_vecs, best_loss, improvements


def save_solution(vecs, score, tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {path} (score={score:.14f})")


def main():
    print("=" * 70)
    print("Extended Optimizer: Kissing Number (d=11, n=594)")
    print("=" * 70)

    vecs, initial_score = load_best()
    print(f"Starting score: {initial_score:.14f}")

    best_vecs = vecs.copy()
    best_score = initial_score

    # Strategy: alternate targeted perturbation at 1e-10 and 1e-11
    # with different seeds, for many rounds
    configs = [
        (1e-10, 2_000_000, 42),
        (1e-11, 2_000_000, 137),
        (1e-10, 2_000_000, 256),
        (1e-11, 2_000_000, 512),
        (1e-10, 2_000_000, 789),
        (1e-11, 2_000_000, 1024),
        (1e-12, 2_000_000, 2048),
    ]

    for i, (scale, iters, seed) in enumerate(configs):
        print(f"\n--- Round {i+1}/{len(configs)}: scale={scale:.0e}, iters={iters:,}, seed={seed} ---")
        new_vecs, new_loss, n_impr = targeted_perturb(
            best_vecs.copy(), scale=scale, n_iters=iters, seed=seed,
        )
        # Verify with exact evaluator
        exact_score = overlap_loss_exact(new_vecs)
        print(f"  Exact score: {exact_score:.14f} ({n_impr} improvements)")

        if exact_score < best_score:
            best_score = exact_score
            best_vecs = new_vecs.copy()
            save_solution(best_vecs, best_score)

    # Final verification
    final_exact = overlap_loss_exact(best_vecs)
    print(f"\n{'=' * 70}")
    print(f"Final score:    {final_exact:.14f}")
    print(f"Initial score:  {initial_score:.14f}")
    print(f"Improvement:    {initial_score - final_exact:.2e}")
    print(f"{'=' * 70}")

    if final_exact < initial_score:
        save_solution(best_vecs, final_exact, tag="best")


if __name__ == "__main__":
    main()
