"""Cage escape: coordinated multi-vector optimization targeting worst pairs.

The SOTA loss is dominated by 3 pairs (72.5% of total):
  (394,414): 30.9% — cos=0.524
  (90,528):  27.0% — cos=0.521
  (32,167):  14.6% — cos=0.511

Strategy: simultaneously perturb the worst vectors AND their pinning
neighbors to find coordinated moves that reduce the dominant penalties.

Approaches:
1. SA with multi-vector moves targeting the cage
2. Subset optimization (move ~50 vectors involved in worst pairs)
3. Directional push: move worst pair vectors away from each other
4. Basin hopping on the cage subspace

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/optimize_cage_escape.py
"""

import json
import time
from pathlib import Path

import numpy as np
from scipy.linalg import expm

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


def find_cage_vectors(vecs, n_target=50):
    """Find the vectors involved in worst overlapping pairs + their neighbors."""
    gram = vecs @ vecs.T
    n = len(vecs)
    i_idx, j_idx = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[i_idx, j_idx], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    penalties = np.maximum(0.0, 2.0 - dists)

    # Per-vector contribution
    contribs = np.zeros(n)
    mask = penalties > 0
    np.add.at(contribs, i_idx[mask], penalties[mask])
    np.add.at(contribs, j_idx[mask], penalties[mask])

    # Start with top contributors
    cage = set(np.argsort(-contribs)[:n_target])

    # Add overlapping neighbors of top vectors
    top_vecs = np.argsort(-contribs)[:10]
    for v in top_vecs:
        for k in range(len(i_idx)):
            if not mask[k]:
                continue
            if i_idx[k] == v:
                cage.add(j_idx[k])
            elif j_idx[k] == v:
                cage.add(i_idx[k])

    cage = sorted(cage)
    print(f"Cage: {len(cage)} vectors (top {n_target} + neighbors of top 10)")
    return np.array(cage)


def multi_vector_perturbation(vecs, cage_indices, scale, n_iters, seed, accept_worse_prob=0.0):
    """Perturb multiple cage vectors simultaneously with optional SA acceptance."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
    accepted_worse = 0
    n_cage = len(cage_indices)

    for it in range(n_iters):
        # Pick 1-5 cage vectors to perturb simultaneously
        n_move = rng.integers(1, min(6, n_cage + 1))
        indices = rng.choice(cage_indices, n_move, replace=False)

        old_vecs = vecs[indices].copy()
        for idx in indices:
            vecs[idx] += rng.standard_normal(D) * scale
            vecs[idx] /= np.linalg.norm(vecs[idx])

        new_loss = overlap_loss_fast(vecs)

        if new_loss < current_loss:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        elif accept_worse_prob > 0 and rng.random() < accept_worse_prob:
            # SA acceptance of worse solution
            current_loss = new_loss
            accepted_worse += 1
        else:
            vecs[indices] = old_vecs

        if (it + 1) % 100_000 == 0:
            exact = overlap_loss_exact(best_vecs)
            print(
                f"  [{scale:.0e}] {it+1:>8,d} | exact {exact:.15f} | "
                f"impr {improvements} | worse_accepted {accepted_worse}"
            )

    return best_vecs, best_loss, improvements


def directional_push(vecs, pair_i, pair_j, scale, n_iters, seed):
    """Push two vectors apart along their connecting direction."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0

    for it in range(n_iters):
        # Direction: push i away from j and vice versa
        # Add random tangent component for exploration
        direction_ij = vecs[pair_j] - vecs[pair_i]
        direction_ij /= np.linalg.norm(direction_ij) + 1e-30

        # Random perturbation with bias away from partner
        noise_i = rng.standard_normal(D) * scale - direction_ij * scale * 0.5
        noise_j = rng.standard_normal(D) * scale + direction_ij * scale * 0.5

        old_i, old_j = vecs[pair_i].copy(), vecs[pair_j].copy()

        vecs[pair_i] += noise_i
        vecs[pair_i] /= np.linalg.norm(vecs[pair_i])
        vecs[pair_j] += noise_j
        vecs[pair_j] /= np.linalg.norm(vecs[pair_j])

        new_loss = overlap_loss_fast(vecs)
        if new_loss < current_loss:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        else:
            vecs[pair_i] = old_i
            vecs[pair_j] = old_j

        if (it + 1) % 100_000 == 0:
            exact = overlap_loss_exact(best_vecs)
            print(
                f"  push({pair_i},{pair_j}) [{scale:.0e}] {it+1:>8,d} | "
                f"exact {exact:.15f} | impr {improvements}"
            )

    return best_vecs, best_loss, improvements


