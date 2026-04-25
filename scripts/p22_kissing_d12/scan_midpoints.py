"""Direct scan: evaluate filler score at midpoints of 60°-neighbor pairs.

For each pair (v_i, v_j) in CHRONOS's 840 with <v_i, v_j> = 0.5 (60° contact),
compute m_{ij} = (v_i + v_j)/||v_i + v_j|| = (v_i + v_j)/sqrt(3). Score the
841-vector config with m_{ij} as the 841st.

Idea: pair (m, v_i) and (m, v_j) contribute γ = sqrt(3)/2 ≈ 0.866 each,
penalty ≈ 0.965 per pair → 1.93 total. If no other core vector has γ > 0.5
with m, the total score beats CHRONOS's 2.0.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"


def load_core() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    v = np.array(data["vectors"], dtype=np.float64)
    seen = {}
    keep = []
    for i, row in enumerate(v):
        key = tuple(row.tolist())
        if key not in seen:
            seen[key] = i
            keep.append(i)
    return v[keep] / np.linalg.norm(v[keep], axis=1, keepdims=True)


def penalty_from_gamma(gamma: np.ndarray) -> np.ndarray:
    """Return hinge penalty for each inner product γ (0 if γ ≤ 0.5)."""
    g = np.clip(gamma, -1.0, 1.0)
    dist = 2.0 * np.sqrt(2.0 * (1.0 - g))
    return np.maximum(0.0, 2.0 - dist)


def main():
    core = load_core()
    n = len(core)
    print(f"Core: {core.shape}", flush=True)

    # Gram matrix
    G = core @ core.T
    # 60°-edges: pairs (i, j) with G[i,j] = 0.5
    iu, ju = np.triu_indices(n, k=1)
    g_vec = G[iu, ju]
    edge_mask = np.abs(g_vec - 0.5) < 1e-10
    n_edges = edge_mask.sum()
    print(f"60°-edges total: {n_edges}", flush=True)

    # Evaluate score at each midpoint
    # For edge (i,j), m = (v_i + v_j) / sqrt(3)
    # γ_k(m) = <m, v_k> = (G[i,k] + G[j,k]) / sqrt(3)
    # Score(m) = sum_k penalty(γ_k(m))
    # But penalty at pair (m, v_i) and (m, v_j) use γ = sqrt(3)/2 specifically.
    # The all-k formula handles both (and any v_k with γ_k > 0.5 contributes)
    # - except we should NOT double-count self (m is not v_k for any k by construction)

    sqrt3 = np.sqrt(3.0)

    edges_i = iu[edge_mask]
    edges_j = ju[edge_mask]

    t0 = time.time()
    print(f"Evaluating {n_edges} midpoints in one shot...", flush=True)

    # γ_k for each midpoint = (G[edges_i, k] + G[edges_j, k]) / sqrt(3) for k=0..n-1
    # Shape: (n_edges, n)
    GAMMA = (G[edges_i, :] + G[edges_j, :]) / sqrt3  # (n_edges, n)
    # Note: <m, v_i> = (G[i,i] + G[j,i])/sqrt(3) = (1 + 0.5)/sqrt(3) = sqrt(3)/2 ✓
    # And <m, v_j> = (G[i,j] + G[j,j])/sqrt(3) = (0.5 + 1)/sqrt(3) = sqrt(3)/2 ✓

    # Compute penalty per (edge, k) and sum over k
    g_clip = np.clip(GAMMA, -1.0, 1.0)
    dist = 2.0 * np.sqrt(2.0 * (1.0 - g_clip))
    pen = np.maximum(0.0, 2.0 - dist)
    scores = pen.sum(axis=1)

    # Rank edges by score
    order = np.argsort(scores)
    print(f"\n=== Midpoint scores (best = lowest) ===", flush=True)
    print(f"min:  {scores.min():.10f}")
    print(f"10%:  {np.percentile(scores, 10):.10f}")
    print(f"50%:  {np.percentile(scores, 50):.10f}")
    print(f"90%:  {np.percentile(scores, 90):.10f}")
    print(f"max:  {scores.max():.10f}")
    below_2 = (scores < 2.0 - 1e-12).sum()
    print(f"Below 2.0: {below_2} / {len(scores)}", flush=True)

    if below_2 > 0:
        print(f"\n*** {below_2} MIDPOINTS SCORE BELOW 2.0! ***", flush=True)

    print(f"\nTop 20 lowest:", flush=True)
    for k in order[:20]:
        i, j = edges_i[k], edges_j[k]
        # Count active pairs
        n_active = (GAMMA[k] > 0.5 + 1e-10).sum()
        print(f"  edge ({i:3d}, {j:3d})  score={scores[k]:.15f}  n_active={n_active}", flush=True)

    # Save the best midpoint as a candidate filler
    best_k = order[0]
    i_best, j_best = edges_i[best_k], edges_j[best_k]
    m_best = (core[i_best] + core[j_best]) / sqrt3
    print(f"\nBest midpoint: edge ({i_best}, {j_best})  |m|={np.linalg.norm(m_best):.12f}")
    print(f"m = {m_best}")

    vectors_out = np.vstack([core, m_best[None, :]])

    out = {
        "core_source": str(CHRONOS_PATH),
        "best_score": float(scores[best_k]),
        "edge": [int(i_best), int(j_best)],
        "vectors": vectors_out.tolist(),
        "scores_top20": [(int(edges_i[k]), int(edges_j[k]), float(scores[k])) for k in order[:20]],
    }
    json.dump(out, open(RESULTS_DIR / "scan_midpoints.json", "w"))
    print(f"Saved → {RESULTS_DIR / 'scan_midpoints.json'}")
    print(f"\nElapsed: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
