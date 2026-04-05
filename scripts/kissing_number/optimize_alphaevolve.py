"""Optimize from an alternative 593-vector starting point + 1 additional vector.

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/optimize_alphaevolve.py
"""

import json
import time
from pathlib import Path

import numpy as np

RESULTS_DIR = Path("results/problem-6-kissing-number")
N = 594
D = 11


def overlap_loss_exact(unit_vecs):
    centers = 2.0 * unit_vecs
    diff = centers[:, None, :] - centers[None, :, :]
    dists = np.sqrt(np.sum(diff**2, axis=-1))
    n = len(unit_vecs)
    i, j = np.triu_indices(n, k=1)
    return float(np.sum(np.maximum(0.0, 2.0 - dists[i, j])))


def overlap_loss_fast(unit_vecs):
    gram = unit_vecs @ unit_vecs.T
    n = len(unit_vecs)
    i, j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[i, j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    return float(np.sum(np.maximum(0.0, 2.0 - dists)))


def incremental_loss(vecs, idx, old_total, old_vec):
    others = np.concatenate([vecs[:idx], vecs[idx + 1 :]], axis=0)
    old_cos = np.clip(old_vec @ others.T, -1.0, 1.0)
    old_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - old_cos))
    old_p = np.maximum(0.0, 2.0 - old_d)
    new_cos = np.clip(vecs[idx] @ others.T, -1.0, 1.0)
    new_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - new_cos))
    new_p = np.maximum(0.0, 2.0 - new_d)
    return old_total - float(np.sum(old_p)) + float(np.sum(new_p))


def vector_contributions(vecs):
    gram = vecs @ vecs.T
    n = len(vecs)
    i, j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[i, j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    pens = np.maximum(0.0, 2.0 - dists)
    c = np.zeros(n)
    np.add.at(c, i, pens)
    np.add.at(c, j, pens)
    return c


def optimize_594th_vector(vecs, n_trials=1_000_000, seed=42):
    """Find the best position for vector 593 (the added one) via targeted search."""
    rng = np.random.default_rng(seed)
    vecs593 = vecs[:593]
    best_vec = vecs[593].copy()
    best_loss = overlap_loss_fast(vecs)

    print(f"  Optimizing 594th vector position ({n_trials} trials)...")
    t0 = time.time()

    for trial in range(n_trials):
        # Try random vectors on S^10
        v = rng.standard_normal(D)
        v /= np.linalg.norm(v)

        # Quick overlap check with 593 existing
        cos_vals = vecs593 @ v
        cos_vals = np.clip(cos_vals, -1.0, 1.0)
        dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
        penalties = np.maximum(0.0, 2.0 - dists)
        loss = float(np.sum(penalties))

        if loss < best_loss:
            best_loss = loss
            best_vec = v.copy()

        if (trial + 1) % 200_000 == 0:
            print(f"    {trial+1}: best_loss={best_loss:.10f} ({time.time()-t0:.0f}s)")

    vecs[593] = best_vec
    return vecs, best_loss


def targeted_perturbation(vecs, scale, n_iters, seed, recompute_every=50_000):
    """Targeted micro-perturbation with contribution-weighted sampling."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
    t0 = time.time()
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

        if (it + 1) % 1_000_000 == 0:
            elapsed = time.time() - t0
            rate = improvements / (it + 1) * 100
            exact = overlap_loss_exact(best_vecs)
            print(
                f"  [{scale:.0e}] {it+1:>10,d} | exact {exact:.15f} | "
                f"impr {improvements:>6d} ({rate:.3f}%) | {elapsed:.0f}s"
            )

    return best_vecs, best_loss, improvements


def save_solution(vecs, score, tag="alphaevolve_best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag} (score={score:.15f})")


def main():
    print("=" * 70)
    print("OPTIMIZE FROM ALPHAEVOLVE 593+1 STARTING POINT")
    print("=" * 70)

    # Load AlphaEvolve initial solution
    with open(RESULTS_DIR / "alphaevolve_594_initial.json") as f:
        data = json.load(f)
    vecs = np.array(data["vectors"], dtype=np.float64)
    initial = overlap_loss_exact(vecs)
    print(f"Initial score: {initial:.15f}")
    # Compare against current best from solution_best.json

    # Phase 0: Better 594th vector placement
    print("\n=== Phase 0: Optimize 594th vector position ===")
    vecs, loss0 = optimize_594th_vector(vecs, n_trials=2_000_000, seed=42)
    exact0 = overlap_loss_exact(vecs)
    print(f"  After placement: {exact0:.15f}")
    best_vecs, best_score = vecs.copy(), exact0

    # Phase 1: Coarse optimization (scale 1e-4 to 1e-6)
    print("\n=== Phase 1: Coarse optimization ===")
    for scale in [1e-4, 1e-5, 1e-6]:
        v, l, n = targeted_perturbation(best_vecs.copy(), scale, 5_000_000, seed=100)
        exact = overlap_loss_exact(v)
        print(f"  Scale {scale:.0e}: exact={exact:.15f} ({n} improvements)")
        if exact < best_score:
            best_score = exact
            best_vecs = v.copy()
            save_solution(best_vecs, best_score)

    # Phase 2: Medium optimization (scale 1e-7 to 1e-9)
    print("\n=== Phase 2: Medium optimization ===")
    for scale in [1e-7, 1e-8, 1e-9]:
        v, l, n = targeted_perturbation(best_vecs.copy(), scale, 5_000_000, seed=200)
        exact = overlap_loss_exact(v)
        print(f"  Scale {scale:.0e}: exact={exact:.15f} ({n} improvements)")
        if exact < best_score:
            best_score = exact
            best_vecs = v.copy()
            save_solution(best_vecs, best_score)

    # Phase 3: Fine optimization (scale 1e-10 to 1e-12)
    print("\n=== Phase 3: Fine optimization ===")
    for scale in [1e-10, 1e-11, 1e-12]:
        v, l, n = targeted_perturbation(best_vecs.copy(), scale, 5_000_000, seed=300)
        exact = overlap_loss_exact(v)
        print(f"  Scale {scale:.0e}: exact={exact:.15f} ({n} improvements)")
        if exact < best_score:
            best_score = exact
            best_vecs = v.copy()
            save_solution(best_vecs, best_score)

    final = overlap_loss_exact(best_vecs)
    print(f"\n{'='*70}")
    print(f"Final:   {final:.15f}")
    print(f"Start:   {initial:.15f}")
    print(f"{'='*70}")
    if final < initial:
        print("*** BEATS SOTA! ***")
        save_solution(best_vecs, final, tag="best")
    else:
        print(f"Does not beat SOTA (gap: {final - initial:.2e})")


if __name__ == "__main__":
    main()