def so11_rotation_escape(vecs, cage_indices, theta_range, n_iters, seed):
    """Apply random SO(11) rotations to cage subset and accept if better."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
    n_cage = len(cage_indices)

    for it in range(n_iters):
        # Random subset of cage to rotate (10-50 vectors)
        m = rng.integers(5, min(51, n_cage + 1))
        subset = rng.choice(cage_indices, m, replace=False)

        # Generate small random SO(11) rotation
        theta = rng.uniform(theta_range[0], theta_range[1])
        # Random skew-symmetric matrix
        A = rng.standard_normal((D, D))
        A = (A - A.T) / 2  # skew-symmetric
        A /= np.linalg.norm(A) + 1e-30
        R = expm(theta * A)

        old_vecs = vecs[subset].copy()
        vecs[subset] = (R @ vecs[subset].T).T
        # Renormalize (rotation should preserve norms but numerical safety)
        norms = np.linalg.norm(vecs[subset], axis=1, keepdims=True)
        vecs[subset] /= norms

        new_loss = overlap_loss_fast(vecs)
        if new_loss < current_loss:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        else:
            vecs[subset] = old_vecs

        if (it + 1) % 10_000 == 0:
            exact = overlap_loss_exact(best_vecs)
            print(
                f"  SO(11) [{theta_range}] {it+1:>8,d} | exact {exact:.15f} | "
                f"impr {improvements}"
            )

    return best_vecs, best_loss, improvements


def sa_multi_scale(vecs, cage_indices, n_iters, seed):
    """Simulated annealing with multi-vector moves at varying scales."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
    accepted_worse = 0
    n_cage = len(cage_indices)

    # Temperature schedule: start high, cool slowly
    T_init = 1e-4
    T_min = 1e-10
    T = T_init

    scales = [1e-4, 1e-5, 1e-6, 1e-7, 1e-8]

    for it in range(n_iters):
        # Adaptive temperature
        T = T_init * (T_min / T_init) ** (it / n_iters)

        # Random scale selection (bias toward finer at low T)
        scale_idx = min(int(it / n_iters * len(scales)), len(scales) - 1)
        scale = scales[scale_idx]

        # Multi-vector move
        n_move = rng.integers(1, min(8, n_cage + 1))
        indices = rng.choice(cage_indices, n_move, replace=False)
        old_vecs_save = vecs[indices].copy()

        for idx in indices:
            vecs[idx] += rng.standard_normal(D) * scale
            vecs[idx] /= np.linalg.norm(vecs[idx])

        new_loss = overlap_loss_fast(vecs)
        delta = new_loss - current_loss

        if delta < 0:
            current_loss = new_loss
            improvements += 1
            if current_loss < best_loss:
                best_loss = current_loss
                best_vecs = vecs.copy()
        elif T > 0 and rng.random() < np.exp(-delta / T):
            current_loss = new_loss
            accepted_worse += 1
        else:
            vecs[indices] = old_vecs_save

        if (it + 1) % 200_000 == 0:
            exact = overlap_loss_exact(best_vecs)
            print(
                f"  SA T={T:.2e} s={scale:.0e} | {it+1:>8,d} | exact {exact:.15f} | "
                f"impr {improvements} | worse {accepted_worse}"
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
    print("CAGE ESCAPE: Coordinated multi-vector optimization")
    print("=" * 70)

    vecs = load_best()
    initial = overlap_loss_exact(vecs)
    print(f"Start: {initial:.15f}")
    best_vecs, best_score = vecs.copy(), initial

    # Find cage vectors
    cage = find_cage_vectors(vecs, n_target=50)

    # Phase 1: Directional push on worst 3 pairs
    print("\n=== Phase 1: Directional push on worst pairs ===")
    worst_pairs = [(394, 414), (90, 528), (32, 167)]
    for pair_i, pair_j in worst_pairs:
        for scale in [1e-5, 1e-6, 1e-7, 1e-8]:
            v, l, n = directional_push(best_vecs.copy(), pair_i, pair_j, scale, 200_000, 42)
            if l < best_score:
                best_score = l
                best_vecs = v.copy()
                exact = overlap_loss_exact(best_vecs)
                print(f"  Improved! exact={exact:.15f}")
                save_solution(best_vecs, exact)

    # Phase 2: Multi-vector cage perturbation
    print("\n=== Phase 2: Multi-vector cage perturbation ===")
    for scale in [1e-5, 1e-6, 1e-7, 1e-8]:
        for seed in [100, 200, 300]:
            v, l, n = multi_vector_perturbation(
                best_vecs.copy(), cage, scale, 500_000, seed, accept_worse_prob=0.0
            )
            if l < best_score:
                best_score = l
                best_vecs = v.copy()
                exact = overlap_loss_exact(best_vecs)
                print(f"  Improved! exact={exact:.15f}")
                save_solution(best_vecs, exact)

    # Phase 3: SA with multi-vector moves on cage
    print("\n=== Phase 3: Simulated annealing on cage ===")
    for seed in [1000, 2000, 3000]:
        v, l, n = sa_multi_scale(best_vecs.copy(), cage, 2_000_000, seed)
        if l < best_score:
            best_score = l
            best_vecs = v.copy()
            exact = overlap_loss_exact(best_vecs)
            print(f"  SA improved! exact={exact:.15f}")
            save_solution(best_vecs, exact)

    # Phase 4: SO(11) rotation escape
    print("\n=== Phase 4: SO(11) rotation of cage subsets ===")
    for theta_range in [(0.001, 0.01), (0.01, 0.1), (0.1, 0.5)]:
        for seed in [4000, 5000]:
            v, l, n = so11_rotation_escape(best_vecs.copy(), cage, theta_range, 50_000, seed)
            if l < best_score:
                best_score = l
                best_vecs = v.copy()
                exact = overlap_loss_exact(best_vecs)
                print(f"  Rotation improved! exact={exact:.15f}")
                save_solution(best_vecs, exact)

    # Final fine polish
    print("\n=== Phase 5: Fine polish (1e-12 to 1e-14) ===")
    from scripts.kissing_number.optimize_harden import run_perturbation
    for scale in [1e-12, 1e-13]:
        v, l, n = run_perturbation(best_vecs.copy(), scale, 5_000_000, 9999)
        if l < best_score:
            best_score = l
            best_vecs = v.copy()

    final = overlap_loss_exact(best_vecs)
    print(f"\n{'='*70}")
    print(f"Final:   {final:.15f}")
    print(f"Start:   {initial:.15f}")
    print(f"Delta:   {initial - final:.2e}")
    print(f"{'='*70}")

    if final < initial:
        save_solution(best_vecs, final)


if __name__ == "__main__":
    main()
