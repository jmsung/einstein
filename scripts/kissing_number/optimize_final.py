"""Final push: heavy 1e-13 and 1e-14 optimization.

Usage:
    uv run python scripts/kissing_number/optimize_final.py
"""

import json
import time
from pathlib import Path

import numpy as np

RESULTS_DIR = Path("results/problem-6-kissing-number")
N = 594
D = 11


def load_best():
    path = RESULTS_DIR / "solution_best.json"
    with open(path) as f:
        data = json.load(f)
    vecs = np.array(data["vectors"], dtype=np.float64)
    norms = np.linalg.norm(vecs, axis=1, keepdims=True)
    return vecs / norms


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
    others = np.concatenate([vecs[:idx], vecs[idx+1:]], axis=0)
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


def run(vecs, scale, n_iters, seed):
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

        if (it + 1) % 1_000_000 == 0:
            elapsed = time.time() - t0
            rate = improvements / (it + 1) * 100
            exact = overlap_loss_exact(best_vecs)
            print(f"  [{scale:.0e}] {it+1:>10,d} | exact {exact:.15f} | impr {improvements:>6d} ({rate:.3f}%) | {elapsed:.0f}s")

    return best_vecs, best_loss, improvements


def save_solution(vecs, score, tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved (score={score:.15f})")


def main():
    print("=" * 70)
    print("FINAL PUSH")
    print("=" * 70)

    vecs = load_best()
    initial = overlap_loss_exact(vecs)
    print(f"Start: {initial:.15f}")
    best_vecs, best_score = vecs.copy(), initial

    configs = [
        (1e-13, 10_000_000, 9001),
        (1e-14, 10_000_000, 9002),
        (1e-13, 10_000_000, 9003),
        (1e-14, 10_000_000, 9004),
    ]

    for i, (scale, iters, seed) in enumerate(configs):
        print(f"\n--- Round {i+1}/{len(configs)}: {scale:.0e}, {iters:,} ---")
        new_vecs, _, n_impr = run(best_vecs.copy(), scale, iters, seed)
        exact = overlap_loss_exact(new_vecs)
        print(f"  Exact: {exact:.15f} ({n_impr} improvements)")
        if exact < best_score:
            best_score = exact
            best_vecs = new_vecs.copy()
            save_solution(best_vecs, best_score)

    final = overlap_loss_exact(best_vecs)
    print(f"\n{'='*70}")
    print(f"Final:   {final:.15f}")
    print(f"Start:   {initial:.15f}")
    print(f"vs SOTA: {0.15613316241364 - final:.2e}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
