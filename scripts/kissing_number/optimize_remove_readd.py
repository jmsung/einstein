"""Remove-and-re-add strategy: reframe the 594-vector problem.

AlphaEvolve proved κ(11) ≥ 593 — so 593 vectors CAN achieve 0 overlap.
Strategy:
1. Remove the worst-contributing vector from our 594
2. Optimize remaining 593 toward 0 overlap (SA tempering)
3. Find optimal placement for the removed vector
4. Optimize all 594 from this new starting point

This is fundamentally different from polishing — it asks "what if we
rebuilt the configuration from a 593-vector zero-overlap base?"

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/optimize_remove_readd.py
"""

import json
import os
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
            return vecs / norms
    raise FileNotFoundError("No solution found")


def overlap_loss(unit_vecs):
    gram = unit_vecs @ unit_vecs.T
    n = len(unit_vecs)
    i, j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[i, j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    return float(np.sum(np.maximum(0.0, 2.0 - dists)))


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


def incremental_loss(vecs, idx, old_total, old_vec):
    others = np.concatenate([vecs[:idx], vecs[idx + 1:]], axis=0)
    old_cos = np.clip(old_vec @ others.T, -1.0, 1.0)
    old_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - old_cos))
    old_p = np.maximum(0.0, 2.0 - old_d)
    new_cos = np.clip(vecs[idx] @ others.T, -1.0, 1.0)
    new_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - new_cos))
    new_p = np.maximum(0.0, 2.0 - new_d)
    return old_total - float(np.sum(old_p)) + float(np.sum(new_p))


def targeted_perturbation(vecs, scale, n_iters, seed):
    """SA with contribution-weighted sampling."""
    rng = np.random.default_rng(seed)
    n = len(vecs)
    d = vecs.shape[1]
    best_vecs = vecs.copy()
    current_loss = overlap_loss(vecs)
    best_loss = current_loss
    improvements = 0

    contribs = vector_contributions(vecs)
    probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(n) / n

    for it in range(n_iters):
        if it > 0 and it % 50_000 == 0:
            contribs = vector_contributions(vecs)
            probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(n) / n

        idx = rng.choice(n, p=probs)
        old_vec = vecs[idx].copy()
        vecs[idx] += rng.standard_normal(d) * scale
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
            exact = overlap_loss(best_vecs)
            print(f"    [{scale:.0e}] {it+1:>8,d} | loss={exact:.15f} | impr={improvements}")

    return best_vecs, best_loss, improvements


def find_best_594th(vecs_593, n_trials=2_000_000, seed=42):
    """Search for optimal placement of 594th vector."""
    rng = np.random.default_rng(seed)
    best_loss = float("inf")
    best_vec = None

    for trial in range(n_trials):
        v = rng.standard_normal(D)
        v /= np.linalg.norm(v)

        cos_vals = np.clip(vecs_593 @ v, -1.0, 1.0)
        dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
        loss = float(np.sum(np.maximum(0.0, 2.0 - dists)))

        if loss < best_loss:
            best_loss = loss
            best_vec = v.copy()

        if (trial + 1) % 500_000 == 0:
            print(f"    {trial+1:,}: best_594th_loss={best_loss:.10f}")

    return best_vec, best_loss


def save_solution(vecs, score, tag="remove_readd"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag} (score={score:.15f})")


def main():
    n_iters_593 = int(os.environ.get("ITERS_593", "10000000"))
    n_iters_594 = int(os.environ.get("ITERS_594", "5000000"))

    print("=" * 70)
    print("REMOVE-AND-RE-ADD: Reframe 594 → 593+1")
    print("=" * 70)

    vecs = load_best()
    initial_594 = overlap_loss(vecs)
    print(f"Start (594 vectors): {initial_594:.15f}")

    # Step 1: Find worst vector
    contribs = vector_contributions(vecs)
    worst_idx = int(np.argmax(contribs))
    print(f"\nWorst vector: {worst_idx} (contribution={contribs[worst_idx]:.10f}, "
          f"{contribs[worst_idx]/initial_594*100:.1f}% of total)")

    # Step 2: Remove worst vector
    removed_vec = vecs[worst_idx].copy()
    vecs_593 = np.delete(vecs, worst_idx, axis=0)
    loss_593 = overlap_loss(vecs_593)
    print(f"After removal (593 vectors): {loss_593:.15f}")
    print(f"Loss reduction: {initial_594 - loss_593:.2e}")

    # Step 3: Optimize 593 toward 0 overlap
    print(f"\n=== Optimizing 593 vectors (target: 0 overlap) ===")
    best_593 = vecs_593.copy()
    best_593_loss = loss_593

    for scale in [1e-6, 1e-8, 1e-10, 1e-12]:
        iters = n_iters_593 // 4
        print(f"\n  Scale {scale:.0e}, {iters:,} iters:")
        v, l, n = targeted_perturbation(best_593.copy(), scale, iters, seed=42)
        exact = overlap_loss(v)
        print(f"  Result: {exact:.15f} ({n} improvements)")
        if exact < best_593_loss:
            best_593_loss = exact
            best_593 = v.copy()

    print(f"\n593-vector result: {best_593_loss:.15f}")
    if best_593_loss < 1e-10:
        print("*** ZERO OVERLAP ACHIEVED for 593! ***")

    # Step 4: Find optimal 594th vector
    print(f"\n=== Finding optimal 594th vector ===")
    new_vec, new_vec_loss = find_best_594th(best_593, n_trials=2_000_000, seed=99)
    print(f"Best 594th vector overlap: {new_vec_loss:.10f}")

    # Step 5: Reassemble 594 and optimize
    vecs_594 = np.vstack([best_593, new_vec.reshape(1, -1)])
    loss_594 = overlap_loss(vecs_594)
    print(f"\nReassembled 594: {loss_594:.15f}")

    print(f"\n=== Final optimization of 594 vectors ===")
    best_594 = vecs_594.copy()
    best_594_loss = loss_594

    for scale in [1e-6, 1e-8, 1e-10, 1e-12]:
        iters = n_iters_594 // 4
        print(f"\n  Scale {scale:.0e}, {iters:,} iters:")
        v, l, n = targeted_perturbation(best_594.copy(), scale, iters, seed=200)
        exact = overlap_loss(v)
        print(f"  Result: {exact:.15f} ({n} improvements)")
        if exact < best_594_loss:
            best_594_loss = exact
            best_594 = v.copy()

    final = overlap_loss(best_594)
    print(f"\n{'='*70}")
    print(f"Original 594:  {initial_594:.15f}")
    print(f"Final 594:     {final:.15f}")
    print(f"Delta:         {initial_594 - final:.2e}")
    print(f"{'='*70}")

    if final < initial_594:
        save_solution(best_594, final)
        print("IMPROVED!")
    else:
        print("No improvement over original.")


if __name__ == "__main__":
    main()
