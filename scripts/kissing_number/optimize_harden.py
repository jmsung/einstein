"""Harden #1 position: extended micro-perturbation at sweet-spot scales.

Focuses on scales 1e-12 through 1e-14 with heavy iteration counts
and multiple seeds to maximize margin over CHRONOS.

Usage:
    uv run python scripts/kissing_number/optimize_harden.py
"""

import json
import time
from pathlib import Path

import numpy as np

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


def overlap_loss_exact(unit_vecs):
    """O(n^2) exact evaluator matching arena verifier."""
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


def run_perturbation(vecs, scale, n_iters, seed):
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
    t0 = time.time()
    contribs = vector_contributions(vecs)
    probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N

    for it in range(n_iters):
        if it > 0 and it % 50_000 == 0:
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

        if (it + 1) % 500_000 == 0:
            elapsed = time.time() - t0
            rate = improvements / (it + 1) * 100
            exact = overlap_loss_exact(best_vecs)
            print(
                f"  [{scale:.0e}] {it+1:>10,d} | exact {exact:.15f} | "
                f"impr {improvements:>6d} ({rate:.3f}%) | {elapsed:.0f}s"
            )

    return best_vecs, best_loss, improvements


def save_solution(vecs, score, tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag} (score={score:.15f})")


def main():
    print("=" * 70)
    print("HARDEN #1: Extended micro-perturbation at sweet-spot scales")
    print("=" * 70)

    vecs = load_best()
    initial = overlap_loss_exact(vecs)
    print(f"Start:   {initial:.15f}")
    print(f"CHRONOS: 0.156133162413645")
    print(f"Margin:  {0.15613316241364483 - initial:.2e}")
    best_vecs, best_score = vecs.copy(), initial

    # Alternating scales with different seeds for diversity
    # 1e-12 = sweet spot (0.10% rate), 1e-13 (0.07%), 1e-14 (0.05%)
    rng = np.random.default_rng(2026)
    configs = [
        (1e-12, 5_000_000, int(rng.integers(100000))),
        (1e-13, 5_000_000, int(rng.integers(100000))),
        (1e-12, 5_000_000, int(rng.integers(100000))),
        (1e-14, 5_000_000, int(rng.integers(100000))),
        (1e-13, 5_000_000, int(rng.integers(100000))),
        (1e-12, 5_000_000, int(rng.integers(100000))),
    ]

    for i, (scale, iters, seed) in enumerate(configs):
        print(f"\n--- Round {i+1}/{len(configs)}: {scale:.0e}, {iters:,}, seed={seed} ---")
        new_vecs, _, n_impr = run_perturbation(best_vecs.copy(), scale, iters, seed)
        exact = overlap_loss_exact(new_vecs)
        delta = best_score - exact
        print(f"  Exact: {exact:.15f} (delta={delta:.2e}, {n_impr} improvements)")
        if exact < best_score:
            best_score = exact
            best_vecs = new_vecs.copy()
            save_solution(best_vecs, best_score)
            margin = 0.15613316241364483 - best_score
            print(f"  New margin over CHRONOS: {margin:.2e}")

    final = overlap_loss_exact(best_vecs)
    margin = 0.15613316241364483 - final
    print(f"\n{'='*70}")
    print(f"Final:   {final:.15f}")
    print(f"Start:   {initial:.15f}")
    print(f"Delta:   {initial - final:.2e}")
    print(f"Margin:  {margin:.2e} (was 5.98e-9)")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
