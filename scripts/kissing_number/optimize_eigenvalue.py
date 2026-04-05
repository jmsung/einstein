"""Eigenvalue-guided perturbation: exploit the deficient direction.

The Gram matrix may have a deficient eigenvalue direction where vectors
are underrepresented. Perturbing vectors INTO this direction could open
space for overlapping pairs to separate.

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/optimize_eigenvalue.py
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


def eigenvalue_analysis(vecs):
    """Analyze Gram matrix eigenstructure."""
    gram = vecs @ vecs.T
    eigvals, eigvecs = np.linalg.eigh(gram)
    # Sort descending
    idx = np.argsort(-eigvals)
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    ideal = N / D  # 594/11 = 54.0 for tight frame
    print(f"  Eigenvalues (ideal={ideal:.1f}):")
    for i in range(D):
        deficit = ideal - eigvals[i]
        print(f"    λ_{i}: {eigvals[i]:.4f} (deficit={deficit:.4f})")

    # The deficient direction: eigenvector of smallest non-zero eigenvalue
    thin_idx = D - 1  # last (smallest) eigenvalue in top-D
    thin_eigval = eigvals[thin_idx]
    thin_eigvec = eigvecs[:, thin_idx]  # (N,) — loading of each vector

    print(f"\n  Thin direction: λ_{thin_idx}={thin_eigval:.4f}")
    print(f"  Top contributors to thin direction:")
    top_loading = np.argsort(-np.abs(thin_eigvec))[:10]
    for v in top_loading:
        print(f"    vec {v}: loading={thin_eigvec[v]:.6f}")

    return eigvals[:D], eigvecs[:, :D], thin_eigvec


def eigenvalue_guided_perturbation(vecs, thin_eigvec, scale, n_iters, seed):
    """Perturb vectors biased toward the thin eigenvalue direction.

    Instead of random noise, bias the perturbation to push vectors
    into the underrepresented direction (where there's more room).
    """
    rng = np.random.default_rng(seed)
    n = len(vecs)
    d = vecs.shape[1]
    best_vecs = vecs.copy()
    current_loss = overlap_loss(vecs)
    best_loss = current_loss
    improvements = 0

    # The thin eigenvector tells us which vectors have low loading
    # in the deficient direction. These vectors should be pushed INTO
    # that direction.
    contribs = vector_contributions(vecs)
    probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(n) / n

    # Compute the actual thin direction in R^D
    # thin_eigvec is (N,) — loadings. We need the D-dimensional direction.
    # The thin direction in R^D is the column of V^T corresponding to
    # the smallest eigenvalue. For vecs (N, D), the Gram matrix is V V^T.
    # The thin direction in R^D is obtained from SVD.
    _, S, Vt = np.linalg.svd(vecs, full_matrices=False)
    thin_dir = Vt[-1]  # last right singular vector = thinnest direction
    print(f"  Thin direction in R^{d}: {thin_dir}")
    print(f"  Singular values: {S}")

    for it in range(n_iters):
        if it > 0 and it % 50_000 == 0:
            contribs = vector_contributions(vecs)
            probs = contribs / contribs.sum() if contribs.sum() > 0 else np.ones(n) / n

        idx = rng.choice(n, p=probs)
        old_vec = vecs[idx].copy()

        # Biased perturbation: random + bias toward thin direction
        noise = rng.standard_normal(d) * scale
        bias = thin_dir * scale * 0.5  # push toward thin direction
        vecs[idx] += noise + bias
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
            print(f"    [{scale:.0e}+bias] {it+1:>8,d} | loss={exact:.15f} | impr={improvements}")

    return best_vecs, best_loss, improvements


def save_solution(vecs, score, tag="eigenvalue"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    data = {"vectors": vecs.tolist(), "score": score, "tag": tag}
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  Saved {tag} (score={score:.15f})")


def main():
    n_iters = int(os.environ.get("N_ITERS", "10000000"))

    print("=" * 70)
    print("EIGENVALUE-GUIDED PERTURBATION")
    print("=" * 70)

    vecs = load_best()
    initial = overlap_loss(vecs)
    print(f"Start: {initial:.15f}")

    # Step 1: Eigenvalue analysis
    print("\n=== Eigenvalue Analysis ===")
    eigvals, eigvecs, thin_eigvec = eigenvalue_analysis(vecs)

    # Step 2: Biased perturbation toward thin direction
    print("\n=== Eigenvalue-guided perturbation ===")
    best_vecs, best_score = vecs.copy(), initial

    for scale in [1e-6, 1e-8, 1e-10, 1e-12]:
        iters = n_iters // 4
        print(f"\n  Scale {scale:.0e} + thin-direction bias:")
        v, l, n = eigenvalue_guided_perturbation(best_vecs.copy(), thin_eigvec, scale, iters, seed=42)
        exact = overlap_loss(v)
        print(f"  Result: {exact:.15f} (delta={best_score - exact:.2e})")
        if exact < best_score:
            best_score = exact
            best_vecs = v.copy()
            save_solution(best_vecs, best_score)

    # Step 3: Compare with unbiased perturbation at same scales
    print("\n=== Control: unbiased perturbation (same budget) ===")
    from scripts.kissing_number.optimize_harden import run_perturbation
    ctrl_vecs, ctrl_score = vecs.copy(), initial
    for scale in [1e-12, 1e-13]:
        iters = n_iters // 2
        v, l, n = run_perturbation(ctrl_vecs.copy(), scale, iters, seed=99)
        exact = overlap_loss(v)
        print(f"  [{scale:.0e}] {exact:.15f} (delta={ctrl_score - exact:.2e})")
        if exact < ctrl_score:
            ctrl_score = exact
            ctrl_vecs = v.copy()

    print(f"\n{'='*70}")
    print(f"Eigenvalue-guided: {best_score:.15f} (delta={initial - best_score:.2e})")
    print(f"Control (unbiased): {ctrl_score:.15f} (delta={initial - ctrl_score:.2e})")
    print(f"Winner: {'EIGENVALUE' if best_score < ctrl_score else 'CONTROL'}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
