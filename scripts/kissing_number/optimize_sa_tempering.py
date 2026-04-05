"""Simulated annealing with parallel tempering.

Multiple replicas at geometric temperature ladder with Metropolis acceptance.
Periodic replica exchange between adjacent temperatures.
Configure via environment variables: N_REPLICAS, SCALE, N_ITERS.

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/optimize_sa_tempering.py
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


def save_solution(vecs, score, tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag} (score={score:.15f})")


def main():
    print("=" * 70)
    print("SA + PARALLEL TEMPERING: 8 replicas, geometric temperature ladder")
    print("=" * 70)

    vecs_init = load_best()
    initial = overlap_loss_exact(vecs_init)
    print(f"Start: {initial:.15f}")

    # Configuration
    N_REP = 8
    temps = np.geomspace(1e-12, 1e-4, N_REP)
    print(f"Temperatures: {[f'{t:.1e}' for t in temps]}")

    n_iters = 20_000_000  # per replica
    swap_interval = 500
    scale = 1e-6  # perturbation scale (much larger than greedy)
    recompute_every = 50_000

    rng = np.random.default_rng(42)

    # Initialize replicas
    replicas = [vecs_init.copy() for _ in range(N_REP)]
    losses = [overlap_loss_fast(r) for r in replicas]
    best_loss = min(losses)
    best_vecs = replicas[np.argmin(losses)].copy()

    # Per-replica stats
    accepts = [0] * N_REP
    improvements = [0] * N_REP
    swaps_attempted = 0
    swaps_accepted = 0

    # Contribution-weighted probabilities (shared, updated periodically)
    contribs = vector_contributions(replicas[0])
    probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N

    t0 = time.time()

    for it in range(n_iters):
        # Recompute contribution probabilities periodically
        if it > 0 and it % recompute_every == 0:
            contribs = vector_contributions(replicas[0])  # use coldest replica
            probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(N) / N

        # Metropolis step for each replica
        for r in range(N_REP):
            idx = rng.choice(N, p=probs)
            old_vec = replicas[r][idx].copy()
            replicas[r][idx] += rng.standard_normal(D) * scale
            replicas[r][idx] /= np.linalg.norm(replicas[r][idx])

            new_loss = incremental_loss(replicas[r], idx, losses[r], old_vec)
            delta_E = new_loss - losses[r]

            if delta_E < 0:
                losses[r] = new_loss
                accepts[r] += 1
                if new_loss < best_loss:
                    best_loss = new_loss
                    best_vecs = replicas[r].copy()
                    improvements[r] += 1
            elif temps[r] > 0 and rng.random() < np.exp(-delta_E / temps[r]):
                losses[r] = new_loss
                accepts[r] += 1
            else:
                replicas[r][idx] = old_vec

        # Replica exchange (swap adjacent temperatures)
        if (it + 1) % swap_interval == 0:
            for r in range(N_REP - 1):
                swaps_attempted += 1
                delta = (losses[r] - losses[r + 1]) * (1.0 / temps[r] - 1.0 / temps[r + 1])
                if rng.random() < min(1.0, np.exp(delta)):
                    replicas[r], replicas[r + 1] = replicas[r + 1], replicas[r]
                    losses[r], losses[r + 1] = losses[r + 1], losses[r]
                    swaps_accepted += 1

        # Progress report
        if (it + 1) % 1_000_000 == 0:
            elapsed = time.time() - t0
            exact = overlap_loss_exact(best_vecs)
            swap_rate = swaps_accepted / max(1, swaps_attempted) * 100

            print(f"\n  iter {it+1:>10,d} | {elapsed:.0f}s")
            print(f"  BEST exact: {exact:.15f} (delta={initial - exact:.2e})")
            print(f"  Swap rate: {swap_rate:.1f}%")
            for r in range(N_REP):
                rate = accepts[r] / (it + 1) * 100
                print(f"    T={temps[r]:.1e}: loss={losses[r]:.10f}, accept={rate:.2f}%")

            if exact < initial:
                save_solution(best_vecs, exact)

            # Reset counters
            accepts = [0] * N_REP
            swaps_attempted = 0
            swaps_accepted = 0

    final = overlap_loss_exact(best_vecs)
    print(f"\n{'='*70}")
    print(f"Final:   {final:.15f}")
    print(f"Start:   {initial:.15f}")
    print(f"Delta:   {initial - final:.2e}")
    print(f"{'='*70}")

    if final < initial:
        save_solution(best_vecs, final, "best")
        print("Improved! Saved.")
    else:
        print("No improvement.")


if __name__ == "__main__":
    main()
