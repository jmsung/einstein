"""Diagnostic: random restarts to determine landscape structure.

Perturb SOTA at large scale (1e-2), re-optimize, check if all converge
to the same basin. If yes = single funnel (frozen). If no = multi-modal (hope).

Usage:
    PYTHONUNBUFFERED=1 uv run python scripts/kissing_number/diagnostic_restarts.py
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
            return vecs / norms
    raise FileNotFoundError("No solution found")


def overlap_loss_fast(unit_vecs):
    gram = unit_vecs @ unit_vecs.T
    n = len(unit_vecs)
    i, j = np.triu_indices(n, k=1)
    cos_vals = np.clip(gram[i, j], -1.0, 1.0)
    dists = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos_vals))
    return float(np.sum(np.maximum(0.0, 2.0 - dists)))


def overlap_loss_exact(unit_vecs):
    centers = 2.0 * unit_vecs
    diff = centers[:, None, :] - centers[None, :, :]
    dists = np.sqrt(np.sum(diff**2, axis=-1))
    n = len(unit_vecs)
    i, j = np.triu_indices(n, k=1)
    return float(np.sum(np.maximum(0.0, 2.0 - dists[i, j])))


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


def targeted_perturbation(vecs, scale, n_iters, seed):
    """Targeted micro-perturbation with contribution-weighted sampling."""
    rng = np.random.default_rng(seed)
    best_vecs = vecs.copy()
    current_loss = overlap_loss_fast(vecs)
    best_loss = current_loss
    improvements = 0
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

    return best_vecs, best_loss, improvements


def perturb_solution(vecs, scale, rng):
    """Apply large-scale perturbation to entire solution."""
    perturbed = vecs + rng.standard_normal(vecs.shape) * scale
    norms = np.linalg.norm(perturbed, axis=1, keepdims=True)
    return perturbed / norms


def optimize_from_perturbed(vecs, seed):
    """Multi-scale optimization pipeline from a perturbed starting point."""
    best_vecs = vecs.copy()
    best_loss = overlap_loss_fast(vecs)

    # Phase 1: Coarse optimization at 1e-6 (find nearest basin quickly)
    v, l, n = targeted_perturbation(best_vecs.copy(), 1e-6, 500_000, seed)
    if l < best_loss:
        best_vecs, best_loss = v, l

    # Phase 2: Medium scale at 1e-8
    v, l, n = targeted_perturbation(best_vecs.copy(), 1e-8, 500_000, seed + 1)
    if l < best_loss:
        best_vecs, best_loss = v, l

    # Phase 3: Fine scale at 1e-10
    v, l, n = targeted_perturbation(best_vecs.copy(), 1e-10, 1_000_000, seed + 2)
    if l < best_loss:
        best_vecs, best_loss = v, l

    # Phase 4: Ultra-fine at 1e-12
    v, l, n = targeted_perturbation(best_vecs.copy(), 1e-12, 2_000_000, seed + 3)
    if l < best_loss:
        best_vecs, best_loss = v, l

    return best_vecs, best_loss


def main():
    print("=" * 70)
    print("DIAGNOSTIC: Random restarts to determine landscape structure")
    print("=" * 70)

    sota = load_best()
    sota_score = overlap_loss_exact(sota)
    print(f"SOTA score: {sota_score:.15f}")

    # Test perturbation scales: 1e-3, 1e-2, 1e-1
    perturbation_scales = [1e-3, 1e-2, 1e-1]
    n_restarts_per_scale = 3
    rng = np.random.default_rng(42)

    results = []

    for scale in perturbation_scales:
        print(f"\n{'='*70}")
        print(f"Perturbation scale: {scale:.0e}")
        print(f"{'='*70}")

        for trial in range(n_restarts_per_scale):
            seed = int(rng.integers(100000))
            trial_rng = np.random.default_rng(seed)

            # Perturb
            perturbed = perturb_solution(sota, scale, trial_rng)
            initial_loss = overlap_loss_fast(perturbed)
            print(f"\n  Trial {trial+1}/{n_restarts_per_scale} (seed={seed})")
            print(f"  After perturbation: {initial_loss:.10f}")

            # Optimize
            t0 = time.time()
            final_vecs, final_loss = optimize_from_perturbed(perturbed, seed)
            elapsed = time.time() - t0
            exact = overlap_loss_exact(final_vecs)

            # Compare to SOTA: compute angular distance
            # Frobenius distance of Gram matrices as basin signature
            gram_sota = sota @ sota.T
            gram_final = final_vecs @ final_vecs.T
            gram_dist = np.linalg.norm(gram_sota - gram_final, "fro")

            print(f"  Converged: {exact:.15f} ({elapsed:.0f}s)")
            print(f"  vs SOTA:   {sota_score:.15f}")
            print(f"  Delta:     {exact - sota_score:.2e}")
            print(f"  Gram dist: {gram_dist:.6f}")

            results.append({
                "scale": scale,
                "trial": trial,
                "seed": seed,
                "initial": initial_loss,
                "final": exact,
                "delta_vs_sota": exact - sota_score,
                "gram_dist": gram_dist,
                "time": elapsed,
            })

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    print(f"SOTA: {sota_score:.15f}")
    print()
    print(f"{'Scale':>8} {'Trial':>5} {'Final Score':>18} {'Delta vs SOTA':>14} {'Gram Dist':>10} {'Same Basin?':>12}")
    print("-" * 75)
    for r in results:
        same_basin = "YES" if abs(r["delta_vs_sota"]) < 1e-6 else "NO (different!)"
        print(
            f"{r['scale']:>8.0e} {r['trial']+1:>5} {r['final']:>18.15f} "
            f"{r['delta_vs_sota']:>14.2e} {r['gram_dist']:>10.4f} {same_basin:>12}"
        )

    # Verdict
    all_same = all(abs(r["delta_vs_sota"]) < 1e-6 for r in results)
    any_better = any(r["delta_vs_sota"] < -1e-6 for r in results)
    print()
    if all_same:
        print("VERDICT: All restarts converge to the SAME basin. Landscape is likely SINGLE-FUNNELED.")
        print("         Micro-perturbation refinement is the only viable approach.")
    elif any_better:
        best = min(results, key=lambda r: r["final"])
        print(f"VERDICT: Found a BETTER basin! Score {best['final']:.15f}")
        print(f"         Improvement: {sota_score - best['final']:.2e}")
        print("         Basin hopping is VIABLE — pursue aggressively!")
    else:
        worse_basins = [r for r in results if r["delta_vs_sota"] > 1e-6]
        print(f"VERDICT: Found {len(worse_basins)} DIFFERENT but WORSE basins.")
        print("         Landscape is multi-modal. Better basins may exist — more restarts needed.")


if __name__ == "__main__":
    main()
